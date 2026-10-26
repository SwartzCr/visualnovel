"""Procedurally paint every background in the game (1280x720).

    python3 tools/make_backgrounds.py            # all
    python3 tools/make_backgrounds.py pool roof  # just some
"""
import math
import os
import sys

from artlib import Canvas, col, mix, rng, star_field, blob, wobble

W, H = 1280, 720
OUT = os.path.join(os.path.dirname(__file__), "..", "game", "images", "bg")
os.makedirs(OUT, exist_ok=True)

PINK, CYAN, VIOLET, GOLD, LIME = "#ff5fb8", "#5ae6ff", "#9b6bff", "#ffc65a", "#9dff6a"


# ---------------------------------------------------------------- shared bits
def floor_perspective(c, y0, color_a, color_b, lines="#000000", n=14, alpha=60):
    c.vgrad((0, y0, W, H), color_a, color_b)
    vx = W / 2
    for i in range(-n, n + 1):
        c.line([(vx + i * 20, y0), (vx + i * 160, H)], col(lines, alpha), 1.5)
    y = y0
    step = 8
    while y < H:
        c.line([(0, y), (W, y)], col(lines, alpha), 1.2)
        step *= 1.35
        y += step


def wallpaper_stripes(c, box, a, b, width=26):
    x0, y0, x1, y1 = box
    c.rect(box, fill=a)
    x = x0
    i = 0
    while x < x1:
        if i % 2:
            c.rect((x, y0, x + width, y1), fill=b)
        x += width
        i += 1


def door(c, x, y, w, h, color="#5a2d4a", num=None, light=None, hanger=False):
    c.rect((x - 4, y - 4, x + w + 4, y + h), fill="#2a1424")
    c.rect((x, y, x + w, y + h), fill=color)
    c.rect((x + w * 0.12, y + h * 0.08, x + w * 0.88, y + h * 0.45), outline=mix(color, "#000000", 0.35), width=2)
    c.rect((x + w * 0.12, y + h * 0.52, x + w * 0.88, y + h * 0.92), outline=mix(color, "#000000", 0.35), width=2)
    c.circle(x + w * 0.82, y + h * 0.5, max(2, w * 0.04), fill=GOLD)
    if num:
        c.text((x + w / 2, y - 14), num, max(9, w * 0.14), "#e8c98a", font="serif")
    if light:
        c.poly([(x, y + h), (x + w, y + h), (x + w * 1.6, y + h + 40), (x - w * 0.6, y + h + 40)], fill=col(light, 70), blur=6)
        c.rect((x + w - 6, y, x + w, y + h), fill=col(light, 200), blur=3)
    if hanger:
        hx, hy = x + w * 0.78, y + h * 0.42
        c.rect((hx - w * 0.1, hy, hx + w * 0.1, hy + h * 0.28), fill="#ffe14d", r=3)
        c.text((hx, hy + h * 0.14), "DO NOT\nDISTURB", max(5, w * 0.05), "#3a1020", font="cond", spacing=0)


def string_lights(c, x0, y0, x1, y1, sag=30, n=16, colors=(PINK, GOLD, CYAN, LIME), seed=3):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t + math.sin(t * math.pi) * sag
        pts.append((x, y))
    c.line(pts, "#1b1b1b", 1.5)
    R = rng(seed)
    for i, (x, y) in enumerate(pts[1:-1]):
        cc = colors[i % len(colors)]
        c.circle(x, y + 6, 9, fill=col(cc, 120), blur=5)
        c.circle(x, y + 6, 3.5, fill=mix(cc, "#ffffff", 0.5))


def disco_ball(c, cx, cy, r, seed=5):
    c.line([(cx, 0), (cx, cy - r)], "#888888", 2)
    c.circle(cx, cy, r, fill="#b7c0d8")
    R = rng(seed)
    for i in range(-r, r, 7):
        for j in range(-r, r, 7):
            if i * i + j * j < (r - 3) ** 2:
                v = R.randint(140, 255)
                c.rect((cx + i, cy + j, cx + i + 6, cy + j + 6), fill=(v, v, min(255, v + 20), 255))
    c.circle(cx - r * 0.35, cy - r * 0.35, r * 0.25, fill=col("#ffffff", 160), blur=4)


def light_beam(c, x, y, angle, length, spread, color, alpha=50):
    a1, a2 = math.radians(angle - spread), math.radians(angle + spread)
    pts = [(x, y), (x + math.cos(a1) * length, y + math.sin(a1) * length),
           (x + math.cos(a2) * length, y + math.sin(a2) * length)]
    c.poly(pts, fill=col(color, alpha), blur=10)


def crowd(c, y, n, seed=9, colors=("#140a20", "#1d0f2c", "#26123a"), scale=1.0):
    R = rng(seed)
    for i in range(n):
        x = R.uniform(-40, W + 40)
        h = R.uniform(120, 200) * scale
        w = h * 0.32
        cc = R.choice(colors)
        yy = y + R.uniform(-15, 25)
        c.ell((x - w / 2, yy - h, x + w / 2, yy - h + w), fill=cc)
        c.poly([(x - w * 0.8, yy - h + w * 0.9), (x + w * 0.8, yy - h + w * 0.9), (x + w, H), (x - w, H)], fill=cc)
        if R.random() < 0.35:  # raised arm
            side = R.choice([-1, 1])
            c.line([(x + side * w * 0.6, yy - h + w), (x + side * w * 1.1, yy - h - w * 0.8)], cc, w * 0.25)


def plant(c, x, y, s=1.0, seed=1):
    R = rng(seed)
    c.poly([(x - 28 * s, y), (x + 28 * s, y), (x + 20 * s, y + 50 * s), (x - 20 * s, y + 50 * s)], fill="#b5532f")
    for i in range(9):
        a = math.radians(R.uniform(200, 340))
        L = R.uniform(60, 120) * s
        ex, ey = x + math.cos(a) * L, y + math.sin(a) * L
        c.poly([(x, y), (ex - 10 * s, ey), (ex, ey - 4 * s), (ex + 10 * s, ey)], fill=R.choice(["#2f8f4e", "#3fa65b", "#24733e"]))


def framed(c, box, inner="#d8a35a", frame="#6b4520"):
    x0, y0, x1, y1 = box
    c.rect(box, fill=frame)
    c.rect((x0 + 6, y0 + 6, x1 - 6, y1 - 6), fill=inner)


