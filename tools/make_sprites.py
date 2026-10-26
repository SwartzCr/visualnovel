"""Paint the character sprites in an anime visual-novel style.

Bust-up framing, ink outlines, cel shading, layered eyes with highlights and
clumped hair with shine bands. Four expressions per character:
neutral, happy, surprised, blush.

    python3 tools/make_sprites.py            # everyone
    python3 tools/make_sprites.py juni wren  # just some
"""
import math
import os
import sys

from artlib import Canvas, col, mix, rng

OUT = os.path.join(os.path.dirname(__file__), "..", "game", "images", "sprites")
os.makedirs(OUT, exist_ok=True)
EXPRS = ("neutral", "happy", "surprised", "blush")
LINE = "#2b1a2e"
LW = 3  # ink line width


# ------------------------------------------------------------------ helpers
def smooth(pts, n=2, closed=True):
    """Chaikin corner cutting."""
    for _ in range(n):
        out = []
        m = len(pts) if closed else len(pts) - 1
        if not closed:
            out.append(pts[0])
        for i in range(m):
            p, q = pts[i], pts[(i + 1) % len(pts)]
            out.append((0.75 * p[0] + 0.25 * q[0], 0.75 * p[1] + 0.25 * q[1]))
            out.append((0.25 * p[0] + 0.75 * q[0], 0.25 * p[1] + 0.75 * q[1]))
        if not closed:
            out.append(pts[-1])
        pts = out
    return pts


def ink(c, pts, fill, line=LINE, lw=LW, sm=2):
    pts = smooth(pts, sm) if sm else pts
    c.poly(pts, fill=fill, outline=line, width=lw)
    return pts


def ink_ell(c, box, fill, line=LINE, lw=LW):
    c.ell(box, fill=fill, outline=line, width=lw)


def arc_pts(cx, cy, rx, ry, a0, a1, n=24):
    return [(cx + math.cos(math.radians(a0 + (a1 - a0) * i / n)) * rx,
             cy + math.sin(math.radians(a0 + (a1 - a0) * i / n)) * ry) for i in range(n + 1)]


def spikes(base, tips, depth=0.45):
    """Hair clump outline: walk along base points (left->right) and put a
    pointed tip between each consecutive pair. depth pulls valleys up."""
    pts = [base[0]]
    for i, tip in enumerate(tips):
        a, b = base[i], base[i + 1]
        pts.append(tip)
        mid = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
        if i < len(tips) - 1:
            vx = b[0]
            vy = b[1] + (tip[1] - b[1]) * depth
            pts.append((vx, vy))
    pts.append(base[-1])
    return pts


def shine(c, cx, cy, rx, ry, a0, a1, color, width=6, gaps=5, seed=1):
    """Anime 'angel ring' highlight: broken arc."""
    R = rng(seed)
    step = (a1 - a0) / (gaps * 2)
    a = a0
    while a < a1:
        seg = arc_pts(cx, cy, rx, ry, a, a + step * R.uniform(0.6, 1.2), 6)
        c.line(seg, col(color, 200), width)
        a += step * 2


