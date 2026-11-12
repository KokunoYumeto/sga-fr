import re, sys
sys.stdout.reconfigure(encoding='utf-8')
t = open(r'C:\Users\user\Documents\sga_scan_check_20261105\sga5\diplomatic\s5.tex', encoding='utf-8').read().split('\n')
U = chr(92) + 'underline'
for lo, hi, name in [(1, 1940, 'I-II'), (1940, 4356, 'III'), (4356, 5400, 'IIIB part')]:
    seg = '\n'.join(t[lo-1:hi-1])
    sts = re.findall(r'\\begin\{statement\}\{([^}]*)\}(.*?)\\end\{statement\}', seg, re.S)
    withu = sum(1 for l, b in sts if U in b)
    print(name, len(sts), 'with underline:', withu)
    for l, b in sts[:4]:
        print('   ', l, '|', b[:160].replace('\n', ' '))
