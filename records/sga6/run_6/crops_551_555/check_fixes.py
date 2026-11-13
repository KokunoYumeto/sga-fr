import json, sys, pathlib
sys.stdout.reconfigure(encoding='utf-8')
run = pathlib.Path(r'C:\Users\user\Documents\sga_scan_check_20261105\run_6')
d = json.load(open(run / 'findings_551_555.json', encoding='utf-8'))
ok = True
allowed = {'word','formula','symbol','font','underline','missing','extra','number','punctuation','accent','misprint_in_print','marker','other'}
from collections import Counter
cnt = Counter()
for i, x in enumerate(d):
    p = x['page']
    t = (run / 'b551_555' / f'page_{p}.tex').read_text(encoding='utf-8')
    if x['kind'] not in allowed: print(i, 'bad kind', x['kind']); ok = False
    if x['confidence'] not in ('high','medium','low'): print(i, 'bad conf'); ok = False
    for k in ('page','where','scan','tex','kind','confidence','fix','note'):
        if k not in x: print(i, 'missing key', k); ok = False
    if x['kind'] == 'misprint_in_print' and 'corrected' not in x: print(i, 'no corrected'); ok = False
    if x['kind'] != 'misprint_in_print' and 'corrected' in x: print(i, 'corrected on non-misprint'); ok = False
    cnt[(p, 'm' if x['kind']=='misprint_in_print' else 'n')] += 1
    f = x['fix']
    if f is not None:
        n = t.count(f['old'])
        if n != 1: print(i, p, 'old occurs', n, repr(f['old'][:80])); ok = False
        if '%%%%%%%%%%' in f['old'] or '%%%%%%%%%%' in f['new']: print(i, 'touches marker'); ok = False
        t2 = t.replace(f['old'], f['new'])
        print(i, p, x['kind'], 'OK ->', repr(f['new'][:90]))
    else:
        print(i, p, x['kind'], 'fix null')
print('counts', sorted(cnt.items()))
print('ALL OK' if ok else 'PROBLEMS')
