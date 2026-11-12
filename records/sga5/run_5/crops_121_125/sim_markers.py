"""In-memory simulation of move_marker.py for the marker findings of pp. 121-125 (nothing is written)."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
BASE = r"C:\Users\user\Documents\sga_scan_check_20261105\sga5"
MOVES = [
    (121, "rappelons qu'on dit que", True),
    (123, "2.2.3, 2.2.4 (", True),
    (125, "\\begin{equation}\n\\tag{6.5.4}", True),
    (126, "Le théorème 4.4 a l'", True),
]


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
    return t2, (m.start() - k)


for edition in ("diplomatic", "current"):
    t = open(rf"{BASE}\{edition}\s5.tex", encoding="utf-8").read()
    for folio, anchor, before in MOVES:
        t2, dist = move(t, folio, anchor, before)
        if t2 is None:
            print(edition, folio, "ANCHOR NOT FOUND")
            continue
        m = next(m for m in MARK.finditer(t2) if int(m.group(2)) == folio)
        print(f"== {edition} folio {folio}: anchor {anchor!r} found {dist} chars before the old marker")
        print(repr(t2[m.start() - 160:m.start()]))
        print("   [MARKER]")
        print(repr(t2[m.end():m.end() + 160]))
        t = t2
