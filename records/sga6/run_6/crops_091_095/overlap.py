"""Estimate the vertical overlap (in rows) between consecutive strips of a page.
usage: python -I overlap.py PAGE   (e.g. 092)"""
import sys

from PIL import Image, ImageChops, ImageStat

base = r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\b091_095\page_%s_s%d.png"
p = sys.argv[1]
for k in (1, 2, 3):
    a = Image.open(base % (p, k)).convert("L")
    b = Image.open(base % (p, k + 1)).convert("L")
    best = None
    for ov in range(5, 120):
        ca = a.crop((0, a.height - ov, a.width, a.height))
        cb = b.crop((0, 0, b.width, ov))
        d = ImageStat.Stat(ImageChops.difference(ca, cb)).mean[0]
        if best is None or d < best[0]:
            best = (d, ov)
    print("s%d-s%d overlap" % (k, k + 1), best[1], "mean diff %.2f" % best[0])
