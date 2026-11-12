import sys
from PIL import Image

# usage: python -I cols.py <strip.png> <y0> <y1> [x0 x1]
# prints the x-runs of columns that contain dark pixels within rows y0..y1
src = sys.argv[1]
y0, y1 = int(sys.argv[2]), int(sys.argv[3])
im = Image.open(src).convert("L")
w, h = im.size
x0 = int(sys.argv[4]) if len(sys.argv) > 4 else 0
x1 = int(sys.argv[5]) if len(sys.argv) > 5 else w
px = im.load()
runs = []
inside = False
for x in range(x0, x1 + 1):
    dark = x < x1 and any(px[x, y] < 128 for y in range(y0, y1 + 1))
    if dark and not inside:
        inside, s = True, x
    elif not dark and inside:
        inside = False
        runs.append((s, x - 1))
prev = None
for a, b in runs:
    gap = "" if prev is None else f"  gap {a - prev - 1}"
    print(f"{a}-{b}{gap}")
    prev = b
