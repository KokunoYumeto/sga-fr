import json, sys

sys.stdout.reconfigure(encoding='utf-8')
run = sys.argv[1]
data = json.load(open(run + '/findings_471_475_recheck.json', encoding='utf-8'))
ok = True
counts = {}
for i, f in enumerate(data):
    page = f['page']
    src = open('%s/b471_475/page_%d.tex' % (run, page), encoding='utf-8', newline='').read()
    assert '\r' not in src
    for key in ('page', 'where', 'scan', 'tex', 'kind', 'confidence', 'fix', 'note'):
        if key not in f:
            print('missing key', key, i); ok = False
    if f['kind'] == 'misprint_in_print' and 'corrected' not in f:
        print('missing corrected', i); ok = False
    if f['kind'] != 'misprint_in_print' and 'corrected' in f:
        print('corrected on non-misprint', i); ok = False
    n_tex = src.count(f['tex'])
    if n_tex != 1:
        print('tex count', n_tex, i, f['tex']); ok = False
    if f['fix'] is not None:
        old = f['fix']['old']
        n = src.count(old)
        if n != 1:
            print('fix old count', n, i, old); ok = False
        if '%%%%%%%%%%' in old:
            print('marker in old', i); ok = False
    c = counts.setdefault(page, [0, 0])
    c[1 if f['kind'] == 'misprint_in_print' else 0] += 1
print('ok' if ok else 'PROBLEMS', len(data))
print('; '.join('%d: %d/%d' % (p, c[0], c[1]) for p, c in sorted(counts.items())))
