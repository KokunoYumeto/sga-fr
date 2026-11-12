import sys
from PIL import Image
import numpy as np
# usage: lines.py strip.png  -> prints row bands containing ink
im = np.array(Image.open(sys.argv[1]).convert('L'))
ink = (im < 140).sum(axis=1)
rows = ink > 2
bands = []
start = None
for y, r in enumerate(rows):
    if r and start is None:
        start = y
    if not r and start is not None:
        bands.append((start, y)); start = None
if start is not None:
    bands.append((start, len(rows)))
for a, b in bands:
    xs = np.where((im[a:b] < 140).any(axis=0))[0]
    print(a, b, xs.min(), xs.max())
