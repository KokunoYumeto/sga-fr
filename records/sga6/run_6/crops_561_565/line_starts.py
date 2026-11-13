"""line_starts.py FOLIO : leftmost dark pixel of each text line of the witness page (full resolution)."""
import sys, pathlib
from PIL import Image
HERE = pathlib.Path(__file__).resolve().parent
folio = int(sys.argv[1])
im = Image.open(HERE / f"wit_{folio}.png").convert("L")
w, h = im.size
px = im.load()
rows = []
for y in range(h):
    dark = [x for x in range(150, w - 150) if px[x, y] < 128]
    rows.append((min(dark), max(dark)) if dark else None)
# group consecutive rows with ink into lines
y = 0
while y < h:
    if rows[y] is None:
        y += 1
        continue
    y0 = y
    xs = []
    while y < h and rows[y] is not None:
        xs.append(rows[y][0]); y += 1
    if y - y0 >= 8:
        print(f"y {y0:4d}-{y:4d}  left {min(xs):4d}")
