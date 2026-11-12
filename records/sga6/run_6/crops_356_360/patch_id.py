"""One-off: replace the line-number references of the \\id entry in make_findings.py (main.tex is being edited, line
numbers shift) by a description of the macro blocks."""
import pathlib

p = pathlib.Path(__file__).resolve().parent / "make_findings.py"
s = p.read_text(encoding="utf-8")
old1 = r"(main.tex line 8473, \renewcommand{\id}{\operatorname{id}})"
new1 = r"(the block '% Local macros for Exposé V, §§6--7' of main.tex has \renewcommand{\id}{\operatorname{id}})"
old2 = "(\\\\providecommand at main.tex line 1525)"
new2 = "(\\\\providecommand{\\\\Id} near the start of main.tex, line 1525)"
assert s.count(old1) == 1 and s.count(old2) == 1, (s.count(old1), s.count(old2))
p.write_text(s.replace(old1, new1).replace(old2, new2), encoding="utf-8")
print("patched")
