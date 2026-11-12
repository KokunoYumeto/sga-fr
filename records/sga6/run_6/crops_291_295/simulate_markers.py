"""Simulate move_marker.py (same logic) in memory for folios 291 and 296 in both SGA 6 layers; print the result.
No file is written."""
import io
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
BASE = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6"


def simulate(t, folio, anchor, before):
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
    return t2[j - 160:j + len(line) + 120]


for layer in ("diplomatic", "current"):
    t = open(rf"{BASE}\{layer}\main.tex", encoding="utf-8").read()
    for folio, anchor in ((291, "est"), (296, "(")):
        m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
        print(f"=== {layer} folio {folio}: before the move")
        print(t[m.start() - 120:m.end() + 60])
        print(f"--- after move_marker.py 6 {folio} {anchor!r} --before")
        print(simulate(t, folio, anchor, True))
        print()
    i = t.find("pour \\(f\\) propre, \\(a\\in")
    print(layer, "projection line:", t[i:i + 200].replace("\n", " | "))
    i = t.find("f_*(a x)=a f_*(x)")
    print(layer, "display:", repr(t[i - 5:i + 30]))
    print()
