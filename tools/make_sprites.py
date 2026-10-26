"""Paint the character sprites (transparent PNGs, three expressions each).

    python3 tools/make_sprites.py
"""
import math
import os

from artlib import Canvas, col, mix, rng, blob

OUT = os.path.join(os.path.dirname(__file__), "..", "game", "images", "sprites")
os.makedirs(OUT, exist_ok=True)
EXPRS = ("neutral", "happy", "surprised")
INK = "#2a1426"


def shaggy(cx, cy, rx, ry, n=90, amp=0.07, seed=0, start=0, end=2 * math.pi):
    """Fur-edged blob: alternating spikes."""
    R = rng(seed)
    pts = []
    for i in range(n):
        a = start + (end - start) * i / n
        k = 1 + (amp if i % 2 else -amp * 0.4) * R.uniform(0.5, 1.2)
        pts.append((cx + math.cos(a) * rx * k, cy + math.sin(a) * ry * k))
    return pts


def eyes(c, lx, rx, y, expr, size=9, color=INK, lash=False, white=True):
    for x in (lx, rx):
        if expr == "happy":
            c.arc((x - size, y - size * 0.7, x + size, y + size * 0.9), 200, 340, color, max(3, int(size / 3)))
        elif expr == "surprised":
            if white:
                c.ell((x - size * 1.1, y - size * 1.3, x + size * 1.1, y + size * 1.3), fill="#ffffff")
            c.ell((x - size * 0.6, y - size * 0.75, x + size * 0.6, y + size * 0.75), fill=color)
            c.circle(x - size * 0.2, y - size * 0.3, size * 0.22, fill="#ffffff")
        else:
            c.ell((x - size * 0.65, y - size * 0.9, x + size * 0.65, y + size * 0.9), fill=color)
            c.circle(x - size * 0.2, y - size * 0.35, size * 0.25, fill="#ffffff")
        if lash and expr != "happy":
            c.line([(x + size * 0.5, y - size * 0.8), (x + size * 1.0, y - size * 1.2)], color, 2)


def mouth(c, x, y, w, expr, color=INK, inner="#7a2a3a"):
    if expr == "happy":
        c.pieslice((x - w, y - w * 0.5, x + w, y + w * 0.9), 0, 180, inner)
        c.arc((x - w, y - w * 0.5, x + w, y + w * 0.9), 0, 180, color, 3)
        c.rect((x - w * 0.6, y + w * 0.18, x + w * 0.6, y + w * 0.3), fill="#ffffff")
    elif expr == "surprised":
        c.ell((x - w * 0.35, y - w * 0.1, x + w * 0.35, y + w * 0.6), fill=inner, outline=color, width=2)
    else:
        c.arc((x - w * 0.7, y - w * 0.6, x + w * 0.7, y + w * 0.35), 25, 155, color, 3)


def blush(c, lx, rx, y, r=14, color="#ff6f8f", a=110):
    for x in (lx, rx):
        c.ell((x - r, y - r * 0.55, x + r, y + r * 0.55), fill=col(color, a), blur=3)


def brows(c, lx, rx, y, expr, w=14, color=INK, width=4):
    lift = -6 if expr == "surprised" else 0
    for x, s in ((lx, 1), (rx, -1)):
        tilt = 3 if expr == "neutral" else 0
        c.line([(x - w, y + lift + tilt * s * -1), (x + w, y + lift - tilt * s * -1)], color, width)