# ------------------------------------------------------------------ faces
class Face:
    def __init__(self, cx, cy, w, h, skin, shadow, iris, brow, lash=LINE):
        self.cx, self.cy, self.w, self.h = cx, cy, w, h
        self.skin, self.shadow, self.iris, self.brow, self.lash = skin, shadow, iris, brow, lash

    def outline_pts(self):
        cx, cy, w, h = self.cx, self.cy, self.w, self.h
        pts = arc_pts(cx, cy - 0.15 * h, w, h * 0.85, 180, 360, 16)
        pts += [(cx + w * 0.99, cy + 0.2 * h), (cx + w * 0.86, cy + 0.55 * h), (cx + w * 0.48, cy + 0.86 * h),
                (cx + w * 0.1, cy + 1.02 * h), (cx, cy + 1.05 * h), (cx - w * 0.1, cy + 1.02 * h),
                (cx - w * 0.48, cy + 0.86 * h), (cx - w * 0.86, cy + 0.55 * h), (cx - w * 0.99, cy + 0.2 * h)]
        return pts

    def ears(self, c, pointed=False):
        cx, cy, w, h = self.cx, self.cy, self.w, self.h
        for s in (-1, 1):
            x = cx + s * w * 0.95
            if pointed:
                ink(c, [(x, cy - 0.05 * h), (x + s * w * 0.55, cy - 0.45 * h), (x + s * w * 0.12, cy + 0.38 * h)], self.skin, sm=1)
            else:
                ink_ell(c, (x - w * 0.16, cy - 0.02 * h, x + w * 0.16, cy + 0.38 * h), self.skin)

    def neck(self, c, width=0.36, length=0.55):
        cx, cy, w, h = self.cx, self.cy, self.w, self.h
        ink(c, [(cx - w * width, cy + 0.6 * h), (cx + w * width, cy + 0.6 * h),
                (cx + w * width * 1.05, cy + (1 + length) * h), (cx - w * width * 1.05, cy + (1 + length) * h)],
            self.skin, sm=0)
        c.poly([(cx - w * width, cy + 0.85 * h), (cx + w * width, cy + 0.85 * h), (cx + w * width, cy + 1.2 * h),
                (cx, cy + 1.3 * h), (cx - w * width, cy + 1.2 * h)], fill=self.shadow)

    def base(self, c):
        ink(c, self.outline_pts(), self.skin, sm=2)

    def bang_shadow(self, c, depth=0.25):
        cx, cy, w, h = self.cx, self.cy, self.w, self.h
        pts = arc_pts(cx, cy - 0.15 * h, w * 0.97, h * 0.82, 180, 360, 14)
        pts += [(cx + w * 0.95, cy + (depth - 0.05) * h)]
        for i in range(9):
            t = i / 8
            x = cx + w * 0.95 - t * w * 1.9
            pts.append((x, cy + depth * h + (12 if i % 2 else 0)))
        c.poly(pts, fill=col(self.shadow, 230))

    def eyes(self, c, expr, lid=0.0, size=1.0, gap=0.42):
        cx, cy, w, h = self.cx, self.cy, self.w, self.h
        ew, eh = w * 0.26 * size, w * 0.3 * size
        ey = cy + 0.2 * h
        for s in (-1, 1):
            self.eye(c, cx + s * w * gap, ey, ew, eh, s, expr, lid)

    def eye(self, c, x, y, ew, eh, side, expr, lid):
        iris = self.iris
        dark = mix(iris, "#000000", 0.55)
        light = mix(iris, "#ffffff", 0.35)
        if expr == "happy":
            pts = [(x - ew * 1.05, y + eh * 0.25), (x - ew * 0.5, y - eh * 0.35), (x, y - eh * 0.5),
                   (x + ew * 0.5, y - eh * 0.35), (x + ew * 1.05, y + eh * 0.25)]
            c.line(smooth(pts, 2, closed=False), self.lash, eh * 0.22)
            return
        sc = 1.12 if expr == "surprised" else 1.0
        # sclera
        sclera = [(x - ew * 1.05 * sc, y - eh * 0.2), (x - ew * 0.6, y - eh * 0.85 * sc), (x + ew * 0.6, y - eh * 0.85 * sc),
                  (x + ew * 1.05 * sc, y - eh * 0.25), (x + ew * 0.75, y + eh * 0.85 * sc), (x, y + eh * 0.98 * sc),
                  (x - ew * 0.75, y + eh * 0.85 * sc)]
        c.poly(smooth(sclera, 2), fill="#ffffff")
        # iris
        ir = 0.55 if expr == "surprised" else 0.74
        ix0, iy0, ix1, iy1 = x - ew * ir, y - eh * 0.82, x + ew * ir, y + eh * 0.95
        if expr == "surprised":
            iy0, iy1 = y - eh * 0.55, y + eh * 0.6
        c.ell((ix0, iy0, ix1, iy1), fill=dark)
        c.ell((ix0 + ew * 0.1, iy0 + (iy1 - iy0) * 0.3, ix1 - ew * 0.1, iy1 - eh * 0.05), fill=iris)
        c.ell((ix0 + ew * 0.22, iy0 + (iy1 - iy0) * 0.55, ix1 - ew * 0.22, iy1 - eh * 0.1), fill=light)
        pr = 0.22 if expr == "surprised" else 0.32
        c.ell((x - ew * pr, (iy0 + iy1) / 2 - eh * pr * 1.1, x + ew * pr, (iy0 + iy1) / 2 + eh * pr * 1.3), fill=mix(iris, "#000000", 0.8))
        c.ell((ix0, iy0, ix1, iy1), outline=mix(iris, "#000000", 0.7), width=2)
        # lid shadow on top of eye
        c.poly([(x - ew * 1.05, y - eh * 0.2), (x - ew * 0.6, y - eh * 0.9), (x + ew * 0.6, y - eh * 0.9),
                (x + ew * 1.05, y - eh * 0.25), (x + ew * 0.7, y - eh * 0.45), (x - ew * 0.7, y - eh * 0.45)],
               fill=col(mix(iris, "#000000", 0.6), 120))
        # highlights
        c.circle(x - side * ew * 0.28 - ew * 0.05, y - eh * 0.32, ew * 0.24, fill="#ffffff")
        c.circle(x + side * ew * 0.3, y + eh * 0.42, ew * 0.11, fill="#ffffff")
        if expr == "blush":
            c.circle(x + ew * 0.05, y + eh * 0.05, ew * 0.08, fill=col("#ffffff", 220))
        # half-closed lid
        if lid > 0:
            ly = y - eh * 0.9 + lid * eh * 1.2
            c.poly([(x - ew * 1.2, y - eh * 1.2), (x + ew * 1.2, y - eh * 1.2), (x + ew * 1.2, ly), (x - ew * 1.2, ly + eh * 0.05)],
                   fill=self.skin)
            top = ly
        else:
            top = y - eh * 0.85 * sc
        # upper lash: thick, flicked at the outer corner
        outer = x + side * ew * 1.15
        inner = x - side * ew * 1.0
        lash = [(inner, y - eh * 0.12 if lid == 0 else top + eh * 0.2), (x - side * ew * 0.4, top - eh * 0.02),
                (x + side * ew * 0.45, top + eh * 0.02), (outer, y - eh * 0.35 if lid == 0 else top + eh * 0.15),
                (outer + side * ew * 0.25, y - eh * 0.48 if lid == 0 else top + eh * 0.05)]
        c.line(smooth(lash, 2, closed=False), self.lash, eh * 0.24)
        # lower lash hint
        c.line([(x + side * ew * 0.35, y + eh * 0.92), (x + side * ew * 0.85, y + eh * 0.62)], self.lash, 2)

    def brows(self, c, expr, y_off=-0.42, w_mul=1.0, thick=4):
        cx, cy, w, h = self.cx, self.cy, self.w, self.h
        for s in (-1, 1):
            x = cx + s * w * 0.42
            y = cy + y_off * h + (-0.08 * h if expr == "surprised" else 0)
            tilt = {"neutral": 0.0, "happy": -0.03, "surprised": 0.0, "blush": 0.07}[expr]
            pts = [(x - s * w * 0.2 * w_mul, y + tilt * h * -1 + 2), (x, y - 3), (x + s * w * 0.22 * w_mul, y + tilt * h + 5)]
            c.line(smooth(pts, 2, closed=False), self.brow, thick)

    def nose(self, c):
        cx, cy, w, h = self.cx, self.cy, self.w, self.h
        c.line([(cx + w * 0.04, cy + 0.5 * h), (cx - w * 0.02, cy + 0.56 * h)], mix(self.shadow, "#000000", 0.3), 2)

    def mouth(self, c, expr, y=0.76, scale=1.0):
        cx, cy, w, h = self.cx, self.cy, self.w, self.h
        my = cy + y * h
        mw = w * 0.17 * scale
        dark = "#6a1f2e"
        if expr == "happy":
            pts = [(cx - mw * 1.3, my - mw * 0.2), (cx + mw * 1.3, my - mw * 0.2), (cx + mw * 0.8, my + mw * 0.9),
                   (cx, my + mw * 1.15), (cx - mw * 0.8, my + mw * 0.9)]
            c.poly(smooth(pts, 2), fill=dark, outline=LINE, width=2)
            c.ell((cx - mw * 0.7, my + mw * 0.35, cx + mw * 0.7, my + mw * 1.1), fill="#ff8a9a")
        elif expr == "surprised":
            c.ell((cx - mw * 0.45, my - mw * 0.2, cx + mw * 0.45, my + mw * 0.8), fill=dark, outline=LINE, width=2)
        elif expr == "blush":
            pts = [(cx - mw * 0.8, my), (cx - mw * 0.3, my + mw * 0.25), (cx, my + mw * 0.05),
                   (cx + mw * 0.3, my + mw * 0.25), (cx + mw * 0.8, my)]
            c.line(smooth(pts, 2, closed=False), LINE, 2.5)
        else:
            pts = [(cx - mw * 0.75, my), (cx, my + mw * 0.3), (cx + mw * 0.75, my - mw * 0.05)]
            c.line(smooth(pts, 2, closed=False), LINE, 2.5)

    def blush(self, c, strength=1.0, color="#ff6f8f"):
        cx, cy, w, h = self.cx, self.cy, self.w, self.h
        for s in (-1, 1):
            x, y = cx + s * w * 0.55, cy + 0.52 * h
            c.ell((x - w * 0.24, y - h * 0.08, x + w * 0.24, y + h * 0.08), fill=col(color, int(130 * strength)), blur=4)
            if strength >= 1:
                for k in range(3):
                    hx = x - w * 0.12 + k * w * 0.1
                    c.line([(hx, y + h * 0.04), (hx + w * 0.06, y - h * 0.04)], col("#e04a6a", 200), 2)

    def features(self, c, expr, lid_neutral=0.0, blush_always=0.0, eye_size=1.0):
        lid = lid_neutral if expr == "neutral" else 0.0
        self.eyes(c, expr, lid=lid, size=eye_size)
        self.brows(c, expr)
        self.nose(c)
        self.mouth(c, expr)
        if expr == "blush":
            self.blush(c, 1.0)
        elif expr == "happy":
            self.blush(c, 0.6)
        elif blush_always:
            self.blush(c, blush_always)


