# In-memory simulation of move_marker.py --before for folios 136, 137, 141 (no file is written).
import re, sys, pathlib
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
root = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5")
moves = [(136, "\section*{B"), (137, "\item"), (141, "$D_{\ctf}(X)$ (resp. $D_{\ctf}(Y)$) est")]
for ed in ("diplomatic", "current"):
    t = (root / ed / "s5.tex").read_text(encoding="utf-8")
    for folio, anchor in moves:
        m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
        line = m.group(0)
        end = m.end() + (1 if t[m.end():m.end()+1] == "\n" else 0)
        t2 = t[:m.start()] + t[end:]
        k = t2.rfind(anchor, 0, m.start())
        if k < 0:
            print(ed, folio, "anchor not found"); continue
        ls = t2.rfind("\n", 0, k) + 1
        if t2[ls:k].strip() == "":
            t2 = t2[:ls] + line + "\n" + t2[ls:]
        else:
            t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
        t = t2
        j = t.find(line)
        print("==", ed, folio, "count of anchor in file:", t.count(anchor))
        print(repr(t[max(0, j-120):j+len(line)+120]))
