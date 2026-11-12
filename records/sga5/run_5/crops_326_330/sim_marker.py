"""Read-only simulation of move_marker.py on both layers of SGA 5; prints the context around the moved marker."""
import pathlib, re, sys
sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5")
folio, anchor = int(sys.argv[1]), sys.argv[2]
before = "--before" in sys.argv
for edition in ("diplomatic", "current"):
    f = W / edition / "s5.tex"
    t = f.read_text(encoding="utf-8")
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    if not m:
        print(edition, "marker not found"); continue
    print("==", edition, "line", t.count("\n", 0, m.start()) + 1, "BEFORE ==")
    print(t[max(0, m.start() - 300):m.end() + 200])
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        print("anchor not found"); continue
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    m2 = next((m for m in MARK.finditer(t2) if int(m.group(2)) == folio))
    print("==", edition, "AFTER ==")
    print(t2[max(0, m2.start() - 200):m2.end() + 200])
