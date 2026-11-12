"""crop.py SRC OUT x0 y0 x1 y1 [scale]: crop a strip (original pixel coordinates) and enlarge it."""
import sys
from PIL import Image
src, out = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
s = float(sys.argv[7]) if len(sys.argv) > 7 else 2.0
im = Image.open(src).crop((x0, y0, x1, y1))
im = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS)
im.save(out)
print(out, im.size)
