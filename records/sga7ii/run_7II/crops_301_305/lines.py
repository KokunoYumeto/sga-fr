import sys
from PIL import Image
import numpy as np
p=sys.argv[1]
im=np.array(Image.open(p).convert('L'))
dark=(im<128).sum(axis=1)
inrun=False
for y,v in enumerate(dark):
    if v>0 and not inrun:
        start=y; inrun=True
    elif v==0 and inrun:
        inrun=False
        xs=np.where((im[start:y]<128).any(axis=0))[0]
        print(f'{start}-{y}  x {xs.min()}-{xs.max()}')
if inrun: print(start,'-end')
