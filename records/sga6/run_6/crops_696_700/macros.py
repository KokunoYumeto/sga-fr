"""Print the preamble definitions of the given macro names in the diplomatic main.tex of SGA 6.
usage: python -I macros.py NAME [NAME ...]"""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
t = open(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex", encoding="utf-8").read()
head = t[:t.find("\\begin{document}")]
for n in sys.argv[1:]:
    pat = r"\\(?:newcommand|renewcommand|providecommand|DeclareMathOperator|def)\*?\{?\\" + n + r"(?![A-Za-z])[^\n]*"
    hits = [m.group(0) for m in re.finditer(pat, head)]
    print(n, "->", hits if hits else "NOT DEFINED IN PREAMBLE")
