import json, pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")
B = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\b171_175")
OUT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\findings_171_175.json")

F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 171
add(171, "first line of the page (marker)",
    "cohérent définissant S - U. D'après (iii'), il existe ...",
    "définissant $S-U$. D'après (iii$'$), il existe ...",
    "marker", "high", None,
    "Page 171 really begins with 'cohérent': p. 170 ends '... F un Idéal quasi-' and p. 171 begins 'cohérent définissant S - U.' "
    "(both scans, OCR of pp. 170/171), so 'quasi-cohérent' is divided at the page break and 'quasi-' belongs to p. 170. "
    "Two commands, in this order: python -I move_marker.py 6 171 \"quasi-coh\" --before, then "
    "python -I marker_split_word.py 6 171 split \"quasi-\" \"coh\" (simulated in memory on both layers: "
    "'... $F$ un Idéal ' / 'quasi-%' / the marker / 'cohérent' / 'définissant $S-U$.'; the % keeps 'quasi-cohérent' one word). "
    "Apply once: the checker of p. 170 may report the same break.")
add(171, "Preuve of 2.2.6, sentence before the diagram",
    "on obtient un diagramme cartésien :",
    "on obtient un diagramme cartésien",
    "punctuation", "high",
    {"old": "un diagramme cartésien", "new": "un diagramme cartésien :"},
    "The print ends the sentence with ' :' before the diagram (both scans).")
add(171, "footnote to 'famille ample' (Définition 2.2.4)",
    "M. BORELLI et S.L. KLEIMAN",
    r"M.~\textsc{Borelli} et S.~L.~\textsc{Kleiman}",
    "font", "medium",
    {"old": r"\textsc{Borelli} et S.~L.~\textsc{Kleiman}", "new": r"BORELLI et S.~L.~KLEIMAN"},
    "The typescript types both names in capitals (both scans); \\textsc prints them in small capitals. The file keeps typed "
    "capitals elsewhere (par A. GROTHENDIECK) and has \\textsc only here and once more (\\textsc{Berthelot}).")
add(171, "Preuve of 2.2.6, after the diagram",
    "où Y' = X' - U.",
    "où $Y'=X'-U$.",
    "misprint_in_print", "low", None,
    "The TeX keeps the printed reading (both scans: U without prime). Y' = Y x_X X' is the complement of U' = U x_X X' in X'; "
    "the corrected layer already reads X'-U'. Low: X' - U may be meant loosely as the complement of the inverse image of U.",
    corrected="$Y'=X'-U'$")
add(171, "statements of Définition 2.2.4, Définition 2.2.5, Lemme 2.2.6 (the same on pp. 172-175)",
    "statement text underlined word group by word group; symbols, references and the defined terms 'famille ample', "
    "'divisoriel' left plain",
    r"statements in plain text, with \emph{famille ample} and \emph{divisoriel}",
    "underline", "high", None,
    "Convention of this exposé, for one decision, not itemized: the typescript underlines every statement (Déf. 2.2.4, 2.2.5, "
    "Lemme 2.2.6 on p. 171; Prop. 2.2.7, Cor. 2.2.7.1 on p. 172; Lemme 2.2.8 on pp. 173-174; Prop. 2.2.9 on pp. 174-175) "
    "word group by word group; the TeX sets all of them without underline and puts \\emph (the file's underline command) on "
    "exactly the words the print leaves plain inside the statement (\\emph{famille ample}, \\emph{divisoriel}), the inverse "
    "of the print. Not the pending 'one block' form (SGA 7 II items 48/73): here there is no underline at all. Following the "
    "print, Définition 2.2.5 would read: \\emph{On dit qu'un schéma} $S$ \\emph{est} divisoriel \\emph{si} $S$ \\emph{est "
    "quasi-compact et quasi-séparé et s'il existe une famille ample} (2.2.4) \\emph{de} $\\mathcal O_S$\\emph{-Modules inversibles}.")

# ---------------- page 172
add(172, "label of the proof of 2.2.7",
    "Preuve de 2.2.7. (only 'Preuve' underlined)",
    r"\emph{Preuve de 2.2.7.}",
    "underline", "high",
    {"old": r"\emph{Preuve de 2.2.7.}", "new": r"\emph{Preuve} de 2.2.7."},
    "The underline stops after 'Preuve' (both scans); 'de 2.2.7.' is plain.")
add(172, "after the statement of Proposition 2.2.7",
    "'En particulier (EGA IV 21.11.1) :' on its own indented line after '... est divisoriel (2.2.5).'",
    "... divisoriel (2.2.5). En particulier (EGA IV 21.11.1) : (run on in the proposition's paragraph)",
    "other", "medium",
    {"old": "divisoriel (2.2.5). En particulier", "new": "divisoriel (2.2.5).\n\nEn particulier"},
    "The print ends the statement at '(2.2.5).' and starts a new indented paragraph 'En particulier (EGA IV 21.11.1) :' "
    "that leads to Corollaire 2.2.7.1 (both scans); in the TeX it reads as part of the proposition.")

