"""Crop a region of a page strip and enlarge it.

Usage: python -I crop.py <strip.png> <x0> <y0> <x1> <y1> <scale> <out.png>
"""
import sys
from PIL import Image

src, x0, y0, x1, y1, scale, out = sys.argv[1:8]
x0, y0, x1, y1 = (int(v) for v in (x0, y0, x1, y1))
scale = float(scale)
im = Image.open(src)
region = im.crop((x0, y0, x1, y1))
w, h = region.size
region = region.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
region.save(out)
print(out, region.size)
