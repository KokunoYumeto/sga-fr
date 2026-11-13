"""Count literal strings ('@' = backslash) over the whole diplomatic main.tex; with -v print up to 8 line hits."""
import sys
sys.stdout.reconfigure(encoding='utf-8')
B = chr(92)
lines = open(r'C:/Users/user/Documents/sga_scan_check_20261105/sga6/diplomatic/main.tex', encoding='utf-8').read().split('\n')
verbose = '-v' in sys.argv
for a in [x for x in sys.argv[1:] if x != '-v']:
    lit = a.replace('@', B)
    hits = [(i, l) for i, l in enumerate(lines, 1) if lit in l]
    print(f'{lit!s:40s} lines={len(hits)} total={sum(l.count(lit) for _, l in hits)}')
    if verbose:
        for i, l in hits[:8]:
            k = l.find(lit)
            print(f'   {i}: ...{l[max(0, k - 60):k + 80]}...')
