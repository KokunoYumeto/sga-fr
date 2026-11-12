"""Assemble a test document from main.tex's preamble and the patched page copies (patched_221..225.tex) of this
folder, for a compile check of the proposed fixes. Writes test_patched.tex here; compile it with pdflatex.
usage: python -I build_test.py"""
import pathlib

HERE = pathlib.Path(__file__).parent
MAIN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex")
lines = MAIN.read_text(encoding="utf-8").split("\n")
k = next(i for i, l in enumerate(lines) if l.startswith(r"\begin{document}"))
pre = "\n".join(lines[:k])
body = [r"\begin{document}", r"\providecommand{\ob}{\operatorname{ob}}", r"\providecommand{\Ob}{\operatorname{ob}}",
        r"\begin{enumerate}[label={[\arabic*]}]", r"\setcounter{enumi}{13}", r"\item"]
for p in range(221, 226):
    body.append((HERE / f"patched_{p}.tex").read_text(encoding="utf-8"))
body.append(r"\end{document}")
(HERE / "test_patched.tex").write_text(pre + "\n" + "\n".join(body) + "\n", encoding="utf-8", newline="\n")
print("written", HERE / "test_patched.tex")
