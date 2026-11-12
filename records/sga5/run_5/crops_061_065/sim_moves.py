"""Simulate, in memory only, the marker moves for folios 61 and 62 (logic of move_marker.py) on both layers of
SGA 5 as they stand now; print marker lines and the text around the moved folio-62 marker. Nothing is written.
usage: python -I sim_moves.py"""
import os
import pathlib
import re
import sys
import time

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
A41 = "\\begin{equation}\\tag{4.1}"
A43 = "\\begin{equation}\\tag{4.3}"


def move(t, folio, anchor, before):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        return t, "anchor not found (no change)"
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2, "marker now on its own line before line %d" % (t2[:k].count("\n") + 1)


def lineno(t, s):
    k = t.find(s)
    return None if k < 0 else t[:k].count("\n") + 1


for edition in ("diplomatic", "current"):
    p = W / "sga5" / edition / "s5.tex"
    t = p.read_text(encoding="utf-8")
    print(edition, "mtime", time.strftime("%H:%M:%S", time.localtime(os.path.getmtime(p))))
    for f in (61, 62, 63):
        m = next(m for m in MARK.finditer(t) if int(m.group(2)) == f)
        print("  folio", f, "marker at line", t[:m.start()].count("\n") + 1)
    print("  (4.1) at line", lineno(t, A41), " (4.3) at line", lineno(t, A43))
    _, info = move(t, 61, A41, True)
    print("  folio 61 move again:", info)
    t2, info = move(t, 62, A43, True)
    print("  folio 62 move:", info)
    m = next(m for m in MARK.finditer(t2) if int(m.group(2)) == 62)
    a = t2.rfind("\n", 0, t2.rfind("\n", 0, m.start() - 1)) + 1
    print(t2[a:m.end() + 260])
    print()
