"""Simulate move_marker.py in memory (no file is written) for the folio-102 and folio-104 markers of SGA 5."""
import pathlib
import re

W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")


def move(t, folio, anchor, before=True):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        return None
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2


for edition in ("diplomatic", "current"):
    t = (W / "sga5" / edition / "s5.tex").read_text(encoding="utf-8")
    print("==", edition, "anchor count '$z$ de $C':", t.count("$z$ de $C"))
    t = move(t, 102, "$z$ de $C")
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == 102)
    print(repr(t[m.start() - 120:m.end() + 140]))
    t = move(t, 104, "\\[")
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == 104)
    print(repr(t[m.start() - 160:m.end() + 200]))
