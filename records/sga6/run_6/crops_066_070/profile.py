"""Row profile of a letter box: for each row, the leftmost and rightmost dark pixel (as x offsets) and a bar.
usage: python -I profile.py IMAGE X0 Y0 X1 Y1 [THRESH]"""
import sys

from PIL import Image

img, x0, y0, x1, y1 = sys.argv[1], *map(int, sys.argv[2:6])
th = int(sys.argv[6]) if len(sys.argv) > 6 else 100
im = Image.open(img).convert("L").crop((x0, y0, x1 + 1, y1 + 1))
w, h = im.size
px = im.load()
for y in range(h):
    row = "".join("#" if px[x, y] < th else "." for x in range(w))
    print("%3d %s" % (y, row))
