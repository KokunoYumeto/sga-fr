import io, re, sys
D = r'C:/Users/user/Documents/sga_scan_check_20261105/sga6/diplomatic/main.tex'
L = io.open(D, encoding='utf-8').read().split('\n')
BS = chr(92)
names = sys.argv[1].split(',')
for n in names:
    tok = BS + n
    rx = re.compile(re.escape(tok) + r'(?![A-Za-z])')
    defs = [i + 1 for i, l in enumerate(L) if rx.search(l) and ('newcommand' in l or 'DeclareMathOperator' in l or 'def' + BS in l or (BS + 'def') in l or 'providecommand' in l)]
    uses = [i + 1 for i, l in enumerate(L) if rx.search(l)]
    vii = [u for u in uses if 10490 <= u <= 11931]
    print(n, 'defs:', defs[:5], 'uses:', len(uses), 'in VII:', len(vii), 'first VII uses:', vii[:8])
    for d in defs[:3]:
        print('   ', L[d - 1].strip()[:200])
