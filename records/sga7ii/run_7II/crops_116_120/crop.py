"""Crop a region of a strip image, upscale it, and list the dark connected
components (glyph boxes) inside it.

usage: python crop.py PAGE STRIP x0 y0 x1 y1 SCALE OUTNAME
"""
import sys
from PIL import Image
import numpy as np

BASE = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II"
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
scale = float(sys.argv[7])
out = sys.argv[8]

im = Image.open(rf"{BASE}\b116_120\page_{page}_s{strip}.png").convert("L")
c = im.crop((x0, y0, x1, y1))
c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS).save(
    rf"{BASE}\crops_116_120\{out}")

a = np.array(c) < 140
h, w = a.shape
lab = np.zeros((h, w), int)
n = 0
boxes = []
for yy in range(h):
    for xx in range(w):
        if a[yy, xx] and not lab[yy, xx]:
            n += 1
            st = [(yy, xx)]
            lab[yy, xx] = n
            mnx = mxx = xx
            mny = mxy = yy
            cnt = 0
            while st:
                py, px = st.pop()
                cnt += 1
                mnx, mxx = min(mnx, px), max(mxx, px)
                mny, mxy = min(mny, py), max(mxy, py)
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        qy, qx = py + dy, px + dx
                        if 0 <= qy < h and 0 <= qx < w and a[qy, qx] and not lab[qy, qx]:
                            lab[qy, qx] = n
                            st.append((qy, qx))
            if cnt >= 15:
                boxes.append((mnx + x0, mny + y0, mxx - mnx + 1, mxy - mny + 1, cnt))
boxes.sort()
for b in boxes:
    print("x=%d y=%d w=%d h=%d px=%d" % b)
