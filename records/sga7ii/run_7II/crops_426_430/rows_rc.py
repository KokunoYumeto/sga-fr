import sys
from PIL import Image
# usage: rows_rc.py img x0 x1 : print row bands with ink between columns x0..x1
im = Image.open(sys.argv[1]).convert('L')
x0, x1 = int(sys.argv[2]), int(sys.argv[3])
w, h = im.size
px = im.load()
ink = [sum(1 for x in range(x0, min(x1, w)) if px[x, y] < 128) for y in range(h)]
bands, start = [], None
for y, v in enumerate(ink):
    if v > 0 and start is None:
        start = y
    if v == 0 and start is not None:
        bands.append((start, y)); start = None
if start is not None:
    bands.append((start, h))
print(bands)
