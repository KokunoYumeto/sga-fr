import sys
from PIL import Image
# usage: crop.py src x0 y0 x1 y1 scale out
src, x0, y0, x1, y1, scale, out = sys.argv[1:8]
im = Image.open(src)
box = (int(x0), int(y0), int(x1), int(y1))
c = im.crop(box)
s = float(scale)
c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS)
c.save(out)
print(out, c.size)
