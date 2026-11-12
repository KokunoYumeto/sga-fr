"""Simulate move_marker.py (VOL 6, --before) in memory on both layers and print the text around the moved marker.
Writes nothing. usage: python -I simulate_move.py FOLIO ANCHOR"""
import re
import sys

MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
folio, anchor = int(sys.argv[1]), sys.argv[2]
for edition in ("diplomatic", "current"):
    p = rf"C:\Users\user\Documents\sga_scan_check_20261105\sga6\{edition}\main.tex"
    t = open(p, encoding="utf-8").read()
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start())
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    j = t2.find(line)
    print("==", edition, "chars moved up:", m.start() - j)
    print(t2[j - 160:j + len(line) + 160])
    print()
