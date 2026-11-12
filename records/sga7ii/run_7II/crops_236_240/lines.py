import sys
from PIL import Image
src_dir = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II\b236_240"
page, strip = sys.argv[1], sys.argv[2]
im = Image.open(rf"{src_dir}\page_{page}_s{strip}.png")
px = im.load()
w, h = im.size
rows = []
for y in range(h):
    n = sum(1 for x in range(w) if px[x, y] < 140)
    rows.append(n)
# group into bands of ink
bands = []
inb = False
for y, n in enumerate(rows):
    if n > 3 and not inb:
        start = y; inb = True
    elif n <= 3 and inb:
        bands.append((start, y)); inb = False
if inb:
    bands.append((start, h))
for b in bands:
    print(b)
