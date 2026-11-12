import json
import sys
sys.stdout.reconfigure(encoding='utf-8')
from collections import Counter

run = sys.argv[1]
data = json.load(open(run + '/findings_041_045.json', encoding='utf-8'))
kinds = {'word', 'formula', 'symbol', 'font', 'underline', 'missing', 'extra', 'number',
         'punctuation', 'accent', 'misprint_in_print', 'marker', 'other'}
ok = True
counts = Counter()
for i, f in enumerate(data):
    page = f['page']
    tex = open('%s/b041_045/page_%03d.tex' % (run, page), encoding='utf-8').read()
    first, body = tex.split('\n', 1)
    for key in ('page', 'where', 'scan', 'tex', 'kind', 'confidence', 'fix', 'note'):
        if key not in f:
            print(i, 'missing key', key); ok = False
    if f['kind'] not in kinds:
        print(i, 'bad kind', f['kind']); ok = False
    if f['confidence'] not in ('high', 'medium', 'low'):
        print(i, 'bad confidence'); ok = False
    if f['kind'] == 'misprint_in_print':
        counts[(page, 'misprint')] += 1
        if f['fix'] is not None or 'corrected' not in f:
            print(i, 'misprint needs fix null and corrected'); ok = False
    else:
        counts[(page, 'normal')] += 1
        if 'corrected' in f:
            print(i, 'corrected only for misprints'); ok = False
    if f['fix'] is not None:
        old, new = f['fix']['old'], f['fix']['new']
        n = tex.count(old)
        if n != 1:
            print(i, 'page', page, 'old occurs', n, 'times:', repr(old)); ok = False
        if old in first:
            print(i, 'old in comment line'); ok = False
        if old == new:
            print(i, 'old == new'); ok = False
        # result of applying the fix, for a visual check
        after = tex.replace(old, new)
        pos = after.find(new)
        print('%2d p%d %-17s ok=%d  ...%s...' % (i, page, f['kind'], n, after[max(0, pos - 15):pos + len(new) + 10].replace('\n', '\\n')))
# overlapping fixes on the same page
for i, f in enumerate(data):
    for j, g in enumerate(data):
        if j <= i or f['page'] != g['page'] or not f['fix'] or not g['fix']:
            continue
        tex = open('%s/b041_045/page_%03d.tex' % (run, f['page']), encoding='utf-8').read()
        a = tex.find(f['fix']['old']); b = tex.find(g['fix']['old'])
        if a < b + len(g['fix']['old']) and b < a + len(f['fix']['old']):
            print('OVERLAP', i, j); ok = False
for page in range(41, 46):
    print(page, '%d/%d' % (counts[(page, 'normal')], counts[(page, 'misprint')]))
print('ALL OK' if ok else 'PROBLEMS')
