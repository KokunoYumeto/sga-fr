"""Build findings_441_445.json: check every fix's old string (once in its page file, no marker line, still once after
the page's earlier fixes), simulate the two marker edits in both layers of main.tex in memory (nothing is written
there), then write the JSON next to the batch folder."""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
B = RUN / "b441_445"
SGA6 = RUN.parent / "sga6"
OUT = RUN / "findings_441_445.json"
NL = "<NL>"


def s(x):
    """raw string with <NL> for a line break"""
    return x.replace(NL, "\n")


F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if fix is None else {"old": s(fix[0]), "new": s(fix[1])}}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- conventions (pp. 441-445), not itemized
add(441, "statements of pp. 441-445: Proposition 3.4 and Lemme 3.5 (p. 441), the Lemme recalled from Exposé III (p. 442), "
         "Proposition 3.6 (p. 444), Théorème 3.7 (pp. 444-445)",
    "underlined word group by word group (both scans): Prop. 3.4 'Avec les hypothèses et les notations de', 'et', 'on a', "
    "'pour tout', 'la relation'; Lemme 3.5 'Avec les hypothèses et les notations de', 'on a les isomorphismes suivants', "
    "i) 'pour tout', 'et pour tout', ii) 'pour tout'; Lemme (p. 442) 'Soit', 'un morphisme projectif et parfait', 'avec', "
    "'quasi-compact', 'et soit', 'un complexe parfait sur', 'acyclique en degrés', 'Alors il existe un entier', "
    "'tel que pour', 'le complexe', 'soit acyclique en degrés'; Prop. 3.6 'Avec les hypothèses et les notations de', 'et', "
    "'on a', 'la relation'; Th. 3.7 'Soient', 'une immersion fermée régulière', 'le schéma obtenu en faisant éclater', "
    "'et', 'de sorte qu'on a le diagramme commutatif', p. 445 'On suppose que', 'est quasi-compact et a un faisceau ample', "
    "'Alors', 'on a', 'la suite exacte', 'où on pose', 'pour', 'et pour', 'les notations étant celles de', 'et', "
    "'En outre', 'admet un inverse à gauche', 'défini par', 'Si de plus', 'est noethérien', 'et', 'régulier', 'alors', "
    "'est surjectif', 'donc on a la suite exacte'; letters, formulas, numbers and punctuation plain; the labels underline "
    "only the word",
    "the statements in roman (no \\underline, no \\emph)",
    "underline", "high", None,
    "Exposé VII follows the Exposé II pattern of GLOBAL_ISSUES 82 (pending volume decision), as findings_416_420, "
    "426_430 and 431_435 report: not itemized. No emphasized defined terms and no category letter on pp. 441-445.")

add(441, "letters of sheaves and complexes on pp. 441-445",
    "underlined in the print (both scans): every M of p. 441 (fini M, Ri_*(M), i_*(M), Tor_i(M,O_X'), M⊗), the F of "
    "∧^iF (twice) and J of J^n (p. 441); L˙ (twice), N of P(N), every J and S (p. 442); every S, L'', L', M'', M', "
    "L''_n, L'_n, J^n, M''(n), M'(n) (p. 443); every J, the N of S(N) (p. 444). Plain in the print: X, Y, X', Y', x, y, "
    "y', u, v, f, g, i, j, p, P, T_i, f_i, and the F of λ_{-1}(F), λ^i(F) (pp. 441, 445)",
    "all plain",
    "underline", "high", None,
    "Convention of the Exposé VII transcription (findings_416_420 ff.): not itemized. The underlined O of O_X, O_Y, "
    "O_X', O_Y', O_P written \\cO falls under the pending volume decision. Three examples, in the form to use if the "
    "diplomatic layer reproduces the underline: p. 441 'de type fini \\(M\\). L'élément' -> 'de type fini "
    "\\(\\underline{M}\\). L'élément'; p. 442 'on peut supposer \\(J\\) défini' -> 'on peut supposer "
    "\\(\\underline{J}\\) défini'; p. 443 'une présentation finie graduée de \\(S\\) sur' -> 'une présentation finie "
    "graduée de \\(\\underline{S}\\) sur'.")

