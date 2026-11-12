import sys
from PIL import Image
import numpy as np

# usage: lines.py <strip png> [threshold]
# prints the y-ranges of rows that contain ink, with the x-extent of the ink
src = sys.argv[1]
thr = int(sys.argv[2]) if len(sys.argv) > 2 else 128
a = np.array(Image.open(src).convert('L'))
ink = a < thr
rows = ink.sum(axis=1)
inrun = False
start = 0
for y, v in enumerate(rows):
    if v > 0 and not inrun:
        inrun = True
        start = y
    elif v == 0 and inrun:
        inrun = False
        xs = np.where(ink[start:y].any(axis=0))[0]
        print(f"y {start}-{y - 1}  x {xs.min()}-{xs.max()}  ink {int(rows[start:y].sum())}")
if inrun:
    xs = np.where(ink[start:].any(axis=0))[0]
    print(f"y {start}-{len(rows) - 1}  x {xs.min()}-{xs.max()}")
