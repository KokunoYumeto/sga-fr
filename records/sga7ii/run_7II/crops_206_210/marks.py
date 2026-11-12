import sys
from PIL import Image
import numpy as np
from collections import deque

# usage: marks.py src.png x0 y0 x1 y1 [thresh]
src = sys.argv[1]
x0, y0, x1, y1 = map(int, sys.argv[2:6])
th = int(sys.argv[6]) if len(sys.argv) > 6 else 128
im = np.array(Image.open(src).convert('L').crop((x0, y0, x1, y1)))
mask = im < th
H, W = mask.shape
seen = np.zeros_like(mask, bool)
comps = []
for y in range(H):
    for x in range(W):
        if mask[y, x] and not seen[y, x]:
            q = deque([(y, x)]); seen[y, x] = True
            pts = []
            while q:
                cy, cx = q.popleft(); pts.append((cy, cx))
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        ny, nx = cy + dy, cx + dx
                        if 0 <= ny < H and 0 <= nx < W and mask[ny, nx] and not seen[ny, nx]:
                            seen[ny, nx] = True; q.append((ny, nx))
            ys = [p[0] for p in pts]; xs = [p[1] for p in pts]
            comps.append((min(xs) + x0, max(xs) + x0, min(ys) + y0, max(ys) + y0, len(pts)))
comps.sort()
for c in comps:
    if c[4] >= 4:
        print('x %d-%d  y %d-%d  n=%d' % c)
