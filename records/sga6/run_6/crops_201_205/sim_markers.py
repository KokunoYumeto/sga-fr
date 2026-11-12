r"""Simulate in memory (nothing written) the marker fix of p. 201 on both layers of SGA 6 main.tex,
python -I move_marker.py 6 201 '\[' --before, and show the present state of the folio-206 marker
(split 'consé%' / marker / 'quence', reported by batch 206-210 and applied at 20:28)."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
BASE = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6"


def move(t, folio, anchor, before):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        return t, None
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2, t2.find(line)


for layer in ("diplomatic", "current"):
    with open(BASE + "\\" + layer + r"\main.tex", encoding="utf-8") as fh:
        t = fh.read()
    t, pos = move(t, 201, r"\[", True)
    print(f"--- {layer} folio 201 after the move:\n{t[max(0, pos - 90):pos]!r}\n{t[pos:pos + 170]!r}\n")
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == 206)
    print(f"--- {layer} folio 206 now:\n{t[max(0, m.start() - 60):m.start()]!r}\n{t[m.start():m.start() + 90]!r}\n")
