"""Print a region of a strip as ASCII art (# dark, + mid, . light) to inspect strokes pixel by pixel.
usage: python -I ascii.py PAGE STRIP X0 Y0 X1 Y1 [THRESH_DARK THRESH_MID]"""
import pathlib
import sys

from PIL import Image

here = pathlib.Path(__file__).resolve().parent
src = here.parent / "b061_065"
page, strip, x0, y0, x1, y1 = (int(a) for a in sys.argv[1:7])
td = int(sys.argv[7]) if len(sys.argv) > 7 else 110
tm = int(sys.argv[8]) if len(sys.argv) > 8 else 190
im = Image.open(src / f"page_{page:03d}_s{strip}.png").convert("L")
px = im.load()
print("     " + "".join(str((x // 10) % 10) if x % 10 == 0 else " " for x in range(x0, x1)))
for y in range(y0, y1):
    row = "".join("#" if px[x, y] < td else ("+" if px[x, y] < tm else ".") for x in range(x0, x1))
    print(f"{y:4d} {row}")
