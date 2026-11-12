"""Simulate move_marker.py in memory (no writes) on both layers of SGA 6 and print the text around the moved marker.
usage: python -I sim_marker.py FOLIO ANCHOR [--before]"""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = r"C:\Users\user\Documents\sga_scan_check_20261105"
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
folio, anchor = int(sys.argv[1]), sys.argv[2]
before = "--before" in sys.argv
for edition in ("diplomatic", "current"):
    t = open(W + rf"\sga6\{edition}\main.tex", encoding="utf-8").read()
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    print("=====", edition)
    print("BEFORE:", repr(t[m.start() - 160:m.end() + 120]))
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        print("anchor not found")
        continue
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    m2 = next((m for m in MARK.finditer(t2) if int(m.group(2)) == folio), None)
    print("AFTER: ", repr(t2[m2.start() - 160:m2.end() + 120]))
