"""Simulate move_marker.py (in memory only, never writes) for the markers of pages 176-181."""
import re, pathlib, sys
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
moves = [(176, r"\begin{equation}\tag{5.10.10}"), (177, r"de $\Tr_B:B\to B_\natural$ ("),
         (179, "\["), (180, r"\begin{equation}\tag{5.12.3}"), (181, r"$G$ un $A$-")]
for edition in ("diplomatic", "current"):
    t = (W / "sga5" / edition / "s5.tex").read_text(encoding="utf-8")
    for folio, anchor in moves:
        m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
        line = m.group(0)
        end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
        t2 = t[:m.start()] + t[end:]
        k = t2.rfind(anchor, 0, m.start())
        if k < 0:
            print(edition, folio, "ANCHOR NOT FOUND"); continue
        ls = t2.rfind("\n", 0, k) + 1
        if t2[ls:k].strip() == "":
            t2 = t2[:ls] + line + "\n" + t2[ls:]
        else:
            t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
        t = t2
        m2 = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio))
        sys.stdout.buffer.write((f"== {edition} folio {folio}\n" + t[max(0, m2.start()-160):m2.end()+120] + "\n").encode("utf-8"))
