"""Apply the fixes of findings_041_045.json in memory to the LIVE diplomatic s5.tex text of pp. 41-46 (folio-41 marker
to folio-47 marker), plus the removal of the p. 45 note's paragraph from p. 46, and write a test document.
No source file is changed.
usage: python -I compile_live.py OUTDIR"""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
out = pathlib.Path(sys.argv[1])
root = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
F = json.load(open(root / "run_5" / "findings_041_045.json", encoding="utf-8"))
t = (root / "sga5" / "diplomatic" / "s5.tex").read_text(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
ms = {int(m.group(2)): m for m in MARK.finditer(t)}
pre = t[:t.index(r"\begin{document}")].replace(r"\nofiles", "")
seg = t[ms[41].start():ms[47].start()]
for d in F:
    if d["fix"]:
        n = seg.count(d["fix"]["old"])
        print(d["page"], d["kind"], "found", n)
        assert n == 1
        seg = seg.replace(d["fix"]["old"], d["fix"]["new"])
para = ("(*) (ajouté en 77) Inexact: il est facile, en fait, de prolonger "
        r"$\overset{\mathrm L}{\otimes}:\D^-(A)\times\D^-(A)\to\D^-(A)$ en "
        r"$\overset{\mathrm L}{\otimes}:\D^-(A)\times\D(A)\to\D(A)$." + "\n\n")
print("p46 paragraph found", seg.count(para))
assert seg.count(para) == 1
seg = seg.replace(para, "")
doc = pre + r"\begin{document}" + "\n" + seg + "\n" + r"\end{document}" + "\n"
(out / "live41_46.tex").write_text(doc, encoding="utf-8")
print("written", len(doc))
