"""Read-only simulation of move_marker.py: prints the text around the marker after the move; writes nothing."""
import pathlib, re, sys
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5")
folio, anchor = int(sys.argv[1]), sys.argv[2]
before = "--before" in sys.argv
sys.stdout.reconfigure(encoding="utf-8")
for edition in ("diplomatic", "current"):
    f = W / edition / "s5.tex"
    t = f.read_text(encoding="utf-8")
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    if not m:
        print(edition, "marker not found"); continue
    print("==", edition, "current context:")
    print(t[m.start()-400:m.end()+150])
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        print(edition, "anchor not found"); continue
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t3 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t3 = t2[:k] + "\n" + line + "\n" + t2[k:]
    p = t3.find(line)
    print("== after move:")
    print(t3[p-250:p+len(line)+250])
