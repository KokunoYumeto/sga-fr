"""Simulate move_marker.py in memory (no writing) and show the text around the moved marker.
usage: python -I sim_marker.py FOLIO ANCHOR [--before]"""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
folio, anchor = int(sys.argv[1]), sys.argv[2]
before = "--before" in sys.argv
for edition in ("diplomatic", "current"):
    f = rf"C:\Users\user\Documents\sga_scan_check_20261105\sga5\{edition}\s5.tex"
    t = open(f, encoding="utf-8").read()
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t3 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t3 = t2[:k] + "\n" + line + "\n" + t2[k:]
    j = t3.find(line)
    print("=====", edition, "line", t3.count("\n", 0, j) + 1)
    print(t3[j - 250:j + len(line) + 120])
