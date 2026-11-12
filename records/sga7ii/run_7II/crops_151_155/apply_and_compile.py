"""Apply the findings' fixes to copies of the page files and compile them, to check that the edits are valid TeX."""
import json
import pathlib
import subprocess

BASE = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II")
CROPS = BASE / "crops_151_155"
F = json.loads((BASE / "findings_151_155.json").read_text(encoding="utf-8"))

bodies = []
for p in range(151, 156):
    t = (BASE / "b151_155" / f"page_{p}.tex").read_text(encoding="utf-8")
    for x in F:
        if x["page"] == p and x.get("fix"):
            assert t.count(x["fix"]["old"]) == 1
            t = t.replace(x["fix"]["old"], x["fix"]["new"])
    (CROPS / f"fixed_page_{p}.tex").write_text(t, encoding="utf-8", newline="")
    bodies.append(t)

doc = ("\\documentclass{article}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n"
       "\\usepackage{tikz-cd}\n\\begin{document}\n" + "\n\\clearpage\n".join(bodies) + "\n\\end{document}\n")
(CROPS / "fixed_pages.tex").write_text(doc, encoding="utf-8", newline="")
r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "fixed_pages.tex"],
                   cwd=CROPS, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=300)
print("exit", r.returncode)
log = (CROPS / "fixed_pages.log").read_text(encoding="utf-8", errors="replace")
for line in log.splitlines():
    if line.startswith("!") or "Error" in line or "Undefined" in line:
        print(line)
print(log.splitlines()[-2:])
