"""line_starts.py FOLIO : left-most ink x of each text line of the witness page (wit_FOLIO.png), to judge indents."""
import pathlib, sys
from PIL import Image
HERE = pathlib.Path(__file__).resolve().parent
folio = int(sys.argv[1])
im = Image.open(HERE / f"wit_{folio}.png").convert("L")
w, h = im.size
px = im.load()
x0, x1 = 120, w - 120  # skip the scan's edge marks
rows = []
for y in range(h):
    ink = [x for x in range(x0, x1, 2) if px[x, y] < 110]
    rows.append(min(ink) if ink else None)
y = 0
while y < h:
    if rows[y] is None:
        y += 1
        continue
    y2 = y
    while y2 < h and rows[y2] is not None:
        y2 += 1
    if y2 - y >= 8:
        left = min(r for r in rows[y:y2])
        print(f"y {y:4d}-{y2:4d}  left {left}")
    y = y2
