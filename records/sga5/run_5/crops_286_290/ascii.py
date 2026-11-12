import sys
from PIL import Image

# usage: python -I ascii.py <strip.png> <x0> <y0> <x1> <y1> [threshold]
src, x0, y0, x1, y1 = sys.argv[1:6]
thr = int(sys.argv[6]) if len(sys.argv) > 6 else 140
x0, y0, x1, y1 = map(int, (x0, y0, x1, y1))
im = Image.open(src).convert('L')
px = im.load()
for y in range(y0, y1):
    row = ''.join('#' if px[x, y] < thr else ('+' if px[x, y] < 200 else '.') for x in range(x0, x1))
    print('%4d %s' % (y, row))
