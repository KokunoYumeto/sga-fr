"""Make some fix anchors of build_findings.py unique in the whole main.tex (both layers) and add that check."""
import pathlib
p = pathlib.Path(__file__).resolve().parent / "build_findings.py"
s = p.read_text(encoding="utf-8")
reps = [
    (r'fx(r"(G_S^{n,\infty})", r"(\mathbf G_S^{n,\infty})")',
     r'fx(r"(G_S^{n,\infty})\) est le séparé", r"(\mathbf G_S^{n,\infty})\) est le séparé")'),
    (r'fx(r"\subsection*{5.1}", r"\subsection*{5.1.}")',
     r'fx(L(r"\subsection*{5.1}", "Dans ce paragraphe"), L(r"\subsection*{5.1.}", "Dans ce paragraphe"))'),
    (r'fx(r"\subsection*{5.2}", r"\subsection*{5.2.}")',
     r'fx(L(r"\subsection*{5.2}", "Si $G$ est"), L(r"\subsection*{5.2.}", "Si $G$ est"))'),
    (r'fx(L(r"\end{equation}", "Il est clair"), L(r"\end{equation}", "", "Il est clair"))',
     r'fx(L(r"  f_*(y)=a_0 .", r"\end{equation}", "Il est clair"), '
     r'L(r"  f_*(y)=a_0 .", r"\end{equation}", "", "Il est clair"))'),
    (r'fx(r"\begin{equation}\tag{5.3.1}", r"\begin{equation}\notag")',
     r'fx(L("-modules :", r"\begin{equation}\tag{5.3.1}"), L("-modules :", r"\begin{equation}\notag"))'),
    (r'fx(r"\oplus\cdots\oplus", r"\oplus\ldots\oplus")',
     r'fx(r".\bar x\oplus\cdots\oplus", r".\bar x\oplus\ldots\oplus")'),
    (r'''fx(r"\Fil^kK'(X)", r"\Fil^kK^{\bullet}(X)")''',
     r'''fx(r"f_*(\Fil^kK'(X))", r"f_*(\Fil^kK^{\bullet}(X))")'''),
]
for a, b in reps:
    n = s.count(a)
    print(n, a[:80])
    assert n == 1, a
    s = s.replace(a, b)
extra = r'''ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
for layer in ("diplomatic", "current"):
    t = (ROOT / layer / "main.tex").read_text(encoding="utf-8")
    for n, x in enumerate(F):
        f = x["fix"]
        if f is not None and t.count(f["old"]) != 1:
            print("main.tex", layer, "entry", n, "page", x["page"], "old occurs", t.count(f["old"]), "times:",
                  repr(f["old"][:70]))
'''
anchor = 'print("ALL OK" if ok else "PROBLEMS")'
assert s.count(anchor) == 1
s = s.replace(anchor, extra + anchor)
p.write_text(s, encoding="utf-8")
print("patched")