add(441, "K˙ on pp. 441-445: 'x ∈ K˙(Y)', 'la classe dans K˙(X')' (p. 441); 'Id_{K˙(X)}', 'x ∈ K˙(X)' (p. 444); "
         "the two exact sequences of Théorème 3.7, 'pour y ∈ K˙(Y)', 'y' ∈ K˙(Y'), x ∈ K˙(X)', 'Si y ∈ K˙(Y)', "
         "'x ∈ K˙(X), y' ∈ K˙(Y')' (p. 445)",
    "K with a raised dot in all 18 places (both scans; crops_441_445/c441_KY.png, w441_top_half.png)",
    "K^\\circ (18 places: 2 on p. 441, 2 on p. 444, 14 on p. 445)",
    "symbol", "high", None,
    "The Exposé VII convention reported in findings_416_420 (one script K^\\circ -> K^{\\bullet} for VII, both "
    "layers): not itemized. Three examples: p. 441 'pour tout \\(x\\in K^\\circ(Y)\\)' -> 'pour tout "
    "\\(x\\in K^{\\bullet}(Y)\\)'; p. 444 '\\Id_{K^\\circ(X)}' -> '\\Id_{K^{\\bullet}(X)}'; p. 445 'où on pose, pour "
    "\\(y\\in K^\\circ(Y)\\)' -> 'où on pose, pour \\(y\\in K^{\\bullet}(Y)\\)'. No old string below contains K^\\circ, "
    "so the entries apply before or after the script.")

# ---------------------------------------------------------------- p. 441
add(441, "'Les faisceaux d'homologie du complexe ainsi obtenu sont les Tor_i^{O_X}(M,O_X')'",
    "Tor underlined, the sheaf Tor of O_X-Modules (both scans)",
    "\\Tor plain", "underline", "high",
    (r"sont les \(\Tor_i", r"sont les \(\underline{\Tor}_i"),
    "\\underline{\\Tor}, the form of findings_431_435 (Exposé VII writes all its sheaf Tor plain).")

add(441, "display 'Tor_i^{O_X}(M,O_X') ≃ M⊗_{O_Y} Tor_i^{O_X}(O_X',O_Y) ≃ M⊗_{O_Y} ∧^iF', left member",
    "Tor underlined (both scans)",
    "\\Tor plain", "underline", "high",
    (r"\[<NL>\Tor_i^{\cO_X}(M,\cO_{X'})", r"\[<NL>\underline{\Tor}_i^{\cO_X}(M,\cO_{X'})"),
    "As above.")

add(441, "same display, middle member M⊗_{O_Y} Tor_i^{O_X}(O_X',O_Y)",
    "Tor underlined (both scans)",
    "\\Tor plain", "underline", "high",
    (r"M\otimes_{\cO_Y}\Tor_i", r"M\otimes_{\cO_Y}\underline{\Tor}_i"),
    "As above.")

add(441, "'L'élément f^*(i_*(x)) est alors la classe du complexe Lf^*(Ri_*(M))': the L",
    "L with a double underline, the double-struck L of the derived functor (both scans; crops_441_445/w441_top_half.png)",
    "\\mathrm Lf^*", "font", "high",
    (r"alors la classe du complexe \(\mathrm L", r"alors la classe du complexe \(\mathbb L"),
    "Double-struck L written plain (reported singly as asked); \\mathbb L as in Exposé I (main.tex lines 2949-3033). "
    "Independent of the R entry of the same formula (no common text).")

add(441, "same formula Lf^*(Ri_*(M)): the R",
    "R with a double underline, the double-struck R of the derived functor (both scans)",
    "Ri_*(M)", "font", "high",
    (r"(Ri_*(M))\), obtenu", r"(\mathbb Ri_*(M))\), obtenu"),
    "Double-struck R written plain; \\mathbb R as in the applied fixes of pp. 167-217 and the p. 435 entry of "
    "findings_431_435.")

add(441, "'obtenu en prenant une résolution projective de i_*(M) et en lui appliquant le foncteur f_*'",
    "'foncteur f_*.' with the asterisk low, as an index (both scans; crops_441_445/c441_fonct.png, w441_top_half.png)",
    "le foncteur \\(f_*\\) (printed reading kept)",
    "misprint_in_print", "high", None,
    "The complex is Lf^*(Ri_*(M)): one resolves i_*(M) on X and applies the inverse image f^* (f_* goes from X' to X "
    "and does not apply to a complex on X). The current layer also reads f_*: the corrected edition needs f^*.",
    corrected="le foncteur \\(f^*\\)")

