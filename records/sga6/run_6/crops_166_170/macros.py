"""List the definitions of some macros in SGA 6 diplomatic main.tex (read only)."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
P = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex"
t = open(P, encoding="utf-8").read().split("\n")
names = sys.argv[1:]
pat = re.compile(r"(newcommand|providecommand|renewcommand|DeclareMathOperator)\*?\{?\\(" + "|".join(names) + r")\}")
for i, l in enumerate(t, 1):
    if pat.search(l):
        print(i, l[:220])
