"""ascii.py IMG x0 y0 x1 y1 [thr]: ASCII rendering of a region (image pixels)."""
import sys
from PIL import Image
img, x0, y0, x1, y1 = sys.argv[1], *map(int, sys.argv[2:6])
thr = int(sys.argv[6]) if len(sys.argv) > 6 else 100
im = Image.open(img).convert("L")
for y in range(y0, y1):
    print("%4d " % y + "".join("#" if im.getpixel((x, y)) < thr else ("+" if im.getpixel((x, y)) < thr + 25 else ".") for x in range(x0, x1)))
