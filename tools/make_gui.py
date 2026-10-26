"""Generate the GUI images that the Ren'Py launcher would normally create,
in the game's neon-on-midnight palette. Run from the repo root:

    python3 tools/make_gui.py

(Inside Ren'Py you can also regenerate the plain versions with
`renpy.sh . gui_images`, but that would overwrite this styling.)
"""
import os
from PIL import Image, ImageDraw, ImageFilter

OUT = os.path.join(os.path.dirname(__file__), "..", "game", "gui")
W, H = 1280, 720

BORING = (22, 12, 40)        # deep midnight purple
ACCENT = (255, 95, 184)      # neon pink
CYAN = (90, 230, 255)
MUTED = (74, 37, 82)
HOVER_MUTED = (110, 51, 120)
HOVER = (255, 191, 227)


def path(name):
    fn = os.path.join(OUT, name + ".png")
    os.makedirs(os.path.dirname(fn), exist_ok=True)
    return fn


def save(img, name):
    img.save(path(name))


def blank(w, h, color=(0, 0, 0, 0)):
    return Image.new("RGBA", (w, h), color)


def rgba(c, a):
    return (c[0], c[1], c[2], int(255 * a))


def ramp(points, size):
    """Piecewise-linear opacity ramp like the launcher's templates."""
    out = []
    for i in range(size):
        for (x0, v0), (x1, v1) in zip(points, points[1:]):
            if x0 <= i <= x1:
                t = 0 if x1 == x0 else (i - x0) / (x1 - x0)
                out.append(v0 + (v1 - v0) * t)
                break
        else:
            out.append(points[-1][1])
    return out


def ramp_image(name, xpts, ypts, color, alpha):
    w, h = xpts[-1][0], ypts[-1][0]
    xs, ys = ramp(xpts, w), ramp(ypts, h)
    img = blank(w, h)
    px = img.load()
    for x in range(w):
        for y in range(h):
            px[x, y] = color + (int(255 * alpha * xs[x] * ys[y]),)
    save(img, name)
    return img


def neon_line(img, y, color, width=2, glow=6):
    """Horizontal neon rule with a soft glow."""
    layer = blank(*img.size)
    d = ImageDraw.Draw(layer)
    d.rectangle([0, y - glow, img.size[0], y + glow], fill=rgba(color, 0.35))
    layer = layer.filter(ImageFilter.GaussianBlur(glow / 1.5))
    img.alpha_composite(layer)
    d = ImageDraw.Draw(img)
    d.rectangle([0, y, img.size[0], y + width - 1], fill=rgba(color, 0.95))


def textbox():
    w, h = W, 185
    xin = (w - 744) // 2
    img = ramp_image("textbox", [(0, 0.55), (xin, 1.0), (w - xin, 1.0), (w, 0.55)],
                     [(0, 1.0), (h, 1.0)], BORING, 0.86)
    neon_line(img, 3, ACCENT)
    save(img, "textbox")

    img = blank(w, 240, rgba(BORING, 0.86))
    neon_line(img, 3, ACCENT)
    save(img, "phone/textbox")

    # Name box: a little neon tag.
    nb = blank(300, 36)
    d = ImageDraw.Draw(nb)
    d.rounded_rectangle([2, 2, 297, 33], radius=10, fill=rgba(BORING, 0.92), outline=rgba(ACCENT, 1), width=2)
    save(nb, "namebox")


def nvl():
    w = W
    xin = (w - 800) // 2
    ramp_image("nvl", [(0, 0.0), (xin, 1.0), (w - xin, 1.0), (w, 0.0)], [(0, 1.0), (H, 1.0)], BORING, 0.85)
    save(blank(w, H, rgba(BORING, 0.85)), "phone/nvl")


def choice_buttons():
    w, h = 790, 40
    for state, fill, line in [("idle", rgba(BORING, 0.85), rgba(CYAN, 0.55)),
                              ("hover", rgba((70, 20, 70), 0.95), rgba(ACCENT, 1.0)),
                              ("insensitive", rgba(BORING, 0.6), rgba(MUTED, 0.8))]:
        img = blank(w, h)
        d = ImageDraw.Draw(img)
        d.rounded_rectangle([1, 1, w - 2, h - 2], radius=18, fill=fill, outline=line, width=2)
        for prefix in ("", "phone/"):
            save(img, prefix + "button/choice_%s_background" % state)
    # Un-prefixed fallback.
    save(Image.open(path("button/choice_idle_background")), "button/choice_background")


