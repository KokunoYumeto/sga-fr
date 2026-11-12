import sys
from PIL import Image
import numpy as np
from scipy import ndimage
path=sys.argv[1]; thr=int(sys.argv[2])
im=np.array(Image.open(path).convert('L')).astype(int)
mask=im<thr
lab,n=ndimage.label(mask,structure=np.ones((3,3)))
objs=ndimage.find_objects(lab)
res=[]
for i,sl in enumerate(objs):
    ys,xs=sl
    h=ys.stop-ys.start; w=xs.stop-xs.start
    cnt=int((lab[sl]==i+1).sum())
    if cnt<=30 and h<=7 and w<=7:
        # isolation: no other dark pixels within 10 px except itself
        y0=max(0,ys.start-10); y1=min(im.shape[0],ys.stop+10); x0=max(0,xs.start-10); x1=min(im.shape[1],xs.stop+10)
        region=lab[y0:y1,x0:x1]
        others=set(np.unique(region))-{0,i+1}
        if not others:
            mn=int(im[sl][lab[sl]==i+1].min())
            res.append((xs.start,ys.start,w,h,cnt,mn))
for r in res: print('x=%d y=%d w=%d h=%d n=%d min=%d'%r)
print('total isolated small comps:',len(res))
