import re, sys, pathlib

# Extract every tikzcd block from pages 178 and 179 (exact source) and build a
# test document: each block as written, then with the proposed label fixes.
base = pathlib.Path(sys.argv[1])  # b176_180 folder
out = pathlib.Path(sys.argv[2])   # output .tex

fixes = {
    178: [('H^n(U,K) \\arrow[ul, "\\wr"\']', 'H^n(U,K) \\arrow[ul, "\\wr"]')],
    179: [('\\arrow[r, "\\partial"] \\arrow[d, "\\wr"\']', '\\arrow[r, "\\partial"] \\arrow[d, "\\wr"]'),
          ('\\arrow[d, "\\wr"] & H^i(X)', '\\arrow[d, "\\wr"\'] & H^i(X)'),
          ('\\arrow[d, "\\wr"\', "(2.1.2(\\mathrm{i}))"]', '\\arrow[d, "\\wr", "(2.1.2(\\mathrm{i}))"\']')],
}

parts = [r"""\documentclass{article}
\usepackage[a4paper,margin=1cm]{geometry}
\usepackage{amsmath,amssymb,tikz-cd}
\pagestyle{empty}
\begin{document}
"""]
for p in (178, 179):
    src = (base / f"page_{p}.tex").read_text(encoding="utf-8")
    blocks = re.findall(r"\\begin\{tikzcd\}.*?\\end\{tikzcd\}", src, flags=re.S)
    for i, b in enumerate(blocks, 1):
        fb = b
        for old, new in fixes.get(p, []):
            if old in fb:
                fb = fb.replace(old, new)
        parts.append(f"\\noindent p{p} diagram {i}, AS WRITTEN:\\par\\medskip\n\\begin{{center}}\n{b}\n\\end{{center}}\n")
        if fb != b:
            parts.append(f"\\noindent p{p} diagram {i}, FIXED:\\par\\medskip\n\\begin{{center}}\n{fb}\n\\end{{center}}\n")
        parts.append("\\bigskip\\hrule\\bigskip\n")
parts.append("\\end{document}\n")
out.write_text("".join(parts), encoding="utf-8")
print("wrote", out)