add(441, "'Il en résulte que ces faisceaux d'homologie sont localement libres'",
    "begins a new, indented paragraph after the Tor display (both scans)",
    "'\\]' followed directly by 'Il en résulte' (the paragraph runs on)",
    "other", "high",
    (r"\]<NL>Il en résulte", r"\]<NL><NL>Il en résulte"),
    "Missing paragraph break.")

add(441, "'la classe dans K˙(X') du complexe Lf^*(Ri_*(M)) est la somme alternée': the L",
    "L with a double underline (both scans; crops_441_445/w441_bot_half.png)",
    "\\mathrm Lf^*", "font", "high",
    (r"(X')\) du complexe \(\mathrm L", r"(X')\) du complexe \(\mathbb L"),
    "As in the first Lf^*; the old leaves out the K^\\circ before it.")

add(441, "same formula Lf^*(Ri_*(M)): the R",
    "R with a double underline (both scans)",
    "Ri_*(M)", "font", "high",
    (r"(Ri_*(M))\) est la somme", r"(\mathbb Ri_*(M))\) est la somme"),
    "As in the first Ri_*(M).")

add(441, "'On peut évidemment supposer X affine, donc quasi-compact.' after Lemme 3.5 ii)",
    "begins a new, indented paragraph (both scans)",
    "'\\end{enumerate}' followed directly by 'On peut' (set as a continuation, without indent)",
    "other", "high",
    (r"\end{enumerate}<NL>On peut", r"\end{enumerate}<NL><NL>On peut"),
    "Missing paragraph break.")

add(441, "last line: 'i) Rappelons d'abord le lemme suivant, qui a été démontré dans exp.'",
    "'dans exp.' ends the page; no number follows (both scans; crops_441_445/c441_exp.png, w441_bot_half.png); "
    "p. 442 begins with 'Lemme.'",
    "dans exp. III. (silently completed)",
    "misprint_in_print", "high",
    (r"dans exp. III.", r"dans exp."),
    "The typescript leaves out the number of the exposé; the lemma recalled on p. 442 is III, Corollaire 2.3 "
    "(main.tex line 5775). The current layer also reads 'dans exp. III.' (the corrected edition keeps it).",
    corrected="dans exp. III.")

# ---------------------------------------------------------------- p. 442
add(442, "Lemme: 'et soit L˙ un complexe parfait sur O_X''",
    "L with a raised dot (L˙), underlined (both scans; crops_441_445/c442_Ldot.png, w442_top_half.png)",
    "\\(L'\\) (a prime)", "symbol", "high",
    (r"soit \(L'\) un complexe", r"soit \(L^\bullet\) un complexe"),
    "L^\\bullet is the file's form for this complex (p. 435: Ri_*(L^\\bullet)). The underline falls under the "
    "convention for sheaf letters.")

add(442, "Lemme: 'le complexe Rf_*(L˙⊗_{O_X'}O_X'(n))': the R",
    "R with a double underline (both scans; crops_441_445/c442_RfL.png)",
    "\\(Rf_*", "font", "high",
    (r"le complexe \(Rf_*", r"le complexe \(\mathbb Rf_*"),
    "As on p. 441; independent of the L˙ entry of the same formula.")

add(442, "same formula: the L˙ of Rf_*(L˙⊗_{O_X'}O_X'(n))",
    "L with a raised dot, underlined (both scans; crops_441_445/c442_RfL.png)",
    "L' (a prime)", "symbol", "high",
    (r"\bigl(L'\otimes", r"\bigl(L^\bullet\otimes"),
    "As above.")

add(442, "'Or on a Rf_*(O_Y'(n)) = i_*∘Rg_*(O_Y'(n))': the first R",
    "R with a double underline (both scans; page_442_s2.png, w442_top_half.png)",
    "\\(Rf_*", "font", "high",
    (r"Or on a \(Rf_*", r"Or on a \(\mathbb Rf_*"),
    "As on p. 441.")

add(442, "same formula: the R of Rg_*",
    "R with a double underline (both scans)",
    "Rg_*", "font", "high",
    (r"\circ Rg_*", r"\circ\mathbb Rg_*"),
    "As on p. 441.")

