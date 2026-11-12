"""Simulate move_marker.py in memory (no file is written): show where the marker of FOLIO would land.
usage: python -I sim_marker.py FOLIO ANCHOR [--before]"""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
folio, anchor = int(sys.argv[1]), sys.argv[2]
before = "--before" in sys.argv
for edition in ("diplomatic", "current"):
    f = W / "sga5" / edition / "s5.tex"
    t = f.read_text(encoding="utf-8")
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
        t3 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t3 = t2[:k] + "\n" + line + "\n" + t2[k:]
    lineno = t2.count("\n", 0, k) + 1
    j = t3.find(line)
    print(f"{edition}: anchor at line {lineno}; result:")
    print("   ..." + t3[max(0, j - 120):j + len(line) + 120].replace("\n", " | ") + "...")
    # the next marker must still come after
    nxt = [mm for mm in MARK.finditer(t3) if int(mm.group(2)) == folio + 1]
    print("   next marker after it:", bool(nxt and nxt[0].start() > j))
