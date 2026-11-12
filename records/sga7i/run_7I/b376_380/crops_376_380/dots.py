import sys
from PIL import Image
im = Image.open(sys.argv[1]).convert('L')
x0,y0,x1,y1 = map(int, sys.argv[2:6])
thr = int(sys.argv[6]) if len(sys.argv) > 6 else 140
c = im.crop((x0,y0,x1,y1))
w,h = c.size
px = c.load()
seen = set()
comps = []
for y in range(h):
    for x in range(w):
        if px[x,y] < thr and (x,y) not in seen:
            stack=[(x,y)]; seen.add((x,y)); pts=[]
            while stack:
                a,b = stack.pop(); pts.append((a,b))
                for da in (-1,0,1):
                    for db in (-1,0,1):
                        u,v=a+da,b+db
                        if 0<=u<w and 0<=v<h and (u,v) not in seen and px[u,v]<thr:
                            seen.add((u,v)); stack.append((u,v))
            xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
            mn = min(px[p] for p in pts)
            comps.append((min(xs)+x0, max(xs)+x0, min(ys)+y0, max(ys)+y0, len(pts), mn))
for cc in sorted(comps):
    if cc[4] >= 2:
        print(cc)