# ---------------------------------------------------------------- p. 443
add(443, "start of page (folio-443 marker)",
    "p. 442 ends '... O_X[T_1,...,T_d] →v S, surjectif, en envoyant'; p. 443 begins 'T_i sur f_i^{(1)}. Cet "
    "homomorphisme définit une immersion fermée' (both scans; page_442_s4.png, page_443_s1.png)",
    "page_442.tex ends 'en envoyant \\(T_i\\) sur \\(f_i^{(1)}\\). Cet' above the folio-443 marker; page_443.tex "
    "begins 'homomorphisme définit'",
    "marker", "high", None,
    "Page 443 really begins at '\\(T_i\\) sur \\(f_i^{(1)}\\). Cet'. Exact edit in main.tex, both layers (diplomatic "
    "lines 11167-11169, current 11173-11175): replace 'en envoyant \\(T_i\\) sur \\(f_i^{(1)}\\). Cet\\n%%%%%%%%%%  "
    "scan idx 456  |  folio 443  %%%%%%%%%%\\nhomomorphisme définit' by 'en envoyant\\n%%%%%%%%%%  scan idx 456  |  "
    "folio 443  %%%%%%%%%%\\n\\(T_i\\) sur \\(f_i^{(1)}\\). Cet homomorphisme définit' (old string once per layer; "
    "simulated in memory: crops_441_445/build_findings.py). The sentence runs on, so no blank line. "
    "python -I move_marker.py 6 443 '\\(T_i\\) sur' --before gives the same page split.")

add(443, "'où M'' = Proj(L''), M' = Proj(L')': the first Proj",
    "Proj underlined (both scans; crops_441_445/c443_proj.png, w443_proj.png)",
    "\\Proj (= \\operatorname{Proj}, plain)", "underline", "high",
    (r"\(M''=\Proj(L'')\)", r"\(M''=\underline{\Proj}(L'')\)"),
    "The Proj of a graded Module, underlined as the sheaf Tor; Exposé VII renews \\Projz plain (main.tex line "
    "10497) and has no underlined Proj.")

add(443, "same line: the second Proj",
    "Proj underlined (both scans)",
    "\\Proj plain", "underline", "high",
    (r"\(M'=\Proj(L')\)", r"\(M'=\underline{\Proj}(L')\)"),
    "As above.")

add(443, "diagram of p. 443 (L''_n → L'_n → J^n → 0 over p_*(M''(n)) → p_*(M'(n)) → p_*(O_X'(n)) → 0), right-hand column",
    "three vertical arrows only, under L''_n, L'_n and J^n; no arrow joins the two 0 of the right-hand column (both "
    "scans; crops_441_445/c443_diag_top.png, w443_mid.png)",
    "0 \\arrow[d] (a fourth vertical arrow)", "extra", "high",
    (r"0 \arrow[d]\\", r"0\\"),
    "The diagram of p. 444 has its two outer vertical arrows; this one does not.")

# ---------------------------------------------------------------- p. 444
add(444, "display 'f_*(O_Y'(n)) = i_*(g_*(O_Y'(n))) = i_*(S(N)_n) = J^n/J^{n+1}'",
    "S with two underlines (the symmetric algebra, the typescript's bold S), N underlined (both scans; "
    "crops_441_445/c444_SN.png, w444_top.png)",
    "S(N)_n (a plain S)", "font", "high",
    (r"i_*(S(N)_n)", r"i_*(\mathbf S(N)_n)"),
    "\\mathbf S, the form proposed for the doubly underlined S of pp. 425-428 (findings_426_430: \\cS -> \\mathbf S) "
    "and the bold S of Exposé VI's \\Sym; here the TeX has a roman S. The underline of N falls under the convention "
    "for sheaf letters.")

add(444, "'celle du milieu en est donc un également' (end of the paragraph before Proposition 3.6)",
    "no full stop after 'également' (both scans; crops_441_445/c444_egal.png, w444_top.png)",
    "un également. (silently corrected)",
    "misprint_in_print", "high",
    (r"un également.", r"un également"),
    "The typist's dropped full stop at the end of the paragraph; the current layer has it (the corrected edition "
    "keeps it).",
    corrected="un également.")

add(444, "'Soit x ∈ K˙(X) ; on peut écrire, d'après la formule de projection :'",
    "begins a new, indented paragraph after the display of Proposition 3.6 (both scans; w444_bot.png)",
    "'\\]' followed directly by 'Soit' (the paragraph of the statement runs on)",
    "other", "high",
    (r"\]<NL>Soit \(x\in", r"\]<NL><NL>Soit \(x\in"),
    "Missing paragraph break; the old stops before the K^\\circ.")

