"""measure.py PAGE STRIP x0 y0 x1 y1 -- print the dark-pixel row extent of each connected column run (glyph) in a box."""
import sys
from PIL import Image
page, strip, x0, y0, x1, y1 = sys.argv[1:7]
x0, y0, x1, y1 = map(int, (x0, y0, x1, y1))
im = Image.open(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\b291_295\page_%s_s%s.png" % (page, strip)).convert("L")
px = im.load()
th = 140
cols = []
for x in range(x0, x1):
    ys = [y for y in range(y0, y1) if px[x, y] < th]
    cols.append((x, (min(ys), max(ys)) if ys else None))
# group consecutive non-empty columns into glyph runs
runs, cur = [], None
for x, e in cols:
    if e:
        if cur and x == cur[1] + 1:
            cur = [cur[0], x, min(cur[2], e[0]), max(cur[3], e[1])]
        else:
            if cur:
                runs.append(cur)
            cur = [x, x, e[0], e[1]]
    else:
        if cur:
            runs.append(cur)
            cur = None
if cur:
    runs.append(cur)
for r in runs:
    print("x %d-%d  y %d-%d  h %d" % (r[0], r[1], r[2], r[3], r[3] - r[2]))
