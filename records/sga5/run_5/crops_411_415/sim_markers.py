"""In-memory simulation of move_marker.py --before for the markers of pages 411-415 (writes nothing)."""
import re
import sys
import pathlib

MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
W = pathlib.Path(r"C:/Users/user/Documents/sga_scan_check_20261105/sga5")
moves = [
    (411, r"\["),
    (412, "\u00e0 l'"),
    (413, r"\begin{align*}"),
    (414, r"\begin{equation}\tag{3.1}"),
    (415, r"\["),
]
sys.stdout.reconfigure(encoding="utf-8")
for ed in ("diplomatic", "current"):
    t = (W / ed / "s5.tex").read_text(encoding="utf-8")
    for folio, anchor in moves:
        m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
        line = m.group(0)
        mline = t.count("\n", 0, m.start()) + 1
        end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
        t2 = t[:m.start()] + t[end:]
        k = t2.rfind(anchor, 0, m.start())
        aline = t2.count("\n", 0, k) + 1
        ls = t2.rfind("\n", 0, k) + 1
        if t2[ls:k].strip() == "":
            t2 = t2[:ls] + line + "\n" + t2[ls:]
        else:
            t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
        t = t2
        m2 = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
        print(f"== {ed} folio {folio}: marker was line {mline}, anchor {anchor!r} found at line {aline}")
        print(t[max(0, m2.start() - 160):m2.end() + 140])
        print()
