"""Compare each page_NNN.tex of the batch with the same span of the diplomatic s5.tex (by marker lines)."""
import re
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
t = open(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5\diplomatic\s5.tex", encoding="utf-8").read()
ms = list(MARK.finditer(t))
for n in range(296, 301):
    p = open(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\b296_300\page_%d.tex" % n, encoding="utf-8").read()
    i = next(k for k, m in enumerate(ms) if int(m.group(2)) == n)
    seg = t[ms[i].start():ms[i + 1].start()]
    body = p.split("\n", 1)[1]
    print(n, "identical" if body.rstrip("\n") == seg.rstrip("\n") else "DIFFERENT", len(body), len(seg))
