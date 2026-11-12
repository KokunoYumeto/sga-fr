"""Print the definitions of given macros in the SGA 6 diplomatic main.tex."""
import re
import sys

t = open(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex", encoding="utf-8").read()
for name in sys.argv[1:]:
    pat = r"\\(?:newcommand|renewcommand|providecommand|DeclareMathOperator)\*?\{?\\" + name + r"(?![A-Za-z])[^\n]*"
    for m in re.finditer(pat, t):
        ln = t.count("\n", 0, m.start()) + 1
        print(name, ln, m.group(0)[:160])
