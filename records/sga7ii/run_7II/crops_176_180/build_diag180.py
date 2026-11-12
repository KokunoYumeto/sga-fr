import re, pathlib

src = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II\b176_180\page_180.tex").read_text(encoding="utf-8")
blocks = re.findall(r"\\begin\{tikzcd\}.*?\\end\{tikzcd\}", src, flags=re.S)
doc = [r"\documentclass{article}\usepackage[a4paper,margin=1cm]{geometry}\usepackage{amsmath,amssymb,tikz-cd}\pagestyle{empty}\begin{document}"]
for b in blocks:
    doc.append(r"\begin{center}" + b + r"\end{center}\bigskip\hrule\bigskip")
doc.append(r"\end{document}")
out = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II\crops_176_180\diag_test180.tex")
out.write_text("\n".join(doc), encoding="utf-8")
print(len(blocks), "blocks ->", out)
