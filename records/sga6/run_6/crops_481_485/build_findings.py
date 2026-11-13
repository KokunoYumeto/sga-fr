"""Build findings_481_485.json; check that every fix's old string occurs exactly once in its page file."""
import json, pathlib, sys
sys.stdout.reconfigure(encoding='utf-8')
HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
B = RUN / "b481_485"
OUT = RUN / "findings_481_485.json"
NL = "\u23ce"  # placeholder for a real line break inside raw strings


def T(s):
    return s.replace(NL, "\n")


def Q(s):
    return "'" + s.replace("\n", "\\n") + "'"


M482 = "%%%%%%%%%%  scan idx 495  |  folio 482  %%%%%%%%%%"
M485 = "%%%%%%%%%%  scan idx 498  |  folio 485  %%%%%%%%%%"
PAR = (r"Par additivité, on peut donc supposer que $x$ est la classe d'un $\mathcal O_X$-Module localement libre de type "
       r"fini $E$. De plus, quitte à remplacer $X$ par le schéma des drapeaux de $E$, ce qui donne une injection sur les")
OLD482 = "(1.9) est\n" + M482 + "\nconstante sur $X$."
NEW482 = "(1.9)\n" + M482 + "\nest constante sur $X$."
OLD485 = r"$c_t(x)=\sum_{i\geq0}c^i(x)t^i$." + "\n" + M485 + "\n" + PAR + r" $\Gr K^{\bullet}$ (VI 5.5), on"
NEW485 = r"$c_t(x)=\sum_{i\geq0}c^i(x)t^i$." + "\n\n" + PAR + "\n" + M485 + "\n" + r"$\Gr K^{\bullet}$ (VI 5.5), on"

F = []

# ---------------- page 481 ----------------
F.append(dict(page=481,
    where=r"(2.6.2): '0 -> f^*(j^*(Ω^1_{V'/Z})) -> (j'∘i)^*(Ω^1_{V''/Z}) -> i^*(Ω^1_{V/Y}) -> 0 .'",
    scan=r"f^*(j^*(Ω^1_{V'/Z}))",
    tex=r"f^*(j^*\Omega^1_{V'/Z})",
    kind="formula", confidence="high",
    fix={"old": r"0\longrightarrow f^*(j^*\Omega^1_{V'/Z})", "new": r"0\longrightarrow f^*(j^*(\Omega^1_{V'/Z}))"},
    note="The print has the parentheses round Omega^1_{V'/Z} (witness the same), as in the lower row of the diagram below."))
F.append(dict(page=481,
    where="diagram after 'on est ramené à voir que le diagramme :', lower row",
    scan=r"0 -> f^*(j^*(Ω^1_{V'/Z})) -> (j'∘i)^*(Ω^1_{V''/Z}) -> i^*(Ω^1_{V/Y}) -> 0",
    tex=r"f^*(j^*\Omega^1_{V'/Z}), (j'\circ i)^*\Omega^1_{V''/Z}, i^*\Omega^1_{V/Y}",
    kind="formula", confidence="high",
    fix={"old": r"& f^*(j^*\Omega^1_{V'/Z}) \arrow[r] & (j'\circ i)^*\Omega^1_{V''/Z} \arrow[r] & i^*\Omega^1_{V/Y} \arrow[r]",
         "new": r"& f^*(j^*(\Omega^1_{V'/Z})) \arrow[r] & (j'\circ i)^*(\Omega^1_{V''/Z}) \arrow[r] & i^*(\Omega^1_{V/Y}) \arrow[r]"},
    note="All three nodes of the lower row have the parentheses in the print (witness the same); one edit for the row."))
F.append(dict(page=481,
    where="'En combinant (2.6.1) et (2.6.2), on est ramené à voir que le diagramme :'",
    scan="new indented paragraph after (2.6.2)",
    tex="runs on after \\end{equation}",
    kind="other", confidence="high",
    fix={"old": T(r"\end{equation}⏎En combinant"), "new": T(r"\end{equation}⏎⏎En combinant")},
    note="Missing paragraph break."))
F.append(dict(page=481,
    where="'De la suite exacte de complexes ainsi obtenue, on déduit le triangle distingué'",
    scan="new indented paragraph after '... des morphismes en jeu.'",
    tex="run into the paragraph 'est commutatif, ... en jeu.'",
    kind="other", confidence="high",
    fix={"old": "en jeu. De la suite", "new": T("en jeu.⏎⏎De la suite")},
    note="Missing paragraph break."))
