import sys
from PIL import Image

# usage: cc.py <strip.png> <x0> <y0> <x1> <y1> [threshold]
# prints bounding boxes (x0,y0,x1,y1,w,h,npix) of connected dark components in the region
src = sys.argv[1]
x0, y0, x1, y1 = map(int, sys.argv[2:6])
thr = int(sys.argv[6]) if len(sys.argv) > 6 else 140
im = Image.open(src).convert('L')
px = im.load()
W, H = x1 - x0, y1 - y0
dark = [[px[x0 + i, y0 + j] < thr for i in range(W)] for j in range(H)]
seen = [[False] * W for _ in range(H)]
comps = []
for j in range(H):
    for i in range(W):
        if dark[j][i] and not seen[j][i]:
            stack = [(i, j)]
            seen[j][i] = True
            xs, ys = [], []
            while stack:
                a, b = stack.pop()
                xs.append(a); ys.append(b)
                for da in (-1, 0, 1):
                    for db in (-1, 0, 1):
                        c, d = a + da, b + db
                        if 0 <= c < W and 0 <= d < H and dark[d][c] and not seen[d][c]:
                            seen[d][c] = True
                            stack.append((c, d))
            if len(xs) >= 4:
                comps.append((min(xs) + x0, min(ys) + y0, max(xs) + x0, max(ys) + y0, len(xs)))
comps.sort()
for c in comps:
    print(c[0], c[1], c[2], c[3], 'w=%d h=%d n=%d' % (c[2] - c[0] + 1, c[3] - c[1] + 1, c[4]))
