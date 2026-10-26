"""Tiny supersampled drawing helper used by make_backgrounds.py and make_sprites.py."""
import math
import random
from PIL import Image, ImageDraw, ImageFilter, ImageFont

SS = 2  # supersampling factor
FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
FONTS = {
    "sans": "DejaVuSans.ttf",
    "bold": "DejaVuSans-Bold.ttf",
    "serif": "DejaVuSerif-Bold.ttf",
    "mono": "DejaVuSansMono-Bold.ttf",
    "cond": "DejaVuSansCondensed-Bold.ttf",
}


def hexc(h, a=255):
    h = h.lstrip("#")
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), a)


def col(c, a=None):
    if isinstance(c, str):
        c = hexc(c)
    if len(c) == 3:
        c = tuple(c) + (255,)
    if a is not None:
        c = c[:3] + (int(a),)
    return c


def mix(a, b, t):
    a, b = col(a), col(b)
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(4))


class Canvas:
    def __init__(self, w, h, bg=None):
        self.w, self.h = w, h
        self.im = Image.new("RGBA", (w * SS, h * SS), col(bg) if bg else (0, 0, 0, 0))
        self.d = ImageDraw.Draw(self.im)

    # --- coordinate helpers
    @staticmethod
    def s(v):
        if isinstance(v, (list, tuple)):
            return [Canvas.s(x) for x in v]
        return v * SS

    def _layer(self):
        layer = Image.new("RGBA", self.im.size, (0, 0, 0, 0))
        return layer, ImageDraw.Draw(layer)

    def _comp(self, layer, blur=0):
        if blur:
            layer = layer.filter(ImageFilter.GaussianBlur(blur * SS))
        self.im.alpha_composite(layer)

    # --- primitives (all composite through a layer so alpha blends properly)
    def rect(self, box, fill=None, outline=None, width=1, r=0, blur=0):
        layer, d = self._layer()
        b = self.s(list(box))
        if r:
            d.rounded_rectangle(b, radius=r * SS, fill=col(fill) if fill else None,
                                outline=col(outline) if outline else None, width=width * SS)
        else:
            d.rectangle(b, fill=col(fill) if fill else None,
                        outline=col(outline) if outline else None, width=width * SS)
        self._comp(layer, blur)

    def ell(self, box, fill=None, outline=None, width=1, blur=0):
        layer, d = self._layer()
        d.ellipse(self.s(list(box)), fill=col(fill) if fill else None,
                  outline=col(outline) if outline else None, width=width * SS)
        self._comp(layer, blur)

    def circle(self, cx, cy, r, fill=None, outline=None, width=1, blur=0):
        self.ell((cx - r, cy - r, cx + r, cy + r), fill, outline, width, blur)

    def poly(self, pts, fill=None, outline=None, width=1, blur=0):
        layer, d = self._layer()
        P = [tuple(self.s(list(p))) for p in pts]
        d.polygon(P, fill=col(fill) if fill else None)
        if outline:
            d.line(P + [P[0]], fill=col(outline), width=width * SS, joint="curve")
        self._comp(layer, blur)

    def line(self, pts, fill, width=1, blur=0):
        layer, d = self._layer()
        P = [tuple(self.s(list(p))) for p in pts]
        d.line(P, fill=col(fill), width=max(1, int(width * SS)), joint="curve")
        if width >= 3:
            for p in (P[0], P[-1]):
                rr = width * SS / 2
                d.ellipse([p[0] - rr, p[1] - rr, p[0] + rr, p[1] + rr], fill=col(fill))
        self._comp(layer, blur)

    def arc(self, box, start, end, fill, width=1, blur=0):
        layer, d = self._layer()
        d.arc(self.s(list(box)), start, end, fill=col(fill), width=width * SS)
        self._comp(layer, blur)

    def pieslice(self, box, start, end, fill, blur=0):
        layer, d = self._layer()
        d.pieslice(self.s(list(box)), start, end, fill=col(fill))
        self._comp(layer, blur)

    def vgrad(self, box, top, bottom, stops=None):
        x0, y0, x1, y1 = [int(v) for v in self.s(list(box))]
        layer, d = self._layer()
        if not stops:
            top, bottom = col(top), col(bottom)
        hgt = max(1, y1 - y0)
        for y in range(y0, y1):
            t = (y - y0) / hgt
            if stops:
                c = _stops(stops, t)
            else:
                c = mix(top, bottom, t)
            d.line([(x0, y), (x1, y)], fill=c)
        self._comp(layer)

    def radial(self, cx, cy, r, inner, outer=None, steps=40):
        outer = outer or col(inner, 0)
        layer, d = self._layer()
        for i in range(steps, 0, -1):
            t = i / steps
            rr = r * t * SS
            d.ellipse([cx * SS - rr, cy * SS - rr, cx * SS + rr, cy * SS + rr], fill=mix(inner, outer, t))
        self._comp(layer, blur=r / steps)

    def glow_rect(self, box, color, blur=8, r=0, strength=1):
        for _ in range(strength):
            self.rect(box, fill=color, r=r, blur=blur)

    def text(self, xy, txt, size, fill, font="bold", anchor="mm", blur=0, glow=None, spacing=4, align="center"):
        f = ImageFont.truetype(FONT_DIR + FONTS[font], int(size * SS))
        if glow:
            layer, d = self._layer()
            d.multiline_text(tuple(self.s(list(xy))), txt, font=f, fill=col(glow), anchor=anchor,
                             spacing=spacing * SS, align=align)
            self._comp(layer, blur=max(3, size / 5))
            self._comp(layer.copy(), blur=max(1, size / 12))
        layer, d = self._layer()
        d.multiline_text(tuple(self.s(list(xy))), txt, font=f, fill=col(fill), anchor=anchor,
                         spacing=spacing * SS, align=align)
        self._comp(layer, blur)

    def neon_text(self, xy, txt, size, color, font="bold", anchor="mm"):
        self.text(xy, txt, size, mix(color, "#ffffff", 0.55), font=font, anchor=anchor, glow=color)

    def neon_line(self, pts, color, width=3):
        self.line(pts, color, width=width * 3, blur=width * 2)
        self.line(pts, mix(color, "#ffffff", 0.6), width=width)

    def paste(self, other, xy=(0, 0)):
        self.im.alpha_composite(other.im, tuple(self.s(list(xy))))

    def vignette(self, strength=150):
        layer, d = self._layer()
        W, H = self.im.size
        for i in range(30):
            t = i / 30
            a = int(strength * (1 - t) ** 2)
            pad = int(t * min(W, H) * 0.35)
            d.rectangle([pad, pad, W - pad, H - pad], outline=(0, 0, 0, a), width=int(min(W, H) * 0.012) + 1)
        self._comp(layer, blur=40)

    def save(self, fn):
        out = self.im.resize((self.w, self.h), Image.LANCZOS)
        out.save(fn, optimize=True)
        return out


def _stops(stops, t):
    for (t0, c0), (t1, c1) in zip(stops, stops[1:]):
        if t0 <= t <= t1:
            return mix(c0, c1, (t - t0) / max(1e-6, t1 - t0))
    return col(stops[-1][1])


def rng(seed):
    return random.Random(seed)


def star_field(c, n, box, seed=1, color="#ffffff", maxr=1.6):
    R = rng(seed)
    x0, y0, x1, y1 = box
    for _ in range(n):
        x, y = R.uniform(x0, x1), R.uniform(y0, y1)
        r = R.uniform(0.4, maxr)
        c.circle(x, y, r, fill=col(color, R.randint(120, 255)))


def wobble(points, amp, seed=0):
    R = rng(seed)
    return [(x + R.uniform(-amp, amp), y + R.uniform(-amp, amp)) for x, y in points]


def blob(cx, cy, rx, ry, n=40, amp=0.0, seed=0, start=0, end=2 * math.pi):
    R = rng(seed)
    pts = []
    for i in range(n):
        a = start + (end - start) * i / n
        k = 1 + R.uniform(-amp, amp)
        pts.append((cx + math.cos(a) * rx * k, cy + math.sin(a) * ry * k))
    return pts
