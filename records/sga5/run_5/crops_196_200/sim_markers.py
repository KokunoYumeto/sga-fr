"""Simulate move_marker.py in memory (no writing) for folios 196, 199, 200 of SGA 5, both editions."""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5")


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
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    j = t2.find(line)
    return t2, j


jobs = [(196, "(III 4.7) entraîne que", False),
        (199, "\\[", True),
        (200, "$d_1^{-1}(V)\\subset d_2^{-1}(V)$", True)]
for ed in ("diplomatic", "current"):
    t = (ROOT / ed / "s5.tex").read_text(encoding="utf-8")
    for folio, anchor, before in jobs:
        t2, j = move(t, folio, anchor, before)
        print("=====", ed, folio, repr(anchor), "before" if before else "after")
        if t2 is None:
            print("anchor not found")
            continue
        print(t2[j - 160:j + 160])
