"""Simulate (in memory only) the marker moves for pp. 186-190 with the logic of move_marker.py, applied in sequence,
and print the text around each new marker, for both editions. Writes nothing."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
BASE = r"C:/Users/user/Documents/sga_scan_check_20261105/sga5/"
MOVES = [(186, "\\begin{equation}", True), (187, "et la flèche d'évaluation 5.3.5", True), (188, "\\[", False),
         (189, "\\subsection*{6.7}", True), (190, "\\begin{equation}", True)]


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


for ed in ("diplomatic", "current"):
    t = open(BASE + ed + "/s5.tex", encoding="utf-8").read()
    for folio, anchor, before in MOVES:
        t = move(t, folio, anchor, before)
    print("=====", ed)
    for m in MARK.finditer(t):
        if 186 <= int(m.group(2)) <= 190:
            print("--- folio", m.group(2))
            print(t[max(0, m.start() - 160):m.start()])
            print("[MARKER]")
            print(t[m.end():m.end() + 120])