# ----------------------------------------------------------------- Juni
def juni(expr):
    W, H = 440, 660
    c = Canvas(W, H)
    pink, deep, belly, gill = "#ff9ccc", "#f07aae", "#ffd6e8", "#e0407a"
    skin, hair = "#c98d6b", "#2a1a1a"
    # tail
    c.line([(270, 560), (360, 560), (410, 510), (420, 450)], deep, 46)
    c.line([(270, 560), (360, 560), (410, 510), (420, 450)], pink, 34)
    c.poly([(400, 455), (420, 390), (440, 455)], fill=deep)
    # feet
    c.ell((120, 600, 210, 650), fill=deep)
    c.ell((230, 600, 320, 650), fill=deep)
    # body
    c.poly(blob(220, 470, 140, 170, n=60), fill=pink)
    c.poly(blob(220, 500, 82, 120, n=40), fill=belly)
    c.line([(220, 380), (220, 600)], col("#c45a8a", 160), 2)
    c.rect((214, 380, 226, 396), fill="#d0d0d8", r=3)
    # arms (sleeves)
    c.poly(blob(95, 470, 38, 80, n=30), fill=pink)
    c.poly(blob(345, 470, 38, 80, n=30), fill=pink)
    c.ell((70, 520, 120, 560), fill=deep)
    c.ell((320, 520, 370, 560), fill=deep)
    # gills behind head
    for side in (-1, 1):
        for k, ang in enumerate((-35, -5, 25)):
            a = math.radians(ang)
            x0, y0 = 220 + side * 125, 200 + k * 30
            x1 = x0 + side * math.cos(a) * 95
            y1 = y0 + math.sin(a) * 95
            c.line([(x0, y0), (x1, y1)], gill, 14)
            for t in (0.35, 0.55, 0.75, 0.95):
                px, py = x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
                c.circle(px + side * 4, py - 10, 9, fill=gill)
                c.circle(px - side * 4, py + 10, 9, fill=gill)
    # hood
    c.circle(220, 220, 150, fill=pink)
    c.ell((105, 110, 335, 190), fill=col("#ffffff", 40), blur=6)
    # hood's own little axolotl eyes + smile
    for x in (150, 290):
        c.circle(x, 112, 13, fill=INK)
        c.circle(x - 4, 108, 4, fill="#ffffff")
    c.arc((195, 108, 245, 138), 20, 160, INK, 3)
    # face opening
    c.ell((128, 160, 312, 352), fill=deep)
    c.ell((138, 168, 302, 344), fill=skin)
    # bangs
    c.poly([(140, 230), (150, 182), (190, 168), (250, 168), (292, 186), (300, 232), (272, 205), (246, 220),
            (226, 198), (198, 222), (176, 200)], fill=hair)
    eyes(c, 192, 248, 262, expr, size=10)
    blush(c, 170, 270, 290, a=150 if expr == "happy" else 80)
    mouth(c, 220, 310, 16, expr)
    c.save(os.path.join(OUT, "juni_%s.png" % expr))


# ----------------------------------------------------------------- Gerald
def gerald(expr):
    W, H = 600, 720
    c = Canvas(W, H)
    fur, dark, light = "#6b4a32", "#4a3020", "#8a6444"
    face, skin_dark = "#7a5640", "#2e1e14"
    # legs/feet
    c.poly(shaggy(220, 640, 70, 70, seed=3), fill=dark)
    c.poly(shaggy(380, 640, 70, 70, seed=4), fill=dark)
    c.ell((150, 680, 290, 718), fill=skin_dark)
    c.ell((310, 680, 450, 718), fill=skin_dark)
    # body
    c.poly(shaggy(300, 430, 210, 250, n=140, seed=1, amp=0.05), fill=fur)
    # arms
    c.poly(shaggy(110, 440, 62, 200, n=60, seed=5, amp=0.08), fill=dark)
    c.poly(shaggy(490, 400, 62, 150, n=60, seed=6, amp=0.08), fill=dark)
    c.ell((70, 600, 150, 660), fill=skin_dark)
    # right arm folded to chest holding teacup
    c.poly(shaggy(420, 500, 110, 50, n=50, seed=7, amp=0.08), fill=dark)
    c.ell((330, 470, 390, 525), fill=skin_dark)
    c.rect((340, 446, 384, 482), fill="#ffffff", r=6)
    c.arc((376, 452, 398, 474), 270, 90, "#ffffff", 4)
    c.ell((330, 476, 396, 490), fill="#f0f0f0")
    c.line([(352, 436), (348, 420), (356, 404)], col("#ffffff", 140), 2)
    # fur texture
    R = rng(11)
    for _ in range(420):
        x, y = R.uniform(110, 490), R.uniform(200, 650)
        if ((x - 300) / 200) ** 2 + ((y - 430) / 240) ** 2 < 0.95:
            a = math.radians(R.uniform(70, 110))
            L = R.uniform(10, 26)
            c.line([(x, y), (x + math.cos(a) * L * 0.4, y + math.sin(a) * L)], R.choice([dark, light]), 2)
    # head
    c.poly(shaggy(300, 150, 120, 125, n=90, seed=2, amp=0.07), fill=fur)
    c.poly(shaggy(300, 60, 50, 40, n=30, seed=8, amp=0.12), fill=fur)  # crest
    for _ in range(80):
        x, y = R.uniform(200, 400), R.uniform(50, 120)
        c.line([(x, y), (x + R.uniform(-3, 3), y + R.uniform(8, 16))], R.choice([dark, light]), 2)
    # face
    c.ell((228, 120, 372, 270), fill=face)
    c.ell((222, 128, 378, 168), fill=dark)  # heavy brow
    if expr == "surprised":
        c.ell((222, 116, 378, 152), fill=dark)
    if expr != "happy":
        for x in (268, 332):
            c.ell((x - 14, 172 - 12, x + 14, 172 + 12), fill="#e8d8c0")
    eyes(c, 268, 332, 172, expr, size=10, color="#120a06", white=False)
    for x in (268, 332):
        if expr == "neutral":
            c.circle(x, 172, 13, outline=col("#d8b080", 120), width=2)
    c.ell((282, 192, 318, 222), fill=skin_dark)
    c.circle(292, 212, 5, fill="#120a06")
    c.circle(308, 212, 5, fill="#120a06")
    mouth(c, 300, 240, 22, expr, color="#120a06", inner="#3a1414")
    if expr == "happy":
        blush(c, 252, 348, 222, r=16, color="#c8506a", a=90)
    c.save(os.path.join(OUT, "gerald_%s.png" % expr))


