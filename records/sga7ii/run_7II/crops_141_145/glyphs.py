import sys
from PIL import Image
import numpy as np
from scipy import ndimage
def boxes(f, x0, y0, x1, y1, thr=140):
    a = np.array(Image.open(f).convert('L'))[y0:y1, x0:x1] < thr
    lab, n = ndimage.label(a, structure=np.ones((3,3)))
    out=[]
    for s in ndimage.find_objects(lab):
        if s is None: continue
        b=(s[1].start + x0, s[0].start + y0, s[1].stop + x0, s[0].stop + y0)
        w,h=b[2]-b[0],b[3]-b[1]
        if w*h>=6: out.append((b,w,h))
    return sorted(out)
if __name__=='__main__':
    f=sys.argv[1]; x0,y0,x1,y1=map(int,sys.argv[2:6])
    for b,w,h in boxes(f,x0,y0,x1,y1): print(b,w,h)
