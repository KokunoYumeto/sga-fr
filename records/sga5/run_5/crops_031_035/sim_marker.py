"""Read-only simulation of move_marker.py (same logic), printing the text around the moved marker."""
import pathlib
import re
import sys

MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
folio, anchor = int(sys.argv[1]), sys.argv[2]
before = "--before" in sys.argv
for edition in ("diplomatic", "current"):
    f = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5") / edition / "s5.tex"
    t = f.read_text(encoding="utf-8")
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t3 = t2[:ls] + line + "\n" + t2[ls:]
        pos = ls
    else:
        t3 = t2[:k] + "\n" + line + "\n" + t2[k:]
        pos = k
    print("==", edition, "line", t3.count("\n", 0, pos) + 1)
    print(repr(t3[max(0, pos - 120):pos + 220]))
