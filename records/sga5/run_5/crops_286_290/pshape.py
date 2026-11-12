import sys
from PIL import Image

# usage: python -I pshape.py <strip.png> <x0> <y0> <x1> <y1> [threshold]
# For each connected component in the box that is about the size of a letter p/P
# (h 18-25, w 12-19), report rows with a right-side bowl vs rows with the stem only.
# Capital P of this typewriter: bowl about 12-13 rows, stem below about 9 rows.
# Small p: bowl about 15-16 rows, stem below about 6-7 rows.
src, x0, y0, x1, y1 = sys.argv[1:6]
thr = int(sys.argv[6]) if len(sys.argv) > 6 else 140
x0, y0, x1, y1 = map(int, (x0, y0, x1, y1))
im = Image.open(src).convert('L')
px = im.load()
W, H = x1 - x0, y1 - y0
dark = [[px[x0 + i, y0 + j] < thr for i in range(W)] for j in range(H)]
seen = [[False] * W for _ in range(H)]
for j in range(H):
    for i in range(W):
        if dark[j][i] and not seen[j][i]:
            stack = [(i, j)]
            seen[j][i] = True
            pts = []
            while stack:
                a, b = stack.pop()
                pts.append((a, b))
                for da in (-1, 0, 1):
                    for db in (-1, 0, 1):
                        c, d = a + da, b + db
                        if 0 <= c < W and 0 <= d < H and dark[d][c] and not seen[d][c]:
                            seen[d][c] = True
                            stack.append((c, d))
            xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
            minx, maxx, miny, maxy = min(xs), max(xs), min(ys), max(ys)
            h, w = maxy - miny + 1, maxx - minx + 1
            if not (17 <= h <= 26 and 11 <= w <= 20):
                continue
            rows = {}
            for (a, b) in pts:
                rows.setdefault(b, []).append(a)
            # a row belongs to the bowl if it has dark pixels in the right 40% of the glyph
            rlim = minx + int(w * 0.6)
            bowl = [b for b in range(miny, maxy + 1) if any(a >= rlim for a in rows.get(b, []))]
            bowl_end = max(bowl) if bowl else miny
            nb = bowl_end - miny + 1
            ns = maxy - bowl_end
            print('comp x %d-%d y %d-%d h %d w %d: bowl rows %d, stem rows below %d -> %s' % (
                minx + x0, maxx + x0, miny + y0, maxy + y0, h, w, nb, ns,
                'small p?' if ns <= 7 and nb >= 14 else ('CAPITAL P?' if ns >= 8 else '?')))
