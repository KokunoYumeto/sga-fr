import sys
from PIL import Image
import numpy as np
from scipy import ndimage
f, x0, y0, x1, y1 = sys.argv[1], *map(int, sys.argv[2:6])
a = np.array(Image.open(f).convert('L'))[y0:y1, x0:x1] < 140
lab, n = ndimage.label(a, structure=np.ones((3,3)))
objs = ndimage.find_objects(lab)
boxes = sorted([(s[1].start + x0, s[0].start + y0, s[1].stop + x0, s[0].stop + y0) for s in objs if s is not None], key=lambda b: b[0])
for b in boxes:
    w, h = b[2]-b[0], b[3]-b[1]
    if w*h >= 6:
        print(b, w, h)
