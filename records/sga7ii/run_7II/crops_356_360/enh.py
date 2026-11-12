import sys
from PIL import Image
import numpy as np
# usage: enh.py strip x0 y0 x1 y1 scale out  -> contrast-stretched crop (values < 250 darkened)
p, x0, y0, x1, y1, s, out = sys.argv[1], *map(int, sys.argv[2:7]), sys.argv[7]
im = Image.open(p).convert('L').crop((x0, y0, x1, y1))
a = np.array(im).astype(float)
lo, hi = a.min(), 255.0
# gamma stretch to reveal faint marks
b = ((a - lo) / (hi - lo + 1e-9)) ** 4 * 255
im2 = Image.fromarray(b.clip(0,255).astype('uint8'))
im2 = im2.resize((im2.width * s, im2.height * s), Image.NEAREST)
im2.save(out); print(out, im2.size)
