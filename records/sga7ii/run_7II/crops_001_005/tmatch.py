import sys
from PIL import Image
thr = 140
def mask(src, box, pad=4):
    im = Image.open(src)
    x0, y0, x1, y1 = box
    reg = im.crop((x0-pad, y0-pad, x1+1+pad, y1+1+pad))
    w, h = reg.size; px = reg.load()
    return {(x, y) for y in range(h) for x in range(w) if px[x, y] < thr}, (w, h)
P = '../b001_005/page_005_s4.png'
target, _ = mask(P, (1272, 66, 1286, 83))
temps = {
 's_sorte': (P, (220,121,233,136)),
 's_inters': (P, (726,124,738,140)),
 'a_la': (P, (433,123,448,138)),
 'a_negat': (P, (1173,125,1187,141)),
 'a_local': (P, (1193,48,1207,63)),
 'a_anneau1': (P, (998,48,1012,62)),
 'a_anneau2': (P, (1076,48,1090,63)),
 'e_de': (P, (179,121,195,135)),
 'o_sorte': (P, (238,121,254,137)),
 'g_negat': (P, (1153,125,1168,142)),
}
def best(tm, tg):
    bestv = (0, None)
    for dx in range(-6, 7):
        for dy in range(-6, 7):
            sh = {(x+dx, y+dy) for (x, y) in tm}
            inter = len(sh & tg); uni = len(sh | tg)
            v = inter/uni
            if v > bestv[0]: bestv = (v, (dx, dy))
    return bestv
for k, (src, box) in temps.items():
    tm, _ = mask(src, box)
    print(k, 'IoU=%.3f' % best(tm, target)[0], best(tm, target)[1], 'npx', len(tm))
# overstrike hypotheses: union of an a and an s with relative shifts
sm, _ = mask(P, (220,121,233,136)); am, _ = mask(P, (1193,48,1207,63))
res = []
for ddx in range(-3, 4):
    for ddy in range(-4, 5):
        u = sm | {(x+ddx, y+ddy) for (x, y) in am}
        res.append((best(u, target)[0], ddx, ddy))
res.sort(reverse=True)
print('a+s union best', res[:3])
print('target npx', len(target))
def unbest(m1, m2):
    res = []
    for ddx in range(-3, 4):
        for ddy in range(-4, 5):
            u = m1 | {(x+ddx, y+ddy) for (x, y) in m2}
            res.append((round(best(u, target)[0], 3), ddx, ddy))
    res.sort(reverse=True)
    return res[:2]
s2, _ = mask(P, (726,124,738,140)); a2, _ = mask(P, (1173,125,1187,141)); a3, _ = mask(P, (433,123,448,138))
print('s+s', unbest(sm, s2))
print('s+s self', unbest(sm, sm))
print('a+a', unbest(am, a2))
print('a+a self', unbest(a2, a2))
print('a_negat+s_sorte', unbest(a2, sm))
print('a_la+s_inters', unbest(a3, s2))