# ---------------------------------------------------------------- scenes
def motel(c, night=True):
    # building
    base_y = 470
    c.rect((140, 250, 1180, base_y + 120), fill="#e9b98c" if not night else "#3b2a48")
    c.rect((140, 235, 1180, 255), fill="#c56b4a" if not night else "#5a2a4a")
    c.rect((140, 395, 1180, 410), fill="#c56b4a" if not night else "#5a2a4a")
    # walkway railing upper floor
    for x in range(150, 1180, 22):
        c.line([(x, 360), (x, 395)], "#2b1d33" if night else "#7a4a35", 2)
    c.line([(140, 360), (1180, 360)], "#2b1d33" if night else "#7a4a35", 3)
    R = rng(11)
    lights = [PINK, GOLD, CYAN, VIOLET, LIME, "#ff8f4a"]
    for row, y in enumerate((280, 430)):
        for i, x in enumerate(range(175, 1150, 95)):
            lit = night and R.random() < 0.8
            dc = "#7a3a5a" if not night else "#2a1830"
            c.rect((x, y, x + 34, y + 78 - row * 6), fill=dc)
            wc = R.choice(lights) if lit else ("#9ec7d9" if not night else "#1a1222")
            c.rect((x + 44, y + 8, x + 80, y + 40), fill=wc)
            if lit:
                c.rect((x + 38, y + 2, x + 86, y + 46), fill=col(wc, 90), blur=8)
            c.text((x + 17, y - 9), str(100 * (2 - row) + i + 1), 9, "#f3dcb0" if not night else "#c9a0d0", font="cond")
    # sign
    sx = 1080
    c.rect((sx - 8, 120, sx + 8, 600), fill="#2a2a32")
    c.rect((sx - 120, 60, sx + 120, 210), fill="#1c1426", r=12)
    if night:
        c.neon_text((sx, 105), "HOTEL", 34, PINK)
        c.neon_text((sx, 150), "MAR SOL", 34, CYAN)
        c.neon_text((sx, 190), "NO VACANCY", 16, "#ff4040")
    else:
        c.text((sx, 105), "HOTEL", 34, "#f05a9a")
        c.text((sx, 150), "MAR SOL", 34, "#3cc0e0")
        c.text((sx, 190), "NO VACANCY", 16, "#aa3333")
    string_lights(c, 140, 245, 660, 245, sag=40, seed=4) if night else None
    string_lights(c, 660, 245, 1180, 245, sag=40, seed=5) if night else None


def bg_exterior():
    c = Canvas(W, H)
    c.vgrad((0, 0, W, H), None, None, stops=[(0, "#2b1650"), (0.45, "#c2477a"), (0.7, "#ff9a5a"), (1, "#ffd39a")])
    c.circle(300, 470, 110, fill=col("#ffd56b", 200), blur=30)
    c.circle(300, 470, 60, fill="#ffe7a0")
    c.poly(blob(200, 640, 520, 160, seed=1, amp=0.03), fill="#5a2a4e")
    c.poly(blob(1100, 660, 640, 190, seed=2, amp=0.03), fill="#4a2244")
    motel(c, night=False)
    c.rect((0, 590, W, H), fill="#2d2030")
    for x in range(0, W, 120):
        c.rect((x + 20, 650, x + 80, 656), fill="#e8d26a")
    c.save(os.path.join(OUT, "exterior.png"))


def bg_exterior_night(name="exterior_night.png"):
    c = Canvas(W, H)
    c.vgrad((0, 0, W, H), None, None, stops=[(0, "#05030f"), (0.55, "#1b0f38"), (1, "#3b1d4a")])
    star_field(c, 220, (0, 0, W, 330), seed=7)
    c.circle(220, 110, 46, fill=col("#fff3d0", 90), blur=20)
    c.circle(220, 110, 34, fill="#fff3d0")
    c.circle(234, 102, 30, fill="#120a26")
    c.poly(blob(200, 640, 520, 160, seed=1, amp=0.03), fill="#120a1e")
    c.poly(blob(1100, 660, 640, 190, seed=2, amp=0.03), fill="#0e0818")
    motel(c, night=True)
    c.rect((0, 590, W, H), fill="#120c18")
    for x in range(0, W, 120):
        c.rect((x + 20, 650, x + 80, 656), fill="#5a5030")
    c.rect((0, 560, W, 600), fill=col(PINK, 40), blur=20)
    c.vignette()
    c.save(os.path.join(OUT, name))


def bg_lobby():
    c = Canvas(W, H)
    wallpaper_stripes(c, (0, 0, W, 520), "#2f6b5e", "#2a5f54", 30)
    c.rect((0, 0, W, 60), fill="#1c3a33")
    for x in range(0, W, 60):
        c.poly([(x, 60), (x + 30, 80), (x + 60, 60)], fill="#c9a24a")
    # chandelier
    c.line([(640, 0), (640, 90)], "#c9a24a", 3)
    for i in range(7):
        x = 560 + i * 27
        c.line([(640, 90), (x, 130)], "#c9a24a", 2)
        c.circle(x, 135, 6, fill="#fff2b0")
        c.circle(x, 135, 22, fill=col("#ffe08a", 70), blur=10)
    # key cubbies
    c.rect((780, 140, 1160, 400), fill="#4a2a1a")
    R = rng(3)
    for r in range(5):
        for k in range(8):
            x, y = 795 + k * 45, 155 + r * 48
            c.rect((x, y, x + 38, y + 40), fill="#2e180e")
            if R.random() < 0.55:
                c.line([(x + 19, y + 6), (x + 19, y + 26)], GOLD, 2)
                c.circle(x + 19, y + 30, 5, fill="#d84a6a")
    c.rect((780, 100, 1160, 135), fill="#1c3a33")
    c.text((970, 118), "ALL WHO ENTER ARE ALREADY CHECKED IN", 13, "#f0d690", font="cond")
    # desk
    c.rect((0, 520, W, H), fill="#3a1f2a")
    for x in range(0, W, 80):
        c.line([(x, 520), (x - 40, H)], col("#000000", 50), 2)
    c.rect((230, 440, 1050, 600), fill="#6b2f2f")
    c.rect((220, 430, 1060, 452), fill="#a8553f")
    c.rect((230, 600, 1050, 615), fill="#2a1414")
    for x in range(270, 1040, 110):
        c.rect((x, 470, x + 80, 580), outline="#4e1f1f", width=3)
    c.ell((600, 410, 650, 432), fill=GOLD)
    c.rect((622, 400, 628, 412), fill=GOLD)
    c.rect((300, 405, 380, 430), fill="#f2ead8")
    c.text((340, 418), "NO PHOTOS", 9, "#7a2222", font="cond")
    plant(c, 110, 450, 1.2, seed=4)
    plant(c, 1180, 450, 1.1, seed=8)
    c.rect((60, 120, 220, 300), fill="#e8dcc0")
    framed(c, (60, 120, 220, 300), inner="#e8dcc0")
    c.text((140, 210), "TEA BAR\n→\nNO BOOZE\nALL\nFEELINGS", 15, "#3a1f2a", font="cond", spacing=6)
    c.vignette(110)
    c.save(os.path.join(OUT, "lobby.png"))


