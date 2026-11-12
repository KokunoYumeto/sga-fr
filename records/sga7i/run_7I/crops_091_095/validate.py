import json
import sys

findings_path, folder = sys.argv[1], sys.argv[2]
d = json.load(open(findings_path, encoding='utf-8'))
ok = True
counts = {}
for k, x in enumerate(d):
    p = x['page']
    src = open(f'{folder}/page_{p:03d}.tex', encoding='utf-8', newline='').read()
    kind = x['kind']
    c = counts.setdefault(p, [0, 0])
    if kind == 'misprint_in_print':
        c[1] += 1
        if 'corrected' not in x:
            print(k, p, 'MISSING corrected'); ok = False
    else:
        c[0] += 1
    t = x.get('tex')
    if t and src.count(t) < 1:
        print(k, p, 'tex not found:', repr(t)); ok = False
    f = x.get('fix')
    if f is not None:
        n = src.count(f['old'])
        if n != 1:
            print(k, p, 'old count', n, repr(f['old'])); ok = False
        if '%%%%%%%%%%' in f['old'] or '%%%%%%%%%%' in f['new']:
            print(k, p, 'touches marker'); ok = False
        if f['old'] == f['new']:
            print(k, p, 'old == new'); ok = False
    for key in ('page', 'where', 'scan', 'tex', 'kind', 'confidence', 'fix', 'note'):
        if key not in x:
            print(k, p, 'missing key', key); ok = False
print('entries', len(d), 'counts (normal, misprint):', counts)
print('ALL OK' if ok else 'PROBLEMS')
