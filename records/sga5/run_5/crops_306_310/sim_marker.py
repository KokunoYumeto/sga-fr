"""Read-only simulation of move_marker.py (same algorithm) on both layers of SGA 5; prints the context after the move.
usage: python -I sim_marker.py FOLIO ANCHOR [--before]"""
import re, sys, pathlib
sys.stdout.reconfigure(encoding='utf-8')
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
folio, anchor = int(sys.argv[1]), sys.argv[2]
before = "--before" in sys.argv
for edition in ("diplomatic", "current"):
    f = W / "sga5" / edition / "s5.tex"
    t = f.read_text(encoding="utf-8")
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    if not m:
        print(edition, "marker not found"); continue
    line = m.group(0)
    lineno = t.count("\n", 0, m.start()) + 1
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        print(edition, "anchor not found"); continue
    # how many occurrences of the anchor lie between k and the old marker place
    seg = t2[k:m.start()] if before else t2[m.start():k]
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t3 = t2[:ls] + line + "\n" + t2[ls:]
        pos = ls
    else:
        t3 = t2[:k] + "\n" + line + "\n" + t2[k:]
        pos = k
    print("=====", edition, "marker at line", lineno, "| anchor found at offset", k, "| chars between anchor and old marker place:", len(seg))
    a = t3.rfind("\n", 0, max(0, pos - 300))
    b = t3.find("\n", pos + len(line) + 250)
    print(t3[a + 1:b])
    print("----- (old context)")
    a = t.rfind("\n", 0, max(0, m.start() - 200))
    b = t.find("\n", m.end() + 150)
    print(t[a + 1:b])
