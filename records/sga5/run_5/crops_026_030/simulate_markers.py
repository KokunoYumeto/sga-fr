"""In-memory simulation of move_marker.py (no file is written): prints the text around each moved marker."""
import re
import sys
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
moves = [(27, "pureté", False), (29, r"\item[(ii~bis)]", False), (30, "de", True), (31, r"$j : V \to U$", True)]
for edition in ("diplomatic", "current"):
    path = rf"C:\Users\user\Documents\sga_scan_check_20261105\sga5\{edition}\s5.tex"
    t = open(path, encoding="utf-8").read()
    for folio, anchor, before in moves:
        m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
        line = m.group(0)
        end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
        t2 = t[:m.start()] + t[end:]
        k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
        if k < 0:
            print(edition, folio, "anchor not found"); continue
        ls = t2.rfind("\n", 0, k) + 1
        if t2[ls:k].strip() == "":
            t3 = t2[:ls] + line + "\n" + t2[ls:]
        else:
            t3 = t2[:k] + "\n" + line + "\n" + t2[k:]
        lineno = t[:m.start()].count("\n") + 1
        p = t3.find(line)
        print(f"== {edition} folio {folio} (marker now at line {lineno}); after move:")
        print(repr(t3[max(0, p - 120):p + len(line) + 80]))
        t = t3
