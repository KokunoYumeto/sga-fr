"""Connected components (dark pixels) in a region of a strip: bounding boxes and sizes.
usage: python -I cc.py PAGE STRIP X0 Y0 X1 Y1 [THRESH] [MINPIX]"""
import sys
import numpy as np
from PIL import Image

page, strip, x0, y0, x1, y1 = sys.argv[1:7]
thr = int(sys.argv[7]) if len(sys.argv) > 7 else 128
minpix = int(sys.argv[8]) if len(sys.argv) > 8 else 4
x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)
src = r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\b296_300\page_%s_s%s.png" % (page, strip)
im = np.array(Image.open(src).convert("L"))[y0:y1, x0:x1]
dark = im < thr
h, w = dark.shape
lab = np.zeros((h, w), dtype=int)
n = 0
comps = []
for y in range(h):
    for x in range(w):
        if dark[y, x] and lab[y, x] == 0:
            n += 1
            stack = [(y, x)]
            lab[y, x] = n
            pts = []
            while stack:
                cy, cx = stack.pop()
                pts.append((cy, cx))
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        ny, nx = cy + dy, cx + dx
                        if 0 <= ny < h and 0 <= nx < w and dark[ny, nx] and lab[ny, nx] == 0:
                            lab[ny, nx] = n
                            stack.append((ny, nx))
            ys = [p[0] for p in pts]
            xs = [p[1] for p in pts]
            if len(pts) >= minpix:
                comps.append((min(xs) + x0, max(xs) + x0, min(ys) + y0, max(ys) + y0, len(pts)))
comps.sort()
for c in comps:
    print("x %4d-%4d  y %4d-%4d  w %3d h %3d  n %4d" % (c[0], c[1], c[2], c[3], c[1] - c[0] + 1, c[3] - c[2] + 1, c[4]))
