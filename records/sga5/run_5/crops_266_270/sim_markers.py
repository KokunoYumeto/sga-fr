"""Read-only simulation of move_marker.py for folios 266 and 269 (SGA 5): prints the text around the marker's
new place in both editions, also after the full-stop fix of 1.4.6 (applied in memory only). Writes nothing."""
import pathlib
import re

W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
CASES = [(266, "\\["), (269, "\\subsubsection*{1.4.6")]


def move(t, folio, anchor):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    if not m:
        return None, None
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start())
    if k < 0:
        return None, None
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        return t2[:ls] + line + "\n" + t2[ls:], ls
    return t2[:k] + "\n" + line + "\n" + t2[k:], k


for edition in ("diplomatic", "current"):
    t0 = (W / "sga5" / edition / "s5.tex").read_text(encoding="utf-8")
    for label, t in (("as is", t0), ("after 1.4.6 stop fix", t0.replace("\\subsubsection*{1.4.6}", "\\subsubsection*{1.4.6.}", 1))):
        for folio, anchor in CASES:
            t3, pos = move(t, folio, anchor)
            print("=====", edition, label, "folio", folio, "anchor", repr(anchor))
            if t3 is None:
                print("FAILED")
                continue
            print(t3[max(0, pos - 90):pos + 150])
            print()
