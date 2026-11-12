"""Apply the fixes of findings_041_045.json in memory to pages 41-45 and write a test document (no page file changed).
usage: python -I compile_check.py OUTDIR"""
import json
import pathlib
import sys

out = pathlib.Path(sys.argv[1])
root = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
run = root / "run_5"
F = json.load(open(run / "findings_041_045.json", encoding="utf-8"))
pre = (root / "sga5" / "diplomatic" / "s5.tex").read_text(encoding="utf-8")
pre = pre[:pre.index(r"\begin{document}")].replace(r"\nofiles", "")
body = []
for p in range(41, 46):
    t = (run / "b041_045" / f"page_{p:03d}.tex").read_text(encoding="utf-8")
    for d in F:
        if d["page"] == p and d["fix"]:
            assert t.count(d["fix"]["old"]) == 1, d
            t = t.replace(d["fix"]["old"], d["fix"]["new"])
    body.append(t)
doc = pre + r"\begin{document}" + "\n" + "\n".join(body) + "\n" + r"\end{document}" + "\n"
(out / "p41_45.tex").write_text(doc, encoding="utf-8")
print("written", len(doc))
