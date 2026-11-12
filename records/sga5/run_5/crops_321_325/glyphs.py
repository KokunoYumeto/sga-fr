"""Bounding boxes of dark connected components in a region of a strip (8-connectivity).
usage: python -I glyphs.py PAGE STRIP X0 Y0 X1 Y1 [THRESH]"""
import sys

from PIL import Image

page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
th = int(sys.argv[7]) if len(sys.argv) > 7 else 140
im = Image.open(rf"C:\Users\user\Documents\sga_scan_check_20261105\run_5\b321_325\page_{page}_s{strip}.png")
px = im.load()
seen = set()
comps = []
for y in range(y0, y1):
    for x in range(x0, x1):
        if (x, y) in seen or px[x, y] >= th:
            continue
        stack = [(x, y)]
        seen.add((x, y))
        pts = []
        while stack:
            a, b = stack.pop()
            pts.append((a, b))
            for da in (-1, 0, 1):
                for db in (-1, 0, 1):
                    c, d = a + da, b + db
                    if x0 <= c < x1 and y0 <= d < y1 and (c, d) not in seen and px[c, d] < th:
                        seen.add((c, d))
                        stack.append((c, d))
        if len(pts) >= 15:
            xs = [p[0] for p in pts]
            ys = [p[1] for p in pts]
            comps.append((min(xs), min(ys), max(xs), max(ys), len(pts)))
for c in sorted(comps):
    print("x %4d-%4d  y %4d-%4d  h %2d  w %2d  n %3d" % (c[0], c[2], c[1], c[3], c[3] - c[1] + 1, c[2] - c[0] + 1, c[4]))
