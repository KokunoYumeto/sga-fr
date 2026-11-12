import sys
import numpy as np
from PIL import Image
from scipy import ndimage
# usage: components.py <png> x0 y0 x1 y1 [threshold]
src=sys.argv[1]; x0,y0,x1,y1=map(int,sys.argv[2:6]); th=int(sys.argv[6]) if len(sys.argv)>6 else 128
a=np.array(Image.open(src).convert('L'))[y0:y1,x0:x1]
m=a<th
lab,n=ndimage.label(m)
objs=ndimage.find_objects(lab)
res=[]
for i,s in enumerate(objs):
    ys,xs=s
    cnt=(lab[s]==i+1).sum()
    if cnt<4: continue
    res.append((xs.start+x0,xs.stop+x0,ys.start+y0,ys.stop+y0,cnt))
for r in sorted(res): print('x %4d-%4d  y %4d-%4d  n=%d'%r)
