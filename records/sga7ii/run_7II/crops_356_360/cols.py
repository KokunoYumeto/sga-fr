import sys
from PIL import Image
import numpy as np
# usage: cols.py strip y0 y1 [x0 x1] -> print dark column runs (glyph extents)
p = sys.argv[1]; y0, y1 = int(sys.argv[2]), int(sys.argv[3])
im = np.array(Image.open(p).convert('L'))
x0 = int(sys.argv[4]) if len(sys.argv) > 4 else 0
x1 = int(sys.argv[5]) if len(sys.argv) > 5 else im.shape[1]
band = im[y0:y1, x0:x1]
dark = (band < 140).sum(axis=0)
runs=[]; start=None
for x, d in enumerate(dark):
    if d>0 and start is None: start=x
    if d==0 and start is not None: runs.append((start+x0, x+x0-1)); start=None
if start is not None: runs.append((start+x0, x1-1))
print(runs)
