"""Cut a Midjourney expression sheet into four transparent sprites.

The sheet is one row of four equal panels of the same character on a flat
background (any color: green, blue, white...). Each panel is keyed out,
cleaned up, scaled and saved as game/images/sprites/<name>_<expression>.webp.

    python3 tools/import_sprite_sheet.py SHEET NAME [ORDER] [--height N]

ORDER says which expression each panel is, left to right, comma separated.
It defaults to the order the prompts ask for: neutral,happy,surprised,blush.
Use "-" to skip a panel, e.g. "happy,-,surprised,blush" to keep the current
neutral sprite. Requires Pillow, numpy and scikit-image.

Figures may overlap their neighbors' panels (gills, hair, hands): each pixel
goes to the figure it's connected to, so nothing gets cut off.
"""

import argparse
import os
from collections import deque

import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "game", "images", "sprites")


def strip_bars(rgb):
    """Remove black letterbox bars above and below the art."""
    dark = rgb.max(axis=2).mean(axis=1) < 12
    rows = np.where(~dark)[0]
    return rgb[rows[0]:rows[-1] + 1]


def flood_background(dist, near):
    """Pixels within `near` of the background color that touch the border."""
    h, w = dist.shape
    cand = dist < near
    seen = np.zeros_like(cand)
    q = deque()
    for x in range(w):
        for y in (0, h - 1):
            if cand[y, x] and not seen[y, x]:
                seen[y, x] = True
                q.append((y, x))
    for y in range(h):
        for x in (0, w - 1):
            if cand[y, x] and not seen[y, x]:
                seen[y, x] = True
                q.append((y, x))
    while q:
        y, x = q.popleft()
        for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
            if 0 <= ny < h and 0 <= nx < w and cand[ny, nx] and not seen[ny, nx]:
                seen[ny, nx] = True
                q.append((ny, nx))
    return seen


def components(mask):
    """Label 4-connected components of a boolean mask."""
    h, w = mask.shape
    labels = np.zeros((h, w), dtype=np.int32)
    sizes = [0]
    n = 0
    for sy, sx in zip(*np.nonzero(mask)):
        if labels[sy, sx]:
            continue
        n += 1
        size = 0
        q = deque([(sy, sx)])
        labels[sy, sx] = n
        while q:
            y, x = q.popleft()
            size += 1
            for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
                if 0 <= ny < h and 0 <= nx < w and mask[ny, nx] and not labels[ny, nx]:
                    labels[ny, nx] = n
                    q.append((ny, nx))
        sizes.append(size)
    return labels, sizes


def key_panel(rgb, bg, single=True):
    rgbf = rgb.astype(np.float32)
    dist = np.sqrt(((rgbf - bg) ** 2).sum(axis=2))
    # Soft edge: fully clear below `clear`, fully solid above `solid`.
    clear, solid = 28.0, 80.0
    bgmask = flood_background(dist, solid)
    alpha = np.full(dist.shape, 255.0, dtype=np.float32)
    ramp = np.clip((dist - clear) / (solid - clear), 0, 1) * 255
    alpha[bgmask] = ramp[bgmask]

    # Background showing through enclosed gaps (between strands of hair,
    # under an arm) isn't reached by the flood fill. Clear any enclosed patch
    # that is very close to the background color and more than a few pixels.
    # Skipped on white or near-white backgrounds, where it would also eat
    # highlights and pale hair.
    if bg.min() < 200:
        pocket = (dist < 45) & ~bgmask
        plabels, psizes = components(pocket)
        big = np.array([s > 25 for s in psizes])
        big[0] = False
        alpha[big[plabels]] = ramp[big[plabels]]

    # Drop bits of the neighboring panels: keep the main figure plus any
    # sizable piece that doesn't touch the left or right edge.
    labels, sizes = components(alpha > 40) if single else (None, [0])
    if len(sizes) > 1:
        main = int(np.argmax(sizes))
        edge = set(labels[:, 0].tolist()) | set(labels[:, -1].tolist())
        keep = np.zeros(len(sizes), dtype=bool)
        keep[main] = True
        for i, s in enumerate(sizes):
            if i and i != main and i not in edge and s > 0.002 * sizes[main]:
                keep[i] = True
        alpha[~keep[labels] & (alpha > 0)] = 0
        # Faint fringe pixels next to removed pieces.
        alpha[(labels == 0) & (alpha <= 40)] = np.where(
            bgmask[(labels == 0) & (alpha <= 40)], 0, alpha[(labels == 0) & (alpha <= 40)])

    # A neighboring panel's edge can stay attached at the bottom. If a fully
    # clear column sits near either side, clear everything beyond it.
    w = alpha.shape[1]
    clear_cols = np.where((alpha > 40).sum(axis=0) <= 3)[0] if single else []
    for c in clear_cols:
        if c < 0.15 * w:
            alpha[:, :c] = 0
        elif c > 0.85 * w:
            alpha[:, c:] = 0
            break

    # Despill: pull the background tint out of semi-transparent edge pixels.
    edge = (alpha > 0) & (alpha < 255)
    a = (alpha[edge] / 255.0)[:, None]
    rgbf[edge] = np.clip((rgbf[edge] - bg * (1 - a)) / np.maximum(a, 0.25), 0, 255)

    out = np.dstack([rgbf, alpha]).astype(np.uint8)
    return Image.fromarray(out, "RGBA")


