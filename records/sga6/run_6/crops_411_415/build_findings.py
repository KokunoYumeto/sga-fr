"""Build findings_411_415.json; check every fix's old string occurs exactly once in its page file;
simulate (in memory only) the folio-412 marker move in both layers of main.tex. Writes only the findings JSON."""
import json, pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
B = RUN / "b411_415"
OUT = RUN / "findings_411_415.json"
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
NL = "\n"

F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": confidence, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 411 ----------------
add(411, "6.5, after the display i), ii): 'Les K˙(X)_i ainsi définis sont des sous-groupes additifs de K˙(X).'",
    "no comma after K˙(X)_i and none after 'définis' (both scans; crops_411_415/c411_les.png, w411_les.png)",
    r"Les $K^{\bullet}(X)_i$, ainsi définis, sont",
    "punctuation", "high",
    {"old": ", ainsi définis, sont", "new": " ainsi définis sont"},
    "Both commas are the transcription's. Independent of the paragraph entry below (no common text).")

add(411, "same sentence, its place after the display i), ii)",
    "'Les K˙(X)_i ainsi définis ...' begins a new, indented paragraph (indented as 'Soient' below; 'En effet' "
    "continues it on the next line at the left margin) (both scans; crops_411_415/w411_les.png)",
    r"'\]' followed directly by 'Les' (the paragraph runs on)",
    "other", "high",
    {"old": r"\]" + NL + "Les", "new": r"\]" + NL + NL + "Les"},
    "Missing paragraph break.")

add(411, "'On a alors : xx' = cl(M˙ ⊗ M'˙), et :' after the display '... ≥ j .'",
    "'On a alors' begins a new, indented paragraph (both scans; crops_411_415/w411_mid.png)",
    r"'\]' followed directly by 'On a alors' (the paragraph runs on)",
    "other", "high",
    {"old": r"\]" + NL + "On a alors", "new": r"\]" + NL + NL + "On a alors"},
    "Missing paragraph break; independent of the L entry of the same line.")

add(411, "'On a alors : xx' = cl(M˙ ⊗ M'˙)', the L over the tensor sign",
    "double-struck L: a typed L with a doubled stem (like IL), not underlined (both scans; "
    "crops_411_415/c411_L2.png, w411_mid.png)",
    r"\overset{\mathbf L}{\otimes}",
    "font", "high",
    {"old": r"\overset{\mathbf L}{\otimes}", "new": r"\overset{\mathbb L}{\otimes}"},
    r"The derived tensor's L in the print's double-struck form, not the doubly underlined L that the file writes "
    r"\mathbf (p. 389, findings_386_390). The same L on p. 412.")

add(411, "Proposition 6.6, 'La filtration 5.5 de K˙(X) est une filtration d'anneau'",
    "'5.5' (both scans; crops_411_415/c411_prop.png, w411_prop.png)",
    "La filtration 5.5 (printed reading kept)",
    "misprint_in_print", "high", None,
    "Wrong reference number: the filtration is defined in 6.5, just above; § 5 defines none (5.5 is Corollaire 5.5 "
    "on flag schemes, main.tex line 10171). The diplomatic layer keeps the printed reading; the current layer "
    "already reads 6.5.",
    corrected="La filtration 6.5")

add(411, "statements on pp. 411-413: Proposition 6.6 (p. 411), Lemme 6.7 and Lemme 6.8 (p. 412; 6.8 ends on p. 413), "
         "Théorème 6.9 (p. 413)",
    "underlined word group by word group (both scans): Prop. 6.6 'La filtration', 'de', 'est une filtration "
    "d'anneau', 'et' (5.5, K˙(X), K˙(X)_{d+1} = 0 plain); Lemme 6.7 'Soit', 'un schéma affine noethérien', 'un "
    "nombre fini de points de', 'un', '-Module inversible', 'Alors', 'il existe une section', 'telle que pour "
    "tout', 'soit une base de'; Lemme 6.8 'Soient', 'un schéma noethérien ayant un faisceau ample', 'un', "
    "'-Module inversible', 'des points de', 'Alors il existe un', p. 413 'entier', 'tel que pour tout', 'il existe "
    "une section', 'qui soit une base de', 'pour tout'; Théorème 6.9 'Soit', 'un schéma noethérien de dimension', "
    "'ayant un faisceau ample', 'Alors', 'et à fortiori'",
    r"the statements in roman (no \underline, no \emph)",
    "underline", "high", None,
    "Exposé VI follows the Exposé II pattern of GLOBAL_ISSUES 82 (as on pp. 365-405): not itemized; the word "
    "groups are listed for the scripted pass. Problème 6.10 (p. 415) underlines only its label, as the TeX has it. "
    "No emphasized defined terms and no category L on pp. 411-415.")

