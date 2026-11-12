"""List connected ink blobs (bbox, size) in a region of an image, to compare heights of dots, arrows and letters.
usage: python -I blobs.py IMAGE X0 Y0 X1 Y1 [THRESH]"""
import sys
from PIL import Image
import numpy as np
from collections import deque

src = sys.argv[1]
x0, y0, x1, y1 = map(int, sys.argv[2:6])
th = int(sys.argv[6]) if len(sys.argv) > 6 else 100
im = np.array(Image.open(src).convert("L").crop((x0, y0, x1, y1)))
ink = im < th
h, w = ink.shape
seen = np.zeros_like(ink)
out = []
for y in range(h):
    for x in range(w):
        if ink[y, x] and not seen[y, x]:
            q = deque([(y, x)]); seen[y, x] = True; pts = []
            while q:
                cy, cx = q.popleft(); pts.append((cy, cx))
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        ny, nx = cy + dy, cx + dx
                        if 0 <= ny < h and 0 <= nx < w and ink[ny, nx] and not seen[ny, nx]:
                            seen[ny, nx] = True; q.append((ny, nx))
            ys = [p[0] for p in pts]; xs = [p[1] for p in pts]
            if len(pts) >= 4:
                out.append((min(xs) + x0, min(ys) + y0, max(xs) + x0, max(ys) + y0, len(pts)))
for b in sorted(out):
    print("x %4d-%4d  y %4d-%4d  n=%d  cy=%.1f" % (b[0], b[2], b[1], b[3], b[4], (b[1] + b[3]) / 2))
