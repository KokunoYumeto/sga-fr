"""In-memory simulation of the two marker moves (reads both layers, writes nothing)."""
import sys
sys.stdout.reconfigure(encoding='utf-8')
NL = chr(10)
base = 'C:/Users/user/Documents/sga_scan_check_20261105/sga6/'
M366 = '%%%%%%%%%%  scan idx 379  |  folio 366  %%%%%%%%%%'
M370 = '%%%%%%%%%%  scan idx 383  |  folio 370  %%%%%%%%%%'
L366 = r'\(2^\circ\)) \(1,\ldots,\xi^{r+1}\)'
for layer in ('diplomatic', 'current'):
    t = open(base + layer + '/main.tex', encoding='utf-8').read()
    old366 = L366 + NL + M366 + NL
    new366 = M366 + NL + L366 + NL
    print(layer, '366 old count', t.count(old366))
    t2 = t.replace(old366, new366)
    i = t2.find(M366); print(repr(t2[i-40:i+len(M366)+80]))
    old370 = r"\(\lambda'\geq\lambda\) et un" + NL + M370 + NL + "faisceau"
    new370 = r"\(\lambda'\geq\lambda\)" + NL + M370 + NL + "et un faisceau"
    print(layer, '370 old count', t.count(old370))
    t3 = t2.replace(old370, new370)
    i = t3.find(M370); print(repr(t3[i-60:i+len(M370)+40]))
