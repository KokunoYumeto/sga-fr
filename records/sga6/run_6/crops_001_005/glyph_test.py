"""IoU test: is the last glyph of 'corpa' (p. 4) an 'a', an 's', or an a/s overstrike?"""
import sys
import numpy as np
from PIL import Image

im = np.array(Image.open(sys.argv[1]).convert('L')).astype(float)
TH = float(sys.argv[2]) if len(sys.argv) > 2 else 110


def glyph(cx, cy=177, hw=16, hh=24):
    cx, cy = int(round(cx)), int(round(cy))
    return im[cy - hh:cy + hh, cx - hw:cx + hw] < TH


g = glyph(880.4)
a = glyph(1149.5)
s = glyph(1174.8)


def shift(m, dx, dy):
    out = np.zeros_like(m)
    h, w = m.shape
    ys = slice(max(0, dy), min(h, h + dy)); yd = slice(max(0, -dy), min(h, h - dy))
    xs = slice(max(0, dx), min(w, w + dx)); xd = slice(max(0, -dx), min(w, w - dx))
    out[ys, xs] = m[yd, xd]
    return out


def iou(p, q):
    return (p & q).sum() / max(1, (p | q).sum())


def best(t):
    return max((iou(g, shift(t, dx, dy)), dx, dy) for dx in range(-6, 7) for dy in range(-4, 5))


print('ink pixels: glyph', g.sum(), 'a', a.sum(), 's', s.sum())
print('best IoU with a      :', best(a))
print('best IoU with s      :', best(s))
res = []
for rdx in range(-3, 4):
    for rdy in range(-2, 3):
        u = a | shift(s, rdx, rdy)
        res.append(best(u) + (rdx, rdy))
print('best IoU with a|s     :', max(res))
