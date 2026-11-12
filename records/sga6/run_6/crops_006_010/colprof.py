"""Column ink profile of a box: python -I colprof.py FILE X0 Y0 X1 Y1 [TH]
prints runs of columns containing ink (< TH) with their row span, to locate glyphs and gaps."""
import sys
import numpy as np
from PIL import Image
f = sys.argv[1]
x0, y0, x1, y1 = map(int, sys.argv[2:6])
th = float(sys.argv[6]) if len(sys.argv) > 6 else 100
a = np.array(Image.open(f).convert('L')).astype(float)[y0:y1, x0:x1]
ink = a < th
cols = ink.any(axis=0)
runs, start = [], None
for j, c in enumerate(cols):
    if c and start is None:
        start = j
    if not c and start is not None:
        runs.append((start, j)); start = None
if start is not None:
    runs.append((start, len(cols)))
for s, e in runs:
    rows = np.where(ink[:, s:e].any(axis=1))[0]
    print('x', x0 + s, '-', x0 + e, 'y', y0 + rows.min(), '-', y0 + rows.max(), 'min', a[:, s:e].min())
