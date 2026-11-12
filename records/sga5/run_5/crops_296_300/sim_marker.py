"""In-memory simulation of move_marker.py (VOL 5, FOLIO, ANCHOR, --before) on both layers; writes nothing."""
import re
import sys
sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
folio, anchor, before = int(sys.argv[1]), sys.argv[2], "--before" in sys.argv
for ed in ("diplomatic", "current"):
    p = r"C:\Users\user\Documents\sga_scan_check_20261105\sga5\%s\s5.tex" % ed
    t = open(p, encoding="utf-8", newline="").read()
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    print("=====", ed, "anchor occurrences in file:", t.count(anchor), "| found at", k)
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    j = t2.find(line)
    print("marker now at line", t2[:j].count("\n") + 1, "(was", t[:m.start()].count("\n") + 1, ")")
    print(t2[j - 200:j + len(line) + 420])
