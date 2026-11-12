"""Build findings_251_255.json (helper for the scan check of SGA 5 pp. 251-255)."""
import json
import pathlib

OUT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\findings_251_255.json")


def L(*parts):
    return "\n".join(parts)


F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, confidence=conf, fix=fix)
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- p. 250 (text of p. 251 under the folio-250 marker)
add(250, "heading of Exposé VI (printed at the top of p. 251; in page_250.tex as the files stand)",
    "E X P O S É  VI: capitals (letter-spaced, underlined)",
    r"\section*{Exposé VI}", "word", "high",
    {"old": r"\section*{Exposé VI}", "new": r"\section*{EXPOSÉ VI}"},
    "Capitals as printed, as 'EXPOSÉ V' on p. 204. Filed under p. 250, where the line stands now: apply before "
    "the marker move of p. 251 (the move's anchor '\\section*{E' matches the line before and after this edit).")

# ---------------------------------------------------------------- p. 251
add(251, "top of the page: the heading EXPOSÉ VI",
    "p. 251 begins with 'EXPOSÉ VI', then 'COHOMOLOGIE L-ADIQUE' and 'par J.P, JOUANOLOU'; p. 250 ends with "
    "'A.2. a) que : E_inf^(n)(X) = grs T^n(X).'",
    "'\\section*{Exposé VI}' and '\\begin{center}' (s5.tex lines 8459-8461 diplomatic, 8458-8460 current) end "
    "page_250.tex; the folio-251 marker (line 8462 diplomatic) stands inside the center environment, before "
    "'\\textbf{COHOMOLOGIE'",
    "marker", "high", None,
    "Page 251 really begins at s5.tex line 8459 '\\section*{Exposé VI}' (diplomatic). Exact fix: "
    "python -I move_marker.py 5 251 '\\section*{E' --before (simulated in memory on both layers, before and after "
    "the EXPOSÉ capitals fix filed under p. 250: the marker then stands after the '\\renewenvironment{prooftext}' "
    "line, just before '\\section*{Exposé VI}', and the center environment is whole on p. 251). Text not moved.")

add(251, "title of the exposé",
    "COHOMOLOGIE L-ADIQUE (a typed capital L, not the hand-drawn script l)",
    r"\textbf{COHOMOLOGIE \(\ell\)-ADIQUE}", "symbol", "high",
    {"old": r"COHOMOLOGIE \(\ell\)-ADIQUE", "new": r"COHOMOLOGIE L-ADIQUE"},
    "The capitals title has the typewriter's L; the script l appears only in the text.")

add(251, "byline",
    "par J.P, JOUANOLOU: no hyphen between the initials, surname in capitals",
    r"par J.-P. Jouanolou", "word", "high",
    {"old": r"par J.-P. Jouanolou", "new": r"par J.P. JOUANOLOU"},
    "As the byline of Exposé V on p. 204 (logged 'par J.P. JOUANOLOU'). The mark after P is the next item.")

add(251, "byline, after the P of 'J.P'",
    "a comma: 'J.P, JOUANOLOU' (ring with a descending tail, as the comma of 'l'exposé,' below; the stop after J "
    "has no tail)",
    r"J.P. (after the byline fix above)", "misprint_in_print", "medium",
    {"old": r"J.P. JOUANOLOU", "new": r"J.P, JOUANOLOU"},
    "Typing error, comma for full stop; the TeX silently gives the stop. 'old' is the text after the byline fix "
    "above (listed first). Drop this item if the mark is read as a stop.",
    corrected=r"J.P. JOUANOLOU")

add(251, "Définition 1.1.1, the defined term",
    "'faisceau' and '-adique constructible' underlined (the hand-drawn l is not)",
    r"On appelle faisceau \(\ell\)-adique constructible sur", "underline", "high",
    {"old": r"On appelle faisceau \(\ell\)-adique constructible sur",
     "new": r"On appelle \emph{faisceau} \(\ell\)-\emph{adique constructible} sur"},
    "The file's command for the underline (\\emph, as Exposé V and '\\emph{Preuve}').")

