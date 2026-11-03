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
    c.rect((540, 20, 760, 66), fill="#f4e4c8", outline="#7a3a1a", width=3, r=10)
    c.text((650, 43), "THE COZY", 24, "#7a3a1a", font="serif")
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


# ---------------------------------------------------------------- art-room encounters
def bg_penguinpost():
    c = Canvas(W, H)
    c.vgrad((0, 0, W, H), "#0b1440", "#1c2f6b")
    # icy back wall with neon
    for i in range(14):
        x = i * 100 - 20
        c.poly([(x, 0), (x + 120, 0), (x + 90, 420), (x + 10, 420)], fill=col(["#9fd8ff", "#c8ecff", "#7fb8f0"][i % 3], 70))
    c.rect((0, 400, W, 430), fill="#d8f0ff")
    for x in range(0, W, 60):  # icicles along the top
        c.poly([(x, 0), (x + 30, 0), (x + 15, 40 + (x // 60 % 3) * 18)], fill="#e8f8ff")
    c.neon_text((640, 90), "PENGUIN POST", 52, PINK)
    c.neon_text((640, 150), "PLEASE TAKE A NUMBER", 20, CYAN)
    # NOW SERVING display
    c.rect((960, 190, 1180, 270), fill="#05060c", r=8)
    c.text((1070, 212), "NOW SERVING", 14, "#ffcf5a", font="mono")
    c.text((1070, 246), "3", 34, "#ff5a5a", font="mono", glow="#ff2a2a")
    # counter
    c.rect((300, 330, 980, 470), fill="#e8f4ff")
    c.rect((290, 318, 990, 336), fill="#ffffff")
    c.rect((300, 470, 980, 478), fill=col(CYAN, 160), blur=3)
    for k, x in enumerate((420, 640, 860)):  # penguins behind the counter
        c.ell((x - 46, 220, x + 46, 336), fill="#14141c")
        c.ell((x - 30, 250, x + 30, 336), fill="#f4f4f8")
        c.circle(x - 13, 248, 5, fill="#ffffff"); c.circle(x + 13, 248, 5, fill="#ffffff")
        c.circle(x - 13, 249, 2.5, fill="#111111"); c.circle(x + 13, 249, 2.5, fill="#111111")
        c.poly([(x - 8, 262), (x + 8, 262), (x, 274)], fill="#ffb02a")
        c.rect((x - 26, 204, x + 26, 222), fill="#1d3a8a", r=4)
        c.rect((x - 30, 218, x + 30, 224), fill="#1d3a8a")
    # mailboxes left, parcels right
    for r in range(3):
        for k in range(3):
            c.rect((60 + k * 62, 200 + r * 62, 112 + k * 62, 252 + r * 62), fill="#3a5ab0", outline="#9fd8ff", width=2)
            c.circle(100 + k * 62, 226 + r * 62, 4, fill="#ffcf5a")
    for (x, y, w, h, cc) in [(1040, 330, 90, 70, "#c89a5a"), (1120, 350, 70, 50, "#d8aa6a"), (1060, 290, 60, 42, "#b88a4a")]:
        c.rect((x, y, x + w, y + h), fill=cc)
        c.line([(x + w / 2, y), (x + w / 2, y + h)], "#8a5a2a", 3)
    # snowy floor
    c.vgrad((0, 478, W, H), "#cfe8ff", "#9cc8f0")
    R = rng(31)
    for _ in range(160):
        c.circle(R.uniform(0, W), R.uniform(0, H), R.uniform(1, 2.6), fill=col("#ffffff", R.randint(120, 230)))
    c.vignette(120)
    c.save(os.path.join(OUT, "penguinpost.png"))


def fan(c, x, y, r, blade="#d8e0ec", hub="#5a6a80", spin=0):
    c.circle(x, y, r + 6, outline="#8a9ab0", width=3)
    for k in range(4):
        a = math.radians(spin + k * 90)
        c.ell((x + math.cos(a) * r * 0.55 - r * 0.32, y + math.sin(a) * r * 0.55 - r * 0.32,
               x + math.cos(a) * r * 0.55 + r * 0.32, y + math.sin(a) * r * 0.55 + r * 0.32), fill=blade)
    c.circle(x, y, r * 0.2, fill=hub)
    for k in range(-r, r + 1, 9):
        c.line([(x + k, y - math.sqrt(max(0, r * r - k * k))), (x + k, y + math.sqrt(max(0, r * r - k * k)))], col("#8a9ab0", 90), 1)


def bg_fanbar():
    c = Canvas(W, H)
    c.vgrad((0, 0, W, H), "#bfe8f4", "#7fc4dc")
    for x in range(0, W, 90):
        c.rect((x, 0, x + 45, 520), fill=col("#ffffff", 40))
    # breeze lines
    R = rng(7)
    for _ in range(30):
        y = R.uniform(40, 500); x = R.uniform(0, W - 200)
        c.arc((x, y, x + R.uniform(120, 260), y + 30), 200, 340, col("#ffffff", 150), 2)
    c.rect((300, 40, 980, 110), fill="#ffffff", r=10)
    c.text((640, 75), "PLEASE SUBSCRIBE!!", 40, PINK, font="bold")
    c.rect((40, 150, 260, 230), fill="#fff4b0", r=6)
    c.text((150, 190), "FOR SUBSCRIBERS\nONLY!", 18, "#c03060", font="bold", spacing=4)
    # wall of fans
    for (x, y, r, s) in [(120, 330, 70, 0), (1150, 300, 80, 20), (1000, 170, 50, 45), (300, 200, 45, 10),
                         (980, 360, 60, 30), (210, 470, 55, 15)]:
        fan(c, x, y, r, spin=s)
    # Fanny Bar counter
    c.rect((430, 380, 850, 500), fill="#ff8fc0", r=8)
    c.rect((420, 366, 860, 386), fill="#ffd0e6", r=6)
    c.neon_text((640, 270), "FANNY BAR", 32, PINK)
    for x in (480, 560, 720, 800):
        c.rect((x - 12, 330, x + 12, 366), fill=col("#ffffff", 200), r=6)
        c.rect((x - 6, 320, x + 6, 332), fill="#c0c8d8")
    # Nutbuster booth
    c.rect((1110, 420, 1270, 620), fill="#1a3a8a")
    c.rect((1110, 400, 1270, 440), fill="#ffd21a")
    c.text((1190, 420), "NUTBUSTER", 18, "#1a3a8a", font="bold")
    c.rect((1130, 460, 1250, 620), fill="#0a1a4a")
    c.rect((0, 520, W, H), fill="#e8dcc8")
    c.vignette(90)
    c.save(os.path.join(OUT, "fanbar.png"))


def bg_tentacletopia():
    c = Canvas(W, H)
    c.vgrad((0, 0, W, H), "#063a5a", "#021428")
    # light rays
    for i in range(6):
        x = 120 + i * 220
        c.poly([(x, 0), (x + 60, 0), (x + 220, 720), (x + 80, 720)], fill=col("#9fe8ff", 22), blur=12)
    # sunken art-deco towers
    for (x, w, h, sign, cc) in [(140, 180, 380, "OCEAN", PINK), (900, 220, 430, "HOTEL", CYAN), (1150, 120, 300, None, None)]:
        top = 560 - h
        c.rect((x, top, x + w, 560), fill="#0c4a5a")
        c.rect((x + w * 0.2, top - 40, x + w * 0.8, top), fill="#0c4a5a")
        c.rect((x + w * 0.4, top - 80, x + w * 0.6, top - 40), fill="#0c4a5a")
        for k in range(int(h / 50)):
            for j in range(3):
                c.rect((x + 20 + j * (w - 40) / 3, top + 20 + k * 50, x + 10 + (j + 1) * (w - 40) / 3, top + 44 + k * 50), fill="#08303c")
        if sign:
            c.neon_text((x + w / 2, top + 40), sign, 22, cc)
    # kelp
    R = rng(41)
    for x in list(range(10, 260, 26)) + list(range(1000, 1280, 30)):
        pts = [(x + math.sin(t / 2.2 + x) * 16, 720 - t * 22) for t in range(int(R.uniform(10, 22)))]
        c.line(pts, R.choice(["#2f8f4e", "#3fa65b", "#58b86a"]), 8)
    # jellyfish
    for (x, y, r, cc) in [(420, 150, 60, "#ff8fe0"), (760, 230, 46, "#b08fff"), (600, 90, 34, "#8fe8ff"), (330, 320, 30, "#ffb0f0")]:
        c.circle(x, y, r * 1.6, fill=col(cc, 50), blur=12)
        c.pieslice((x - r, y - r, x + r, y + r), 180, 360, col(cc, 210))
        for k in range(6):
            tx = x - r * 0.8 + k * r * 0.32
            c.line([(tx + math.sin(j / 1.6 + k) * 6, y + j * 12) for j in range(9)], col(cc, 170), 3)
    # coral wall + sand
    c.vgrad((0, 560, W, H), "#c8a86a", "#8a6a3a")
    for _ in range(26):
        x = R.uniform(300, 980)
        c.circle(x, R.uniform(560, 600), R.uniform(10, 26), fill=R.choice(["#ff7f6a", "#ffb05a", "#e05a8a", "#ff9fb0"]))
    for _ in range(60):
        x, y = R.uniform(0, W), R.uniform(0, 560)
        c.circle(x, y, R.uniform(2, 6), outline=col("#d8f8ff", 140), width=1)
    c.vignette(150)
    c.save(os.path.join(OUT, "tentacletopia.png"))


def bg_optical():
    c = Canvas(W, H)
    c.vgrad((0, 0, W, 520), "#ffb8e0", "#8ae0e8")
    for x in range(0, W, 140):  # palm wallpaper
        for y in (60, 260):
            c.line([(x + 40, y + 120), (x + 50, y)], "#5ac8b0", 4)
            for a in (-60, -20, 20, 60, 100):
                aa = math.radians(a - 90)
                c.line([(x + 50, y), (x + 50 + math.cos(aa) * 40, y + math.sin(aa) * 40 + 10)], "#5ac8b0", 4)
    c.rect((360, 30, 920, 110), fill="#140a28", r=12)
    c.neon_text((640, 70), "ZANY OPTICAL", 44, PINK)
    # giant googly eye
    c.circle(1060, 230, 140, fill="#ffffff", outline="#2a1a3a", width=6)
    c.circle(1090, 270, 70, fill="#111111")
    c.circle(1070, 248, 18, fill="#ffffff")
    # reception iPad
    c.rect((160, 260, 300, 360), fill="#1a1a2a", r=10)
    c.rect((170, 270, 290, 350), fill="#5ae6ff", r=6)
    c.text((230, 300), "◕‿◕", 26, "#141428", font="sans")
    c.rect((222, 360, 238, 430), fill="#8a8aa0")
    # eye chart
    c.rect((440, 150, 580, 360), fill="#ffffff", outline="#2a1a3a", width=3)
    for i, (t, sz) in enumerate([("E", 46), ("F P", 30), ("T O Z", 22), ("L P E D", 16), ("P E C F D", 12)]):
        c.text((510, 186 + i * 36), t, sz, "#141428", font="bold")
    # A/B machine
    c.rect((650, 220, 860, 380), fill="#c8c8d8", r=16)
    c.circle(710, 290, 34, fill="#2a1a3a"); c.circle(800, 290, 34, fill="#2a1a3a")
    c.circle(710, 290, 24, fill="#8ae0ff"); c.circle(800, 290, 24, fill="#ff8fd0")
    c.text((710, 350), "A", 20, "#2a1a3a", font="bold"); c.text((800, 350), "B", 20, "#2a1a3a", font="bold")
    # floor grid
    c.rect((0, 520, W, H), fill="#1a0a2a")
    for x in range(-600, 1900, 90):
        c.line([(640, 520), (x, H)], col(PINK, 140), 2)
    y = 530; step = 6
    while y < H:
        c.line([(0, y), (W, y)], col(CYAN, 140), 2); step *= 1.4; y += step
    c.save(os.path.join(OUT, "optical.png"))


def bg_speeddating():
    c = Canvas(W, H)
    c.vgrad((0, 0, W, H), "#3a1640", "#1c0a24")
    for x in range(60, W, 170):
        c.rect((x, 40, x + 24, 520), fill="#4a2050")
    # chandelier
    c.line([(640, 0), (640, 60)], GOLD, 3)
    for i in range(9):
        x = 560 + i * 20
        c.circle(x, 76 + (i % 2) * 8, 6, fill="#fff0b0")
        c.circle(x, 76, 26, fill=col("#ffe08a", 50), blur=10)
    # banner
    c.rect((290, 120, 990, 200), fill="#ff5fb8", r=10)
    c.text((640, 160), "PLATONIC SPEED DATING", 36, "#ffffff", font="bold")
    # two paddles on the side walls
    for (x, label, cc) in [(170, "THIS", CYAN), (1110, "THAT", GOLD)]:
        c.rect((x - 6, 300, x + 6, 470), fill="#c8a070")
        c.rect((x - 80, 240, x + 80, 330), fill="#ffffff", outline=cc, width=6, r=10)
        c.text((x, 285), label, 34, "#2a1a3a", font="bold")
    # tape line down the middle of the floor
    c.vgrad((0, 520, W, H), "#6a3a2a", "#4a2418")
    c.poly([(632, 520), (648, 520), (690, H), (590, H)], fill="#ffe14d")
    # grab bag
    c.ell((1180, 560, 1260, 640), fill="#c84a4a")
    c.text((1220, 600), "MISSIONS", 9, "#ffffff", font="cond")
    c.vignette(140)
    c.save(os.path.join(OUT, "speeddating.png"))


def bg_letitgo():
    c = Canvas(W, H)
    c.vgrad((0, 0, W, H), "#2a2238", "#141020")
    # stage + projector screen
    c.rect((300, 70, 980, 400), fill="#f4f0e8")
    c.rect((290, 60, 990, 76), fill="#3a3448")
    c.text((640, 160), "LET IT GO", 64, "#2a2238", font="bold")
    c.text((640, 240), "life after the phone", 26, "#7a6a90", font="sans")
    c.rect((560, 290, 720, 370), outline="#2a2238", width=4, r=14)
    c.line([(560, 290), (720, 370)], "#ff5a5a", 6)
    c.rect((220, 420, 1060, 470), fill="#4a3a5a")
    # posterboard slides on an easel
    c.line([(1110, 300), (1080, 520)], "#8a6a40", 6); c.line([(1170, 300), (1200, 520)], "#8a6a40", 6)
    c.rect((1060, 220, 1220, 340), fill="#fffbe8")
    c.text((1140, 280), "STEP 1:\nBREATHE", 18, "#2a2238", font="bold", spacing=4)
    # craft table with emotional support phones
    c.rect((40, 400, 230, 430), fill="#a8784a")
    R = rng(9)
    for k in range(5):
        x = 60 + k * 34
        c.rect((x, 360, x + 24, 400), fill=R.choice([PINK, CYAN, GOLD, VIOLET, LIME]), r=4)
        c.circle(x + 8, 372, 3, fill="#ffffff"); c.circle(x + 16, 372, 3, fill="#ffffff")
    # rows of folding chairs, backs to us
    c.rect((0, 470, W, H), fill="#241c30")
    for row, (y, s) in enumerate([(540, 0.8), (620, 1.0)]):
        for k in range(8):
            x = 120 + k * 150 + (row * 70)
            c.rect((x - 34 * s, y - 60 * s, x + 34 * s, y), fill="#5a5470", r=4)
    c.vignette(140)
    c.save(os.path.join(OUT, "letitgo.png"))


# ---------------------------------------------------------------- the Hotel Paradiso (Tahoe hotel-casino)
def mountains(c, y, color_far, color_near, seed=3):
    R = rng(seed)
    for layer, (base, amp, colr) in enumerate([(y, 150, color_far), (y + 30, 100, color_near)]):
        pts = [(-20, base)]
        x = -20
        while x < W + 40:
            x += R.uniform(60, 140)
            pts.append((x, base - R.uniform(0.3, 1.0) * amp))
        pts += [(W + 40, base + 400), (-20, base + 400)]
        c.poly(pts, fill=colr)
        if layer == 0:  # snow caps
            for i in range(1, len(pts) - 2):
                px, py = pts[i]
                if py < base - amp * 0.75:
                    c.poly([(px, py), (px - 26, py + 30), (px + 26, py + 30)], fill=col("#f4f0ff", 200))


def pines(c, y, n, color, seed=1, hmin=60, hmax=140):
    R = rng(seed)
    for _ in range(n):
        x = R.uniform(-20, W + 20)
        h = R.uniform(hmin, hmax)
        for k in range(4):
            w = h * (0.42 - k * 0.08)
            top = y - h + k * h * 0.2
            c.poly([(x, top), (x - w, top + h * 0.45), (x + w, top + h * 0.45)], fill=color)
        c.rect((x - 3, y - 10, x + 3, y + 4), fill="#2a1a14")


def casino_tower(c, night):
    """A 1970s hotel-casino tower with a porte-cochere and a big marquee."""
    wall = "#d8c8b0" if not night else "#2c2440"
    wall_d = "#b8a890" if not night else "#221a34"
    trim = "#c86a3a" if not night else "#4a2a50"
    x0, x1, top, base = 360, 920, 70, 520
    # tower
    c.rect((x0, top, x1, base), fill=wall)
    c.rect((x0 + (x1 - x0) * 0.62, top, x1, base), fill=wall_d)
    c.rect((x0 - 10, top - 18, x1 + 10, top + 6), fill=trim)
    # window grid: 14 floors x 12 columns, horizontal bands like a 70s tower
    R = rng(17)
    lights = [PINK, GOLD, CYAN, VIOLET, LIME, "#ff8f4a"]
    for f in range(14):
        y = top + 20 + f * 30
        c.rect((x0, y + 20, x1, y + 24), fill=trim)
        for k in range(12):
            x = x0 + 14 + k * 45
            lit = night and R.random() < 0.72
            wc = R.choice(lights) if lit else ("#8ab8d0" if not night else "#151022")
            c.rect((x, y, x + 34, y + 18), fill=wc)
            if lit:
                c.rect((x - 6, y - 6, x + 40, y + 24), fill=col(wc, 70), blur=6)
    # low casino wing
    c.rect((120, 400, 1160, 560), fill=wall_d)
    c.rect((110, 388, 1170, 404), fill=trim)
    # porte-cochere with a band of bulbs
    c.rect((480, 450, 800, 478), fill="#e8d8b8" if not night else "#3a2a48")
    for x in range(486, 800, 14):
        c.circle(x, 482, 3.5, fill="#ffe8a0" if night else "#fff4c8")
        if night:
            c.circle(x, 482, 9, fill=col("#ffd070", 80), blur=4)
    for x in (500, 780):
        c.rect((x - 6, 478, x + 6, 560), fill=trim)
    # entrance glow
    c.rect((560, 500, 720, 560), fill="#ffd890" if night else "#5a4a40")
    # big marquee sign on a pylon
    sx = 1060
    c.rect((sx - 10, 160, sx + 10, 560), fill="#3a3040")
    c.rect((sx - 130, 120, sx + 130, 330), fill="#1c1426", r=14)
    if night:
        c.rect((sx - 136, 114, sx + 136, 336), outline=col(PINK, 220), width=4, r=16)
        c.neon_text((sx, 160), "HOTEL", 30, CYAN)
        c.neon_text((sx, 212), "PARADIS", 42, PINK)
        c.neon_text((sx, 258), "CASINO", 24, GOLD)
        c.rect((sx - 110, 282, sx + 110, 316), fill="#0c0814")
        c.text((sx, 299), "WELCOME HOME", 16, "#ffcf5a", font="mono", glow="#ff9a2a")
    else:
        c.rect((sx - 136, 114, sx + 136, 336), outline="#c84a7a", width=4, r=16)
        c.text((sx, 160), "HOTEL", 30, "#3cc0e0")
        c.text((sx, 212), "PARADIS", 42, "#f05a9a")
        c.text((sx, 258), "CASINO", 24, "#d8a030")
        c.rect((sx - 110, 282, sx + 110, 316), fill="#0c0814")
        c.text((sx, 299), "WELCOME HOME", 16, "#d8a040", font="mono")


def bg_exterior():
    c = Canvas(W, H)
    c.vgrad((0, 0, W, H), None, None, stops=[(0, "#3a2a6a"), (0.35, "#c2578a"), (0.6, "#ff9a5a"), (1, "#ffd39a")])
    c.circle(220, 300, 90, fill=col("#ffd56b", 180), blur=30)
    c.circle(220, 300, 46, fill="#ffe7a0")
    mountains(c, 420, "#6a4a7a", "#4a3a5a", seed=3)
    pines(c, 560, 40, "#2a3a2a", seed=2, hmin=80, hmax=170)
    casino_tower(c, night=False)
    c.rect((0, 560, W, H), fill="#3a3038")
    for x in range(0, W, 120):
        c.rect((x + 20, 640, x + 80, 646), fill="#e8d26a")
    c.save(os.path.join(OUT, "exterior.png"))


def bg_exterior_night(name="exterior_night.png"):
    c = Canvas(W, H)
    c.vgrad((0, 0, W, H), None, None, stops=[(0, "#05030f"), (0.55, "#1b0f38"), (1, "#3b1d4a")])
    star_field(c, 220, (0, 0, W, 300), seed=7)
    c.circle(200, 100, 46, fill=col("#fff3d0", 90), blur=20)
    c.circle(200, 100, 34, fill="#fff3d0")
    c.circle(214, 92, 30, fill="#120a26")
    mountains(c, 420, "#1c1430", "#140e24", seed=3)
    pines(c, 560, 40, "#0a0e12", seed=2, hmin=80, hmax=170)
    casino_tower(c, night=True)
    c.rect((0, 560, W, H), fill="#120c18")
    for x in range(0, W, 120):
        c.rect((x + 20, 640, x + 80, 646), fill="#5a5030")
    c.rect((0, 548, W, 600), fill=col(PINK, 40), blur=20)
    c.vignette()
    c.save(os.path.join(OUT, name))


def casino_carpet(c, y0, seed=5):
    """The famous migraine carpet: orange and purple swirls on maroon."""
    c.rect((0, y0, W, H), fill="#5a1a3a")
    R = rng(seed)
    for _ in range(90):
        x, y = R.uniform(-40, W + 40), R.uniform(y0, H + 20)
        r = R.uniform(14, 40) * (0.5 + (y - y0) / (H - y0))
        c.arc((x - r, y - r * 0.4, x + r, y + r * 0.4), R.uniform(0, 180), R.uniform(200, 360),
              R.choice(["#ff8a3a", "#b04aff", "#ffd05a", "#2ac0b0"]), 4)
        c.circle(x, y, 3, fill=R.choice(["#ffd05a", "#ff5fb8"]))


def slot_machine(c, x, y, s=1.0, lit="#ff5fb8"):
    w, h = 70 * s, 130 * s
    c.rect((x - w / 2, y - h, x + w / 2, y), fill="#8a1a2a", r=8 * s)
    c.rect((x - w / 2 + 8 * s, y - h + 14 * s, x + w / 2 - 8 * s, y - h + 50 * s), fill="#1a0a14")
    for k in range(3):
        c.rect((x - w / 2 + 12 * s + k * 16 * s, y - h + 20 * s, x - w / 2 + 24 * s + k * 16 * s, y - h + 44 * s), fill="#fff4d8")
    c.rect((x - w / 2 - 4 * s, y - h - 16 * s, x + w / 2 + 4 * s, y - h), fill=lit, r=6 * s)
    c.rect((x - w / 2, y - h - 22 * s, x + w / 2, y - h - 4 * s), fill=col(lit, 90), blur=6)
    c.line([(x + w / 2, y - h + 40 * s), (x + w / 2 + 14 * s, y - h + 20 * s)], "#c0c0c8", 3 * s)
    c.circle(x + w / 2 + 14 * s, y - h + 18 * s, 6 * s, fill="#e04a4a")


def bg_lobby():
    c = Canvas(W, H)
    # mirrored ceiling and dark wood
    c.rect((0, 0, W, H), fill="#2a1a24")
    c.rect((0, 0, W, 70), fill="#3a2a30")
    for x in range(0, W, 80):
        c.rect((x, 0, x + 78, 68), fill="#4a3a44")
    # chandelier
    c.line([(640, 0), (640, 70)], GOLD, 3)
    for ring, r in enumerate((90, 60, 30)):
        for i in range(14 - ring * 4):
            a = 2 * math.pi * i / (14 - ring * 4)
            x, y = 640 + math.cos(a) * r, 100 + ring * 14 + math.sin(a) * r * 0.25
            c.circle(x, y, 4, fill="#fff2b0")
    c.circle(640, 110, 130, fill=col("#ffe08a", 60), blur=30)
    # back: the old casino floor through an archway, dark, slots in fairy lights
    c.rect((700, 150, 1240, 470), fill="#140a18")
    c.rect((690, 140, 1250, 160), fill=GOLD)
    for k, x in enumerate(range(760, 1220, 90)):
        slot_machine(c, x, 450, 0.9, lit=[PINK, CYAN, GOLD, VIOLET, LIME, PINK][k % 6])
    R = rng(4)
    pts = [(700 + i * 18, 190 + math.sin(i / 2) * 14) for i in range(31)]
    c.line(pts, "#1b1b1b", 1.5)
    for i, (x, y) in enumerate(pts[::2]):
        cc = [PINK, GOLD, CYAN, LIME][i % 4]
        c.circle(x, y + 5, 8, fill=col(cc, 120), blur=4)
        c.circle(x, y + 5, 3, fill=mix(cc, "#ffffff", 0.5))
    c.text((970, 168), "CASINO", 14, "#2a1a24", font="bold")
    # front desk
    c.rect((60, 360, 640, 500), fill="#6a2f2f")
    c.rect((50, 348, 650, 370), fill="#c89a5a")
    for x in range(90, 620, 110):
        c.rect((x, 390, x + 80, 480), outline="#4e1f1f", width=3)
    c.ell((330, 330, 380, 352), fill=GOLD)
    c.rect((352, 320, 358, 332), fill=GOLD)
    c.rect((120, 324, 210, 350), fill="#f2ead8")
    c.text((165, 337), "NO PHOTOS", 9, "#7a2222", font="cond")
    # sign over the desk
    c.rect((90, 200, 610, 280), fill="#1c1426", r=10)
    c.neon_text((350, 240), "REGISTRATION", 30, PINK)
    plant(c, 30, 420, 1.1, seed=4)
    casino_carpet(c, 500)
    c.vignette(110)
    c.save(os.path.join(OUT, "lobby.png"))


def bg_pool():
    c = Canvas(W, H)
    # glass atrium roof, panes gone green at the seams
    c.vgrad((0, 0, W, 300), "#8ad0f0", "#d8f0ff")
    for x in range(-200, W + 200, 120):
        c.line([(640, -400), (x, 300)], "#4a7a6a", 5)
    for y in (60, 140, 220, 290):
        c.line([(0, y), (W, y)], "#4a7a6a", 5)
    c.rect((0, 0, W, 300), fill=col("#ffffff", 30))
    c.poly([(380, 0), (560, 0), (760, 700), (420, 700)], fill=col("#fff8d8", 45), blur=20)
    # tiled back wall with big arched windows onto pines and the lake
    c.rect((0, 290, W, 470), fill="#e8f4f0")
    for x in range(0, W, 24):
        c.line([(x, 290), (x, 470)], "#cfe4e0", 1)
    for k, x in enumerate((80, 380, 680, 980)):
        c.rect((x, 310, x + 220, 450), fill="#7ac0e0")
        c.rect((x, 400, x + 220, 450), fill="#3a8ab0")
        for j in range(4):
            px = x + 30 + j * 55
            c.poly([(px, 340), (px - 18, 410), (px + 18, 410)], fill="#2f6a4a")
        c.rect((x, 310, x + 220, 450), outline="#b8d8d0", width=6)
        c.line([(x + 110, 310), (x + 110, 450)], "#b8d8d0", 4)
    # banner
    c.line([(160, 300), (1120, 300)], "#555555", 2)
    c.poly([(380, 300), (900, 300), (880, 352), (400, 352)], fill="#fff4dc")
    c.text((640, 326), "WATER IS LOVE", 26, "#2a8ab0", font="bold")
    # deck tiles
    c.rect((0, 470, W, H), fill="#f2ead8")
    for y in range(480, H, 26):
        c.line([(0, y), (W, y)], "#e0d4b8", 1.5)
    # pool
    R = rng(2)
    c.poly(blob(640, 600, 490, 116, n=60), fill="#f8f8f8")
    c.poly(blob(640, 600, 470, 102, n=60), fill="#29b8d8")
    c.poly(blob(640, 618, 420, 78, n=60), fill="#1fa2c6")
    for i in range(22):
        x, y = R.uniform(240, 1040), R.uniform(520, 680)
        if ((x - 640) / 470) ** 2 + ((y - 600) / 102) ** 2 < 0.8:
            c.arc((x - 40, y - 6, x + 40, y + 6), 200, 340, col("#e9fbff", 200), 2)
    # flamingo
    fx, fy = 860, 600
    c.ell((fx - 60, fy - 20, fx + 60, fy + 26), fill="#ff7fb0")
    c.line([(fx + 40, fy - 5), (fx + 55, fy - 70), (fx + 75, fy - 80)], "#ff7fb0", 16)
    c.poly([(fx + 75, fy - 88), (fx + 98, fy - 78), (fx + 76, fy - 70)], fill="#222222")
    # heat lamps
    for x in (90, 1190):
        c.rect((x - 4, 380, x + 4, 560), fill="#555560")
        c.poly([(x - 34, 380), (x + 34, 380), (x + 22, 350), (x - 22, 350)], fill="#3a3a44")
        c.ell((x - 30, 372, x + 30, 392), fill="#ff9a3a")
        c.circle(x, 400, 70, fill=col("#ff8a3a", 60), blur=20)
    # potted palms
    for x in (230, 1050):
        plant(c, x, 440, 1.0, seed=x)
    # indoor beach umbrella (Zyx's)
    c.line([(1010, 390), (1010, 520)], "#7a5a3a", 4)
    for i in range(8):
        c.pieslice((920, 360, 1100, 440), 180 + i * 22.5, 180 + (i + 1) * 22.5, ["#ff5f7a", "#fff1d0"][i % 2])
    c.save(os.path.join(OUT, "pool.png"))


def bg_roof(name="roof.png", dawn=False):
    c = Canvas(W, H)
    if dawn:
        c.vgrad((0, 0, W, H), None, None, stops=[(0, "#3a3a8a"), (0.35, "#c87ab0"), (0.55, "#ffb08a"), (0.68, "#ffe0a0"), (1, "#ffe0a0")])
        c.circle(880, 380, 140, fill=col("#fff0b0", 160), blur=40)
        c.circle(880, 392, 56, fill="#fff4c8")
        star_field(c, 20, (0, 0, W, 140), seed=3, maxr=1.0)
    else:
        c.vgrad((0, 0, W, H), "#03020c", "#1e1040")
        star_field(c, 320, (0, 0, W, 380), seed=9)
        c.circle(1000, 120, 40, fill=col("#fff6d8", 90), blur=20)
        c.circle(1000, 120, 30, fill="#fff6d8")
    # mountains across the lake
    mountains(c, 420, "#2a1a40" if not dawn else "#8a6a9a", "#1c1230" if not dawn else "#6a5080", seed=11)
    # the lake
    c.vgrad((0, 420, W, 520), "#0c1430" if not dawn else "#c8a0b8", "#141c40" if not dawn else "#f0c8a0")
    if dawn:
        c.poly([(840, 420), (920, 420), (980, 520), (780, 520)], fill=col("#fff0c0", 140), blur=8)
    else:
        c.poly([(980, 420), (1020, 420), (1060, 520), (940, 520)], fill=col("#fff6d8", 60), blur=8)
    # other casinos' lights along the shore
    R = rng(5)
    for _ in range(120):
        x, y = R.uniform(0, W), R.uniform(470, 515)
        c.circle(x, y, 1.6, fill=col(R.choice([GOLD, "#ffffff", PINK, CYAN]), 220 if not dawn else 90))
    # water tank + HVAC
    c.rect((80, 260, 300, 470), fill="#3a2a2a" if not dawn else "#7a5a5a")
    c.poly([(70, 260), (310, 260), (190, 200)], fill="#2a1a1a" if not dawn else "#6a4a4a")
    for x in (100, 180, 280):
        c.line([(x, 470), (x - 10, 560)], "#2a1a1a", 8)
    c.rect((330, 470, 470, 540), fill="#4a4a58" if not dawn else "#9a90a0")
    c.circle(400, 490, 18, outline="#2a2a34", width=3)
    # roof floor + parapet
    c.rect((0, 540, W, H), fill="#3a2e3a" if not dawn else "#8a7080")
    c.rect((0, 520, W, 556), fill="#4a3a4a" if not dawn else "#9a8090")
    string_lights(c, 330, 330, 1280, 360, sag=60, seed=8)
    # rigging for the ark, down into the skylight
    c.line([(700, 0), (760, 540)], "#8a8a9a", 3)
    c.line([(1260, 0), (1120, 540)], "#8a8a9a", 3)
    c.rect((740, 520, 1150, 560), fill="#555060")
    c.rect((560, 590, 760, 640), fill="#6a4a3a")  # bench
    c.rect((570, 640, 584, 680), fill="#4a3a2a")
    c.rect((736, 640, 750, 680), fill="#4a3a2a")
    c.save(os.path.join(OUT, name))


def bg_backstage():
    c = Canvas(W, H)
    c.vgrad((0, 0, W, H), "#120a1a", "#08040e")
    # scaffolding
    for x in (80, 300, 980, 1200):
        c.rect((x, 0, x + 10, 560), fill="#4a4a58")
    for y in (120, 300, 480):
        c.rect((80, y, 310, y + 8), fill="#4a4a58")
        c.rect((980, y, 1210, y + 8), fill="#4a4a58")
    for (x0, y0, x1, y1) in [(80, 120, 300, 300), (300, 300, 80, 480), (980, 120, 1200, 300), (1200, 300, 980, 480)]:
        c.line([(x0 + 5, y0), (x1 + 5, y1)], "#3a3a48", 5)
    # the curtain gap onto the ballroom
    c.rect((420, 60, 860, 560), fill="#3a0a2a")
    for k in range(9):
        x = 420 + k * 50
        c.rect((x, 60, x + 24, 560), fill="#5a1440")
    c.rect((600, 60, 680, 560), fill="#1a0626")
    for (a, cc) in [(70, PINK), (95, CYAN), (115, LIME)]:
        light_beam(c, 640, 60, a, 520, 2, cc, 90)
    c.rect((600, 60, 680, 560), fill=col("#ffffff", 20))
    # cables
    R = rng(3)
    for k in range(7):
        y = 520 + k * 14
        pts = [(x, y + math.sin(x / 70 + k) * 10) for x in range(0, W + 20, 20)]
        c.line(pts, R.choice(["#1a1a1a", "#2a2a2a", "#3a2a2a"]), 7)
    # road cases
    for (x, y, w, h, label) in [(40, 470, 210, 110, "PARTY HARDER"), (1010, 460, 240, 120, "FRAGILE: FEELINGS"), (170, 400, 150, 80, "LASERS")]:
        c.rect((x, y, x + w, y + h), fill="#1c1c24", outline="#8a8a98", width=3)
        for cx in (x, x + w - 14):
            c.rect((cx, y, cx + 14, y + 14), fill="#8a8a98")
        c.text((x + w / 2, y + h / 2), label, 14, "#e8e0d0", font="mono")
    # ladder
    c.line([(880, 560), (930, 120)], "#c0a040", 8)
    c.line([(940, 560), (990, 120)], "#c0a040", 8)
    for k in range(9):
        t = k / 8
        c.line([(880 + 50 * t, 560 - 440 * t), (940 + 50 * t, 560 - 440 * t)], "#c0a040", 6)
    # work light
    c.circle(300, 100, 20, fill="#fff4c8")
    c.circle(300, 100, 120, fill=col("#ffe8a0", 50), blur=30)
    c.rect((0, 560, W, H), fill="#0e0a14")
    c.vignette(150)
    c.save(os.path.join(OUT, "backstage.png"))


SCENES = {
    "exterior": bg_exterior, "exterior_night": bg_exterior_night, "lobby": bg_lobby, "pool": bg_pool,
    "hallway": bg_hallway, "room404": bg_room404, "lostfound": bg_lostfound, "regen": bg_regen,
    "breakfast": bg_breakfast, "forest": bg_forest, "cryptid": bg_cryptid, "exchange": bg_exchange,
    "karaoke": bg_karaoke, "ballroom": bg_ballroom,
    "ballroom_ark": lambda: bg_ballroom("ballroom_ark.png", ark=True),
    "livingroom": bg_livingroom, "mission": bg_mission, "roof": bg_roof,
    "roof_dawn": lambda: bg_roof("roof_dawn.png", dawn=True),
    "main_menu": bg_main_menu, "fortune": bg_fortune, "clinic": bg_clinic, "planetarium": bg_planetarium, "bedroom": bg_bedroom,
    "penguinpost": bg_penguinpost, "fanbar": bg_fanbar, "tentacletopia": bg_tentacletopia,
    "optical": bg_optical, "speeddating": bg_speeddating, "letitgo": bg_letitgo,
    "backstage": bg_backstage,
}

if __name__ == "__main__":
    names = sys.argv[1:] or list(SCENES)
    for n in names:
        SCENES[n]()
        print("painted", n)
