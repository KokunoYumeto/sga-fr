"""Apply the findings' fixes (in memory) to pages 241-245 and write a test document with the s5.tex preamble.
The page files and s5.tex are not modified."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
SRC = RUN / "b241_245"
S5 = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5\diplomatic\s5.tex")
F = json.loads((RUN / "findings_241_245.json").read_text(encoding="utf-8"))
pre = S5.read_text(encoding="utf-8").split("\\begin{document}")[0]
envs = r"""
\renewenvironment{statement}[1]{\par\medskip\noindent\textbf{#1.}\ }{\par\medskip}
\renewcommand{\uRHom}{\underline{\RHom}}
\renewcommand{\R}{\mathbb{R}}
\renewenvironment{prooftext}[1][Preuve]{\par\noindent\emph{#1} :\ }{\par\medskip}
"""
body = []
for p in range(241, 246):
    t = (SRC / f"page_{p}.tex").read_text(encoding="utf-8")
    for d in F:
        if d["page"] == p and d["fix"]:
            o, n = d["fix"]["old"], d["fix"]["new"]
            assert t.count(o) == 1, (p, o[:60])
            t = t.replace(o, n)
    body.append(t)
doc = pre + "\\begin{document}\n" + envs + "".join(body) + "\n\\end{document}\n"
(HERE / "test_241_245.tex").write_text(doc, encoding="utf-8", newline="\n")
print("written", len(doc))
