import sys
from PIL import Image
# usage: rows.py strip.png [x0 x1] ; prints runs of rows containing ink (text lines)
im = Image.open(sys.argv[1]).convert('L')
w, h = im.size
x0 = int(sys.argv[2]) if len(sys.argv) > 2 else 0
x1 = int(sys.argv[3]) if len(sys.argv) > 3 else w
px = im.load()
rows = []
for y in range(h):
    n = sum(1 for x in range(x0, x1) if px[x, y] < 128)
    rows.append(n)
inrun = False
for y, n in enumerate(rows):
    if n > 2 and not inrun:
        start = y; inrun = True
    elif n <= 2 and inrun:
        inrun = False
        # find leftmost/rightmost ink in run
        xs = [x for yy in range(start, y) for x in range(x0, x1) if px[x, yy] < 128]
        print(f"rows {start}-{y-1}  x {min(xs)}-{max(xs)}")
if inrun:
    xs = [x for yy in range(start, h) for x in range(x0, x1) if px[x, yy] < 128]
    print(f"rows {start}-{h-1}  x {min(xs)}-{max(xs)}")
