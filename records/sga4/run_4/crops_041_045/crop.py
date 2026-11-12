import sys
from PIL import Image

# usage: crop.py src.png out.png x0 y0 x1 y1 [scale]
src, out = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
scale = int(sys.argv[7]) if len(sys.argv) > 7 else 3
im = Image.open(src)
c = im.crop((x0, y0, x1, y1))
c = c.resize((c.width * scale, c.height * scale), Image.LANCZOS)
c.save(out)
print(out, c.size)