add(411, "letters of sheaves and complexes on pp. 411-414",
    "underlined in the print (both scans): the M of every complex M˙, M'˙ (27 places on p. 411, 9 on p. 412); L "
    "('faisceau ample L' of 6.5, Lemme 6.8, Théorème 6.9; L^{⊗n_o}, L^n, L^{⊗-kn}, L^{⊗-k'n'} on p. 413; "
    "L^{⊗-nn'} twice on p. 414); E of Lemme 6.7 and its proof (E un O_X-Module, Γ(X,E), E_{x_i}, 'Comme E est', "
    "'section s de E', E_{x'_i}, 'base de E est un ouvert'), E of Lemme 6.8; E(kn), Γ(X_f,E), E(n_on'_o), E(n), "
    "E((k+1)n), E_{x_i}, 'si E, E' sont deux faisceaux', E'(k'n') and the E, E' of the display (p. 413); N˙ "
    "(4 places), E', E of the complex N˙, and E_i, F_i in 'E_i et F_i ayant même rang', 'les E_i, F_i de rang "
    "constant', 'des E_i, F_i. Dans K˙(X')' (p. 414). The classes stay plain: 'de classes E, E'' (p. 413), 'les "
    "E_i, F_i, étant les classes', 'des E_i, F_i sont sommes de classes' (p. 414)",
    "all plain",
    "underline", "high", None,
    r"Convention of the Exposé VI transcription, reported for pp. 366-405 (findings_366_370 to findings_401_405): "
    r"not itemized. Here too only the underline tells a sheaf from its class: p. 413 'si \(E,E'\) sont deux "
    r"faisceaux inversibles sur \(X\), de classes \(E,E'\)'. Three examples, in the form to use if the diplomatic "
    r"layer reproduces it: p. 411 'faisceau ample $L$. On munit' -> 'faisceau ample $\underline{L}$. On munit'; "
    r"p. 413 'si $E,E'$ sont deux faisceaux' -> 'si $\underline{E},\underline{E}'$ sont deux faisceaux'; p. 414 "
    r"'La classe de $N^\bullet$ est' -> 'La classe de $\underline{N}^\bullet$ est'. The underlined O of O_X, "
    r"O_{X'} stays \mathcal O (pending volume decision); the underlined m of p. 412 is a separate entry.")

# ---------------- page 412 ----------------
add(412, "start of page (folio-412 marker)",
    "p. 411 ends with '(EGA 0_IV 14.2.2.3).'; p. 412 begins 'Il suffit donc, pour achever la démonstration, de "
    "noter que :' (both scans; crops_411_415/w411_mid.png, w412_top.png)",
    r"page_411.tex ends '(EGA $0_{\mathrm{IV}}$ 14.2.2.3). Il' above the folio-412 marker; page_412.tex begins "
    r"'suffit donc'",
    "marker", "high", None,
    r"Page 412 really begins at the word 'Il' (the last word of page_411.tex). Exact edit in main.tex, both layers "
    r"(diplomatic lines 10398-10400, current 10404-10406): replace '(EGA $0_{\mathrm{IV}}$ 14.2.2.3). Il\n"
    r"%%%%%%%%%%  scan idx 425  |  folio 412  %%%%%%%%%%\nsuffit donc' by '(EGA $0_{\mathrm{IV}}$ 14.2.2.3).\n"
    r"%%%%%%%%%%  scan idx 425  |  folio 412  %%%%%%%%%%\nIl suffit donc' (one occurrence in each layer; "
    r"simulated in memory: crops_411_415/build_findings.py). 'Il' continues the paragraph (left margin), so no "
    r"blank line.")

add(412, "display 'Supp(H^*(M˙ ⊗ M'˙)) ⊂ Supp(H^*(M˙))∩Supp(H^*(M'˙)) .', the L over the tensor sign",
    "double-struck L (doubled stem), as on p. 411 (both scans; crops_411_415/c412_L.png, w412_L.png)",
    r"\overset{\mathbf L}{\otimes}",
    "font", "high",
    {"old": r"\overset{\mathbf L}{\otimes}", "new": r"\overset{\mathbb L}{\otimes}"},
    "As p. 411.")

