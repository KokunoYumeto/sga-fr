"""Simulate move_marker.py in memory (writes nothing): report the line where the marker would land in each layer.
usage: python -I sim_marker.py FOLIO ANCHOR [--before]"""
import re
import sys

MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
folio, anchor = int(sys.argv[1]), sys.argv[2]
before = "--before" in sys.argv
base = r"C:\Users\user\Documents\sga_scan_check_20261105\sga5"
for layer in ("diplomatic", "current"):
    t = open(base + "\\" + layer + "\\s5.tex", encoding="utf-8", newline="").read()
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    if not m:
        print(layer, "no marker")
        continue
    line = m.group(0)
    mline = t.count("\n", 0, m.start()) + 1
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        print(layer, "anchor not found")
        continue
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t3 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t3 = t2[:k] + "\n" + line + "\n" + t2[k:]
    m3 = next(mm for mm in MARK.finditer(t3) if int(mm.group(2)) == folio)
    nl = t3.count("\n", 0, m3.start()) + 1
    lines = t3.split("\n")
    print(f"{layer}: marker now at line {mline}; anchor at line {t2.count(chr(10), 0, k) + 1}; after move:")
    for i in range(nl - 3, nl + 2):
        print(f"   {i + 1}: {lines[i][:110]!r}")