add(251, "'il suffit que F_o soit constructible.'",
    "'constructible' underlined",
    r"soit constructible. En effet", "underline", "high",
    {"old": r"soit constructible. En effet", "new": r"soit \emph{constructible}. En effet"},
    "")

add(251, "'En effet, l'assertion est locale et résulte dans le cas noethérien de (V 5.1.2).'",
    "no commas around 'dans le cas noethérien'",
    r"résulte, dans le cas noethérien, de", "punctuation", "high",
    {"old": r"résulte, dans le cas noethérien, de", "new": r"résulte dans le cas noethérien de"},
    "The TeX adds two commas.")

add(251, "'la sous-catégorie pleine de Hom(N°, Abc(X))'",
    "Hom underlined (the functor category)",
    r"\Hom(\mathbb N^{\circ},\Abc(X))", "underline", "high",
    {"old": r"\Hom(\mathbb N^{\circ},\Abc(X))", "new": r"\uHom(\mathbb N^{\circ},\Abc(X))"},
    "As the logged \\uHom(\\NN^\\circ,...) of Exposé V.")

# ---------------------------------------------------------------- p. 252
add(252, "top of the page: 'l-adiques constructibles.'",
    "p. 252 begins '\u2113-adiques constructibles. Avec les notations de Exp. V :'; p. 251 ends 'engendrée par les "
    "faisceaux'",
    "'\\(\\ell\\)-' ends the last line of page_251.tex (s5.tex line 8491 diplomatic, 8490 current); page_252.tex begins "
    "'adiques constructibles.'",
    "marker", "high", None,
    "Page 252 really begins with '\\(\\ell\\)-adiques'. Exact fix: python -I marker_split_word.py 5 252 pull "
    "'\\(\\ell\\)-' (simulated in memory on both layers: the line before the marker then ends 'engendrée par les faisceaux' and the "
    "line after the marker begins '\\(\\ell\\)-adiques constructibles.', which also removes the space the line "
    "break now prints after the hyphen). Independent of the \\uHom fix on the same line of p. 251. Text not moved.")

add(252, "'Avec les notations de Exp. V :'",
    "Exp. V (abbreviated, no article)",
    r"de l'Exposé V:", "word", "high",
    {"old": r"de l'Exposé V:", "new": r"de Exp. V:"},
    "The TeX writes the abbreviation out.")

add(252, "'s'identifie clairement à la catégorie notée (lZ)-adn(Ab(X)) dans Exp. V.'",
    "dans Exp. V.",
    r"dans l'Exposé V.", "word", "high",
    {"old": r"dans l'Exposé V.", "new": r"dans Exp. V."},
    "The TeX writes the abbreviation out.")

add(252, "Proposition 1.1.2, 'un objet de la catégorie Hom(N°, Ab(X))'",
    "Hom underlined",
    r"\Hom(\mathbb N^\circ,\Ab(X))", "underline", "high",
    {"old": r"\Hom(\mathbb N^\circ,\Ab(X))", "new": r"\uHom(\mathbb N^\circ,\Ab(X))"},
    "")

add(252, "end of the page: '... possède un noyau et un conoyau.' / p. 253 'En ce qui concerne le conoyau'",
    "no paragraph break: p. 253 begins flush left ('En ce qui concerne' is not indented; the paragraphs of the "
    "exposé begin with a deep indent)",
    "a blank line after 'conoyau.' ends page_252.tex", "other", "medium",
    {"old": L(r"un noyau et un conoyau.", "", ""), "new": L(r"un noyau et un conoyau.", "")},
    "Paragraph break added by the TeX; drop it if paragraphing is left to a global pass. The marker line then "
    "follows 'conoyau.' directly.")

