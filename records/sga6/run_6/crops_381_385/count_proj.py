import re, sys
sys.stdout.reconfigure(encoding='utf-8')
L = open(r'C:/Users/user/Documents/sga_scan_check_20261105/sga6/diplomatic/main.tex', encoding='utf-8').read().split('\n')
lo, hi = int(sys.argv[1]), int(sys.argv[2])
BS = chr(92)
pats = [BS + BS + 'Projz', BS + BS + 'Proj_0', BS + BS + 'Proj(?![a-zA-Z_])',
        BS + BS + 'operatorname' + BS + '{Proj' + BS + '}_0',
        BS + BS + 'operatorname' + BS + '{Proj' + BS + '}(?!_)']
for p in pats:
    n = 0; lines = []
    for i in range(lo - 1, hi):
        k = len(re.findall(p, L[i]))
        if k:
            n += k; lines.append(i + 1)
    print(p, n, lines[:80])
