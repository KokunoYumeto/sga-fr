"""Write findings_271_275_recheck.json and check that every fix's old occurs exactly once on its page."""
import json
import pathlib
import sys

RUN = pathlib.Path(sys.argv[1])
PAGES = RUN / "b271_275"
OUT = RUN / "findings_271_275_recheck.json"

F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": confidence,
         "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 271
add(271, "below formula (4.2.1), right half",
    "under the arrow of Ker(f_*:H^•(X̃,Z_ℓ) → H^•(X,Z_ℓ)) the print has a hand-drawn vertical arrow pointing down "
    "(head partly broken) and, under it, very faint broken typed characters (perhaps H^•(X,Z_ℓ))",
    "nothing after the display",
    "other", "low",
    {"old": r"\end{equation*}",
     "new": "\\end{equation*}\n"
            "% STRUCTURE: sous « \\longrightarrow H^{\\bullet}(X,\\mathbb{Z}_{\\ell})) » le tirage montre une flèche verticale\n"
            "%   descendante tracée à la main (pointe incomplète) et, au-dessous, des caractères dactylographiés très pâles\n"
            "%   et cassés, illisibles (peut-être « H^{\\bullet}(X,\\mathbb{Z}_{\\ell}) ») : vestige apparent d'une première\n"
            "%   disposition verticale effacée, remplacée par la flèche horizontale ; non reproduit."},
    "The marks are printed in black (not show-through). They look like the remains of a deleted first layout "
    "(target typed under a vertical arrow) that the in-line → H^•(X,Z_ℓ)) replaced; the TeX gives the corrected "
    "wording, so only a comment is proposed.")

add(271, "Remarque 3.2.12, second line",
    "'(condition vérifiéeen tous cas': the é is blotted and an e is typed into the following space, so "
    "'vérifiée' runs into 'en'",
    "vérifiée en",
    "misprint_in_print", "medium",
    {"old": "vérifiée en", "new": "vérifiéeen"},
    "The typist's correction vérifié -> vérifiée took the space after the word (monospaced columns: 'tous cas' "
    "stays where 'vérifié en tous cas' put it), the same slip as 'totalede' on p. 273, which the TeX keeps. "
    "The TeX silently corrects; the fix restores the printed reading.",
    corrected="vérifiée en")

# ---------------- page 272
add(272, "(4.2.3), second line",
    "par \"transport de structure\" par: 'par', 'transport de structure' and 'par' underlined separately, the "
    "quotation marks not underlined",
    r"\underline{déduite par ``transport de structure'' par}",
    "underline", "high",
    {"old": r"\underline{déduite par ``transport de structure'' par}",
     "new": r"\underline{déduite par} ``\underline{transport de structure}'' \underline{par}"},
    "The underline stops before each quotation mark. Leave it out if the global underline rule (inner comma) is "
    "extended to quotation marks.")

add(272, "(4.2.3), display of the elements",
    "x,y ∈ H^{•-2}(Δ,Z_ℓ(-1)  ,",
    r"x,y \in H^{\bullet-2}(\Delta,\mathbb{Z}_{\ell}(-1) \quad ,",
    "misprint_in_print", "high", None,
    "The closing parenthesis of H^{•-2}(...) is missing in the print. The TeX keeps the printed reading.",
    corrected=r"x,y \in H^{\bullet-2}(\Delta,\mathbb{Z}_{\ell}(-1)) \quad ,")

add(272, "(4.2.3.2)",
    "(a ⊕ 0) ∧ (b ⊕ 0   =   ab ⊕ 0  ,",
    r"(a \oplus 0) \wedge (b \oplus 0 \;=\;",
    "misprint_in_print", "high", None,
    "The closing parenthesis after b ⊕ 0 is missing in the print. The TeX keeps the printed reading.",
    corrected=r"(a \oplus 0) \wedge (b \oplus 0) \;=\;")

add(272, "after 'En particulier, pour', first display",
    "a ⊕ x ∈ H^•(X,Z_ℓ) ⊕ H^{•-2}(Δ,Z_ℓ(-1)",
    r"\;\; \oplus H^{\bullet-2}(\Delta,\mathbb{Z}_{\ell}(-1)",
    "misprint_in_print", "high", None,
    "The closing parenthesis of H^{•-2}(...) is missing in the print. The TeX keeps the printed reading.",
    corrected=r"\;\; \oplus H^{\bullet-2}(\Delta,\mathbb{Z}_{\ell}(-1))")

# ---------------- page 273
add(273, "Autrement dit, ...",
    "la matrice d'intersection totalede H^•(X̃, Z_ℓ)",
    "totalede",
    "misprint_in_print", "high", None,
    "Missing space in the print. The TeX keeps the printed reading.",
    corrected="totale de")

add(273, "Démonstration, first sentence",
    "On a déjà démontré (4.2.1) ;(cf. 2.2.22)).",
    "(4.2.1) ;(cf. 2.2.22)).",
    "misprint_in_print", "medium", None,
    "Unbalanced parentheses: the opening parenthesis of the formula number (2.2.22) is missing (cf. "
    "'est exacte (cf. (1.2.2))' on the same page). The semicolon before '(cf.' is odd too but is left as printed. "
    "The TeX keeps the printed reading.",
    corrected="(4.2.1) ;(cf. (2.2.22)).")

add(273, "diagram (4.2.5), vertical arrow j^*",
    "open head pointing down at the bottom and a heavy solid head pointing up at the top of the shaft",
    r'\arrow[d, leftrightarrow, "j^{*}"]',
    "misprint_in_print", "low", None,
    "j^*: H^•(X,Z_ℓ) → H^•(Δ,Z_ℓ) goes down only; the upper head is a slip of the drawing (perhaps a blotted "
    "correction). The TeX and its STRUCTURE comment reproduce both heads; the corrected edition needs the plain "
    "downward arrow.",
    corrected=r'\arrow[d, "j^{*}"]')

