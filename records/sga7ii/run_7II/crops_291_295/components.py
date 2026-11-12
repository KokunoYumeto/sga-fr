import sys
from PIL import Image
import numpy as np
from scipy import ndimage

# usage: components.py <strip png> x0 y0 x1 y1 [threshold]
# prints the connected ink components inside the box (strip coordinates)
src = sys.argv[1]
x0, y0, x1, y1 = map(int, sys.argv[2:6])
thr = int(sys.argv[6]) if len(sys.argv) > 6 else 128
a = np.array(Image.open(src).convert('L'))[y0:y1, x0:x1]
ink = a < thr
lab, n = ndimage.label(ink)
objs = ndimage.find_objects(lab)
rows = []
for i, sl in enumerate(objs, 1):
    ys, xs = sl
    size = int((lab[sl] == i).sum())
    rows.append((xs.start + x0, xs.stop - 1 + x0, ys.start + y0, ys.stop - 1 + y0, size))
for r in sorted(rows):
    print("x %d-%d  y %d-%d  px %d" % r)
