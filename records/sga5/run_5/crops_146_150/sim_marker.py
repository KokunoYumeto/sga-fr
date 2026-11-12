import re, sys
sys.stdout.reconfigure(encoding='utf-8')
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
folio, anchor = 147, "On a de même"
for ed in ("diplomatic", "current"):
    p = rf"C:/Users/user/Documents/sga_scan_check_20261105/sga5/{ed}/s5.tex"
    t = open(p, encoding="utf-8", newline="").read()
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    end = m.end() + (1 if t[m.end():m.end()+1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start())
    prev = MARK.search(t, 0)
    # occurrences of the anchor between the folio-146 marker and the folio-147 marker
    m146 = next(mm for mm in MARK.finditer(t) if int(mm.group(2)) == 146)
    print(ed, "anchor count on p146 span:", t[m146.end():m.start()].count(anchor), "line of anchor:", t2[:k].count("\n")+1)
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t3 = t2[:ls] + m.group(0) + "\n" + t2[ls:]
    else:
        t3 = t2[:k] + "\n" + m.group(0) + "\n" + t2[k:]
    j = t3.find(m.group(0))
    print(repr(t3[j-120:j+len(m.group(0))+60]))
