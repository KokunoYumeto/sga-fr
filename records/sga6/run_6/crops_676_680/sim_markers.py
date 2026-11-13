"""Read-only simulation of move_marker.py --before for folios 676-678 on both layers; prints the context."""
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
base = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6"
moves = [(676, "résolu de"), (677, "de $Y$"), (678, "Or")]
for edition in ("diplomatic", "current"):
    t = open(base + "\\" + edition + "\\main.tex", encoding="utf-8").read()
    for folio, anchor in moves:
        m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
        if not m:
            print(edition, folio, "no marker")
            continue
        line = m.group(0)
        end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
        t2 = t[:m.start()] + t[end:]
        k = t2.rfind(anchor, 0, m.start())
        ls = t2.rfind("\n", 0, k) + 1
        if t2[ls:k].strip() == "":
            t3 = t2[:ls] + line + "\n" + t2[ls:]
        else:
            t3 = t2[:k] + "\n" + line + "\n" + t2[k:]
        p = t3.find(line)
        print("==", edition, folio, "distance moved back:", m.start() - k)
        print(repr(t3[p - 80:p + len(line) + 80]))
