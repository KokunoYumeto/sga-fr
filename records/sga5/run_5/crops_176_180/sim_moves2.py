"""In-memory simulation (never writes) of the marker fixes for folios 177, 179, 180 on both layers of s5.tex."""
import re, pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")

def pull(t, folio, piece):
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    ls = t.rfind("\n", 0, m.start()) + 1
    le = t.find("\n", m.end()) + 1
    prev_end = ls - 1
    assert t[:prev_end].endswith(piece), "piece not at line end"
    return t[:prev_end - len(piece)].rstrip(" ") + t[prev_end:le] + piece + t[le:]

def move_before(t, folio, anchor):
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start())
    assert k >= 0
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        return t2[:ls] + line + "\n" + t2[ls:]
    return t2[:k] + "\n" + line + "\n" + t2[k:]

for edition in ("diplomatic", "current"):
    t = (W / "sga5" / edition / "s5.tex").read_text(encoding="utf-8")
    t = pull(t, 177, r"de $\Tr_B:B\to B_\natural$ (")
    t = move_before(t, 179, "\[")
    t = move_before(t, 180, r"\begin{equation}\tag{5.12.3}")
    for folio in (177, 179, 180):
        m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
        ln = t.count("\n", 0, m.start()) + 1
        print(f"== {edition} folio {folio} (marker now on line {ln})")
        print(t[max(0, m.start() - 110):m.end() + 110])
