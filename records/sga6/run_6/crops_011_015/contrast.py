"""Contrast-stretched crop: python -I contrast.py FILE X0 Y0 X1 Y1 OUT SCALE [LO HI]"""
import sys
import numpy as np
from PIL import Image
f = sys.argv[1]
x0, y0, x1, y1 = map(int, sys.argv[2:6])
out = sys.argv[6]
scale = float(sys.argv[7])
im = np.array(Image.open(f).convert('L').crop((x0, y0, x1, y1))).astype(float)
lo = float(sys.argv[8]) if len(sys.argv) > 8 else np.percentile(im, 1)
hi = float(sys.argv[9]) if len(sys.argv) > 9 else np.percentile(im, 60)
im = np.clip((im - lo) / max(1, hi - lo) * 255, 0, 255).astype(np.uint8)
c = Image.fromarray(im)
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(out)
print('saved', out, c.size, 'lo', lo, 'hi', hi)
