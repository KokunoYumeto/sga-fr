"""Connected components (dark pixels) in a region of a rendered witness page: python -I cc.py FOLIO x0 y0 x1 y1"""
import sys
import pathlib
import numpy as np
from PIL import Image
HERE = pathlib.Path(__file__).resolve().parent
folio = int(sys.argv[1]); x0, y0, x1, y1 = map(int, sys.argv[2:6])
a = np.array(Image.open(HERE / f"wit_{folio}.png").convert("L").crop((x0, y0, x1, y1))) < 128
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
    print(k, "x", x0 + xs.min(), x0 + xs.max(), "y", y0 + ys.min(), y0 + ys.max(), "h", ys.max() - ys.min() + 1, "w", xs.max() - xs.min() + 1, "px", len(ys))
