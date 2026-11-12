"""Simulate move_marker.py (--before) in memory, without writing: show the context after moving the markers of
folios 22 and 23 of SGA 6 in the given main.tex files.
usage: python -I sim_markers.py MAIN_TEX [MAIN_TEX ...]"""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
MOVES = ((22, r"\begin{equation}\tag{1.4}"), (23, "les"))
for path in sys.argv[1:]:
    t = open(path, encoding="utf-8").read()
    print("=====", path)
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
        print(f"--- folio {folio}:\n{t[j - 90:j + len(line) + 70]!r}\n")
