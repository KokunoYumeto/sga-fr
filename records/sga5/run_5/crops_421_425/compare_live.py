"""Compare page_NNN.tex of the batch with the live span of s5.tex (diplomatic) between the markers."""
import re
import sys
import pathlib

B = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\b421_425")
src = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5\diplomatic\s5.tex")
t = src.read_text(encoding="utf-8")
marks = [(int(m.group(2)), m.start()) for m in re.finditer(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%", t)]
pos = dict(marks)
order = [f for f, _ in marks]
for n in range(421, 426):
    p = (B / ("page_%d.tex" % n)).read_text(encoding="utf-8")
    body = p.split("\n", 1)[1]
    s = pos[n]
    nxt = order[order.index(n) + 1]
    live = t[s:pos[nxt]]
    print(n, "same" if live == body else "DIFFERENT", len(body), len(live), repr(p[-30:]))
