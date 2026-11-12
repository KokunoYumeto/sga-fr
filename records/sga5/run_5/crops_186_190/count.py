"""Count literal occurrences of strings in s5.tex (whole file, and lines 5800-6200), printing line numbers.
usage: python -I count.py STRING [STRING ...]"""
import sys

SRC = r"C:/Users/user/Documents/sga_scan_check_20261105/sga5/diplomatic/s5.tex"
lines = open(SRC, encoding="utf-8").read().split("\n")
sys.stdout.reconfigure(encoding="utf-8")
for s in sys.argv[1:]:
    tot = sum(l.count(s) for l in lines)
    where = [i + 1 for i, l in enumerate(lines) if s in l]
    print(repr(s), "total", tot, "lines", where[:60])
