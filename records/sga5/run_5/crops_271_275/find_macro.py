"""find_macro.py FILE FIRST LAST PATTERN: print matches of a regex between two line numbers (1-based, inclusive)."""
import re
import sys
sys.stdout.reconfigure(encoding="utf-8")
fn, a, b, pat = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
lines = open(fn, encoding="utf-8").read().split("\n")
rx = re.compile(pat)
for i in range(a - 1, min(b, len(lines))):
    for m in rx.finditer(lines[i]):
        print(i + 1, lines[i][max(0, m.start() - 35):m.end() + 25])
