import sys
from PIL import Image
# usage: crop.py src x0 y0 x1 y1 scale out
src, x0, y0, x1, y1, scale, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), float(sys.argv[6]), sys.argv[7]
im = Image.open(src)
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width*scale), int(c.height*scale)), Image.LANCZOS)
c.save(out)
print(out, c.size)
