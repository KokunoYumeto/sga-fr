"""Crop a region of a strip (coordinates in the 2000-px display space) and enlarge it.
usage: python -I crop.py <strip.png> <x0> <y0> <x1> <y1> <scale> <out.png>"""
import sys
from PIL import Image
src, x0, y0, x1, y1, scale, out = sys.argv[1:8]
im = Image.open(src)
f = im.width / 2000.0
box = tuple(int(round(float(v) * f)) for v in (x0, y0, x1, y1))
c = im.crop(box)
s = float(scale)
c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS)
c.save(out)
print(out, c.size)
