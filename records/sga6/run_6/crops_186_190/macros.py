"""List definitions (incl. renewcommand) of macros in SGA 6 diplomatic main.tex, with line numbers (read only).
usage: python -I macros.py NAME [NAME ...]"""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
P = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex"
t = open(P, encoding="utf-8").read().split("\n")
BS = chr(92)
names = sys.argv[1:]
alt = "|".join(names)
pat = re.compile("(newcommand|providecommand|renewcommand|DeclareMathOperator|def)[*]?[{]?" + re.escape(BS) + "(" + alt + ")(?![A-Za-z])")
for i, l in enumerate(t, 1):
    if pat.search(l):
        print(i, l[:220])
mark = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
for i, l in enumerate(t, 1):
    m = mark.search(l)
    if m and 183 <= int(m.group(2)) <= 192:
        print("marker", m.group(2), "line", i)
