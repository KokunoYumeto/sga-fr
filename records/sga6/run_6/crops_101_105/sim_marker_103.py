"""Simulate (in memory, nothing written) the marker move of p. 103 on both layers of SGA 6 main.tex, with the
logic of move_marker.py (python -I move_marker.py 6 103 "l'%" --before); print the text around the moved marker.
usage: python -I sim_marker_103.py"""
import pathlib
import re
import sys

W = pathlib.Path(__file__).resolve().parents[2]
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")


def move(t, folio, anchor, before=True):
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        print("  anchor not found", repr(anchor))
        return t
    print("  anchor found at offset", k, "marker was at", m.start())
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        return t2[:ls] + line + "\n" + t2[ls:]
    return t2[:k] + "\n" + line + "\n" + t2[k:]


sys.stdout.reconfigure(encoding="utf-8")
for edition in ("diplomatic", "current"):
    t = (W / "sga6" / edition / "main.tex").read_text(encoding="utf-8")
    print("==", edition)
    t = move(t, 103, "l'%")
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == 103)
    print(repr(t[m.start() - 120:m.end() + 60]))
