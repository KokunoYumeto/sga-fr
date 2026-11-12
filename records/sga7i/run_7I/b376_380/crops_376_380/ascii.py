import sys
from PIL import Image
im = Image.open(sys.argv[1]).convert('L')
x0,y0,x1,y1 = map(int, sys.argv[2:6])
thr = int(sys.argv[6]) if len(sys.argv) > 6 else 140
for y in range(y0,y1):
    print(''.join('#' if im.getpixel((x,y)) < thr-30 else ('+' if im.getpixel((x,y)) < thr else '.') for x in range(x0,x1)), y)
