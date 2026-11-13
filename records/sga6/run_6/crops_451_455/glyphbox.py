"""glyphbox.py IMG x0 y0 x1 y1 [thr]: bounding boxes of dark connected components in a region (image pixels)."""
import sys
from PIL import Image
img, x0, y0, x1, y1 = sys.argv[1], *map(int, sys.argv[2:6])
thr = int(sys.argv[6]) if len(sys.argv) > 6 else 90
im = Image.open(img).convert("L").crop((x0, y0, x1, y1))
w, h = im.size; px = im.load()
seen = [[False]*w for _ in range(h)]
comps = []
for y in range(h):
    for x in range(w):
        if px[x, y] < thr and not seen[y][x]:
            st = [(x, y)]; seen[y][x] = True; xs = []; ys = []
            while st:
                a, b = st.pop(); xs.append(a); ys.append(b)
                for da in (-1, 0, 1):
                    for db in (-1, 0, 1):
                        c, d = a+da, b+db
                        if 0 <= c < w and 0 <= d < h and not seen[d][c] and px[c, d] < thr:
                            seen[d][c] = True; st.append((c, d))
            if len(xs) > 8:
                comps.append((min(xs)+x0, min(ys)+y0, max(xs)+x0, max(ys)+y0, len(xs)))
for c in sorted(comps):
    print("x %4d-%4d  y %4d-%4d  h %3d  w %3d  n %4d" % (c[0], c[2], c[1], c[3], c[3]-c[1]+1, c[2]-c[0]+1, c[4]))
