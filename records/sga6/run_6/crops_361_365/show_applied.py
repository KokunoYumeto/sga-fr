"""Print each page with the findings' fixes applied in order (in memory only)."""
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')
RUN = 'C:/Users/user/Documents/sga_scan_check_20261105/run_6/'
sys.argv = [sys.argv[0]]
ns = {}
exec(open(RUN + 'crops_361_365/build_findings.py', encoding='utf-8').read(), ns)
F = ns['F']
for p in (361, 362, 363, 364, 365):
    t = open(RUN + 'b361_365/page_%03d.tex' % p, encoding='utf-8').read()
    for d in F:
        if d['page'] == p and d['fix']:
            t = t.replace(d['fix']['old'], d['fix']['new'], 1)
    print('=' * 30, p)
    print(t)
