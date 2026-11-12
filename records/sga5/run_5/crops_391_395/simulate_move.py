"""Simulate move_marker.py in memory (no writes) for both editions of s5.tex.
usage: python -I -B simulate_move.py FOLIO ANCHOR [--before]"""
import re
import sys

MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
folio, anchor = int(sys.argv[1]), sys.argv[2]
before = "--before" in sys.argv
sys.stdout.reconfigure(encoding="utf-8")
for edition in ("diplomatic", "current"):
    p = f"C:/Users/user/Documents/sga_scan_check_20261105/sga5/{edition}/s5.tex"
    t = open(p, encoding="utf-8", newline="").read()
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        print(edition, "anchor not found")
        continue
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    lines = t2.split("\n")
    i = next(j for j, s in enumerate(lines) if s == line)
    print(edition, "marker now at line", i + 1)
    for s in lines[i - 3:i + 3]:
        print("   ", s[:100])
