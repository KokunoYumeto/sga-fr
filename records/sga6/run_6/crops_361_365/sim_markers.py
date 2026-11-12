"""In-memory simulation of the folio-362 and folio-363 marker moves (reads both layers, writes nothing)."""
import sys
sys.stdout.reconfigure(encoding='utf-8')
NL = chr(10)
base = 'C:/Users/user/Documents/sga_scan_check_20261105/sga6/'
M362 = '%%%%%%%%%%  scan idx 375  |  folio 362  %%%%%%%%%%'
M363 = '%%%%%%%%%%  scan idx 376  |  folio 363  %%%%%%%%%%'
old362 = r'(1.8). Les opérations \(\psi^k\)' + NL + M362 + NL + 'définissent'
new362 = r'(1.8). Les' + NL + M362 + NL + r'opérations \(\psi^k\)' + NL + 'définissent'
old363 = '« dérivée logarithmique » est un' + NL + M363 + NL + 'homomorphisme de groupes'
new363 = '« dérivée logarithmique » est' + NL + M363 + NL + 'un homomorphisme de groupes'
for layer in ('diplomatic', 'current'):
    t = open(base + layer + '/main.tex', encoding='utf-8').read()
    print(layer, 'old362', t.count(old362), 'old363', t.count(old363))
    t2 = t.replace(old362, new362).replace(old363, new363)
    for M in (M362, M363):
        i = t2.find(M); print(repr(t2[i-60:i+len(M)+60]))
    # same result as move_marker.py with the anchors 'opérations \(\psi^k\)' and 'un\n' (--before)?
    import re
    MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
    def mm(t, folio, anchor):
        m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
        line = m.group(0); end = m.end() + 1
        t2 = t[:m.start()] + t[end:]
        k = t2.rfind(anchor, 0, m.start()); ls = t2.rfind(NL, 0, k) + 1
        if t2[ls:k].strip() == '':
            return t2[:ls] + line + NL + t2[ls:]
        return t2[:k] + NL + line + NL + t2[k:]
    t3 = mm(mm(t, 362, r'opérations \(\psi^k\)'), 363, 'un' + NL)
    for M in (M362, M363):
        i = t3.find(M); print('script:', repr(t3[i-60:i+len(M)+60]))
