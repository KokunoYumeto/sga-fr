import sys
from PIL import Image

# usage: marks.py SRC x0 y0 x1 y1 [maxsize]
# Prints bounding boxes (absolute coordinates) of small dark connected components.
src = sys.argv[1]
x0, y0, x1, y1 = map(int, sys.argv[2:6])
maxsize = int(sys.argv[6]) if len(sys.argv) > 6 else 400
im = Image.open(src).convert('L')
px = im.load()
seen = set()
comps = []
for y in range(y0, y1):
    for x in range(x0, x1):
        if px[x, y] < 128 and (x, y) not in seen:
            stack = [(x, y)]
            seen.add((x, y))
            pts = []
            while stack:
                cx, cy = stack.pop()
                pts.append((cx, cy))
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        nx, ny = cx + dx, cy + dy
                        if x0 <= nx < x1 and y0 <= ny < y1 and (nx, ny) not in seen and px[nx, ny] < 128:
                            seen.add((nx, ny))
                            stack.append((nx, ny))
            xs = [p[0] for p in pts]
            ys = [p[1] for p in pts]
            comps.append((min(xs), min(ys), max(xs), max(ys), len(pts)))
comps.sort()
for c in comps:
    if c[4] <= maxsize:
        bx0, by0, bx1, by1, n = c
        print('x %4d-%4d  y %4d-%4d  w %2d h %2d  px %3d' % (bx0, bx1, by0, by1, bx1 - bx0 + 1, by1 - by0 + 1, n))
