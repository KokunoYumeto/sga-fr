"""In-memory simulation of move_marker.py (no file is written)."""
import re
import sys
import pathlib

MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")


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
    return t2, t2.find(line)


moves = [(302, "\\[", True), (305, "\\subsubsection*{4.10", True)]
for edition in ("diplomatic", "current"):
    t = pathlib.Path(r"C:/Users/user/Documents/sga_scan_check_20261105/sga5/%s/s5.tex" % edition).read_text(encoding="utf-8")
    for folio, anchor, before in moves:
        t2, pos = move(t, folio, anchor, before)
        print("=====", edition, folio, repr(anchor))
        print(t2[pos - 200: pos + 260])
    # also: with the 4.10 punctuation fix applied first
    t3 = t.replace("\\subsubsection*{4.10}", "\\subsubsection*{4.10.}", 1)
    t4, pos = move(t3, 305, "\\subsubsection*{4.10", True)
    print("===== after 4.10. fix", edition)
    print(t4[pos - 80: pos + 120])
