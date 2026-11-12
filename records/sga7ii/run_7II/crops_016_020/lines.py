import sys
from PIL import Image

# usage: python -I lines.py <strip.png> [x0 x1]
# prints the y-ranges of text lines (rows containing dark pixels) and,
# for each line, the x-extent of its dark pixels
src = sys.argv[1]
im = Image.open(src).convert("L")
w, h = im.size
x0 = int(sys.argv[2]) if len(sys.argv) > 2 else 0
x1 = int(sys.argv[3]) if len(sys.argv) > 3 else w
px = im.load()
rows = []
for y in range(h):
    n = sum(1 for x in range(x0, x1) if px[x, y] < 128)
    rows.append(n)
inside = False
start = 0
for y in range(h + 1):
    dark = y < h and rows[y] > 0
    if dark and not inside:
        inside, start = True, y
    elif not dark and inside:
        inside = False
        xs = [x for yy in range(start, y) for x in range(x0, x1) if px[x, yy] < 128]
        print(f"y {start}-{y - 1}  x {min(xs)}-{max(xs)}  ink {sum(rows[start:y])}")
