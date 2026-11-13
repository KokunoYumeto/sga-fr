"""Print, for the markers of folios 426-431, the end of the line before and the start of the line after, in both layers."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
BASE = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6"
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
for layer in ("diplomatic", "current"):
    lines = open(BASE + "\\" + layer + "\\main.tex", encoding="utf-8", newline="").read().split("\n")
    for i, ln in enumerate(lines):
        m = MARK.fullmatch(ln)
        if m and 426 <= int(m.group(2)) <= 431:
            print(layer, "folio", m.group(2), "marker line", i + 1)
            print("   before (line %d): ...%r" % (i, lines[i - 1][-90:]))
            print("   after  (line %d): %r..." % (i + 2, lines[i + 1][:90]))
