"""Cut a Midjourney expression sheet into four transparent sprites.

The sheet is one row of four equal panels of the same character on a flat
background (any color: green, blue, white...). Each panel is keyed out,
cleaned up, scaled and saved as game/images/sprites/<name>_<expression>.png.

    python3 tools/import_sprite_sheet.py SHEET NAME [ORDER] [--height N]

ORDER says which expression each panel is, left to right, comma separated.
It defaults to the order the prompts ask for: neutral,happy,surprised,blush.
Use "-" to skip a panel, e.g. "happy,-,surprised,blush" to keep the current
neutral sprite. Requires Pillow and numpy.
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


def key_panel(rgb, bg):
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
    labels, sizes = components(alpha > 40)
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
    clear_cols = np.where((alpha > 40).sum(axis=0) <= 3)[0]
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
    pw = w / len(order)
    for i, expr in enumerate(order):
        if expr in ("", "-"):
            continue
        panel = rgb[:, int(round(i * pw)):int(round((i + 1) * pw))]
        img = key_panel(panel, bg)
        if args.height and args.height != img.height:
            s = args.height / img.height
            img = img.resize((round(img.width * s), args.height), Image.LANCZOS)
        path = os.path.join(OUT, "%s_%s.png" % (args.name, expr))
        img.save(path, optimize=True)
        print("wrote", os.path.relpath(path, ROOT), img.size)


if __name__ == "__main__":
    main()
