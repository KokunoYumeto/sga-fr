"""Read-only simulation of 'move_marker.py VOL FOLIO ANCHOR --before' on both layers of s5.tex.

Usage: python -I simulate_marker.py FOLIO ANCHOR
Nothing is written; the lines around the moved marker are printed.
"""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
folio, anchor = int(sys.argv[1]), sys.argv[2]

for edition in ("diplomatic", "current"):
    f = ROOT / edition / "s5.tex"
    t = f.read_text(encoding="utf-8")
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start())
    count_before = t2.count(anchor, 0, m.start())
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    n = t2.find(line)
    lineno = t2.count("\n", 0, n) + 1
    print(f"== {edition}: anchor occurrences before old marker: {count_before}; marker would stand on line {lineno}")
    lines = t2.split("\n")
    for i in range(lineno - 2, lineno + 2):
        print(i + 1, "|", lines[i][-90:] if i < lineno - 1 else lines[i][:90])
