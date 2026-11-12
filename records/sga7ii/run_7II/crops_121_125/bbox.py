import sys
from PIL import Image

# usage: bbox.py <strip png> <x0> <y0> <x1> <y1> [threshold]
# prints bounding boxes (x0,y0,x1,y1,w,h,count) of dark connected components in the region
src = sys.argv[1]
x0, y0, x1, y1 = map(int, sys.argv[2:6])
thr = int(sys.argv[6]) if len(sys.argv) > 6 else 128
im = Image.open(src).convert("L").crop((x0, y0, x1, y1))
W, H = im.size
px = im.load()
seen = [[False] * W for _ in range(H)]
comps = []
for y in range(H):
    for x in range(W):
        if px[x, y] < thr and not seen[y][x]:
            stack = [(x, y)]
            seen[y][x] = True
            minx = maxx = x
            miny = maxy = y
            n = 0
            while stack:
                cx, cy = stack.pop()
                n += 1
                minx = min(minx, cx); maxx = max(maxx, cx)
                miny = min(miny, cy); maxy = max(maxy, cy)
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        nx, ny = cx + dx, cy + dy
                        if 0 <= nx < W and 0 <= ny < H and not seen[ny][nx] and px[nx, ny] < thr:
                            seen[ny][nx] = True
                            stack.append((nx, ny))
            if n >= 8:
                comps.append((minx + x0, miny + y0, maxx + x0, maxy + y0, maxx - minx + 1, maxy - miny + 1, n))
comps.sort()
for c in comps:
    print(c)
