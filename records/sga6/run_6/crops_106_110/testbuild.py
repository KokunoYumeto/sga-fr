"""Compile check for pp. 106-110 of SGA 6: two test documents (the pages as they are, and with every fix of
findings_106_110.json applied in list order and the folio-107/108 marker moves simulated on copies), with the
preamble and the macro definitions of main.tex in force at p. 106. Nothing outside this folder is written.
A third document applies all fixes except the display entry (to check the \\emph groups around the display)."""
import json
import pathlib
import subprocess

here = pathlib.Path(__file__).resolve().parent
RUN = here.parent
main = (RUN.parent / "sga6" / "diplomatic" / "main.tex").read_text(encoding="utf-8").split("\n")
pre = "\n".join(main[:81])
k106 = next(i for i, l in enumerate(main) if "|  folio 106  %" in l)
macros = "\n".join(l for l in main[82:k106]
                   if l.lstrip().startswith(("\\providecommand", "\\newcommand", "\\renewcommand", "\\def",
                                             "\\DeclareMathOperator")))
pages = {p: (RUN / "b106_110" / f"page_{p:03d}.tex").read_text(encoding="utf-8") for p in range(106, 111)}
F = json.loads((RUN / "findings_106_110.json").read_text(encoding="utf-8"))


def apply(skip_display=False):
    cur = dict(pages)
    for x in F:
        fx = x.get("fix")
        if not fx:
            continue
        if skip_display and x["kind"] == "other":
            continue
        if skip_display and fx["old"] == "(*=+,-,b)":
            pass
        assert cur[x["page"]].count(fx["old"]) == 1, (x["page"], fx["old"][:50])
        cur[x["page"]] = cur[x["page"]].replace(fx["old"], fx["new"])
    return cur


def move(text, folio, anchor):
    """move_marker.py logic (--before) on one string holding the pages in order"""
    import re
    MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
    m = next(m for m in MARK.finditer(text) if int(m.group(2)) == folio)
    line = m.group(0)
    end = m.end() + (1 if text[m.end():m.end() + 1] == "\n" else 0)
    t2 = text[:m.start()] + text[end:]
    k = t2.rfind(anchor, 0, m.start())
    assert k >= 0, anchor
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        return t2[:ls] + line + "\n" + t2[ls:]
    return t2[:k] + "\n" + line + "\n" + t2[k:]


def joined(src):
    # the page files each start with '% from main.tex' and their marker; main.tex has the marker only
    return "".join(src[p].split("\n", 1)[1] for p in range(106, 111))


docs = {"t_orig": joined(pages)}
fixed = joined(apply())
fixed = move(fixed, 107, r"on a \(F=F^p[-p]\)")
fixed = move(fixed, 108, r"\emph{Alors} :")
docs["t_fixed"] = fixed
docs["t_fixed_nodisplay"] = move(move(joined(apply(skip_display=True)), 107, r"on a \(F=F^p[-p]\)"), 108,
                                 r"\emph{Alors} :")
(here / "sim_markers.txt").write_text(fixed, encoding="utf-8")
for name, body in docs.items():
    doc = pre + "\n\\begin{document}\n" + macros + "\n" + body + "\n\\end{document}\n"
    (here / f"{name}.tex").write_text(doc, encoding="utf-8")
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", f"{name}.tex"], cwd=here,
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    log = (here / f"{name}.log").read_text(encoding="utf-8", errors="replace")
    errs = [l for l in log.split("\n") if l.startswith("!")]
    print(name, "exit", r.returncode, "errors:", errs[:5])