def bg_pool():
    c = Canvas(W, H)
    c.vgrad((0, 0, W, 330), "#4fb6ff", "#bfe9ff")
    c.circle(1080, 90, 80, fill=col("#fff6c0", 140), blur=30)
    c.circle(1080, 90, 46, fill="#fff8d8")
    for i, (x, y) in enumerate([(200, 80), (520, 130), (760, 60)]):
        for dx, r in ((0, 30), (30, 40), (70, 30)):
            c.circle(x + dx, y, r, fill=col("#ffffff", 230))
    # hills + palms
    c.poly(blob(300, 340, 500, 70, seed=4, amp=0.02, start=math.pi, end=2 * math.pi) + [(800, 340), (-200, 340)], fill="#7fb07a")
    # motel behind
    c.rect((0, 220, W, 340), fill="#f1c59a")
    c.rect((0, 210, W, 228), fill="#e0705a")
    R = rng(2)
    for x in range(30, W, 110):
        c.rect((x, 250, x + 32, 330), fill="#e0705a")
        c.rect((x + 45, 258, x + 85, 292), fill="#9ad4ea")
    # deck
    c.rect((0, 340, W, H), fill="#f2e2c4")
    for y in range(350, H, 26):
        c.line([(0, y), (W, y)], "#e0cba6", 1.5)
    # pool
    pool = blob(640, 520, 470, 150, n=60, seed=1, amp=0.0)
    c.poly(blob(640, 520, 490, 166, n=60), fill="#f8f8f8")
    c.poly(pool, fill="#29b8d8")
    c.poly(blob(640, 545, 430, 120, n=60), fill="#1fa2c6")
    for i in range(26):
        x, y = R.uniform(220, 1060), R.uniform(410, 640)
        if ((x - 640) / 470) ** 2 + ((y - 520) / 150) ** 2 < 0.8:
            c.arc((x - 40, y - 6, x + 40, y + 6), 200, 340, col("#e9fbff", 200), 2)
    # inflatable flamingo
    fx, fy = 820, 520
    c.ell((fx - 60, fy - 20, fx + 60, fy + 26), fill="#ff7fb0")
    c.line([(fx + 40, fy - 5), (fx + 55, fy - 70), (fx + 75, fy - 80)], "#ff7fb0", 16)
    c.poly([(fx + 75, fy - 88), (fx + 98, fy - 78), (fx + 76, fy - 70)], fill="#222222")
    c.circle(fx + 66, fy - 82, 3, fill="#111111")
    # loungers
    for x in (60, 1110):
        c.poly([(x, 600), (x + 120, 600), (x + 140, 650), (x - 10, 650)], fill="#ffffff")
        for k in range(6):
            c.line([(x + k * 24, 600), (x + k * 26 - 4, 650)], "#5ac0d8", 6)
    # umbrella
    c.line([(150, 330), (150, 600)], "#7a5a3a", 5)
    for i in range(8):
        a0, a1 = 180 + i * 22.5, 180 + (i + 1) * 22.5
        c.pieslice((20, 280, 280, 400), a0, a1, fill=["#ff5f7a", "#fff1d0"][i % 2])
    # sign
    c.rect((1180, 360, 1186, 470), fill="#555555")
    c.rect((1130, 350, 1240, 410), fill="#ffffff", outline="#cc2222", width=3)
    c.text((1185, 380), "NO DIVING\nNO PHOTOS\nNO PANIC", 10, "#cc2222", font="cond", spacing=2)
    c.save(os.path.join(OUT, "pool.png"))


def bg_hallway(name="hallway.png", seed=1):
    c = Canvas(W, H)
    vx, vy = W / 2, 330
    # ceiling
    c.poly([(0, 0), (W, 0), (vx + 90, vy - 70), (vx - 90, vy - 70)], fill="#1a0f22")
    # walls
    c.poly([(0, 0), (vx - 90, vy - 70), (vx - 90, vy + 70), (0, H)], fill="#3a1d3e")
    c.poly([(W, 0), (vx + 90, vy - 70), (vx + 90, vy + 70), (W, H)], fill="#341a3a")
    # end wall
    c.rect((vx - 90, vy - 70, vx + 90, vy + 70), fill="#24112c")
    c.neon_text((vx, vy - 30), "EXIT?", 18, "#ff4a4a")
    c.text((vx, vy + 20), "→ BALLROOM\n← ICE MACHINE", 10, col("#d0b0e0", 220), font="cond")
    # carpet
    c.poly([(0, H), (vx - 90, vy + 70), (vx + 90, vy + 70), (W, H)], fill="#6b1f3a")
    R = rng(seed)
    for t in [i / 18 for i in range(1, 18)]:
        y = vy + 70 + (H - vy - 70) * (t ** 1.8)
        xl = vx - 90 - (vx - 90) * (t ** 1.8)
        xr = vx + 90 + (W - vx - 90) * (t ** 1.8)
        c.line([(xl, y), (xr, y)], "#a83a5c", 1 + 3 * t)
    for i in range(-6, 7):
        c.line([(vx + i * 14, vy + 70), (vx + i * 130, H)], "#8a2a4c", 2)
    # doors along walls
    lights = [PINK, CYAN, GOLD, VIOLET, LIME]
    for k, t in enumerate([0.08, 0.32, 0.52, 0.68]):
        s = 1 - t
        for side in (-1, 1):
            if side < 0:
                x = (vx - 90) * t + 10 * s
                xw = (vx - 90) * (t + 0.11) - x
            else:
                x2 = W - (W - vx - 90) * t - 10 * s
                xw = (W - vx - 90) * 0.11 * 1.0
                x = x2 - xw
            top = vy - 70 - (vy - 70) * s * 0.75
            bot = vy + 70 + (H - vy - 70) * s * 0.85
            lit = R.random() < 0.7
            colr = R.choice(lights)
            c.rect((x, top, x + xw, bot), fill="#5a2a4a")
            c.rect((x + xw * 0.15, top + (bot - top) * 0.1, x + xw * 0.85, top + (bot - top) * 0.45), outline="#3a1430", width=2)
            if lit:
                edge = x + xw if side < 0 else x
                c.rect((edge - 4, top, edge + 4, bot), fill=col(colr, 220), blur=4)
                c.poly([(edge, bot), (edge + side * -90 * s, bot + 30 * s), (edge - side * -10, bot + 40 * s)], fill=col(colr, 60), blur=10)
            c.text((x + xw / 2, top - 10 * s - 4), str(300 + k * 2 + (side > 0)), 8 + 10 * s, "#e8c98a", font="serif")
    # ceiling lights
    for t in (0.15, 0.45, 0.7):
        y = (vy - 70) * t
        c.ell((vx - 40 * (1 - t) - 20, y + 10, vx + 40 * (1 - t) + 20, y + 24), fill="#ffe7b0")
        c.ell((vx - 140, y - 20, vx + 140, y + 60), fill=col("#ffd38a", 40), blur=20)
    # neon arrow on left wall
    c.neon_line([(70, 200), (210, 230)], PINK, 3)
    c.neon_line([(210, 230), (190, 210)], PINK, 3)
    c.neon_line([(210, 230), (185, 245)], PINK, 3)
    c.text((140, 250), "art this way", 14, "#ffd0ea", font="sans")
    c.vignette(170)
    c.save(os.path.join(OUT, name))


