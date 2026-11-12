import sys
from PIL import Image
import numpy as np
src = sys.argv[1]
im = np.array(Image.open(src).convert('L'))
dark = (im < 128).sum(axis=1)
inband = False
start = 0
for y, d in enumerate(dark):
    if d > 2 and not inband:
        inband = True; start = y
    elif d <= 2 and inband:
        inband = False
        if y - start > 3:
            print(start, y)
if inband: print(start, len(dark))
