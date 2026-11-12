import sys
from PIL import Image
# list small connected components (dots) in a strip: bbox, pixel count
src = sys.argv[1]
thr = 140
im = Image.open(src).convert('L')
W, H = im.size
px = im.load()
seen = bytearray(W * H)
out = []
for y in range(H):
    for x in range(W):
        i = y * W + x
        if seen[i] or px[x, y] >= thr:
            continue
        stack = [(x, y)]
        seen[i] = 1
        pts = []
        while stack:
            cx, cy = stack.pop()
            pts.append((cx, cy))
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < W and 0 <= ny < H:
                        j = ny * W + nx
                        if not seen[j] and px[nx, ny] < thr:
                            seen[j] = 1
                            stack.append((nx, ny))
        xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
        w = max(xs) - min(xs) + 1; h = max(ys) - min(ys) + 1
        if w <= 9 and h <= 9 and len(pts) >= 5:
            out.append((min(ys), min(xs), w, h, len(pts)))
for o in sorted(out):
    print('y=%d x=%d w=%d h=%d n=%d' % o)
