import sys
from PIL import Image

# usage: python -I glyphs.py <strip.png> x0 y0 x1 y1 [thr]
# prints the connected dark components in the box (bbox, size) and an ASCII map of the box
src = sys.argv[1]
x0, y0, x1, y1 = map(int, sys.argv[2:6])
thr = int(sys.argv[6]) if len(sys.argv) > 6 else 140
im = Image.open(src)
seen = set()
comps = []
for y in range(y0, y1):
    for x in range(x0, x1):
        if (x, y) in seen or im.getpixel((x, y)) >= thr:
            continue
        st = [(x, y)]
        seen.add((x, y))
        pts = []
        while st:
            a, b = st.pop()
            pts.append((a, b))
            for da in (-1, 0, 1):
                for db in (-1, 0, 1):
                    c, d = a + da, b + db
                    if x0 <= c < x1 and y0 <= d < y1 and (c, d) not in seen and im.getpixel((c, d)) < thr:
                        seen.add((c, d))
                        st.append((c, d))
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]
        if len(pts) >= 6:
            comps.append((min(xs), min(ys), max(xs), max(ys), len(pts)))
for c in sorted(comps):
    print("comp x%d-%d y%d-%d n=%d" % (c[0], c[2], c[1], c[3], c[4]))
for y in range(y0, y1):
    print("%4d " % y + "".join("#" if im.getpixel((x, y)) < thr else "." for x in range(x0, x1)))
