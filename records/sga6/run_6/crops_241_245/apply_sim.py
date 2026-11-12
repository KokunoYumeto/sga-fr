import json, pathlib, sys, difflib
sys.stdout.reconfigure(encoding='utf-8')
B = pathlib.Path(r'C:\Users\user\Documents\sga_scan_check_20261105\run_6\b241_245')
F = json.loads(pathlib.Path(r'C:\Users\user\Documents\sga_scan_check_20261105\run_6\findings_241_245.json').read_text(encoding='utf-8'))
for p in range(241, 246):
    t0 = (B / f'page_{p}.tex').read_text(encoding='utf-8')
    t = t0
    for e in F:
        if e['page'] != p or not e['fix']:
            continue
        o, n = e['fix']['old'], e['fix']['new']
        c = t.count(o)
        if c != 1:
            print('FAIL in sequence', p, c, repr(o))
            continue
        t = t.replace(o, n)
    for x in difflib.unified_diff(t0.split('\n'), t.split('\n'), lineterm='', n=0):
        if x.startswith(('+', '-')) and not x.startswith(('+++', '---')):
            print(p, x[:260])
