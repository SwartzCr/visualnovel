"""Convert game art to WebP, which is several times smaller than PNG and loads
much faster in the web version.

    python3 tools/to_webp.py path/to/image.png [more.png ...]

Each PNG is replaced by a .webp next to it (backgrounds at quality 85,
anything with transparency at quality 90 with lossless alpha). New art can be
dropped in as PNG and converted with this; the game loads the .webp files.
"""

import os
import sys

from PIL import Image


def convert(path):
    im = Image.open(path)
    has_alpha = im.mode in ("RGBA", "LA") or "transparency" in im.info
    im = im.convert("RGBA" if has_alpha else "RGB")
    out = os.path.splitext(path)[0] + ".webp"
    im.save(out, "WEBP", quality=90 if has_alpha else 85, method=6, alpha_quality=100)
    before, after = os.path.getsize(path), os.path.getsize(out)
    os.remove(path)
    print("%s: %d KB -> %d KB" % (out, before // 1024, after // 1024))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    for p in sys.argv[1:]:
        convert(p)
