import sys
from PIL import Image
# usage: helper.py crop SRC x0 y0 x1 y1 OUT [scale]   (coordinates in the source image's pixels)
#        helper.py size SRC
#        helper.py convert SRC OUT.png
#        helper.py frac SRC fx0 fy0 fx1 fy1 OUT [scale]  (coordinates as fractions of width/height)
#        helper.py count FILE STRING   (occurrences of STRING in FILE; STRING may use \n for line breaks)
cmd = sys.argv[1]
if cmd == "crop":
    src, x0, y0, x1, y1, out = sys.argv[2], *map(int, sys.argv[3:7]), sys.argv[7]
    scale = float(sys.argv[8]) if len(sys.argv) > 8 else 1.0
    im = Image.open(src).convert("L")
    c = im.crop((x0, y0, x1, y1))
    if scale != 1.0:
        c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    c.save(out)
    print(out, c.size)
elif cmd == "frac":
    src, out = sys.argv[2], sys.argv[7]
    fx0, fy0, fx1, fy1 = map(float, sys.argv[3:7])
    scale = float(sys.argv[8]) if len(sys.argv) > 8 else 1.0
    im = Image.open(src).convert("L")
    w, h = im.size
    c = im.crop((int(fx0 * w), int(fy0 * h), int(fx1 * w), int(fy1 * h)))
    if scale != 1.0:
        c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    c.save(out)
    print(out, c.size)
elif cmd == "size":
    im = Image.open(sys.argv[2])
    print(im.size, im.mode)
elif cmd == "convert":
    im = Image.open(sys.argv[2])
    im.save(sys.argv[3])
    print(sys.argv[3], im.size, im.mode)
elif cmd == "count":
    t = open(sys.argv[2], encoding="utf-8", newline="").read()
    s = sys.argv[3].replace("\\n", "\n")
    print(t.count(s))
