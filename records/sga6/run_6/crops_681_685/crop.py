"""Helpers for the 681-685 check.

python -I crop.py strips <pgm> <outprefix> [n]       : split a witness page into n horizontal strips (PNG)
python -I crop.py crop <img> <out.png> x0 y0 x1 y1 [scale] : crop a box (pixel coords of <img>) and upscale
"""
import sys
from PIL import Image


def strips(src, prefix, n=4):
    im = Image.open(src)
    w, h = im.size
    step = h // n
    ov = 60
    for i in range(n):
        y0 = max(0, i * step - ov)
        y1 = min(h, (i + 1) * step + ov)
        im.crop((0, y0, w, y1)).save(f"{prefix}_s{i + 1}.png")
    print(w, h)


def crop(src, out, x0, y0, x1, y1, scale=2.0):
    im = Image.open(src)
    c = im.crop((x0, y0, x1, y1))
    if scale != 1:
        c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    c.save(out)
    print(im.size, c.size)


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "strips":
        strips(sys.argv[2], sys.argv[3], int(sys.argv[4]) if len(sys.argv) > 4 else 4)
    elif cmd == "crop":
        a = sys.argv
        crop(a[2], a[3], int(a[4]), int(a[5]), int(a[6]), int(a[7]), float(a[8]) if len(a) > 8 else 2.0)
