# Build findings_276_280.json; "¶" in old/new stands for a line break (LF).
import json
import re

RUN = r"C:/Users/user/Documents/sga_scan_check_20261105/run_5"
ROOT = r"C:/Users/user/Documents/sga_scan_check_20261105"
NL = "\n"


def fx(old, new):
    return {"old": old.replace("¶", NL), "new": new.replace("¶", NL)}


R_NOTE = ("The print's R is the typewriter's plain R; \\R is \\mathbb{R} in Exposé VI (renewed at the start of "
          "Exposé V, s5.tex l. 6860, not reset), as the logged fixes of pp. 274-275.")
HOM_NOTE = "\\uHom (the file's \\underline{\\Hom}), as the logged \\uHom fixes of Exposés V and VI (pp. 251-274)."

F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- p. 276 ----------------
add(276, "'Associant à tout objet F de Hom(N°, Ab(X)) la suite spectrale'", "Hom underlined", "\\Hom",
    "underline", "high", fx(r"Associant à tout objet \(F\) de \(\Hom", r"Associant à tout objet \(F\) de \(\uHom"),
    HOM_NOTE)
add(276, "'la suite spectrale de LERAY ordinaire'", "LERAY in capitals", "Leray", "word", "high",
    fx("de Leray ordinaire", "de LERAY ordinaire"),
    "The name in capitals, as the logged LERAY of p. 275 and SERRE of p. 259.")
add(276, "display (S)", "R^i_! g (R^j_! f (F)) => R^{i+j}_! (gof) (F) : three plain typed R",
    "\\R (\\mathbb{R}) three times", "font", "high",
    fx(r"\R^i_! g(\R^j_! f(F))\Longrightarrow \R^{i+j}_!",
       r"\mathrm{R}^i_! g(\mathrm{R}^j_! f(F))\Longrightarrow \mathrm{R}^{i+j}_!"), R_NOTE)
add(276, "display 'Hom(N°,Ab(X)) --> Sp(Hom(N°, Ab(Z))) ,'", "both Hom underlined", "\\Hom twice", "underline",
    "high", fx(r"\Hom(\mathbb N^\circ,\Ab(X))\longrightarrow \Sp(\Hom(",
               r"\uHom(\mathbb N^\circ,\Ab(X))\longrightarrow \Sp(\uHom("), HOM_NOTE)
add(276, "'U(Z) est épaisse dans Hom(N°,Ab(Z)), un foncteur'", "Hom underlined", "\\Hom", "underline", "high",
    fx(r"épaisse dans \(\Hom", r"épaisse dans \(\uHom"), HOM_NOTE)
add(276, "'un foncteur :' before display (1)", "un foncteur :", "un foncteur", "punctuation", "high",
    fx(r"un foncteur¶\[¶U(X)", r"un foncteur:¶\[¶U(X)"),
    "The TeX drops the colon; written without a space as the logged 'un foncteur:' of p. 272.")
add(276, "'on déduit de (1) un foncteur additif :'", "un foncteur additif :", "un foncteur additif", "punctuation",
    "high", fx("un foncteur additif", "un foncteur additif:"), "The TeX drops the colon.")
add(276, "'Pour tout objet F de Hom (N°,Ab(X)), la suite spectrale (S)'", "Hom underlined", "\\Hom", "underline",
    "high", fx(r"Pour tout objet \(F\) de \(\Hom", r"Pour tout objet \(F\) de \(\uHom"), HOM_NOTE)
add(276, "'Ceci montre que pour tout objet de U(X), la'", "no comma after 'que'", "Ceci montre que, pour tout",
    "punctuation", "high", fx("Ceci montre que, pour tout", "Ceci montre que pour tout"), "Comma added by the TeX.")

# ---------------- p. 277 ----------------
SPLIT = ("One of three edits for this display (first R, '(\\R^j_!', '\\Longrightarrow \\R^{i+j}_!'), split so that "
         "none contains the interchanged f and g: the corrected layer reads g(...f...) there and the edits replay "
         "on it unchanged. ")
add(277, "display 'R^i_! f(R^j_! g(F)) => R^{i+j}_! (gof)(F) .', first R", "plain typed R", "\\R (\\mathbb{R})",
    "font", "high", fx(r"birégulière:¶\[¶\R^i_!", r"birégulière:¶\[¶\mathrm{R}^i_!"), SPLIT + R_NOTE)
add(277, "same display, second R", "plain typed R", "\\R (\\mathbb{R})", "font", "high",
    fx(r"(\R^j_!", r"(\mathrm{R}^j_!"), SPLIT + R_NOTE)
