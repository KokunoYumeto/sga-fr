"""linestarts.py PAGE: for each strip, the text-line bands (y range) and the x of their first dark pixel.
Coordinates in the strip's own pixels; an indented line starts about 130-150 px right of the margin."""
import sys
from PIL import Image

B = r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\b451_455"
page = int(sys.argv[1])
thr = int(sys.argv[2]) if len(sys.argv) > 2 else 90
for s in range(1, 5):
    im = Image.open(B + r"\page_%d_s%d.png" % (page, s)).convert("L")
    w, h = im.size
    px = im.load()
    x0, x1 = 60, w - 250  # skip the dark binding edge and the right margin
    dark = []
    for y in range(h):
        n = 0
        for x in range(x0, x1, 2):
            if px[x, y] < thr:
                n += 1
        dark.append(n)
    bands = []
    start = None
    for y in range(h):
        if dark[y] > 2 and start is None:
            start = y
        elif dark[y] <= 2 and start is not None:
            if y - start > 6:
                bands.append((start, y))
            start = None
    if start is not None:
        bands.append((start, h))
    print("strip", s)
    for a, b in bands:
        xs = [x for x in range(x0, x1) for y in range(a, b) if px[x, y] < thr]
        print("   y %4d-%4d  first x %4d  last x %4d" % (a, b, min(xs), max(xs)))
