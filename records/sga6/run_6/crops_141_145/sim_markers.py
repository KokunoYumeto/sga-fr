"""Simulate move_marker.py (--before) in memory on both layers of SGA 6; print the result around each moved marker.
Writes nothing."""
import re
import sys
sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
W = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6"
moves = [(141, r"\textbf{6.2.}"), (144, "l'%"), (145, r"\textbf{6.8.}"), (146, "(les")]
for ed in ("diplomatic", "current"):
    t = open(W + "\\" + ed + "\main.tex", encoding="utf-8").read()
    for folio, anchor in moves:
        m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
        line = m.group(0)
        end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
        t2 = t[:m.start()] + t[end:]
        k = t2.rfind(anchor, 0, m.start())
        ls = t2.rfind("\n", 0, k) + 1
        if t2[ls:k].strip() == "":
            t2 = t2[:ls] + line + "\n" + t2[ls:]
        else:
            t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
        t = t2
        m2 = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
        print(ed, folio, "distance moved:", m.start() - m2.start())
        print(repr(t[m2.start() - 120:m2.end() + 80]))
        print()