# ---------------------------------------------------------------- p. 253
add(253, "'on sait que la restriction de u à V'",
    "no comma after V (the display follows)",
    r"à \(V\),", "punctuation", "high",
    {"old": L(r"de \(u\) à \(V\),", r"\["), "new": L(r"de \(u\) à \(V\)", r"\[")},
    "The TeX adds a comma.")

add(253, "display u_V: F_V -> G_V",
    "no punctuation after G_V",
    r"u_V:F_V\longrightarrow G_V,", "punctuation", "high",
    {"old": L(r"\longrightarrow G_V,", r"\]"), "new": L(r"\longrightarrow G_V", r"\]")},
    "The TeX adds a comma at the end of the display.")

add(253, "'Si K est le noyau de u_V dans la catégorie Hom(N°, Ab(V))'",
    "Hom underlined",
    r"\Hom(\mathbb N^\circ,\Ab(V))", "underline", "high",
    {"old": r"\Hom(\mathbb N^\circ,\Ab(V))", "new": r"\uHom(\mathbb N^\circ,\Ab(V))"},
    "")

add(253, "'Soit alors (V_i)_{i in I} un recouvrement'",
    "new paragraph (indented) after '... est un noyau pour u_W .'",
    r"pour \(u_W\). Soit alors", "other", "high",
    {"old": r"pour \(u_W\). Soit alors", "new": L(r"pour \(u_W\).", "", r"Soit alors")},
    "Paragraph break dropped by the TeX.")

add(253, "numbered paragraph 1.1.4",
    "1.1.4. (with a full stop)",
    r"\subsubsection*{1.1.4}", "punctuation", "high",
    {"old": r"\subsubsection*{1.1.4}", "new": r"\subsubsection*{1.1.4.}"},
    "As the logged '1.1.' of p. 140 and '5.3.' of p. 165.")

# ---------------------------------------------------------------- p. 254
add(254, "'Ceci montre que l-adc(X) est canoniquement munie d'une structure de Z_l-catégorie abélienne.'",
    "'est canoniquement munie d'une structure de' and '-catégorie abélienne' underlined (not Z_l, not the stop)",
    r"est canoniquement munie d'une structure de \(\mathbb Z_\ell\)-catégorie abélienne.", "underline", "high",
    {"old": r"est canoniquement munie d'une structure de \(\mathbb Z_\ell\)-catégorie abélienne.",
     "new": r"\emph{est canoniquement munie d'une structure de} \(\mathbb Z_\ell\)-\emph{catégorie abélienne}."},
    "")

add(254, "label 'Terminologie :'",
    "'Terminologie :' (underlined word, then a colon; no full stop)",
    "\\begin{statement}{Terminologie} (prints 'Terminologie.')", "punctuation", "medium",
    {"old": L(r"\begin{statement}{Terminologie}",
              r"On appellera dans la suite \(\mathbb Z_\ell\)-faisceaux constructibles les faisceaux "
              r"\(\ell\)-adiques constructibles.",
              r"\end{statement}"),
     "new": r"\emph{Terminologie} : On appellera dans la suite \(\mathbb Z_\ell\)-faisceaux constructibles les "
            r"faisceaux \(\ell\)-adiques constructibles."},
    "The statement environment of Exposé VI adds a full stop after its label; the print has ' :', as "
    "'\\emph{Preuve} :' and the logged '\\emph{Exemples} :' of p. 228. One edit (environment and label together). "
    "Medium only for the form of the label.")

add(254, "underlined title 1.2.",
    "'1.2. Z_l-faisceaux constants tordus constructibles.' ends with a full stop",
    r"\subsubsection*{1.2. \(\mathbb Z_\ell\)-faisceaux constants tordus constructibles}", "punctuation", "high",
    {"old": r"tordus constructibles}", "new": r"tordus constructibles.}"},
    "Underlined title: the full stop dropped.")

