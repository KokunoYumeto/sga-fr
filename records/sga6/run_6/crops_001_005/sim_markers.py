"""Simulate move_marker.py (--before) in memory, without writing: show the context after moving the markers of
folios 2-6 of SGA 6 in the given main.tex.
usage: python -I sim_markers.py MAIN_TEX"""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
t = open(sys.argv[1], encoding="utf-8").read()
MOVES = ((2, "de"), (3, r"\subsubsection*{2.1}"), (4, "("), (5, "est un"), (6, r"\subsection*{3.}"))
for folio, anchor in MOVES:
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
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
    j = t.find(line)
    print(f"--- folio {folio}:\n{t[j - 60:j + len(line) + 50]}\n")