def bg_room404():
    c = Canvas(W, H, "#e9ecf2")
    c.rect((0, 520, W, H), fill="#c8ccd6")
    R = rng(4)
    # glitch bands
    for i in range(20):
        y = R.uniform(0, H)
        c.rect((0, y, W, y + R.uniform(2, 10)), fill=col(R.choice([CYAN, PINK, "#40ff80"]), 70))
    c.text((640, 170), "404", 170, "#1d2b6b", font="bold", glow="#5ae6ff")
    c.text((640, 280), "ROOM NOT FOUND", 40, "#1d2b6b", font="mono")
    c.text((640, 320), "the room you are standing in does not exist", 18, "#4a5592", font="mono")
    for (x, y, w, h, t) in [(120, 380, 300, 130, "ERROR\nFeeling not found.\n[ OK ]   [ ALSO OK ]"),
                            (880, 360, 320, 140, "WARNING\nVibes exceed buffer.\nRetry?  Y / Y"),
                            (480, 420, 330, 150, "Are you sure you\nwant to be here?\n[ YES ]   [ ALSO YES ]")]:
        c.rect((x + 8, y + 8, x + w + 8, y + h + 8), fill=col("#000000", 50), blur=6)
        c.rect((x, y, x + w, y + h), fill="#f6f6f6", outline="#1d2b6b", width=2)
        c.rect((x, y, x + w, y + 26), fill="#1d2b6b")
        c.text((x + w - 16, y + 13), "x", 14, "#ffffff", font="mono")
        c.text((x + w / 2, y + 26 + (h - 26) / 2), t, 15, "#1d2b6b", font="mono", spacing=6)
    for (x, y) in [(230, 130), (1010, 600), (700, 640), (1100, 210)]:
        c.poly([(x, y), (x, y + 34), (x + 9, y + 26), (x + 16, y + 40), (x + 21, y + 37), (x + 14, y + 23), (x + 25, y + 23)], fill="#ffffff", outline="#000000", width=2)
    c.save(os.path.join(OUT, "room404.png"))


def bg_lostfound():
    c = Canvas(W, H, "#2a1a14")
    wallpaper_stripes(c, (0, 0, W, 560), "#5a3a2a", "#523426", 40)
    c.radial(640, 120, 520, col("#ffcf7a", 120))
    labels = ["MISPLACED\nCONFIDENCE", "UNCLAIMED\nAPOLOGIES", "SPARE\nEXCUSES", "ONE (1)\nCOURAGE",
              "LOST\nWEEKENDS", "OLD\nNICKNAMES", "BORROWED\nCOURAGE", "UNSENT\nTEXTS",
              "FIRST\nIMPRESSIONS", "LEFT\nSOCKS", "SECOND\nCHANCES", "MISC.\nFEELINGS"]
    i = 0
    for row in range(3):
        y = 110 + row * 140
        c.rect((90, y + 100, 1190, y + 112), fill="#3a2214")
        for k in range(4):
            x = 120 + k * 270
            c.rect((x, y + 20, x + 220, y + 100), fill=["#c8a070", "#9fb7c8", "#c890a0", "#a8c090"][(k + row) % 4])
            c.rect((x + 40, y + 34, x + 180, y + 86), fill="#f4ecd8")
            c.text((x + 110, y + 60), labels[i], 12, "#3a2214", font="cond", spacing=1)
            i += 1
    c.rect((0, 560, W, H), fill="#3a2418")
    c.rect((360, 540, 920, 640), fill="#6b4226")
    c.rect((350, 530, 930, 548), fill="#8a5a36")
    c.ell((600, 500, 680, 534), fill="#d84a4a")
    c.text((640, 518), "TAKE ONE\nLEAVE ONE", 9, "#ffffff", font="cond", spacing=0)
    c.vignette(140)
    c.save(os.path.join(OUT, "lostfound.png"))


def bg_regen():
    c = Canvas(W, H)
    c.vgrad((0, 0, W, H), "#031a3a", "#06061a")
    for k in range(14):
        pts = []
        for x in range(0, W + 20, 20):
            pts.append((x, 60 + k * 50 + math.sin(x / 90 + k) * 18))
        c.line(pts, col(CYAN, 40), 6, blur=6)
    R = rng(6)
    for _ in range(60):
        x, y, r = R.uniform(0, W), R.uniform(0, H), R.uniform(3, 12)
        c.circle(x, y, r, outline=col("#bff6ff", 140), width=1)
    for x in (80, 260, 1040, 1200):
        for j in range(5):
            pts = [(x + j * 10 + math.sin(t / 3) * 14, 720 - t * 18) for t in range(18 + j * 2)]
            c.line(pts, col(LIME, 160), 5, blur=2)
    c.ell((300, 540, 980, 680), fill="#16244e")
    c.ell((320, 530, 960, 650), fill="#20367a")
    for i in range(4):
        c.arc((360 + i * 20, 550 + i * 6, 920 - i * 20, 630 - i * 6), 190, 350, col("#7fe6ff", 120), 2)
    c.neon_text((640, 80), "THE REGENERATION TANK", 30, CYAN)
    c.text((640, 120), "lie down. grow something back.", 16, "#9fe6ff", font="sans")
    c.save(os.path.join(OUT, "regen.png"))


def bg_breakfast():
    c = Canvas(W, H)
    c.vgrad((0, 0, W, H), "#3a1508", "#140804")
    for x in (120, 1160):
        c.rect((x - 4, 60, x + 4, 520), fill="#555555")
    c.poly([(30, 70), (380, 70), (380, 330), (205, 290), (30, 330)], fill="#1a1a1a")
    c.text((205, 150), "CHURCH OF\nCAST IRON", 30, "#e0e0e0", font="serif", spacing=8)
    c.text((205, 250), "seasoned. eternal.", 16, "#aaaaaa", font="sans")
    c.poly([(900, 70), (1250, 70), (1250, 330), (1075, 290), (900, 330)], fill="#f2f2f2")
    c.text((1075, 150), "TEMPLE OF\nTEFLON", 30, "#c03030", font="serif", spacing=8)
    c.text((1075, 250), "nothing sticks to us.", 16, "#c06060", font="sans")
    # altar
    c.rect((440, 430, 840, 600), fill="#5a2a14")
    c.rect((420, 415, 860, 440), fill="#7a3a1a")
    c.radial(640, 330, 260, col(GOLD, 120))
    c.ell((520, 280, 760, 400), fill="#222222")
    c.ell((540, 290, 740, 385), fill="#333333")
    c.line([(740, 340), (860, 300)], "#222222", 18)
    c.ell((590, 310, 690, 365), fill="#ffffff")
    c.circle(640, 336, 20, fill="#ffbf1a")
    c.neon_text((640, 230), "THE HOLY SKILLET", 22, GOLD)
    for x in range(470, 820, 70):
        c.rect((x, 380, x + 10, 415), fill="#f6e8c0")
        c.circle(x + 5, 374, 5, fill="#ffcc55")
        c.circle(x + 5, 374, 14, fill=col("#ffaa33", 90), blur=6)
    c.rect((0, 600, W, H), fill="#241008")
    c.vignette(170)
    c.save(os.path.join(OUT, "breakfast.png"))


