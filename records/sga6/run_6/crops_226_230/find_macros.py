import re
import sys

path = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex"
names = sys.argv[1:]
lines = open(path, encoding="utf-8").read().split("\n")
pat = re.compile(r"(newcommand|providecommand|renewcommand|DeclareMathOperator|\\def)\*?\{?\\(" + "|".join(names) + r")(?![A-Za-z])")
for i, l in enumerate(lines, 1):
    if pat.search(l):
        print(i, l[:220])
