"""Simulate move_marker.py in memory (no write) and print the text around the moved marker in both layers.

usage: python -I sim_marker.py FOLIO ANCHOR [--before]
"""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
folio, anchor = int(sys.argv[1]), sys.argv[2]
before = "--before" in sys.argv
for edition in ("diplomatic", "current"):
    f = W / edition / "s5.tex"
    t = f.read_text(encoding="utf-8")
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    lineno = t.count("\n", 0, m.start()) + 1
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
    print("==", edition, "marker at line", lineno, "anchor line", t2.count("\n", 0, k) + 1,
          "chars moved", m.start() - k)
    print(t3[max(0, pos - 250):pos + 250])
    print()