add(412, "'Pour montrer que K˙(X)_{d+1} est nul' after the display",
    "begins a new, indented paragraph (both scans; crops_411_415/w412_top.png)",
    r"'\]' followed directly by 'Pour montrer que' (the paragraph runs on)",
    "other", "high",
    {"old": r"\]" + NL + "Pour montrer", "new": r"\]" + NL + NL + "Pour montrer"},
    "Missing paragraph break.")

add(412, "'on prend x ∈ K˙(X)_{d+1}, et Y = X il existe alors M˙ tel que'",
    "no punctuation after 'Y = X', the last words of the line; 'il existe alors' begins the next (both scans; "
    "crops_411_415/c412_YX.png, w412_top.png)",
    "et $Y=X$; il existe (silently corrected)",
    "misprint_in_print", "medium",
    {"old": "$Y=X$; il", "new": "$Y=X$ il"},
    "The stop between the two clauses is missing in the print; the diplomatic layer should drop the TeX's ';', "
    "the corrected edition keeps it (the current layer has it).",
    corrected="$Y=X$; il")

add(412, "Lemme 6.7, end of the statement: 'pour tout i, s_{x_i} soit une base de E_{x_i}.'",
    "after the index x of E a tall prime-like stroke, with a small hook over the i where its dot stands (both "
    "scans; crops_411_415/c412_Exi2.png, w412_mark_st.png): read E_{x'_i}; the s_{x_i} of the same line has a "
    "plain index",
    "soit une base de $E_{x_i}$ (silently corrected, if the stroke is the prime)",
    "misprint_in_print", "low",
    {"old": "soit une base de $E_{x_i}$", "new": "soit une base de $E_{x'_i}$"},
    "The statement is about the x_i; the closed points x'_i come only in the proof, whose E_{x'_i} has a short "
    "straight prime (crops_411_415/w412_Exip.png). Low: this stroke is longer than the typist's prime elsewhere; "
    "if it is judged a stray mark, drop the entry.",
    corrected="soit une base de $E_{x_i}$")

add(412, "proof of Lemme 6.7, 'soit x'_i un point fermé de X tel que x'_i ∈ {x_i} with a bar'",
    "a bar over {x_i} (the closure of the point x_i) (both scans; crops_411_415/c412_bar.png, w412_xip.png)",
    r"$x'_i\in\{x_i\}$ (no bar)",
    "formula", "high",
    {"old": r"$x'_i\in\{x_i\}$", "new": r"$x'_i\in\overline{\{x_i\}}$"},
    r"Not a misprint: the print has the bar; the current layer already reads \overline{\{x_i\}}, the diplomatic "
    r"layer lost it.")

add(412, "proof of Lemme 6.7, 'chacun des m_i intervienne une fois et une seule fans la famille (m_i)'",
    "'fans' (both scans; crops_411_415/w412_top.png)",
    "fans la famille (printed reading kept)",
    "misprint_in_print", "high", None,
    "Typing error for 'dans'; the diplomatic layer keeps it, the current layer already reads 'dans'.",
    corrected="dans la famille")

add(412, "proof of Lemme 6.7, 'on a pour tout i un isomorphisme M_{m_i} ≃ A_{m_i} d'où on déduit'",
    "no punctuation after A_{m_i}, the end of the line; 'd'où' begins the next (both scans; "
    "crops_411_415/c412_MA.png, w412_bot.png)",
    r"A_{\mathfrak m_i}$; d'où (silently corrected)",
    "misprint_in_print", "medium",
    {"old": "$; d'où", "new": "$ d'où"},
    "As 'Y = X il existe' above: the diplomatic layer should drop the ';', the corrected edition keeps it (the "
    r"current layer has it). Independent of the \mathfrak m entry.",
    corrected="$; d'où")

add(412, "Lemme 6.8, 'x_1 ...,x_k des points de X'",
    "no comma after x_1: 'x_1  ...,x_k' (both scans; crops_411_415/c412_x1k.png, w412_bot.png)",
    r"$x_1,\ldots,x_k$ des points (silently corrected)",
    "misprint_in_print", "medium",
    {"old": r"$x_1,\ldots,x_k$ des points", "new": r"$x_1\ldots,x_k$ des points"},
    "The comma after x_1 is missing in the print (Lemme 6.7 has x_1,...,x_k).",
    corrected=r"$x_1,\ldots,x_k$ des points")