F.append(dict(page=481,
    where="statements on pp. 481-485: Corollaire 2.7 (p. 481), Proposition 3.2 (p. 483), Proposition 3.5 (p. 484), Théorème 3.6 (p. 485)",
    scan="statement word groups underlined ('Avec les notations et les hypothèses de' 2.6, 'on a dans' K˙(X) 'l'égalité suivante' :)",
    tex="statements in roman, no underline",
    kind="underline", confidence="high", fix=None,
    note=("Exposé VIII follows the Exposé II pattern of GLOBAL_ISSUES 82 (pending volume decision): not itemized. "
          "Exposé VIII has no \\underline in either layer; the TeX adds no emphasis on defined terms on these pages. "
          "The underlined continuation of Théorème 3.6 after its display ('désignant l'élément dual de la classe du "
          "complexe cotangent relatif' and the 'et' of '(2.5 et 2.3)', p. 485) belongs to the same pattern.")))
F.append(dict(page=481,
    where="letters the print underlines, pp. 481-485",
    scan=("Ω̲ (11 on p. 481), J̲/J̲², K̲/K̲², I̲/I̲² (p. 481 diagram), Z̲ (double-struck, underlined) in H^0(X,Z̲), "
          "H^0(Y,Z̲) (p. 484), the module E̲ and the dual Ě̲ (pp. 484-485), the L̲ of the cotangent complex L̲_•^{X/Y} (p. 485)"),
    tex="plain \\Omega, J, K, I, \\mathbb Z, E, \\check E, L",
    kind="underline", confidence="high", fix=None,
    note=("Convention of the Exposé VIII transcription (no \\underline anywhere in VIII, either layer; as the letters of "
          "sheaves in Exposé VII, findings_461_465): not itemized, except paragraph 3.4 (own entry, p. 484), where the "
          "underline is what separates the class Ě from the dual module Ě̲. Not by blind script: the print leaves the "
          "class Ě plain ('on note Ě', 'associe Ě', p. 484). Three examples: p. 481 "
          "'$j'^*(\\Omega^1_{V''/V'})=\\Omega^1_{V/Y}$' -> '$j'^*(\\underline{\\Omega}^1_{V''/V'})=\\underline{\\Omega}^1_{V/Y}$'; "
          "p. 484 '$H^0(X,\\mathbb Z)$ et $H^0(Y,\\mathbb Z)$' -> '$H^0(X,\\underline{\\mathbb Z})$ et $H^0(Y,\\underline{\\mathbb Z})$'; "
          "p. 485 '$L^{X/Y}_\\bullet$' -> '$\\underline{L}^{X/Y}_\\bullet$' (all 16 L^{X/Y} of VIII are plain). "
          "Other places on these pages: p. 481 the other nine Omega (first display, (2.6.2), the diagram) and the diagram's J/J^2, K/K^2, I/I^2 (after the "
          "parenthesis fixes above); page_485.tex 'fini $E$', 'drapeaux de $E$', 'que $E$ est', '$\\check E=E^{-1}$' "
          "(print Ě̲ = E̲^{-1}). The underlined O of O_X (\\mathcal O) falls under the pending structure-sheaf decision.")))

# ---------------- page 482 ----------------
F.append(dict(page=482,
    where="start of page (folio-482 marker)",
    scan="page 482 begins 'est constante sur X. Comme f est projectif'",
    tex="'est' is the last word of page_481.tex ('... virtuelle de $f$ (1.9) est'); page_482.tex begins 'constante sur $X$.'",
    kind="marker", confidence="high", fix=None,
    note=("Page 482 really begins at 'est constante sur X'. Exact edit in main.tex, both layers (diplomatic about lines "
          "12326-12328, current about 12332-12334 on 13 Nov 16:10; the files are being edited, so the lines move): replace "
          + Q(OLD482) + " by " + Q(NEW482)
          + " (old string once per layer; simulated in memory: crops_481_485/sim_markers.py).")))
F.append(dict(page=482,
    where="'on peut supposer que P = P^r_Y' and the factorisation diagram",
    scan="doubly underlined P (P̳^r_Y), twice",
    tex="\\mathbb P^r_Y",
    kind="font", confidence="low", fix=None,
    note=("Volume convention, not itemized: Exposé VIII writes the print's doubly underlined P as \\mathbb P (13 places, "
          "folios 480-492), Exposé VII writes the same printed P̳ as \\mathbf P (folio 449 '\\mathbf P_X^r', print checked), "
          "and \\Sym prints the doubly underlined S of VI as a bold S. One form for the volume. The two places here: "
          "'P=\\mathbb P^r_Y' -> 'P=\\mathbf P^r_Y'; '& \\mathbb P^r_Y \\arrow[d,\"g\"]' -> '& \\mathbf P^r_Y \\arrow[d,\"g\"]'.")))

