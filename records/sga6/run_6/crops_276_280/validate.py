import json, re, sys, pathlib
sys.stdout.reconfigure(encoding='utf-8')
BS = chr(92)
run = pathlib.Path(r'C:\Users\user\Documents\sga_scan_check_20261105\run_6')
d = json.loads((run / 'findings_276_280.json').read_text(encoding='utf-8'))
kinds = set('word formula symbol font underline missing extra number punctuation accent misprint_in_print marker other'.split())
ok = True
counts = {}
for i, x in enumerate(d):
    p = x['page']
    k = x['kind']
    assert k in kinds, (i, k)
    assert x['confidence'] in ('high', 'medium', 'low'), i
    counts.setdefault(p, [0, 0])
    counts[p][1 if k == 'misprint_in_print' else 0] += 1
    if k == 'misprint_in_print':
        assert 'corrected' in x, i
    t = (run / 'b276_280' / f'page_{p:03d}.tex').read_text(encoding='utf-8')
    f = x['fix']
    if f is not None:
        n = t.count(f['old'])
        bad_marker = '%%%%%%%%%%' in f['old'] or '%%%%%%%%%%' in f['new']
        print(i, p, k, 'old count =', n, 'MARKER!' if bad_marker else '')
        if n != 1 or bad_marker:
            ok = False
    else:
        print(i, p, k, 'fix null')
# marker notes: check replacement strings against both layers of main.tex
for L in ('diplomatic', 'current'):
    mt = (run.parent / 'sga6' / L / 'main.tex').read_text(encoding='utf-8')
    for i, x in enumerate(d):
        if x['kind'] != 'marker':
            continue
        note = x['note']
        a = note.index("replace '") + len("replace '")
        b = note.index("' by '", a)
        c0 = b + len("' by '")
        # the replacement ends at the last quote followed by ' (' or '.' or end
        m = re.search(r"'(?: \(|\.(?: |$)|$)", note[c0:])
        src = note[a:b].replace(BS + 'n', '\n')
        dst = note[c0:c0 + m.start()].replace(BS + 'n', '\n')
        c = mt.count(src)
        res = mt.replace(src, dst, 1)
        j = res.find(dst)
        print(L, 'marker note', i, 'page', x['page'], 'source count =', c,
              '| marker lines kept:', res.count('scan idx') == mt.count('scan idx'))
        print('    result:', repr(res[max(0, j - 40):j + len(dst) + 40])[:260])
        if c != 1:
            ok = False
print('counts per page (normal, misprint):', dict(sorted(counts.items())))
print('ALL OK' if ok else 'PROBLEM')
