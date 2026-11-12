"""Read-only simulation of move_marker.py --before: print where the marker of FOLIO would land.

Usage: python -I sim_marker.py FOLIO ANCHOR
"""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = r"C:/Users/user/Documents/sga_scan_check_20261105/sga5"
folio, anchor = int(sys.argv[1]), sys.argv[2]
for ed in ("diplomatic", "current"):
    t = open(f"{ROOT}/{ed}/s5.tex", encoding="utf-8").read()
    m = re.search(r"%%%%%%%%%%  scan idx \d+  \|  folio " + str(folio) + r"  %%%%%%%%%%\n", t)
    t2 = t[: m.start()] + t[m.end():]
    k = t2.rfind(anchor, 0, m.start())
    ls = t2.rfind("\n", 0, k) + 1
    where = "at line start" if t2[ls:k].strip() == "" else "mid-line (line split)"
    print(ed, where, repr(t2[max(0, k - 70):k]), "|MARKER|", repr(t2[k:k + 50]))
