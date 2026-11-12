"""Simulate move_marker.py moves in memory (no writes) on both layers of SGA 6 and print the context.
usage: python -I sim_markers.py"""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
MOVES = [(66, "La", True), (67, r"\textbf{N.B.}", True), (68, "Il", True), (70, r"\(z\in\underline K(X)\)", True)]
if "--nb-plain" in sys.argv:  # the p. 66 font fix applied first: anchor N.B.
    MOVES[1] = (67, "N.B.", True)


def move(t, folio, anchor, before):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2


for ed in ("diplomatic", "current"):
    t = (W / ed / "main.tex").read_text(encoding="utf-8")
    if "--nb-plain" in sys.argv:
        assert t.count("\\textbf{N.B.}\n%%%%%%%%%%  scan idx 80") == 1
        t = t.replace("\\textbf{N.B.}\n%%%%%%%%%%  scan idx 80", "N.B.\n%%%%%%%%%%  scan idx 80")
    for folio, anchor, before in MOVES:
        t = move(t, folio, anchor, before)
    print("=====", ed)
    for folio, _, _ in MOVES:
        m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
        print("--- folio", folio)
        print(t[max(0, m.start() - 90):m.end() + 70])
