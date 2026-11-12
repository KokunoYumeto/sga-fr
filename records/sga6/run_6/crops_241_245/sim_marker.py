"""Simulate move_marker.py VOL FOLIO ANCHOR --before in memory on both layers; print the result around the marker."""
import pathlib, re, sys
sys.stdout.reconfigure(encoding='utf-8')
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
folio, anchor = int(sys.argv[1]), sys.argv[2]
for ed in ("diplomatic", "current"):
    f = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6") / ed / "main.tex"
    t = f.read_text(encoding="utf-8")
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    print("==", ed, "before:")
    print(t[max(0, m.start() - 200):m.end() + 80])
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start())
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t3 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t3 = t2[:k] + "\n" + line + "\n" + t2[k:]
    j = t3.find(line)
    print("== after:")
    print(t3[max(0, j - 200):j + len(line) + 80])
    print()
