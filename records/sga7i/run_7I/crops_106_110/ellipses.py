import sys
import numpy as np
from PIL import Image
from scipy import ndimage

# usage: ellipses.py <strip png> [threshold]
# Finds runs of small round blobs (typewriter dots) spaced about one
# character pitch apart on a common baseline, and prints each run with its
# position and the number of blobs (the end blobs may be commas).
src = sys.argv[1]
thr = int(sys.argv[2]) if len(sys.argv) > 2 else 140
im = np.asarray(Image.open(src).convert("L"))
mask = im < thr
lab, n = ndimage.label(mask)
objs = ndimage.find_objects(lab)
blobs = []
for i, sl in enumerate(objs, start=1):
    ys, xs = sl
    h = ys.stop - ys.start
    w = xs.stop - xs.start
    area = int((lab[sl] == i).sum())
    if 6 <= w <= 16 and 6 <= h <= 17 and area >= 40:
        blobs.append((xs.start, ys.start, w, h, area))
blobs.sort(key=lambda b: (b[1] // 6, b[0]))
used = set()
runs = []
for i, b in enumerate(blobs):
    if i in used:
        continue
    run = [i]
    cur = b
    while True:
        nxt = None
        for j, c in enumerate(blobs):
            if j in used or j in run:
                continue
            dx = c[0] - cur[0]
            dy = abs((c[1] + c[3]) - (cur[1] + cur[3]))
            if 17 <= dx <= 30 and dy <= 6:
                nxt = j
                break
        if nxt is None:
            break
        run.append(nxt)
        cur = blobs[nxt]
    if len(run) >= 3:
        for j in run:
            used.add(j)
        runs.append([blobs[j] for j in run])
for r in sorted(runs, key=lambda r: (r[0][1], r[0][0])):
    hs = ",".join(str(b[3]) for b in r)
    print(f"y={r[0][1]:4d} x={r[0][0]:5d}..{r[-1][0]:5d} n={len(r)} heights={hs}")