def overlays():
    width, line = 280, 3
    mm = blank(W, H)
    d = ImageDraw.Draw(mm)
    d.rectangle([0, 0, width, H], fill=rgba(BORING, 0.78))
    d.rectangle([width - line, 0, width, H], fill=rgba(ACCENT, 1))
    save(mm, "overlay/main_menu")

    mm = blank(W, H)
    d = ImageDraw.Draw(mm)
    d.rectangle([0, 0, 340, H], fill=rgba(BORING, 0.78))
    d.rectangle([340 - line, 0, 340, H], fill=rgba(ACCENT, 1))
    save(mm, "phone/overlay/main_menu")

    for prefix, wd in (("", width), ("phone/", 340)):
        gm = blank(W, H, rgba(BORING, 0.88))
        d = ImageDraw.Draw(gm)
        d.rectangle([wd - line, 120, wd, 690], fill=rgba(ACCENT, 1))
        save(gm, prefix + "overlay/game_menu")

    save(blank(W, H, rgba((5, 0, 15), 0.6)), "overlay/confirm")


def frames():
    fr = blank(600, 250)
    d = ImageDraw.Draw(fr)
    d.rectangle([0, 0, 599, 249], fill=rgba(ACCENT, 1))
    d.rectangle([3, 3, 596, 246], fill=rgba(BORING, 0.97))
    save(fr, "frame")
    save(fr, "confirm_frame")


def misc_buttons():
    save(blank(100, 30), "button/quick_idle_background")
    save(blank(100, 30), "button/quick_hover_background")
    save(blank(100, 30), "button/quick_background")

    ramp_image("skip", [(0, 1.0), (190, 1.0), (240, 0.0)], [(0, 1.0), (43, 1.0)], BORING, 0.85)
    ramp_image("notify", [(0, 1.0), (872, 1.0), (922, 0.0)], [(0, 1.0), (43, 1.0)], BORING, 0.9)

    bw, bh = 300, 33
    for n in ("idle_background", "hover_background", "background"):
        save(blank(bw, bh), "button/" + n)

    cw = 18
    for kind in ("check", "radio"):
        save(blank(cw, bh), "button/%s_foreground" % kind)
        img = blank(cw, bh)
        d = ImageDraw.Draw(img)
        d.rectangle([3, 4, 8, bh - 5], fill=rgba(ACCENT, 1))
        save(img, "button/%s_selected_foreground" % kind)
        save(blank(cw, 43), "phone/button/%s_foreground" % kind)
        save(img.resize((cw, 43)), "phone/button/%s_selected_foreground" % kind)

    sw, sh = 276, 206
    for state, color in (("idle", MUTED), ("hover", HOVER_MUTED)):
        img = blank(sw, sh)
        d = ImageDraw.Draw(img)
        tx = (sw - 256) // 2
        d.rectangle([tx, 10, tx + 255, 10 + 143], fill=rgba(color, 1))
        save(img, "button/slot_%s_background" % state)
    save(Image.open(path("button/slot_idle_background")), "button/slot_background")


def bars():
    long_size, size = 350, 25
    fills = {"left": HOVER, "right": MUTED, "bottom": HOVER, "top": MUTED}
    for n, c in fills.items():
        wh = (long_size, size) if n in ("left", "right") else (size, long_size)
        for prefix in ("", "phone/"):
            save(blank(*wh, rgba(c, 1)), prefix + "bar/" + n)

    for prefix in ("", "phone/"):
        thumb = 15 if prefix else 10
        for orient in ("horizontal", "vertical"):
            for state, bar_c, thumb_c in (("idle", MUTED, ACCENT), ("hover", HOVER_MUTED, HOVER)):
                if orient == "horizontal":
                    bar_wh, thumb_wh = (long_size, size), (thumb, size)
                else:
                    bar_wh, thumb_wh = (size, long_size), (size, thumb)
                save(blank(*bar_wh, rgba(bar_c, 1)), prefix + "slider/%s_%s_bar" % (orient, state))
                save(blank(*thumb_wh, rgba(thumb_c, 1)), prefix + "slider/%s_%s_thumb" % (orient, state))

        long_s, sb = 700, 12
        for orient in ("horizontal", "vertical"):
            for state, bar_c, thumb_c in (("idle", MUTED, ACCENT), ("hover", HOVER_MUTED, HOVER)):
                wh = (long_s, sb) if orient == "horizontal" else (sb, long_s)
                save(blank(*wh, rgba(bar_c, 1)), prefix + "scrollbar/%s_%s_bar" % (orient, state))
                save(blank(*wh, rgba(thumb_c, 1)), prefix + "scrollbar/%s_%s_thumb" % (orient, state))


def icon():
    src = os.path.join(os.path.dirname(__file__), "template_icon.png")
    ic = Image.open(src).convert("RGBA")
    px = ic.load()
    for y in range(ic.size[1]):
        for x in range(ic.size[0]):
            r, g, b, a = px[x, y]
            px[x, y] = (min(255, r + ACCENT[0] - 23), max(0, min(255, g + ACCENT[1] - 23)),
                        max(0, min(255, b + ACCENT[2] - 23)), a)
    save(ic, "window_icon")


if __name__ == "__main__":
    textbox()
    nvl()
    choice_buttons()
    overlays()
    frames()
    misc_buttons()
    bars()
    icon()
    print("GUI images written to", os.path.abspath(OUT))
