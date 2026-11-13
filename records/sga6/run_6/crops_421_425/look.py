import io, re, sys
D = r'C:/Users/user/Documents/sga_scan_check_20261105/sga6/diplomatic/main.tex'
C = r'C:/Users/user/Documents/sga_scan_check_20261105/sga6/current/main.tex'
def load(p):
    return io.open(p, encoding='utf-8').read().split('\n')
LD, LC = load(D), load(C)
BS = chr(92)
names = ['cS', 'Sym', 'codim', 'rang', 'Tor', 'Proj', 'Spec', 'cO', 'Projz']
for i, l in enumerate(LD[:4000]):
    for n in names:
        if (BS + n + '}' in l or BS + n + '{' in l or BS + n + ' ' in l) and ('newcommand' in l or 'DeclareMathOperator' in l or BS + 'def' in l):
            print('def', i + 1, l.strip())
            break
mode = sys.argv[1] if len(sys.argv) > 1 else ''
if mode == 'grep':
    pat = sys.argv[2]
    lo, hi = int(sys.argv[3]), int(sys.argv[4])
    which = sys.argv[5] if len(sys.argv) > 5 else 'dip'
    L = LD if which == 'dip' else LC
    for i in range(lo - 1, min(hi, len(L))):
        if pat in L[i]:
            print(which, i + 1, L[i][:300])
elif mode == 'show':
    lo, hi = int(sys.argv[2]), int(sys.argv[3])
    which = sys.argv[4] if len(sys.argv) > 4 else 'dip'
    L = LD if which == 'dip' else LC
    for i in range(lo - 1, hi):
        print(which, i + 1, L[i])
elif mode == 'diff':
    import difflib
    lo, hi, lo2, hi2 = map(int, sys.argv[2:6])
    a = LD[lo - 1:hi]
    b = LC[lo2 - 1:hi2]
    for l in difflib.unified_diff(a, b, 'dip', 'cur', lineterm='', n=0):
        print(l)
