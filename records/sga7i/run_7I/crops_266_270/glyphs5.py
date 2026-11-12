from PIL import Image
import numpy as np
src = r'C:/Users/user/Documents/sga_scan_check_20261105/run_7I/b266_270/page_270_s2.png'
im = np.array(Image.open(src).convert('L')).astype(float)
bg = np.median(im[740:760, 0:1700])
ink = (bg - im).clip(0, None)
y0, y1 = 774, 812
def patch(x0, x1, w=34):
    c = (x0 + x1)//2
    return ink[y0:y1, c - w//2: c + w//2]
E = {'e189': (189,207), 'e282': (282,301), 'e561': (561,580), 'e1662': (1662,1681)}
S = {'s308': (308,324), 's400': (400,417), 's891': (891,907), 's1032': (1032,1048)}
X = {'suspect': (1077,1095)}
P = {k: patch(*v) for k, v in {**E, **S, **X}.items()}
def shift(a, dx, dy): return np.roll(np.roll(a, dy, 0), dx, 1)
def fit(target, tmpl):
    best = None
    for dx in range(-5, 6):
        for dy in range(-3, 4):
            t = shift(tmpl, dx, dy)
            s = (t*target).sum() / max((t*t).sum(), 1e-9)
            r = ((target - s*t)**2).sum() / (target**2).sum()
            if best is None or r < best: best = r
    return best
def avg_fit(target, group, exclude=None):
    vals = [fit(target, P[k]) for k in group if k != exclude]
    return round(float(np.mean(vals)), 3), round(float(np.min(vals)), 3)
for k in list(E) + list(S) + list(X):
    print(k, 'ink', int(P[k].sum()/1000), 'vs e (mean,min):', avg_fit(P[k], E, k), ' vs s (mean,min):', avg_fit(P[k], S, k))
