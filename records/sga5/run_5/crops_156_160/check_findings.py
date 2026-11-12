"""Check findings: every fix's old occurs exactly once in its page_NNN.tex (in the original, and when applied in
order in memory); no old/new touches a marker line. Prints counts per page."""
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
RUN = 'C:/Users/user/Documents/sga_scan_check_20261105/run_5/'
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
F = json.load(open(RUN + 'findings_156_160.json', encoding='utf-8'))
keys = {'page', 'where', 'scan', 'tex', 'kind', 'confidence', 'fix', 'note'}
kinds = set('word formula symbol font underline missing extra number punctuation accent misprint_in_print marker other'.split())
texts = {p: open(RUN + f'b156_160/page_{p}.tex', encoding='utf-8', newline='').read() for p in range(156, 161)}
work = dict(texts)
ok = True
counts = {}
for i, f in enumerate(F):
    p = f['page']
    mis = f['kind'] == 'misprint_in_print'
    counts.setdefault(p, [0, 0])[1 if mis else 0] += 1
    missing = keys - set(f)
    if missing or f['kind'] not in kinds or f['confidence'] not in ('high', 'medium', 'low'):
        ok = False
        print('FIELD PROBLEM', i, p, missing, f['kind'], f['confidence'])
    if mis and 'corrected' not in f:
        ok = False
        print('NO CORRECTED', i, p)
    if not mis and 'corrected' in f:
        ok = False
        print('CORRECTED ON NON-MISPRINT', i, p)
    fx = f['fix']
    if fx is None:
        continue
    old, new = fx['old'], fx['new']
    if '\r' in old or MARK.search(old) or MARK.search(new):
        ok = False
        print('MARKER/CR PROBLEM', i, p)
    n0 = texts[p].count(old)
    n1 = work[p].count(old)
    if n1 != 1:
        ok = False
    flag = '' if n1 == 1 else '  <-- PROBLEM'
    if n0 != 1 or n1 != 1:
        print(f'#{i} p{p} {f["kind"]}: original {n0}, sequential {n1}{flag} | {old[:60]!r}')
    work[p] = work[p].replace(old, new, 1)
print('counts (normal/misprint):', {p: f'{a}/{b}' for p, (a, b) in sorted(counts.items())})
print('ALL OK' if ok else 'PROBLEMS FOUND')
for p in range(156, 161):
    open(RUN + f'crops_156_160/after_{p}.tex', 'w', encoding='utf-8', newline='').write(work[p])
