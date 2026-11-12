"""Count each fix's old in the page's span of the present diplomatic main.tex (read only), to see whether the
snapshot pages still match the live file."""
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = r"C:\Users\user\Documents\sga_scan_check_20261105"
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
t = open(W + r"\sga6\diplomatic\main.tex", encoding="utf-8").read()
ms = list(MARK.finditer(t))
span = {}
for i, m in enumerate(ms):
    end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
    span[int(m.group(2))] = t[m.start():end]
F = json.load(open(W + r"\run_6\findings_181_185.json", encoding="utf-8"))
for i, x in enumerate(F):
    if x["fix"] is None:
        continue
    n = span[x["page"]].count(x["fix"]["old"])
    if n != 1:
        print("entry", i, "p.", x["page"], "count in live span:", n, repr(x["fix"]["old"][:60]))
for p in range(181, 186):
    snap = open(W + rf"\run_6\b181_185\page_{p:03d}.tex", encoding="utf-8").read()
    body = snap.split("\n", 1)[1]
    print(p, "snapshot == live span:", body.rstrip("\n") == span[p].rstrip("\n"))
