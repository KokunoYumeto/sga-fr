import sys
from PIL import Image
import numpy as np
from scipy import ndimage
src, x0, y0, x1, y1 = sys.argv[1], *map(int, sys.argv[2:6])
a = np.array(Image.open(src))[y0:y1, x0:x1] < 140
lab, n = ndimage.label(a, structure=np.ones((3,3)))
objs = ndimage.find_objects(lab)
res = []
for i, sl in enumerate(objs):
    ys, xs = sl
    h = ys.stop - ys.start; w = xs.stop - xs.start
    cnt = (lab[sl] == i+1).sum()
    if cnt < 8: continue
    res.append((xs.start + x0, ys.start + y0, w, h, cnt))
res.sort()
for r in res:
    print('x=%d y=%d w=%d h=%d px=%d  bottom=%d' % (r[0], r[1], r[2], r[3], r[4], r[1]+r[3]))