def bg_forest():
    c = Canvas(W, H)
    c.vgrad((0, 0, W, H), "#0b1f1a", "#04100c")
    R = rng(8)
    for i in range(18):
        x = R.uniform(-40, W)
        w = R.uniform(30, 90)
        shade = R.choice(["#14291f", "#1b3527", "#0f2018"])
        c.rect((x, 0, x + w, H), fill=shade)
        for b in range(4):
            y = R.uniform(40, 400)
            c.line([(x + w / 2, y), (x + w / 2 + R.choice([-1, 1]) * R.uniform(60, 140), y - R.uniform(20, 80))], shade, w * 0.18)
    c.rect((0, 0, W, 90), fill=col("#000000", 120))
    # hotel lamp + bed under moss
    c.ell((780, 470, 1180, 610), fill="#2f5a2a")
    c.rect((800, 470, 1160, 560), fill="#3f7a35", r=30)
    c.rect((1100, 300, 1108, 470), fill="#7a6040")
    c.poly([(1060, 260), (1150, 260), (1130, 310), (1080, 310)], fill="#e8d8a0")
    c.radial(1104, 300, 160, col("#ffe0a0", 110))
    # moss floor
    c.vgrad((0, 560, W, H), "#2d5a26", "#1a3a16")
    for _ in range(300):
        x, y = R.uniform(0, W), R.uniform(560, H)
        c.circle(x, y, R.uniform(2, 7), fill=R.choice(["#3f7a35", "#2a5022", "#4f8a3a"]))
    # fog
    for k in range(4):
        c.ell((-200 + k * 380, 470, 380 + k * 380, 640), fill=col("#cfe8e0", 50), blur=30)
    # fireflies
    for _ in range(40):
        x, y = R.uniform(0, W), R.uniform(80, 560)
        c.circle(x, y, 8, fill=col("#e8ff8a", 90), blur=4)
        c.circle(x, y, 2, fill="#fbffd0")
    c.text((200, 60), "ROOM 312", 16, col("#d8e8c0", 200), font="serif")
    c.vignette(170)
    c.save(os.path.join(OUT, "forest.png"))