add(412, "proof of Lemme 6.7: the maximal ideals m_i (14 places)",
    "a typed m, underlined (m_i with the underline), in all 14 places (both scans; crops_411_415/w412_top.png, "
    "w412_bot.png)",
    r"\mathfrak m_i (14 times)",
    "font", "low", None,
    r"The typist's underlined letter, read as Fraktur: main.tex writes \mathfrak m throughout and never "
    r"\underline{m} (as the underlined m_s of p. 179, findings_176_180). For the pending decision on the typist's "
    r"underlined letters (with the O of O_X): with \underline these become \underline{m}_i, e.g. 'idéaux maximaux "
    r"$\mathfrak m_i$ de $A$' -> 'idéaux maximaux $\underline{m}_i$ de $A$'; 'modulo $\mathfrak m_i$, donc' -> "
    r"'modulo $\underline{m}_i$, donc'; '$M_{\mathfrak m_i}\simeq A_{\mathfrak m_i}$' -> "
    r"'$M_{\underline{m}_i}\simeq A_{\underline{m}_i}$'. No page fix meanwhile.")

# ---------------- page 413: nothing beyond the conventions (entries on p. 411) ----------------

# ---------------- page 414 ----------------
add(414, "display N˙ = ... → 0 → L^{⊗-nn'} → E'⊕L^{⊗-nn'} → E → 0 → ..., the leading '...'",
    "three typed full stops on the baseline (both scans; crops_411_415/w414_top.png)",
    r"N^\bullet=\cdots\to0",
    "symbol", "medium",
    {"old": r"N^\bullet=\cdots", "new": r"N^\bullet=\ldots"},
    r"\cdots sets the dots at mid-height; the same fix as pp. 387-404 (findings_386_390, findings_401_405).")

add(414, "same display, its end 'E → 0 →...'",
    "the line ends with three typed full stops on the baseline after the last arrow, and no full stop for the "
    "sentence (both scans; crops_411_415/c414_end.png, w414_top.png)",
    r"E\to0\to\cdots. (\cdots, then a full stop the print does not have)",
    "punctuation", "high",
    {"old": r"E\to0\to\cdots.", "new": r"E\to0\to\ldots"},
    "One edit for the two differences (the height of the dots, the added full stop), which touch the same "
    "characters.")

add(414, "display x = γ^{i_1}(E_1-F_1) ... γ^{i_k}(E_k-F_k), between the factors",
    "three typed full stops on the baseline (both scans; crops_411_415/w414_top.png)",
    r"(E_1-F_1)\cdots\gamma^{i_k}",
    "symbol", "medium",
    {"old": r"(E_1-F_1)\cdots", "new": r"(E_1-F_1)\ldots"},
    "As the dots of the complex N˙.")

add(414, "same display, 'avec i_1+...+i_k ≥ d+1'",
    "three typed full stops on the baseline (both scans; crops_411_415/w414_top.png)",
    r"i_1+\cdots+i_k",
    "symbol", "medium",
    {"old": r"i_1+\cdots+i_k", "new": r"i_1+\ldots+i_k"},
    "As the dots of the complex N˙.")

add(414, "'Soient ξ, η les classes de deux O_{X'}-Modules inversibles'",
    "a comma after the index X: 'O_X,-Modules' (a comma with its tail, sitting on the line, unlike the straight "
    "prime of 'X' est noethérien' below) (both scans; crops_411_415/c414_OX2.png, c414_Xp.png, w414_bot.png)",
    r"$\mathcal O_{X'}$-Modules (silently corrected)",
    "misprint_in_print", "medium",
    {"old": "O_{X'}$-Modules", "new": "O_X$,-Modules"},
    "Typing slip, a comma for the prime: ξ and η are classes on X'. The diplomatic layer should give the comma, "
    "the corrected edition keeps O_{X'}.",
    corrected="O_{X'}$-Modules")

