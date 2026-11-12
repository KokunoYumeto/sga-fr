# Read-only simulation of move_marker.py (same logic, never writes).
import re, sys, pathlib
sys.stdout.reconfigure(encoding='utf-8')
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
folio, anchor = int(sys.argv[1]), sys.argv[2]
before = "--before" in sys.argv
for edition in ("diplomatic", "current"):
    f = W / "sga5" / edition / "s5.tex"
    t = f.read_text(encoding="utf-8")
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    mline = t.count("\n", 0, m.start()) + 1
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t3 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t3 = t2[:k] + "\n" + line + "\n" + t2[k:]
    m3 = next((mm for mm in MARK.finditer(t3) if int(mm.group(2)) == folio))
    a = t3.rfind("\n", 0, t3.rfind("\n", 0, m3.start())) + 1
    b = t3.find("\n", t3.find("\n", m3.end()) + 1)
    b = t3.find("\n", b + 1)
    print("==", edition, "marker now at line", mline, "; anchor line", t.count("\n", 0, t.rfind(anchor, 0, m.start())) + 1)
    print(repr(t3[a:b]))
