"""Simulate move_marker.py (same logic) in memory on both layers of SGA 6 main.tex; writes nothing."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
BASE = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6"
MOVES = [(331, r"\textbf{3.10", True), (334, "d'une", True), (335, r"\(f'\),", True), (336, "on", True)]


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
    t = open(BASE + "\\" + ed + "\main.tex", encoding="utf-8").read()
    if "--misprint" in sys.argv and ed == "diplomatic":
        assert t.count(r"\textbf{3.10.}") == 1
        t = t.replace(r"\textbf{3.10.}", r"\textbf{3.10}")
    for folio, anchor, before in MOVES:
        t = move(t, folio, anchor, before)
    for folio, _, _ in MOVES:
        m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
        print(ed, folio, repr(t[m.start() - 70:m.end() + 60]))
    print()
