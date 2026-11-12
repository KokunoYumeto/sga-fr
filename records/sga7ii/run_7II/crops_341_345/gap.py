import sys
from PIL import Image
# print min pixel value and count of pixels < thresholds in a box, plus a small ascii map
src, x0, y0, x1, y1 = sys.argv[1], *map(int, sys.argv[2:6])
im = Image.open(src).convert('L')
px = im.load()
vals = [px[x, y] for y in range(y0, y1) for x in range(x0, x1)]
print('min', min(vals), 'n<200', sum(v < 200 for v in vals), 'n<230', sum(v < 230 for v in vals), 'n<160', sum(v < 160 for v in vals))
for y in range(y0, y1):
    row = ''
    for x in range(x0, x1):
        v = px[x, y]
        row += '#' if v < 100 else ('+' if v < 170 else ('.' if v < 230 else ' '))
    print(row)
