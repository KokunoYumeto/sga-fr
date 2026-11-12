"""Find literal strings in the diplomatic s5.tex (or a given file); print counts and line numbers.
usage: python -I find.py [--file PATH] [--lines A-B] STRING [STRING ...]"""
import sys

sys.stdout.reconfigure(encoding="utf-8")
args = sys.argv[1:]
path = r"C:\Users\user\Documents\sga_scan_check_20261105\sga5\diplomatic\s5.tex"
rng = None
if args and args[0] == "--file":
    path = args[1]
    args = args[2:]
if args and args[0] == "--lines":
    a, b = args[1].split("-")
    rng = (int(a), int(b))
    args = args[2:]
lines = open(path, encoding="utf-8").read().split("\n")
for s in args:
    hits = [i + 1 for i, l in enumerate(lines) if s in l and (rng is None or rng[0] <= i + 1 <= rng[1])]
    print(repr(s), len(hits), hits[:60])
