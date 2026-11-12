"""In-memory simulation of the folio-381 marker move (reads both layers, writes nothing)."""
import sys

sys.stdout.reconfigure(encoding="utf-8")
NL = "\n"
base = "C:/Users/user/Documents/sga_scan_check_20261105/sga6/"
M381 = "%%%%%%%%%%  scan idx 394  |  folio 381  %%%%%%%%%%"
LINE = r"\textbf{2.3.}"
for layer in ("diplomatic", "current"):
    t = open(base + layer + "/main.tex", encoding="utf-8").read()
    old = LINE + NL + M381 + NL
    new = M381 + NL + LINE + NL
    print(layer, "old count", t.count(old), "| marker count", t.count(M381))
    t2 = t.replace(old, new)
    i = t2.find(M381)
    print(repr(t2[i - 60:i + len(M381) + 60]))