def touch_rows(mine, others):
    """How many rows this figure shares a border with another figure."""
    from skimage.morphology import dilation, disk
    contact = dilation(mine, disk(2)) & others
    return int(contact.any(axis=1).sum())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("sheet")
    ap.add_argument("name")
    ap.add_argument("order", nargs="?", default="neutral,happy,surprised,blush")
    ap.add_argument("--height", type=int, default=0,
                    help="output height in px (default: the sheet's own height)")
    args = ap.parse_args()

    rgb = strip_bars(np.array(Image.open(args.sheet).convert("RGB")))
    h, w, _ = rgb.shape
    corners = np.array([rgb[2, 2], rgb[2, -3], rgb[h // 3, 2], rgb[h // 3, -3]], dtype=np.float32)
    bg = np.median(corners, axis=0)

    order = [o.strip() for o in args.order.split(",")]
    n = len(order)
    pw = w / n

    # Key out the whole sheet at once, then give every pixel to the figure it
    # is connected to. That keeps hair, gills and hands that reach into the
    # next panel with their own figure instead of cutting them off.
    sheet = np.array(key_panel(rgb, bg, single=False))
    fg = sheet[:, :, 3] > 40
    markers = np.zeros((h, w), dtype=np.int32)
    for i in range(n):
        x0, x1 = int((i + 0.35) * pw), int((i + 0.65) * pw)
        markers[:, x0:x1][fg[:, x0:x1]] = i + 1
    # Flood outward from the middle of each panel. Dark outline pixels are
    # "high ground", so where two figures touch, the boundary falls on the
    # outlines between them rather than cutting through one of them.
    from skimage.segmentation import watershed
    lum = rgb.astype(np.float32).mean(axis=2)
    elevation = np.clip(255 - lum, 0, 255)
    owner = watershed(elevation, markers, mask=sheet[:, :, 3] > 0)

    # Every expression gets the same frame: the panel plus a margin on each
    # side, so the character doesn't shift sideways when the expression changes.
    margin = int(pw * 0.2)
    for i, expr in enumerate(order):
        if expr in ("", "-"):
            continue
        rgba = sheet.copy()
        mine = owner == i + 1
        # Trim thin strands of a neighbor's outline that tag along.
        from skimage.morphology import opening, dilation, disk
        from skimage.measure import label
        core = opening(mine, disk(3))
        lab = label(core)
        if lab.max():
            body = lab == np.bincount(lab.ravel())[1:].argmax() + 1
            # Fine detail (outlines, gill fringe, hair tips) within a few
            # pixels of the body stays; long thin strands don't.
            mine &= dilation(body, disk(6))
        # Where figures merge into each other (shoulders, fur), the outlines
        # can't say whose pixels are whose. Below the heads, keep only this
        # panel's strip and fade the cut edges so they don't look sliced.
        px0, px1 = int(round(i * pw)), int(round((i + 1) * pw))
        neighbours = (owner > 0) & (owner != i + 1)
        rows = np.where(neighbours[:, max(px0 - margin, 0):min(px1 + margin, w)].any(axis=1)
                        & mine[:, max(px0 - margin, 0):min(px1 + margin, w)].any(axis=1))[0]
        if len(rows) and touch_rows(mine, neighbours) > 0.15 * h:
            top = int(h * 0.45)
            xs = np.arange(w)
            fade = int(pw * 0.06)
            weight = np.clip(np.minimum(xs - px0, px1 - 1 - xs) / max(fade, 1), 0, 1)
            band = np.zeros((h, w), dtype=np.float32) + 1.0
            band[top:] = weight[None, :]
            ramp = np.clip((np.arange(h) - top) / (h * 0.08), 0, 1)[:, None]
            band = 1.0 - ramp * (1.0 - band)
            rgba[:, :, 3] = (rgba[:, :, 3] * band).astype(np.uint8)
        rgba[~mine, 3] = 0
        x0 = int(round(i * pw)) - margin
        x1 = int(round((i + 1) * pw)) + margin
        frame = np.zeros((h, x1 - x0, 4), dtype=np.uint8)
        sx0, sx1 = max(x0, 0), min(x1, w)
        frame[:, sx0 - x0:sx1 - x0] = rgba[:, sx0:sx1]
        img = Image.fromarray(frame, "RGBA")
        if args.height and args.height != img.height:
            s = args.height / img.height
            img = img.resize((round(img.width * s), args.height), Image.LANCZOS)
        path = os.path.join(OUT, "%s_%s.webp" % (args.name, expr))
        img.save(path, "WEBP", quality=90, method=6, alpha_quality=100)
        print("wrote", os.path.relpath(path, ROOT), img.size)

if __name__ == "__main__":
    main()
