import sys
from PIL import Image
import numpy as np
from scipy import ndimage

def blobs(path, box):
    im = Image.open(path)
    a = np.array(im.crop(box)) < 128
    lab, n = ndimage.label(a)
    out = []
    for i in range(1, n+1):
        ys, xs = np.where(lab == i)
        out.append((xs.min()+box[0], ys.min()+box[1], xs.max()+box[0], ys.max()+box[1], len(ys)))
    out.sort()
    for o in out:
        print("x %d-%d y %d-%d area %d h %d w %d" % (o[0], o[2], o[1], o[3], o[4], o[3]-o[1]+1, o[2]-o[0]+1))

if __name__ == '__main__':
    p = sys.argv[1]
    box = tuple(int(v) for v in sys.argv[2:6])
    blobs(p, box)
