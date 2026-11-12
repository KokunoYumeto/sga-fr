"""Simulate (in memory only, nothing written) the marker moves proposed for folios 202, 203, 205, 206 of SGA 5,
with the same logic as move_marker.py, on both layers; print the lines around each moved marker."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
BASE = r"C:\Users\user\Documents\sga_scan_check_20261105\sga5"
MOVES = [(202, "\\begin{equation}", True), (203, "\\section*{B", True),
         (205, "\\begin{enumerate}[label=(\\roman*)]", True), (206, "\\[", False)]


def move(t, folio, anchor, before):
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
    return t2


for ed in ("diplomatic", "current"):
    t = open(rf"{BASE}\{ed}\s5.tex", encoding="utf-8", newline="").read()
    for folio, anchor, before in MOVES:
        t = move(t, folio, anchor, before)
    lines = t.split("\n")
    print("=====", ed)
    for i, ln in enumerate(lines):
        m = MARK.search(ln)
        if m and int(m.group(2)) in (202, 203, 205, 206):
            print("-- folio", m.group(2), "at line", i + 1)
            for j in range(max(0, i - 3), min(len(lines), i + 4)):
                print(f"{j + 1:6d}: {lines[j][:110]}")
