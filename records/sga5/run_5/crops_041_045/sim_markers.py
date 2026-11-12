"""Simulate move_marker.py in memory (no file is written) for the markers of pp. 41-46 and print the result.
usage: python -I sim_markers.py"""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")

MOVES = [  # (folio, anchor, before); 41 and 46 were moved by the coordinator at 16:51-16:59
    (43, "``", True),
    (44, "\\[", True),
]


def move(t, folio, anchor, before):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        return t, None
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2, k


for ed in ("diplomatic", "current"):
    t = (ROOT / ed / "s5.tex").read_text(encoding="utf-8")
    for folio, anchor, before in MOVES:
        t, k = move(t, folio, anchor, before)
        m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
        ln = t.count("\n", 0, m.start()) + 1
        print(f"--- {ed} folio {folio}: anchor {anchor!r} -> marker now at line {ln}")
        a = t.rfind("\n", 0, max(0, m.start() - 160))
        print(t[a + 1:m.end() + 160])
        print()
