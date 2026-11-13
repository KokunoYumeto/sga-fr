import re, sys
# Simulate move_marker.py --before for folio 601 on in-memory copies of both layers (no file is written).
BS = chr(92)
anchor = BS + "((X_i)_" + BS + "eta" + BS + "cap(X_j)_" + BS + "eta=" + BS + "varnothing" + BS + ")"
MARK = re.compile(r"%{10}  scan idx (\d+)  \|  folio (\d+)  %{10}")
for ed in ("diplomatic", "current"):
    p = r"C:/Users/user/Documents/sga_scan_check_20261105/sga6/%s/main.tex" % ed
    t = open(p, encoding="utf-8").read()
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == 601), None)
    if not m:
        print(ed, "no marker 601")
        continue
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start())
    print(ed, "anchor count", t.count(anchor), "found at", k, "marker at", m.start())
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t3 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t3 = t2[:k] + "\n" + line + "\n" + t2[k:]
    j = t3.find(line)
    print(repr(t3[j - 120:j + len(line) + 160]))