add(277, "same display, third R", "plain typed R", "\\R (\\mathbb{R})", "font", "high",
    fx(r"\Longrightarrow \R^{i+j}_!", r"\Longrightarrow \mathrm{R}^{i+j}_!"), SPLIT + R_NOTE)
add(277, "same display: 'R^i_! f(R^j_! g(F))'",
    "R^i_! f(R^j_! g(F)) => R^{i+j}_!(gof)(F): f and g interchanged on the left (f: X -> Y, g: Y -> Z, F on X)",
    "\\R^i_!f(\\R^j_!g(F)) (the printed reading)", "misprint_in_print", "high", None,
    "The TeX keeps the printed reading. (S) on p. 276 and Proposition 2.2.4 (p. 275) read R^i_! g(R^j_! f(F)); "
    "the corrected layer already reads g(...f...). The corrected reading is given with the R of the font edits above.",
    corrected=r"\mathrm{R}^i_!g(\mathrm{R}^j_!f(F))")
add(277, "underlined title 2.2.3.", "2.2.3. Autres propriétés.", "\\subsubsection*{2.2.3. Autres propriétés}",
    "punctuation", "high", fx("Autres propriétés}", "Autres propriétés.}"),
    "Underlined title: the TeX drops the print's final full stop.")
add(277, "item A)", "'A) Soit f: X --> Y un morphisme séparé ...': no title after 'A)'",
    "\\paragraph{A) Dimension cohomologique.}", "extra", "high",
    fx(r"\paragraph{A) Dimension cohomologique.}¶Soit", "A) Soit"),
    "The TeX adds a title the print does not have (only B) and C) have underlined titles); 'A)' as plain text.")
add(277, "'Alors pour tout (AR, Z_l)-faisceau constructible F,'", "no comma after 'Alors'", "Alors, pour tout",
    "punctuation", "high", fx("Alors, pour tout", "Alors pour tout"), "Comma added by the TeX.")
add(277, "display 'R^i_! f (F) = 0  pour i > 2d.'", "plain typed R", "\\R (\\mathbb{R})", "font", "high",
    fx(r"\R^i_!f(F)=0", r"\mathrm{R}^i_!f(F)=0"), R_NOTE)
add(277, "'(SGA 4 X 4.1. et 5.2.).'", "4.1. and 5.2. each with a full stop", "(SGA 4 X 4.1 et 5.2).", "punctuation",
    "high", fx("X 4.1 et 5.2)", "X 4.1. et 5.2.)"), "The TeX drops the two full stops of the references.")
add(277, "B) Changement de base propre: before the square", "the square follows the title directly, no text",
    "Considérons un carré cartésien", "extra", "high", fx(r"Considérons un carré cartésien¶\[", r"\["),
    "Sentence added by the TeX.")
add(277, "square of B), bottom arrow Y' --> Y", "label g above the arrow", "\\arrow[r,\"g\"'] (label below)", "other",
    "medium", fx("\\arrow[r,\"g\"']", "\\arrow[r,\"g\"]"),
    "Label position as in the print (as the logged label fixes of pp. 39, 57, 71).")
add(277, "square of B), bottom right corner", "Y with no full stop", "Y .", "punctuation", "high", fx("& Y .", "& Y"),
    "Full stop added by the TeX at the end of the diagram.")
add(277, "'Soit X' = X x_Y Y' (qui est localement noethérien puisque f est de type fini) et'",
    "the relative clause in parentheses", ", qui est ... de type fini, et", "punctuation", "high",
    fx(r"Y'\), qui est localement noethérien puisque \(f\) est de type fini, et",
       r"Y'\) (qui est localement noethérien puisque \(f\) est de type fini) et"),
    "The TeX replaces the print's parentheses by commas.")
add(277, "display 'w_i : g^*(R^i_! f(F)) --> R^i_! f'(g'^* F) .', first R", "plain typed R", "\\R (\\mathbb{R})",
    "font", "high", fx(r"g^*(\R^i_!f(F))", r"g^*(\mathrm{R}^i_!f(F))"), R_NOTE)
add(277, "same display, the arrow", "a plain long arrow, no ~ over it", "\\xrightarrow{\\sim}", "symbol", "high",
    fx(r"\xrightarrow{\sim}", r"\longrightarrow"), "The TeX adds the isomorphism sign.")
add(277, "same display, second R", "plain typed R", "\\R (\\mathbb{R})", "font", "high",
    fx(r"\R^i_!f'(g'^*F)", r"\mathrm{R}^i_!f'(g'^*F)"), R_NOTE)

