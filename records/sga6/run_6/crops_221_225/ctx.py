"""Count and list markup in a line range of the SGA 6 diplomatic main.tex (read only).
usage: python -I ctx.py FIRST_LINE LAST_LINE PATTERN [MAX]"""
import pathlib
import re
import sys

main = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex")
lines = main.read_text(encoding="utf-8").split("\n")
a, b, pat = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
mx = int(sys.argv[4]) if len(sys.argv) > 4 else 60
rx = re.compile(pat.replace("@", r"\\"))
n = 0
for i in range(a - 1, min(b, len(lines))):
    hits = rx.findall(lines[i])
    if hits:
        n += len(hits)
        if mx > 0:
            mx -= 1
            sys.stdout.buffer.write(f"{i + 1}: {lines[i][:220]}\n".encode("utf-8"))
print("total matches:", n)
