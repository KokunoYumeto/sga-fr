import sys
from PIL import Image
src, x0, y0, x1, y1, thr = sys.argv[1], *map(int, sys.argv[2:7])
im = Image.open(src).convert('L')
for y in range(y0, y1):
    row = ''.join('#' if im.getpixel((x, y)) < thr else ('+' if im.getpixel((x,y)) < thr+40 else '.') for x in range(x0, x1))
    print(f'{y:4d} {row}')
