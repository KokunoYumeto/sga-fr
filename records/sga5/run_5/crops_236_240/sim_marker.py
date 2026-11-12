"""Simulate move_marker.py VOL FOLIO ANCHOR [--before] in memory on both layers of SGA 5 (nothing is written)."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
folio, anchor = int(sys.argv[1]), sys.argv[2]
before = "--before" in sys.argv
base = r"C:/Users/user/Documents/sga_scan_check_20261105/sga5/"
for edition in ("diplomatic", "current"):
    t = open(base + edition + "/s5.tex", encoding="utf-8").read()
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == chr(10) else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    ls = t2.rfind(chr(10), 0, k) + 1
    if t2[ls:k].strip() == "":
        t3 = t2[:ls] + line + chr(10) + t2[ls:]
        at = ls
    else:
        t3 = t2[:k] + chr(10) + line + chr(10) + t2[k:]
        at = k
    print("=====", edition, "anchor found at line", t2.count(chr(10), 0, k) + 1)
    s = t3.find(line)
    print(t3[max(0, s - 260):s + len(line) + 420])
