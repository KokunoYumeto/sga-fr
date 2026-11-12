import sys
from PIL import Image

# usage: python -I cc.py <strip.png> <x0> <y0> <x1> <y1> [threshold]
# prints bounding boxes (in strip coordinates) of connected dark components
src, x0, y0, x1, y1 = sys.argv[1:6]
thr = int(sys.argv[6]) if len(sys.argv) > 6 else 140
x0, y0, x1, y1 = map(int, (x0, y0, x1, y1))
im = Image.open(src).convert('L')
W, H = x1 - x0, y1 - y0
px = im.load()
dark = [[px[x0 + i, y0 + j] < thr for i in range(W)] for j in range(H)]
seen = [[False] * W for _ in range(H)]
comps = []
for j in range(H):
    for i in range(W):
        if dark[j][i] and not seen[j][i]:
            stack = [(i, j)]
            seen[j][i] = True
            minx = maxx = i
            miny = maxy = j
            n = 0
            while stack:
                a, b = stack.pop()
                n += 1
                minx = min(minx, a); maxx = max(maxx, a)
                miny = min(miny, b); maxy = max(maxy, b)
                for da in (-1, 0, 1):
                    for db in (-1, 0, 1):
                        c, d = a + da, b + db
                        if 0 <= c < W and 0 <= d < H and dark[d][c] and not seen[d][c]:
                            seen[d][c] = True
                            stack.append((c, d))
            if n >= 6:
                comps.append((minx + x0, miny + y0, maxx + x0, maxy + y0, n))
comps.sort()
for c in comps:
    print('x %4d-%4d  y %4d-%4d  h %3d  w %3d  n %4d' % (c[0], c[2], c[1], c[3], c[3] - c[1] + 1, c[2] - c[0] + 1, c[4]))
