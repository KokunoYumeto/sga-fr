import sys
from PIL import Image

base = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\b121_125"

# usage: profile.py strip x0 y0 x1 y1 [threshold]
# prints, for each row, the number of dark pixels and the dark column span
src, x0, y0, x1, y1 = sys.argv[1:6]
thr = int(sys.argv[6]) if len(sys.argv) > 6 else 140
x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)
im = Image.open(base + "\\" + src).convert("L")
px = im.load()
for y in range(y0, y1):
    cols = [x for x in range(x0, x1) if px[x, y] < thr]
    if cols:
        print(y, len(cols), min(cols), max(cols))
    else:
        print(y, 0)
