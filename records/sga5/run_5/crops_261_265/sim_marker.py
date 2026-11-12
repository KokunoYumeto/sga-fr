# In-memory simulation of move_marker.py (no file is written).
import re, sys
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
sys.stdout.reconfigure(encoding="utf-8")
base = r"C:\Users\user\Documents\sga_scan_check_20261105\sga5"
def sim(folio, anchor, before):
    for ed in ("diplomatic", "current"):
        t = open(base + "\\" + ed + r"\s5.tex", encoding="utf-8").read()
        m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
        line = m.group(0)
        end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
        t2 = t[:m.start()] + t[end:]
        k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
        if k < 0:
            print(ed, "anchor not found"); continue
        ls = t2.rfind("\n", 0, k) + 1
        if t2[ls:k].strip() == "":
            t2 = t2[:ls] + line + "\n" + t2[ls:]
        else:
            t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
        j = t2.find(line)
        print("==", ed, "folio", folio, "anchor", repr(anchor))
        print(t2[j - 250:j + len(line) + 120])
        print()
sim(264, "des propriétés", False)
sim(266, "\[", True)
