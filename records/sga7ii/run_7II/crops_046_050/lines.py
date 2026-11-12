import sys
from PIL import Image
d = 'C:/Users/user/Documents/sga_scan_check_20261105/run_7II/b046_050'
page, strip = int(sys.argv[1]), int(sys.argv[2])
im = Image.open(f'{d}/page_{page:03d}_s{strip}.png')
w, h = im.size
px = im.load()
rows = []
for y in range(h):
    c = sum(1 for x in range(0, w, 2) if px[x, y] < 128)
    rows.append(c)
# print bands of ink
inband = False
for y, c in enumerate(rows):
    if c > 0 and not inband:
        start = y; inband = True
    elif c == 0 and inband:
        print(f'{start}-{y-1}', max(rows[start:y]))
        inband = False
if inband:
    print(f'{start}-{h-1}')
