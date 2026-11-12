import sys
from PIL import Image
# usage: crop.py src x0 y0 x1 y1 out [scale]
src, x0, y0, x1, y1, out = sys.argv[1], *map(int, sys.argv[2:6]), sys.argv[6]
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 1.0
im = Image.open(src)
c = im.crop((x0, y0, x1, y1))
if scale != 1.0:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(out)
print(im.size, c.size)