# ---------------- p. 278 ----------------
add(278, "'De plus si 0 --> F' --> F --> F'' --> 0'", "no comma after 'De plus'", "De plus, si", "punctuation",
    "high", fx("plus, si", "plus si"), "Comma added by the TeX.")
add(278, "'(resp. (AR, Z_l)-fc(X) ), (w_i)_{i in N} commute aux opérateurs bords,'",
    "'(w_i)_{i in N} commute' (no article, singular verb)", "les (w_i)_{i in N} commutent", "word", "high",
    fx(r"les \((w_i)_{i\in\mathbb N}\) commutent", r"\((w_i)_{i\in\mathbb N}\) commute"),
    "The TeX adds 'les' and changes the verb to the plural.")
add(278, "'opérateurs bords, autrement dit les diagrammes ci-dessous'",
    "a comma after 'bords', no comma after 'dit'", "bords; autrement dit, les", "punctuation", "high",
    fx("bords; autrement dit, les", "bords, autrement dit les"), "")
add(278, "diagram, top row: g^*(R^i_! f(F'')) --> R^i_! f'(g'^* F'')", "plain typed R twice",
    "\\R (\\mathbb{R}) twice", "font", "high",
    fx(r"""g^*(\R^i_!f(F'')) \arrow[r,"w_i"] \arrow[d,"g^*(\delta)"']¶&¶\R^i_!f'(g'^*F'')""",
       r"""g^*(\mathrm{R}^i_!f(F'')) \arrow[r,"w_i"] \arrow[d,"g^*(\delta)"']¶&¶\mathrm{R}^i_!f'(g'^*F'')"""), R_NOTE)
add(278, "diagram, bottom left: g^*(R^{i+1}_! f(F'))", "plain typed R", "\\R (\\mathbb{R})", "font", "high",
    fx(r"g^*(\R^{i+1}_!f(F'))", r"g^*(\mathrm{R}^{i+1}_!f(F'))"), R_NOTE)
add(278, "diagram, bottom arrow", "label w_{i+1} above the arrow", "\\arrow[r,\"w_{i+1}\"'] (label below)", "other",
    "medium", fx("\\arrow[r,\"w_{i+1}\"']", "\\arrow[r,\"w_{i+1}\"]"),
    "Label position as in the print (w_i of the top arrow is above in both).")
add(278, "diagram, bottom right: R^{i+1}_! f'(g'^* F') .", "plain typed R", "\\R (\\mathbb{R})", "font", "high",
    fx(r"\R^{i+1}_!f'(g'^*F').", r"\mathrm{R}^{i+1}_!f'(g'^*F')."), R_NOTE)
add(278, "Preuve of B): '(cf SGA 4 XII 5.1 dans le cas propre'", "cf without a full stop", "(cf. SGA 4 XII",
    "punctuation", "high", fx("(cf. SGA 4 XII", "(cf SGA 4 XII"), "Full stop added by the TeX.")
add(278, "C): 'U un ouvert de X et Z le fermé complémentaire'", "no comma before 'et'", "ouvert de X, et",
    "punctuation", "high", fx(r"ouvert de \(X\), et", r"ouvert de \(X\) et"), "Comma added by the TeX.")
add(278, "C): 'Il existe pour tout Z_l-faisceau constructible F une suite exacte,'",
    "no commas around 'pour tout ... F'", "Il existe, pour tout ... \\(F\\), une suite", "punctuation", "high",
    fx(r"Il existe, pour tout \(\mathbb Z_\ell\)-faisceau constructible \(F\), une suite",
       r"Il existe pour tout \(\mathbb Z_\ell\)-faisceau constructible \(F\) une suite"), "Two commas added by the TeX.")
add(278, "C): display '... --> R^i_! f_U(F/U) --> R^i_! f(F) --> R^i_! f_Z(F/Z) --> R^{i+1}_! f_U(F/U) --> ...'",
    "four plain typed R", "\\R (\\mathbb{R}) four times", "font", "high",
    fx(r"\cdots\longrightarrow \R^i_!f_U(F/U)¶\longrightarrow \R^i_!f(F)¶\longrightarrow \R^i_!f_Z(F/Z)¶\longrightarrow \R^{i+1}_!f_U(F/U)",
       r"\cdots\longrightarrow \mathrm{R}^i_!f_U(F/U)¶\longrightarrow \mathrm{R}^i_!f(F)¶\longrightarrow \mathrm{R}^i_!f_Z(F/Z)¶\longrightarrow \mathrm{R}^{i+1}_!f_U(F/U)"),
    R_NOTE)
