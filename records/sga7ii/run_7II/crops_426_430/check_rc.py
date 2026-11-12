import json, sys, collections
d = json.load(open(sys.argv[1], encoding='utf-8'))
base = sys.argv[2]
cnt = collections.Counter()
ok = True
texts = {}
for x in d:
    p = x['page']
    t = texts.setdefault(p, open(f"{base}/page_{p}.tex", encoding='utf-8', newline='').read())
    mis = x['kind'] == 'misprint_in_print'
    cnt[(p, mis)] += 1
    for k in ('page', 'where', 'scan', 'tex', 'kind', 'confidence', 'fix', 'note'):
        if k not in x:
            print('MISSING KEY', k, x); ok = False
    if mis and 'corrected' not in x:
        print('NO corrected', x['where']); ok = False
    f = x['fix']
    if f is None:
        continue
    n = t.count(f['old'])
    if n != 1:
        print('NOT UNIQUE', p, n, repr(f['old'])); ok = False
    if '%%%%%%%%%%' in f['old']:
        print('MARKER IN OLD', p); ok = False
    # apply to a copy to check sequential application
    texts[p] = t.replace(f['old'], f['new'], 1)
for p in sorted({k[0] for k in cnt}):
    print(p, f"{cnt[(p, False)]}/{cnt[(p, True)]}")
print('OK' if ok else 'PROBLEMS')
