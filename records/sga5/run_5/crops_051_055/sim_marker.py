"""Read-only simulation of move_marker.py (same logic) for several moves in sequence, on both layers of SGA 5;
prints the text around each moved marker. usage: python -I sim_marker.py FOLIO ANCHOR [--before] [FOLIO ANCHOR [--before] ...]"""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
args = sys.argv[1:]
moves = []
i = 0
while i < len(args):
    folio, anchor = int(args[i]), args[i + 1]
    before = i + 2 < len(args) and args[i + 2] == "--before"
    moves.append((folio, anchor, before))
    i += 3 if before else 2
for edition in ("diplomatic", "current"):
    f = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5") / edition / "s5.tex"
    t = f.read_text(encoding="utf-8")
    for folio, anchor, before in moves:
        m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
        line = m.group(0)
        end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
        t2 = t[:m.start()] + t[end:]
        k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
        if k < 0:
            print(edition, folio, "anchor not found")
            continue
        ls = t2.rfind("\n", 0, k) + 1
        if t2[ls:k].strip() == "":
            t = t2[:ls] + line + "\n" + t2[ls:]
            pos = ls
        else:
            t = t2[:k] + "\n" + line + "\n" + t2[k:]
            pos = k
        print("==", edition, "folio", folio, "marker now at line", t.count("\n", 0, pos) + 1)
        print(t[max(0, pos - 160):pos + 200])
        print()
