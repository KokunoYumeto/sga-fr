"""Build two test documents from pages 91-95 (as they are, and with every fix of findings_091_095.json applied in
list order) with the preamble and the Exposé I macro block of main.tex, for a compile check."""
import json
import pathlib

here = pathlib.Path(__file__).resolve().parent
RUN = here.parent
main = (RUN.parent / "sga6" / "diplomatic" / "main.tex").read_text(encoding="utf-8").split("\n")
pre = "\n".join(main[:81])  # lines 1-81: preamble up to (not including) \begin{document}
k91 = next(i for i, l in enumerate(main) if "|  folio 91  %" in l)
# every macro definition line of the body before the folio-91 marker, in order (the macro state at p. 91)
macros = "\n".join(l for l in main[82:k91]
                   if l.lstrip().startswith(("\\providecommand", "\\newcommand", "\\renewcommand", "\\def",
                                             "\\DeclareMathOperator")))
pages = {p: (RUN / "b091_095" / f"page_{p:03d}.tex").read_text(encoding="utf-8") for p in range(91, 96)}
fixed = dict(pages)
for x in json.loads((RUN / "findings_091_095.json").read_text(encoding="utf-8")):
    fx = x.get("fix")
    if fx:
        assert fixed[x["page"]].count(fx["old"]) == 1, (x["page"], fx["old"][:50])
        fixed[x["page"]] = fixed[x["page"]].replace(fx["old"], fx["new"])
for name, src in (("t_orig", pages), ("t_fixed", fixed)):
    body = "\n\n\\medskip\\hrule\\medskip\n\n".join(src[p] for p in range(91, 96))
    doc = pre + "\n\\begin{document}\n" + macros + "\n" + body + "\n\\end{document}\n"
    (here / f"{name}.tex").write_text(doc, encoding="utf-8")
    print("wrote", name)
