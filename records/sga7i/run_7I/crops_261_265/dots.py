import sys
from PIL import Image
import numpy as np
from collections import deque

def comps(path, box, thr):
    im = np.array(Image.open(path).convert('L')).astype(int)
    x0,y0,x1,y1 = box
    sub = im[y0:y1, x0:x1]
    mask = sub < thr
    seen = np.zeros_like(mask, bool)
    out = []
    H,W = mask.shape
    for y in range(H):
        for x in range(W):
            if mask[y,x] and not seen[y,x]:
                q = deque([(y,x)]); seen[y,x]=True; pts=[]
                while q:
                    cy,cx = q.popleft(); pts.append((cy,cx))
                    for dy in (-1,0,1):
                        for dx in (-1,0,1):
                            ny,nx = cy+dy,cx+dx
                            if 0<=ny<H and 0<=nx<W and mask[ny,nx] and not seen[ny,nx]:
                                seen[ny,nx]=True; q.append((ny,nx))
                ys=[p[0] for p in pts]; xs=[p[1] for p in pts]
                vals=[sub[p] for p in pts]
                out.append((x0+min(xs), y0+min(ys), max(xs)-min(xs)+1, max(ys)-min(ys)+1, len(pts), min(vals)))
    return out

path = sys.argv[1]; box = tuple(int(v) for v in sys.argv[2].split(',')); thr=int(sys.argv[3])
for c in comps(path, box, thr):
    print('x=%d y=%d w=%d h=%d n=%d min=%d' % c)
