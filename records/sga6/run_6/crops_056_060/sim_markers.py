"""Simulate move_marker.py in memory (no file is written) and show the TeX around each moved marker.
usage: python -I sim_markers.py"""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
MOVES = [(56, r"\begin{equation}\tag{2.30}", True), (57, "noté", True),
         (59, r"$X\times k$ ($n$ est la", True), (61, r"$\Atil$ soumis aux restrictions", False)]


def move(t, folio, anchor, before):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        return None
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        return t2[:ls] + line + "\n" + t2[ls:]
    return t2[:k] + "\n" + line + "\n" + t2[k:]


for edition in ("diplomatic", "current"):
    t = (W / "sga6" / edition / "main.tex").read_text(encoding="utf-8")
    for folio, anchor, before in MOVES:
        t3 = move(t, folio, anchor, before)
        if t3 is None:
            print(edition, folio, "ANCHOR NOT FOUND")
            continue
        m = next(m for m in MARK.finditer(t3) if int(m.group(2)) == folio)
        print(f"=== {edition} folio {folio}")
        print(repr(t3[m.start() - 140:m.end() + 90]))
