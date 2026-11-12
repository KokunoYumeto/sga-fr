import re, sys, bisect
from collections import Counter
sys.stdout.reconfigure(encoding='utf-8')
t = open(r'C:\Users\user\Documents\sga_scan_check_20261105\sga5\diplomatic\s5.tex', encoding='utf-8').read()
M = re.compile(r'%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%')
marks = [(m.start(), int(m.group(2))) for m in M.finditer(t)]
pos = [p for p, _ in marks]
def pg(i):
    k = bisect.bisect(pos, i) - 1
    return marks[k][1] if k >= 0 else 0
for pat in sys.argv[1:]:
    c = Counter(pg(m.start()) for m in re.finditer(pat, t))
    print(repr(pat), sum(c.values()), sorted(c.items()))
