"""Print bounding boxes (x0,y0,x1,y1,height,width) of dark connected components in a region of an image.
usage: python -I bbox.py IMAGE X0 Y0 X1 Y1 [THRESH]"""
import sys

from PIL import Image

img, x0, y0, x1, y1 = sys.argv[1], *map(int, sys.argv[2:6])
th = int(sys.argv[6]) if len(sys.argv) > 6 else 90
im = Image.open(img).convert("L").crop((x0, y0, x1, y1))
w, h = im.size
px = im.load()
seen = [[False] * w for _ in range(h)]
comps = []
for y in range(h):
    for x in range(w):
        if not seen[y][x] and px[x, y] < th:
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
                        if 0 <= nx < w and 0 <= ny < h and not seen[ny][nx] and px[nx, ny] < th:
                            seen[ny][nx] = True
                            stack.append((nx, ny))
            if len(xs) > 8:
                comps.append((min(xs) + x0, min(ys) + y0, max(xs) + x0, max(ys) + y0, len(xs)))
comps.sort()
for c in comps:
    print(c[:4], "h=%d w=%d n=%d" % (c[3] - c[1] + 1, c[2] - c[0] + 1, c[4]))
