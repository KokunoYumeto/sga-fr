"""Print every definition line (anywhere in the diplomatic main.tex of SGA 6) of the given macro names.
usage: python -I macros2.py NAME [NAME ...]"""
import sys

sys.stdout.reconfigure(encoding="utf-8")
lines = open(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex",
             encoding="utf-8").read().split("\n")
kinds = ("newcommand", "providecommand", "renewcommand", "DeclareMathOperator", "def")
for n in sys.argv[1:]:
    found = False
    for i, ln in enumerate(lines, 1):
        for k in kinds:
            for form in ("\\" + k + "{\\" + n + "}", "\\" + k + "*{\\" + n + "}", "\\" + k + "\\" + n + "{",
                         "\\" + k + "\\" + n + "#", "\\" + k + "{\\" + n + "}["):
                if form in ln:
                    j = ln.find(form)
                    print(n, i, ln[j:j + 160])
                    found = True
                    break
            else:
                continue
            break
    if not found:
        print(n, "NOT FOUND")
