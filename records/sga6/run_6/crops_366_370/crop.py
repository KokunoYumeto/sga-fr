import sys
from PIL import Image
# usage: crop.py src x0 y0 x1 y1 scale out   (coords in displayed 2000-wide units)
src, x0, y0, x1, y1, scale, out = sys.argv[1], *map(float, sys.argv[2:7]), sys.argv[7]
im = Image.open(src)
f = im.width / 2000.0
box = tuple(int(round(v * f)) for v in (x0, y0, x1, y1))
c = im.crop(box)
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(out)
print(out, c.size)
