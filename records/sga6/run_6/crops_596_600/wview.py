import sys
from PIL import Image
# usage: wview.py in.tif out.png [x0 y0 x1 y1 scale]
im = Image.open(sys.argv[1]).convert("L")
print("size", im.size)
if len(sys.argv) > 3:
    x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
    sc = float(sys.argv[7]) if len(sys.argv) > 7 else 1.0
    im = im.crop((x0, y0, x1, y1))
    if sc != 1.0:
        im = im.resize((int(im.width * sc), int(im.height * sc)), Image.LANCZOS)
else:
    im = im.resize((im.width // 2, im.height // 2), Image.LANCZOS)
im.save(sys.argv[2])
print("out", im.size)
