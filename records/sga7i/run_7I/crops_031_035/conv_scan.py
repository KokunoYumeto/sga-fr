import re
import sys

path = sys.argv[1]
lines = open(path, encoding='utf-8').read().split('\n')
folio = None
res = {'wedge': [], 'varepsilon': [], 'epsilon': []}
pats = {
    'wedge': re.compile(r'\\wedge(?![a-zA-Z])'),
    'varepsilon': re.compile(r'\\varepsilon(?![a-zA-Z])'),
    'epsilon': re.compile(r'\\epsilon(?![a-zA-Z])'),
}
for i, l in enumerate(lines, 1):
    m = re.search(r'scan idx (\d+)\s*\|\s*folio (\d+)', l)
    if m:
        folio = int(m.group(2))
        continue
    if l.lstrip().startswith('%'):
        continue
    for k, pat in pats.items():
        for mm in pat.finditer(l):
            res[k].append((folio, i, l[max(0, mm.start() - 45):mm.end() + 25]))

for k, v in res.items():
    fol = sorted(set(f for f, _, _ in v))
    print(k, len(v), 'folios:', fol)
print()
# wedge occurrences that are not obviously the ring Lambda (C_wedge or "over wedge")
lam_ctx = re.compile(r'C\}_\{?\\wedge|over\s+\$\\wedge|\\wedge\$-|\\wedge\}\{\\otimes')
for f, i, ctx in res['wedge']:
    if not lam_ctx.search(ctx):
        print('WEDGE-OTHER', f, i, ctx)
print()
for k in ('varepsilon', 'epsilon'):
    for f, i, ctx in res[k][:4]:
        print(k.upper(), f, i, ctx)
