"""Crop a region of a strip and enlarge it.
usage: python -I crop.py STRIP.png x0 y0 x1 y1 SCALE OUT.png"""
import sys

from PIL import Image

src, x0, y0, x1, y1, scale, out = sys.argv[1:8]
im = Image.open(src).convert("L")
c = im.crop((int(x0), int(y0), int(x1), int(y1)))
s = float(scale)
c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS)
c.save(out)
print(out, c.size)
