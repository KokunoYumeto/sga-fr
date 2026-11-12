"""Crop helper: python -I crop.py <strip.png> <x0> <y0> <x1> <y1> <scale> <out.png>"""
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