# ---------------- page 274
add(274, "diagram (4.2.7), lower row, second node",
    "H^{•-2}(Δ, Z_ℓ(-2))",
    r"0 & H^{\cdot-2}(\Delta,\mathbb{Z}_\ell(-2))",
    "misprint_in_print", "high", None,
    "The transpose of H^{2n-•}(Δ,Z_ℓ) (dim Δ = n-2) is H^{•-4}(Δ,Z_ℓ(-2)): this node is the target of "
    "g_*: H^{•-2}(Δ̃,Z_ℓ(-1)) → and the source of the codimension-2 Gysin map j_* into H^•(X,Z_ℓ), both of which "
    "need •-4; the twist (-2) agrees. The TeX keeps the printed exponent.",
    corrected=r"0 & H^{\cdot-4}(\Delta,\mathbb{Z}_\ell(-2))")

add(274, "diagram (4.2.7), lower row, arrow H^{•-2}(Δ,Z_ℓ(-1)) → H^{•-2}(Δ̃,Z_ℓ(-1))",
    "label g_*",
    "\\arrow[l, \"g_*\"'] \\arrow[u, equal]",
    "misprint_in_print", "high", None,
    "A map from the cohomology of Δ to that of Δ̃ can only be g^* (g: Δ̃ → Δ); it is the transpose of g_* in "
    "(4.2.5), and commutativity with i_*g^* in the upper row and the equality column requires g^*. The TeX keeps "
    "g_*.",
    corrected="\\arrow[l, \"g^*\"'] \\arrow[u, equal]")

add(274, "(4.2.10)",
    "g_*i*i_*g*(X) = X pour X ∈ H^•(Δ,Z_ℓ(-1))  (capital X three times)",
    r"g_*i^*i_*g^*(X) = X \ \text{pour} \ X \in",
    "misprint_in_print", "low", None,
    "The element of H(Δ) is written with capital X, the letter of the variety; elsewhere in 4.2 such elements are "
    "x, y ((4.2.3), (4.2.11), (4.2.12)). Probably the typist's reading of a handwritten x. The TeX keeps the printed "
    "capitals.",
    corrected=r"g_*i^*i_*g^*(x) = x \ \text{pour} \ x \in")

add(274, "Exposé XVIII throughout: degree superscript of H",
    "one printed symbol, a small raised dot (H^•), on all these pages",
    r"H^{\bullet} on pp. 271-273 (e.g. (4.2.1), (4.2.2), (4.2.4)); H^{\cdot} on p. 274 ((4.2.6)-(4.2.10)); "
    r"expose_XVIII_body.tex has 21 lines with H^{\bullet} and 23 with H^{\cdot}",
    "symbol", "medium", None,
    "Convention: the same printed dot has two TeX renderings within the exposé; one rule for the exposé is needed "
    "(cf. global issue 15 for SGA 7 I). Not changed page by page.")

# ---------------- page 275
add(275, "En vertu de EGA II 8.1.7, ...",
    "si J̃ est l'Idéal Δ̃ dans X̃",
    r"l'Idéal $\widetilde{\Delta}$ dans $\widetilde{X}$",
    "misprint_in_print", "high", None,
    "'de' is missing in the print (cf. 'l'Idéal de Δ dans X' a few lines below). The TeX keeps the printed "
    "reading.",
    corrected=r"l'Idéal de $\widetilde{\Delta}$ dans $\widetilde{X}$")

add(275, "display after 'cet isomorphisme transforme', tensor product",
    "⊗ with subscript O²_Δ (underlined O with exponent 2)",
    r"\otimes_{\underline{O}^2_\Delta}",
    "misprint_in_print", "medium", None,
    "The tensor product is over O_Δ (EGA II 4.1.4: O_{P(E⊗L)}(1) corresponds to O_{P(E)}(1) ⊗_{O_Δ} L); the "
    "exponent 2 is carried over from P(O²_Δ). The TeX keeps it.",
    corrected=r"\otimes_{\underline{O}_\Delta}")

add(275, "same display, last term",
    "O_{P1}(1) ⊗_K O_Δ(-1)  (capital K)",
    r"\otimes_K",
    "misprint_in_print", "low", None,
    "The base field of the exposé is k (3.1: 'sur un corps k algébriquement clos'); no K is defined in §§ 3-4. "
    "The TeX keeps the printed capital.",
    corrected=r"\otimes_k")

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")

# check every fix's old occurs exactly once on its page
bad = 0
for x in F:
    fx = x["fix"]
    if fx is None:
        continue
    t = (PAGES / f"page_{x['page']}.tex").read_text(encoding="utf-8")
    n = t.count(fx["old"])
    print(x["page"], x["kind"], "old count", n)
    if n != 1:
        bad += 1
    if "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]:
        print("touches marker!", x["where"])
        bad += 1
# check tex fields are substrings where they are literal snippets
for x in F:
    t = (PAGES / f"page_{x['page']}.tex").read_text(encoding="utf-8")
    if x["tex"] in t:
        print(x["page"], "tex snippet found:", x["tex"][:50])
    else:
        print(x["page"], "tex snippet NOT literal:", x["tex"][:60])
from collections import Counter
c = Counter((x["page"], x["kind"] == "misprint_in_print") for x in F)
for p in range(271, 276):
    print(p, f"{c[(p, False)]}/{c[(p, True)]}")
print("bad", bad, "total", len(F))
