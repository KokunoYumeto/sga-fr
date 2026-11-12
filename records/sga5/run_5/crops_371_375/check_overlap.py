import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
RUN = r'C:\Users\user\Documents\sga_scan_check_20261105\run_5'
F = json.load(open(RUN + r'\findings_371_375.json', encoding='utf-8'))
pages = sorted({d['page'] for d in F})
for p in pages:
    t = open(RUN + r'\b371_375\page_%d.tex' % p, encoding='utf-8', newline='').read()
    spans = []
    for i, d in enumerate(F):
        if d['page'] != p or d['fix'] is None:
            continue
        o = d['fix']['old']
        k = t.index(o)
        spans.append((k, k + len(o), i))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            print('OVERLAP page', p, F[a[2]]['where'], '|', F[b[2]]['where'])
    # apply all edits in order of the list, each old must still occur once
    u = t
    for d in F:
        if d['page'] != p or d['fix'] is None:
            continue
        o, n = d['fix']['old'], d['fix']['new']
        if u.count(o) != 1:
            print('SEQ FAIL', p, repr(o[:60]), u.count(o))
        u = u.replace(o, n, 1)
    print('== page', p, 'edits', len(spans))
    if p in (374, 375):
        print(u)
