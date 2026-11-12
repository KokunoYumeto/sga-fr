"""Simulate move_marker.py in memory (no writes) for the marker fixes of pp. 382, 384, 386."""
import re, sys
sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
T0 = open(r"C:/Users/user/Documents/sga_scan_check_20261105/sga6/diplomatic/main.tex", encoding="utf-8").read()

def move(t, folio, anchor, before):
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2

for folio, anchor, before in [(382, "\[", True), (384, "\(\Proj", False), (386, "\[", True)]:
    t = move(T0, folio, anchor, before)
    i = t.index("|  folio %d  " % folio)
    print("=====", folio)
    print(t[i - 260:i + 160])
