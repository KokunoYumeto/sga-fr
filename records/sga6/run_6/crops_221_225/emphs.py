"""Tally the arguments of a command (default emph) in a line range of the SGA 6 diplomatic main.tex (read only).
usage: python -I emphs.py FIRST_LINE LAST_LINE [COMMAND]"""
import pathlib
import re
import sys
from collections import Counter

main = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex")
lines = main.read_text(encoding="utf-8").split("\n")
a, b = int(sys.argv[1]), int(sys.argv[2])
cmd = sys.argv[3] if len(sys.argv) > 3 else "emph"
seg = "\n".join(lines[a - 1:b])
c = Counter(re.findall("\\\\" + cmd + r"\{([^{}]*)\}", seg))
for k, v in c.most_common():
    sys.stdout.buffer.write(f"{v}  {k}\n".encode("utf-8"))
