"""Print the definitions of the given macros in the SGA 6 diplomatic main.tex.
usage: python -I macros.py NAME [NAME ...]"""
import re
import sys

t = open(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex", encoding="utf-8").read()
for name in sys.argv[1:]:
    pat = re.compile(r"(newcommand|providecommand|renewcommand|DeclareMathOperator|def)\*?\{?\\" + name + r"(?![A-Za-z])[^\n]*")
    hits = [m.group(0)[:140] for m in pat.finditer(t)]
    print(name, "::", hits if hits else "no definition found")
