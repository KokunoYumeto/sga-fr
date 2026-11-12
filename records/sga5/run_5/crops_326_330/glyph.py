"""Print a binarized glyph region as text: python -I glyph.py IMG x0 y0 x1 y1 [threshold]"""
import sys
from PIL import Image
p, x0, y0, x1, y1 = sys.argv[1], *map(int, sys.argv[2:6])
th = int(sys.argv[6]) if len(sys.argv) > 6 else 140
im = Image.open(p).convert("L").crop((x0, y0, x1, y1))
w, h = im.size
px = im.load()
for y in range(h):
    row = "".join("#" if px[x, y] < th else "." for x in range(w))
    print(f"{y0 + y:4d} {row}")
