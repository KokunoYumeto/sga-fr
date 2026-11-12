"""Simulate move_marker.py on copies of both editions (nothing is written).
usage: python -I sim_marker.py FOLIO ANCHOR [--before]"""
import pathlib
import re
import sys

W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
folio, anchor = int(sys.argv[1]), sys.argv[2]
before = "--before" in sys.argv
for ed in ("diplomatic", "current"):
    t = (W / "sga6" / ed / "main.tex").read_text(encoding="utf-8")
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        print(ed, "anchor not found")
        continue
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    i = t2.find(line)
    sys.stdout.buffer.write((ed + ": " + repr(t2[i - 160:i + len(line) + 80]) + "\n").encode("utf-8"))
