import sys
from PIL import Image
# usage: crop.py SRC X0 Y0 X1 Y1 SCALE OUT
src, x0, y0, x1, y1, sc, out = sys.argv[1], *map(int, sys.argv[2:6]), float(sys.argv[6]), sys.argv[7]
im = Image.open(src)
c = im.crop((x0, y0, x1, y1))
if sc != 1:
    c = c.resize((int(c.width*sc), int(c.height*sc)), Image.LANCZOS)
c.save(out)
print(im.size, c.size)
