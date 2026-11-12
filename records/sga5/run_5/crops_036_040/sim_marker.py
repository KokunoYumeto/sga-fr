import sys, re, pathlib
sys.stdout.reconfigure(encoding="utf-8")
root = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
folio, anchor = int(sys.argv[1]), sys.argv[2]
for ed in ("diplomatic", "current"):
    t = (root / ed / "s5.tex").read_text(encoding="utf-8")
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end()+1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start())
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    i = t2.find(line)
    print(ed, "| before:", repr(t2[i-120:i]), "| after:", repr(t2[i+len(line):i+len(line)+60]))
