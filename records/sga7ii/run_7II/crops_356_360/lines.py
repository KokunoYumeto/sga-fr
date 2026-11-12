import sys
from PIL import Image
import numpy as np
for p in sys.argv[1:]:
    im = np.array(Image.open(p).convert('L'))
    dark = (im < 128).sum(axis=1)
    rows = dark > 2
    runs = []
    start = None
    for y, r in enumerate(rows):
        if r and start is None: start = y
        if not r and start is not None:
            runs.append((start, y)); start = None
    if start is not None: runs.append((start, len(rows)))
    print(p, im.shape, [(a,b) for a,b in runs if b-a>3])