# ---------------- page 483 ----------------
F.append(dict(page=483,
    where="'On obtient donc en particulier un homomorphisme additif :'",
    scan="new indented paragraph after the display of Proposition 3.2",
    tex="runs on after \\]",
    kind="other", confidence="high",
    fix={"old": T(r"\]⏎On obtient donc"), "new": T(r"\]⏎⏎On obtient donc")},
    note="Missing paragraph break."))
F.append(dict(page=483,
    where="'Pour toute K-λ-algèbre augmentée Λ, nous avons défini'",
    scan="new indented paragraph after 'Ch(A) = K x (1+Â^+) .'",
    tex="runs on after \\]",
    kind="other", confidence="high",
    fix={"old": T(r"\]⏎Pour toute"), "new": T(r"\]⏎⏎Pour toute")},
    note="Missing paragraph break."))
F.append(dict(page=483,
    where="'Enfin, nous avons défini un homomorphisme d'anneaux'",
    scan="new indented paragraph after the display of c̃",
    tex="runs on after \\]",
    kind="other", confidence="high",
    fix={"old": T(r"\]⏎Enfin, nous avons"), "new": T(r"\]⏎⏎Enfin, nous avons")},
    note="Missing paragraph break."))

# ---------------- page 484 ----------------
F.append(dict(page=484,
    where="'Nous allons appliquer ces définitions aux λ-anneaux augmentés' (top of the page)",
    scan="new indented paragraph after the display 'Todd : 1+Â^+ -> 1+Â^+ .' that ends p. 483",
    tex="runs on after the \\] at the end of page_483.tex (only the marker comment between)",
    kind="other", confidence="high",
    fix={"old": "Nous allons appliquer ces", "new": T("⏎Nous allons appliquer ces")},
    note="Missing paragraph break; the blank line goes after the marker line (the marker line itself is unchanged)."))
F.append(dict(page=484,
    where="3.4: 'de type fini E, on note Ě la classe dans K˙(X) du dual Ě de E. Il est clair que la fonction qui à E associe Ě'",
    scan="E̲, on note Ě la classe dans K˙(X) du dual Ě̲ de E̲ ... qui à E̲ associe Ě",
    tex="$E$, on note $\\check E$ la classe ... du dual $\\check E$ de $E$ ... qui à $E$ associe $\\check E$",
    kind="underline", confidence="high",
    fix={"old": r"fini $E$, on note $\check E$ la classe dans $K^{\bullet}(X)$ du dual $\check E$ de $E$. Il est clair que la fonction qui à $E$ associe",
         "new": r"fini $\underline{E}$, on note $\check E$ la classe dans $K^{\bullet}(X)$ du dual $\underline{\check E}$ de $\underline{E}$. Il est clair que la fonction qui à $\underline{E}$ associe"},
    note=("The print underlines the module E and its dual and leaves the class Ě plain (witness the same); with '\\check E' "
          "for both, the TeX's 'on note Ě la classe ... du dual Ě de E' defines Ě by itself. Itemized for that reason; the "
          "other underlined letters are in the convention entry (p. 481).")))
F.append(dict(page=484,
    where="end of 3.4: 'qu'on notera x ~> x̌.'",
    scan="wavy arrow (x ⇝ x̌)",
    tex="x\\mapsto\\check x",
    kind="symbol", confidence="high",
    fix={"old": r"$x\mapsto\check x$", "new": r"$x\rightsquigarrow\check x$"},
    note="Witness the same; the file writes the print's wavy arrow \\rightsquigarrow (16 places, one in VIII on folio 488)."))
F.append(dict(page=484,
    where="'La relation à démontrer peut encore s'écrire :'",
    scan="new indented paragraph after the display of Proposition 3.5",
    tex="runs on after \\]",
    kind="other", confidence="high",
    fix={"old": T(r"\]⏎La relation"), "new": T(r"\]⏎⏎La relation")},
    note="Missing paragraph break."))

