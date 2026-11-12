"""Simulate move_marker.py moves in memory on both layers of SGA 6 (no file is written) and print the result."""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
MOVES = [(296, "(", True), (298, "abéliens, de la", True), (299, r"\(f_\psi\) de", False)]


def move(t, folio, anchor, before):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        raise SystemExit(f"anchor not found {folio}")
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2


for edition in ("diplomatic", "current"):
    t = (W / edition / "main.tex").read_text(encoding="utf-8")
    for folio, anchor, before in MOVES:
        t = move(t, folio, anchor, before)
    print("=====", edition)
    for folio, _, _ in MOVES:
        m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
        a = t.rfind("\n", 0, t.rfind("\n", 0, m.start() - 1)) + 1
        b = t.find("\n", t.find("\n", m.end() + 1) + 1)
        ctx = t[max(a, m.start() - 160):min(b, m.end() + 120)]
        print(f"--- folio {folio}:")
        print(ctx)
        print()