# ---------------- page 415 ----------------
add(415, "Problème 6.10, 'Fil^kK˙(X) ⊂ K˙(X)_k ?'",
    "both K with the raised dot (both scans; crops_411_415/w415_all.png)",
    r"\Fil^kK'(X)\subset K^{\bullet}(X)_k",
    "symbol", "high",
    {"old": r"\Fil^kK'(X)", "new": r"\Fil^kK^{\bullet}(X)"},
    r"Left by the 10 Nov K' -> K^{\bullet} pass of Exposé VI (missed after a superscript letter), as findings_401_405 "
    r"announced; the same string in the current layer (line 10465).")

add(415, "heading of the bibliography",
    "BIBLIOGRAPHIE: typed capitals, underlined, no further words (both scans; crops_411_415/w415_all.png)",
    r"\subsection*{Bibliographie de l'Exposé VI}",
    "word", "high",
    {"old": r"\subsection*{Bibliographie de l'Exposé VI}", "new": r"\subsection*{BIBLIOGRAPHIE}"},
    "'de l'Exposé VI' is the transcription's; capitals as the headings fixed on pp. 19, 159, 220, 273, 296 and 364; "
    "the missing underline of a section title is accepted.")

for title, num in (("K-Theory and stable algebra", "[1] Bass"),
                   ("Anneaux de Chow et applications", "[2] Chevalley"),
                   ("Topos localement annelés et schémas relatifs", "[3] Hakim"),
                   ("Residues and duality", "[4] Hartshorne"),
                   ("Le groupe de Grothendieck des schémas en groupes réductifs", "[5] Serre")):
    add(415, f"bibliography {num}, title",
        f"'{title}' typed plain, not underlined (both scans; crops_411_415/w415_all.png)",
        r"\emph{" + title + "}",
        "font", "high",
        {"old": r"\emph{" + title + "}", "new": title},
        "The typescript neither underlines nor italicizes the titles of this bibliography; the same fix as the "
        "bibliographies of pp. 19, 159, 273, 296 and 364.")

add(415, "bibliography [4] Hartshorne, 'Lectures notes in Mathematics n°20'",
    "'Lectures notes' (both scans; crops_411_415/w415_all.png)",
    "Lectures notes in Mathematics (printed reading kept)",
    "misprint_in_print", "medium", None,
    "The series is Lecture Notes in Mathematics (main.tex line 104 writes it so); the diplomatic layer keeps the "
    "printed reading, the current layer already reads 'Lecture Notes'.",
    corrected="Lecture Notes in Mathematics")

# ---------------- checks ----------------
ok = True
for f in F:
    fx = f["fix"]
    if fx is None:
        continue
    t = (B / f"page_{f['page']}.tex").read_text(encoding="utf-8")
    n = t.count(fx["old"])
    if n != 1:
        ok = False
    if "%%%%%%%%%%" in fx["old"]:
        ok = False
        print("MARKER IN OLD", f["page"], fx["old"])
    print(f["page"], f["kind"], n, repr(fx["old"])[:70])

# misprint fixes and other fixes must not share text on the same page
for i, a in enumerate(F):
    for j, b in enumerate(F):
        if i < j and a["page"] == b["page"] and a["fix"] and b["fix"]:
            t = (B / f"page_{a['page']}.tex").read_text(encoding="utf-8")
            ia = t.find(a["fix"]["old"]); ib = t.find(b["fix"]["old"])
            ra = set(range(ia, ia + len(a["fix"]["old"]))); rb = set(range(ib, ib + len(b["fix"]["old"])))
            if ra & rb:
                print("OVERLAP", a["page"], repr(a["fix"]["old"]), repr(b["fix"]["old"]))

# simulate the marker move (both layers)
M412 = "%%%%%%%%%%  scan idx 425  |  folio 412  %%%%%%%%%%"
m_old = "(EGA $0_{" + chr(92) + "mathrm{IV}}$ 14.2.2.3). Il" + NL + M412 + NL + "suffit donc"
m_new = "(EGA $0_{" + chr(92) + "mathrm{IV}}$ 14.2.2.3)." + NL + M412 + NL + "Il suffit donc"
for layer in ("diplomatic", "current"):
    t = (ROOT / layer / "main.tex").read_text(encoding="utf-8")
    c = t.count(m_old)
    i = t.find(m_old)
    print(layer, "marker old count:", c, "line", t.count(NL, 0, i) + 1)
    t2 = t.replace(m_old, m_new)
    k = t2.find(M412)
    print("   ", repr(t2[k - 60:k + 90]))
    if c != 1:
        ok = False

print("all olds unique:", ok, " findings:", len(F))
if ok:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
    print("written", OUT)
