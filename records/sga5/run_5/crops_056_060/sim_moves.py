"""Simulate move_marker.py in memory (no file is written) and print the text around each moved marker."""
import pathlib
import sys

sys.path.insert(0, r"C:\Users\user\Documents\sga_scan_check_20261105")
from sga_config import MARK, files  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
MOVES = [(57, r"où l'on", True), (58, r"où $i$ est une", True), (60, r"de base, la", True),
         (61, r"\begin{equation}\tag{4.1}", True)]


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
    for f in files("5", edition):
        t = f.read_text(encoding="utf-8")
        orig = t
        for folio, anchor, before in MOVES:
            mk = next(m for m in MARK.finditer(orig) if int(m.group(2)) == folio)
            old_line = orig[:mk.start()].count("\n") + 1
            k = orig.rfind(anchor, 0, mk.start())
            anchor_line = orig[:k].count("\n") + 1
            t, pos = move(t, folio, anchor, before)
            if t is None:
                print(edition, folio, "ANCHOR NOT FOUND")
                break
            print(f"== {edition} folio {folio}: marker now at line {old_line}; anchor found on line {anchor_line}")
            print(t[max(0, pos - 120):pos + 120])
            print()