add(444, "'Or 3.5 montre que la cohomologie de ℝf_*(O_X') est nulle'",
    "begins a new, indented paragraph after 'Il suffit donc de montrer que f_*(1) = 1.' (both scans; w444_bot.png)",
    "one paragraph with 'Il suffit donc ...'",
    "other", "high",
    (r"\(f_*(1)=1\). Or 3.5", r"\(f_*(1)=1\).<NL><NL>Or 3.5"),
    "Missing paragraph break.")

add(444, "same sentence: ℝf_*(O_X')",
    "a double-struck R, typed as R overstruck with I (both scans; crops_441_445/c444_IR.png, w444_bot.png)",
    "\\(Rf_*(\\cO_{X'})\\)", "font", "high",
    (r"de \(Rf_*(\cO_{X'})\)", r"de \(\mathbb Rf_*(\cO_{X'})\)"),
    "As on p. 441; independent of the paragraph entry above (no common text).")

# ---------------------------------------------------------------- p. 445
add(445, "diagram of Théorème 3.7: label i of the bottom arrow Y → X",
    "i above the arrow (both scans; page_445_s1.png)",
    "\\arrow[r,\"i\"'] (label below the arrow)", "formula", "medium",
    (r"""\arrow[r,"i"']""", r"""\arrow[r,"i"]"""),
    "j, g and f stand where the TeX sets them (above, left, right). Same kind of entry as p. 59 (findings_056_060).")

add(445, "Théorème 3.7: 'Si de plus X est noethérien, et Y régulier, alors v est surjectif'",
    "begins a new, indented paragraph of the statement (both scans)",
    "one paragraph with 'les notations étant celles de 3.1 et 3.3 ...'",
    "other", "high",
    (r"g_*(y')\).<NL>Si de plus", r"g_*(y')\).<NL><NL>Si de plus"),
    "Missing paragraph break.")

add(445, "display 'g_*(g^*(y).λ_{-1}(F)) = y.g_*(λ_{-1}(F))' before 'd'après la formule de projection'",
    "no punctuation after the display (both scans; crops_441_445/c445_disp_proj.png, w445_bot.png)",
    "=y.g_*(\\lambda_{-1}(F)),", "punctuation", "high",
    (r"=y.g_*(\lambda_{-1}(F)),", r"=y.g_*(\lambda_{-1}(F))"),
    "The comma is the TeX's addition.")

add(445, "'Par ailleurs, g_*(λ_{-1}(F)) = 1 (VI 5.9) d'où le résultat.'",
    "no comma after '(VI 5.9)', which ends the line; 'd'où le résultat.' opens the next (both scans; "
    "crops_441_445/c445_VI59.png, w445_bot.png)",
    "(VI 5.9), d'où (silently corrected)",
    "misprint_in_print", "medium",
    (r"(VI 5.9), d'où", r"(VI 5.9) d'où"),
    "The typist's dropped comma before 'd'où'; the current layer has it (the corrected edition keeps it).",
    corrected="(VI 5.9), d'où")

add(445, "display 'v∘u(y) = v(g^*(y)λ_{-1}(F),-i_*(y)) = j_*(g^*(y)λ_{-1}(F)) - f^*(i_*(x)) = 0 ,'",
    "'f^*(i_*(x))' (both scans; crops_441_445/w445_bot.png)",
    "f^*(i_*(x)) (printed reading kept)",
    "misprint_in_print", "high", None,
    "v∘u(y) = j_*(g^*(y)λ_{-1}(F)) - f^*(i_*(y)), which 3.4 makes 0; the proof has no x here. The current layer "
    "already reads f^*(i_*(y)).",
    corrected="f^*(i_*(y))")

