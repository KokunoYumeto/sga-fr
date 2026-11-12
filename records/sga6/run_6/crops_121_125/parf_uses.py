"""List the uses of \\Parf in SGA 6 main.tex (diplomatic) that stand where the print has the lowercase index 'parf'
(subscript or the 'C_o-parf-amp' name), with line numbers; read only.
usage: python -I parf_uses.py"""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(__file__).resolve().parents[2]
t = (W / "sga6" / "diplomatic" / "main.tex").read_text(encoding="utf-8")
lines = t.split("\n")
pat_low = re.compile(r"(_\{\\Parf\}|\\text\{-\}\\Parf|\\Parf\\text\{-\}|\\Parf\\\)-\\\(\\amp)")
n_all = 0
for i, line in enumerate(lines, 1):
    for m in re.finditer(r"\\Parf\b", line):
        n_all += 1
    for m in pat_low.finditer(line):
        print(i, "|", line[max(0, m.start() - 45):m.end() + 20])
print("all \\Parf:", n_all)
