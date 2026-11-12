"""Print the dark-pixel bounding box of glyph components in a region (threshold 128).
usage: python -I glyphw.py STRIP x0 y0 x1 y1"""
import sys
from PIL import Image
src, x0, y0, x1, y1 = sys.argv[1], *map(int, sys.argv[2:6])
im = Image.open(src).crop((x0, y0, x1, y1))
w, h = im.size
px = im.load()
cols = [any(px[x, y] < 128 for y in range(h)) for x in range(w)]
runs, start = [], None
for x, c in enumerate(cols + [False]):
    if c and start is None:
        start = x
    elif not c and start is not None:
        runs.append((start, x - 1)); start = None
for a, b in runs:
    ys = [y for y in range(h) for x in range(a, b + 1) if px[x, y] < 128]
    print(f"cols {a+x0}-{b+x0} (w={b-a+1}) rows {min(ys)+y0}-{max(ys)+y0} (h={max(ys)-min(ys)+1})")
