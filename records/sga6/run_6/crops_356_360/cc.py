"""Connected components of dark pixels in a region of a rendered witness page (wit_FOLIO.png) or of a main-scan strip.
usage: python -I cc.py wit FOLIO x0 y0 x1 y1
       python -I cc.py strip FOLIO S x0 y0 x1 y1 [THRESH]
"""
import pathlib
import sys

import numpy as np
from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
mode = sys.argv[1]
if mode == "wit":
    folio = int(sys.argv[2])
    x0, y0, x1, y1 = map(int, sys.argv[3:7])
    a = np.array(Image.open(HERE / f"wit_{folio}.png").convert("L").crop((x0, y0, x1, y1))) < 128
    minpx = 3
else:
    folio, s = int(sys.argv[2]), int(sys.argv[3])
    x0, y0, x1, y1 = map(int, sys.argv[4:8])
    t = int(sys.argv[8]) if len(sys.argv) > 8 else 100
    a = np.array(Image.open(HERE.parent / "b356_360" / f"page_{folio:03d}_s{s}.png").convert("L").crop((x0, y0, x1, y1))) < t
    minpx = 8
h, w = a.shape
lab = np.zeros((h, w), int)
n = 0
for y in range(h):
    for x in range(w):
        if a[y, x] and not lab[y, x]:
            n += 1
            st = [(y, x)]
            lab[y, x] = n
            while st:
                cy, cx = st.pop()
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        ny, nx = cy + dy, cx + dx
                        if 0 <= ny < h and 0 <= nx < w and a[ny, nx] and not lab[ny, nx]:
                            lab[ny, nx] = n
                            st.append((ny, nx))
rows = []
for k in range(1, n + 1):
    ys, xs = np.nonzero(lab == k)
    if len(ys) < minpx:
        continue
    rows.append((x0 + xs.min(), x0 + xs.max(), y0 + ys.min(), y0 + ys.max(), len(ys)))
for r in sorted(rows):
    print("x", r[0], r[1], "y", r[2], r[3], "h", r[3] - r[2] + 1, "w", r[1] - r[0] + 1, "px", r[4])
