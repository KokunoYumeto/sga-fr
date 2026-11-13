import sys
from PIL import Image
# usage: helper.py convert  -> convert all w_*.pnm to png, print sizes
#        helper.py crop SRC x0 y0 x1 y1 OUT [scale]
cmd = sys.argv[1]
if cmd == "convert":
    import glob
    for f in sorted(glob.glob("w_*.pnm")):
        im = Image.open(f)
        print(f, im.size, im.mode)
        im.save(f[:-4] + ".png")
elif cmd == "crop":
    src, x0, y0, x1, y1, out = sys.argv[2], *map(int, sys.argv[3:7]), sys.argv[7]
    scale = float(sys.argv[8]) if len(sys.argv) > 8 else 1.0
    im = Image.open(src).convert("L")
    c = im.crop((x0, y0, x1, y1))
    if scale != 1.0:
        c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    c.save(out)
    print(out, c.size)
elif cmd == "small":
    src, out, scale = sys.argv[2], sys.argv[3], float(sys.argv[4])
    im = Image.open(src).convert("L")
    c = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
    c.save(out)
    print(out, c.size)
