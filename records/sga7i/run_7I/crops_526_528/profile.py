import sys
from PIL import Image

# usage: python profile.py <src.png> x0 y0 x1 y1 [threshold]
# prints, for each column, the rows that are dark (as a compact string)
src = sys.argv[1]
x0, y0, x1, y1 = map(int, sys.argv[2:6])
thr = int(sys.argv[6]) if len(sys.argv) > 6 else 120
im = Image.open(src).convert("L")
for y in range(y0, y1):
    row = "".join("#" if im.getpixel((x, y)) < thr else ("+" if im.getpixel((x, y)) < thr + 40 else ".") for x in range(x0, x1))
    print(f"{y:4d} {row}")
