import json, pathlib
OUT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\findings_361_365.json")
NL = "\n"
F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- p. 361
add(361, "throughout pp. 361-365 (category letters; first: line 1 'dans D(C)')",
    "plain typed capitals C and D (D(C), C_o, C_1, _A C, C_A, _A D), neither underlined nor script",
    r"\cC, \cD (defined as \mathcal C, \mathcal D)", "font", "high", None,
    r"Convention of the transcription for Exposé VIII, not itemized: the print's category letters are ordinary typed "
    r"capitals, the TeX sets them calligraphic. Examples: p. 361 'commutatif (dans $D(\cC)$)', p. 362 'Soit $A$ un "
    r"anneau et $\cC$ la catégorie', p. 364 'et par ${}_A\cD$ la sous-catégorie triangulée pleine'. One pass for the "
    r"exposé (\cC -> C, \cD -> D in the diplomatic layer) or one volume decision (compare GLOBAL_ISSUES 81 and 87, "
    r"SGA 6, where the print has an underlined or a script C).")
add(361, "'Soit Z le \"mapping cylinder\" de f'",
    "\"mapping cylinder\" (straight typewriter quotes)", "«mapping cylinder»", "punctuation", "high",
    {"old": "«mapping cylinder»", "new": "``mapping cylinder''"},
    "Guillemets for the print's straight quotes (the accepted forms are ``...'' and \"...\"), as logged on pp. 335, "
    "337, 343.")
add(361, "'(condition (A)). D'autre part' before the triangle",
    "D'autre part (no comma; the triangle follows)", "D'autre part,", "punctuation", "high",
    {"old": "D'autre part,", "new": "D'autre part"}, "Comma added by the TeX.")
add(361, "triangle diagram, base arrow X -> Y",
    "the base arrow X· ---> Y· carries no label (only h and g are labelled)", r"""\arrow[rr,"f"']""", "extra", "high",
    {"old": r"""\arrow[rr,"f"']""", "new": r"\arrow[rr]"},
    "The label f is the TeX's; the print labels f only in the square above. Checked at full resolution: nothing under "
    "or over the base arrow.")
add(361, "last paragraph, 'sera appelé pseudo-cohérent'",
    "pseudo-cohérent underlined", "pseudo-cohérent (plain)", "underline", "high",
    {"old": "appelé pseudo-cohérent", "new": r"appelé \emph{pseudo-cohérent}"},
    r"Defined term underlined in the print; \emph is the file's command for underlines in this part of s5.tex (as the "
    r"applied fixes of Exposé VII).")

# ---------------- p. 362
add(362, "start of the page",
    "p. 362 begins 'pour cela qu'il admette une résolution à gauche'; p. 361 ends '... on prouve qu'il faut et suffit'",
    "'pour' is the last word before the folio-362 marker (folio 361's TeX)", "marker", "high", None,
    "Page 362 really begins at 'pour' (the end of the line before the folio-362 marker). Exact fix: python -I "
    "move_marker.py 5 362 'pour' --before (simulated in memory on both layers: '... on prouve qu'il faut et suffit ' / "
    "marker / 'pour' / 'cela qu'il admette ...'). Text not moved. Not marker_split_word.py pull 'pour', which would "
    "give 'pourcela'.")
add(362, "heading 6",
    "6. Complexes parfaits. (full stop after the underlined title)", r"\subsection*{6. Complexes parfaits}",
    "punctuation", "high",
    {"old": r"\subsection*{6. Complexes parfaits}", "new": r"\subsection*{6. Complexes parfaits.}"},
    "Underlined title ends with a full stop in the print; the TeX drops it. The run-in layout is not reported.")
add(362, "heading 7",
    "7. Cas particulier important. (full stop after the underlined title)",
    r"\subsection*{7. Cas particulier important}", "punctuation", "high",
    {"old": r"\subsection*{7. Cas particulier important}", "new": r"\subsection*{7. Cas particulier important.}"},
    "As heading 6.")

