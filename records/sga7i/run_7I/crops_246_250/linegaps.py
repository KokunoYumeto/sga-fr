import sys
from PIL import Image
# usage: linegaps.py src lo hi [thresh]
# finds text lines, reports gaps with lo <= width <= hi px, plus the median word-space width per line
src = sys.argv[1]; lo = int(sys.argv[2]); hi = int(sys.argv[3])
th = int(sys.argv[4]) if len(sys.argv) > 4 else 140
im = Image.open(src).convert("L"); W, H = im.size; px = im.load()
rows = [sum(1 for x in range(0, W, 2) if px[x, y] < th) for y in range(H)]
lines = []; inl = False
for y, r in enumerate(rows):
    if r > 2 and not inl: inl = True; s = y
    elif r <= 2 and inl:
        inl = False
        if y - s > 12: lines.append((s, y))
for (a, b) in lines:
    cols = [any(px[x, y] < th for y in range(a, b)) for x in range(W)]
    xs = [x for x, c in enumerate(cols) if c]
    if not xs: continue
    runs = []; cur = None
    for x in range(xs[0], xs[-1] + 1):
        c = cols[x]
        if c != cur:
            runs.append([c, x, 0]); cur = c
        runs[-1][2] += 1
    gaps = [(x, w) for c, x, w in runs if not c]
    hits = [(x, w) for x, w in gaps if lo <= w <= hi]
    ws = sorted(w for x, w in gaps if w > hi)
    print(f"line y={a}-{b}: wordspaces~{ws[len(ws)//2] if ws else '-'} hits={hits}")
