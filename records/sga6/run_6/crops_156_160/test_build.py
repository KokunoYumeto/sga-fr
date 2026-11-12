"""Test build: the preamble of the SGA 6 diplomatic main.tex, every \\providecommand / \\renewcommand line of main.tex
before folio 156 (in order), then pages 156-160 with this batch's fixes applied, concatenated as in main.tex (the
'% from main.tex' first line of each page file dropped). Writes test_156_160.tex here only."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).parent
RUN = HERE.parent
main = (RUN.parent / "sga6" / "diplomatic" / "main.tex").read_text(encoding="utf-8")
lines = main.split("\n")
doc = next(i for i, l in enumerate(lines) if l.startswith("\\begin{document}"))
pre = lines[:doc]
start = next(i for i, l in enumerate(lines) if "|  folio 156  %" in l)
macros = [l for l in lines[doc + 1:start] if l.startswith(("\\providecommand", "\\renewcommand", "\\newcommand"))]
items = json.loads((RUN / "findings_156_160.json").read_text(encoding="utf-8"))
body = []
for p in range(156, 161):
    t = (RUN / "b156_160" / f"page_{p}.tex").read_text(encoding="utf-8")
    for d in items:
        if d["page"] == p and d["fix"]:
            assert t.count(d["fix"]["old"]) == 1, (p, d["fix"]["old"])
            t = t.replace(d["fix"]["old"], d["fix"]["new"], 1)
    body.append(t.split("\n", 1)[1] if t.startswith("% from") else t)
src = "\n".join(pre) + "\n\\begin{document}\n" + "\n".join(macros) + "\n" + "".join(body) + "\n\\end{document}\n"
(HERE / "test_156_160.tex").write_text(src, encoding="utf-8")
print("macros", len(macros), "chars", len(src))
