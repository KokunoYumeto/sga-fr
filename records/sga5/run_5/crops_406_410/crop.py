"""crop.py SRC X0 Y0 X1 Y1 SCALE OUT : crop a box of a strip image and enlarge it."""
import sys
from PIL import Image
src, x0, y0, x1, y1, s, out = sys.argv[1], *map(int, sys.argv[2:6]), float(sys.argv[6]), sys.argv[7]
im = Image.open(src)
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS)
c.save(out)
print(im.size, '->', c.size)
