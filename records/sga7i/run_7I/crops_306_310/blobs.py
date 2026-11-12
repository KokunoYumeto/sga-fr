import sys
from PIL import Image
im = Image.open(sys.argv[1]).convert('L')
x0,y0,x1,y1 = map(int, sys.argv[2:6])
thr = int(sys.argv[6]) if len(sys.argv)>6 else 150
c = im.crop((x0,y0,x1,y1))
w,h = c.size
px = c.load()
seen = set()
blobs = []
for y in range(h):
    for x in range(w):
        if px[x,y] < thr and (x,y) not in seen:
            stack=[(x,y)]; seen.add((x,y)); pts=[]
            while stack:
                a,b = stack.pop(); pts.append((a,b))
                for da in (-1,0,1):
                    for db in (-1,0,1):
                        na,nb=a+da,b+db
                        if 0<=na<w and 0<=nb<h and (na,nb) not in seen and px[na,nb]<thr:
                            seen.add((na,nb)); stack.append((na,nb))
            xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
            mn=min(px[p] for p in pts)
            blobs.append((min(xs)+x0,min(ys)+y0,max(xs)+x0,max(ys)+y0,len(pts),mn))
for b in sorted(blobs): print(b)
