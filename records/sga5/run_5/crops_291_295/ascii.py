"""ascii.py PAGE STRIP x0 y0 x1 y1 [TH] -- print a box of a strip as ASCII art (# dark)."""
import sys
from PIL import Image
page, strip, x0, y0, x1, y1 = sys.argv[1:7]
th = int(sys.argv[7]) if len(sys.argv) > 7 else 140
im = Image.open(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\b291_295\page_%s_s%s.png" % (page, strip)).convert("L")
px = im.load()
for y in range(int(y0), int(y1)):
    print("%4d " % y + "".join("#" if px[x, y] < th else "." for x in range(int(x0), int(x1))))
