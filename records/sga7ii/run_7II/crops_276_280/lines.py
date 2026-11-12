import sys
from PIL import Image
import numpy as np
for src in sys.argv[1:]:
    a = np.array(Image.open(src)) < 128
    rows = a.sum(axis=1)
    bands = []
    inb = False
    for y, v in enumerate(rows):
        if v > 2 and not inb:
            inb = True; y0 = y
        elif v <= 2 and inb:
            inb = False; bands.append((y0, y))
    if inb: bands.append((y0, len(rows)))
    print(src)
    for b in bands:
        cols = np.where(a[b[0]:b[1]].any(axis=0))[0]
        print('  y %d-%d  x %d-%d' % (b[0], b[1], cols.min(), cols.max()))
