import sys
from PIL import Image
import numpy as np
from scipy import ndimage
# usage: comps.py <png> x0 y0 x1 y1  -> list connected components (x, y, w, h, ink)
path = sys.argv[1]
box = tuple(int(v) for v in sys.argv[2:6])
im = Image.open(path).convert('L').crop(box)
a = np.array(im) < 140
lab, n = ndimage.label(a)
out = []
for i, sl in enumerate(ndimage.find_objects(lab)):
    ys, xs = sl
    w = xs.stop - xs.start; h = ys.stop - ys.start
    if w * h > 30:
        out.append((box[0] + xs.start, box[1] + ys.start, w, h, int((lab[sl] == i + 1).sum())))
for o in sorted(out):
    print(o)
