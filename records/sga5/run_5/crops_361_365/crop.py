import sys
from PIL import Image
# usage: crop.py src x0 y0 x1 y1 scale out
src, x0, y0, x1, y1, sc, out = sys.argv[1:8]
im = Image.open(src)
c = im.crop((int(x0), int(y0), int(x1), int(y1)))
s = float(sc)
c = c.resize((int(c.width*s), int(c.height*s)), Image.LANCZOS)
c.save(out)
print(out, c.size)
