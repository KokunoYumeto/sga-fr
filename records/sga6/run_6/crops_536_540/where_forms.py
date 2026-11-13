"""For each literal form ('@' = backslash), print the folios (by marker) where it occurs in Expose X of the
diplomatic main.tex, with counts. Also prints definitions of given macro names anywhere in main.tex."""
import re, sys
sys.stdout.reconfigure(encoding='utf-8')
B = chr(92)
lines = open(r'C:/Users/user/Documents/sga_scan_check_20261105/sga6/diplomatic/main.tex', encoding='utf-8').read().split('\n')
MARK = re.compile(r'%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%')
args = sys.argv[1:]
defs = [a[4:] for a in args if a.startswith('def:')]
forms = [a.replace('@', B) for a in args if not a.startswith('def:')]
for name in defs:
    nm = B + name.replace('@', '')
    for i, l in enumerate(lines, 1):
        for cmd in ('newcommand', 'renewcommand', 'providecommand', 'DeclareMathOperator'):
            if (B + cmd + '{' + nm + '}') in l or (B + cmd + '*{' + nm + '}') in l:
                print(f'def {nm} line {i}: {l.strip()[:150]}')
folio = None
counts = {f: {} for f in forms}
for i, l in enumerate(lines, 1):
    m = MARK.search(l)
    if m:
        folio = int(m.group(2))
        continue
    if i < 13409 or i > 15269:
        continue
    for f in forms:
        c = l.count(f)
        if c:
            counts[f][folio] = counts[f].get(folio, 0) + c
for f in forms:
    print(f, sum(counts[f].values()), dict(sorted(counts[f].items())))