# ---------------- page 485 ----------------
F.append(dict(page=485,
    where="start of page (folio-485 marker)",
    scan=("page 485 begins 'GrK˙ (VI 5.5), on peut supposer que E est un faisceau inversible'; 'Par additivité, ... ce qui "
          "donne une injection sur les' are the last three lines of p. 484, an indented new paragraph there"),
    tex="page_485.tex begins 'Par additivité, on peut donc supposer que $x$ est la classe'",
    kind="marker", confidence="high", fix=None,
    note=("Page 485 really begins at '$\\Gr K^{\\bullet}$ (VI 5.5), on'. Exact edit in main.tex, both layers (diplomatic about "
          "lines 12412-12414, current about 12418-12420 on 13 Nov 16:10; the lines move as the files are edited): replace "
          + Q(OLD485) + " by " + Q(NEW485)
          + ". The same edit gives 'Par additivité' the paragraph break the print has (no separate entry). Old string once "
          "per layer; simulated in memory: crops_481_485/sim_markers.py.")))
F.append(dict(page=485,
    where="'Il suffit donc de montrer que c^1(x^{-1}) = -c^1(x). Or c^1(x) est la classe'",
    scan="the formula in the running text",
    tex="a display \\[ c^1(x^{-1})=-c^1(x). \\]",
    kind="other", confidence="high",
    fix={"old": T(r"montrer que⏎\[⏎c^1(x^{-1})=-c^1(x).⏎\]⏎Or"), "new": r"montrer que $c^1(x^{-1})=-c^1(x)$. Or"},
    note="The TeX makes an inline formula a display (as findings_461_465, p. 461)."))
F.append(dict(page=485,
    where="'Or c^1(x) est la classe dans Gr^kK˙(X) de x-1'",
    scan="Gr^kK˙(X)",
    tex="\\Gr^kK^{\\bullet}(X)",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"\Gr^1K^{\bullet}(X)",
    note=("The TeX keeps the printed k (witness the same). c^1(x) is the class of x-1 in Gr^1 = Fil^1/Fil^2, as the next "
          "lines use it (x^{-1}-1 ≡ 1-x mod. Fil^2K˙(X)); no k is in play in this proof. The current layer also reads Gr^k.")))
F.append(dict(page=485,
    where="display 'x^{-1}-1 ≡ 1-x   mod. Fil^2K˙(X) ;'",
    scan="mod. Fil^2K˙(X) (no parentheses)",
    tex="\\pmod{\\Fil^2K^{\\bullet}(X)}",
    kind="formula", confidence="high",
    fix={"old": r"\pmod{\Fil^2K^{\bullet}(X)}", "new": r"\qquad\mathrm{mod.}\ \Fil^2K^{\bullet}(X)"},
    note="\\pmod adds parentheses and drops the full stop of the print's plain 'mod.'; '\\qquad\\mathrm{mod.}\\ ' is the file's own form (Exposé X, 2.18)."))
F.append(dict(page=485,
    where="label 'Théorème 3.6. (Riemann-Roch).'",
    scan="3.6. (full stop after the number)",
    tex="\\textbf{Théorème 3.6 (Riemann--Roch).}",
    kind="punctuation", confidence="high",
    fix={"old": r"\textbf{Théorème 3.6 (Riemann--Roch).}", "new": r"\textbf{Théorème 3.6. (Riemann--Roch).}"},
    note="Witness the same; the bold label is accepted."))
F.append(dict(page=485,
    where="end of page_485.tex, before the folio-486 marker",
    scan="no heading: p. 485 ends 'est commutatif.'; p. 486 begins 'La démonstration du théorème 3.6 occupera la fin de cet exposé.'",
    tex="\\subsection*{Suite de la démonstration du théorème 3.6}",
    kind="extra", confidence="high",
    fix={"old": r"\subsection*{Suite de la démonstration du théorème 3.6}", "new": ""},
    note="A heading the print does not have (p. 486 checked on its scan in b486_490); both layers have it."))

# ---------------- checks ----------------
ok = True
for f in F:
    fx = f.get("fix")
    if fx is None:
        continue
    txt = (B / f"page_{f['page']}.tex").read_text(encoding="utf-8")
    n = txt.count(fx["old"])
    marker_hit = "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]
    print(f["page"], f["kind"], "count", n, "marker-in-fix" if marker_hit else "", repr(fx["old"][:60]))
    if n != 1 or marker_hit:
        ok = False
# key order as asked
KEYS = ["page", "where", "scan", "tex", "kind", "confidence", "fix", "corrected", "note"]
out = []
for f in F:
    d = {}
    for k in KEYS:
        if k == "corrected" and f["kind"] != "misprint_in_print":
            continue
        d[k] = f.get(k)
    out.append(d)
OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
from collections import Counter
c = Counter((f["page"], f["kind"] == "misprint_in_print") for f in F)
for p in (481, 482, 483, 484, 485):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
print("ALL OLD UNIQUE" if ok else "PROBLEM", len(F))
