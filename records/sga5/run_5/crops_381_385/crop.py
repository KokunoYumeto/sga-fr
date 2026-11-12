"""Crop a region of a page strip and upscale it.

usage: python -I crop.py <strip.png> x0 y0 x1 y1 scale <out.png>
"""
import sys
from PIL import Image

src, x0, y0, x1, y1, scale, out = sys.argv[1:8]
x0, y0, x1, y1, scale = int(x0), int(y0), int(x1), int(y1), float(scale)
im = Image.open(src).crop((x0, y0, x1, y1))
im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
im.save(out)
print(out, im.size)
