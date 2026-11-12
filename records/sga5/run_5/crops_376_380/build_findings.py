"""Build findings_376_380.json and check every fix: exactly one occurrence of 'old' when the fixes of a page are
applied in the listed order (diplomatic edition), and also when the misprint fixes are skipped (corrected edition)."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
B = RUN / "b376_380"
OUT = RUN / "findings_376_380.json"

UL = ("Exposé X has no underline markup in the TeX; \\emph as for the underlined statements of Exposé XII and "
      "the rest of s5.tex.")

F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def fx(old, new):
    return {"old": old, "new": new}


# ---------------------------------------------------------------- page 376
add(376, "section title 3", "3. Rappels sur les représentations linéaires des groupes finis. (underlined, full stop)",
    r"\subsection*{3. Rappels sur les représentations linéaires des groupes finis}", "punctuation", "high",
    fx(r"des groupes finis}", r"des groupes finis.}"),
    "The underlined title ends with a full stop in the print.")
add(376, "first sentence of 3", "Dans ce n° , Λ désigne un anneau commutatif",
    "Dans ce numéro, $\\Lambda$ désigne", "word", "high",
    fx("Dans ce numéro,", r"Dans ce n\textsuperscript{o},"),
    "The print abbreviates: n with a raised o (as reported on pp. 150, 164).")
add(376, "paragraph 3.1", "3.1. Considérons la sous-catégorie pleine ... (no title)",
    r"\subsubsection*{3.1. Caractères}", "extra", "high",
    fx(r"\subsubsection*{3.1. Caractères}", r"\subsubsection*{3.1.}"),
    "The print has no title 'Caractères': the number 3.1. runs into the text.")
add(376, "3.1, 'la sous-catégorie pleine 𝒞 de Mod(Λ[G])'", "hand-drawn script C",
    r"$\mathcal E$", "symbol", "medium",
    fx(r"pleine $\mathcal E$ de", r"pleine $\mathcal C$ de"),
    "The hand-drawn letter is a script C (one bowl with a loop at the top, no middle stroke of an E); p. 377 "
    "names the same category C(G), C(G'), which the TeX writes \\mathcal C. Same letter in Ob(...) below.")
add(376, "3.1, 'l'endomorphisme (pour la structure de Λ-module)'",
    "l'endomorphisme (pour la structure de Λ-module)",
    "l'endomorphisme, pour la structure de $\\Lambda$-module,", "punctuation", "high",
    fx(r"l'endomorphisme, pour la structure de $\Lambda$-module,",
       r"l'endomorphisme (pour la structure de $\Lambda$-module)"),
    "The print has parentheses and no commas.")
add(376, "3.1, 'une fonction centrale sur G'", "centrale underlined", "fonction centrale sur", "underline", "high",
    fx("fonction centrale sur", r"fonction \emph{centrale} sur"), UL)
add(376, "3.1, 'le caractère du Λ[G]-module M'", "'caractère du' and 'module' underlined, not 'Λ[G]-'",
    "le caractère du $\\Lambda[G]$-module $M$.", "underline", "high",
    fx(r"le caractère du $\Lambda[G]$-module $M$.", r"le \emph{caractère du} $\Lambda[G]$-\emph{module} $M$."),
    UL)
add(376, "3.1, 'M ∈ Ob(𝒞 )'", "Ob (capital O)", r"$M\in\Ob(\mathcal E)$ (\Ob prints 'ob')", "word", "high",
    fx(r"\in\Ob", r"\in\operatorname{Ob}"),
    "\\Ob is \\operatorname{ob} in s5.tex (first \\providecommand, preamble line 101), so the TeX prints 'ob'; the "
    "print has 'Ob'.")
add(376, "3.1, 'Ob(𝒞 )'", "hand-drawn script C", r"(\mathcal E)", "symbol", "medium",
    fx(r"(\mathcal E)", r"(\mathcal C)"),
    "Same hand-drawn script C as in 'la sous-catégorie pleine 𝒞'.")
add(376, "3.1, 'son caractère χ_M on obtient'", "no comma after χ_M", "$\\chi_M$, on obtient", "punctuation", "high",
    fx(r"$\chi_M$, on obtient", r"$\chi_M$ on obtient"),
    "No comma in the print.")
add(376, "display R˙(G) --Tr--> 𝓕(G,Λ) ,", "R˙(G) with Tr written over the arrow, then 𝓕(G,Λ) ,",
    r"\Tr:R^{\bullet}(G)\longrightarrow \mathcal F(G,\Lambda),", "formula", "high",
    fx(r"\Tr:R^{\bullet}(G)\longrightarrow \mathcal F(G,\Lambda),", r"R^{\bullet}(G)\xrightarrow{\Tr}\mathcal F(G,\Lambda),"),
    "The print labels the arrow with Tr; it does not write 'Tr :' before R˙(G).")

# ---------------------------------------------------------------- page 377
add(377, "Proposition 3.2, first sentence", "statement underlined word group by word group",
    "Soient $\\mathbb Z_\\ell$ l'anneau des entiers ... Alors l'homomorphisme (no underline)", "underline", "high",
    fx(r"Soient $\mathbb Z_\ell$ l'anneau des entiers $\ell$-adiques et $G$ un groupe fini. Alors l'homomorphisme",
       r"\emph{Soient} $\mathbb Z_\ell$ \emph{l'anneau des entiers} $\ell$-\emph{adiques et} $G$ \emph{un groupe fini}. \emph{Alors l'homomorphisme}"),
    "Underlined: 'Soient', 'l'anneau des entiers', 'adiques et' (not the hyphen after ℓ), 'un groupe fini', 'Alors "
    "l'homomorphisme'; Z_ℓ, ℓ, G and the full stop are not. " + UL)
add(377, "Proposition 3.2, after the display", "statement underlined word group by word group",
    "est un monomorphisme. Deux ... sont isomorphes. (no underline)", "underline", "high",
    fx(r"est un monomorphisme. Deux $\mathbb Z_\ell[G]$-modules projectifs ayant même fonction trace dans $\mathcal F(G,\mathbb Z_\ell)$ sont isomorphes.",
       r"\emph{est un monomorphisme}. \emph{Deux} $\mathbb Z_\ell[G]$-\emph{modules projectifs ayant même fonction trace dans} $\mathcal F(G,\mathbb Z_\ell)$ \emph{sont isomorphes}."),
    "The underline restarts after '[G]-'; Z_ℓ[G] and 𝓕(G,Z_ℓ) are not underlined.")
add(377, "paragraph 3.3", "3.3. Soit α : G → G' ... (no title)", r"\subsubsection*{3.3. Restriction et induction}",
    "extra", "high",
    fx(r"\subsubsection*{3.3. Restriction et induction}", r"\subsubsection*{3.3.}"),
    "The print has no title 'Restriction et induction': the number 3.3. runs into the text.")
add(377, "3.3, 'on obtient un foncteur exact :'", "colon before the display", "on obtient un foncteur exact",
    "punctuation", "high",
    fx("on obtient un foncteur exact", "on obtient un foncteur exact:"),
    "The print ends the sentence with a colon.")
add(377, "display J : Mod(Λ[G']) ⇝ Mod(Λ[G]) .", "hand-drawn wavy arrow", r"\longrightarrow", "symbol", "high",
    fx(r"J:\Mod(\Lambda[G'])\longrightarrow", r"J:\Mod(\Lambda[G'])\rightsquigarrow"),
    "The arrows of the functors J and I are hand-drawn wavy arrows; the other arrows of the page are straight.")
add(377, "3.3, 'Ce foncteur admet un adjoint à gauche :'", "colon before the display", "un adjoint à gauche",
    "punctuation", "high",
    fx("un adjoint à gauche", "un adjoint à gauche:"),
    "The print ends the sentence with a colon.")
add(377, "display I : Mod(Λ[G]) ⇝ Mod(Λ[G']) ,", "hand-drawn wavy arrow", r"\longrightarrow", "symbol", "high",
    fx(r"I:\Mod(\Lambda[G])\longrightarrow", r"I:\Mod(\Lambda[G])\rightsquigarrow"),
    "As for J.")
add(377, "3.3, 'Si F est projectif de type fini (resp. de type fini) I(F) l'est aussi.'",
    "(resp. de type fini) without commas", "type fini, respectivement de type fini, $I(F)$", "word", "high",
    fx(r"projectif de type fini, respectivement de type fini, $I(F)$", r"projectif de type fini (resp. de type fini) $I(F)$"),
    "The print abbreviates 'resp.' and has parentheses, no commas.")
add(377, "display α♮ : 𝓕(G',Λ) → 𝓕(G,Λ) .", "α with a hand-drawn natural sign ♮ as subscript", r"\alpha^*",
    "symbol", "medium",
    fx(r"\alpha^*: \mathcal F", r"\alpha_\natural: \mathcal F"),
    "The sign after α is a hand-drawn natural sign (two strokes joined by a parallelogram, the left rising, the right "
    "descending) set low, not a superscript star; the same sign in α♮(φ) below.")
add(377, "3.3, 'M dans C(G'),'", "typed plain C", r"$\mathcal C(G')$", "font", "medium",
    fx(r"dans $\mathcal C(G')$,", r"dans $C(G')$,"),
    "On this page the typist types a plain C for the category (the typewriter C of 'Ce foncteur'); p. 376 draws a "
    "script C. Also C(G) and C(G') below.")
add(377, "3.3, 'α♮ (φ) est le caractère'", "α with subscript natural sign", r"$\alpha^*(\varphi)$", "symbol", "medium",
    fx(r"$\alpha^*(\varphi)$", r"$\alpha_\natural(\varphi)$"),
    "As in the display α♮ : 𝓕(G',Λ) → 𝓕(G,Λ).")
add(377, "3.3, 'Supposons maintenant que α : G → G' est une injection'", "est une injection", "soit une injection",
    "word", "high",
    fx("soit une injection", "est une injection"),
    "The print has the indicative 'est' (then 'et que G soit d'indice fini').")
add(377, "3.3, 'Dans ce cas si F est'", "no comma", "Dans ce cas, si", "punctuation", "high",
    fx("Dans ce cas, si", "Dans ce cas si"),
    "No comma in the print.")
add(377, "3.3, 'dans C(G) dont le caractère'", "typed plain C", r"$\mathcal C(G)$", "font", "medium",
    fx(r"dans $\mathcal C(G)$ dont", r"dans $C(G)$ dont"),
    "As 'dans C(G'),' above.")
add(377, "3.3, 'I(F) est dans C(G') et'", "typed plain C", r"$\mathcal C(G')$", "font", "medium",
    fx(r"dans $\mathcal C(G')$ et", r"dans $C(G')$ et"),
    "As 'dans C(G'),' above.")
add(377, "3.3, 'par ψ , i.e. la fonction sur G''", "i.e.", "c'est-à-dire", "word", "high",
    fx("c'est-à-dire la fonction", "i.e. la fonction"),
    "The print abbreviates.")
add(377, "3.3, 'par la formule :' (last line of the page)", "colon", "par la formule", "punctuation", "high",
    fx(r"déduite de $\psi$ par la formule", r"déduite de $\psi$ par la formule:"),
    "The print ends the page with a colon.")

# ---------------------------------------------------------------- page 378
add(378, "top of the page / folio-378 marker",
    "p. 377 ends with 'par la formule :'; p. 378 begins with the display (3.3.1) ψ*(g) = Σ_{t∈G'/G} ψ(t⁻¹gt) ,",
    "the display (3.3.1) is the last thing in page_377.tex", "marker", "high", None,
    "Page 378 really begins at the '\\[' that opens the display (3.3.1) (the last four lines of page_377.tex). "
    "Exact fix: python -I move_marker.py 5 378 '\\[' --before (simulated in memory on both layers: the marker "
    "goes on its own line between 'par la formule' and that '\\[').")
add(378, "paragraph 3.4", "3.4.", r"\subsubsection*{3.4}", "punctuation", "high",
    fx(r"\subsubsection*{3.4}", r"\subsubsection*{3.4.}"),
    "The paragraph number has a full stop in the print, as the reported 8.4., 8.6., 9.5.")
add(378, "3.4, 'X˙ est un objet de D˙(A)' and 'X˙ dans D˙(A)'", "D with the raised dot of the complexes (twice)",
    r"$D^\bullet(A)$ (twice)", "misprint_in_print", "low", None,
    "The diplomatic TeX keeps the printed reading. A projective resolution P˙ → X˙ needs a bounded-above complex, "
    "so D⁻(A) is meant; the current layer already reads $D^-(A)$ in both places.",
    corrected=r"$D^-(A)$")
add(378, "3.4, 'dépendant fonctoriellement de X˙ dans D˙(A) et Y dans D(A ⊗_ℤ B)'", "Y without the raised dot",
    r"$Y^\bullet$", "misprint_in_print", "medium",
    fx(r"et $Y^\bullet$ dans $D(A", r"et $Y$ dans $D(A"),
    "The print omits the dot here (sharp scan, no trace of it); the TeX silently adds it. Fix restores the print.",
    corrected=r"$Y^\bullet$")
add(378, "3.4, 'pour le cas du complexe X˙ ⊗^𝕃_A Y˙'", "hand-drawn double-struck L over the tensor sign",
    r"\otimes_A^{\mathbf L}", "font", "high",
    fx(r"du complexe $X^\bullet\otimes_A^{\mathbf L}", r"du complexe $X^\bullet\otimes_A^{\mathbb L}"),
    "The L is double-struck (two stems), not bold; same in the second derived tensor of the page and on p. 379.")
add(378, "3.4, 'comme plus haut et X et un complexe de A-modules'", "et X et un complexe", "et $X$ et un complexe",
    "misprint_in_print", "high", None,
    "'et' for 'est' (and X without the dot); the diplomatic TeX keeps the printed reading; the current layer "
    "already reads '$X^\\bullet$ est'.",
    corrected=r"et $X^\bullet$ est un complexe")
add(378, "3.4, 'à droite et borné a droite'", "borné a droite", "borné a droite", "misprint_in_print", "high", None,
    "Accent missing in the print; the TeX keeps it; the current layer already reads 'à droite'.",
    corrected="borné à droite")
add(378, "3.4, 'on peut définir X˙ ⊗^𝕃_A Y˙'", "double-struck L", r"\otimes_A^{\mathbf L}", "font", "high",
    fx(r"définir $X^\bullet\otimes_A^{\mathbf L}", r"définir $X^\bullet\otimes_A^{\mathbb L}"),
    "As above.")
add(378, "paragraph 3.5", "3.5.", r"\subsubsection*{3.5}", "punctuation", "high",
    fx(r"\subsubsection*{3.5}", r"\subsubsection*{3.5.}"),
    "The paragraph number has a full stop in the print.")

# ---------------------------------------------------------------- page 379
add(379, "top of the page / folio-379 marker",
    "p. 378 ends with '3.5. Soient Λ un anneau commutatif, A et B deux algèbres sur Λ et'; p. 379 begins "
    "'C = A ⊗_Λ B . Les C-modules sont donc les A-B-bimodules.'",
    "'$C=A\\otimes_{\\Lambda}B$. Les $C$-' ends page_378.tex; the marker splits C-modules", "marker", "high", None,
    "Page 379 really begins at '$C=A\\otimes_{\\Lambda}B$. Les $C$-' (the end of the last line of page_378.tex); the "
    "marker also splits the word C-modules ('Les $C$-' / marker / 'modules', which prints 'C- modules'). Exact fix: "
    "python -I marker_split_word.py 5 379 pull '$C=A\\otimes_{\\Lambda}B$. Les $C$-' (simulated in memory on both "
    "layers: p. 378 ends '... sur $\\Lambda$ et' and p. 379 begins '$C=A\\otimes_{\\Lambda}B$. Les $C$-modules sont "
    "donc les $A$-$B$-bimodules.').")
add(379, "Proposition 3.6, first lines", "statement underlined word group by word group",
    "Les notations étant celles de 3.4 et 3.5, ... (VIII 7) et (no underline)", "underline", "high",
    fx(r"Les notations étant celles de 3.4 et 3.5, soit $\Delta$ une sous-catégorie triangulée pleine de $D(A)$ stable par facteurs directs. Si $P^\bullet$ est un objet de $D(B)_{\parf}$ (VIII 7) et",
       r"\emph{Les notations étant celles de} 3.4 \emph{et} 3.5, \emph{soit} $\Delta$ \emph{une sous-catégorie triangulée pleine de} $D(A)$ \emph{stable par facteurs directs}. \emph{Si} $P^\bullet$ \emph{est un objet de} $D(B)_{\parf}$ (VIII 7) \emph{et}"),
    "Numbers, letters, formulas, (VIII 7) and the punctuation are not underlined. " + UL)
add(379, "Proposition 3.6, 'et M est un objet de D(C)_Δ'", "M without the raised dot", r"$M^\bullet$",
    "misprint_in_print", "medium",
    fx(r"$M^\bullet$", r"$M$"),
    "The print omits the dot (sharp scan); the TeX silently adds it. Fix restores the print.",
    corrected=r"$M^\bullet$")
add(379, "Proposition 3.6, 'est un objet de D(C)_Δ , le complexe de A-modules'", "underlined word groups",
    "no underline", "underline", "high",
    fx(r"est un objet de $D(C)_{\Delta}$, le complexe de $A$-modules",
       r"\emph{est un objet de} $D(C)_{\Delta}$, \emph{le complexe de} $A$-\emph{modules}"),
    "'A-' is not underlined.")
add(379, "Proposition 3.6, 'défini dans 4.1 est un objet de Δ . Il en résulte ... triangulées'",
    "underlined word groups", "no underline", "underline", "high",
    fx(r"défini dans 4.1 est un objet de $\Delta$. Il en résulte en particulier un accouplement de catégories triangulées",
       r"\emph{défini dans} 4.1 \emph{est un objet de} $\Delta$. \emph{Il en résulte en particulier un accouplement de catégories triangulées}"),
    "")
add(379, "Proposition 3.6, 'défini dans 4.1'", "4.1", "4.1", "misprint_in_print", "medium", None,
    "Wrong reference number, kept by the TeX: RHom with the structure coming from a bimodule is defined in 3.4 "
    "(Lemme 4.1 is about fixed points). The print keeps an older numbering in this part (p. 380 '(4.3.1)' for "
    "(3.7.1); the current layer already corrects p. 382 '(4.3.4)' to (3.8.1)).",
    corrected="3.4")
add(379, "Proposition 3.6, after (3.6.1)", "underlined word groups; colon after 'bilinéaire'",
    "no underline, no colon", "underline", "high",
    fx(r"c'est-à-dire un bifoncteur exact en chaque variable, et par conséquent (VIII 3) une application bilinéaire",
       r"\emph{c'est-à-dire un bifoncteur exact en chaque variable}, \emph{et par conséquent} (VIII 3) \emph{une application bilinéaire}:"),
    "One edit: it also gives the print's colon after 'bilinéaire' (punctuation).")
add(379, "Proposition 3.6, 'telle que'", "underlined", "telle que", "underline", "high",
    fx("telle que", r"\emph{telle que}"), "")
add(379, "(3.6.3), first argument", "cℓ_{K˙(B)}(P) (P without the dot)", r"\cl_{K^{\bullet}(B)}(P^\bullet)",
    "misprint_in_print", "medium",
    fx(r"(B)}(P^\bullet)", r"(B)}(P)"),
    "The print omits the dot; the TeX silently adds it. Fix restores the print.",
    corrected=r"(B)}(P^\bullet)")
add(379, "(3.6.3), second subscript", "cℓ_{K(D(C)_Λ)} (Λ, no base stroke)", r"\cl_{K(D(C)_{\Delta})}",
    "misprint_in_print", "high",
    fx(r"K(D(C)_{\Delta})}", r"K(D(C)_{\Lambda})}"),
    "The print types Λ (the ring's letter) for Δ here; the TeX silently corrects. Fix restores the print.",
    corrected=r"K(D(C)_{\Delta})}")
add(379, "Proposition 3.6, last sentence, first part",
    "'On obtient un énoncé analogue si l'on remplace', 'par son opposé', 'et' underlined",
    "no underline", "underline", "high",
    fx(r"On obtient un énoncé analogue si l'on remplace $B$ par son opposé $B^\circ$ et",
       r"\emph{On obtient un énoncé analogue si l'on remplace} $B$ \emph{par son opposé} $B^\circ$ \emph{et}"),
    "Apply before the next finding (its 'old' starts with this edit's '\\emph{et}').")
add(379, "Proposition 3.6, last sentence, 'ℝHom_B(P,M) par'", "ℝHom_B(P,M) (P, M without the dots)",
    r"\RHom_B(P^\bullet,M^\bullet)", "misprint_in_print", "medium",
    fx(r"\emph{et} $\RHom_B(P^\bullet,M^\bullet)$", r"\emph{et} $\RHom_B(P,M)$"),
    "The print omits both dots (the following P˙ ⊗ M˙ has them); the TeX silently adds them. The 'old' is taken "
    "from the text after the preceding underline fix (apply after it).",
    corrected=r"\RHom_B(P^\bullet,M^\bullet)")
add(379, "Proposition 3.6, last sentence, 'par P˙ ⊗ M˙'", "'par' underlined", "par", "underline", "high",
    fx(r" par $P^\bullet", r" \emph{par} $P^\bullet"), "")
add(379, "Proposition 3.6, 'P˙ ⊗^𝕃_B M˙'", "hand-drawn double-struck L", r"\otimes_B^{\mathbf L}", "font", "high",
    fx(r"\otimes_B^{\mathbf L}", r"\otimes_B^{\mathbb L}"),
    "As on p. 378.")
add(379, "Démonstration, 'R Hom_B(P,M)'", "plain typewriter R (one stem)",
    r"$\RHom_B$ (\mathbb{R}\mathrm{Hom} in the diplomatic layer)", "font", "medium",
    fx(r"que $\RHom_B", r"que $\mathrm{R}\Hom_B"),
    "In the diplomatic s5.tex \\RHom is \\mathbb{R}\\mathrm{Hom}, which matches the double-struck R of the statement "
    "and of p. 378; in the Démonstration the typist types a plain R.")
add(379, "Démonstration, 'R Hom_B(P,M) est un objet'", "P, M without the dots",
    r"(P^\bullet,M^\bullet)", "misprint_in_print", "medium",
    fx(r"(P^\bullet,M^\bullet)$ est un", r"(P,M)$ est un"),
    "The print omits both dots; the TeX silently adds them. Fix restores the print.",
    corrected=r"(P^\bullet,M^\bullet)$ est un")
add(379, "Démonstration, 'est un objet de Λ dans le cas particulier'", "Λ", r"$\Delta$", "misprint_in_print", "high",
    fx(r"de $\Delta$ dans", r"de $\Lambda$ dans"),
    "The print types Λ for Δ; the TeX silently corrects. Fix restores the print.",
    corrected=r"de $\Delta$ dans")
add(379, "paragraph 3.7 (printed at the top of p. 380)", "3.7.", r"\subsubsection*{3.7}", "punctuation", "high",
    fx(r"\subsubsection*{3.7}", r"\subsubsection*{3.7.}"),
    "The heading stands in page_379.tex but is printed on p. 380 (see the folio-380 marker finding); apply this "
    "edit before moving the marker, or on the whole file.")

# ---------------------------------------------------------------- page 380
add(380, "top of the page / folio-380 marker",
    "p. 379 ends with the Démonstration ('... de P˙ .'); p. 380 begins '3.7. Soit P un Λ[G]-module.'",
    "\\subsubsection*{3.7} is the last line of page_379.tex", "marker", "high", None,
    "Page 380 really begins at '\\subsubsection*{3.7}' (the last line of page_379.tex). Exact fix: "
    "python -I move_marker.py 5 380 '\\subsubsection*{3.7}' --before (simulated in memory on both layers).")
add(380, "3.7, 'i.e. :' before (3.7.1)", "colon after i.e.", "i.e.", "punctuation", "high",
    fx(r"$(gu)(x)=u(g^{-1}x)$, i.e.", r"$(gu)(x)=u(g^{-1}x)$, i.e.:"),
    "The print has 'i.e. :'.")
add(380, "(3.7.1)", "g_P = ᵗ(g⁻¹)_P . (no check over the left subscript P)", r"g_{\check P}={}^{t}(g^{-1})_P.",
    "misprint_in_print", "high",
    fx(r"g_{\check P}=", r"g_P="),
    "The hand-drawn check is missing over the left subscript (the other checks of the page are clear); the TeX "
    "silently adds it. Fix restores the print.",
    corrected=r"g_{\check P}=")
add(380, "3.7, 'sera appelé le dual de P'", "'le dual' underlined", "le dual", "underline", "high",
    fx("appelé le dual de", r"appelé \emph{le dual} de"), UL)
add(380, "3.7, 'd'un complexe P de Λ[G]-modules'", "P without the raised dot", r"$P^\bullet$",
    "misprint_in_print", "medium",
    fx(r"d'un complexe $P^\bullet$", r"d'un complexe $P$"),
    "The print omits the dot; the TeX silently adds it. Fix restores the print.",
    corrected=r"$P^\bullet$")
add(380, "3.7, 'qui se déduit immédiatement de (4.3.1)'", "(4.3.1)", "(4.3.1)", "misprint_in_print", "medium", None,
    "Wrong reference number, kept by the TeX: (3.7.2) follows from (3.7.1) and the trace formula; there is no "
    "(4.3.1) in Exposé X. Same older numbering as '4.1' on p. 379 and '(4.3.4)' for (3.8.1) on p. 382 (corrected "
    "there in the current layer).",
    corrected="(3.7.1)")
add(380, "3.7, 'l'homomorphisme canonique de Λ-modules :'", "colon before the display",
    "canonique de $\\Lambda$-modules", "punctuation", "high",
    fx(r"canonique de $\Lambda$-modules", r"canonique de $\Lambda$-modules:"),
    "The print ends the sentence with a colon.")
add(380, "display x ⟶ x̌ ,", "plain long arrow", r"x\longmapsto \check x,", "symbol", "high",
    fx(r"x\longmapsto \check x,", r"x\longrightarrow \check x,"),
    "The print's arrow has no bar at its tail.")
add(380, "last line, 'commute aux involutions x ⟶ x̌ sur'", "plain long arrow", r"$x\longmapsto \check x$",
    "symbol", "high",
    fx(r"involutions $x\longmapsto \check x$", r"involutions $x\longrightarrow \check x$"),
    "As in the display.")
add(380, "end of the page / folio-381 marker",
    "p. 380 ends with 'commute aux involutions x ⟶ x̌ sur'; p. 381 begins 'K˙(Λ[G]) et K˙(Γ[G]) .'",
    "'$K^{\\bullet}(\\Lambda[G])$ et $K^{\\bullet}(\\Gamma[G])$.' ends page_380.tex", "marker", "high", None,
    "The rest of the page is blank in the scan and the OCR of p. 381 (ocr_5/page_381.txt) begins with "
    "'K˙(Λ[G]) et K˙(Γ[G]) .'. Page 381 really begins at '$K^{\\bullet}(\\Lambda[G])$ et "
    "$K^{\\bullet}(\\Gamma[G])$.' (end of the last line of page_380.tex). Exact fix: python -I move_marker.py 5 381 "
    "'$K^{\\bullet}(\\Lambda[G])$ et' --before (simulated in memory on both layers).")

# ---------------------------------------------------------------- checks
ok = True
for page in sorted({f["page"] for f in F}):
    orig = (B / f"page_{page}.tex").read_text(encoding="utf-8")
    dip, cor = orig, orig
    for f in [f for f in F if f["page"] == page]:
        fix = f["fix"]
        if not fix:
            continue
        old, new = fix["old"], fix["new"]
        if "%%%%%%%%%%" in old or "%%%%%%%%%%" in new:
            print("MARKER LINE TOUCHED", page, old); ok = False
        n_orig = orig.count(old)
        n_dip = dip.count(old)
        if n_dip != 1:
            print("DIPLOMATIC COUNT", n_dip, page, repr(old)); ok = False
        dip = dip.replace(old, new, 1)
        if f["kind"] != "misprint_in_print":
            n_cor = cor.count(old)
            if n_cor != 1:
                print("CORRECTED COUNT", n_cor, page, repr(old)); ok = False
            cor = cor.replace(old, new, 1)
        if n_orig != 1:
            print("note: old not once in the original page file (taken after a preceding fix):", page, repr(old), n_orig)
    # the marker line must be unchanged
    assert dip.split("\n")[1] == orig.split("\n")[1]
print("all fixes apply" if ok else "PROBLEMS")
counts = {}
for f in F:
    c = counts.setdefault(f["page"], [0, 0])
    c[1 if f["kind"] == "misprint_in_print" else 0] += 1
print(counts, len(F))
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("written", OUT)
