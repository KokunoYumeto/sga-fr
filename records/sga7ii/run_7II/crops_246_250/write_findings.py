"""Write findings_246_250.json for SGA 7 II pp. 246-250 and check that each fix's old occurs exactly once on its page."""
import json
import pathlib
import sys

run = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II")
out = run / "findings_246_250.json"
folder = run / "b246_250"

F = [
    # ---------------- page 246 ----------------
    dict(page=246,
         where="label of the display after \"D'autre part,\" (the one cited as (5.3.7) below it)",
         scan="5.3.7. : no parentheses, a full stop after the number (checked at 1.8x); the other numbers of the "
              "page are (5.3.5), (5.3.6), (5.3.8)",
         tex="\\tag{5.3.7.}",
         kind="number", confidence="high",
         fix={"old": "\\tag{5.3.7.}", "new": "\\tag*{5.3.7.}"},
         note="\\tag{5.3.7.} prints (5.3.7.); \\tag* (amsmath) prints the label as the typescript has it, without "
              "parentheses. The edit also reaches the corrected layer, which has the same \\tag{5.3.7.}."),
    dict(page=246,
         where="last line: 'Démontrons maintenant (5.3.2), ou se qui revient au même, (5.3.5).'",
         scan="ou se qui revient au même (checked at 1x)",
         tex="ou se qui revient au même",
         kind="misprint_in_print", confidence="high", fix=None,
         corrected="ou ce qui revient au même",
         note="Spelling slip of the typescript (se for ce). The TeX keeps the printed reading; the corrected layer "
              "has it too."),
    # ---------------- page 247 ----------------
    dict(page=247,
         where="(5.3.9)",
         scan="π_*( Σ_{j=0}^{a-1} π^*(U_i) ξ^i ) = U_{j-i} . : summation index j, terms in i (checked at 1.8x)",
         tex="\\pi_*\\left( \\sum_{j=0}^{a-1} \\pi^*(U_i) \\, \\xi^i \\right) \\;=\\; U_{j-i} \\ .",
         kind="misprint_in_print", confidence="high", fix=None,
         corrected="\\pi_*\\left( \\sum_{i=0}^{a-1} \\pi^*(U_i) \\, \\xi^i \\right) \\;=\\; U_{a-1} \\ .",
         note="The sum runs over j while its terms are indexed by i, and U_{j-i} keeps a free j. By the two "
              "displays above (π_*(ξ^i) = 0 for i < a-1, π_*(ξ^{a-1}) = 1_X) the projection formula gives "
              "π_*(Σ_{i=0}^{a-1} π^*(U_i) ξ^i) = Σ_i U_i π_*(ξ^i) = U_{a-1}; this is what the deduction of 5.3.5 "
              "from Lemme 5.4 uses (U_{a-1} is the coefficient a_j of T^{a-1} in T^{a-1+j}, 5.4.4). The corrected "
              "layer already reads so (SGA7II-FR-XVII-014). The TeX keeps the printed reading."),
    dict(page=247,
         where="sentence after (5.3.9): 'conséquence du lemme suivant dans lequelle ξ devient T'",
         scan="dans / lequelle (checked at 1x)",
         tex="dans lequelle",
         kind="misprint_in_print", confidence="high", fix=None,
         corrected="dans lequel",
         note="Agreement slip: the antecedent is 'le lemme suivant' (masculine). The TeX keeps the printed reading; "
              "the corrected layer has it too."),
    dict(page=247,
         where="Lemme 5.4, first line: 'Soit a un entier > 0 ,'",
         scan="the underline stops after 'un entier'; '> 0' is not underlined (checked at 1.3x)",
         tex="\\underline{un entier $> 0$}",
         kind="underline", confidence="high",
         fix={"old": "\\underline{un entier $> 0$}", "new": "\\underline{un entier} $> 0$"},
         note=""),
    # ---------------- page 248 ----------------
    dict(page=248,
         where="first line: 'Désignons par S_i ∈ A la i-ième fonction symétrique'",
         scan="'la' underlined on its own, 'i-' not underlined, 'ième fonction symétrique' underlined (checked at 1.6x)",
         tex="\\underline{la $i$-ième fonction symétrique}",
         kind="underline", confidence="high",
         fix={"old": "\\underline{la $i$-ième fonction symétrique}",
              "new": "\\underline{la} $i$-\\underline{ième fonction symétrique}"},
         note="Same pattern as $A$-\\underline{algèbre} and $A$-\\underline{module libre} on p. 247."),
    # ---------------- page 249 ----------------
    dict(page=249,
         where="(5.4.7), the summation sign",
         scan="Σ_{i=0} with no upper bound (checked at 1.6x); (5.4.2) and (5.4.6) print the bound a",
         tex="\\sum_{i=0} (-1)^i",
         kind="misprint_in_print", confidence="medium", fix=None,
         corrected="\\sum_{i=0}^{a} (-1)^i",
         note="(5.4.7) is 5.4.2 multiplied by T^{j-1} ('relation obtenue en multipliant 5.4.2 par T^{j-1}'), and "
              "5.4.2 sums over i = 0,...,a. The printed sum is not false read as unbounded, since S_i = 0 for i > a; "
              "it is an omission of the typescript. The corrected layer supplies the bound (SGA7II-FR-XVII-016). "
              "The TeX keeps the printed reading."),
    # ---------------- page 250 ----------------
    dict(page=250,
         where="(5.5.3): 'dans CH(P^r)'",
         scan="CH (Chow ring) typed upright like the rest of the typescript",
         tex="\\text{dans } CH(\\mathbb{P}^r)",
         kind="font", confidence="medium",
         fix={"old": "\\text{dans } CH(\\mathbb{P}^r)", "new": "\\text{dans } \\mathrm{CH}(\\mathbb{P}^r)"},
         note="The file writes the Chow ring \\mathrm{CH} everywhere else (11 times, e.g. \\mathrm{CH}(X) on pp. 245-246); "
              "bare CH in math mode is italic and reads as the product of C and H, both variables on this page."),
    dict(page=250,
         where="(5.5.4): 'dans CH(X)'",
         scan="CH typed upright, as in (5.5.3)",
         tex="\\text{dans } CH(X)",
         kind="font", confidence="medium",
         fix={"old": "\\text{dans } CH(X)", "new": "\\text{dans } \\mathrm{CH}(X)"},
         note="As in (5.5.3)."),
    dict(page=250,
         where="(5.6.1), the sign",
         scan="(-1)^r over deg(φ) (checked at 2.2x)",
         tex="\\frac{(-1)^r}{\\deg(\\varphi)}",
         kind="misprint_in_print", confidence="high", fix=None,
         corrected="\\frac{(-1)^n}{\\deg(\\varphi)}",
         note="(5.5.3) and (5.5.4) give 1/C(N) = C(X)/(1+H)^{r+1}; put into (5.5.1), whose sign is (-1)^n "
              "((5.3.3) with a = rk N = r-n and F(T) = (T-H)^{r-1} gives (-1)^{a-1}(-1)^{r-1} = (-1)^n), this is "
              "(-1)^n/deg(φ) ∫_X C(X)/(1+H)^2: the substitution leaves the sign unchanged. (5.7.3), which rewrites "
              "(5.6.1) (∫_X C(X)/(1+H)^2 = χ(X) + χ(Δ) - 2χ(Y)), prints (-1)^n. The corrected layer already reads "
              "(-1)^n (SGA7II-FR-XVII-017). The TeX keeps the printed reading."),
    dict(page=250,
         where="Proposition 5.7.2, first line: 'une section hyperplanelisse de X'",
         scan="hyperplanelisse: no word space; its 15 letters sit in consecutive cells of the 19.4 px typewriter "
              "pitch (h at x 1022 to the last e at x 1294 = 14 pitches; pixel-measured)",
         tex="hyperplanelisse",
         kind="misprint_in_print", confidence="high", fix=None,
         corrected="hyperplane lisse",
         note="Missing word space in the typescript. The TeX keeps the printed reading; the corrected layer has "
              "it too."),
]

for x in F:
    if x["kind"] != "misprint_in_print":
        x.pop("corrected", None)
    if not x.get("note"):
        x.pop("note", None)

ok = True
for x in F:
    fx = x.get("fix")
    if not fx:
        continue
    t = (folder / f"page_{x['page']}.tex").read_text(encoding="utf-8")
    n = t.count(fx["old"])
    if n != 1 or "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]:
        ok = False
    print(x["page"], x["kind"], "old count", n)
for x in F:
    if x["kind"] == "misprint_in_print" and x.get("tex"):
        t = (folder / f"page_{x['page']}.tex").read_text(encoding="utf-8")
        print(x["page"], "misprint tex present:", x["tex"] in t)
out.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
print("written", out, len(F), "items; all olds unique:", ok)
sys.exit(0 if ok else 1)
