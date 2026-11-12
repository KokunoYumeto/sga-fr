"""Column ink profile of a region: python -I colprof.py FILE X0 Y0 X1 Y1 [THRESH]"""
import sys
import numpy as np
from PIL import Image
f = sys.argv[1]
x0, y0, x1, y1 = map(int, sys.argv[2:6])
th = int(sys.argv[6]) if len(sys.argv) > 6 else 128
a = np.array(Image.open(f).convert('L').crop((x0, y0, x1, y1)))
ink = (a < th)
cols = ink.sum(axis=0)
runs = []
inrun = False
for i, c in enumerate(cols):
    if c and not inrun:
        start = i; inrun = True
    elif not c and inrun:
        runs.append((x0 + start, x0 + i - 1)); inrun = False
if inrun:
    runs.append((x0 + start, x0 + len(cols) - 1))
print('ink column runs:', runs)
rows = ink.sum(axis=1)
r = [y0 + i for i, v in enumerate(rows) if v]
print('ink rows:', (r[0], r[-1]) if r else None)
