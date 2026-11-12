"""Simulate, in memory only, the p. 34 underline fix and the moves of the folio-34 and folio-35 markers of SGA 6
(the logic of move_marker.py) on both layers, and print the context. Nothing is written.
usage: python -I sim_markers.py"""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")


def move(t, folio, anchor, before):
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    assert k >= 0, (folio, anchor)
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2


for edition in ("diplomatic", "current"):
    t = (W / edition / "main.tex").read_text(encoding="utf-8")
    old, new = r"\emph{On fait opérer", r"On \emph{fait opérer"
    assert t.count(old) == 1, (edition, t.count(old))
    t = t.replace(old, new)
    t = move(t, 34, r"\emph{fait opérer", before=False)
    t = move(t, 35, "au", before=True)
    for folio in (34, 35):
        m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
        print(f"--- {edition}, folio {folio}:\n{t[m.start() - 90:m.end() + 60]}\n")
