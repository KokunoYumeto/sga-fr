"""Measure ink bounding boxes of the connected components in a region of a strip (read-only).
usage: python -I measure.py page strip x0 y0 x1 y1"""
import sys
import numpy as np
from PIL import Image
from scipy import ndimage
page, strip, x0, y0, x1, y1 = sys.argv[1:7]
x0, y0, x1, y1 = map(int, (x0, y0, x1, y1))
im = np.array(Image.open(rf"C:/Users/user/Documents/sga_scan_check_20261105/run_5/b051_055/page_{int(page):03d}_s{strip}.png"))
reg = im[y0:y1, x0:x1] < 140
lab, n = ndimage.label(reg, structure=np.ones((3, 3)))
for i, sl in enumerate(ndimage.find_objects(lab), 1):
    ys, xs = sl
    size = (lab[sl] == i).sum()
    if size < 15:
        continue
    print(f"comp {i}: x {xs.start + x0}-{xs.stop + x0 - 1}  y {ys.start + y0}-{ys.stop + y0 - 1}  h {ys.stop - ys.start}  w {xs.stop - xs.start}  px {size}")
