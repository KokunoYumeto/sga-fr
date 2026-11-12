"""In-memory simulation of move_marker.py (no file is written).
usage: python -I simulate_move.py FOLIO ANCHOR [--before]"""
import pathlib
import re
import sys

MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5")
folio, anchor = int(sys.argv[1]), sys.argv[2]
before = "--before" in sys.argv
for edition in ("diplomatic", "current"):
    f = W / edition / "s5.tex"
    if not f.exists():
        print(edition, "missing")
        continue
    t = f.read_text(encoding="utf-8")
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    print(edition, "anchor count in file:", t2.count(anchor))
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t3 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t3 = t2[:k] + "\n" + line + "\n" + t2[k:]
    j = t3.find(line)
    seg = t3[j - 200: j + len(line) + 300]
    print(edition, "marker old line:", t[:m.start()].count("\n") + 1, "new line:", t3[:j].count("\n") + 1)
    sys.stdout.buffer.write(seg.encode("utf-8") + b"\n-----\n")
