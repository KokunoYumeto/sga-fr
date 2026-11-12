import re, sys
sys.stdout.reconfigure(encoding='utf-8')
BS = chr(92)
p = r'C:/Users/user/Documents/sga_scan_check_20261105/sga6/diplomatic/main.tex'
t = open(p, encoding='utf-8').read().split('\n')
idx = {}
for i, l in enumerate(t):
    m = re.search(r'folio (\d+) ', l)
    if l.startswith('%%%%%%%%%%  scan idx') and m:
        idx[int(m.group(1))] = i
a, b = idx[222], idx[274]
seg = '\n'.join(t[a:b])
def rx(s):
    return s.replace('@', BS + BS)
pats = {
    'mathbf L': rx(r'@mathbf\s*\{?L\}?'),
    'mathrm L': rx(r'@mathrm\s*\{?L\}?'),
    'mathbb L': rx(r'@mathbb\s*\{?L\}?'),
    'mathbf R': rx(r'@mathbf\s*\{?R\}?'),
    'mathbb R': rx(r'@mathbb\s*\{?R\}?'),
    'plain Lx^*': rx(r'(?<![A-Za-z@{])L[a-z]\^\*'),
    'plain Rx_*': rx(r'(?<![A-Za-z@{])R[a-z]_\*'),
    'Ob': rx(r'@Ob\b'),
}
for k, v in pats.items():
    print(k, len(re.findall(v, seg)))
print('lines', a + 1, b + 1)
fol = sorted((i, f) for f, i in idx.items())
def folio_of(line):
    best = None
    for i, f in fol:
        if i <= line:
            best = f
    return best
for name in ('mathbf L', 'Ob', 'mathrm L', 'plain Lx^*'):
    cnt = {}
    for i in range(a, b):
        n = len(re.findall(pats[name], t[i]))
        if n:
            cnt[folio_of(i)] = cnt.get(folio_of(i), 0) + n
    print(name, 'by folio', cnt)
key = 'renewcommand{' + BS + 'Ob}'
for i in range(a - 30, b):
    if key in t[i]:
        print('renew Ob at line', i + 1, 'folio', folio_of(i), t[i])
