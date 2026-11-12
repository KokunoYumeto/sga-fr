"""usage: python -I crop.py SRC OUT.png x0 y0 x1 y1 [scale]  (coordinates in the source image's pixels)"""
import sys
from PIL import Image
src, out = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
sc = float(sys.argv[7]) if len(sys.argv) > 7 else 2.0
im = Image.open(src).convert("L").crop((x0, y0, x1, y1))
im = im.resize((int(im.width * sc), int(im.height * sc)), Image.LANCZOS)
im.save(out)
print(out, im.size)
