import sys
import numpy as np
from PIL import Image
from scipy import ndimage

# usage: dots.py <strip png> <x0> <y0> <x1> <y1> [threshold]
# Lists dark connected components in the box (sorted by x) with their
# bounding boxes, so that the dots of an ellipsis can be told from commas.
src = sys.argv[1]
x0, y0, x1, y1 = (int(v) for v in sys.argv[2:6])
thr = int(sys.argv[6]) if len(sys.argv) > 6 else 140
im = np.asarray(Image.open(src).convert("L"))[y0:y1, x0:x1]
mask = im < thr
lab, n = ndimage.label(mask)
objs = ndimage.find_objects(lab)
rows = []
for i, sl in enumerate(objs, start=1):
    ys, xs = sl
    h = ys.stop - ys.start
    w = xs.stop - xs.start
    area = int((lab[sl] == i).sum())
    if area < 6:
        continue
    rows.append((xs.start + x0, ys.start + y0, w, h, area))
rows.sort()
for r in rows:
    x, y, w, h, a = r
    kind = "dot?" if (w <= 16 and h <= 16 and a >= 20) else ""
    print(f"x={x:5d} y={y:5d} w={w:3d} h={h:3d} area={a:4d} {kind}")
