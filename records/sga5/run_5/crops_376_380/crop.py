import sys
from PIL import Image
# usage: crop.py src.png x0 y0 x1 y1 scale out.png
src, x0, y0, x1, y1, scale, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), float(sys.argv[6]), sys.argv[7]
im = Image.open(src).crop((x0, y0, x1, y1))
if scale != 1:
    im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
im.save(out)
print(out, im.size)
