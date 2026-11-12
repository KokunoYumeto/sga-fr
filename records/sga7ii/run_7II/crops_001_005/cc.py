import sys
from PIL import Image
# list connected components (dark pixels) in a box: cc.py img x0 y0 x1 y1 [thr]
src = sys.argv[1]
x0, y0, x1, y1 = map(int, sys.argv[2:6])
thr = int(sys.argv[6]) if len(sys.argv) > 6 else 140
im = Image.open(src).crop((x0, y0, x1, y1))
w, h = im.size
px = im.load()
seen = [[False]*w for _ in range(h)]
comps = []
for y in range(h):
    for x in range(w):
        if px[x, y] < thr and not seen[y][x]:
            stack = [(x, y)]; seen[y][x] = True; pts = []
            while stack:
                cx, cy = stack.pop(); pts.append((cx, cy))
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        nx, ny = cx+dx, cy+dy
                        if 0 <= nx < w and 0 <= ny < h and not seen[ny][nx] and px[nx, ny] < thr:
                            seen[ny][nx] = True; stack.append((nx, ny))
            xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
            if len(pts) >= 6:
                comps.append((min(xs)+x0, min(ys)+y0, max(xs)+x0, max(ys)+y0, len(pts)))
comps.sort()
for c in comps:
    print(c)
