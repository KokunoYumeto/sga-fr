"""Assemble a compile test: the s5.tex preamble, Exposé V's environments, and the simulated region of pp. 246-250."""
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
HERE = W / "run_5" / "crops_246_250"
src = (W / "sga5" / "diplomatic" / "s5.tex").read_text(encoding="utf-8")
k = src.index("\\begin{document}") + len("\\begin{document}\n")
pre = src[:k]
env = ("\\renewenvironment{statement}[1]{\\par\\medskip\\noindent\\textbf{#1.}\\ }{\\par\\medskip}\n"
       "\\renewenvironment{prooftext}[1][Preuve]{\\par\\noindent\\emph{#1} :\\ }{\\par\\medskip}\n")
for name in ("dipl", "curr"):
    body = (HERE / f"sim_{name}_246_250.tex").read_text(encoding="utf-8")
    (HERE / f"test_{name}.tex").write_text(pre + env + body + "\n\\end{document}\n", encoding="utf-8", newline="")
print("ok")
