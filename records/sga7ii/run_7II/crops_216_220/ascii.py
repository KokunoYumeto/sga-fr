import sys
from PIL import Image
src, x0, y0, x1, y1 = sys.argv[1], *map(int, sys.argv[2:6])
thr = int(sys.argv[6]) if len(sys.argv) > 6 else 160
im = Image.open(src).convert('L')
for y in range(y0, y1):
    row = ''
    for x in range(x0, x1):
        v = im.getpixel((x, y))
        row += '#' if v < 100 else ('+' if v < thr else ('.' if v < 230 else ' '))
    print(f'{y:4d} {row}')
