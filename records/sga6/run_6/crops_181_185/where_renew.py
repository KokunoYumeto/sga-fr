"""Print line number, folio and context of each \\renewcommand{\\Ob} in SGA 6 diplomatic main.tex (read only)."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = r"C:\Users\user\Documents\sga_scan_check_20261105"
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
BS = chr(92)
t = open(W + r"\sga6\diplomatic\main.tex", encoding="utf-8").read()
ren = BS + "renewcommand{" + BS + "Ob}"
marks = [(m.start(), int(m.group(2))) for m in MARK.finditer(t)]
k = t.find(ren)
while k >= 0:
    fo = None
    for p, f in marks:
        if p <= k:
            fo = f
    line = t.count("\n", 0, k) + 1
    sec = t.rfind(BS + "section", 0, k)
    print(line, "folio", fo, t[k:k + 40].replace("\n", " "), "| last section:", t[sec:sec + 70].replace("\n", " "))
    k = t.find(ren, k + 1)