# ---------------- p. 363
add(363, "start of the page",
    "p. 363 begins '(C). Nous utilisons dans ce cas les notations suivantes'; p. 362 ends '... satisfait les "
    "conditions (A), (B),'",
    "'(C).' ends folio 362's TeX, before the folio-363 marker", "marker", "high", None,
    "Page 363 really begins at '(C).' (the end of the line before the folio-363 marker). Exact fix: python -I "
    "move_marker.py 5 363 '(C).' --before (simulated in memory on both layers: '... satisfait les conditions (A), "
    "(B), ' / marker / '(C).' / 'Nous utilisons dans ce cas ...'). Text not moved.")
add(363, "first display, line 1",
    "D^-(A)_coh = D_o^-(C)_coh (no comma)", r"D_o^-(\cC)_{\coh},\qquad", "punctuation", "high",
    {"old": r"D_o^-(\cC)_{\coh},\qquad", "new": r"D_o^-(\cC)_{\coh}\qquad"},
    "The print sets the three equalities on three lines, the first two without punctuation, the third ending with a "
    "full stop; the TeX adds the commas (the line layout is not reported).")
add(363, "first display, line 2",
    "D^b(A)_coh = D_o^b(C)_coh (no comma)", r"D_o^b(\cC)_{\coh},", "punctuation", "high",
    {"old": r"D_o^b(\cC)_{\coh}," + NL + r"\]", "new": r"D_o^b(\cC)_{\coh}" + NL + r"\]"},
    "As line 1.")
add(363, "'seront appelés simplement des complexes pseudo-cohérents (resp. parfaits)'",
    "'complexes pseudo-cohérents' underlined; 'parfaits' underlined (not 'resp.', not the parentheses)",
    "plain", "underline", "high",
    {"old": "des complexes pseudo-cohérents (resp. parfaits).",
     "new": r"des \emph{complexes pseudo-cohérents} (resp. \emph{parfaits})."},
    "Defined terms underlined in the print.")
add(363, "display K.(A) = K(D^b(A)_coh)",
    "K.(A) = K(D^b(A)_coh) (no comma; the next line K·(A) = K(D(A)_parf) ends with a full stop)",
    r"K(D^b(A)_{\coh}),", "punctuation", "high",
    {"old": r"K(D^b(A)_{\coh}),", "new": r"K(D^b(A)_{\coh})"},
    "Comma added at the end of a display line.")
add(363, "'le classique \"groupe des classes de modules projectifs de type fini\" de A'",
    "\"groupe des classes de modules projectifs de type fini\" (straight typewriter quotes)",
    "«groupe des classes de modules projectifs de type fini»", "punctuation", "high",
    {"old": "«groupe des classes de modules projectifs de type fini»",
     "new": "``groupe des classes de modules projectifs de type fini''"},
    "Guillemets for the print's straight quotes, as on p. 361.")
add(363, "'le groupe K.(A) admet aussi une description classique'",
    "K (A): no subscript dot (a blank space after K; the other K.(A) of the page have a solid dot)",
    r"$K_\bullet(A)$", "misprint_in_print", "medium",
    {"old": r"le groupe $K_\bullet(A)$ admet", "new": r"le groupe $K(A)$ admet"},
    "The TeX silently corrects. At full resolution there is no trace of a dot below or beside the K, while the dots "
    "of the neighbouring K.(A) are crisp: read as the typist's omission, not a loss in the scan.",
    corrected=r"le groupe $K_\bullet(A)$ admet")
add(363, "last display K(C_1) = K(D^b(C_1)) = K(D^b_{C_1}(C))",
    "the display ends the page without punctuation; the sentence goes on 'car on a aussitôt' on p. 364",
    r"K(D^b_{\cC_1}(\cC)),", "punctuation", "high",
    {"old": r"K(D^b_{\cC_1}(\cC)),", "new": r"K(D^b_{\cC_1}(\cC))"},
    "Comma added at the end of the display.")

# ---------------- p. 364
add(364, "heading 8",
    "8. Tor de complexes. (full stop after the underlined title)", r"\subsection*{8. Tor de complexes}",
    "punctuation", "high",
    {"old": r"\subsection*{8. Tor de complexes}", "new": r"\subsection*{8. Tor de complexes.}"},
    "As headings 6 and 7 (p. 362).")
