"""Build findings_271_275.json. LaTeX backslashes are written as the placeholder BS_MARK and line breaks as NL_MARK,
so that no tool layer can decode them; both are replaced at run time. Checks every fix's old string (exactly once in
its page file, also after the earlier fixes of the same page are applied in list order)."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
BS = chr(92)
NL = chr(10)
BS_MARK = "¤"
NL_MARK = "¶"
RUN = pathlib.Path(r"C:/Users/user/Documents/sga_scan_check_20261105/run_5")
BATCH = RUN / "b271_275"
OUT = RUN / "findings_271_275.json"


def d(s):
    return s.replace(BS_MARK, BS).replace(NL_MARK, NL) if isinstance(s, str) else s


F = []


def add(page, where, scan, tex, kind, conf, old, new, note="", corrected=None):
    item = {"page": page, "where": d(where), "scan": d(scan), "tex": d(tex), "kind": kind, "confidence": conf,
            "fix": None if old is None else {"old": d(old), "new": d(new)}}
    if kind == "misprint_in_print":
        item["corrected"] = d(corrected)
    item["note"] = d(note)
    F.append(item)


UH = "As the logged ¤uHom fixes of Exposés V and VI (pp. 251-253)."
EM = "Exposé VI: the TeX has no underline markup; ¤emph, the file's form for the print's underline."
TT = "Underlined title: the TeX drops the print's final full stop."
RR = ("The print's R is the typewriter's plain R; ¤R is ¤mathbb{R} here (renewed with the scoped definitions "
      "before the heading of Exposé V and not reset for Exposé VI).")

# ---------------- page 271
add(271, "end of Définition 1.5.1: 'soit un objet (AR, ℓZ)-noethérien (5 1.3).'",
    "(5 1.3)", "(V 1.3)", "misprint_in_print", "high",
    "(V 1.3)", "(5 1.3)",
    "Wrong character: the typescript has the arabic 5 for the exposé numeral (the same page cites '(V 5.2.1)', "
    "'(V 2.2.1)', '(V 2.2.2)'); the TeX silently gives V.",
    corrected="(V 1.3)")
add(271, "'la sous-catégorie pleine de Hom(N°, Ab(X)) engendrée par les'",
    "Hom underlined", "¤Hom", "underline", "high",
    "pleine de ¤(¤Hom", "pleine de ¤(¤uHom", UH)
add(271, "'En particulier, c'est une catégorie abélienne.'",
    "'catégorie abélienne' underlined", "no underline", "underline", "high",
    "c'est une catégorie abélienne.", "c'est une ¤emph{catégorie abélienne}.", EM)
add(271, "underlined title 1.5.2",
    "1.5.2. (AR, Z_ℓ)-faisceaux constructibles localement AR-nuls.",
    "¤subsubsection*{1.5.2. ... localement ¤(AR¤)-nuls}", "punctuation", "high",
    "localement ¤(AR¤)-nuls}", "localement ¤(AR¤)-nuls.}", TT)
add(271, "'Il est clair qu'un objet AR-nul (V 2.2.1) de Hom(N°,Ab(X)) est un'",
    "Hom underlined", "¤Hom", "underline", "high",
    "(V 2.2.1) de ¤(¤Hom", "(V 2.2.1) de ¤(¤uHom", UH)
add(271, "'une sous-catégorie abélienne épaisse de la catégorie pleine engendrée'",
    "'épaisse' underlined", "no underline", "underline", "high",
    "abélienne épaisse de la catégorie pleine", "abélienne ¤emph{épaisse} de la catégorie pleine",
    "The second 'épaisse' of the page ('épaisse de celle des') is not underlined.")
add(271, "'constructibles dans Hom(N°,Ab(X)).'",
    "Hom underlined", "¤Hom", "underline", "high",
    "constructibles dans ¤(¤Hom", "constructibles dans ¤(¤uHom", UH)
add(271, "'Convenant de dire qu'un objet P de Hom(N°,Ab(X)) est localement'",
    "Hom underlined", "¤Hom", "underline", "high",
    "¤(P¤) de ¤(¤Hom", "¤(P¤) de ¤(¤uHom", UH)
add(271, "'est localement AR-nul s'il existe un recouvrement ouvert de X'",
    "'localement' (line end) and 'AR-nul' (next line) underlined", "no underline", "underline", "high",
    "est localement ¤(AR¤)-nul s'il", "est ¤emph{localement} ¤(AR¤)-¤emph{nul} s'il",
    "The underline also runs under AR; math and hyphen kept outside ¤emph as in the file's earlier fixes "
    "(AR-¤(J¤)-¤emph{adique}).")
add(271, "'On observera que si X est noethérien, les'",
    "'noethérien' underlined", "no underline", "underline", "high",
    "est noethérien, les", "est ¤emph{noethérien}, les", EM)
add(271, "'les objets (AR, ℓZ)-adiques noethériens de Hom(N°,Ab(X)),'",
    "Hom underlined", "¤Hom", "underline", "high",
    "noethériens de ¤(¤Hom", "noethériens de ¤(¤uHom", UH)

# ---------------- page 272
add(272, "top of the page: the display '(AR, Z_ℓ)-fc(X) ,' of Définition 1.5.3",
    "p. 272 begins with the display (AR, Z_ℓ)-fc(X) , and then 'la catégorie abélienne quotient'",
    "the display stands at the end of page_271.tex, above the marker of p. 272", "marker", "high",
    None, None,
    "Page 272 really begins with the display '¤[ (AR,¤mathbb Z_¤ell)¤text{-}¤fc(X), ¤]' (p. 271 ends with "
    "'et on note'). Exact fix: python -I move_marker.py 5 272 '¤[' --before (simulated in memory on both layers: "
    "the marker line then stands between 'et on note' and the display's '¤[', followed by the display and "
    "'la' / 'catégorie abélienne quotient ...'). Text not moved.")
add(272, "Définition 1.5.3, display 'Hom ( N°, Ab(X) )'",
    "Hom underlined", "¤Hom", "underline", "high",
    "¤[¶¤Hom(¤mathbb N^¤circ", "¤[¶¤uHom(¤mathbb N^¤circ", UH)
add(272, "Définition 1.5.3: 'par la sous-catégorie pleine, épaisse, engendrée par les (AR- Z_ℓ)-faisceaux "
         "constructibles localement AR-nuls.'",
    "(AR- Z_ℓ)", "(AR,¤mathbb Z_¤ell)", "misprint_in_print", "high",
    "¤((AR,¤mathbb Z_¤ell)¤)-faisceaux constructibles localement",
    "¤((AR¤text{-}¤mathbb Z_¤ell)¤)-faisceaux constructibles localement",
    "Typing error: a hyphen for the comma of (AR, Z_ℓ); the TeX silently gives the comma. The hyphen in math "
    "as the file's ¤text{-}.",
    corrected="¤((AR,¤mathbb Z_¤ell)¤)-faisceaux constructibles localement")
add(272, "Notation 1.5.4: 'la sous-catégorie pleine de Hom(N°,Ab(X)) engendrée par les'",
    "Hom underlined", "¤Hom", "underline", "high",
    "pleine de ¤(¤Hom", "pleine de ¤(¤uHom", UH)
add(272, "'on définit de façon évidente un foncteur :'",
    "un foncteur :", "un foncteur", "punctuation", "high",
    "un foncteur¶¤[", "un foncteur:¶¤[",
    "The TeX drops the colon; written without a space as the logged 'le foncteur:' of p. 255.")
add(272, "Proposition 1.5.5, the statement",
    "'Le foncteur u ci-dessus est une équivalence de catégories' underlined throughout (also under u)",
    "no underline", "underline", "high",
    "Le foncteur ¤(u¤) ci-dessus est une équivalence de catégories.",
    "¤emph{Le foncteur} ¤(u¤) ¤emph{ci-dessus est une équivalence de catégories}.",
    "Math kept outside ¤emph as in the file's earlier fixes.")

# ---------------- page 273
add(273, "underlined title 2.",
    "2. Formalisme de la cohomologie ℓ-adique.", "¤subsection*{2. Formalisme de la cohomologie ¤(¤ell¤)-adique}",
    "punctuation", "high",
    "cohomologie ¤(¤ell¤)-adique}", "cohomologie ¤(¤ell¤)-adique.}", TT)
add(273, "underlined title 2.1.",
    "2.1. Image réciproque.", "¤subsubsection*{2.1. Image réciproque}", "punctuation", "high",
    "Image réciproque}", "Image réciproque.}", TT)
add(273, "'se prolonge donc de façon évidente en un foncteur exact, noté de la même manière,'",
    "the second 'exact' underlined", "no underline", "underline", "high",
    "foncteur exact, noté", "foncteur ¤emph{exact}, noté", EM)
add(273, "display 'f^* : Hom(N°,Ab(Y)) → Hom(N°, Ab(X)) .'",
    "both Hom underlined", "¤Hom twice", "underline", "high",
    "f^*:¤Hom(¤mathbb N^¤circ,¤Ab(Y))¤longrightarrow ¤Hom(",
    "f^*:¤uHom(¤mathbb N^¤circ,¤Ab(Y))¤longrightarrow ¤uHom(", UH)
add(273, "'L'équivalence de catégories (1.5.5) et le fait que f^* transforme ... localement AR-nul montre alors que'",
    "montre", "montrent", "misprint_in_print", "high",
    "montrent alors", "montre alors",
    "Agreement error: the subject is compound ('L'équivalence ... et le fait que ...'); the print has the "
    "singular, the TeX silently gives the plural.",
    corrected="montrent alors")
add(273, "'avec la propriété d'\"associativité\" habituelle'",
    "d'\"associativité\"", "d'associativité", "punctuation", "high",
    "d'associativité", "d'``associativité''",
    "The TeX drops the quotation marks; ``...'' as the file's other quotes.")
add(273, "end of the page: 'avec la propriété d'\"associativité\" habituelle (SGA 1 VI 7 et suiv.)'",
    "(SGA 1 VI 7 et suiv.) with no full stop after the parenthesis", "(SGA 1 VI 7 et suiv.).",
    "misprint_in_print", "medium",
    "suiv.).", "suiv.)",
    "The sentence and paragraph end without a full stop in the print (only the stop of 'suiv.' inside the "
    "parenthesis); the TeX silently adds one. If the missing stop is not counted as a misprint, the same edit "
    "is an added full stop (punctuation). Does not overlap the quotation-mark edit above.",
    corrected="suiv.).")

# ---------------- page 274
add(274, "underlined title 2.2.",
    "2.2. Images directes supérieures.", "¤subsubsection*{2.2. Images directes supérieures}", "punctuation", "high",
    "directes supérieures}", "directes supérieures.}", TT)
add(274, "Lemme 2.2.1, display 'R^i_! f(M)'",
    "plain typed R", "¤R (¤mathbb{R})", "font", "high",
    "¤R^i_!f(M)", "¤mathrm{R}^i_!f(M)",
    RR + " These are the first ¤R of Exposé VI.")
add(274, "Lemme 2.2.2, display 'R^i_! f(F)'",
    "plain typed R", "¤R (¤mathbb{R})", "font", "high",
    "¤R^i_!f(F)", "¤mathrm{R}^i_!f(F)", "As Lemme 2.2.1.")
add(274, "display '(R^i_! f)_{i∈Z} : Ab(X) → Ab(Y)'",
    "plain typed R", "¤R (¤mathbb{R})", "font", "high",
    "(¤R^i_!f)_{i¤in¤mathbb Z}", "(¤mathrm{R}^i_!f)_{i¤in¤mathbb Z}", "As Lemme 2.2.1.")
add(274, "display 'Hom(N°, Ab(X)) → Hom(N°,Ab(Y)) ,'",
    "both Hom underlined", "¤Hom twice", "underline", "high",
    "¤Hom(¤mathbb N^¤circ,¤Ab(X))¤longrightarrow ¤Hom(",
    "¤uHom(¤mathbb N^¤circ,¤Ab(X))¤longrightarrow ¤uHom(", UH)
add(274, "'Par ailleurs, les foncteurs R^i_! f transforment'",
    "plain typed R", "¤R (¤mathbb{R})", "font", "high",
    "¤(¤R^i_!f¤) transforment", "¤(¤mathrm{R}^i_!f¤) transforment", "As Lemme 2.2.1.")
add(274, "'AR-nul, de sorte que par passage au'",
    "de sorte que par passage", "de sorte que, par passage", "punctuation", "high",
    "de sorte que, par passage", "de sorte que par passage", "Comma added by the TeX.")

# ---------------- page 275
add(275, "display '(R^i_! f)_{i∈Z} :(AR, Z_ℓ)-fc(X) → (AR, Z_ℓ)-fc(Y) .'",
    "plain typed R", "¤R (¤mathbb{R})", "font", "high",
    "(¤R^i_!f)_{i¤in¤mathbb Z}", "(¤mathrm{R}^i_!f)_{i¤in¤mathbb Z}", "As on p. 274.")
add(275, "Définition 2.2.3: 'Le foncteur :'",
    "Le foncteur :", "Le foncteur", "punctuation", "high",
    "Le foncteur¶¤[", "Le foncteur:¶¤[",
    "The TeX drops the colon (as 'un foncteur :' on p. 272).")
add(275, "Définition 2.2.3, display 'R^i_! f : Z_ℓ-fc(X) → Z_ℓ-fc(Y)'",
    "plain typed R", "¤R (¤mathbb{R})", "font", "high",
    "¤R^i_!f:¤mathbb Z_¤ell", "¤mathrm{R}^i_!f:¤mathbb Z_¤ell", "As on p. 274.")
add(275, "Définition 2.2.3: 'est appelé foncteur i^ème image directe à supports propres de f.'",
    "i with a raised 'ème', no hyphen", "¤(i¤)-ième", "word", "high",
    "¤(i¤)-ième", "¤(i¤)¤textsuperscript{ème}",
    "¤textsuperscript{ème} as the file's '2¤textsuperscript{ème} Réduction'.")
add(275, "label of Proposition 2.2.4: '(Suite spectrale de LERAY).'",
    "LERAY", "Leray", "word", "high",
    "(Suite spectrale de Leray)", "(Suite spectrale de LERAY)",
    "The name in capitals, as the restored SERRE of p. 259.")
add(275, "Proposition 2.2.4, display 'R^i_! g (R^j_! f (F)) ⟹ R^{i+j}_! (gof) (F) .'",
    "three plain typed R", "¤R (¤mathbb{R}) three times", "font", "high",
    "¤R^i_!g¤bigl(¤R^j_!f(F)¤bigr)¤Longrightarrow ¤R^{i+j}_!",
    "¤mathrm{R}^i_!g¤bigl(¤mathrm{R}^j_!f(F)¤bigr)¤Longrightarrow ¤mathrm{R}^{i+j}_!", "As on p. 274.")
add(275, "end of page_275.tex: 'la' after 'convenons de noter ¤(¤Sp(C)¤)'",
    "p. 275 ends with the display Sp(C); p. 276 begins 'la catégorie des suites spectrales commençant au degré 2'",
    "'la' ends the line before the marker of p. 276", "marker", "high",
    None, None,
    "Page 276 really begins with 'la' (the OCR of p. 276 begins 'la catégorie des suites spectrales'). Exact fix: "
    "python -I move_marker.py 5 276 'la' --before (simulated in memory on both layers: the marker line then stands "
    "between 'convenons de noter ¤(¤Sp(C)¤) ' and 'la', followed by 'catégorie des suites spectrales'). Not "
    "marker_split_word.py pull 'la', which would glue 'la' to 'catégorie'. Text not moved.")

# ---------------- checks
ok = True
texts = {p: (BATCH / f"page_{p}.tex").read_text(encoding="utf-8") for p in range(271, 276)}
work = dict(texts)
for i, it in enumerate(F):
    fx = it["fix"]
    if fx is None:
        continue
    p = it["page"]
    n0 = texts[p].count(fx["old"])
    n1 = work[p].count(fx["old"])
    if n0 != 1 or n1 != 1 or fx["old"] == fx["new"] or "%%%%" in fx["old"]:
        ok = False
        print("PROBLEM", i, p, repr(fx["old"]), n0, n1)
    work[p] = work[p].replace(fx["old"], fx["new"], 1)
    for ch in fx["old"] + fx["new"]:
        if ord(ch) < 32 and ch != NL:
            ok = False
            print("CONTROL CHAR", i, p, repr(fx["new"]))
counts = {}
for it in F:
    c = counts.setdefault(it["page"], [0, 0])
    c[1 if it["kind"] == "misprint_in_print" else 0] += 1
print("items", len(F), "counts", counts, "all checks ok" if ok else "CHECKS FAILED")
if ok:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8", newline=NL)
    print("written", OUT)