# ---------------- page 173
add(173, "Lemme 2.2.8 and after (pp. 173-175): the category L(S)",
    "underlined typed L in L(S), L(U) and L alone (the sheaves L_i are not underlined)",
    r"plain L: $L(S)$, $L(U)$, $L$, $\mathcal C_0=L$",
    "underline", "high", None,
    "Convention for one decision, not itemized: every L that names the category generated by the L_i^{-n} is an underlined "
    "typed L in the print, the TeX writes a plain L. 22 places on pp. 173-175: p. 173 'Notons $L(S)$', 'Les catégories $L(S)$', "
    "both members of \\mathrm K^{-}(L(S))/\\mathrm K^{-,\\varnothing}(L(S)), 'relativement à $L(S)$', '$F^i\\in\\Ob L(S)$'; "
    "p. 174 '$E\\in\\Ob L(S)$', '$\\Loclib(S)$ ou $L(S)$', '(resp. $L(U)$)', 'et $L(U)$', 'objet de $L$', "
    "'relativement à $L$ (I 2.14)', 'relative à $L(S)$', 'dans $L$ si', 'la catégorie $L$ est', '$\\mathcal C_0=L$', "
    "both members of the display of 2.2.9 a); p. 175 both members of the display of 2.2.9 a), '$F^i\\in\\Ob L(S))$', "
    "'$L(S)=\\Lib(S)$'. Following the print: \\underline{L}.")

# ---------------- page 174
add(174, "Proposition 2.2.9 a)",
    "a) Les foncteur canoniques",
    r"\item Les foncteur canoniques",
    "misprint_in_print", "high", None,
    "The TeX keeps the printed singular (both scans); the corrected layer already has 'foncteurs'.",
    corrected="Les foncteurs canoniques")
add(174, "proof of 2.2.8, last sentence but one",
    "Par suite, les assertions c)) résultent de (1.2)",
    "Par suite, les assertions c)) résultent de (1.2)",
    "misprint_in_print", "medium", None,
    "Doubled closing parenthesis in the print (both scans), kept by the TeX.",
    corrected="les assertions c) résultent")
add(174, "proof of 2.2.8, last sentence",
    "Ceci achève la démonstration (no full stop)",
    "Ceci achève la démonstration",
    "misprint_in_print", "medium", None,
    "The print has no full stop after 'démonstration' (both scans; the same sentence on p. 172 has one); the TeX keeps "
    "the printed reading.",
    corrected="Ceci achève la démonstration.")

# ---------------- page 175
add(175, "Preuve of 2.2.9, first line",
    "Compte tenu de (3.5) et (3.7) (1), c'est un corollaire immédiat",
    "Compte tenu de (3.5) et (3.7), c'est un corollaire immédiat",
    "missing", "high",
    {"old": "(3.7), c'est un corollaire", "new": r"(3.7)\footnotemark[\value{footnote}], c'est un corollaire"},
    "The print calls footnote (1) ('Le § 3 est indépendant du reste de l'exposé.') a second time here (both scans); the TeX "
    "has only the first call, in 2.2.9 a). \\footnotemark[\\value{footnote}] repeats the last footnote's number, as the file "
    "does at main.tex lines 692 and 3049.")
add(175, "Remarque 2.2.10 a)",
    "le foncteur RΓ_S : D^+(S) -> D^+(A), the R double-underlined",
    r"$R\Gamma_S:\mathrm D^+(S)",
    "font", "high",
    {"old": r"$R\Gamma_S:", "new": r"$\mathbb R\Gamma_S:"},
    "The derived-functor R is double-underlined (double-struck) in both scans, the TeX has a plain R; the file writes the "
    "print's double-struck letters with \\mathbb (\\mathbb E, \\mathbb N, \\mathbb Z).")
add(175, "Proposition 2.2.9 b)",
    "F^i ∈ ob L(S)) pour i > m",
    r"$F^i\in\Ob L(S))$ pour $i>m$",
    "misprint_in_print", "medium", None,
    "Extra closing parenthesis in the print (both scans), kept by the TeX (inside the math).",
    corrected=r"$F^i\in\Ob L(S)$")
add(175, "end of the page (marker of p. 176)",
    "... dont l'image essentielle est | footnote (1) | p. 176 begins 'la sous-catégorie triangulée'",
    "... dont l'image essentielle est la",
    "marker", "high", None,
    "Page 175 ends with 'est'; the last word of its TeX, 'la', is the first word of p. 176 (both scans; OCR of p. 176). "
    "Move the folio-176 marker before it: python -I move_marker.py 6 176 \"la\" --before (simulated in memory on both layers: "
    "'... dont l'image essentielle est ' / the marker / 'la' / 'sous-catégorie triangulée'). Apply once: the checker of p. 176 "
    "will see the same break, and a second run would move the marker to an earlier 'la'.")

# ---------------- checks
bad = 0
for d in F:
    t = (B / f"page_{d['page']}.tex").read_text(encoding="utf-8")
    if d["fix"] is not None:
        n = t.count(d["fix"]["old"])
        mk = "%%%%%%%%%%" in d["fix"]["old"]
        print(d["page"], d["kind"], "old count =", n, "MARKER!" if mk else "")
        if n != 1 or mk:
            bad += 1
    elif d["kind"] == "misprint_in_print":
        # the TeX keeps the printed reading: check the quoted TeX text is on the page
        probe = d["tex"].replace(r"\item ", "")
        print(d["page"], "misprint kept, printed reading in TeX:", probe in t or probe.split(" (")[0] in t)
print("bad:", bad, "findings:", len(F))
if bad == 0:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("written", OUT)
