from PIL import Image
import numpy as np
src = r'C:/Users/user/Documents/sga_scan_check_20261105/run_7I/b266_270/page_270_s2.png'
im = np.array(Image.open(src).convert('L')).astype(float)
bg = np.median(im[740:760, 0:1700])
ink = (bg - im).clip(0, None)  # ink density
y0, y1 = 774, 812
def patch(cx, w=34):
    return ink[y0:y1, cx - w//2: cx + w//2]
# glyph centers from column runs
cands = {'suspect': (1077+1095)//2, 's_avons': (1032+1048)//2, 's_nous': (891+907)//2,
         'e_que': (1662+1681)//2}
P = {k: patch(c) for k, c in cands.items()}
def shift(a, dx, dy):
    return np.roll(np.roll(a, dy, 0), dx, 1)
def fit_single(target, tmpl):
    best = None
    for dx in range(-5, 6):
        for dy in range(-3, 4):
            t = shift(tmpl, dx, dy)
            # scale factor least squares
            s = (t*target).sum() / max((t*t).sum(), 1e-9)
            r = ((target - s*t)**2).sum()
            if best is None or r < best[0]: best = (r, dx, dy, s)
    return best
def fit_overlay(target, t1, t2):
    best = None
    for dx1 in range(-4, 5):
        for dy1 in range(-2, 3):
            a = shift(t1, dx1, dy1)
            for dx2 in range(-4, 5):
                for dy2 in range(-2, 3):
                    b = shift(t2, dx2, dy2)
                    ov = np.maximum(a, b)  # overstrike: darker wins
                    s = (ov*target).sum() / max((ov*ov).sum(), 1e-9)
                    r = ((target - s*ov)**2).sum()
                    if best is None or r < best[0]: best = (r, dx1, dy1, dx2, dy2, s)
    return best
T = P['suspect']
tot = (T**2).sum()
print('target energy', round(tot))
for k in ['e_que', 's_avons', 's_nous']:
    r = fit_single(T, P[k]); print('single', k, 'resid frac', round(r[0]/tot, 3), r[1:])
r = fit_overlay(T, P['e_que'], P['s_avons']); print('overlay e+s(avons) resid frac', round(r[0]/tot, 3), r[1:])
r = fit_overlay(T, P['e_que'], P['s_nous']); print('overlay e+s(nous) resid frac', round(r[0]/tot, 3), r[1:])
# control: a clean e fitted by another clean e, and by e+s overlay
ctrl = P['e_que']
