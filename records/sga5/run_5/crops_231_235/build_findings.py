"""Build findings_231_235.json (SGA 5, Exposé V, pp. 231-235) and check every fix against its page file:
fixes are applied in list order; each "old" must occur exactly once in the text at that point, never contain a
marker line; non-misprint "old" strings must also occur exactly once in the original page file."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
BATCH = HERE.parent / "b231_235"
OUT = HERE.parent / "findings_231_235.json"
N = "\n"

F = []


def add(page, where, scan, tex, kind, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


UL = "Exposé V: the TeX has no underline markup; \\emph as on pp. 204-205 and in III B."

# ---------------------------------------------------------------- p. 231
add(231, "top of the page",
    "p. 231 begins 'Il montre l'existence d'un isomorphisme canonique entre'; p. 230 ends with the diagram (last row 0  0)",
    "'Il' (s5.tex line 7739 diplomatic, 7738 current) is the last line of page_230.tex, just above the folio-231 marker; page_231.tex begins 'montre l'existence'",
    "marker", "high", None, None,
    "Page 231 really begins with the word 'Il' on the line above the marker. Exact fix: python -I move_marker.py 5 231 'Il' --before "
    "(simulated in memory on both layers: the marker then stands between '\\]' and 'Il'). Text not moved.")
add(231, "end of the proof of 4.2.5 (begun on p. 230), after 'l'assertion (ii) .'",
    "no end mark; the next line is the label THEOREME 4.2.6.",
    "\\end{prooftext}", "extra", "high",
    r"(ii)." + N + r"\end{prooftext}", r"(ii).",
    "Goes with the p. 230 fix of this proof's label: page_230.tex '\\begin{prooftext}' prints 'Proof.' where the print has "
    "'Preuve :' ('Preuve' underlined), i.e. '\\emph{Preuve} : ' as on pp. 38-39. Apply both or neither (LaTeX fails otherwise).")
add(231, "Théorème 4.2.6, title",
    "'(Lemme d'Artin-Rees) .': the title in parentheses, underlined together with them, then ' .'",
    "Lemme d'Artin-Rees.", "punctuation", "high",
    r"Lemme d'Artin-Rees.", r"\emph{(Lemme d'Artin-Rees)}.",
    "The TeX drops the parentheses; one edit with the underline.")
add(231, "Théorème 4.2.6, 'Soit X un système projectif indexé par'",
    "underlined: 'Soit', 'un système projectif indexé' / 'par'; not X",
    "no underline markup", "underline", "high",
    r"Soit \(X\) un système projectif indexé par",
    r"\emph{Soit} \(X\) \emph{un système projectif indexé par}", UL)
add(231, "Théorème 4.2.6, 'par N à valeurs dans C'",
    "no comma after N",
    r"\(\mathbb N\), à valeurs", "punctuation", "high",
    r"\(\mathbb N\),", r"\(\mathbb N\)", "The TeX adds a comma.")
add(231, "Théorème 4.2.6, 'à valeurs dans C . On suppose que :'",
    "underlined: 'à valeurs dans', 'On suppose que'; not C, the stop, the colon",
    "no underline markup", "underline", "high",
    r"à valeurs dans \(\mathcal C\). On suppose que:",
    r"\emph{à valeurs dans} \(\mathcal C\). \emph{On suppose que}:", "")
add(231, "Théorème 4.2.6 (i)", "'vérifie' underlined", "no underline markup", "underline", "high",
    r"vérifie", r"\emph{vérifie}", "")
add(231, "Théorème 4.2.6 (i), end", "'(MLAR) ,': a comma", "(MLAR);", "punctuation", "high",
    r"(MLAR);", r"(MLAR),", "")
add(231, "Théorème 4.2.6 (ii)", "'est adapté à' underlined; not X, J", "no underline markup", "underline", "high",
    r"\item \(X\) est adapté à", r"\item \(X\) \emph{est adapté à}", "")
add(231, "Théorème 4.2.6 (ii), end", "'J ,': a comma", r"\(J\);", "punctuation", "high",
    r"\(J\);", r"\(J\),", "")
add(231, "Théorème 4.2.6 (iii), first line",
    "underlined: 'est un', '-module gradué de type fini, i.e.' / 'pour toute suite croissante'; not grs(X), (gr_J(A),C)",
    "no underline markup", "underline", "high",
    r"est un \((\gr_J(A),\mathcal C)\)-module gradué de type fini, i.e. pour toute suite croissante",
    r"\emph{est un} \((\gr_J(A),\mathcal C)\)-\emph{module gradué de type fini, i.e. pour toute suite croissante}", "")
add(231, "Théorème 4.2.6 (iii), 'de sous-'",
    "'de sous-' underlined; not (M_n)_{n∈N}", "no underline markup", "underline", "high",
    r"\((M_n)_{n\in\mathbb N}\) de sous-", r"\((M_n)_{n\in\mathbb N}\) \emph{de sous-}", "")
add(231, "Théorème 4.2.6 (iii), 'sous-(gr_J(A)-modules gradués'",
    "'sous-(gr_J(A)-modules': a parenthesis opens before gr and only the one of (A) closes (clear at 2.5x)",
    r"sous-\((\gr_J(A))\)-modules", "misprint_in_print", "high",
    r"(\gr_J(A))\)", r"(\gr_J(A)\)",
    "Unbalanced parenthesis in the print; the TeX silently adds the closing one. The fix restores the printed reading "
    "(diplomatic layer only). Corrected as the TeX; the sense may be 'sous-(gr_J(A),C)-modules' as in the line above.",
    corrected=r"(\gr_J(A))\)")
add(231, "Théorème 4.2.6 (iii), 'modules gradués de grs(X) dont grs(X) est réunion, il existe un entier p tel que'",
    "underlined: '-modules gradués' / 'de', 'dont', 'est réunion, il existe un entier', 'tel que'; not grs(X), p",
    "no underline markup", "underline", "high",
    r"-modules gradués de \(\grs(X)\) dont \(\grs(X)\) est réunion, il existe un entier \(p\) tel que",
    r"-\emph{modules gradués de} \(\grs(X)\) \emph{dont} \(\grs(X)\) \emph{est réunion, il existe un entier} \(p\) \emph{tel que}",
    "")
add(231, "Théorème 4.2.6, 'Alors X est AR-J-adique.'",
    "underlined: 'Alors', 'est', 'adique.' (the line runs under the stop); not X, AR-J-",
    "no underline markup", "underline", "high",
    r"Alors \(X\) est AR-\(J\)-adique.", r"\emph{Alors} \(X\) \emph{est} AR-\(J\)-\emph{adique.}", "")
add(231, "proof of 4.2.6, label",
    "'Preuve : Rappelons': 'Preuve' underlined, then ' :', run into the text",
    "\\begin{prooftext} (the Exposé V environment, s5.tex line 6859, prints its default label: italic 'Proof.')",
    "other", "high",
    r"\begin{prooftext}" + N + r"Rappelons", r"\emph{Preuve} : Rappelons",
    "Same form as the global '\\emph{Preuve} :'. Apply together with the removal of its \\end{prooftext} (before Lemme 4.2.7, below).")
add(231, "proof of 4.2.6, 'on a posé :'", "a colon before the display", "on a posé", "punctuation", "high",
    r"on a posé", r"on a posé :", "")
add(231, "proof of 4.2.6, 'Supposons prouvé le lemme suivant'",
    "'Supposons prouvé ...' begins a new, indented paragraph", "run on after 'AR-\\(J\\)-adique.'", "other", "high",
    r"AR-\(J\)-adique. Supposons", r"AR-\(J\)-adique." + N + N + r"Supposons", "Paragraph break.")
add(231, "proof of 4.2.6, 'le lemme suivant :'", "a colon", "le lemme suivant.", "punctuation", "high",
    r"le lemme suivant.", r"le lemme suivant :", "")
add(231, "end of the first part of the proof of 4.2.6",
    "no end mark (LEMME 4.2.7. follows)", "\\end{prooftext}", "extra", "high",
    r"\end{prooftext}" + N + N + r"\begin{statement}{Lemme 4.2.7}", N + r"\begin{statement}{Lemme 4.2.7}",
    "Apply together with the label fix '\\emph{Preuve} : Rappelons' above.")
add(231, "Lemme 4.2.7, first sentence",
    "underlined: 'Soit', 'un système projectif strict adapté à', 'Pour tout' / 'entier'; not X, J, s, the stop, the comma",
    "no underline markup", "underline", "high",
    r"Soit \(X\) un système projectif strict adapté à \(J\). Pour tout entier \(s\),",
    r"\emph{Soit} \(X\) \emph{un système projectif strict adapté à} \(J\). \emph{Pour tout entier} \(s\),", "")
add(231, "Lemme 4.2.7, 'le sous objet gradué'", "'le sous objet gradué' underlined", "no underline markup",
    "underline", "high", r"le sous-objet gradué", r"\emph{le sous-objet gradué}",
    "Listed before the misprint fix of the same words.")
add(231, "Lemme 4.2.7, 'sous objet'", "'le sous objet gradué': no hyphen (clear at 3x)", "sous-objet",
    "misprint_in_print", "high", r"\emph{le sous-objet", r"\emph{le sous objet",
    "Missing hyphen; the TeX silently corrects. 'old' taken from the text after the underline fix above. The fix restores "
    "the printed reading (diplomatic layer only).",
    corrected=r"\emph{le sous-objet")
add(231, "Lemme 4.2.7, '[(M_s)_n]_{n∈N}'", "square brackets: '[(M_s)_n]_{n∈N}'",
    r"\bigl((M_s)_n\bigr)_{n\in\mathbb N}", "symbol", "high",
    r"\bigl((M_s)_n\bigr)_{n\in\mathbb N}", r"[(M_s)_n]_{n\in\mathbb N}", "The TeX writes parentheses for the brackets.")
add(231, "Lemme 4.2.7, 'de grs(X) défini par les égalités ci-dessous :'",
    "underlined: 'de', 'défini par les' / 'égalités ci-dessous'; not grs(X), the colon",
    "no underline markup", "underline", "high",
    r"de \(\grs(X)\) défini par les égalités ci-dessous:",
    r"\emph{de} \(\grs(X)\) \emph{défini par les égalités ci-dessous}:", "")

# ---------------------------------------------------------------- p. 232
add(232, "Lemme 4.2.7, 'est un sous'", "'est un sous' underlined", "no underline markup", "underline", "high",
    r"est un" + N + r"sous", r"\emph{est un" + N + r"sous}", UL)
add(232, "Lemme 4.2.7, 'sous gr_J(A)-module'", "'est un sous  gr_J(A)-module': space, no hyphen (clear at 2x)",
    r"sous-\(\gr_J(A)\)-module", "misprint_in_print", "high",
    r"-\(\gr_J(A)\)", r" \(\gr_J(A)\)",
    "Missing hyphen; the TeX silently corrects. The fix restores the printed reading (diplomatic layer only).",
    corrected=r"-\(\gr_J(A)\)")
add(232, "Lemme 4.2.7, '-module gradué de grs(X) .'", "'-module gradué de' underlined; not gr_J(A), grs(X), the stop",
    "no underline markup", "underline", "high",
    r"-module gradué de \(\grs(X)\)", r"-\emph{module gradué de} \(\grs(X)\)", "")
add(232, "proof label of Lemme 4.2.7",
    "'Démonstration de 4.2.7. Reprenons': only 'Démonstration de' underlined, '4.2.7.' plain, run into the text",
    "\\begin{prooftext}[Démonstration de 4.2.7] (prints the whole label in italics: '\\emph{Démonstration de 4.2.7.}')",
    "other", "high",
    r"\begin{prooftext}[Démonstration de 4.2.7]" + N, r"\emph{Démonstration de} 4.2.7. ",
    "Proof label of another form than 'Preuve :'. Apply together with the removal of '\\end{prooftext}' after 'D'où le lemme.' (below).")
add(232, "proof of 4.2.7, the image displayed after 'est'",
    "'J^p/J^{p+1}⊗_A[(J^{q-s}X_{p+q} ∩ F^q(X_{p+q})) + F^{q+1}(X_{p+q})]/F^{q+1}(X_{p+q}) .': square brackets and a slash on one line",
    "\\frac{(J^{q-s}X_{p+q}\\cap F^q(X_{p+q}))+F^{q+1}(X_{p+q})}{F^{q+1}(X_{p+q})}.", "formula", "high",
    r"\frac{(J^{q-s}X_{p+q}\cap F^q(X_{p+q}))+F^{q+1}(X_{p+q})}" + N + r"     {F^{q+1}(X_{p+q})}.",
    r"[(J^{q-s}X_{p+q}\cap F^q(X_{p+q}))+F^{q+1}(X_{p+q})]/F^{q+1}(X_{p+q}).",
    "The TeX builds a fraction and drops the brackets.")
add(232, "proof of 4.2.7, 'On en déduit que l'image réciproque'",
    "'On en déduit ...' begins a new, indented paragraph", "run on after 'sur \\(J^{q-s}X_q\\).'", "other", "high",
    r"\(J^{q-s}X_q\). On en déduit", r"\(J^{q-s}X_q\)." + N + N + r"On en déduit", "Paragraph break.")
add(232, "proof of 4.2.7, 'Il est maintenant clair'",
    "'Il est maintenant clair ...' begins a new, indented paragraph", "continues the paragraph after the display",
    "other", "high",
    r"\]" + N + r"Il est maintenant clair", r"\]" + N + N + r"Il est maintenant clair", "Paragraph break.")
add(232, "end of the proof of 4.2.7", "no end mark after 'D'où le lemme.'", "\\end{prooftext}", "extra", "high",
    r"D'où le lemme." + N + r"\end{prooftext}", r"D'où le lemme.",
    "Apply together with the label fix '\\emph{Démonstration de} 4.2.7. ' above.")

# ---------------------------------------------------------------- p. 233
add(233, "heading 5", "'5. Systèmes projectifs J-adiques et AR-J-adiques noethériens.' with a full stop (title underlined)",
    "\\subsection*{5. Systèmes projectifs \\(J\\)-adiques et AR-\\(J\\)-adiques noethériens}", "punctuation", "high",
    r"AR-\(J\)-adiques noethériens}", r"AR-\(J\)-adiques noethériens.}", "Underlined title: the print's full stop.")
add(233, "§5, first sentence, 'un idéal J de A et une A-catégorie'", "no comma after 'de A'",
    r"de \(A\), et une", "punctuation", "high", r"de \(A\), et une", r"de \(A\) et une", "The TeX adds a comma.")
add(233, "heading 5.1", "'5.1. Généralités.' with a full stop (title underlined)",
    "\\subsubsection*{5.1. Généralités}", "punctuation", "high",
    r"\subsubsection*{5.1. Généralités}", r"\subsubsection*{5.1. Généralités.}", "Underlined title: the print's full stop.")
add(233, "Définition 5.1.1, first line and a half",
    "underlined: 'Un objet', 'de la catégorie', 'Hom' (alone, not '(N°,C)'), 'est dit', 'adique' / 'noethérien (resp. artinien) s'il est'; not X, J-",
    "no underline markup; \\Hom plain", "underline", "high",
    r"Un objet \(X\) de la catégorie \(\Hom(\mathbb N^\circ,\mathcal C)\) est dit \(J\)-adique noethérien (resp. artinien) s'il est",
    r"\emph{Un objet} \(X\) \emph{de la catégorie} \(\uHom(\mathbb N^\circ,\mathcal C)\) \emph{est dit} \(J\)-\emph{adique noethérien (resp. artinien) s'il est}",
    UL + " The underlined Hom is \\uHom (preamble).")
add(233, "Définition 5.1.1, rest",
    "underlined: 'adique et si ses composantes sont des' / 'objets noethériens (resp. artiniens) de la catégorie'; not J-, C, the stop",
    "no underline markup", "underline", "high",
    r"\(J\)-adique et si ses composantes sont des objets noethériens (resp. artiniens) de la catégorie \(\mathcal C\).",
    r"\(J\)-\emph{adique et si ses composantes sont des objets noethériens (resp. artiniens) de la catégorie} \(\mathcal C\).", "")
add(233, "'la sous-catégorie pleine de P = Hom(N°,C)'", "'de' at the start of the line is underlined (clear at 2x)",
    "no underline markup", "underline", "medium",
    r"pleine de" + N, r"pleine \emph{de}" + N,
    "A lone underline outside a statement; probably a slip of the typist, but printed.")
add(233, "'P = Hom(N°,C)'", "P is a typed plain capital P (as in Prop. 5.1.2)", r"\(\mathcal P=", "font", "high",
    r"\(\mathcal P=", r"\(P=", "The TeX writes a script P; elsewhere in Exposé V it writes plain $P$ (s5.tex lines 7254, 7283).")
add(233, "'P = Hom(N°,C)', Hom", "'Hom' underlined", r"\Hom(\mathbb N^\circ,\mathcal C)\) dont", "underline", "high",
    r"\Hom(\mathbb N^\circ,\mathcal C)\) dont", r"\uHom(\mathbb N^\circ,\mathcal C)\) dont", "\\uHom as in the preamble.")
add(233, "'noethériens (resp. artiniens) , est du même type'", "a comma before 'est du même type'",
    "(resp. artiniens) est du même type", "punctuation", "high",
    r"(resp. artiniens) est du même type", r"(resp. artiniens), est du même type", "The TeX drops the comma.")
add(233, "Proposition 5.1.2, 'Soit X un objet J-adique de P'",
    "underlined: 'Soit', 'un objet', 'adique de'; not X, J-, P", "no underline markup", "underline", "high",
    r"Soit \(X\) un objet \(J\)-adique de", r"\emph{Soit} \(X\) \emph{un objet} \(J\)-\emph{adique de}", UL)
add(233, "Proposition 5.1.2, 'de P .'", "P is a typed plain capital P", r"\(\mathcal P\).", "font", "high",
    r"\(\mathcal P\).", r"\(P\).", "As 'P = Hom(N°,C)' above.")
add(233, "Proposition 5.1.2, from 'Pour que'",
    "underlined: 'Pour que', 'soit', 'adique noethérien (resp. artinien)', 'il faut et il suffit qu'il soit', 'adique et que', 'soit noethérien (resp. artinien)'; not X, J-, X_o, the comma, the stop",
    "no underline markup", "underline", "high",
    r"Pour que \(X\) soit \(J\)-adique noethérien (resp. artinien), il faut et il suffit qu'il soit \(J\)-adique et que \(X_0\) soit noethérien (resp. artinien).",
    r"\emph{Pour que} \(X\) \emph{soit} \(J\)-\emph{adique noethérien (resp. artinien)}, \emph{il faut et il suffit qu'il soit} \(J\)-\emph{adique et que} \(X_0\) \emph{soit noethérien (resp. artinien)}.",
    "")
add(233, "proof of Proposition 5.1.2, label",
    "no label: the proof is an indented paragraph 'Soit en effet X un système projectif ...'",
    "\\begin{prooftext} (prints the default label, italic 'Proof.')", "extra", "high",
    r"\begin{prooftext}" + N + r"Soit en effet", r"Soit en effet",
    "Apply together with the removal of its \\end{prooftext} (next finding).")
add(233, "end of the proof of 5.1.2", "no end mark", "\\end{prooftext}", "extra", "high",
    r"(resp. artiniens)." + N + r"\end{prooftext}", r"(resp. artiniens).",
    "Apply together with the previous finding.")

# ---------------------------------------------------------------- p. 234
add(234, "Définition 5.1.3, the statement",
    "underlined: 'Soit', 'un système projectif indexé par', 'à valeurs' / 'dans', 'On dit qu'il est', 'adique noethérien (resp. artinien) s'il est', 'adique,', 'et si ses composantes sont des objets noethériens (resp.' / 'artiniens' (not the closing parenthesis); not X, N, C, AR-J-, the stops",
    "no underline markup", "underline", "high",
    r"Soit \(X\) un système projectif indexé par \(\mathbb N\) à valeurs dans \(\mathcal C\). On dit qu'il est AR-\(J\)-adique noethérien (resp. artinien) s'il est AR-\(J\)-adique, et si ses composantes sont des objets noethériens (resp. artiniens).",
    r"\emph{Soit} \(X\) \emph{un système projectif indexé par} \(\mathbb N\) \emph{à valeurs dans} \(\mathcal C\). \emph{On dit qu'il est} AR-\(J\)-\emph{adique noethérien (resp. artinien) s'il est} AR-\(J\)-\emph{adique, et si ses composantes sont des objets noethériens (resp. artiniens}).",
    UL)
add(234, "'de Hom_AR(N°,C) (2.4)'", "'Hom' underlined (the subscript AR below the line)",
    r"\(\Hom_{\mathrm{AR}}", "underline", "high",
    r"\(\Hom_{\mathrm{AR}}", r"\(\uHom_{\mathrm{AR}}", "\\uHom as in the preamble.")
add(234, "first display, p^n_AR", "small p (with its descender): 'p^n_AR'", r"P^n_{\mathrm{AR}}", "symbol", "high",
    r"P^n_{\mathrm{AR}}", r"p^n_{\mathrm{AR}}",
    "Capital for small; the TeX writes $p_{AR}$ elsewhere in Exposé V (s5.tex line 7283).")
add(234, "first display, end", "no punctuation after 'AR-J-adn(C)'", "comma", "punctuation", "high",
    r"\text{-adn}(\mathcal C),", r"\text{-adn}(\mathcal C)", "The TeX adds a comma at the end of the display.")
add(234, "second display, p^f_AR", "small p: 'p^f_AR'", r"P^f_{\mathrm{AR}}", "symbol", "high",
    r"P^f_{\mathrm{AR}}", r"p^f_{\mathrm{AR}}", "")
add(234, "second display, end", "no punctuation after 'AR-J-adf(C)'", "comma", "punctuation", "high",
    r"\text{-adf}(\mathcal C),", r"\text{-adf}(\mathcal C)", "The TeX adds a comma at the end of the display.")
add(234, "'obtenus par restriction de p_AR(2.4)'", "small p: 'p_AR'", r"\(P_{\mathrm{AR}}\)", "symbol", "high",
    r"\(P_{\mathrm{AR}}\)", r"\(p_{\mathrm{AR}}\)", "")
add(234, "'p_AR(2.4) sont des équivalences'", "no comma after (2.4)", "(2.4), sont", "punctuation", "high",
    r"(2.4), sont des", r"(2.4) sont des", "The TeX adds a comma.")
add(234, "'les fonctions canoniques ... obtenus par restriction'",
    "'fonctions' (clear), with the masculine 'obtenus' and the equivalences of categories: the functors are meant",
    "les fonctions canoniques", "misprint_in_print", "medium", None, None,
    "The TeX keeps the printed reading.", corrected=r"les foncteurs canoniques")
add(234, "'du théorème de Hilbert :'", "a colon", "de Hilbert.", "punctuation", "high",
    r"théorème de Hilbert.", r"théorème de Hilbert :", "")
add(234, "Théorème 5.1.4, title and first line",
    "'(Théorème de Hilbert) . Soient A un anneau commutatif,': title in parentheses; one continuous underline from '(Théorème' to 'commutatif,'",
    "Théorème de Hilbert. Soient", "punctuation", "high",
    r"Théorème de Hilbert. Soient \(A\) un anneau commutatif,",
    r"\emph{(Théorème de Hilbert). Soient \(A\) un anneau commutatif,}",
    "The TeX drops the parentheses; one edit with the underline (the print underlines the whole line).")
add(234, "Théorème 5.1.4, 'C une A-catégorie abélienne, M un objet de type fini (resp. noethérien) de C'",
    "underlined: 'une', 'catégorie abélienne,', 'un objet de type fini (resp. noethérien)' / 'de'; not C, A-, M",
    "no underline markup", "underline", "high",
    r"\(\mathcal C\) une \(A\)-catégorie abélienne, \(M\) un objet de type fini (resp. noethérien) de",
    r"\(\mathcal C\) \emph{une} \(A\)-\emph{catégorie abélienne,} \(M\) \emph{un objet de type fini (resp. noethérien) de}", "")
add(234, "Théorème 5.1.4, 'Pour toute A-algèbre de type fini'",
    "'Pour toute ...' begins a new, indented paragraph; 'Pour toute A-algèbre de type fini' underlined in one line",
    "run on after 'de \\(\\mathcal C\\).'", "other", "high",
    r"\(\mathcal C\). Pour toute \(A\)-algèbre de type fini",
    r"\(\mathcal C\)." + N + N + r"\emph{Pour toute \(A\)-algèbre de type fini}",
    "Paragraph break; one edit with the underline.")
add(234, "Théorème 5.1.4, 'de type fini B graduée par N'", "no comma after B", r"\(B\), graduée", "punctuation", "high",
    r"\(B\),", r"\(B\)", "The TeX adds a comma.")
add(234, "Théorème 5.1.4, 'graduée par N , le (B,C)-module gradué'",
    "underlined: 'graduée par', 'le', 'module gradué'; not N, (B,C)-", "no underline markup", "underline", "high",
    r"graduée par \(\mathbb N\), le \((B,\mathcal C)\)-module gradué",
    r"\emph{graduée par} \(\mathbb N\), \emph{le} \((B,\mathcal C)\)-\emph{module gradué}", "")
add(234, "Théorème 5.1.4, 'est de type fini (resp. noethérien) .'",
    "underlined: 'est de type fini', '(resp. noethérien)'; not the stop", "no underline markup", "underline", "high",
    r"\]" + N + r"est de type fini (resp. noethérien).",
    r"\]" + N + r"\emph{est de type fini} \emph{(resp. noethérien)}.", "")
add(234, "Théorème 5.1.4, N.B.",
    "'(N.B. Si B = ...': a parenthesis opens before N.B. and is never closed (the line ends '(B_n⊗_A M)_{n∈N} .')",
    "N.B. Si", "misprint_in_print", "high", r"N.B.", r"(N.B.",
    "Unbalanced parenthesis; the TeX silently drops it. The fix restores the printed reading (diplomatic layer only). "
    "Corrected as the TeX, or close it after the last formula.",
    corrected=r"N.B.")
add(234, "Théorème 5.1.4, N.B., 'Si', 'désigne l'objet gradué'",
    "underlined: 'Si', 'désigne l'objet gradué'; not the formulas", "no underline markup", "underline", "high",
    r"Si \(B=\bigoplus_{n\ge0}B_n\), \(B\otimes_A M\) désigne l'objet gradué",
    r"\emph{Si} \(B=\bigoplus_{n\ge0}B_n\), \(B\otimes_A M\) \emph{désigne l'objet gradué}",
    "The sum sign is an overstrike (a circle with both + and x); the TeX's \\bigoplus is kept.")
add(234, "proof of Théorème 5.1.4, label",
    "'Preuve : On se ramène': 'Preuve' underlined, then ' :'",
    "\\begin{prooftext} (prints the default label, italic 'Proof.')", "other", "high",
    r"\begin{prooftext}" + N + r"On se ramène immédiatement", r"\emph{Preuve} : On se ramène immédiatement",
    "Apply together with the removal of its \\end{prooftext} on p. 235 (after 'dans les deux cas.').")
add(234, "proof of 5.1.4, 'une suite croissante :'", "a colon before the display", "une suite croissante",
    "punctuation", "high",
    r"une suite croissante" + N + r"\[", r"une suite croissante :" + N + r"\[", "")

# ---------------------------------------------------------------- p. 235
add(235, "'Supposons maintenant que M soit noetherien'", "'noetherien' without the accent (clear at 2.5x)",
    "noethérien", "misprint_in_print", "high", r"soit noethérien", r"soit noetherien",
    "The TeX silently corrects. The fix restores the printed reading (diplomatic layer only).",
    corrected=r"soit noethérien")
add(235, "display 'N_1 ⊂ N^2 ⊂ ...'", "the first term is N with a lowered 1 (N_1); the others carry upper indices",
    r"N_1\subset N^2", "misprint_in_print", "high", None, None,
    "The TeX keeps the printed reading.", corrected=r"N^1\subset N^2")
add(235, "'qui dans la première hypothèse (lorsque M est de type fini) a pour réunion'", "parentheses, no commas",
    "hypothèse, lorsque \\(M\\) est de type fini, a pour", "punctuation", "high",
    r"hypothèse, lorsque \(M\) est de type fini, a pour", r"hypothèse (lorsque \(M\) est de type fini) a pour",
    "The TeX writes commas for the parentheses.")
add(235, "the double-entry table, third row",
    "only N^1_1 in the first column; the second and third columns have vertical dots from that row down",
    r"N_1^1&&N_1^2&&N_1^p\\", "formula", "high",
    r"N_1^1&&N_1^2&&N_1^p\\", r"N_1^1&&\vdots&&\vdots\\", "The TeX adds N_1^2 and N_1^p.")
add(235, "the double-entry table, last rows",
    "'N^1_n ⊂ N^2_n ⊂ ...... ⊂ N^p_n ..........': no ⊂ after N^p_n and no full stop; then a last row ∩ ∩ ∩ under the three columns",
    r"N_n^p&\subset\cdots ." + " / no last row", "formula", "high",
    r"N_n^p&\subset\cdots ." + N + r"\end{array}",
    r"N_n^p&\cdots\\" + N + r"\cap&&\cap&&\cap" + N + r"\end{array}",
    "One edit: the TeX adds a ⊂ and a full stop and drops the last row of inclusion signs.")
add(235, "'Si p_1 est un entier ≥ p_o'", "'Si p_1 ...' begins a new, indented paragraph",
    "run on after '(resp. égal à \\(M\\)).'", "other", "high",
    r"(resp. égal à \(M\)). Si", r"(resp. égal à \(M\))." + N + N + r"Si", "Paragraph break.")
add(235, "end of the proof of Théorème 5.1.4", "no end mark", "\\end{prooftext}", "extra", "high",
    r"deux cas." + N + r"\end{prooftext}", r"deux cas.",
    "Apply together with the p. 234 label fix '\\emph{Preuve} : On se ramène immédiatement'.")
add(235, "Corollaire 5.1.5, up to 'de C'",
    "underlined: 'Supposons de plus que la catégorie', 'possède des sommes' / 'directes dénombrables. Alors pour tout objet', 'de type fini (resp. noethé-' / 'rien) de'; not C, M",
    "no underline markup", "underline", "high",
    r"Supposons de plus que la catégorie \(\mathcal C\) possède des sommes directes dénombrables. Alors pour tout objet \(M\) de type fini (resp. noethérien) de",
    r"\emph{Supposons de plus que la catégorie} \(\mathcal C\) \emph{possède des sommes directes dénombrables. Alors pour tout objet} \(M\) \emph{de type fini (resp. noethérien) de}",
    UL)
add(235, "Corollaire 5.1.5, 'de C et toute'", "no comma after C", r"\(\mathcal C\), et toute", "punctuation", "high",
    r"\(\mathcal C\),", r"\(\mathcal C\)", "The TeX adds a comma.")
add(235, "Corollaire 5.1.5, from 'et toute'",
    "underlined: 'et toute', 'algèbre de type fini', 'le', 'module', 'est de type fini (resp. noethérien)'; not A-, B, (B,C)-, B⊗_A M, the comma, the stop",
    "no underline markup", "underline", "high",
    r"et toute \(A\)-algèbre de type fini \(B\), le \((B,\mathcal C)\)-module \(B\otimes_A M\) est de type fini (resp. noethérien).",
    r"\emph{et toute} \(A\)-\emph{algèbre de type fini} \(B\), \emph{le} \((B,\mathcal C)\)-\emph{module} \(B\otimes_A M\) \emph{est de type fini (resp. noethérien)}.",
    "")
add(235, "proof of Corollaire 5.1.5, label",
    "'Preuve : On se ramène au cas où': 'Preuve' underlined, then ' :'",
    "\\begin{prooftext} (prints the default label, italic 'Proof.')", "other", "high",
    r"\begin{prooftext}" + N + r"On se ramène au cas où", r"\emph{Preuve} : On se ramène au cas où",
    "Its \\end{prooftext} is on p. 236 (page_236.tex: 'proposition suivante.\\n\\end{prooftext}' -> 'proposition suivante.'): "
    "apply both or neither (LaTeX fails otherwise).")
add(235, "proof of 5.1.5, '(considéré comme objet de C )'", "in parentheses, no comma",
    "\\(A[T]\\otimes_A M\\), considéré comme objet de \\(\\mathcal C\\).", "punctuation", "high",
    r"M\), considéré comme objet de \(\mathcal C\).", r"M\) (considéré comme objet de \(\mathcal C\)).",
    "The TeX writes a comma for the parentheses.")
add(235, "proof of 5.1.5, 'gr(N) est un sous (A[T],C)-module gradué'", "'sous (A[T],C)-module': space, no hyphen (clear at 2x)",
    r"est un sous-\((A[T],\mathcal C)\)-module", "misprint_in_print", "high",
    r"est un sous-\((", r"est un sous \((",
    "Missing hyphen; the TeX silently corrects. The fix restores the printed reading (diplomatic layer only).",
    corrected=r"est un sous-\((")

# ---------------------------------------------------------------- check
MARK = "%%%%%%%%%%"
ok = True
by_page = {}
for f in F:
    by_page.setdefault(f["page"], []).append(f)
for page, fs in by_page.items():
    orig = (BATCH / f"page_{page}.tex").read_text(encoding="utf-8")
    t = orig
    for f in fs:
        fx = f["fix"]
        if fx is None:
            if f["kind"] == "misprint_in_print" and f["tex"].split(" /")[0] not in orig:
                print("tex text not found", page, f["where"])
            continue
        old, new = fx["old"], fx["new"]
        if MARK in old:
            print("MARKER in old", page, f["where"]); ok = False
        c = t.count(old)
        if c != 1:
            print("NOT UNIQUE at application", page, c, repr(old[:60])); ok = False
        if f["kind"] != "misprint_in_print" and orig.count(old) != 1:
            print("not unique in original", page, repr(old[:60])); ok = False
        if f["kind"] == "misprint_in_print" and orig.count(old) != 1:
            print("note: misprint old taken from text after earlier fix:", page, repr(old[:40]))
        t = t.replace(old, new, 1)
    (HERE / f"applied_{page}.tex").write_text(t, encoding="utf-8", newline="\n")
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
counts = {}
for f in F:
    k = "m" if f["kind"] == "misprint_in_print" else "n"
    counts.setdefault(f["page"], {"n": 0, "m": 0})[k] += 1
print("ok" if ok else "PROBLEMS", len(F), counts)
