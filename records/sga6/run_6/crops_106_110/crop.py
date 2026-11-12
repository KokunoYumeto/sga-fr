"""Crop a region of an image (strip PNG or witness TIFF) and upscale it, in grey.
usage: python -I crop.py IMAGE X0 Y0 X1 Y1 SCALE OUT_NAME   (coordinates in original pixels; X1/Y1 = 0 means full size)
A second form stacks two strips vertically before cropping:
       python -I crop.py --stack IMG_TOP Y_TOP_FROM IMG_BOTTOM Y_BOTTOM_TO X0 X1 SCALE OUT_NAME"""
import pathlib
import sys

from PIL import Image

here = pathlib.Path(__file__).parent
if sys.argv[1] == "--stack":
    top, ytop, bot, ybot, x0, x1, scale, out = sys.argv[2], int(sys.argv[3]), sys.argv[4], int(sys.argv[5]), \
        int(sys.argv[6]), int(sys.argv[7]), float(sys.argv[8]), sys.argv[9]
    a = Image.open(top).convert("L")
    b = Image.open(bot).convert("L")
    a = a.crop((x0, ytop, x1, a.height))
    b = b.crop((x0, 80, x1, ybot))  # strips overlap by 80 rows
    im = Image.new("L", (x1 - x0, a.height + b.height), 255)
    im.paste(a, (0, 0))
    im.paste(b, (0, a.height))
else:
    src, x0, y0, x1, y1, scale, out = sys.argv[1], *map(int, sys.argv[2:6]), float(sys.argv[6]), sys.argv[7]
    im = Image.open(src).convert("L")
    if x1 == 0:
        x1 = im.width
    if y1 == 0:
        y1 = im.height
    im = im.crop((x0, y0, x1, y1))
im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
dest = here / out
im.save(dest)
print(dest, im.size)
