"""Read-only simulation of marker_split_word.py 'pull' for one folio in both layers of SGA 5 (writes nothing).
usage: python -I sim_pull.py FOLIO PIECE"""
import re
import sys
import pathlib

MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
root = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5")
folio, piece = int(sys.argv[1]), sys.argv[2]
sys.stdout.reconfigure(encoding="utf-8")
for edition in ("diplomatic", "current"):
    t = (root / edition / "s5.tex").read_text(encoding="utf-8")
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    ls = t.rfind("\n", 0, m.start()) + 1
    le = t.find("\n", m.end()) + 1
    prev_end = ls - 1
    if not t[:prev_end].endswith(piece):
        print(edition, "the line before the marker does not end with", repr(piece))
        continue
    t2 = t[:prev_end - len(piece)].rstrip(" ") + t[prev_end:le] + piece + t[le:]
    j = t2.find(m.group(0))
    print("=====", edition)
    print(t2[max(0, j - 200):j + len(m.group(0)) + 200])
