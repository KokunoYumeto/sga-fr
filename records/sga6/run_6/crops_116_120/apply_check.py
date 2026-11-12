"""Apply the fixes of findings_116_120.json to copies of the pages (JSON order and reverse order), check that each
old is found exactly once at its turn and that both orders give the same text; write the patched pages and a small
LaTeX test document (preamble macros of main.tex) to OUTDIR for a compile check."""
import json
import pathlib
import sys

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
MAIN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex")
OUTDIR = pathlib.Path(sys.argv[1])
OUTDIR.mkdir(parents=True, exist_ok=True)
findings = json.loads((RUN / "findings_116_120.json").read_text(encoding="utf-8"))

body = []
for p in range(116, 121):
    orig = (RUN / "b116_120" / f"page_{p}.tex").read_text(encoding="utf-8")
    fixes = [f["fix"] for f in findings if f["page"] == p and f["fix"]]
    res = []
    for order in (fixes, list(reversed(fixes))):
        t = orig
        for fx in order:
            n = t.count(fx["old"])
            if n != 1:
                print("page", p, "old found", n, "times:", repr(fx["old"][:60]))
            t = t.replace(fx["old"], fx["new"], 1)
        res.append(t)
    print(p, "orders agree:", res[0] == res[1], "braces:", res[0].count("{") - res[0].count("}"))
    (OUTDIR / f"patched_{p}.tex").write_text(res[0], encoding="utf-8")
    body.append(res[0])

main = MAIN.read_text(encoding="utf-8")
pre = main[:main.index(r"\begin{document}")]
# every macro definition line of main.tex before the folio-116 marker, in order (as the volume defines them)
cut = main.index("|  folio 116  %")
blocks = "\n".join(l for l in main[main.index(r"\begin{document}"):cut].splitlines()
                   if l.lstrip().startswith((r"\providecommand", r"\newcommand", r"\renewcommand", r"\DeclareMathOperator")))
doc = pre + "\\begin{document}\n" + blocks + "\n" + "\n".join(body) + "\n\\end{document}\n"
(OUTDIR / "test_116_120.tex").write_text(doc, encoding="utf-8")
print("written", OUTDIR / "test_116_120.tex")
