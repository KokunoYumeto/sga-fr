import sys
from PIL import Image

# usage: glyphbox.py page strip x0 y0 x1 y1
# prints connected dark components (bounding boxes) inside the region, in strip coordinates
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = map(int, sys.argv[3:7])
src = r'C:/Users/user/Documents/sga_scan_check_20261105/run_7II/b186_190/page_%d_s%d.png' % (page, strip)
im = Image.open(src).convert('L').crop((x0, y0, x1, y1))
w, h = im.size
px = im.load()
dark = [[px[x, y] < 140 for x in range(w)] for y in range(h)]
seen = [[False] * w for _ in range(h)]
comps = []
for y in range(h):
    for x in range(w):
        if dark[y][x] and not seen[y][x]:
            stack = [(x, y)]
            seen[y][x] = True
            xs, ys = [], []
            while stack:
                cx, cy = stack.pop()
                xs.append(cx)
                ys.append(cy)
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        nx, ny = cx + dx, cy + dy
                        if 0 <= nx < w and 0 <= ny < h and dark[ny][nx] and not seen[ny][nx]:
                            seen[ny][nx] = True
                            stack.append((nx, ny))
            if len(xs) >= 8:
                comps.append((min(xs) + x0, min(ys) + y0, max(xs) + x0, max(ys) + y0, len(xs)))
comps.sort()
for c in comps:
    print('x %4d-%4d  y %4d-%4d  h %3d  n %4d' % (c[0], c[2], c[1], c[3], c[3] - c[1] + 1, c[4]))
