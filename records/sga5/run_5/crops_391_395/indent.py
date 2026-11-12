"""Print, for each text line of a page's strips, its vertical position and the x of its leftmost dark pixel.
usage: python -I -B indent.py PAGE"""
import sys
from PIL import Image

page = sys.argv[1]
for s in range(1, 5):
    im = Image.open(f"C:/Users/user/Documents/sga_scan_check_20261105/run_5/b391_395/page_{page}_s{s}.png")
    w, h = im.size
    px = im.load()
    rows = []
    for y in range(h):
        dark = [x for x in range(40, w - 40) if px[x, y] < 110]
        rows.append(dark)
    y = 0
    while y < h:
        if len(rows[y]) >= 3:
            y0 = y
            while y < h and len(rows[y]) >= 1:
                y += 1
            band = [x for yy in range(y0, y) for x in rows[yy]]
            if y - y0 >= 8 and len(band) > 40:
                print(f"s{s} y={y0}-{y} left={min(band)} right={max(band)}")
        y += 1
