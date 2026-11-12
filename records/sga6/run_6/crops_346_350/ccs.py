"""Connected components of dark pixels in a region of a main-scan strip: python -I ccs.py FOLIO S x0 y0 x1 y1 [THRESH]"""
import sys
import pathlib
import numpy as np
from PIL import Image
HERE = pathlib.Path(__file__).resolve().parent
folio, s = int(sys.argv[1]), int(sys.argv[2]); x0, y0, x1, y1 = map(int, sys.argv[3:7])
t = int(sys.argv[7]) if len(sys.argv) > 7 else 100
a = np.array(Image.open(HERE.parent / "b346_350" / f"page_{folio:03d}_s{s}.png").convert("L").crop((x0, y0, x1, y1))) < t
h, w = a.shape
lab = np.zeros((h, w), int); n = 0
for y in range(h):
    for x in range(w):
        if a[y, x] and not lab[y, x]:
            n += 1; st = [(y, x)]; lab[y, x] = n
            while st:
                cy, cx = st.pop()
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        ny, nx = cy + dy, cx + dx
                        if 0 <= ny < h and 0 <= nx < w and a[ny, nx] and not lab[ny, nx]:
                            lab[ny, nx] = n; st.append((ny, nx))
for k in range(1, n + 1):
    ys, xs = np.nonzero(lab == k)
    if len(ys) < 8:
        continue
    print(k, "x", x0 + xs.min(), x0 + xs.max(), "y", y0 + ys.min(), y0 + ys.max(), "h", ys.max() - ys.min() + 1, "w", xs.max() - xs.min() + 1, "px", len(ys))
