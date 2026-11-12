import sys
from PIL import Image
import numpy as np
im = np.array(Image.open(sys.argv[1]).convert('L'))
dark = (im < 128).sum(axis=1)
inrun=False; start=0
for y,v in enumerate(dark):
    if v>2 and not inrun: inrun=True; start=y
    elif v<=2 and inrun:
        inrun=False
        xs = np.where((im[start:y] < 128).any(axis=0))[0]
        print(f"rows {start}-{y}  x {xs.min()}-{xs.max()}")
if inrun: print(f"rows {start}-end")
