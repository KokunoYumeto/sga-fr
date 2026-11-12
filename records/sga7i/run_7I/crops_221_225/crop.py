"""Crop a region of a page strip and enlarge it.

Usage: python -I crop.py STRIP_PNG X0 Y0 X1 Y1 SCALE OUT_PNG
"""
import sys
from PIL import Image

src, x0, y0, x1, y1, scale, out = sys.argv[1:8]
x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)
scale = float(scale)
im = Image.open(src)
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(out)
print(out, c.size)
