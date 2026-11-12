import sys
from PIL import Image
import numpy as np
p1,p2=sys.argv[1],sys.argv[2]
a=np.array(Image.open(p1).convert('L')).astype(float)
b=np.array(Image.open(p2).convert('L')).astype(float)
best=None
for ov in range(5,400):
    if ov>a.shape[0] or ov>b.shape[0]: break
    A=a[-ov:,:]; B=b[:ov,:]
    w=min(A.shape[1],B.shape[1])
    d=np.abs(A[:,:w]-B[:,:w]).mean()
    ink=(A<128).sum()
    if best is None or d<best[0]: best=(d,ov,ink)
print(best)