add(254, "Définition 1.2.1, 'est dit constant tordu si et seulement si'",
    "'constant tordu' underlined",
    r"est dit constant tordu", "underline", "high",
    {"old": r"est dit constant tordu", "new": r"est dit \emph{constant tordu}"},
    "")

# ---------------------------------------------------------------- p. 255
add(255, "'Se ramenant pour chaque entier n ...'",
    "new paragraph (indented) after the display Z_l(1) = (mu_{l^{n+1}})_{n in N} .",
    "'\\]' then 'Se ramenant' on the next line, no blank line", "other", "high",
    {"old": L(r"\]", r"Se ramenant"), "new": L(r"\]", "", r"Se ramenant")},
    "Paragraph break dropped by the TeX.")

add(255, "'on constate que le système projectif Z_l(1) est l-adique.'",
    "'adique' underlined (after the hand-drawn l)",
    r"est \(\ell\)-adique.", "underline", "high",
    {"old": r"est \(\ell\)-adique.", "new": r"est \(\ell\)-\emph{adique}."},
    "")

add(255, "'En effet K' contiendrait pour tout entier n une racine primitive'",
    "'pour tout entier n' underlined",
    r"contiendrait pour tout entier \(n\)", "underline", "high",
    {"old": r"contiendrait pour tout entier \(n\)", "new": r"contiendrait \emph{pour tout entier} \(n\)"},
    "The underline runs under the n as well; math kept outside \\emph as in the file.")

add(255, "'une racine primitive l^n-ème de l'unité'",
    "-ème",
    r"\(\ell^n\)-ième", "word", "high",
    {"old": r"\(\ell^n\)-ième", "new": r"\(\ell^n\)-ème"},
    "")

add(255, "Rappels 1.2.3: 'X-groupe abélien. Soit maintenant X un préschéma localement noethérien connexe.'",
    "one paragraph: 'Soit maintenant X ...' runs on in the line of 'X-groupe abélien.' and the paragraph of "
    "Rappels 1.2.3 continues to the display F_a: R_X -> Ensf ,",
    "\\end{statement} after 'abélien.' and a new paragraph 'Soit maintenant'", "other", "medium",
    {"old": L(r"\begin{statement}{Rappels 1.2.3}", r"(SGA 1 V 7)."), "new": r"\textbf{Rappels 1.2.3.} (SGA 1 V 7)."},
    "Pair R with the next item (apply both or neither): the label keeps the environment's bold 'Rappels 1.2.3.', "
    "the environment is dropped so that the paragraph runs on. Drop the pair if paragraphing is left to a "
    "global pass.")

add(255, "same place, end of the statement environment",
    "no break before 'Soit maintenant'",
    "'abélien.', '\\end{statement}', a blank line, 'Soit maintenant'", "other", "medium",
    {"old": L(r"abélien.", r"\end{statement}", "", r"Soit maintenant"), "new": r"abélien. Soit maintenant"},
    "Pair R with the previous item (apply both or neither).")

add(255, "Rappels 1.2.3, 'revêtements étales de T munis d'une structure de X-groupe abélien'",
    "X-groupe abélien (a typed X; the sentence is about a préschéma T)",
    r"\(X\)-groupe abélien", "misprint_in_print", "medium",
    None,
    "Wrong letter: the étale coverings and the sheaves are on T, so the group structure is over T. The TeX keeps "
    "the printed X.",
    corrected=r"\(T\)-groupe abélien")

add(255, "'Soit maintenant X un préschéma localement noethérien connexe.'",
    "'connexe' underlined",
    r"noethérien connexe.", "underline", "high",
    {"old": r"noethérien connexe.", "new": r"noethérien \emph{connexe}."},
    "")

add(255, "'soit F_a le foncteur :'",
    "colon after 'foncteur' (before the display)",
    r"le foncteur", "punctuation", "high",
    {"old": L(r"le foncteur", r"\["), "new": L(r"le foncteur:", r"\[")},
    "The TeX drops the colon.")

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(F), "findings written")
