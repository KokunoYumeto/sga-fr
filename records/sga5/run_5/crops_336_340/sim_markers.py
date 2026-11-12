import re, pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
base = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5")
moves = [(336, "\item", True), (338, "\[", True), (339, "et on pose", True)]
for ed in ("diplomatic", "current"):
    t = (base / ed / "s5.tex").read_text(encoding="utf-8")
    for folio, anchor, before in moves:
        m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
        line = m.group(0)
        end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
        t2 = t[:m.start()] + t[end:]
        k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
        ls = t2.rfind("\n", 0, k) + 1
        if t2[ls:k].strip() == "":
            t3 = t2[:ls] + line + "\n" + t2[ls:]
        else:
            t3 = t2[:k] + "\n" + line + "\n" + t2[k:]
        i = t3.find(line)
        print(ed, folio, "moved by", m.start() - i, "chars")
        print(repr(t3[i - 120:i + len(line) + 80]))
        print()