def bg_cryptid():
    c = Canvas(W, H, "#d8d0b8")
    c.rect((0, 0, W, 470), fill="#c9c0a6")
    c.rect((0, 460, W, H), fill="#8a7a5a")
    for x in range(0, W, 60):
        for y in range(470, H, 60):
            if (x // 60 + y // 60) % 2:
                c.rect((x, y, x + 60, y + 60), fill="#7a6b4c")
    c.rect((180, 50, 1100, 130), fill="#2a5a8a")
    c.text((640, 78), "CRYPTIDS ANONYMOUS", 34, "#ffffff", font="bold")
    c.text((640, 113), "you are not blurry here", 18, "#cfe4ff", font="sans")
    # fluorescent light
    c.rect((500, 0, 780, 14), fill="#f4fff4")
    c.radial(640, 10, 400, col("#f4fff0", 80))
    # coffee urn table
    c.rect((60, 330, 300, 460), fill="#6b5034")
    c.rect((50, 320, 310, 336), fill="#8a6a44")
    c.rect((110, 230, 180, 320), fill="#b0b8c0", r=10)
    c.rect((132, 290, 158, 304), fill="#333333")
    for x in (210, 245):
        c.rect((x, 290, x + 25, 320), fill="#ffffff")
    # circle of folding chairs
    for i in range(7):
        a = math.pi * (0.15 + 0.7 * i / 6)
        x = 640 - math.cos(a) * 420
        y = 560 - math.sin(a) * 90
        s = 0.8 + 0.3 * (y - 470) / 100
        c.rect((x - 26 * s, y - 70 * s, x + 26 * s, y - 20 * s), fill="#5a6a7a")
        c.rect((x - 30 * s, y - 20 * s, x + 30 * s, y - 8 * s), fill="#6b7b8b")
        c.line([(x - 26 * s, y - 8 * s), (x - 30 * s, y + 40 * s)], "#3a4652", 4)
        c.line([(x + 26 * s, y - 8 * s), (x + 30 * s, y + 40 * s)], "#3a4652", 4)
    # inflatable nessie
    nx, ny = 1060, 420
    for k, r in enumerate((40, 32, 26)):
        c.ell((nx - 120 + k * 70, ny - r, nx - 120 + k * 70 + r * 2.2, ny + r), fill="#3fae6a")
    c.line([(nx + 70, ny), (nx + 110, ny - 120), (nx + 140, ny - 130)], "#3fae6a", 26)
    c.circle(nx + 140, ny - 132, 22, fill="#3fae6a")
    c.circle(nx + 148, ny - 138, 4, fill="#111111")
    c.text((nx + 30, ny + 60), "HELLO MY NAME IS: Nessie (inflatable)", 10, "#2a2a2a", font="cond")
    # mothman poster
    c.rect((960, 160, 1110, 300), fill="#1a1a1a")
    c.poly([(1035, 190), (975, 270), (1035, 250), (1095, 270)], fill="#5a3a3a")
    c.circle(1022, 210, 5, fill="#ff2a2a")
    c.circle(1048, 210, 5, fill="#ff2a2a")
    c.text((1035, 288), "BELIEVE IN YOURSELF", 9, "#ffffff", font="cond")
    c.save(os.path.join(OUT, "cryptid.png"))


def bg_exchange():
    c = Canvas(W, H)
    c.vgrad((0, 0, W, H), "#0a0a14", "#14081e")
    R = rng(12)
    tickers = ["SELF ▲4.2", "VIBES ▼1.1", "HUGS ▲12", "SHAME ▼33", "AURA ▲0.8", "NAPS ▲7.7",
               "EGO ▼5.0", "FOMO ▼2.2", "TEA ▲3.3", "GLITTER ▲99", "SOCKS ▼0.1", "YOU ▲∞"]
    for row in range(3):
        y = 60 + row * 54
        c.rect((0, y, W, y + 44), fill="#05050a")
        x = -R.uniform(0, 200)
        while x < W:
            t = R.choice(tickers)
            colr = "#40ff7a" if "▲" in t else "#ff4a5a"
            c.text((x, y + 22), t, 22, colr, font="mono", anchor="lm", glow=colr)
            x += len(t) * 15 + 60
    # trading floor desk
    c.rect((300, 400, 980, 560), fill="#22222e")
    c.rect((290, 390, 990, 410), fill="#3a3a4a")
    for k in range(4):
        x = 330 + k * 165
        c.rect((x, 300, x + 140, 390), fill="#101018")
        pts = [(x + 10 + i * 12, 370 - R.uniform(0, 60)) for i in range(11)]
        c.line(pts, R.choice(["#40ff7a", "#ff4a5a"]), 3)
    c.neon_text((640, 250), "HUMAN STOCK EXCHANGE", 34, GOLD)
    c.text((640, 600), "BUY LOW  •  FEEL HIGH  •  NO REFUNDS", 18, "#f0d090", font="cond")
    for _ in range(120):
        x, y = R.uniform(0, W), R.uniform(220, H)
        c.rect((x, y, x + 6, y + 10), fill=R.choice([PINK, GOLD, CYAN, LIME]))
    c.vignette(160)
    c.save(os.path.join(OUT, "exchange.png"))


def bg_karaoke():
    c = Canvas(W, H, "#120818")
    for x in range(0, W, 40):
        c.rect((x, 0, x + 26, H), fill="#3a0d2a")
        c.rect((x + 26, 0, x + 40, H), fill="#2a0820")
    c.rect((0, 520, W, H), fill="#1a0a1c")
    c.radial(640, 520, 380, col(VIOLET, 120))
    disco_ball(c, 640, 110, 50)
    for a in range(0, 360, 30):
        light_beam(c, 640, 110, a, 700, 2, [PINK, CYAN, GOLD][a // 30 % 3], 30)
    c.rect((420, 210, 860, 450), fill="#050510", r=8)
    c.rect((430, 220, 850, 440), fill="#1c1c64")
    c.text((640, 260), "CONFESSION BOOTH KARAOKE", 18, "#ffffff", font="cond")
    for i, w in enumerate((300, 340, 260, 320)):
        y = 300 + i * 34
        c.rect((640 - w / 2, y, 640 + w / 2, y + 12), fill=col("#ffffff", 120 if i else 230), r=6)
        if i == 0:
            c.rect((640 - w / 2, y, 640 - w / 2 + w * 0.55, y + 12), fill=PINK, r=6)
    c.line([(640, 480), (640, 640)], "#555555", 5)
    c.ell((620, 450, 660, 490), fill="#333333")
    c.neon_text((180, 120), "CONFESS", 40, PINK)
    c.neon_text((1100, 120), "ABSOLVED", 34, CYAN)
    c.vignette(170)
    c.save(os.path.join(OUT, "karaoke.png"))


def bg_ballroom(name="ballroom.png", ark=False):
    c = Canvas(W, H)
    c.vgrad((0, 0, W, H), "#08020f", "#1a0626")
    R = rng(21)
    for i in range(10):
        x = 80 + i * 125
        c.rect((x, 60, x + 30, 520), fill="#1d0d29")
        c.rect((x - 8, 50, x + 38, 70), fill="#2d1838")
    # projections
    for k in range(12):
        cx, cy = R.uniform(100, 1180), R.uniform(80, 420)
        r = R.uniform(30, 90)
        sides = R.choice([3, 4, 6])
        pts = [(cx + math.cos(2 * math.pi * j / sides + k) * r, cy + math.sin(2 * math.pi * j / sides + k) * r) for j in range(sides)]
        c.poly(pts, outline=col(R.choice([PINK, CYAN, LIME, GOLD, VIOLET]), 200), width=3)
    for i in range(14):
        light_beam(c, R.choice([100, 640, 1180]), 0, R.uniform(30, 150), 900, 1.2, R.choice([PINK, CYAN, LIME, VIOLET]), 70)
    disco_ball(c, 640, 120, 60)
    if ark:
        oy = -150
        c.radial(640, 420 + oy, 300, col(GOLD, 160))
        c.rect((500, 330 + oy, 780, 470 + oy), fill="#d9a62a", r=10)
        c.rect((490, 320 + oy, 790, 345 + oy), fill="#f0c650", r=6)
        for j in range(6):
            c.circle(540 + j * 40, 400 + oy, 12, outline="#7a2aa0", width=3)
        c.text((640, 440 + oy), "DON'T PANIC", 24, "#7a1a5a", font="bold")
        for x in (470, 810):  # carrying poles, held aloft
            c.line([(x, 360 + oy), (x, 560)], "#c08a1a", 8)
    crowd(c, 640, 46, seed=4)
    c.rect((0, 680, W, H), fill="#0a0410")
    c.vignette(140)
    c.save(os.path.join(OUT, name))


def bg_livingroom():
    c = Canvas(W, H)
    wallpaper_stripes(c, (0, 0, W, 500), "#e6b98a", "#ddb07f", 22)
    for x in range(30, W, 90):
        for y in range(30, 480, 90):
            c.circle(x + (y // 90 % 2) * 45, y, 7, fill="#c9895a")
    c.radial(300, 280, 380, col("#ffcf80", 150))
    framed(c, (520, 90, 640, 210), inner="#8ab0c8")
    framed(c, (680, 70, 830, 190), inner="#c88aa0")
    framed(c, (870, 110, 960, 220), inner="#a0c88a")
    c.text((750, 230), "BLESS THIS MESS", 16, "#7a3a1a", font="serif")
    # lamp
    c.rect((290, 250, 298, 470), fill="#7a5a30")
    c.poly([(240, 200), (350, 200), (330, 260), (260, 260)], fill="#f2e4b0")
    # rug + floor
    c.rect((0, 500, W, H), fill="#7a4a2a")
    c.ell((180, 540, 1100, 710), fill="#a83a3a")
    c.ell((240, 560, 1040, 690), fill="#c85a3a")
    c.ell((360, 590, 920, 660), fill="#e0a040")
    # rocking chair
    rx, ry = 960, 480
    c.arc((rx - 120, ry + 60, rx + 140, ry + 120), 10, 170, "#5a3a1a", 10)
    c.rect((rx - 90, ry - 150, rx - 70, ry + 80), fill="#6b4220")
    c.rect((rx + 70, ry - 150, rx + 90, ry + 80), fill="#6b4220")
    for k in range(5):
        c.rect((rx - 70, ry - 140 + k * 26, rx + 70, ry - 128 + k * 26), fill="#7a5230")
    c.rect((rx - 95, ry + 10, rx + 95, ry + 30), fill="#7a5230")
    c.rect((rx - 70, ry - 8, rx + 70, ry + 12), fill="#e07a9a", r=6)
    # cushions
    R = rng(3)
    for (x, y) in [(260, 560), (360, 600), (480, 570), (620, 610), (740, 580)]:
        c.rect((x - 50, y - 30, x + 50, y + 30), fill=R.choice(["#7a3aa0", "#3a8aa0", "#e0b040", "#c04a6a"]), r=20)
    # candy bowl
    c.ell((560, 470, 680, 500), fill="#d0f0f0")
    for k in range(10):
        c.circle(575 + k * 10, 478 - (k % 3) * 4, 6, fill=R.choice([PINK, GOLD, LIME, CYAN]))
    c.vignette(110)
    c.save(os.path.join(OUT, "livingroom.png"))


def bg_mission():
    c = Canvas(W, H, "#101418")
    # linen shelves
    for y in (80, 230, 380):
        c.rect((0, y + 110, W, y + 122), fill="#3a3a44")
        R = rng(int(y))
        x = 20
        while x < 330:
            w = R.uniform(40, 70)
            c.rect((x, y + 50, x + w, y + 110), fill=R.choice(["#f2f2f2", "#e0e8f0", "#f0e8e0"]), r=4)
            x += w + 6
    # monitors
    for i, (x, y) in enumerate([(400, 90), (650, 90), (900, 90), (400, 280), (650, 280), (900, 280)]):
        c.rect((x, y, x + 230, y + 160), fill="#05080a", outline="#2a3a44", width=3)
        R = rng(i)
        if i % 3 == 0:
            for gx in range(x + 10, x + 230, 22):
                c.line([(gx, y + 8), (gx, y + 152)], "#0f3a2a", 1)
            for gy in range(y + 10, y + 160, 22):
                c.line([(x + 8, gy), (x + 222, gy)], "#0f3a2a", 1)
            for _ in range(8):
                c.circle(R.uniform(x + 20, x + 210), R.uniform(y + 20, y + 140), 5, fill="#40ff9a")
        elif i % 3 == 1:
            for k in range(7):
                c.text((x + 12, y + 18 + k * 20), R.choice(["RM 312  FOREST  OK", "RM 404  ???  OK", "POOL  CLOSED", "TEA BAR  LOW MILK", "NANA  2 GUESTS", "ICE MACH  STARS", "ARK  STANDBY"]), 11, "#7affc0", font="mono", anchor="lm")
        else:
            c.text((x + 115, y + 80), "11:11", 48, "#ff5a5a", font="mono", glow="#ff2a2a")
    # cue board
    c.rect((400, 470, 1130, 560), fill="#1a2028")
    for k, (lbl, colr) in enumerate([("FOG", CYAN), ("LASERS", PINK), ("ARK", GOLD), ("PANIC", "#555555")]):
        x = 450 + k * 175
        c.circle(x + 30, 515, 28, fill=col(colr, 120), blur=6)
        c.circle(x + 30, 515, 22, fill=colr)
        c.text((x + 100, 515), lbl, 18, "#d8e0e8", font="cond")
    # walkie chargers
    c.rect((1160, 300, 1260, 460), fill="#22262c")
    for k in range(4):
        c.rect((1172 + (k % 2) * 46, 312 + (k // 2) * 70, 1204 + (k % 2) * 46, 372 + (k // 2) * 70), fill="#0a0a0a")
        c.circle(1188 + (k % 2) * 46, 318 + (k // 2) * 70, 3, fill="#40ff40")
    c.rect((0, 580, W, H), fill="#1c2024")
    c.text((1210, 50), "STAFF\nONLY", 20, "#ff5a5a", font="bold")
    c.vignette(150)
    c.save(os.path.join(OUT, "mission.png"))


def bg_roof(name="roof.png", dawn=False):
    c = Canvas(W, H)
    if dawn:
        c.vgrad((0, 0, W, H), None, None, stops=[(0, "#3a3a8a"), (0.4, "#c87ab0"), (0.62, "#ffb08a"), (0.75, "#ffe0a0"), (1, "#ffe0a0")])
        c.circle(900, 470, 140, fill=col("#fff0b0", 160), blur=40)
        c.circle(900, 480, 60, fill="#fff4c8")
        star_field(c, 20, (0, 0, W, 160), seed=3, maxr=1.0)
    else:
        c.vgrad((0, 0, W, H), "#03020c", "#1e1040")
        star_field(c, 320, (0, 0, W, 460), seed=9)
        c.circle(1000, 130, 40, fill=col("#fff6d8", 90), blur=20)
        c.circle(1000, 130, 30, fill="#fff6d8")
    # distant hills + town lights
    c.poly(blob(400, 520, 700, 90, seed=3, amp=0.04, start=math.pi, end=2 * math.pi) + [(1100, 520), (-300, 520)], fill="#2a1a40" if not dawn else "#7a5a8a")
    c.rect((0, 500, W, 540), fill="#1a1028" if not dawn else "#6a4a7a")
    R = rng(5)
    for _ in range(140):
        x, y = R.uniform(0, W), R.uniform(500, 535)
        c.circle(x, y, 1.6, fill=col(R.choice([GOLD, "#ffffff", PINK]), 200 if not dawn else 90))
    # water tank
    c.rect((80, 260, 300, 470), fill="#3a2a2a" if not dawn else "#7a5a5a")
    c.poly([(70, 260), (310, 260), (190, 200)], fill="#2a1a1a" if not dawn else "#6a4a4a")
    for x in (100, 180, 280):
        c.line([(x, 470), (x - 10, 560)], "#2a1a1a", 8)
    # roof floor + parapet
    c.rect((0, 540, W, H), fill="#3a2e3a" if not dawn else "#8a7080")
    c.rect((0, 530, W, 556), fill="#4a3a4a" if not dawn else "#9a8090")
    string_lights(c, 330, 330, 1280, 360, sag=60, seed=8)
    # rigging for the ark
    c.line([(700, 0), (760, 540)], "#8a8a9a", 3)
    c.line([(1260, 0), (1120, 540)], "#8a8a9a", 3)
    c.rect((740, 520, 1150, 560), fill="#555060")
    c.rect((560, 590, 760, 640), fill="#6a4a3a")  # bench
    c.rect((570, 640, 584, 680), fill="#4a3a2a")
    c.rect((736, 640, 750, 680), fill="#4a3a2a")
    c.save(os.path.join(OUT, name))


def bg_fortune():
    c = Canvas(W, H)
    c.vgrad((0, 0, W, H), "#1a0838", "#090212")
    star_field(c, 80, (0, 0, W, 300), seed=2, color="#d0b0ff")
    c.rect((0, 540, W, H), fill="#14082a")
    # robot
    rx, ry = 380, 300
    c.radial(rx, ry + 60, 260, col(VIOLET, 120))
    c.rect((rx - 110, ry, rx + 110, ry + 240), fill="#9aa0b8", r=16)
    c.rect((rx - 90, ry + 30, rx + 90, ry + 110), fill="#101420", r=8)
    c.text((rx, ry + 70), "◉ ◉", 34, "#5affd0", font="sans", glow="#2affb0")
    c.ell((rx - 70, ry - 90, rx + 70, ry + 20), fill=col("#bfe8ff", 120), outline="#c0c8e0", width=3)
    c.circle(rx, ry - 40, 22, fill="#ff5fb8")
    c.circle(rx, ry - 40, 40, fill=col(PINK, 80), blur=10)
    c.rect((rx - 40, ry + 140, rx + 40, ry + 156), fill="#202020")
    c.text((rx, ry + 200), "FORTUNES 1¢\n(you are the cent)", 14, "#202030", font="cond")
    for k in range(3):
        c.circle(rx - 20 + k * 22, ry + 172, 9, fill="#ffffff")
    # lottery machine
    lx, ly = 900, 350
    c.rect((lx - 20, ly + 120, lx + 20, ly + 200), fill="#c0a040")
    c.rect((lx - 90, ly + 190, lx + 90, ly + 220), fill="#c0a040")
    c.circle(lx, ly, 140, fill=col("#d8f0ff", 60), outline="#e0f0ff", width=4)
    R = rng(4)
    for _ in range(36):
        a, r = R.uniform(0, 2 * math.pi), R.uniform(0, 120)
        c.circle(lx + math.cos(a) * r, ly + math.sin(a) * r * 0.9 + 20, 13, fill="#ffffff", outline="#c0c0c0", width=1)
    # capes on hooks
    for k, cc in enumerate(["#7a1a3a", "#1a3a7a", "#3a7a1a", "#7a5a1a"]):
        x = 1120 + (k % 2) * 70
        y = 120 + (k // 2) * 200
        c.circle(x, y, 6, fill="#cccccc")
        c.poly([(x - 10, y + 6), (x + 10, y + 6), (x + 40, y + 170), (x - 40, y + 170)], fill=cc)
    c.neon_text((640, 70), "THE ORACLE OF PING PONG", 30, VIOLET)
    c.vignette(150)
    c.save(os.path.join(OUT, "fortune.png"))


def bg_clinic():
    c = Canvas(W, H, "#bfe0cc")
    for x in range(0, W, 40):
        c.line([(x, 0), (x, 520)], "#a8ccb8", 2)
    for y in range(0, 520, 40):
        c.line([(0, y), (W, y)], "#a8ccb8", 2)
    c.rect((0, 520, W, H), fill="#e8ece8")
    for x in range(0, W, 80):
        c.line([(x, 520), (x - 30, H)], "#cfd6cf", 2)
    c.rect((200, 40, 1080, 110), fill="#ffffff", outline="#2a7a5a", width=4)
    c.text((640, 75), "CLINIC OF UNNECESSARY PROCEDURES", 30, "#2a7a5a", font="bold")
    # eye chart with symbols
    c.rect((90, 150, 290, 450), fill="#ffffff", outline="#888888", width=2)
    rows = ["☾", "✶ ♒", "☿ ♄ ✷", "♎ ☉ ⚘ ✦", "∞ ⚚ ☊ ♆ ✿"]
    for i, r in enumerate(rows):
        c.text((190, 190 + i * 54), r, 40 - i * 6, "#111111", font="sans")
    # exam table
    c.rect((470, 410, 900, 450), fill="#c8ccd2")
    c.rect((480, 380, 890, 412), fill="#3a8ac8", r=8)
    c.rect((500, 450, 520, 560), fill="#888888")
    c.rect((850, 450, 870, 560), fill="#888888")
    c.rect((480, 372, 890, 386), fill="#f2f2f2")
    # curtain
    c.line([(960, 130), (1260, 130)], "#888888", 4)
    for k in range(9):
        x = 970 + k * 32
        c.poly([(x, 132), (x + 32, 132), (x + 40, 560), (x - 6, 560)], fill=["#f4a8c8", "#f8c0d8"][k % 2])
    # stethoscope on hook + aura chart
    c.rect((600, 160, 820, 330), fill="#ffffff", outline="#888888", width=2)
    c.text((710, 180), "YOUR AURA", 16, "#333333", font="cond")
    for k, cc in enumerate([PINK, GOLD, LIME, CYAN, VIOLET]):
        c.circle(710, 260, 60 - k * 11, fill=cc)
    c.save(os.path.join(OUT, "clinic.png"))


def bg_planetarium():
    c = Canvas(W, H)
    c.vgrad((0, 0, W, H), "#020414", "#070a26")
    star_field(c, 500, (0, 0, W, 560), seed=13, color="#dfe8ff", maxr=2.0)
    R = rng(14)
    for k in range(5):
        pts = [(R.uniform(100, 1180), R.uniform(40, 420)) for _ in range(5)]
        pts.sort()
        c.line(pts, col("#9fd8ff", 110), 1.5)
        for p in pts:
            c.circle(p[0], p[1], 3.5, fill="#ffffff")
            c.circle(p[0], p[1], 10, fill=col("#9fd8ff", 80), blur=5)
    # a nebula
    c.circle(900, 200, 180, fill=col(VIOLET, 50), blur=60)
    c.circle(980, 260, 120, fill=col(PINK, 40), blur=50)
    # ice machine
    ix, iy = 640, 470
    c.radial(ix, iy, 300, col("#7ad8ff", 120))
    c.rect((ix - 120, iy - 120, ix + 120, iy + 180), fill="#c8d4e0", r=10)
    c.rect((ix - 100, iy - 100, ix + 100, iy - 30), fill="#2a6aa8")
    c.neon_text((ix, iy - 65), "ICE", 40, "#7ad8ff")
    c.rect((ix - 60, iy + 10, ix + 60, iy + 120), fill="#1a2a3a", r=6)
    c.circle(ix, iy + 65, 30, fill="#c8f0ff", blur=6)
    c.line([(ix, iy + 65), (ix - 300, 120)], col("#c8f0ff", 60), 40, blur=20)
    c.line([(ix, iy + 65), (ix + 280, 80)], col("#c8f0ff", 50), 40, blur=20)
    c.rect((0, 650, W, H), fill="#0a0c1a")
    c.text((640, 690), "the ice machine dreams of the cold between stars", 14, "#7a8ac0", font="sans")
    c.save(os.path.join(OUT, "planetarium.png"))


def bg_bedroom():
    c = Canvas(W, H)
    c.rect((0, 0, W, H), fill="#f0d8b8")
    c.rect((0, 0, W, 40), fill="#e0c8a8")
    # window with morning light
    c.rect((780, 90, 1140, 380), fill="#ffe8b8")
    c.rect((790, 100, 1130, 370), fill=None, outline="#a07a50", width=6)
    c.line([(960, 100), (960, 370)], "#a07a50", 6)
    c.line([(790, 235), (1130, 235)], "#a07a50", 6)
    c.vgrad((796, 106, 1124, 364), "#9fd0ff", "#ffe0b0")
    c.poly([(780, 380), (1140, 380), (900, 720), (360, 720)], fill=col("#fff4d0", 80), blur=20)
    c.rect((760, 70, 800, 420), fill="#c84a5a")
    c.rect((1120, 70, 1160, 420), fill="#c84a5a")
    # bed
    c.rect((60, 360, 640, 600), fill="#e8e8f0", r=20)
    c.rect((40, 280, 90, 620), fill="#7a4a2a")
    c.rect((90, 380, 260, 450), fill="#ffffff", r=20)
    c.rect((60, 470, 640, 600), fill="#7a5ab0", r=16)
    c.rect((0, 600, W, H), fill="#7a3a3a")
    # newspaper under door
    c.poly([(840, 640), (1120, 610), (1150, 700), (860, 718)], fill="#f2efe2")
    c.text((990, 646), "THE DAILY DISTURBANCE", 13, "#222222", font="serif")
    c.line([(870, 668), (1120, 642)], "#888888", 2)
    c.line([(872, 682), (1126, 656)], "#888888", 2)
    c.line([(874, 696), (1130, 670)], "#888888", 2)
    framed(c, (300, 120, 500, 260), inner="#5aa0b0")
    c.save(os.path.join(OUT, "bedroom.png"))


def bg_main_menu():
    """Main/game menu art lives in game/gui/."""
    import shutil
    bg_exterior_night("exterior_night.png")
    gui = os.path.join(OUT, "..", "..", "gui")
    shutil.copy(os.path.join(OUT, "exterior_night.png"), os.path.join(gui, "main_menu.png"))
    from PIL import Image, ImageFilter
    im = Image.open(os.path.join(OUT, "exterior_night.png")).convert("RGB").filter(ImageFilter.GaussianBlur(8))
    im.save(os.path.join(gui, "game_menu.png"))


SCENES = {
    "exterior": bg_exterior, "exterior_night": bg_exterior_night, "lobby": bg_lobby, "pool": bg_pool,
    "hallway": bg_hallway, "room404": bg_room404, "lostfound": bg_lostfound, "regen": bg_regen,
    "breakfast": bg_breakfast, "forest": bg_forest, "cryptid": bg_cryptid, "exchange": bg_exchange,
    "karaoke": bg_karaoke, "ballroom": bg_ballroom,
    "ballroom_ark": lambda: bg_ballroom("ballroom_ark.png", ark=True),
    "livingroom": bg_livingroom, "mission": bg_mission, "roof": bg_roof,
    "roof_dawn": lambda: bg_roof("roof_dawn.png", dawn=True),
    "main_menu": bg_main_menu, "fortune": bg_fortune, "clinic": bg_clinic, "planetarium": bg_planetarium, "bedroom": bg_bedroom,
}

if __name__ == "__main__":
    names = sys.argv[1:] or list(SCENES)
    for n in names:
        SCENES[n]()
        print("painted", n)
