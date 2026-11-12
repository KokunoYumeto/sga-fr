import sys
from PIL import Image

# usage: crop.py IN.png x0 y0 x1 y1 scale OUT.png
src, x0, y0, x1, y1, scale, out = sys.argv[1:8]
im = Image.open(src)
box = tuple(int(v) for v in (x0, y0, x1, y1))
c = im.crop(box)
s = float(scale)
if s != 1:
    c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS)
c.save(out)
print(out, c.size)
