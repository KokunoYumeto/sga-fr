"""usage: python -I grepmain.py REGEX [lo hi]  -- search sga6 diplomatic main.tex, print line numbers and context"""
import re, sys
t = open(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex", encoding="utf-8").read().split("\n")
pat = re.compile(sys.argv[1])
lo = int(sys.argv[2]) if len(sys.argv) > 2 else 0
hi = int(sys.argv[3]) if len(sys.argv) > 3 else 10**9
n = 0
for i, l in enumerate(t, 1):
    for m in pat.finditer(l):
        n += 1
        if lo <= i <= hi:
            print(i, l[max(0, m.start() - 40):m.end() + 25])
print("total", n)
