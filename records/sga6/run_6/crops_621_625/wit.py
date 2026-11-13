"""Witness and scan helper for pages 621-625.

usage:
  python -I wit.py strips <img> <outprefix> <n>                     -> n horizontal strips
  python -I wit.py crop <img> <out> <x0> <y0> <x1> <y1> [scale]     (fractions 0..1 of width/height)
"""
import sys
from PIL import Image


def main():
    mode = sys.argv[1]
    if mode == "strips":
        src, pre, n = sys.argv[2], sys.argv[3], int(sys.argv[4])
        im = Image.open(src).convert("L")
        w, h = im.size
        step = h / n
        ov = int(0.03 * h)
        for i in range(n):
            y0 = max(0, int(i * step) - ov)
            y1 = min(h, int((i + 1) * step) + ov)
            im.crop((0, y0, w, y1)).save(f"{pre}_{i + 1}.png")
        print(w, h)
    elif mode == "crop":
        src, out = sys.argv[2], sys.argv[3]
        x0, y0, x1, y1 = (float(a) for a in sys.argv[4:8])
        scale = float(sys.argv[8]) if len(sys.argv) > 8 else 1.0
        im = Image.open(src).convert("L")
        w, h = im.size
        c = im.crop((int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h)))
        if scale != 1.0:
            c = c.resize((int(c.size[0] * scale), int(c.size[1] * scale)), Image.LANCZOS)
        c.save(out)
        print(c.size)


if __name__ == "__main__":
    main()
