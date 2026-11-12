import json, pathlib

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II")
BASE = RUN / "b176_180"
OUTDIR = RUN / "crops_176_180"
F = json.loads((RUN / "findings_176_180.json").read_text(encoding="utf-8"))

body = []
for p in range(176, 181):
    src = (BASE / f"page_{p}.tex").read_text(encoding="utf-8")
    for x in F:
        if x["page"] == p and x["fix"]:
            assert src.count(x["fix"]["old"]) == 1
            src = src.replace(x["fix"]["old"], x["fix"]["new"], 1)
    body.append(f"\\section*{{page {p} (fixed)}}\n" + src + "\n\\clearpage\n")

doc = (r"""\documentclass{article}
\usepackage[a4paper,margin=1.5cm]{geometry}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{amsmath,amssymb,tikz-cd}
\pagestyle{empty}
\begin{document}
""" + "".join(body) + "\\end{document}\n")
(OUTDIR / "fixed_pages.tex").write_text(doc, encoding="utf-8")
print("wrote fixed_pages.tex")
