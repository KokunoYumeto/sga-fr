import sys
from PIL import Image

# usage: profile.py <src.png> <x0> <x1> <y_text0> <y_text1> <y_ul0> <y_ul1> [thresh]
# Prints dark-column runs for the text band and for the underline band.
src = sys.argv[1]
x0, x1, yt0, yt1, yu0, yu1 = map(int, sys.argv[2:8])
thr = int(sys.argv[8]) if len(sys.argv) > 8 else 140
im = Image.open(src).convert("L")
px = im.load()

def runs(y0, y1):
    cols = []
    for x in range(x0, x1):
        dark = any(px[x, y] < thr for y in range(y0, y1))
        cols.append(dark)
    out = []
    start = None
    for i, d in enumerate(cols):
        if d and start is None:
            start = i
        if not d and start is not None:
            out.append((x0 + start, x0 + i - 1))
            start = None
    if start is not None:
        out.append((x0 + start, x0 + len(cols) - 1))
    return out

print("text runs:", runs(yt0, yt1))
print("underline runs:", runs(yu0, yu1))
