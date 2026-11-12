"""Simulate move_marker.py in memory (nothing is written) for the marker fixes of pages 81-85.
usage: python -I sim_markers.py"""
import pathlib
import re

W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
MOVES = [(82, "\\subsection*{2.2}", True), (84, "Donnons-nous", False), (86, "\\[", True)]


def move(t, folio, anchor, before):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        return None, None
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
        pos = ls
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
        pos = k
    return t2, pos


for edition in ("diplomatic", "current"):
    t = (W / "sga5" / edition / "s5.tex").read_text(encoding="utf-8")
    for folio, anchor, before in MOVES:
        t2, pos = move(t, folio, anchor, before)
        if t2 is None:
            print(edition, folio, "anchor not found")
            continue
        print("=" * 20, edition, "folio", folio, "anchor", repr(anchor), "before" if before else "after")
        print(t2[max(0, pos - 160):pos + 200])
        t = t2
