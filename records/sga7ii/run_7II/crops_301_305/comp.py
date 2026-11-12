import sys
from PIL import Image
import numpy as np
from scipy import ndimage
p=sys.argv[1]; x0,y0,x1,y1=map(int,sys.argv[2:6])
a=np.array(Image.open(p).convert('L'))[y0:y1,x0:x1]<140
lab,n=ndimage.label(a)
objs=ndimage.find_objects(lab)
rows=[]
for i,sl in enumerate(objs):
    rows.append((sl[1].start+x0, sl[1].stop+x0, sl[0].start+y0, sl[0].stop+y0, int((lab[sl]==i+1).sum())))
for r in sorted(rows): print('x %4d-%4d  y %4d-%4d  px %d'%r)