add(278, "same display, end", "ends with the dots, no full stop", "\\longrightarrow\\cdots .", "punctuation", "high",
    fx(r"\longrightarrow\cdots .", r"\longrightarrow\cdots"), "Full stop added by the TeX at the end of the display.")
add(278, "paragraph number 2.2.5.", "2.2.5. Le formalisme développé ...", "\\subsubsection*{2.2.5}", "punctuation",
    "high", fx(r"\subsubsection*{2.2.5}", r"\subsubsection*{2.2.5.}"),
    "The TeX drops the full stop of the number, as the logged 1.4.4.-1.4.7. of pp. 267-270.")

# ---------------- p. 279 ----------------
add(279, "underlined title 3.", "3. Classe de cohomologie l-adique associée à un cycle.",
    "\\subsection*{3. Classe de cohomologie \\(\\ell\\)-adique associée à un cycle}", "punctuation", "high",
    fx("associée à un cycle}", "associée à un cycle.}"), "Underlined title: the TeX drops the print's final full stop.")
add(279, "paragraph number 3.1.", "3.1. Si X est un schéma propre", "\\subsubsection*{3.1}", "punctuation", "high",
    fx(r"\subsubsection*{3.1}", r"\subsubsection*{3.1.}"), "The TeX drops the full stop of the number.")
add(279, "'on sait que pour tout faisceau constructible M abélien'", "no comma after 'que'", "on sait que, pour tout",
    "punctuation", "high", fx("on sait que, pour tout", "on sait que pour tout"), "Comma added by the TeX.")
add(279, "'Ceci permet (2.2.1. Remarque) de définir'", "(2.2.1. Remarque): a full stop after 2.2.1",
    "(2.2.1, Remarque)", "punctuation", "high", fx("(2.2.1, Remarque)", "(2.2.1. Remarque)"),
    "The TeX has a comma for the print's full stop.")
add(279, "'la méthode utilisée dans le n° 2 permet de définir'", "n° 2 (abbreviation)", "numéro 2", "word", "high",
    fx("dans le numéro 2", "dans le n° 2"),
    "The TeX writes out the print's abbreviation; n° as the file's 'n°1' (Exposé III) and 'n°2' (Exposé VIII).")
add(279, "'la catégorie des Z_l-modules de type finis, l'équivalence'", "de type finis",
    "de type finis (the printed reading)", "misprint_in_print", "medium", None,
    "Agreement error: 'de type fini' is invariable (the next sentence has 'le Z_l-module de type fini'). The TeX "
    "keeps the printed reading (both layers read 'finis').", corrected="de type fini")
add(279, "paragraph number 3.2. (printed at the top of p. 280; in page_279.tex as the files stand)",
    "3.2. Soient l un nombre premier", "\\subsubsection*{3.2}", "punctuation", "high",
    fx(r"\subsubsection*{3.2}", r"\subsubsection*{3.2.}"),
    "The TeX drops the full stop of the number. Filed under p. 279, where the line stands now: apply before the "
    "marker move of p. 280 (afterwards the line belongs to folio 280's text); the move's anchor "
    "'\\subsubsection*{3.2' matches before and after this edit.")

# ---------------- p. 280 ----------------
add(280, "top of the page: paragraph number 3.2.",
    "p. 280 begins with '3.2. Soient l un nombre premier # car.k'; p. 279 ends with '... au Z_l-faisceau correspondant.'",
    "'\\subsubsection*{3.2}' ends page_279.tex; the folio-280 marker (live s5.tex line 9291, diplomatic) stands "
    "after it, before 'Soient'", "marker", "high", None,
    "Page 280 really begins with '\\subsubsection*{3.2}'. Exact fix: python -I move_marker.py 5 280 "
    "'\\subsubsection*{3.2' --before (simulated in memory on both layers: the marker line then stands between "
    "'... faisceau correspondant.' with its blank line and '\\subsubsection*{3.2}', followed by 'Soient'). Text not moved.")
add(280, "'Soient l un nombre premier # car.k, et X'", "car.k (full stop of the abbreviation)", "\\ne\\car k",
    "punctuation", "high", fx(r"\(\ne\car k\)", r"\(\ne\car.k\)"), "\\car is \\operatorname{car}.")
add(280, "'on lui a associé dans Exp. IV,(*) pour tout entier n'", "Exp. IV (abbreviation, no article)",
    "l'Exposé IV", "word", "high", fx("associé dans l'Exposé IV", "associé dans Exp. IV"),
    "The TeX writes out the print's abbreviation and adds the article (also in 3.3 below).")
