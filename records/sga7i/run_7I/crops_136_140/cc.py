import sys
import numpy as np
from PIL import Image
from scipy import ndimage

base = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\b136_140"
# usage: cc.py src x0 y0 x1 y1 [thresh]
src = sys.argv[1]
x0, y0, x1, y1 = [int(v) for v in sys.argv[2:6]]
th = int(sys.argv[6]) if len(sys.argv) > 6 else 140
im = np.array(Image.open(base + "\\" + src).convert("L")).astype(int)
reg = im[y0:y1, x0:x1]
mask = reg < th
lab, n = ndimage.label(mask)
objs = ndimage.find_objects(lab)
rows = []
for i, sl in enumerate(objs):
    ys, xs = sl
    size = int((lab[sl] == i + 1).sum())
    if size < 8:
        continue
    rows.append((xs.start + x0, ys.start + y0, xs.stop + x0, ys.stop + y0, size))
rows.sort()
for r in rows:
    print("x %4d-%4d  y %4d-%4d  h %3d  w %3d  px %4d" % (r[0], r[2], r[1], r[3], r[3] - r[1], r[2] - r[0], r[4]))
