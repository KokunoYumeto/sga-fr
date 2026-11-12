import sys
from PIL import Image

SRC = r"C:/Users/user/Documents/sga_scan_check_20261105/run_7II/b226_230/"

# print the vertical extents of ink bands (text lines) in a strip
f = sys.argv[1]
im = Image.open(SRC + f).convert("L")
w, h = im.size
px = im.load()
rows = []
for y in range(h):
    n = 0
    for x in range(0, w, 2):
        if px[x, y] < 128:
            n += 1
    rows.append(n)
bands = []
inb = False
for y, n in enumerate(rows):
    if n > 0 and not inb:
        start = y
        inb = True
    elif n == 0 and inb:
        bands.append((start, y))
        inb = False
if inb:
    bands.append((start, h))
for b in bands:
    # horizontal extent
    xs = [x for x in range(w) for y in range(b[0], b[1], 3) if px[x, y] < 128]
    print(b, (min(xs), max(xs)) if xs else None)
