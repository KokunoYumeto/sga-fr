"""Crop helper for the 686-690 scan check.

Usage:
  python -I crop.py SRC OUT x0 y0 x1 y1 [scale]
Coordinates are pixels of SRC (or fractions of width/height when all four are <= 1).
scale enlarges the crop (default 1). Converts TIFF/PNG input to an 8-bit grey PNG.
"""
import sys
from PIL import Image

src, out = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = (float(v) for v in sys.argv[3:7])
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 1.0
im = Image.open(src)
im = im.convert("L")
w, h = im.size
if max(x0, y0, x1, y1) <= 1.0:
    x0, x1 = x0 * w, x1 * w
    y0, y1 = y0 * h, y1 * h
box = (int(x0), int(y0), int(x1), int(y1))
c = im.crop(box)
if scale != 1.0:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(out)
print(src, "size", (w, h), "box", box, "->", out, c.size)
