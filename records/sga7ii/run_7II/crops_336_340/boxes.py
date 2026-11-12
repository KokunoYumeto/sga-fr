import sys
from PIL import Image
# usage: boxes.py src x0 y0 x1 y1 [thresh]
# prints bounding boxes (in strip coordinates) of dark connected components
src = sys.argv[1]
x0, y0, x1, y1 = map(int, sys.argv[2:6])
th = int(sys.argv[6]) if len(sys.argv) > 6 else 128
im = Image.open(src).convert('L').crop((x0, y0, x1, y1))
w, h = im.size
px = im.load()
seen = [[False]*w for _ in range(h)]
comps = []
for y in range(h):
    for x in range(w):
        if px[x, y] < th and not seen[y][x]:
            stack = [(x, y)]; seen[y][x] = True
            xs = []; ys = []
            while stack:
                cx, cy = stack.pop(); xs.append(cx); ys.append(cy)
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        nx, ny = cx+dx, cy+dy
                        if 0 <= nx < w and 0 <= ny < h and not seen[ny][nx] and px[nx, ny] < th:
                            seen[ny][nx] = True; stack.append((nx, ny))
            if len(xs) >= 4:
                comps.append((min(xs)+x0, min(ys)+y0, max(xs)+x0, max(ys)+y0, len(xs)))
comps.sort()
for c in comps:
    print("x %4d-%4d  y %4d-%4d  w %3d h %3d  n %4d" % (c[0], c[2], c[1], c[3], c[2]-c[0]+1, c[3]-c[1]+1, c[4]))