add(280, "'pour tout entier n une classe de cohomologie'", "no comma after n", "entier \\(n\\), une classe",
    "punctuation", "high", fx(r"entier \(n\), une classe", r"entier \(n\) une classe"), "Comma added by the TeX.")
add(280, "'(Z/l^{n+1}Z)_X-Module localement libre'", "Module with a capital M", "-module", "word", "high",
    fx(r"_X\)-module localement libre", r"_X\)-Module localement libre"),
    "The typescript's capital M (sheaf of modules), as the logged 'Module' of pp. 263 and 267.")
add(280, "'des racines l^{n+1}-èmes de l'unité'", "-èmes", "-ièmes", "word", "high",
    fx(r"\)-ièmes de l'unité", r"\)-èmes de l'unité"), "")
add(280, "'gamma_X^{(n)}(Y) est l'image de gamma_X^{(n')}(Y) dans'", "Y twice (the cycle is called Z)",
    "\\gamma_X^{(n)}(Y), \\gamma_X^{(n')}(Y) (the printed reading)", "misprint_in_print", "high", None,
    "Wrong letter: the cycle of 3.2 is Z (gamma_X^{(n)}(Z) just above, gamma_X(Z) below). The TeX keeps the printed "
    "Y; the corrected layer already reads Z.", corrected=r"\gamma_X^{(n)}(Z)\) est l'image de \(\gamma_X^{(n')}(Z)")
add(280, "'dans H^{2d}(X, mu_X^{(n)})^{(x)d}) par le morphisme'",
    "H^{2d}(X, mu^{(n)}_X)^{(x)d}): no opening parenthesis before mu (unbalanced)",
    "H^{2d}\\bigl(X,(\\mu_X^{(n)})^{\\otimes d}\\bigr)", "misprint_in_print", "medium",
    fx(r"\bigl(X,(\mu_X^{(n)})^{\otimes d}\bigr)¶\]¶par", r"\bigl(X,\mu_X^{(n)})^{\otimes d}\bigr)¶\]¶par"),
    "Typing error: the other three H^{2d}(X,(mu ...)^{(x)d}) of the page have the parenthesis; the scan is clean "
    "there. The TeX silently adds it; the edit restores the printed reading (only the parenthesis).",
    corrected=r"H^{2d}\bigl(X,(\mu_X^{(n)})^{\otimes d}\bigr)")
add(280, "paragraph number 3.3.", "3.3. Par passage à la limite", "\\subsubsection*{3.3}", "punctuation", "high",
    fx(r"\subsubsection*{3.3}", r"\subsubsection*{3.3.}"), "The TeX drops the full stop of the number.")
add(280, "'étudiées dans Exp. IV, à savoir :'", "Exp. IV (abbreviation, no article)", "l'Exposé IV", "word", "high",
    fx("étudiées dans l'Exposé IV", "étudiées dans Exp. IV"),
    "The TeX writes out the print's abbreviation and adds the article.")

# ---------------- checks ----------------
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")


def live_pages(edition):
    t = open(f"{ROOT}/sga5/{edition}/s5.tex", encoding="utf-8").read()
    ms = list(MARK.finditer(t))
    return {int(m.group(2)): t[m.start(): ms[i + 1].start()] for i, m in enumerate(ms[:-1])}


dip, cur = live_pages("diplomatic"), live_pages("current")
report = []
bad = 0
for x in F:
    if not x["fix"]:
        continue
    p, old = x["page"], x["fix"]["old"]
    page = open(f"{RUN}/b276_280/page_{p}.tex", encoding="utf-8").read()
    n_page, n_dip, n_cur = page.count(old), dip[p].count(old), cur[p].count(old)
    if MARK.search(old) or MARK.search(x["fix"]["new"]):
        bad += 1
        report.append(f"MARKER IN FIX p{p}: {old!r}")
    if n_page != 1 or n_dip != 1:
        bad += 1
    report.append(f"p{p} page={n_page} live_dip={n_dip} live_cur={n_cur} kind={x['kind']} old={old[:60]!r}")

with open(f"{RUN}/findings_276_280.json", "w", encoding="utf-8", newline="\n") as o:
    json.dump(F, o, ensure_ascii=False, indent=1)
counts = {}
for x in F:
    c = counts.setdefault(x["page"], [0, 0])
    c[1 if x["kind"] == "misprint_in_print" else 0] += 1
report.append(f"bad={bad} total={len(F)} counts={counts}")
open(f"{RUN}/crops_276_280/check_report.txt", "w", encoding="utf-8").write("\n".join(report))
