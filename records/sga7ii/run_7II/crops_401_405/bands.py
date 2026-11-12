import sys
from PIL import Image
p=sys.argv[1]
im=Image.open(p).convert('L')
w,h=im.size
px=im.load()
rows=[]
for y in range(h):
    n=sum(1 for x in range(0,w,2) if px[x,y]<128)
    rows.append(n)
bands=[];inb=False
for y,n in enumerate(rows):
    if n>0 and not inb: start=y;inb=True
    if n==0 and inb: bands.append((start,y));inb=False
if inb: bands.append((start,h))
print(w,h)
for b in bands:
    # x extent
    xs=[x for x in range(w) for y in range(b[0],b[1],2) if px[x,y]<128]
    print(b, min(xs) if xs else None, max(xs) if xs else None)
