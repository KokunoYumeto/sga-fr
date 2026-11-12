"""Build findings_396_400.json, check every old (exactly once on its page; edits applied in order; olds of the
p. 397/398 display still unique on p. 398 after the marker move)."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
SRC = RUN / "b396_400"
OUT = RUN / "findings_396_400.json"


def J(*parts):
    return "\n".join(parts)


F = []


def add(page, where, scan, tex, kind, conf, old=None, new=None, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


RNOTE = ("Every R of RΓ, RHom and Rp on pp. 396-400 is the plain typewriter R (foot serifs), not the sans-serif "
         "double-struck R of p. 391; \\RG = \\R\\Gamma, \\R and \\RHom give ℝ in s5.tex. Itemized (no blanket rule: "
         "the print has ℝ twice on pp. 391-392).")
OBNOTE = ("\\Ob prints 'ob' in s5.tex (the first \\providecommand, preamble line 101, \\operatorname{ob}, wins); "
          "the print has 'Ob'. As the applied fixes of pp. 372 and 376.")
STMT = ("Exposé X's statement environment sets the text upright with no underline markup; the print underlines the "
        "statement word group by word group (\\emph, as Propositions 3.8, 4.4 and 5.1 on pp. 381-390). Formulas, "
        "numbers and the punctuation between the groups are not underlined.")

# ---------------------------------------------------------------- p. 396
add(396, "heading of section 7", "7.   Formule d'Euler-Poincaré.  (underlined title ending with a full stop)",
    r"\subsection*{7. Formule d'Euler-Poincaré}", "punctuation", "high",
    r"\subsection*{7. Formule d'Euler-Poincaré}", r"\subsection*{7. Formule d'Euler-Poincaré.}",
    "The TeX drops the full stop that ends the underlined title.")
add(396, "Théorème 7.1, statement lines 1-3, up to 'η le point générique de C,'",
    "underlined: 'Soient' | 'une courbe algébrique connexe' | 'lisse et propre sur le corps' | 'algébriquement clos' | "
    "'le point générique de'; C, k, η and the commas not",
    "Soient $C$ une courbe algébrique connexe, ... le point générique de $C$, (statement environment, no underline)",
    "underline", "high",
    r"Soient $C$ une courbe algébrique connexe, lisse et propre sur le corps $k$ algébriquement clos, $\eta$ le point générique de $C$,",
    r"\emph{Soient} $C$ \emph{une courbe algébrique connexe}, \emph{lisse et propre sur le corps} $k$ \emph{algébriquement clos}, $\eta$ \emph{le point générique de} $C$,",
    STMT)
add(396, "Théorème 7.1, statement lines 3-6, from 'une sous-catégorie' to 'Sous ces conditions on a'",
    "underlined: 'une sous-catégorie triangulée de' | 'stable par facteurs directs' | 'un complexe de faisceaux de' | "
    "'-modules tel que les conditions' | 'de' (a short stroke under its d only) | 'soient remplies' | "
    "'Sous ces conditions on a'; Δ ⊂ D+(A), D+(A), F, A, 'i), ii)', 7.1 and the punctuation not",
    "une sous-catégorie triangulée de $D^+(A)$ ... Sous ces conditions on a (no underline)",
    "underline", "high",
    r"une sous-catégorie triangulée de $D^+(A)$ stable par facteurs directs, $F$ un complexe de faisceaux de $A$-modules tel que les conditions i), ii) de 7.1 soient remplies. Sous ces conditions on a",
    r"\emph{une sous-catégorie triangulée de} $D^+(A)$ \emph{stable par facteurs directs}, $F$ \emph{un complexe de faisceaux de} $A$-\emph{modules tel que les conditions} i), ii) \emph{de} 7.1 \emph{soient remplies}. \emph{Sous ces conditions on a}",
    "Statement underline, continued. The 'de' before 7.1 has only a short underline stroke under its d; read as "
    "underlined. The misprint 7.1 (next item) stays as printed in this edit.")
add(396, "Théorème 7.1, 'tel que les conditions i), ii) de 7.1 soient remplies'", "de 7.1 (the 7 is clear)",
    "les conditions i), ii) de 7.1 soient remplies (as printed)", "misprint_in_print", "high", None, None,
    "Wrong reference: conditions i) and ii) are those of 6.1 (pp. 393-394); 7.1 is this theorem. The TeX keeps the "
    "printed reading; the current layer already reads 6.1. After the underline edit above the diplomatic text reads "
    "'i), ii) \\emph{de} 7.1'.",
    corrected="les conditions i), ii) de 6.1")
add(396, "Théorème 7.1, 'Sous ces conditions on a RΓ_C(F) ∈ Ob(Δ)'", "R Γ_C(F): plain typewriter R",
    r"\RG_C(F)", "font", "high", r"\RG_C(F)", r"\mathrm{R}\Gamma_C(F)", RNOTE)
add(396, "same line, 'Ob(Δ)'", "Ob(Δ) with a capital O", r"\Ob(\Delta)", "word", "high",
    r"\Ob(\Delta)", r"\operatorname{Ob}(\Delta)", OBNOTE)
add(396, "Théorème 7.1, 'et la formule suivante (formule d'Euler-Poincaré) est vraie :'",
    "underlined: 'et la formule suivante' | 'formule d'Euler-Poincaré' | 'est' | 'vraie'; parentheses and colon not",
    "et la formule suivante (formule d'Euler-Poincaré) est vraie: (no underline)", "underline", "high",
    r"et la formule suivante (formule d'Euler-Poincaré) est vraie:",
    r"\emph{et la formule suivante} (\emph{formule d'Euler-Poincaré}) \emph{est vraie}:",
    "Statement underline, continued (the statement ends on p. 397).")

# ---------------------------------------------------------------- p. 397
add(397, "(7.2), left-hand side", "cℓ_{K(Δ)}(R Γ_C(F)): plain typewriter R", r"\clK{\Delta}(\RG_C(F))",
    "font", "high", r"\RG_C(F)", r"\mathrm{R}\Gamma_C(F)", RNOTE)
add(397, "EP on pp. 397 and 400 (convention, reported once): (7.2); three times in the big display of p. 400; EP_Δ(C,F) at the foot of p. 400",
    "EP double-struck every time (both letters with doubled stems)",
    r"\EP = \operatorname{EP} (roman): '\EP(C)\clK{\Delta}(F_{\bar\eta})' (p. 397), '\EP(C)\clKstar{\Lambda[G]}(\Lambda[G])', '+\EP(C)\clK{\Delta}F_{\bar\eta}', '\EP_\Delta(C,F)' (p. 400)",
    "font", "high", None, None,
    "Convention of Exposé X, not itemized, as filed for pp. 390-393 (findings_391_395): one decision for the exposé "
    "(for example \\EP as \\mathbb{E}\\mathbb{P} inside Exposé X).")
add(397, "end of Théorème 7.1, 'où les ε^Δ_x(F) sont définis dans 6.2 (formule 6.2.2).'",
    "underlined: 'où les' | 'sont définis dans' | 'formule'; ε^Δ_x(F), 6.2, 6.2.2 and the parentheses not",
    "où les $\\varepsilon_x^\\Delta(F)$ sont définis dans 6.2 (formule 6.2.2). (no underline)", "underline", "high",
    r"où les $\varepsilon_x^\Delta(F)$ sont définis dans 6.2 (formule 6.2.2).",
    r"\emph{où les} $\varepsilon_x^\Delta(F)$ \emph{sont définis dans} 6.2 (\emph{formule} 6.2.2).",
    "Last line of the underlined statement of Théorème 7.1 (" + STMT[:60] + "...).")
add(397, "a), 'un complexe borné à gauche de faisceaux de Λ[G]-modûles'", "modûles: a clear circumflex over the u",
    r"faisceaux de $\Lambda[G]$-modules", "misprint_in_print", "high",
    r"faisceaux de $\Lambda[G]$-modules", r"faisceaux de $\Lambda[G]$-modûles",
    "Typing error; the TeX silently corrects. The fix restores the printed reading (diplomatic layer only).",
    corrected=r"faisceaux de $\Lambda[G]$-modules")
add(397, "a), 'sur C . On a un isomorphisme :'", "On a un isomorphisme : (colon before (7.3))",
    "On a un isomorphisme, then the display", "punctuation", "high",
    r"$C$. On a un isomorphisme", r"$C$. On a un isomorphisme:",
    "The TeX drops the colon (the file writes the print's ' :' as ':').")
add(397, "(7.3)", "RΓ^G(RΓ_C (Ψ)) ≃ RΓ_C(R Γ̲^G (Ψ)) : all four R plain typewriter R",
    r"\R\Gamma^G(\RG_C(\Psi))\simeq\RG_C(\R\underline{\Gamma}^G(\Psi))", "font", "high",
    r"\R\Gamma^G(\RG_C(\Psi))\simeq\RG_C(\R\underline{\Gamma}^G(\Psi))",
    r"\mathrm{R}\Gamma^G(\mathrm{R}\Gamma_C(\Psi))\simeq\mathrm{R}\Gamma_C(\mathrm{R}\underline{\Gamma}^G(\Psi))",
    RNOTE)
add(397, "'où Γ̲^G est le foncteur : \"sous faisceau des sections G-invariantes\" .'",
    "straight typewriter double quotes", r"«sous-faisceau des sections $G$-invariantes»", "punctuation", "high",
    r"«sous-faisceau des sections $G$-invariantes»", r"``sous-faisceau des sections $G$-invariantes''",
    "Guillemets are not the print's form (the only guillemets of Exposé X); the file writes the print's quotes "
    "``...'' (p. 394 ``localement constant''). Apply before the next item.")
add(397, "same phrase, 'sous faisceau'", "sous faisceau: a space, no hyphen (p. 396 prints sous-catégorie)",
    "sous-faisceau", "misprint_in_print", "high",
    r"sous-faisceau des sections", r"sous faisceau des sections",
    "Missing hyphen; the TeX silently corrects. Its old occurs once both before and after the quote fix above "
    "(apply after it).",
    corrected=r"sous-faisceau des sections")
add(397, "'et Γ^G transforme un faisceau injectif de Λ[G]-modules dans un faisceau injectif de Λ-modules'",
    "Γ^G without the hand-drawn underline (blank paper under the Γ)", r"et $\underline{\Gamma}^G$ transforme",
    "misprint_in_print", "high",
    r"injectif et $\underline{\Gamma}^G$ transforme", r"injectif et $\Gamma^G$ transforme",
    "The functor meant is the sheaf of invariants Γ̲^G (sheaves to sheaves), underlined in its definition just "
    "above, in (7.3) and in the display below; the underline was not drawn here. The TeX silently corrects.",
    corrected=r"injectif et $\underline{\Gamma}^G$ transforme")
add(397, "'(utiliser pour cela par exemple des adj nts évidents de Γ_C et Γ^G )'",
    "Γ^G without underline", r"de $\Gamma_C$ et $\underline{\Gamma}^G$)", "misprint_in_print", "high",
    r"$\Gamma_C$ et $\underline{\Gamma}^G$)", r"$\Gamma_C$ et $\Gamma^G$)",
    "As the previous item (the adjoints of Γ_C and Γ̲^G); the TeX silently corrects. In 'adj  nts' the oi did not "
    "print (gap of two letters, physical): the TeX's 'adjoints' stands, not reported.",
    corrected=r"$\Gamma_C$ et $\underline{\Gamma}^G$)")
add(397, "b), 'nul en dehors de U . On a un isomorphisme :'", "colon before (7.4)",
    "On a un isomorphisme, then the display", "punctuation", "high",
    r"$U$. On a un isomorphisme", r"$U$. On a un isomorphisme:", "The TeX drops the colon.")
add(397, "(7.4), first member", "Φ ≃ R Γ̲^G(p_*(Φ')): plain typewriter R",
    r"\Phi\simeq \R\underline{\Gamma}^G(p_*(\Phi')),", "font", "high",
    r"\Phi\simeq \R\underline{\Gamma}^G(p_*(\Phi'))", r"\Phi\simeq \mathrm{R}\underline{\Gamma}^G(p_*(\Phi'))",
    RNOTE)
add(397, "(7.4), second part", ", où  Φ' = p*(Φ)  (no full stop)", r"\qquad \Phi'=p^*(\Phi).", "missing", "high",
    r"\qquad \Phi'=p^*(\Phi).", r"\qquad\text{où } \Phi'=p^*(\Phi)",
    "The TeX drops 'où' and adds a full stop at the end of the display (one edit).")
add(397, "last line of the printed page, 'On aura donc l'isomorphisme :'", "l'isomorphisme : (then blank paper)",
    "On aura donc l'isomorphisme", "punctuation", "high",
    r"On aura donc l'isomorphisme", r"On aura donc l'isomorphisme:", "The TeX drops the colon.")
add(397, "display Φ ⥲ R((Γ̲^G ∘ p_*) ∘ p^*)(Φ) (printed at the top of p. 398; in page_397.tex as the files stand)",
    "an arrow with a tilde above it (not ≃); plain typewriter R", r"\Phi\simeq \R\bigl((", "symbol", "high",
    r"\Phi\simeq \R\bigl((", r"\Phi\xrightarrow{\sim} \mathrm{R}\bigl((",
    "One edit: the arrow (\\xrightarrow{\\sim}, as the file's \\xleftarrow{\\sim} in (7.6)) and the plain R. "
    "Old stays unique on p. 398 after the folio-398 marker move.")
add(397, "end of the same display (printed at the top of p. 398)", "... ∘ p^*)(Φ) with no full stop",
    r"p^*\bigr)(\Phi).", "punctuation", "high", r"p^*\bigr)(\Phi).", r"p^*\bigr)(\Phi)",
    "The TeX adds a full stop at the end of the display. Old stays unique on p. 398 after the marker move.")

# ---------------------------------------------------------------- p. 398
add(398, "top of the page: the display Φ ⥲ R((Γ̲^G ∘ p_*) ∘ p^*)(Φ)",
    "p. 398 begins with this display, then 'D'autre part on peut appliquer de nouveau'; p. 397 ends with "
    "'On aura donc l'isomorphisme :' and blank paper",
    "the display ('\\[', '\\Phi\\simeq \\R\\bigl((...)(\\Phi).', '\\]') is the last three lines of page_397.tex; "
    "the folio-398 marker follows it", "marker", "high", None, None,
    "Page 398 really begins at that display's '\\[' (diplomatic s5.tex line 13482, current 13478; the marker stands "
    "at 13485 / 13481). Exact fix: python -I move_marker.py 5 398 \"$(printf '%s\\n%s' '\\[' '\\Phi')\" --before "
    "(simulated in memory on both layers: the marker lands on its own line between 'On aura donc l'isomorphisme' "
    "and '\\['; the anchor still matches after the p. 397 edits of that display). Text not moved; its differences "
    "are filed under p. 397.")
add(398, "first line, 'D'autre part on peut appliquer'", "D'autre part on peut (no comma)",
    "D'%\\nautre part, on peut", "punctuation", "high", r"autre part, on peut", r"autre part on peut",
    "The TeX adds a comma.")
add(398, "'([5] Prop 3.1)'", "Prop 3.1 (no full stop after Prop)", r"([5] Prop. 3.1)", "punctuation", "high",
    r"([5] Prop. 3.1)", r"([5] Prop 3.1)",
    "The TeX adds the abbreviation's full stop (p. 397 prints 'prop. 3.1' with it).")
add(398, "'compte tenu que Rp* = p* , Rp_* = p_* :'", "both R plain typewriter R (foot serifs)",
    r"$\R p^*=p^*$, $\R p_*=p_*$", "font", "high",
    r"$\R p^*=p^*$, $\R p_*=p_*$", r"$\mathrm{R} p^*=p^*$, $\mathrm{R} p_*=p_*$", RNOTE)
add(398, "display Φ ⥲ R(Γ̲^G ∘ p_*)(p*(Φ)) ≃ (RΓ̲^G)(p_* p*(Φ)) ,",
    "the first relation is an arrow with a tilde above it (as at the top of the page), the second ≃; both R plain",
    J(r"\Phi\simeq \R(\underline{\Gamma}^G\circ p_*)(p^*(\Phi))", r"\simeq (\R\underline{\Gamma}^G)(p_*p^*(\Phi)),"),
    "symbol", "high",
    J(r"\Phi\simeq \R(\underline{\Gamma}^G\circ p_*)(p^*(\Phi))", r"\simeq (\R\underline{\Gamma}^G)"),
    J(r"\Phi\xrightarrow{\sim} \mathrm{R}(\underline{\Gamma}^G\circ p_*)(p^*(\Phi))", r"\simeq (\mathrm{R}\underline{\Gamma}^G)"),
    "One edit: the arrow and the two plain R.")
add(398, "(7.5), the members",
    "R Γ_C(Φ) = (RΓ^G)(R Γ_{C'}(Φ')) : three plain R (the blotted subscripts read as C, C', as the TeX)",
    r"\RG_C(\Phi)=(\R\Gamma^G)(\RG_{C'}(\Phi')),", "font", "high",
    r"\RG_C(\Phi)=(\R\Gamma^G)(\RG_{C'}(\Phi'))",
    r"\mathrm{R}\Gamma_C(\Phi)=(\mathrm{R}\Gamma^G)(\mathrm{R}\Gamma_{C'}(\Phi'))", RNOTE)
add(398, "(7.5), second part", ",   où   Φ' = p*(Φ)   .", r"\qquad \Phi'=p^*(\Phi).", "missing", "high",
    r"\qquad \Phi'=p^*(\Phi)", r"\qquad\text{où } \Phi'=p^*(\Phi)", "The TeX drops 'où' (as in (7.4)).")
add(398, "display after 'En effet on a :'",
    "(RΓ^G)(RΓ_{C'}(Φ')) ≃ (RΓ^G)(RΓ_C(p_*(Φ'))) ≃ RΓ_C(RΓ̲^G(p_*(Φ'))) : all six R plain",
    r"(\R\Gamma^G)(\RG_{C'}(\Phi')) ... \RG_C(\R\underline{\Gamma}^G(p_*(\Phi')))", "font", "high",
    J(r"(\R\Gamma^G)(\RG_{C'}(\Phi'))", r"\simeq", r"(\R\Gamma^G)(\RG_C(p_*(\Phi')))", r"\simeq",
      r"\RG_C(\R\underline{\Gamma}^G(p_*(\Phi')))"),
    J(r"(\mathrm{R}\Gamma^G)(\mathrm{R}\Gamma_{C'}(\Phi'))", r"\simeq", r"(\mathrm{R}\Gamma^G)(\mathrm{R}\Gamma_C(p_*(\Phi')))",
      r"\simeq", r"\mathrm{R}\Gamma_C(\mathrm{R}\underline{\Gamma}^G(p_*(\Phi')))"), RNOTE)
add(398, "d), 'les inclusions canoniques et posons :'", "posons : (colon before the display)", "et posons",
    "punctuation", "high", r"canoniques et posons", r"canoniques et posons:", "The TeX drops the colon.")
add(398, "'Pour calculèr RΓ_C(Φ)'", "calculèr: a grave accent on the e", "Pour calculer", "misprint_in_print",
    "high", r"Pour calculer", r"Pour calculèr", "Typing error; the TeX silently corrects.",
    corrected=r"Pour calculer")
add(398, "same line, RΓ_C(Φ)", "plain R", r"$\RG_C(\Phi)$", "font", "high",
    r"$\RG_C(\Phi)$", r"$\mathrm{R}\Gamma_C(\Phi)$", RNOTE)
add(398, "'avec les notations de 7.1 , Φ ≃ Λ_{U',C'} ⊗_Λ M'",
    "Φ without a prime (the primes of Φ' elsewhere on the page are clear ticks)", r"\Phi'\simeq \Lambda_{U',C'}",
    "misprint_in_print", "high", r"\Phi'\simeq \Lambda_{U',C'}", r"\Phi\simeq \Lambda_{U',C'}",
    "The sheaf on C' is Φ' = p*(Φ) (Φ = i_!(F|U) lives on C); the TeX silently corrects. Adjacent to, not "
    "overlapping, the next item.",
    corrected=r"\Phi'\simeq \Lambda_{U',C'}")
add(398, "same formula, the tensor product and what follows",
    "⊗_Λ M   et la formule : a plain ⊗ (no L above it) and no comma",
    "\\otimes_\\Lambda^L M, (then \\] and 'et la formule')", "extra", "high",
    J(r"\otimes_\Lambda^L M,", r"\]"), J(r"\otimes_\Lambda M", r"\]"),
    "The TeX adds the derived-tensor L (the print has the ordinary tensor product here; Λ_{U',C'} is flat over Λ) "
    "and a comma (one edit). The display for the print's run-in formula is layout, not reported.")
add(398, "'la formule de Kunneth (SGA 4 XVII)'",
    "Kunneth: no diaeresis on the u (clean paper above it; p. 393 prints Künneth with it)", "Künneth",
    "misprint_in_print", "medium", r"Künneth", r"Kunneth",
    "Typing slip (the typewriter has the diaeresis, p. 393); the TeX silently corrects.", corrected=r"Künneth")
add(398, "'nous donnent' (the verb)",
    "nous donnent (plural: the subject is 'Φ ≃ Λ_{U',C'} ⊗_Λ M et la formule de Kunneth')", "nous donne",
    "word", "high", r"XVII) nous donne", r"XVII) nous donnent",
    "The TeX's singular follows its display of the first subject; the print's plural is grammatical.")
add(398, "(7.6), first two RΓ", "RΓ_{C'}(Φ') ≃ RΓ_{C'}(Λ_{U',C'} ... : plain R",
    J(r"\RG_{C'}(\Phi')", r"\simeq", r"\RG_{C'}(\Lambda"), "font", "high",
    J(r"\RG_{C'}(\Phi')", r"\simeq", r"\RG_{C'}(\Lambda"),
    J(r"\mathrm{R}\Gamma_{C'}(\Phi')", r"\simeq", r"\mathrm{R}\Gamma_{C'}(\Lambda"), RNOTE)
add(398, "(7.6), first derived tensor", "a double-struck L (doubled stem) above ⊗, Λ below", r"\otimes_\Lambda^L M)",
    "font", "high", r"\otimes_\Lambda^L M)", r"\otimes_\Lambda^{\mathbb{L}} M)",
    "As p. 391 (findings_391_395): outside Exposé III the print's double-struck L is \\mathbb{L}.")
add(398, "(7.6), third RΓ", "plain R (the prime of C' blotted)", J(r"\xleftarrow{\sim}", r"\RG_{C'}"), "font",
    "high", J(r"\xleftarrow{\sim}", r"\RG_{C'}"), J(r"\xleftarrow{\sim}", r"\mathrm{R}\Gamma_{C'}"), RNOTE)
add(398, "(7.6), second derived tensor", "double-struck L above ⊗", r"\otimes_\Lambda^L M.", "font", "high",
    r"\otimes_\Lambda^L M.", r"\otimes_\Lambda^{\mathbb{L}} M.", "As the first derived tensor of (7.6).")

# ---------------------------------------------------------------- p. 399
add(399, "line 1, 'entre les objets de D(A[G])'", "'objets de' underlined (a ragged line under both words)",
    "les objets de $D(A[G])$ (no underline)", "underline", "medium",
    r"les objets de $D(A[G])$", r"les \emph{objets de} $D(A[G])$",
    "Emphasis in the running text (the isomorphism holds between objects of D(A[G])). The line is rougher than "
    "the typed underlines of p. 396 but stands in the print.")
add(399, "'qui est appliquable grâce à 2.1'", "appliquable", "applicable", "misprint_in_print", "high",
    r"qui est applicable", r"qui est appliquable",
    "Non-standard spelling of the print; the TeX silently corrects.", corrected=r"qui est applicable")
add(399, "'on obtient :'", "colon before (7.7)", "2.1, on obtient", "punctuation", "high",
    r"2.1, on obtient", r"2.1, on obtient:", "The TeX drops the colon.")
add(399, "(7.7), first and second members", "RΓ_C(F_{U,C}) ≃ RΓ^G(RΓ_{C'}(... : three plain R",
    J(r"\RG_C(F_{U,C})", r"\simeq", r"\R\Gamma^G\bigl(\RG_{C'}"), "font", "high",
    J(r"\RG_C(F_{U,C})", r"\simeq", r"\R\Gamma^G\bigl(\RG_{C'}"),
    J(r"\mathrm{R}\Gamma_C(F_{U,C})", r"\simeq", r"\mathrm{R}\Gamma^G\bigl(\mathrm{R}\Gamma_{C'}"), RNOTE)
add(399, "(7.7), the derived tensor", "double-struck L above ⊗", r"\otimes_\Lambda^L M\bigr)", "font", "high",
    r"\otimes_\Lambda^L M\bigr)", r"\otimes_\Lambda^{\mathbb{L}} M\bigr)", "As (7.6) on p. 398.")
add(399, "(7.7), third member", "R Hom_{Λ[G]}(RΓ_{C'}(Λ_{U',C'})^∨, M) : both R plain",
    r"\RHom_{\Lambda[G]}\bigl(\RG_{C'}", "font", "high",
    r"\RHom_{\Lambda[G]}\bigl(\RG_{C'}", r"\mathrm{R}\Hom_{\Lambda[G]}\bigl(\mathrm{R}\Gamma_{C'}",
    "\\RHom is \\RHomCore = \\mathbb{R}\\mathrm{Hom} (preamble line 64). " + RNOTE)
add(399, "'Donc compte tenu de M ≃ F_η̄ ∈ Ob(Δ)'", "Ob(Δ) with a capital O", r"F_{\bar\eta}\in\Ob(\Delta)", "word",
    "high", r"F_{\bar\eta}\in\Ob(\Delta)", r"F_{\bar\eta}\in\operatorname{Ob}(\Delta)", OBNOTE)
add(399, "'et de (3.6), on trouve :'", "colon before the display", "on trouve", "punctuation", "high",
    r"et de (3.6), on trouve", r"et de (3.6), on trouve:", "The TeX drops the colon.")
add(399, "display RΓ_C(F_{U,C}) ∈ Ob(Δ) .", "plain R", r"\RG_C(F_{U,C})\in", "font", "high",
    r"\RG_C(F_{U,C})\in", r"\mathrm{R}\Gamma_C(F_{U,C})\in", RNOTE)
add(399, "same display, Ob(Δ)", "capital O", r"\Ob(\Delta).", "word", "high",
    r"\Ob(\Delta).", r"\operatorname{Ob}(\Delta).", OBNOTE)
add(399, "'D'autre part on a le triangle distingué'",
    "an indented new paragraph (the line starts about 115 px right of the margin of 'trouve :' and 'où évidement')",
    "runs on after the display (\\] then 'D'autre part' with no blank line)", "other", "medium",
    J(r"\]", r"D'autre part on a le triangle"), J(r"\]", "", r"D'autre part on a le triangle"), "Paragraph break.")
add(399, "'(où Y = C - U) :'", "colon before the diagram", r"(où $Y=C-U$)", "punctuation", "high",
    r"(où $Y=C-U$)", r"(où $Y=C-U$):", "The TeX drops the colon.")
add(399, "triangle (7.8), the three vertices", "RΓ_Y(F|Y), RΓ_C(F_{U,C}), RΓ_C(F): plain R",
    r"& \RG_Y(F|Y) ... \RG_C(F_{U,C}) ... \RG_C(F)", "font", "high",
    J(r"& \RG_Y(F|Y) \arrow[dl] & \\", r"\RG_C(F_{U,C}) \arrow[rr] && \RG_C(F)"),
    J(r"& \mathrm{R}\Gamma_Y(F|Y) \arrow[dl] & \\", r"\mathrm{R}\Gamma_C(F_{U,C}) \arrow[rr] && \mathrm{R}\Gamma_C(F)"),
    RNOTE + " The arrows agree with the print.")
add(399, "end of the triangle (7.8)", "RΓ_C(F)    , : a comma after the bottom right vertex", "no comma",
    "punctuation", "high", r" \arrow[ul]", r", \arrow[ul]",
    "The TeX drops the comma (set in the node, as the full stop of the triangle on p. 392). Adjacent to, not "
    "overlapping, the R edit.")
add(399, "'où évidement RΓ_Y(F) = ...'", "évidement (one m)", "où évidemment", "misprint_in_print", "high",
    r"où évidemment", r"où évidement", "Typing error; the TeX silently corrects.", corrected=r"où évidemment")
add(399, "'RΓ_Y(F) = ∐_{y∈Y} F_y'", "plain R", r"\RG_Y(F)=", "font", "high",
    r"\RG_Y(F)=", r"\mathrm{R}\Gamma_Y(F)=", RNOTE)
add(399, "same, '∈ Ob(Δ),'", "capital O", r"\Ob(\Delta),", "word", "high",
    r"\Ob(\Delta),", r"\operatorname{Ob}(\Delta),", OBNOTE)
add(399, "'car F_y ∈ Ob(Δ) (condition (i))'", "capital O", r"car $F_y\in\Ob(\Delta)$", "word", "high",
    r"car $F_y\in\Ob(\Delta)$", r"car $F_y\in\operatorname{Ob}(\Delta)$", OBNOTE)
add(399, "'Il en résulte donc que RΓ_C(F) ∈ Ob(Δ)'", "plain R", r"que $\RG_C(F)\in", "font", "high",
    r"que $\RG_C(F)\in", r"que $\mathrm{R}\Gamma_C(F)\in", RNOTE)
add(399, "same, 'Ob(Δ) ,'", "capital O", r"\Ob(\Delta)$, c'est", "word", "high",
    r"\Ob(\Delta)$, c'est", r"\operatorname{Ob}(\Delta)$, c'est", OBNOTE)
add(399, "'nous donne de plus la relation :'", "colon before the display", "de plus la relation", "punctuation",
    "high", r"de plus la relation", r"de plus la relation:", "The TeX drops the colon.")
add(399, "first relation, the two RΓ", "cℓ(RΓ_C(F)) = cℓ(R Γ_C(F_{U,C})) : plain R",
    J(r"\clK{\Delta}(\RG_C(F))", "=", r"\clK{\Delta}(\RG_C(F_{U,C}))"), "font", "high",
    J(r"\clK{\Delta}(\RG_C(F))", "=", r"\clK{\Delta}(\RG_C(F_{U,C}))"),
    J(r"\clK{\Delta}(\mathrm{R}\Gamma_C(F))", "=", r"\clK{\Delta}(\mathrm{R}\Gamma_C(F_{U,C}))"), RNOTE)
add(399, "first relation, the summand", "cℓ_{K(Δ)}(F_ȳ): a bar over the y (as over η in F_η̄)",
    r"\clK{\Delta}(F_y),", "formula", "high", r"\clK{\Delta}(F_y),", r"\clK{\Delta}(F_{\bar y}),",
    "The stalk at the geometric point ȳ; the TeX drops the bar (also in the second relation and three times on "
    "p. 400). The F_y of '∐ F_y ∈ Ob(Δ), car F_y ∈ Ob(Δ)' have no bar in the print, as in the TeX.")
add(399, "second relation, RΓ and R Hom", "cℓ(RΓ_C(F)) = cℓ(R Hom_{Λ[G]}(RΓ_{C'}(... : plain R",
    J(r"\clK{\Delta}(\RG_C(F))", "=", r"\clK{\Delta}\bigl(\RHom_{\Lambda[G]}(\RG_{C'}"), "font", "high",
    J(r"\clK{\Delta}(\RG_C(F))", "=", r"\clK{\Delta}\bigl(\RHom_{\Lambda[G]}(\RG_{C'}"),
    J(r"\clK{\Delta}(\mathrm{R}\Gamma_C(F))", "=", r"\clK{\Delta}\bigl(\mathrm{R}\Hom_{\Lambda[G]}(\mathrm{R}\Gamma_{C'}"),
    RNOTE)
add(399, "second relation, the summand", "cℓ_{K(Δ)}(F_ȳ) .", r"\clK{\Delta}(F_y).", "formula", "high",
    r"\clK{\Delta}(F_y).", r"\clK{\Delta}(F_{\bar y}).", "As the first relation.")

# ---------------------------------------------------------------- p. 400
add(400, "first line, 'Pour obtenir la formule d'Euler-Poincaré'",
    "an indented new paragraph (p. 399 ends with a display)",
    "follows the marker after the closing \\] of p. 399 with no blank line", "other", "medium",
    r"Pour obtenir la formule d'Euler-Poincaré", "\n" + r"Pour obtenir la formule d'Euler-Poincaré",
    "Paragraph break; the edit puts a blank line after the marker line (the marker itself unchanged).")
add(400, "first display, both RΓ", "cℓ(RΓ_{C'}(Λ_{U',C'})) = cℓ(RΓ_{C'}(... : plain R",
    J(r"\clKstar{\Lambda[G]}\bigl(\RG_{C'}(\Lambda_{U',C'})\bigr)", "=", r"\clKstar{\Lambda[G]}\bigl(\RG_{C'}"),
    "font", "high",
    J(r"\clKstar{\Lambda[G]}\bigl(\RG_{C'}(\Lambda_{U',C'})\bigr)", "=", r"\clKstar{\Lambda[G]}\bigl(\RG_{C'}"),
    J(r"\clKstar{\Lambda[G]}\bigl(\mathrm{R}\Gamma_{C'}(\Lambda_{U',C'})\bigr)", "=",
      r"\clKstar{\Lambda[G]}\bigl(\mathrm{R}\Gamma_{C'}"), RNOTE)
add(400, "first display, right-hand side",
    "cℓ_{K•(Λ[G])}(RΓ_{C'}(Λ_{U',C'})^∨   . : the parenthesis opened after cℓ is not closed",
    r"(\Lambda_{U',C'})^\vee\bigr).", "misprint_in_print", "high", r"^\vee\bigr).", r"^\vee.",
    "The TeX silently closes it (\\bigl( needs no partner). The Λ of this Λ_{U',C'} is broken in the scan "
    "(physical).", corrected=r"^\vee\bigr).")
add(400, "big display, first line, RΓ_C(F) and RΓ_{C'}", "plain R",
    J(r"\clK{\Delta}(\RG_C(F))", r"&=\operatorname{hom}\Bigl(", r"\clKstar{\Lambda[G]}\bigl(\RG_{C'}"), "font", "high",
    J(r"\clK{\Delta}(\RG_C(F))", r"&=\operatorname{hom}\Bigl(", r"\clKstar{\Lambda[G]}\bigl(\RG_{C'}"),
    J(r"\clK{\Delta}(\mathrm{R}\Gamma_C(F))", r"&=\operatorname{hom}\Bigl(", r"\clKstar{\Lambda[G]}\bigl(\mathrm{R}\Gamma_{C'}"),
    RNOTE)
add(400, "big display, first line, index of the second class map",
    "cℓ_{K(D(A[G]_Δ)}(F_η̄)) : no parenthesis after ] (the same index on the third line reads K(D(A[G])_Δ))",
    r"\cl_{K(D(A[G])_\Delta)}(F_{\bar\eta})\Bigr)", "misprint_in_print", "high",
    J(r"A[G])_\Delta)}(F_{\bar\eta})\Bigr)", ""), J(r"A[G]_\Delta)}(F_{\bar\eta})\Bigr)", ""),
    "The TeX silently corrects.", corrected=J(r"A[G])_\Delta)}(F_{\bar\eta})\Bigr)", ""))
add(400, "big display, first line, last summand", "cℓ_{K(Δ)}(F_ȳ) (bar over y)",
    r" +\sum_{y\in Y}\clK{\Delta}(F_y)\\", "formula", "high",
    r" +\sum_{y\in Y}\clK{\Delta}(F_y)", r" +\sum_{y\in Y}\clK{\Delta}(F_{\bar y})", "As on p. 399.")
add(400, "big display, second line, first summand", "cℓ_{K(Δ)}(F_ȳ)",
    r"&=\sum_{y\in Y}\clK{\Delta}(F_y)\\", "formula", "high",
    J(r"&=\sum_{y\in Y}\clK{\Delta}(F_y)\\", r"&\quad"), J(r"&=\sum_{y\in Y}\clK{\Delta}(F_{\bar y})\\", r"&\quad"),
    "As on p. 399.")
add(400, "big display, second line, 'hom(EP(C) cℓ_{K•(Λ[G]}(Λ[G] - Σ'",
    "K•(Λ[G] : the parenthesis of the index is not closed", r"\EP(C)\clKstar{\Lambda[G]}", "misprint_in_print",
    "high", r"\EP(C)\clKstar{\Lambda[G]}", r"\EP(C)\operatorname{cl}_{K^{\bullet}(\Lambda[G]}",
    "\\clKstar{#1} is \\operatorname{cl}_{K^{\\bullet}(#1)}; the TeX silently closes the parenthesis. Adjacent "
    "to, not overlapping, the next item.", corrected=r"\EP(C)\clKstar{\Lambda[G]}")
add(400, "same, the argument '(Λ[G] - Σ'",
    "(Λ[G] - Σ_{y∈Y}(Sw^Λ_y + ... : the argument's parenthesis is not closed before the minus sign",
    "(\\Lambda[G])\\n -\\sum", "misprint_in_print", "high",
    J(r"(\Lambda[G])", r" -\sum"), J(r"(\Lambda[G]", r" -\sum"), "The TeX silently closes it.",
    corrected=J(r"(\Lambda[G])", r" -\sum"))
add(400, "big display, fourth line, first summand", "cℓ_{K(Δ)}(F_ȳ)", r"&=\sum_{y\in Y}\clK{\Delta}(F_y)",
    "formula", "high", J(r"&=\sum_{y\in Y}\clK{\Delta}(F_y)", r" +\EP(C)"),
    J(r"&=\sum_{y\in Y}\clK{\Delta}(F_{\bar y})", r" +\EP(C)"), "As on p. 399.")
add(400, "big display, last line", "Σ_{y∈Y} ε^Δ_x(F) : index x under a sum over y", r"\varepsilon_y^\Delta(F).",
    "misprint_in_print", "high", r"\varepsilon_y^\Delta(F).", r"\varepsilon_x^\Delta(F).",
    "The TeX silently corrects.", corrected=r"\varepsilon_y^\Delta(F).")
add(400, "'Compte tenu que ε^Δ_x(F) = 0 pour x ∈ 𝒰'", "an indented new paragraph after the display",
    "\\] then 'Compte tenu que' with no blank line", "other", "medium",
    J(r"\]", r"Compte tenu que"), J(r"\]", "", r"Compte tenu que"), "Paragraph break.")
add(400, "'Pour un complexe de faisceaux F , satisfaisant'",
    "an indented new paragraph after the short line 'formule (7.2) .'", "runs on: '(7.2). Pour un complexe'",
    "other", "medium", r"(7.2). Pour un complexe", J(r"(7.2).", "", r"Pour un complexe"), "Paragraph break.")
add(400, "last display, EP_Δ(C,F) = cℓ_{K(Δ)}(RΓ_C(F))", "plain R", r"\clK{\Delta}(\RG_C(F)).", "font", "high",
    r"\clK{\Delta}(\RG_C(F)).", r"\clK{\Delta}(\mathrm{R}\Gamma_C(F)).", RNOTE)

# ---------------------------------------------------------------- checks
ok = True
pages = {p: (SRC / f"page_{p}.tex").read_text(encoding="utf-8") for p in range(396, 401)}
for i, d in enumerate(F):
    if d["fix"] is None:
        continue
    o = d["fix"]["old"]
    n = pages[d["page"]].count(o)
    if n != 1:
        ok = False
        print("NOT UNIQUE", n, d["page"], repr(o[:70]))
    if "%%%%%%%%%%" in o or "%%%%%%%%%%" in d["fix"]["new"]:
        ok = False
        print("MARKER IN FIX", d["page"])
# apply in order on each page
for p in range(396, 401):
    t = pages[p]
    for d in F:
        if d["page"] != p or d["fix"] is None:
            continue
        o, nw = d["fix"]["old"], d["fix"]["new"]
        if t.count(o) != 1:
            ok = False
            print("SEQUENTIAL FAIL", p, repr(o[:70]))
            continue
        t = t.replace(o, nw)
    # corrected edition: skip misprint fixes
    t2 = pages[p]
    for d in F:
        if d["page"] != p or d["fix"] is None or d["kind"] == "misprint_in_print":
            continue
        o, nw = d["fix"]["old"], d["fix"]["new"]
        if t2.count(o) != 1:
            ok = False
            print("CORRECTED-LAYER FAIL", p, repr(o[:70]))
            continue
        t2 = t2.replace(o, nw)
# olds after the folio-398 marker move: the last display of page_397 goes to page 398
p397 = pages[397]
k = p397.rfind("\\[\n\\Phi")
moved = p397[k:]
new397 = p397[:k]
new398 = pages[398].replace("%%%%%%%%%%  scan idx 409  |  folio 398  %%%%%%%%%%\n",
                            "%%%%%%%%%%  scan idx 409  |  folio 398  %%%%%%%%%%\n" + moved, 1)
for d in F:
    if d["fix"] is None or d["page"] not in (397, 398):
        continue
    o = d["fix"]["old"]
    target = new398 if (d["page"] == 398 or p397.find(o) >= k) else new397
    if target.count(o) != 1:
        ok = False
        print("AFTER MOVE", d["page"], target.count(o), repr(o[:60]))
print("checks ok" if ok else "CHECKS FAILED")
cnt = {}
for d in F:
    a = cnt.setdefault(d["page"], [0, 0])
    a[1 if d["kind"] == "misprint_in_print" else 0] += 1
print(cnt, len(F))
if ok:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    print("wrote", OUT)