def save(c, name, expr):
    c.save(os.path.join(OUT, "%s_%s.png" % (name, expr)))


# ------------------------------------------------------------------ Juni (axolotl kigurumi)
def juni(expr):
    W, H = 560, 720
    c = Canvas(W, H)
    pink, pink_d, pink_l, belly, gill, gill_d = "#ffa6cf", "#ec7fb0", "#ffd0e5", "#fff0f6", "#ff5c9a", "#d63a78"
    skin, skin_s = "#e2a882", "#c6886a"
    hair, hair_l = "#3a2420", "#6a4436"
    f = Face(280, 232, 80, 96, skin, skin_s, "#c8782e", hair)

    # gills behind the hood: three feathery fronds per side
    for s in (-1, 1):
        for k, ang in enumerate((-40, -10, 22)):
            a = math.radians(ang)
            x0, y0 = 280 + s * 130, 150 + k * 42
            L = 120 - k * 8
            x1, y1 = x0 + s * math.cos(a) * L, y0 + math.sin(a) * L
            c.line([(x0, y0), (x1, y1)], LINE, 22)
            c.line([(x0, y0), (x1, y1)], gill, 16)
            for t in (0.3, 0.5, 0.7, 0.9):
                px, py = x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
                for d in (-1, 1):
                    ink_ell(c, (px - 11, py + d * 13 - 11, px + 11, py + d * 13 + 11), gill, lw=2)
            c.line([(x0, y0), (x1, y1)], gill_d, 4)

    # onesie body
    body = [(150, 350), (410, 350), (470, 430), (500, 720), (60, 720), (90, 430)]
    ink(c, body, pink)
    c.poly(smooth([(330, 360), (410, 352), (470, 430), (500, 720), (380, 720)], 2), fill=pink_d)
    ink(c, [(200, 420), (360, 420), (390, 560), (360, 720), (200, 720), (170, 560)], belly)
    c.line([(280, 410), (280, 720)], "#d898b8", 3)
    c.rect((272, 404, 288, 424), fill="#d8d8e8", outline=LINE, width=2, r=3)
    # sleeve arms curled to chest, paws hidden in sleeves (moe sleeves)
    for s in (-1, 1):
        arm = [(280 + s * 150, 380), (280 + s * 205, 470), (280 + s * 170, 560), (280 + s * 70, 560),
               (280 + s * 60, 515), (280 + s * 140, 500), (280 + s * 120, 430)]
        ink(c, arm, pink)
        ink_ell(c, (280 + s * 70 - 42, 512, 280 + s * 70 + 42, 572), pink_d)
        c.arc((280 + s * 70 - 30, 520, 280 + s * 70 + 30, 562), 200, 340, "#c86098", 3)

    # hood
    ink_ell(c, (115, 40, 445, 360), pink)
    c.pieslice((115, 40, 445, 360), 300, 420, pink_d)
    c.ell((150, 60, 330, 140), fill=col("#ffffff", 70), blur=8)
    # the hood's own axolotl face
    for x in (192, 368):
        ink_ell(c, (x - 17, 82, x + 17, 116), "#2b1a2e")
        c.circle(x - 6, 92, 6, fill="#ffffff")
    c.line(smooth([(250, 98), (265, 112), (280, 104), (295, 112), (310, 98)], 2, closed=False), LINE, 3)
    for x in (165, 395):
        c.ell((x - 16, 120, x + 16, 134), fill=col("#ff6f9f", 160), blur=2)
    # hood opening rim
    ink_ell(c, (174, 128, 386, 352), pink_d)

    f.neck(c)
    f.base(c)
    # fluffy bangs peeking out of the hood
    base = arc_pts(280, 214, 92, 72, 195, 345, 7)
    tips = [(200, 250), (226, 262), (252, 248), (276, 270), (302, 250), (330, 262), (360, 246)]
    pts = arc_pts(280, 214, 100, 86, 345, 195, 10)[::-1][::-1]
    bangs = [(184, 170)] + arc_pts(280, 190, 100, 60, 200, 340, 8) + [(376, 170), (372, 242)]
    for i, t in enumerate(reversed(tips)):
        bangs.append(t)
        if i < len(tips) - 1:
            bangs.append((t[0] - 13, 214))
    bangs.append((188, 242))
    f.bang_shadow(c, depth=0.0)
    ink(c, bangs, hair, sm=1)
    for side in (-1, 1):  # side locks
        ink(c, [(280 + side * 88, 200), (280 + side * 98, 250), (280 + side * 86, 300), (280 + side * 70, 250)], hair, sm=1)
    shine(c, 280, 196, 70, 30, 205, 335, hair_l, width=5, gaps=4)
    f.features(c, expr, blush_always=0.35)
    save(c, "juni", expr)