add(364, "'Soient A un anneau (non nécessairement commutatif)'",
    "(non nécessairement commutatif), in parentheses", "non nécessairement commutatif", "punctuation", "high",
    {"old": "un anneau non nécessairement commutatif et", "new": "un anneau (non nécessairement commutatif) et"},
    "Parentheses dropped by the TeX.")
add(364, "'des A-modules (à gauche) plats'",
    "(à gauche), in parentheses", "à gauche", "punctuation", "high",
    {"old": "des $A$-modules à gauche plats", "new": "des $A$-modules (à gauche) plats"},
    "Parentheses dropped by the TeX.")

# ---------------- p. 365
add(365, "start of the page",
    "p. 365 begins 'positions suivantes sont vraies'; p. 364 ends 'Dans ces conditions, les pro-'",
    "folio 365's TeX begins with the whole word 'propositions'", "marker", "high", None,
    "Page 365 really begins at 'positions': 'propositions' is divided at the page break. Exact fix: python -I "
    "marker_split_word.py 5 365 split pro positions (simulated in memory on both layers: '... Dans ces conditions, "
    "les' / 'pro%' / marker / 'positions suivantes sont vraies:'). Text not moved.")
add(365, "end of the page",
    "p. 365 ends 'd'où un bifonc-'",
    r"folio 365's TeX runs on with 'bifoncteur exact' and the display 'D^-(\cC_A)\times D^-({}_A\cC)\longrightarrow "
    r"D^-(\Ab),'",
    "marker", "high", None,
    "Page 366 really begins at 'teur' (second half of 'bifoncteur'): 'teur exact' and the display after it are "
    "printed on p. 366. Exact fix, two commands in this order: python -I move_marker.py 5 366 'bifoncteur' --before, "
    "then python -I marker_split_word.py 5 366 split bifonc teur (simulated in memory on both layers: \"... d'où un \" "
    "/ 'bifonc%' / marker / 'teur exact' / '\\[ D^-(\\cC_A)\\times ...'). A single move_marker.py to 'teur exact' "
    "would print 'bifonc teur'. Text not moved; that text is p. 366's to check.")
add(365, "item 1), before 'En effet, N· étant un objet'",
    "'En effet, ...' begins a new indented paragraph after '... de K^-(Ab) .'", "run on in the item-1) paragraph",
    "other", "high",
    {"old": r"de $K^-(\Ab)$. En effet", "new": r"de $K^-(\Ab)$." + NL + NL + "En effet"},
    "Paragraph break; drop it if paragraphing is left to a global pass.")
add(365, "item 2), before 'Il suffit pour cela'",
    "'Il suffit pour cela ...' begins a new indented paragraph", "run on in the item-2) paragraph", "other", "high",
    {"old": r"${}_A\cD$. Il suffit", "new": r"${}_A\cD$." + NL + NL + "Il suffit"},
    "Paragraph break; drop it if paragraphing is left to a global pass.")
add(365, "display of the left derived functor",
    "L with a double underline and a superscript minus: L^- Phi_X· : D^-(_A C) ---> D^-(Ab) .", r"\underline{L}^{-}",
    "font", "high",
    {"old": r"\underline{L}^{-}", "new": r"\underline{\underline{L}}^{-}"},
    r"The print's derived-functor L is doubly underlined here and in the three places below; the TeX has a single "
    r"underline here and \mathbf L elsewhere. Fix in the form used for the double-underlined L on p. 37 "
    r"(findings_036_040).")
add(365, "'L'objet L^- Phi_X·(Y) peut être obtenu'",
    "double-underlined L with a superscript minus: L^- Phi_X·(Y)", r"\mathbf L\Phi_{X^\bullet}(Y^\bullet)", "formula",
    "high",
    {"old": r"L'objet $\mathbf L", "new": r"L'objet $\underline{\underline{L}}^{-}"},
    "The TeX drops the superscript minus and writes bold for the double underline (as the display above). "
    "Independent of the misprint item below.")
