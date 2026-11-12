import sys
from PIL import Image
# print a coarse ASCII rendering of a region (dark pixels as #) to inspect stems
src, x0, y0, x1, y1 = sys.argv[1], *map(int, sys.argv[2:6])
thr = int(sys.argv[6]) if len(sys.argv) > 6 else 128
im = Image.open(src).convert("L")
for y in range(y0, y1):
    print("".join("#" if im.getpixel((x, y)) < thr else "." for x in range(x0, x1)))
