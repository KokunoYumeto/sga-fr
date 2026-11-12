import sys
from PIL import Image
import numpy as np
# print y-ranges of text lines (rows containing dark pixels)
im = np.array(Image.open(sys.argv[1]).convert('L'))
dark = (im < 128).sum(axis=1)
inrun = False; start = 0
for y, d in enumerate(dark):
    if d > 2 and not inrun:
        inrun = True; start = y
    elif d <= 2 and inrun:
        inrun = False
        if y - start > 3: print(start, y)
if inrun: print(start, len(dark))