add(445, "end of page (folio-446 marker)",
    "p. 445 ends 'Soient donc x ∈ K˙(X), y' ∈ K˙(Y'), tels que :'; p. 446 begins with the display "
    "'j_*(y') + f^*(x) = 0 .' and 'Il faut trouver y ∈ K˙(Y) tel que :' (both scans; page_445_s4.png, "
    "crops_441_445/w446_top.png)",
    "page_445.tex ends with the display '\\[ j_*(y')+f^*(x)=0. \\]' and the word 'Il' above the folio-446 marker",
    "marker", "high", None,
    "Page 446 really begins at the display '\\[\\nj_*(y')+f^*(x)=0.\\n\\]'. Exact edit in main.tex, both layers "
    "(diplomatic lines 11274-11280, current 11280-11286): replace 'tels que:\\n\\[\\nj_*(y')+f^*(x)=0.\\n\\]\\nIl\\n"
    "%%%%%%%%%%  scan idx 459  |  folio 446  %%%%%%%%%%\\nfaut trouver' by 'tels que:\\n%%%%%%%%%%  scan idx 459  |  "
    "folio 446  %%%%%%%%%%\\n\\[\\nj_*(y')+f^*(x)=0.\\n\\]\\nIl faut trouver' (old string once per layer; simulated in "
    "memory: crops_441_445/build_findings.py). The checker of p. 446 may report the same boundary: apply once.")

# ---------------------------------------------------------------- checks
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
ok = True
pages = {p: (B / f"page_{p}.tex").read_text(encoding="utf-8") for p in range(441, 446)}
work = dict(pages)
for d in F:
    if d["fix"] is None:
        continue
    t = pages[d["page"]]
    old, new = d["fix"]["old"], d["fix"]["new"]
    n = t.count(old)
    if n != 1 or MARK.search(old) or "%%%%" in old:
        ok = False
        print("BAD old", d["page"], n, repr(old))
    w = work[d["page"]]
    if w.count(old) != 1:
        ok = False
        print("OVERLAP after earlier fixes", d["page"], repr(old))
    else:
        work[d["page"]] = w.replace(old, new, 1)
for p in pages:
    if MARK.findall(work[p]) != MARK.findall(pages[p]):
        ok = False
        print("marker changed", p)

M443_OLD = ("en envoyant \\(T_i\\) sur \\(f_i^{(1)}\\). Cet\n%%%%%%%%%%  scan idx 456  |  folio 443  %%%%%%%%%%\n"
            "homomorphisme définit")
M443_NEW = ("en envoyant\n%%%%%%%%%%  scan idx 456  |  folio 443  %%%%%%%%%%\n"
            "\\(T_i\\) sur \\(f_i^{(1)}\\). Cet homomorphisme définit")
M446_OLD = ("tels que:\n\\[\nj_*(y')+f^*(x)=0.\n\\]\nIl\n%%%%%%%%%%  scan idx 459  |  folio 446  %%%%%%%%%%\n"
            "faut trouver")
M446_NEW = ("tels que:\n%%%%%%%%%%  scan idx 459  |  folio 446  %%%%%%%%%%\n\\[\nj_*(y')+f^*(x)=0.\n\\]\n"
            "Il faut trouver")
for layer in ("diplomatic", "current"):
    t = (SGA6 / layer / "main.tex").read_text(encoding="utf-8")
    for old, new, folio, start in ((M443_OLD, M443_NEW, 443, "\\(T_i\\) sur"), (M446_OLD, M446_NEW, 446, "\\[\nj_*(y')")):
        c = t.count(old)
        if c != 1:
            ok = False
            print(layer, folio, "marker old count", c)
            continue
        line = t[:t.index(old)].count("\n") + 1
        t2 = t.replace(old, new, 1)
        m = next(m for m in MARK.finditer(t2) if int(m.group(2)) == folio)
        after = t2[m.end() + 1:m.end() + 1 + len(start)]
        print(layer, folio, "old starts on line", line, "| page now begins", repr(after), after == start)
        ok &= after == start
        # same page split by move_marker.py's rule (folio 443 only), on a copy in memory
        if folio == 443:
            m0 = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
            end = m0.end() + 1
            t3 = t[:m0.start()] + t[end:]
            k = t3.rfind(start, 0, m0.start())
            ls = t3.rfind("\n", 0, k) + 1
            t3 = t3[:k] + "\n" + m0.group(0) + "\n" + t3[k:] if t3[ls:k].strip() else t3
            m3 = next(m for m in MARK.finditer(t3) if int(m.group(2)) == folio)
            print("   move_marker rule: page begins", repr(t3[m3.end() + 1:m3.end() + 40]))
print("findings", len(F), "ok", ok)
if ok:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    print("written", OUT)
