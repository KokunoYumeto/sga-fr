"""Simulate move_marker.py in memory (no file is written) for folios 46 and 47 of SGA 5, both layers."""
import pathlib, re, sys
sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")

def move(t, folio, anchor, before):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        return None
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2

for ed in ("diplomatic", "current"):
    t = (W / "sga5" / ed / "s5.tex").read_text(encoding="utf-8")
    t2 = move(t, 46, "\[\n(4.7.7)", True)
    t2 = move(t2, 47, "Mais on a", True)
    lines = t2.split("\n")
    for i, l in enumerate(lines):
        if "folio 46 " in l or "folio 47 " in l:
            print(ed, "line", i + 1)
            print("\n".join("   " + x[:110] for x in lines[i - 3:i + 4]))
