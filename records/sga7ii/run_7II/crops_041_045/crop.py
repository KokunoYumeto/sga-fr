import sys
from PIL import Image
# usage: crop.py strip_png x0 y0 x1 y1 scale out_png
src, x0, y0, x1, y1, scale, out = sys.argv[1], *map(int, sys.argv[2:6]), float(sys.argv[6]), sys.argv[7]
im = Image.open(src).crop((x0, y0, x1, y1))
if scale != 1:
    im = im.resize((int(im.width*scale), int(im.height*scale)), Image.LANCZOS)
im.save(out)
print(out, im.size)
