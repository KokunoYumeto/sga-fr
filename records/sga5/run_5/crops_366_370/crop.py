"""crop.py STRIP_PNG X0 Y0 X1 Y1 OUT_NAME [SCALE]  -- crop a box of a strip, optionally enlarge, save in this folder"""
import sys, pathlib
from PIL import Image
src = pathlib.Path(sys.argv[1])
x0, y0, x1, y1 = map(int, sys.argv[2:6])
out = pathlib.Path(__file__).parent / sys.argv[6]
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 2.0
im = Image.open(src)
c = im.crop((x0, y0, x1, y1))
if scale != 1:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(out)
print(out, im.size, c.size)
