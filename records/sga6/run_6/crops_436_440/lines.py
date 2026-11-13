import sys
from PIL import Image
im = Image.open(sys.argv[1]).convert('L'); w, h = im.size; px = im.load()
inrun = False
for y in range(h):
    s = sum(1 for x in range(0, w, 2) if px[x, y] < 128)
    if s > 3 and not inrun:
        start = y; inrun = True
    elif s <= 3 and inrun:
        inrun = False
        if y - start > 4:
            xs = [x for x in range(0, w, 2) for yy in range(start, y, 3) if px[x, yy] < 128]
            print(start, y, min(xs), max(xs))
