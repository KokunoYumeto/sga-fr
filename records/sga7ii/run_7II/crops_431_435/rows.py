import sys
from PIL import Image
import numpy as np

# usage: python rows.py SRC_PNG  -> prints text-line bands (y ranges with dark pixels)
im = np.asarray(Image.open(sys.argv[1]).convert('L'))
dark = (im < 128).sum(axis=1)
thr = int(sys.argv[2]) if len(sys.argv) > 2 else 3
bands = []
start = None
for y, v in enumerate(dark):
    if v >= thr and start is None:
        start = y
    elif v < thr and start is not None:
        bands.append((start, y))
        start = None
if start is not None:
    bands.append((start, len(dark)))
print(im.shape)
for b in bands:
    cols = np.where((im[b[0]:b[1]] < 128).any(axis=0))[0]
    print(b, 'x', cols.min(), cols.max())