# ----------------------------------------------------------------- Solstice
def solstice(expr):
    W, H = 460, 700
    c = Canvas(W, H)
    skin, skin_d = "#8a5a3a", "#6e4428"
    # hair (behind)
    hair = blob(230, 230, 135, 210, n=60, seed=3, amp=0.05)
    c.poly(hair, fill="#ffb0d8")
    c.poly(blob(230, 300, 120, 150, n=50, seed=5, amp=0.05), fill="#ffd9a0")
    # legs
    c.poly([(180, 460), (226, 460), (218, 560), (186, 560)], fill=skin)
    c.poly([(234, 460), (280, 460), (274, 560), (242, 560)], fill=skin)
    # fur leg warmers (rainbow stripes)
    rainbow = ["#ff5f7a", "#ffc65a", "#9dff6a", "#5ae6ff", "#9b6bff"]
    for x in (200, 258):
        for k in range(6):
            cc = "#fff6fb" if k % 2 == 0 else rainbow[(k // 2 + (x > 230)) % 5]
            c.poly(shaggy(x, 568 + k * 22, 44, 18, n=30, seed=k + x, amp=0.15), fill=cc)
        c.ell((x - 40, 674, x + 44, 698), fill="#e0e0f0")
    # shorts (holographic)
    c.poly([(172, 410), (288, 410), (292, 480), (234, 480), (230, 460), (226, 480), (168, 480)], fill="#9b6bff")
    c.poly([(172, 410), (230, 410), (226, 480), (168, 480)], fill=col("#5ae6ff", 140))
    c.rect((170, 404, 290, 418), fill="#ffe14d")
    # torso
    c.poly([(176, 260), (284, 260), (292, 340), (276, 412), (184, 412), (168, 340)], fill=skin)
    c.ell((214, 380, 222, 392), fill=skin_d)
    # LED crop top
    c.poly([(170, 262), (290, 262), (296, 340), (164, 340)], fill="#141018")
    R = rng(4)
    for i in range(18):
        x, y = R.uniform(180, 282), R.uniform(272, 332)
        cc = rainbow[i % 5]
        c.circle(x, y, 9, fill=col(cc, 140), blur=4)
        c.circle(x, y, 3, fill=mix(cc, "#ffffff", 0.5))
    # arms
    c.line([(176, 272), (140, 360), (130, 430)], skin, 30)
    c.line([(284, 272), (320, 360), (334, 430)], skin, 30)
    for k, cc in enumerate(rainbow):
        c.circle(124 + k * 5, 404, 5, fill=cc)
        c.circle(320 + k * 5, 404, 5, fill=cc)
    c.ell((116, 420, 146, 452), fill=skin)
    c.ell((318, 420, 350, 452), fill=skin)
    # neck + head
    c.rect((214, 220, 246, 268), fill=skin_d)
    c.ell((172, 100, 288, 236), fill=skin)
    # front hair strands
    c.poly([(170, 160), (178, 104), (230, 86), (284, 104), (292, 168), (276, 128), (240, 116), (200, 122)], fill="#ffb0d8")
    # goggles on forehead
    c.line([(166, 130), (294, 130)], "#2a2a2a", 8)
    for x in (204, 256):
        c.circle(x, 124, 24, fill="#3a3a44")
        c.circle(x, 124, 18, fill="#5ae6ff")
        c.circle(x - 6, 118, 5, fill=col("#ffffff", 220))
    eyes(c, 210, 252, 178, expr, size=8, lash=True)
    brows(c, 210, 252, 160, expr, w=10, width=3, color="#5a3020")
    # glitter
    for _ in range(14):
        x = R.choice([R.uniform(180, 205), R.uniform(257, 282)])
        y = R.uniform(185, 205)
        c.circle(x, y, 1.8, fill=R.choice(["#ffffff", "#ffe14d", "#5ae6ff"]))
    mouth(c, 231, 210, 12, expr, color="#3a1010", inner="#8a2a3a")
    # earrings
    c.circle(172, 196, 6, fill="#ffe14d")
    c.circle(288, 196, 6, fill="#ffe14d")
    c.save(os.path.join(OUT, "solstice_%s.png" % expr))


# ----------------------------------------------------------------- Wren
def wren(expr):
    W, H = 420, 700
    c = Canvas(W, H)
    skin, black, black2 = "#f0d2c0", "#16141a", "#24222a"
    # legs + boots
    c.poly([(160, 440), (208, 440), (204, 640), (164, 640)], fill=black2)
    c.poly([(212, 440), (260, 440), (256, 640), (216, 640)], fill=black2)
    c.rect((152, 630, 210, 690), fill="#0a0a0a", r=8)
    c.rect((210, 630, 268, 690), fill="#0a0a0a", r=8)
    # torso: black hoodie
    c.poly([(140, 250), (280, 250), (296, 450), (124, 450)], fill=black)
    c.line([(210, 260), (210, 448)], "#2e2c36", 2)
    # belt + walkie
    c.rect((124, 430, 296, 448), fill="#2e2e2e")
    c.rect((268, 400, 300, 470), fill="#303438", r=4)
    c.line([(292, 400), (292, 360)], "#303438", 5)
    c.circle(284, 418, 4, fill="#40ff40")
    # lanyard + badge
    c.line([(176, 252), (204, 360)], "#ff5fb8", 4)
    c.line([(244, 252), (216, 360)], "#ff5fb8", 4)
    c.rect((186, 356, 234, 404), fill="#ffffff", r=4)
    c.text((210, 372), "CREW", 11, "#16141a", font="bold")
    c.text((210, 390), "care", 9, "#ff5fb8", font="sans")
    # arms: left holds clipboard
    c.line([(146, 262), (118, 360), (170, 400)], black, 34)
    c.poly([(150, 330), (238, 316), (250, 420), (162, 434)], fill="#b08050")
    c.rect((182, 316, 214, 330), fill="#c0c0c8", r=3)
    for k in range(5):
        y = 350 + k * 14
        c.line([(168, y + 2), (232, y - 8)], "#f0f0f0", 3)
    c.ell((150, 380, 186, 412), fill=skin)
    c.line([(274, 262), (300, 360), (292, 430)], black, 34)
    c.ell((276, 424, 308, 454), fill=skin)
    # neck & head
    c.rect((194, 210, 226, 256), fill="#e0bca8")
    c.ell((152, 90, 268, 226), fill=skin)
    # hair: asymmetric undercut
    c.poly([(150, 160), (152, 110), (180, 82), (236, 76), (272, 100), (278, 150), (262, 120), (236, 112),
            (206, 126), (182, 150), (168, 196)], fill="#1a1418")
    c.poly([(262, 120), (272, 100), (278, 150), (270, 140)], fill="#3a3440")
    # headset
    c.arc((144, 70, 276, 200), 190, 350, "#2a2a30", 7)
    c.ell((138, 140, 162, 182), fill="#2a2a30")
    c.line([(150, 175), (160, 206), (178, 214)], "#2a2a30", 4)
    c.circle(180, 214, 5, fill="#ff4a4a")
    eyes(c, 192, 232, 162, expr, size=7)
    if expr != "happy":
        for x in (192, 232):
            c.arc((x - 9, 166, x + 9, 178), 20, 160, col("#9a7080", 160), 2)  # tired eyes
    brows(c, 192, 232, 146, expr, w=9, width=3, color="#1a1418")
    if expr == "happy":
        blush(c, 178, 246, 184, r=10, a=90)
    mouth(c, 212, 198, 10, expr if expr != "neutral" else "neutral")
    c.save(os.path.join(OUT, "wren_%s.png" % expr))


# ----------------------------------------------------------------- Zyx
def zyx(expr):
    W, H = 440, 700
    c = Canvas(W, H)
    suit, suit_d, skin = "#c8ccd8", "#9aa0b4", "#a8e8d8"
    # antennae
    for side in (-1, 1):
        pts = [(220 + side * 40, 70), (220 + side * 70, 20), (220 + side * 96, 10)]
        c.line(pts, "#7ac8b8", 5)
        c.circle(pts[-1][0], pts[-1][1], 18, fill=col("#ff5fb8", 120), blur=6)
        c.circle(pts[-1][0], pts[-1][1], 9, fill="#ffb0e0")
    # legs
    c.poly([(178, 450), (214, 450), (206, 660), (182, 660)], fill=suit_d)
    c.poly([(226, 450), (262, 450), (258, 660), (234, 660)], fill=suit_d)
    c.ell((168, 650, 220, 690), fill="#e8eaf0")
    c.ell((222, 650, 274, 690), fill="#e8eaf0")
    # body
    c.poly([(160, 250), (280, 250), (290, 460), (150, 460)], fill=suit)
    c.poly([(220, 250), (280, 250), (290, 460), (220, 460)], fill=suit_d)
    c.line([(176, 270), (180, 440)], col("#ffffff", 180), 6, blur=2)
    # spiky collar
    for k in range(7):
        x = 160 + k * 20
        c.poly([(x, 254), (x + 20, 254), (x + 10, 226)], fill="#7ac8b8")
    # sash
    c.poly([(160, 270), (186, 254), (290, 420), (264, 440)], fill="#e8c040")
    c.text((226, 350), "AMBASSADOR", 11, "#5a3a00", font="bold")
    # arms with 3-finger gloves
    c.line([(166, 262), (130, 370), (126, 440)], suit, 26)
    c.line([(274, 262), (318, 340), (340, 300)], suit, 26)  # waving
    for (x, y, up) in ((126, 450, False), (344, 288, True)):
        c.circle(x, y, 16, fill="#7ac8b8")
        for k in (-1, 0, 1):
            dy = -1 if up else 1
            c.line([(x + k * 8, y), (x + k * 12, y + dy * 24)], "#7ac8b8", 7)
    # head (big)
    c.rect((206, 210, 234, 256), fill=skin)
    c.ell((120, 40, 320, 250), fill=skin)
    c.ell((140, 52, 230, 110), fill=col("#ffffff", 80), blur=6)
    # three eyes
    def alien_eye(x, y, w, h):
        if expr == "happy":
            c.arc((x - w, y - h * 0.6, x + w, y + h), 200, 340, "#0a1414", 6)
        else:
            k = 1.15 if expr == "surprised" else 1.0
            c.ell((x - w * k, y - h * k, x + w * k, y + h * k), fill="#0a1414")
            c.ell((x - w * 0.5, y - h * 0.65, x - w * 0.05, y - h * 0.15), fill=col("#7affe0", 200))
            if expr == "surprised":
                c.circle(x, y, w * 0.35, fill="#ffffff")
    alien_eye(178, 150, 26, 32)
    alien_eye(262, 150, 26, 32)
    alien_eye(220, 92, 14, 16)
    if expr == "surprised":
        c.ell((212, 200, 228, 222), fill="#0a1414")
    elif expr == "happy":
        c.arc((204, 190, 236, 212), 20, 160, "#0a1414", 3)
        blush(c, 158, 282, 196, r=14, color="#ff8fc8", a=120)
    else:
        c.line([(210, 206), (230, 206)], "#0a1414", 3)
    c.save(os.path.join(OUT, "zyx_%s.png" % expr))


if __name__ == "__main__":
    for fn in (juni, gerald, solstice, wren, zyx):
        for e in EXPRS:
            fn(e)
        print("painted", fn.__name__)
