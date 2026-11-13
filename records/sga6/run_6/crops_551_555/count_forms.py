import re, sys
sys.stdout.reconfigure(encoding='utf-8')
t = open(r'C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex', encoding='utf-8').read().split('\n')
lo, hi = int(sys.argv[1]), int(sys.argv[2])
seg = '\n'.join(t[lo-1:hi])
from collections import Counter
c = Counter(m.group(0) for m in re.finditer(r"(K|cl)\^\{?\x5c(circ|bullet)\}?", seg))
print(c)
