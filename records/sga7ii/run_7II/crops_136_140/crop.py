import sys
from PIL import Image

# usage: crop.py src x0 y0 x1 y1 out [scale]
src, x0, y0, x1, y1, out = sys.argv[1:7]
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 2.0
im = Image.open(src)
c = im.crop((int(x0), int(y0), int(x1), int(y1)))
if scale != 1.0:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(out)
print(out, c.size)
