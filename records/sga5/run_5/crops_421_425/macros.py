import re
import sys

src = r"C:\Users\user\Documents\sga_scan_check_20261105\sga5\diplomatic\s5.tex"
lines = open(src, encoding="utf-8").read().split("\n")
names = sys.argv[1].split(",")
for name in names:
    pat = re.compile(r"(newcommand|providecommand|renewcommand|DeclareMathOperator)\*?\{?\\" + re.escape(name) + r"\}?[\[{]")
    for i, l in enumerate(lines, 1):
        if pat.search(l):
            print(name, i, l[:160])
if len(sys.argv) > 2:
    word = sys.argv[2]
    lo, hi = (int(x) for x in sys.argv[3].split("-")) if len(sys.argv) > 3 else (1, len(lines))
    for i, l in enumerate(lines, 1):
        if lo <= i <= hi and word in l:
            j = l.find(word)
            print(i, "...", l[max(0, j - 70): j + 70])
