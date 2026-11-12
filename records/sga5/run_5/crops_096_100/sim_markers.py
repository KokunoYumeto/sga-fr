"""Simulate move_marker.py (--before) in memory on both layers of s5.tex and print the text around the moved marker.
Writes nothing.  usage: python -I -B sim_markers.py"""
import pathlib
import re

W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
MOVES = [(96, r"\begin{enumerate}"), (97, "où"), (100, r"\begin{equation}")]

for edition in ("diplomatic", "current"):
    t = (W / "sga5" / edition / "s5.tex").read_text(encoding="utf-8")
    for folio, anchor in MOVES:
        m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
        line = m.group(0)
        end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
        t2 = t[:m.start()] + t[end:]
        k = t2.rfind(anchor, 0, m.start())
        ls = t2.rfind("\n", 0, k) + 1
        if t2[ls:k].strip() == "":
            t3 = t2[:ls] + line + "\n" + t2[ls:]
        else:
            t3 = t2[:k] + "\n" + line + "\n" + t2[k:]
        lineno = t2.count("\n", 0, k) + 1
        m3 = next(m for m in MARK.finditer(t3) if int(m.group(2)) == folio)
        print(f"== {edition} folio {folio} anchor {anchor!r} at line {lineno}; moved by "
              f"{t.count(chr(10), 0, m.start()) - t3.count(chr(10), 0, m3.start())} lines")
        print(t3[max(0, m3.start() - 160):m3.end() + 120])
        print()
