"""sim_marker.py FOLIO ANCHOR [--before]: simulate move_marker.py for SGA 5 in memory (no writing) on both layers
and print the text around the marker afterwards."""
import re
import sys
sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
folio, anchor = int(sys.argv[1]), sys.argv[2]
before = "--before" in sys.argv
base = r"C:\Users\user\Documents\sga_scan_check_20261105\sga5"
for edition in ("diplomatic", "current"):
    t = open(base + "\\" + edition + "\s5.tex", encoding="utf-8").read()
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    j = t2.find(line)
    print("==", edition, "anchor", repr(anchor))
    print(t2[j - 160:j + len(line) + 120])
    print()
