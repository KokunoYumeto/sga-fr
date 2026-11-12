"""Simulate move_marker.py (in memory only, nothing is written) for the markers of SGA 6 pp. 11-15.

usage: python -I sim_markers.py
Prints, for each proposed move and for both layers, the text around the moved marker.
"""
import pathlib
import re

ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")

MOVES = [(13, r"alg\'", True), (14, "[1] un", True)]  # folio 11 already moved in main.tex (findings_006_010.json)


def move(t, folio, anchor, before):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    if not m:
        return None, "marker not found"
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        return None, "anchor not found"
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2, "moved"


for edition in ("diplomatic", "current"):
    t = (ROOT / edition / "main.tex").read_text(encoding="utf-8")
    for folio, anchor, before in MOVES:
        t2, msg = move(t, folio, anchor, before)
        print("=" * 20, edition, "folio", folio, repr(anchor), msg)
        if t2 is None:
            continue
        m = next(m for m in MARK.finditer(t2) if int(m.group(2)) == folio)
        print(repr(t2[max(0, m.start() - 120):m.end() + 120]))
