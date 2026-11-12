import sys
from PIL import Image
# usage: glyphbox.py SRC x0 y0 x1 y1  -> bounding box of dark pixels (<128) inside the window, and column profile
src = sys.argv[1]; x0,y0,x1,y1 = map(int, sys.argv[2:6])
im = Image.open(src).convert('L').crop((x0,y0,x1,y1))
w,h = im.size
px = im.load()
cols = [sum(1 for y in range(h) if px[x,y] < 140) for x in range(w)]
rows = [sum(1 for x in range(w) if px[x,y] < 140) for y in range(h)]
xs = [i for i,c in enumerate(cols) if c>0]; ys=[i for i,r in enumerate(rows) if r>0]
if xs and ys:
    print('bbox x', x0+xs[0], x0+xs[-1], 'w', xs[-1]-xs[0]+1, ' y', y0+ys[0], y0+ys[-1], 'h', ys[-1]-ys[0]+1)
print('cols', ''.join('#' if c>0 else '.' for c in cols))
