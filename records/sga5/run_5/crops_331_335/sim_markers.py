"""Read-only: simulate move_marker.py VOL FOLIO ANCHOR --before in memory on both layers of SGA 5 and show
the text around the marker's new place. Nothing is written."""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")

for folio, anchor in ((332, "\\["), (336, "\\item")):
    for edition in ("diplomatic", "current"):
        f = W / edition / "s5.tex"
        t = f.read_text(encoding="utf-8")
        m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
        if not m:
            print(edition, folio, "marker not found")
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
        n = t3.find(line)
        lineno = t[:m.start()].count("\n") + 1
        print("=====", edition, "folio", folio, "marker now at line", lineno, "| moved by", m.start() - k, "chars")
        print(t3[n - 160:n + len(line) + 160])
        print()
