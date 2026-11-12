import sys
from PIL import Image
# usage: ascii.py <png> x0 y0 x1 y1 [thr]
src = sys.argv[1]; x0,y0,x1,y1 = map(int, sys.argv[2:6])
thr = int(sys.argv[6]) if len(sys.argv) > 6 else 140
im = Image.open(src).convert('L'); px = im.load()
for y in range(y0, y1):
    print('%4d ' % y + ''.join('#' if px[x,y] < thr else ('+' if px[x,y] < 200 else '.') for x in range(x0, x1)))