# ------------------------------------------------------------------ Gerald (sasquatch)
def fur_clump_ring(cx, cy, rx, ry, n, depth, seed, a0=0, a1=360, jitter=0.08):
    R = rng(seed)
    pts = []
    for i in range(n * 2 + 1):
        a = math.radians(a0 + (a1 - a0) * i / (n * 2))
        k = 1 + (depth if i % 2 else 0) + R.uniform(-jitter, jitter) * 0.3
        sw = 0.06 if i % 2 else 0
        pts.append((cx + math.cos(a + sw) * rx * k, cy + math.sin(a + sw) * ry * k))
    return pts


def gerald(expr):
    W, H = 700, 720
    c = Canvas(W, H)
    fur, fur_d, fur_l, fur_ll = "#8a5a3c", "#64402a", "#a8744e", "#c8956a"
    face_c, face_s = "#e2bc98", "#c49a78"
    # body: big fluffy mass
    ink(c, fur_clump_ring(350, 560, 300, 260, 26, 0.1, 3, 180, 360) + [(680, 720), (20, 720)], fur, sm=0)
    c.poly(fur_clump_ring(470, 600, 180, 200, 12, 0.08, 4, 230, 360) + [(680, 720), (480, 720)], fill=fur_d)
    # chest fluff highlight clumps
    R = rng(7)
    for _ in range(36):
        x, y = R.uniform(140, 560), R.uniform(380, 700)
        L = R.uniform(28, 50)
        c.poly([(x - 9, y), (x + 9, y), (x + R.uniform(-6, 6), y + L)], fill=R.choice([fur_l, fur_d]))
    # arms
    for s in (-1, 1):
        arm = fur_clump_ring(350 + s * 255, 560, 80, 190, 10, 0.12, 10 + s)
        ink(c, arm, fur_d if s > 0 else fur, sm=0)
    # big hands cradling a tiny teacup
    ink_ell(c, (250, 520, 360, 600), face_s)
    ink_ell(c, (340, 520, 450, 600), face_s)
    ink(c, [(318, 486), (382, 486), (376, 532), (324, 532)], "#ffffff", sm=1)
    c.arc((372, 494, 398, 520), 270, 90, LINE, 3)
    c.arc((373, 496, 396, 518), 270, 90, "#ffffff", 2)
    c.ell((318, 480, 382, 494), fill="#a8603a", outline=LINE, width=2)
    for x in (338, 360):
        c.line([(x, 470), (x - 6, 450), (x + 2, 430)], col("#ffffff", 150), 2)
    c.text((350, 512), "♥", 14, "#ff7fae", font="sans")
    # head: tall shaggy dome with a crest
    ink(c, fur_clump_ring(350, 205, 175, 175, 20, 0.12, 2), fur, sm=0)
    ink(c, fur_clump_ring(350, 52, 60, 46, 7, 0.25, 5, 180, 360), fur, sm=0)
    c.poly(fur_clump_ring(350, 220, 160, 150, 16, 0.08, 6, 20, 160), fill=fur_d)
    shine(c, 350, 150, 120, 70, 210, 330, fur_ll, width=7, gaps=5, seed=3)
    # face plate
    f = Face(350, 230, 92, 96, face_c, face_s, "#7a4a22", fur_d, lash="#2a160c")
    ink(c, smooth(f.outline_pts(), 2), face_c, sm=0)
    # brow fur tufts over the face
    tuft = [(250, 170)] + arc_pts(350, 168, 100, 50, 200, 340, 8) + [(452, 170)]
    for x in range(440, 250, -24):
        tuft += [(x, 210 if (x // 24) % 2 else 192)]
    ink(c, tuft, fur, sm=1)
    f.eyes(c, expr, size=0.9, gap=0.4)
    f.brows(c, expr, y_off=-0.32, thick=6)
    # broad soft nose
    ink_ell(c, (326, 264, 374, 292), "#5a3424")
    c.circle(340, 272, 5, fill=col("#ffffff", 140))
    f.mouth(c, expr, y=0.82, scale=1.2)
    if expr in ("blush", "happy"):
        f.blush(c, 1.0 if expr == "blush" else 0.6, color="#e0607a")
    save(c, "gerald", expr)


# ------------------------------------------------------------------ Solstice (raver)
def solstice(expr):
    W, H = 560, 720
    c = Canvas(W, H)
    skin, skin_s = "#b07450", "#8c563a"
    hp, hb, hl = "#ff9ccb", "#ffd890", "#fff2c8"
    f = Face(280, 216, 80, 96, skin, skin_s, "#18b8c8", "#5a2a20")
    # long flowing hair behind (pink fading to blonde)
    back = [(150, 150), (130, 300), (110, 480), (90, 700), (470, 700), (450, 480), (430, 300), (410, 150)]
    back = arc_pts(280, 190, 140, 150, 180, 360, 12) + [(430, 300), (455, 480), (480, 700), (80, 700), (105, 480), (130, 300)]
    ink(c, back, hp, sm=2)
    c.poly(smooth([(110, 460), (450, 460), (480, 700), (80, 700)], 2), fill=hb)
    c.poly(smooth([(100, 420), (460, 420), (455, 470), (105, 470)], 2), fill=mix(hp, hb, 0.5))
    for x in range(120, 460, 26):
        c.line([(x, 300), (x + 8, 690)], col(mix(hp, "#c04a80", 0.4), 160), 2)

    # torso with LED crop top + bare midriff + holographic shorts
    ink(c, [(165, 345), (395, 345), (420, 420), (400, 720), (160, 720), (140, 420)], skin)
    c.poly(smooth([(320, 350), (395, 345), (420, 420), (400, 720), (350, 720)], 2), fill=skin_s)
    ink(c, [(160, 350), (400, 350), (418, 430), (395, 500), (165, 500), (142, 430)], "#1a1422")
    R = rng(4)
    rainbow = ["#ff5f7a", "#ffc65a", "#9dff6a", "#5ae6ff", "#b07bff"]
    for i in range(30):
        x, y = R.uniform(170, 392), R.uniform(370, 488)
        cc = rainbow[i % 5]
        c.circle(x, y, 11, fill=col(cc, 140), blur=5)
        c.circle(x, y, 3.5, fill=mix(cc, "#ffffff", 0.55))
    c.ell((272, 600, 288, 616), fill=skin_s)
    ink(c, [(158, 660), (402, 660), (410, 720), (150, 720)], "#9b6bff", sm=0)
    c.poly([(158, 664), (280, 664), (276, 720), (152, 720)], fill=col("#5ae6ff", 150))
    c.rect((156, 652, 404, 668), fill="#ffe14d", outline=LINE, width=2)
    # arms with kandi bracelets
    for s in (-1, 1):
        ink(c, [(280 + s * 118, 352), (280 + s * 160, 380), (280 + s * 178, 540), (280 + s * 176, 700),
                (280 + s * 140, 700), (280 + s * 136, 540), (280 + s * 122, 420)], skin if s < 0 else skin_s, sm=1)
        for k in range(3):
            y = 600 + k * 14
            for j in range(7):
                c.circle(280 + s * (140 + j * 5.5), y, 5, fill=rainbow[(j + k) % 5])
    f.neck(c)
    f.ears(c)
    for s in (-1, 1):  # hoop earrings
        c.ell((280 + s * 84 - 12, 250, 280 + s * 84 + 12, 280), outline="#ffd84a", width=4)
    f.base(c)
    f.bang_shadow(c, depth=-0.1)
    # bangs: swept, voluminous
    bangs = arc_pts(280, 190, 108, 122, 185, 355, 12)
    bangs += [(388, 230), (360, 190), (352, 236), (322, 182), (300, 226), (270, 176), (246, 222), (220, 180), (196, 230), (178, 198), (170, 260)]
    ink(c, bangs, hp, sm=1)
    shine(c, 280, 170, 90, 70, 210, 330, hl, width=6, gaps=5, seed=2)
    # goggles pushed up
    c.line(smooth([(168, 130), (280, 110), (392, 130)], 2, closed=False), LINE, 14)
    c.line(smooth([(168, 130), (280, 110), (392, 130)], 2, closed=False), "#3a3a48", 10)
    for x in (238, 322):
        ink_ell(c, (x - 36, 86, x + 36, 146), "#4a4a5a")
        c.ell((x - 27, 94, x + 27, 138), fill="#5ae6ff")
        c.ell((x - 20, 98, x + 4, 116), fill=col("#ffffff", 200))
        c.ell((x - 27, 94, x + 27, 138), outline=col("#ff5fb8", 160), width=3)
    f.features(c, expr, eye_size=1.05)
    # glitter + star sticker
    for _ in range(18):
        s = R.choice([-1, 1])
        x = 280 + s * R.uniform(40, 70)
        y = R.uniform(268, 292)
        c.circle(x, y, 2, fill=R.choice(["#ffffff", "#ffe14d", "#5ae6ff", "#ff9ccb"]))
    sx, sy = 340, 286
    star = [(sx + math.cos(math.radians(-90 + i * 36)) * (9 if i % 2 == 0 else 4),
             sy + math.sin(math.radians(-90 + i * 36)) * (9 if i % 2 == 0 else 4)) for i in range(10)]
    c.poly(star, fill="#ffe14d", outline=LINE, width=1)
    save(c, "solstice", expr)


# ------------------------------------------------------------------ Wren (staff in black)
def wren(expr):
    W, H = 560, 720
    c = Canvas(W, H)
    skin, skin_s = "#f6dccc", "#e2b8a6"
    hair, hair_l, black, black_l = "#17131c", "#4a4058", "#1c1a22", "#2e2b38"
    f = Face(280, 214, 78, 96, skin, skin_s, "#8a6ab8", hair)
    # back hair (short)
    ink(c, arc_pts(280, 200, 104, 120, 160, 380, 16) + [(372, 290), (190, 290)], hair, sm=2)
    # hoodie body
    ink(c, [(160, 340), (400, 340), (440, 420), (450, 720), (110, 720), (120, 420)], black)
    c.poly(smooth([(330, 345), (400, 340), (440, 420), (450, 720), (370, 720)], 2), fill="#111016")
    # hood bunched behind neck
    ink(c, [(190, 318), (370, 318), (390, 360), (280, 384), (170, 360)], black_l)
    # drawstrings + lanyard
    for x in (250, 310):
        c.line([(x, 370), (x + (x - 280) * 0.1, 470)], "#c8c8d0", 3)
    c.line([(214, 360), (262, 520)], "#ff5fb8", 6)
    c.line([(346, 360), (298, 520)], "#ff5fb8", 6)
    # walkie on the right hip
    ink(c, [(392, 560), (440, 560), (440, 680), (392, 680)], "#3a3e46", sm=0)
    c.line([(430, 560), (430, 500)], LINE, 7)
    c.circle(410, 578, 5, fill="#40ff60")
    for k in range(4):
        c.line([(400, 610 + k * 12), (432, 610 + k * 12)], "#22252a", 3)
    # arm hugging the clipboard
    ink(c, [(120, 400), (165, 360), (200, 420), (210, 560), (330, 610), (320, 660), (170, 640), (120, 560)], black_l)
    ink(c, [(170, 470), (330, 440), (360, 640), (196, 668)], "#c08a56", sm=0)
    ink(c, [(236, 446), (284, 438), (288, 462), (240, 470)], "#c8ccd8", sm=0)
    ink(c, [(186, 486), (322, 462), (346, 630), (208, 652)], "#fbfbf6", sm=0)
    for k in range(7):
        y0 = 500 + k * 20
        c.line([(204, y0 + 2), (322, y0 - 20)], "#9aa0c0", 2)
        c.rect((198, y0 - 8, 208, y0 + 2), outline="#9aa0c0", width=2)
    c.text((262, 482), "RUN OF SHOW", 10, "#ff4a6a", font="cond")
    ink_ell(c, (304, 590, 348, 640), skin)
    # badge on the lanyard
    ink(c, [(244, 516), (316, 516), (316, 580), (244, 580)], "#ffffff", sm=0)
    c.text((280, 538), "CREW", 15, black, font="bold")
    c.text((280, 562), "care team", 10, "#ff5fb8", font="sans")
    f.neck(c)
    f.base(c)
    f.bang_shadow(c, depth=0.05)
    # asymmetric bangs: long sweep over the right eye side
    bangs = arc_pts(280, 196, 100, 112, 190, 350, 12)
    bangs += [(378, 214), (372, 268), (350, 300), (344, 250), (320, 214), (300, 242), (268, 196), (246, 224), (222, 194), (200, 222), (184, 214)]
    ink(c, bangs, hair, sm=1)
    c.poly([(176, 190), (186, 220), (180, 250), (172, 220)], fill=hair_l)  # undercut side
    shine(c, 280, 172, 80, 52, 215, 325, hair_l, width=5, gaps=4, seed=5)
    # headset band + earcup + mic
    c.line(smooth([(170, 230), (176, 120), (280, 82), (384, 120), (390, 230)], 2, closed=False), LINE, 12)
    c.line(smooth([(170, 230), (176, 120), (280, 82), (384, 120), (390, 230)], 2, closed=False), "#3a3a44", 8)
    ink_ell(c, (150, 200, 196, 262), "#2a2a32")
    c.circle(173, 231, 8, fill="#ff5fb8")
    c.line(smooth([(170, 258), (190, 300), (226, 312)], 2, closed=False), LINE, 5)
    ink_ell(c, (222, 304, 240, 320), "#2a2a32", lw=2)
    f.features(c, expr, lid_neutral=0.38)
    # faint tired circles
    if expr != "happy":
        for s in (-1, 1):
            x = 280 + s * 78 * 0.42
            c.arc((x - 18, 248, x + 18, 262), 20, 160, col("#b08a9a", 150), 2)
    save(c, "wren", expr)


# ------------------------------------------------------------------ Zyx (alien ambassador)
def zyx(expr):
    W, H = 560, 720
    c = Canvas(W, H)
    skin, skin_s = "#bff2de", "#8fd4ba"
    silver, silver_d, silver_l = "#c9cfdc", "#9aa2b6", "#eef2fa"
    f = Face(280, 228, 82, 98, skin, skin_s, "#e0409a", "#5aa890")
    # antennae
    for s in (-1, 1):
        pts = smooth([(280 + s * 40, 120), (280 + s * 70, 50), (280 + s * 104, 26)], 2, closed=False)
        c.line(pts, LINE, 9)
        c.line(pts, "#7ac8b0", 5)
        c.circle(280 + s * 106, 24, 24, fill=col("#ff5fb8", 120), blur=8)
        ink_ell(c, (280 + s * 106 - 11, 13, 280 + s * 106 + 11, 35), "#ffb8e0", lw=2)
    # metallic bob (hair? helmet? it won't say) behind
    ink(c, arc_pts(280, 214, 116, 130, 165, 375, 16) + [(390, 300), (170, 300)], silver_d, sm=2)
    # bodysuit
    ink(c, [(162, 350), (398, 350), (430, 420), (440, 720), (120, 720), (130, 420)], silver)
    c.poly(smooth([(320, 355), (398, 350), (430, 420), (440, 720), (360, 720)], 2), fill=silver_d)
    for x in (170, 186):
        c.line([(x, 380), (x - 12, 700)], col(silver_l, 200), 5)
    c.line([(280, 360), (280, 720)], "#7ac8b0", 3)
    for y in (430, 520, 610):
        c.circle(280, y, 7, fill="#5affd0", outline=LINE, width=2)
        c.circle(280, y, 16, fill=col("#5affd0", 90), blur=6)
    # sash
    ink(c, [(160, 380), (204, 352), (430, 640), (392, 676)], "#f0c64a", sm=0)
    c.text((300, 520), "AMBASSADOR", 13, "#6a4400", font="bold")
    # waving arm with three-fingered glove
    ink(c, [(398, 360), (440, 380), (470, 300), (478, 230), (446, 228), (436, 300), (410, 330)], silver, sm=1)
    ink_ell(c, (436, 196, 488, 244), "#7ac8b0")
    for k in (-1, 0, 1):
        ink(c, [(462 + k * 14 - 6, 210), (462 + k * 20 - 3, 168), (462 + k * 20 + 6, 168), (462 + k * 14 + 6, 210)], "#7ac8b0", lw=2, sm=1)
    ink(c, [(162, 360), (120, 400), (110, 560), (126, 700), (164, 700), (160, 560), (176, 430)], silver, sm=1)
    # spiky high collar
    for k in range(9):
        x = 196 + k * 21
        ink(c, [(x, 352), (x + 21, 352), (x + 10, 312 - (k % 2) * 14)], "#7ac8b0", lw=2, sm=0)
    f.neck(c, width=0.3)
    f.ears(c, pointed=True)
    f.base(c)
    # bob fringe, very straight and shiny
    fringe = arc_pts(280, 212, 112, 128, 185, 355, 12) + [(394, 300), (370, 300), (368, 180), (192, 180), (190, 300), (166, 300)]
    ink(c, fringe, silver, sm=1)
    c.poly([(192, 178), (368, 178), (368, 192), (192, 192)], fill=silver_d)
    shine(c, 280, 150, 92, 60, 205, 335, "#ffffff", width=7, gaps=6, seed=8)
    # third eye in the forehead
    if expr == "happy":
        c.line(smooth([(266, 206), (280, 196), (294, 206)], 2, closed=False), LINE, 4)
    else:
        ink_ell(c, (266, 192, 294, 216), "#ffffff", lw=2)
        c.circle(280, 204, 7, fill="#e0409a")
        c.circle(277, 200, 3, fill="#ffffff")
    f.eyes(c, expr, size=1.12, gap=0.44)
    f.brows(c, expr, y_off=-0.2, thick=3)
    f.mouth(c, expr, scale=0.8)
    if expr in ("blush", "happy"):
        f.blush(c, 1.0 if expr == "blush" else 0.6, color="#ff7fc0")
    save(c, "zyx", expr)


CHARS = {"juni": juni, "gerald": gerald, "solstice": solstice, "wren": wren, "zyx": zyx}

if __name__ == "__main__":
    for name in sys.argv[1:] or CHARS:
        for e in EXPRS:
            CHARS[name](e)
        print("painted", name)
