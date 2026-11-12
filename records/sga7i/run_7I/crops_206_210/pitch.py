import sys
from PIL import Image
import numpy as np
# usage: pitch.py SRC x0 y0 x1 y1 : print ink runs (columns with dark pixels) in the region
src = sys.argv[1]
x0, y0, x1, y1 = map(int, sys.argv[2:6])
im = np.asarray(Image.open(src).convert('L')).astype(int)[y0:y1, x0:x1]
dark = (im < 120).sum(axis=0) > 0
runs = []
start = None
for i, d in enumerate(dark):
    if d and start is None:
        start = i
    elif not d and start is not None:
        runs.append((start + x0, i - 1 + x0)); start = None
if start is not None:
    runs.append((start + x0, len(dark) - 1 + x0))
gaps = [(runs[k+1][0] - runs[k][1]) for k in range(len(runs)-1)]
for r, g in zip(runs, gaps + [None]):
    print(r, 'gap->', g)
