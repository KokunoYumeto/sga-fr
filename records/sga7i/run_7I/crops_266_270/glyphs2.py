from PIL import Image
import numpy as np
src = r'C:/Users/user/Documents/sga_scan_check_20261105/run_7I/b266_270/page_270_s2.png'
out = r'C:/Users/user/Documents/sga_scan_check_20261105/run_7I/crops_266_270/'
img = Image.open(src).convert('L')
im = np.array(img).astype(float)
y0, y1 = 755, 825
def glyph(x0, x1, pad=4):
    g = im[y0:y1, x0-pad:x1+pad]
    return g
boxes = {'suspect': (1077,1095), 's_avons': (1032,1048), 's_nous': (891,907), 'e_que': (1662,1681), 'e_acc': (1217,1236)}
gl = {k: glyph(*v) for k, v in boxes.items()}
# vertical extent of each glyph
for k, g in gl.items():
    rows = (g < 150).any(axis=1)
    ys = np.where(rows)[0]
    print(k, g.shape, 'rows', ys.min()+y0, ys.max()+y0, 'ink', int((g<150).sum()))
# montage
H = y1-y0
W = sum(g.shape[1] for g in gl.values()) + 10*len(gl)
mont = np.full((H, W), 255.0)
x = 0
for k, g in gl.items():
    mont[:, x:x+g.shape[1]] = g
    x += g.shape[1] + 10
m = Image.fromarray(mont.clip(0,255).astype('uint8'))
m = m.resize((m.width*8, m.height*8), Image.NEAREST)
m.save(out + 'p270_glyph_montage.png')
# correlation: align by best shift
def best_corr(a, b):
    # a,b grayscale arrays same height; pad b width to a
    A = (255 - a); B = (255 - b)
    best = -1; bs = None
    for dx in range(-6, 7):
        for dy in range(-3, 4):
            Bs = np.roll(np.roll(B, dy, axis=0), dx, axis=1)
            w = min(A.shape[1], Bs.shape[1])
            a1 = A[:, :w].ravel(); b1 = Bs[:, :w].ravel()
            c = np.corrcoef(a1, b1)[0,1]
            if c > best: best = c; bs = (dx, dy)
    return best, bs
def padto(g, w):
    if g.shape[1] >= w: return g[:, :w]
    p = np.full((g.shape[0], w), 255.0); p[:, :g.shape[1]] = g; return p
w = max(g.shape[1] for g in gl.values())
G = {k: padto(v, w) for k, v in gl.items()}
for k in ['s_avons', 's_nous', 'e_que', 'e_acc']:
    print('suspect vs', k, best_corr(G['suspect'], G[k]))
print('e_que vs s_avons', best_corr(G['e_que'], G['s_avons']))
print('s_nous vs s_avons', best_corr(G['s_nous'], G['s_avons']))
print('e_que vs e_acc', best_corr(G['e_que'], G['e_acc']))
