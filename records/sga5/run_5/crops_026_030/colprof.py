import sys
from PIL import Image
# usage: colprof.py page strip x0 y0 x1 y1  -> prints per-column dark-pixel counts (threshold 128)
page, strip, x0, y0, x1, y1 = sys.argv[1:7]
im = Image.open(f"C:/Users/user/Documents/sga_scan_check_20261105/run_5/b026_030/page_{int(page):03d}_s{strip}.png").convert('L')
x0, y0, x1, y1 = map(int, (x0, y0, x1, y1))
cols = []
for x in range(x0, x1):
    cols.append(sum(1 for y in range(y0, y1) if im.getpixel((x, y)) < 128))
print(' '.join(f'{c:2d}' for c in cols))
# row profile at mid-height
ym = (y0 + y1) // 2
for y in range(y0, y1):
    print(''.join('#' if im.getpixel((x, y)) < 128 else ('+' if im.getpixel((x, y)) < 200 else '.') for x in range(x0, x1)))
