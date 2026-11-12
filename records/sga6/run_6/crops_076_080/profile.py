"""Print the dark-pixel row range of given column ranges of an image (to compare vertical positions of marks).
usage: python -I profile.py IMAGE THRESH Y0 Y1 X0:X1 [X0:X1 ...]"""
import sys

from PIL import Image

im = Image.open(sys.argv[1]).convert("L")
th = int(sys.argv[2])
y0, y1 = int(sys.argv[3]), int(sys.argv[4])
for spec in sys.argv[5:]:
    a, b = map(int, spec.split(":"))
    rows = [y for y in range(y0, y1) if any(im.getpixel((x, y)) < th for x in range(a, b))]
    print(spec, (min(rows), max(rows)) if rows else None)
