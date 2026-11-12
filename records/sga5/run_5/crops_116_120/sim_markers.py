"""Simulate move_marker.py in memory (no writes) for the folio-117 and folio-121 markers on both layers."""
import pathlib, re, sys
sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")

def sim(t, folio, anchor, before):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        return None, "anchor not found"
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2, "ok"

for ed in ("diplomatic", "current"):
    t = (W / "sga5" / ed / "s5.tex").read_text(encoding="utf-8")
    print("==", ed, "count anchor117:", t.count("correspondance composée, et"),
          "count anchor121:", t.count("rappelons qu'on dit que $L$ est parfait"))
    t2, s = sim(t, 117, "correspondance compos", False)
    i = t2.find("folio 117")
    print(s, repr(t2[i-200:i+120]))
    t3, s = sim(t, 121, "rappelons qu", True)
    i = t3.find("folio 121")
    print(s, repr(t3[i-200:i+160]))
