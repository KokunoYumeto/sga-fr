import re, sys
sys.stdout.reconfigure(encoding='utf-8')
base = r'C:/Users/user/Documents/sga_scan_check_20261105/sga5/'
pat = re.compile(r'\\(re)?newcommand|\\def\\|\\let\\|providecommand|DeclareMathOperator')
for L in ['diplomatic', 'current']:
    print('===', L)
    lines = open(base + L + '/s5.tex', encoding='utf-8').read().split('\n')
    for i, l in enumerate(lines, 1):
        if i > 300 and pat.search(l):
            print(i, l[:220])
