import sys
from PIL import Image
import numpy as np
# usage: lines.py strip.png  -> prints ink bands (y0,y1) and x extent
im = np.array(Image.open(sys.argv[1]).convert('L'))
ink = (im < 128)
rows = ink.sum(axis=1)
bands = []
inb = False
for y, r in enumerate(rows):
    if r > 2 and not inb:
        inb = True; y0 = y
    elif r <= 2 and inb:
        inb = False; bands.append((y0, y))
if inb: bands.append((y0, len(rows)))
for (a, b) in bands:
    cols = np.where(ink[a:b].sum(axis=0) > 0)[0]
    print(a, b, b-a, cols.min(), cols.max())