add(365, "'L'objet L^- Phi_X·(Y) peut être obtenu'",
    "(Y) without the raised dot (the next two occurrences read Y·)", r"(Y^\bullet)", "misprint_in_print", "medium",
    {"old": r"(Y^\bullet)$ peut", "new": "(Y)$ peut"},
    "The TeX silently corrects. No trace of a dot after Y at full resolution, while the dot of X· just before is "
    "crisp: the typist's omission.",
    corrected=r"(Y^\bullet)$ peut")
add(365, "'de la manière suivante :'",
    "suivante : (colon)", "suivante. (full stop)", "punctuation", "high",
    {"old": "de la manière suivante.", "new": "de la manière suivante:"},
    "Colon of the print replaced by a full stop.")
add(365, "before 'Soient P· un objet de _A D'",
    "'Soient ...' begins a new indented paragraph", "run on after 'de la manière suivante.'", "other", "high",
    {"old": r" Soient $P^\bullet$", "new": NL + NL + r"Soient $P^\bullet$"},
    "Paragraph break; drop it if paragraphing is left to a global pass. Adjacent to, and independent of, the colon "
    "item.")
add(365, "'Alors L^- Phi_X·(Y·) est isomorphe à'",
    "double-underlined L with a superscript minus", r"\mathbf L", "formula", "high",
    {"old": r"Alors $\mathbf L", "new": r"Alors $\underline{\underline{L}}^{-}"},
    "As 'L'objet' above.")
add(365, "'est isomorphe à Q(X· (x) P)'",
    "Q(X· (x) P): tensor sign without subscript A", r"Q(X^\bullet\otimes_A P^\bullet)", "formula", "high",
    {"old": r"Q(X^\bullet\otimes_A", "new": r"Q(X^\bullet\otimes"},
    "Subscript A added by the TeX (the print writes it in X·(x)_A· on p. 364 and in H_n(X·(x)_A N·) above, not "
    "here). Independent of the misprint item below.")
add(365, "'est isomorphe à Q(X· (x) P)'",
    "P without the raised dot", r"P^\bullet", "misprint_in_print", "medium",
    {"old": r"P^\bullet),", "new": "P),"},
    "The TeX silently corrects. No trace of a dot after P at full resolution (P· two lines above): the typist's "
    "omission.",
    corrected=r"P^\bullet),")
add(365, "'Il en résulte donc que pour chaque objet'",
    "donc que pour (no comma)", "donc que, pour", "punctuation", "high",
    {"old": "donc que, pour", "new": "donc que pour"}, "Comma added by the TeX.")
add(365, "'de D^-(_A C) le foncteur'",
    "D^-(_A C) le foncteur (no comma)", r"$D^-({}_A\cC)$, le foncteur", "punctuation", "high",
    {"old": r"$D^-({}_A\cC)$, le foncteur", "new": r"$D^-({}_A\cC)$ le foncteur"}, "Comma added by the TeX.")
add(365, "two-line display K^-(C_A) ---> D^-(Ab) / X· ~~> L^- Phi_X·(Y·)",
    "no punctuation after D^-(Ab) (nor at the end of the display)", r"D^-(\Ab),\qquad", "punctuation", "high",
    {"old": r"D^-(\Ab),\qquad", "new": r"D^-(\Ab)\qquad"},
    "Comma added by the TeX (the two lines set side by side is layout, not reported).")
add(365, "same display, second line",
    "wavy arrow X· ~~~> (a squiggle, then a straight shaft and head)", r"\longmapsto", "symbol", "high",
    {"old": r"X^\bullet\longmapsto", "new": r"X^\bullet\rightsquigarrow"},
    r"The print's arrow is wavy, not a maps-to arrow. \rightsquigarrow is in amssymb, which s5.tex loads.")
add(365, "same display, second line",
    "double-underlined L with a superscript minus: L^- Phi_X·(Y·)", r"\mathbf L\Phi_{X^\bullet}(Y^\bullet)",
    "formula", "high",
    {"old": r"\mathbf L\Phi_{X^\bullet}(Y^\bullet)" + NL + r"\]",
     "new": r"\underline{\underline{L}}^{-}\Phi_{X^\bullet}(Y^\bullet)" + NL + r"\]"},
    "As 'L'objet' above. Independent of the arrow item.")

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(F), "findings written")
