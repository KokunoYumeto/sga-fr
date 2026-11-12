"""In-memory simulation of move_marker.py (no writes): print the lines around the moved marker."""
import pathlib, re, sys
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
folio, anchor, before = int(sys.argv[1]), sys.argv[2], "--before" in sys.argv
base = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5")
for ed in ("diplomatic", "current"):
    t = (base / ed / "s5.tex").read_text(encoding="utf-8")
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    i = t2.find(line)
    sys.stdout.buffer.write((ed + ":\n" + t2[i - 200:i + 250] + "\n-----\n").encode("utf-8"))
