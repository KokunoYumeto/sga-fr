"""Simulate move_marker.py for folio 121 (anchor 'si \\(F\\) est', --before) without writing; print the result."""
import pathlib
import re

W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
anchor = r"si \(F\) est"
for ed in ("diplomatic", "current"):
    t = (W / "sga6" / ed / "main.tex").read_text(encoding="utf-8")
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == 121)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start())
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t3 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t3 = t2[:k] + "\n" + line + "\n" + t2[k:]
    j = t3.find(line)
    print(ed, repr(t3[j - 60:j + len(line) + 70]))
