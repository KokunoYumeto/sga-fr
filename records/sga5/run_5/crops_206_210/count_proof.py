import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')
base = os.path.join('C:' + os.sep, 'Users', 'user', 'Documents', 'sga_scan_check_20261105', 'sga5')
for e in ('diplomatic', 'current'):
    t = open(os.path.join(base, e, 's5.tex'), encoding='utf-8').read()
    a = t.index('folio 204 ')
    b = t.index('\\section*{Exposé VI}')
    seg = t[a:b]
    bare = [m.start() for m in re.finditer(r'\\begin\{prooftext\}(?!\[)', seg)]
    folios = []
    for p in bare:
        k = seg.rfind('folio ', 0, p)
        folios.append(seg[k + 6:k + 9])
    print(e, 'bare prooftext in Exposé V:', len(bare), 'on folios', folios)
