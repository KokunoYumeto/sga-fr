import sys, os
from PIL import Image

# usage: python crop.py SRC_PNG OUT_NAME x0 y0 x1 y1 [scale]
src, out, x0, y0, x1, y1 = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:7])
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 2.0
im = Image.open(src)
if x1 <= 0:
    print(im.size)
    sys.exit(0)
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
outdir = os.path.dirname(os.path.abspath(__file__))
c.save(os.path.join(outdir, out))
print(os.path.join(outdir, out), c.size)
