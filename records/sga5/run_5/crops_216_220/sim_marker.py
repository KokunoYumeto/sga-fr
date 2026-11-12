"""Read-only simulation of move_marker.py for one folio in both layers of SGA 5 (writes nothing).
usage: python -I sim_marker.py FOLIO ANCHOR [--before]"""
import re
import sys
import pathlib

MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
root = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5")
folio, anchor = int(sys.argv[1]), sys.argv[2]
before = "--before" in sys.argv
sys.stdout.reconfigure(encoding="utf-8")
for edition in ("diplomatic", "current"):
    f = root / edition / "s5.tex"
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
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    j = t2.find(line)
    print("=====", edition)
    print(t2[max(0, j - 300):j + len(line) + 300])
