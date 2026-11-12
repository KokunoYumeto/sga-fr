import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')
run = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II"
path = run + r"\findings_371_375_recheck.json"
raw = open(path, 'rb').read()
print('CR bytes in JSON:', raw.count(b'\r'))
data = json.loads(raw.decode('utf-8'))
ctrl = re.compile('[\x00-\x08\x0b\x0c\x0e-\x1f]')
allowed_kinds = set('word formula symbol font underline missing extra number punctuation accent misprint_in_print marker other'.split())
counts = {}
for i, d in enumerate(data):
    p = d['page']
    tex = open(run + r"\b371_375\page_%d.tex" % p, 'rb').read().decode('utf-8')
    assert '\r' not in tex
    assert d['kind'] in allowed_kinds, d['kind']
    assert d['confidence'] in ('high', 'medium', 'low')
    for k in ('where', 'scan', 'tex', 'note'):
        assert isinstance(d[k], str) and d[k]
        if ctrl.search(d[k]):
            print('CONTROL CHAR in', i, k)
    mis = d['kind'] == 'misprint_in_print'
    counts.setdefault(p, [0, 0])[1 if mis else 0] += 1
    if mis:
        assert 'corrected' in d and d['corrected'], i
    else:
        assert 'corrected' not in d, i
    fx = d['fix']
    if fx is None:
        assert mis, i
        # the printed reading quoted in 'tex' should be on the page (first token check)
        probe = d['tex']
        print(i, p, 'fix null; tex substring count =', tex.count(probe))
        continue
    old, new = fx['old'], fx['new']
    for s in (old, new):
        if ctrl.search(s.replace('\n', '')):
            print('CONTROL CHAR in fix', i)
    n = tex.count(old)
    marker = '%%%%%%%%%%' in old or '%%%%%%%%%%' in new
    print(i, p, 'old occurs', n, 'marker touched' if marker else '', repr(old)[:80], '->', repr(new)[:80])
print('counts normal/misprint:', counts)
