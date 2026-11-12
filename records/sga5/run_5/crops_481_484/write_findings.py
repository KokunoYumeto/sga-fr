"""Write findings_481_484.json after checking that every fix's old occurs exactly once in its page_NNN.tex."""
import json
import pathlib
import sys

batch = pathlib.Path(sys.argv[1])
out = pathlib.Path(sys.argv[2])

MARKER_484 = "%%%%%%%%%%  scan idx 495  |  folio 484  %%%%%%%%%%"

findings = [
    dict(page=483,
         where="Index des notations, entry 1 (I 1.4)",
         scan="dim.q.inj (typed full stop after 'dim')",
         tex=r"$\dim\mathrm{q.inj}$",
         kind="punctuation", confidence="high",
         fix={"old": r"$\dim\mathrm{q.inj}$", "new": r"$\dim.\mathrm{q.inj}$"},
         note=r"The full stop after 'dim' is missing. Exposé I 1.4 in the same file writes $\dim.\mathrm{q.inj}(K)$."),
    dict(page=483,
         where="entry 'RHom(u,v)' (III 2.1.3, 2.1.5)",
         scan="RHom(u,v): plain typed R, only 'Hom' underlined",
         tex=r"$\R\underline{\Hom}(u,v)$",
         kind="font", confidence="high",
         fix={"old": r"$\R\underline{\Hom}(u,v)$", "new": r"$\mathrm{R}\underline{\Hom}(u,v)$"},
         note=r"\R is \mathbb{R} again after Exposé III B (\renewcommand{\R}{\mathbb{R}} at its end), so the index "
              r"sets a double-struck R where the typescript has a plain typed R (Exposé III's form \mathrm{R}). "
              r"The underline under 'Hom' only is right."),
    dict(page=483,
         where="entry 'RHom_S(L_1,L_2) , Hom_S(L_1,L_2)' (III 3.1.2, 6.4.3)",
         scan="RHom_S(L_1,L_2): plain typed R, only 'Hom' underlined",
         tex=r"$\R\underline{\Hom}_S(L_1,L_2)$",
         kind="font", confidence="high",
         fix={"old": r"$\R\underline{\Hom}_S(L_1,L_2)$", "new": r"$\mathrm{R}\underline{\Hom}_S(L_1,L_2)$"},
         note=r"Same as the entry above: plain typed R, not double-struck."),
    dict(page=483,
         where="entry 'KA_{X,L♮} , KA_{X,♮}' (III B 6.5.2)",
         scan="KA_{X,L♮}: the hand-drawn natural sign stands beside L on the subscript line, at the height of L "
              "(in A_♮, G_♮ higher on the page it is drawn lower, as a subscript)",
         tex=r"K\!A_{X,L_\natural}",
         kind="formula", confidence="medium",
         fix={"old": r"K\!A_{X,L_\natural}", "new": r"K\!A_{X,L\natural}"},
         note=r"The TeX makes the natural sign a subscript of L; the print has L♮ side by side, and the body of "
              r"III B 6.5.2 writes the same symbol KA_{X,L\natural}."),
    dict(page=483,
         where=r"end of page_483.tex: its last 21 entries, from '$\QQ_\ell$-fc$(X)$ VI 1.4.3' to '$|X|$ III B 5.11.1'",
         scan="Printed p. 483 ends with 'A-fc(X)  VI 1.4.1'. Printed p. 484 (scan idx 495, the last page of "
              "SGA5.pdf) begins with 'Q_ℓ-fc(X)  VI 1.4.3' and ends with '|X|  III B 5.11.1'.",
         tex=r"No marker for folio 484: the 21 entries of p. 484 run on under the p. 483 marker, up to \end{document}.",
         kind="marker", confidence="high",
         fix={"old": r"\sgaindexentry{$\QQ_\ell$-fc$(X)$}",
              "new": MARKER_484 + "\n" + r"\sgaindexentry{$\QQ_\ell$-fc$(X)$}"},
         note="Insert the folio-484 marker on its own line before this entry. The batch folder has no strips for "
              "p. 484; I rendered SGA5.pdf idx 495 at 300 dpi (crops_481_484/page_484_s1.png to s4.png) and "
              "checked its 21 entries against the TeX: all present, one difference (the Fraktur F, next finding), "
              "plus the double-underlined fr/Fr reported as a convention."),
    dict(page=483,
         where="printed p. 484, entry 7 (X 3.1); the text sits in page_483.tex under the p. 483 marker",
         scan="typed Fraktur F: 𝔉(G,Λ)",
         tex=r"$\mathcal F(G,\Lambda)$",
         kind="font", confidence="high",
         fix={"old": r"$\mathcal F(G,\Lambda)$", "new": r"$\mathfrak F(G,\Lambda)$"},
         note=r"The index types a Fraktur F; the body of X 3.1 (p. 376) has a hand-drawn script F, where "
              r"\mathcal F is right. Filed under page 483 because the text is in page_483.tex until the "
              r"folio-484 marker is inserted."),
]

ok = True
for x in findings:
    fix = x.get("fix")
    if not fix:
        continue
    p = batch / f"page_{x['page']:03d}.tex"
    t = p.read_text(encoding="utf-8")
    n = t.count(fix["old"])
    marker_in_old = "%%%%%%%%%%" in fix["old"]
    print(x["page"], x["kind"], repr(fix["old"][:50]), "count", n, "marker-in-old" if marker_in_old else "")
    if n != 1 or marker_in_old:
        ok = False
if not ok:
    sys.exit("check failed: not writing")
out.write_text(json.dumps(findings, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
back = json.loads(out.read_text(encoding="utf-8"))
print("written", out, len(back), "findings")
