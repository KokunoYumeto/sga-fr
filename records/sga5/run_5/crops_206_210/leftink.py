"""usage: python -I leftink.py PAGE STRIP
Prints, for each text line of the strip (runs of rows with dark pixels), its y range and the x of its leftmost dark pixel."""
import sys, os
from PIL import Image

base = os.path.join('C:' + os.sep, 'Users', 'user', 'Documents', 'sga_scan_check_20261105', 'run_5')
page, strip = sys.argv[1], sys.argv[2]
im = Image.open(os.path.join(base, 'b206_210', 'page_%s_s%s.png' % (page, strip))).convert('L')
w, h = im.size
px = im.load()
x0 = 30  # skip the scan's dark left edge
rows = []
for y in range(h):
    xs = [x for x in range(x0, w - 30) if px[x, y] < 110]
    rows.append(min(xs) if len(xs) > 3 else None)
y = 0
while y < h:
    if rows[y] is None:
        y += 1
        continue
    y1 = y
    while y1 < h and rows[y1] is not None:
        y1 += 1
    if y1 - y > 6:
        print('rows %4d-%4d  left x %4d' % (y, y1, min(r for r in rows[y:y1])))
    y = y1
