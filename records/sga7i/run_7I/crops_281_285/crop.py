import sys
from PIL import Image
# usage: crop.py src x0 y0 x1 y1 out [scale]
src, x0, y0, x1, y1, out = sys.argv[1], *map(int, sys.argv[2:6]), sys.argv[6]
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 2.0
im = Image.open(src).crop((x0, y0, x1, y1))
im = im.resize((int(im.width*scale), int(im.height*scale)), Image.LANCZOS)
im.save(out)
print(out, im.size)
