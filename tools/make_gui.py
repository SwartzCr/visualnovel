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


# ---------------------------------------------------------------- stylized pieces
SSX = 3  # supersampling for the fancy pieces

VIOLET = (155, 107, 255)
NAME_COLORS = {
    "default": "#ff5fb8",
    "juni": "#ff9ccc", "gerald": "#e0a878", "solstice": "#ffd36b",
    "wren": "#c8b8ff", "zyx": "#7affd0",
}


def _hex(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def _hgrad(w, h, stops):
    """Horizontal gradient image through (t, rgb) stops."""
    img = Image.new("RGBA", (w, h))
    px = img.load()
    for x in range(w):
        t = x / max(1, w - 1)
        for (t0, c0), (t1, c1) in zip(stops, stops[1:]):
            if t0 <= t <= t1:
                k = (t - t0) / max(1e-6, t1 - t0)
                c = tuple(int(c0[i] + (c1[i] - c0[i]) * k) for i in range(3))
                break
        for y in range(h):
            px[x, y] = c + (255,)
    return img


def _vgrad(w, h, top, bottom):
    img = Image.new("RGBA", (w, h))
    d = ImageDraw.Draw(img)
    for y in range(h):
        k = y / max(1, h - 1)
        d.line([(0, y), (w, y)], fill=tuple(int(top[i] + (bottom[i] - top[i]) * k) for i in range(4)))
    return img


def _rr_mask(size, box, r, width=None):
    m = Image.new("L", size, 0)
    d = ImageDraw.Draw(m)
    if width:
        d.rounded_rectangle(box, radius=r, outline=255, width=width)
    else:
        d.rounded_rectangle(box, radius=r, fill=255)
    return m


def _paint(base, src, mask, alpha=1.0):
    if alpha < 1:
        mask = mask.point(lambda v: int(v * alpha))
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    layer.paste(src, (0, 0), mask)
    base.alpha_composite(layer)


def _sparkle(d, cx, cy, r, color):
    """Four-pointed star."""
    pts = [(cx, cy - r), (cx + r * 0.22, cy - r * 0.22), (cx + r, cy), (cx + r * 0.22, cy + r * 0.22),
           (cx, cy + r), (cx - r * 0.22, cy + r * 0.22), (cx - r, cy), (cx - r * 0.22, cy - r * 0.22)]
    d.polygon(pts, fill=color)


def _neon_panel(w, h, box, r, fill_top, fill_bottom, stops, border=3, glow=10, glow_alpha=0.75,
                sheen=True, inner_line=True):
    """A rounded panel with gradient fill, gradient neon border and outer glow (at SSX scale)."""
    S = SSX
    W_, H_ = w * S, h * S
    b = [v * S for v in box]
    img = Image.new("RGBA", (W_, H_), (0, 0, 0, 0))
    grad = _hgrad(W_, H_, stops)

    # outer glow
    gm = _rr_mask((W_, H_), b, r * S, width=border * S * 3).filter(ImageFilter.GaussianBlur(glow * S))
    _paint(img, grad, gm, glow_alpha)

    # body
    body = _rr_mask((W_, H_), b, r * S)
    _paint(img, _vgrad(W_, H_, fill_top, fill_bottom), body)
    if sheen:
        sh = _vgrad(W_, H_, (255, 255, 255, 34), (255, 255, 255, 0))
        cut = Image.new("L", (W_, H_), 0)
        ImageDraw.Draw(cut).rectangle([b[0], b[1], b[2], b[1] + (b[3] - b[1]) * 0.45], fill=255)
        _paint(img, sh, _min(body, cut))
    if inner_line:
        inset = 6 * S
        il = _rr_mask((W_, H_), [b[0] + inset, b[1] + inset, b[2] - inset, b[3] - inset],
                      max(1, (r - 5) * S), width=max(1, S))
        _paint(img, Image.new("RGBA", (W_, H_), (255, 255, 255, 255)), il, 0.10)

    # crisp gradient border
    _paint(img, grad, _rr_mask((W_, H_), b, r * S, width=border * S))
    return img


def _min(a, b):
    from PIL import ImageChops
    return ImageChops.darker(a, b)


def _down(img, w, h):
    return img.resize((w, h), Image.LANCZOS)


def fancy_textbox():
    # The panel floats above a 34px strip at the bottom reserved for the quick menu.
    w, h = W, 226
    box = (36, 32, 1244, 190)
    stops = [(0.0, ACCENT), (0.5, VIOLET), (1.0, CYAN)]
    img = _neon_panel(w, h, box, 26, (30, 14, 54, 244), (14, 7, 28, 250), stops, border=3, glow=9)
    d = ImageDraw.Draw(img)
    S = SSX
    # sparkles: top-right cluster and bottom-left
    for (x, y, r, c) in [(1196, 58, 9, CYAN), (1216, 80, 5, ACCENT), (1178, 82, 4, (255, 255, 255)),
                         (64, 168, 6, ACCENT), (82, 158, 3.5, CYAN)]:
        _sparkle(d, x * S, y * S, r * S, c + (235,))
    # a row of tiny dots along the bottom inner edge, fading toward the middle
    for i in range(60):
        x = 120 + i * 17
        k = abs(i - 30) / 30
        if 0.25 < k:
            d.ellipse([(x - 1.4) * S, 178 * S, (x + 1.4) * S, 180.8 * S], fill=(255, 255, 255, int(70 * k)))
    _down(img, w, h).save(path("textbox"))

    # phone version: full width, taller
    ph = _neon_panel(W, 250, (14, 24, 1266, 246), 22, (30, 14, 54, 245), (14, 7, 28, 250), stops, border=3, glow=8)
    _down(ph, W, 250).save(path("phone/textbox"))


def fancy_nameboxes():
    for who, colr in NAME_COLORS.items():
        c = _hex(colr)
        w, h = 300, 50
        stops = [(0.0, c), (1.0, tuple(int(v * 0.75 + 255 * 0.25) for v in c))]
        img = _neon_panel(w, h, (6, 6, 294, 44), 19, (26, 12, 46, 245), (18, 8, 34, 250), stops,
                          border=2, glow=5, glow_alpha=0.9, inner_line=False)
        d = ImageDraw.Draw(img)
        S = SSX
        # little diamond on the left
        cx, cy, rr = 24, 25, 6
        d.polygon([(cx * S, (cy - rr) * S), ((cx + rr) * S, cy * S), (cx * S, (cy + rr) * S), ((cx - rr) * S, cy * S)],
                  fill=c + (255,))
        name = "namebox" if who == "default" else "namebox_" + who
        _down(img, w, h).save(path(name))


def fancy_choices():
    w, h = 820, 52
    box = (8, 6, 812, 46)
    idle = _neon_panel(w, h, box, 20, (34, 16, 60, 228), (20, 9, 38, 236),
                       [(0, CYAN), (0.5, VIOLET), (1, CYAN)], border=2, glow=5, glow_alpha=0.45, inner_line=False)
    hover = _neon_panel(w, h, box, 20, ACCENT + (240,), VIOLET + (240,),
                        [(0, (255, 210, 235)), (1, (210, 240, 255))], border=2, glow=9, glow_alpha=0.95, inner_line=False)
    # hover: horizontal pink -> violet fill instead of vertical
    S = SSX
    body = _rr_mask((w * S, h * S), [v * S for v in box], 20 * S)
    fill = _hgrad(w * S, h * S, [(0, (255, 95, 184)), (1, (130, 90, 240))])
    _paint(hover, fill, body, 0.92)
    _paint(hover, _hgrad(w * S, h * S, [(0, (255, 220, 240)), (1, (200, 240, 255))]),
           _rr_mask((w * S, h * S), [v * S for v in box], 20 * S, width=2 * S))
    insensitive = _neon_panel(w, h, box, 20, (26, 14, 40, 170), (18, 9, 30, 170),
                              [(0, MUTED), (1, MUTED)], border=2, glow=2, glow_alpha=0.2, inner_line=False)
    for img in (idle, hover):
        d = ImageDraw.Draw(img)
        for x in (30, w - 30):
            _sparkle(d, x * S, 26 * S, 7 * S, (255, 255, 255, 220))
    for state, img in (("idle", idle), ("hover", hover), ("insensitive", insensitive)):
        out = _down(img, w, h)
        for prefix in ("", "phone/"):
            out.save(path(prefix + "button/choice_%s_background" % state))
    _down(idle, w, h).save(path("button/choice_background"))


def fancy_pills():
    """Notify, skip indicator and the time tag."""
    for name, w, h in (("notify", 420, 46), ("skip", 240, 46), ("tag", 300, 40)):
        img = _neon_panel(w, h, (5, 5, w - 5, h - 5), (h - 10) // 2, (26, 12, 46, 238), (18, 8, 34, 244),
                          [(0, ACCENT), (1, VIOLET)], border=2, glow=4, glow_alpha=0.7, inner_line=False)
        _down(img, w, h).save(path(name))


if __name__ == "__main__":
    textbox()
    nvl()
    choice_buttons()
    overlays()
    frames()
    misc_buttons()
    bars()
    icon()
    # Stylized versions override the plain ones above.
    fancy_textbox()
    fancy_nameboxes()
    fancy_choices()
    fancy_pills()
    print("GUI images written to", os.path.abspath(OUT))
