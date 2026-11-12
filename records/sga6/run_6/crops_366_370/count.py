import sys
sys.stdout.reconfigure(encoding='utf-8')
L = open(r'C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex', encoding='utf-8').read().split('\n')
a, b = int(sys.argv[1]), int(sys.argv[2])
t = '\n'.join(L[a-1:b])
for s in sys.argv[3:]:
    print(repr(s), t.count(s))
