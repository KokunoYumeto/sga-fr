"""Build findings_061_065.json for SGA 6 pp. 61-65, check every fix's old (exactly once in its page file, applied in
the listed order, and also in the untouched page file), and write the JSON. Nothing in the .tex files is changed."""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b061_065"
NL = "\n"
F = []


def fx(old, new):
    return {"old": old, "new": new}


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- p. 61
add(61, "start of page",
    "p. 61 begins 'Ã soumis aux restrictions ε(ξ_i) = 0 et η_j = [...]'; p. 60 ends '... et aux E_j des éléments η_j de'"
    " (both scans; DjVu witness pp. 71-72)",
    r"the first part of the statement of Théorème 2.14, '\emph{Soient $x_i$ ... des éléments $\eta_j$ de', stands under"
    r" the folio-61 marker",
    "marker", "high", None,
    r"Page 61 really begins with '$\Atil$ soumis aux restrictions'. Move the folio-61 marker down, inside the \emph group:"
    r" python -I move_marker.py 6 61 '$\Atil$ soumis aux restrictions' (forward search, single quotes; simulated on both"
    r" layers: '... des éléments $\eta_j$ de ' / marker / '$\Atil$ soumis aux restrictions ...'). Same move as the"
    r" end-of-page entry of p. 60 in findings_056_060.json: apply once.")

add(61, "first line, η_j = [n_j, 1 + η_j^(1) + ... + η_j^(nj)]",
    "last term η_j^(nj): the j of n_j typed on the line of the n, inside the superscript (both scans)",
    r"\eta_j^{(n_j)}",
    "misprint_in_print", "low", fx(r"\eta_j^{(n_j)}]", r"\eta_j^{(nj)}]"),
    "The typist did not lower the j of the index inside the superscript; the TeX writes n_j. Apply only if the diplomatic"
    " layer keeps such typewriter forms of nested indices; the corrected layer keeps n_j.",
    corrected=r"\eta_j^{(n_j)}]")

add(61, "Théorème 2.14, '(donc η_j^(k) = 0 pour k > n_j), on ait :'",
    "the parenthesis '(donc ... pour k > n_j),' is not underlined; 'on ait' is (both scans)",
    r"the whole remark inside the \emph of the statement",
    "underline", "high",
    fx(r" (donc $\eta_j^{(k)}=0$ pour $k>n_j$), on ait}", r"} (donc $\eta_j^{(k)}=0$ pour $k>n_j$), \emph{on ait}"),
    "Close the emphasis before the parenthetical remark and reopen it at 'on ait', as for Propositions 1.2 and 1.3"
    " (pp. 30, 32). Either order with the next entry works.")

add(61, "Théorème 2.14, 'on ait :'",
    "on ait : (colon, both scans)",
    "on ait} (no colon)",
    "punctuation", "high", fx("on ait}", "on ait}~:"),
    "The TeX drops the printed colon before the display.")

add(61, "display R((λ^k(ξ_i)),(λ^k(η_j))) ∈ Ã^p",
    "no punctuation after Ã^p (both scans)",
    r"\in\Atil^p.",
    "punctuation", "high", fx(r"\in\Atil^p.", r"\in\Atil^p"),
    "The TeX adds a full stop at the end of the display.")

add(61, "footnote call (*), display R((λ^k(x'_i)),(λ^k(γ(E'_j))) ∈ K(X)^p",
    "the footnote's only call is the (*) typed to the right of the display, followed by the full stop: 'K(X)^p   (*)   .'"
    " (both scans); equation numbers stand at the left in this typescript ((2.35), (2.36)); nothing is printed after"
    " 'on a'",
    r"\footnote{...} called after 'on a}', and the display tagged \tag{*}",
    "other", "medium",
    fx(r"on a}\footnote{",
       r"on a}" + NL + r"\[" + NL + r" R((\lambda^k(x'_i)),(\lambda^k(\gamma(E'_j))))\in\underline K(X)^p\qquad"
       r"\text{\footnotemark}\ ." + NL + r"\]" + NL + r"\footnotetext{"),
    r"Moves the call to the place of the printed (*), with the \footnotemark/\footnotetext pair already used in"
    r" main.tex (\text{\footnotemark} in a display, then \footnotetext). Apply together with the next entry, which"
    r" deletes the old display; then the misprint entry of the same display.")

add(61, "same display (old copy)",
    "(see the previous entry)",
    r"\begin{equation}\tag{*} ... \end{equation} after the footnote",
    "other", "medium",
    fx(r"\begin{equation}\tag{*}" + NL + r" R((\lambda^k(x'_i)),(\lambda^k(\gamma(E'_j))))\in\underline K(X)^p." + NL
       + r"\end{equation}" + NL, ""),
    "Apply right after the previous entry (the display now stands before the footnote text). The misprint entry"
    " below comes after both.")

add(61, "display R((λ^k(x'_i)),(λ^k(γ(E'_j))) ∈ K(X)^p, closing parentheses",
    "(λ^k(γ(E'_j))) ∈: three closing parentheses after E'_j, so the parenthesis opened after R is never closed (both"
    " scans)",
    "four closing parentheses (silently corrected)",
    "misprint_in_print", "high", fx(r"\gamma(E'_j))))", r"\gamma(E'_j)))"),
    "Apply after the two footnote-call entries above (in between, the display exists twice). Diplomatic layer: three"
    " parentheses; the corrected layer keeps four.",
    corrected=r"\gamma(E'_j))))")

add(61, "proof of Théorème 2.14, 'qu'on est ramené au cas où X est un produit de grasmaniennes.'",
    "'on est ramené au cas où' and 'est un produit de grasmaniennes' underlined; qu', X and the full stop not (both"
    " scans)",
    "no emphasis",
    "underline", "high",
    fx(r"qu'on est ramené au cas où $X$ est un produit de grasmaniennes.",
       r"qu'\emph{on est ramené au cas où} $X$ \emph{est un produit de grasmaniennes}."),
    "Missing underline.")

add(61, "footnote (*), 'l'hypothèse faite implique si R est exprimé'",
    "implique  si (no comma; a wide space, both scans); the comma after 'que' is printed",
    "implique, si",
    "punctuation", "high", fx("implique, si", "implique si"),
    "The TeX adds a comma.")

add(61, "footnote (*), 'en termes des γ^k(ξ_i), γ^k(E_i-ε(E_i))'",
    "E_i - ε(E_i) (index i, both scans)",
    r"\gamma^k(E_i-\varepsilon(E_i)) (printed reading kept)",
    "misprint_in_print", "medium", None,
    "The bundles are E_j (1 ≤ j ≤ r) in the statement; i indexes the x_i. The TeX keeps the printed reading.",
    corrected=r"\gamma^k(E_j-\varepsilon(E_j))")

# ---------------------------------------------------------------- p. 62
add(62, "start of page",
    "p. 62 begins 'Ã (où A est un anneau gradué), compatible avec les filtrations'; p. 61 ends with the first two lines"
    " of Lemme 2.15, '... sans torsion de la forme' (both scans; DjVu witness pp. 72-73)",
    r"'\emph{Supposons que $X$ soit ... de la forme' (printed on p. 61) stands under the folio-62 marker",
    "marker", "high", None,
    r"Page 62 really begins with '$\Atil$ (où'. Move the folio-62 marker down, inside the \emph group: python -I"
    r" move_marker.py 6 62 '$\Atil$ (où' (forward search, single quotes; simulated on both layers: '... sans torsion de"
    r" la forme ' / marker / '$\Atil$ (où $A$ est un anneau gradué), ...'). The moved text agrees with the print of"
    " p. 61.")

add(62, "Lemme 2.15 (first), 'G(K(X)) ⟶ G(A) soit injectif'",
    "G(K(X)): this K is not underlined (both scans), unlike K(X) in the line above",
    r"G(\underline K(X)) (silently corrected)",
    "misprint_in_print", "medium",
    fx(r"G(\underline K(X))\longrightarrow G(A)", r"G(K(X))\longrightarrow G(A)"),
    "The typist dropped the underline of K, as in (2.34) on p. 59; the corrected layer reads \\underline K.",
    corrected=r"G(\underline K(X))\longrightarrow G(A)")

add(62, "'Pour le prouver le lemme, nous utiliserons'",
    "Pour le prouver le lemme (both scans)",
    "Pour le prouver le lemme (printed reading kept)",
    "misprint_in_print", "medium", None,
    "One object too many: 'le' and 'le lemme'. The TeX keeps the printed reading.",
    corrected="Pour prouver le lemme")

add(62, "before 'Nous considérerons l'homomorphisme C̃'",
    "'(cf. § 5).' ends a short line; 'Nous considérerons' starts an indented new paragraph (both scans)",
    r"(cf.\ \S 5). Nous considérerons (same paragraph)",
    "other", "high", fx(r"(cf.\ \S 5). Nous", r"(cf.\ \S 5)." + NL + NL + "Nous"),
    "Missing paragraph break.")

add(62, "'comme X est un produit de grasmaniennes C_j'",
    "C_j (typed C, both scans)",
    "C_j (printed reading kept)",
    "misprint_in_print", "low", None,
    "The grassmannian is G on p. 61, and C̃, C^i name the Chow maps in the same paragraph; G_j is probably meant. The"
    " TeX keeps the printed reading.",
    corrected="G_j")

add(62, "before 'De a) résulte que φ : A(X) ⟶ G(K(X))'",
    "'De a) résulte' is indented like the items a), b) and the other new paragraphs (both scans)",
    r"\end{enumerate} followed directly by 'De a)'",
    "other", "medium", fx(r"\end{enumerate}" + NL + "De a)", r"\end{enumerate}" + NL + NL + "De a)"),
    "Missing paragraph break (text that continues a sentence after a display or list starts at the margin, as 'où,"
    " par définition' on p. 65).")

# ---------------------------------------------------------------- p. 63
add(63, "start of page",
    "p. 63 begins '1 pour F = O_(x) pour tout x ∈ X.'; p. 62 ends '... cette fonction est égale à' (both scans)",
    "'$1$' is the last token of page_062.tex (under the folio-62 marker); page_063.tex begins 'pour $F=...'",
    "marker", "high", None,
    r"Page 63 really begins with '$1$'. Move the folio-63 marker before it: python -I move_marker.py 6 63 '$1$'"
    r" --before (single quotes; the last '$1$' before the marker is that one; simulated on both layers: '... est égale"
    r" à ' / marker / '$1$' / 'pour $F=\cO_{(x)}$ ...').")

add(63, "'que l'application C̃ de K(X) dans Ã(X) est surjective'",
    "a wide hand-drawn tilde over the whole A(X) (both scans); on p. 62 'dans Ã(X)' has the typed tilde over A only",
    r"$\Atil(X)$ (\Atil = \widetilde A)",
    "formula", "medium", fx(r"dans $\Atil(X)$ est surjective", r"dans $\widetilde{A(X)}$ est surjective"),
    r"As \widetilde{G(\underline K(X))} in (Th. 2.16) and the wide hat of p. 32.")

add(63, "'de G(K(X)) dans G(Ã(X)) est bijectif'",
    "the same wide tilde over A(X) (both scans)",
    r"$G(\Atil(X))$",
    "formula", "medium", fx(r"$G(\Atil(X))$", r"$G(\widetilde{A(X)})$"),
    "As the previous entry.")

add(63, "heading '§ 5. Définition faisceautique des classes de Chern. ...'",
    "§ 5. (section sign, both scans)",
    r"\subsection*{5. Définition ...}",
    "missing", "high", fx(r"\subsection*{5. Définition", r"\subsection*{\S 5. Définition"),
    r"As § 4 on p. 54 (applied); §§ 1-4 of this chapter have \S.")

add(63, "end of the heading '... des morphismes d'injection.'",
    "d'injection. (full stop after the underlined title, both scans; § 4 on p. 54 has none)",
    r"... d'injection} (no full stop)",
    "punctuation", "medium", fx("morphismes d'injection}", "morphismes d'injection.}"),
    "The printed heading ends with a full stop.")

add(63, "Théorème 2.16, 'pour tout x ∈ K(X), et pour tout entier i ≥ 0'",
    "x ∈ K(X): this K is not underlined (both scans), unlike G^i(K(X)) and K(X)^{i+1} two lines below",
    r"x\in\underline K(X) (silently corrected)",
    "misprint_in_print", "medium", fx(r"pour tout $x\in\underline K(X)$", r"pour tout $x\in K(X)$"),
    "Dropped underline of K, as on p. 62; the corrected layer reads \\underline K.",
    corrected=r"pour tout $x\in\underline K(X)$")

add(63, "Théorème 2.16, display c̃(x) = [ε(x), 1 + Σ c^i(x)], index of the sum",
    "Σ with index i≥φ: the last character is the typed φ (same glyph as 'que φ' on p. 62), not a 0 (both scans)",
    r"\sum_{i\geq0} (silently corrected)",
    "misprint_in_print", "high", fx(r"\sum_{i\geq0}c^i(x)", r"\sum_{i\geq\varphi}c^i(x)"),
    "Diplomatic layer: φ as printed. For the corrected layer the sum must start at 1: c^0(x) is the class of"
    " γ^0 = 1, already written as the leading 1 (the elements of Ã are [n, 1 + Σ_{i≥1} x^i], Chap. I § 3); the TeX's"
    " i≥0 counts it twice. If only the typist's φ is to be undone, the reading is i≥0.",
    corrected=r"\sum_{i\geq1}c^i(x)")

# ---------------------------------------------------------------- p. 64
add(64, "start of page",
    "p. 64 begins '(2.8) résulte de (2.31).' and 'cqfd'; p. 63 ends '... se vérifie immédiatement, et' (both scans)",
    "'(2.8) résulte de (2.31).' ends the last line of page_063.tex (under the folio-63 marker)",
    "marker", "high", None,
    "Page 64 really begins with '(2.8)'. Move the folio-64 marker before it: python -I move_marker.py 6 64"
    " '(2.8) résulte' --before (simulated on both layers: '... se vérifie immédiatement, et ' / marker / '(2.8)"
    " résulte de (2.31).' / '\\begin{flushright}cqfd...').")

add(64, "'cqfd' after '(2.8) résulte de (2.31).'",
    "cqfd (no full stop, both scans; the cqfd of p. 63 has one)",
    "cqfd.",
    "punctuation", "high", fx(r"cqfd.\end{flushright}", r"cqfd\end{flushright}"),
    "The TeX adds a full stop.")

add(64, "label 'Corollaire 1' (of Théorème 2.16)",
    "Corollaire 1 : On a ... (colon, both scans)",
    r"\textbf{Corollaire 1.}",
    "punctuation", "medium", fx(r"\textbf{Corollaire 1.}", r"\textbf{Corollaire 1~:}"),
    "As pp. 57 and 59 (applied): the label's colon became a full stop.")

add(64, "proof of Corollaire 1, 'par la détermination explicité de K(Y)'",
    "explicité (accent on the last e, both scans)",
    "explicité (printed reading kept)",
    "misprint_in_print", "high", None,
    "The adjective is 'explicite'. The TeX keeps the printed reading.",
    corrected="explicite")

add(64, "label 'Corollaire 2'",
    "Corollaire 2 : Supposons que ... (colon, both scans)",
    r"\textbf{Corollaire 2.}",
    "punctuation", "medium", fx(r"\textbf{Corollaire 2.}", r"\textbf{Corollaire 2~:}"),
    "As Corollaire 1.")

add(64, "after (2.35), 'Comme φ est surjective'",
    "'Comme φ est surjective' starts an indented new paragraph (both scans)",
    r"\end{equation} followed directly by 'Comme'",
    "other", "high", fx(r"\end{equation}" + NL + "Comme", r"\end{equation}" + NL + NL + "Comme"),
    "Missing paragraph break (same kind of fix as p. 50, applied).")

add(64, "display γ^i(x - ε(X)) ≡ (-1)^{i-1}(i-1)! x mod K(X)^{i+1}",
    "ε(X): capital X (both scans; the x before it is small)",
    r"\varepsilon(X) (printed reading kept)",
    "misprint_in_print", "high", None,
    "ε is taken of the element x, as in Théorème 2.16 (γ^i(x - ε(x))). The TeX keeps the printed reading.",
    corrected=r"\gamma^i(x-\varepsilon(x))")

add(64, "'Comme ψ est injective, il suffit de prouver la relation analogue'",
    "'injective' underlined (both scans)",
    "plain 'injective'",
    "underline", "high", fx(r"Comme $\psi$ est injective", r"Comme $\psi$ est \emph{injective}"),
    "Missing underline.")

add(64, "label 'Remarque'",
    "Remarque : Le corollaire 2 ... (colon, both scans)",
    r"\textbf{Remarque.}",
    "punctuation", "medium", fx(r"\textbf{Remarque.}", r"\textbf{Remarque~:}"),
    "As the Corollaire labels above.")

# ---------------------------------------------------------------- p. 65
SHRIEK = ("the print writes the direct image with a lower shriek, i_! (an exclamation mark typed under the i), in all"
          " ten places of this page (both scans); the TeX has i_* in all ten, each given with its own fix; same as"
          " f_! on pp. 53-54 (applied)")
add(65, "'On a alors, pour i^! et i_! les formules suivantes :'",
    "et i_! (lower shriek, both scans)",
    "et $i_*$",
    "symbol", "high", fx("et $i_*", "et $i_!"),
    SHRIEK + ".")

add(65, "same line, after i_!",
    "'i_! les formules': no comma; the stroke right of the i is the stem of the lower shriek, whose dot is under it"
    " (same shape in (ii)-(iv), both scans)",
    "$i_*$, les formules",
    "punctuation", "medium", fx("$, les formules suivantes", "$ les formules suivantes"),
    "The TeX adds a comma (probably the shriek's stem read as a comma).")

add(65, "(ii), first line",
    "i_!(x.i^!(y)) = i_!(x).y (lower shriek twice)",
    r"$i_*(x.i^!(y))=i_*(x).y$",
    "symbol", "high", fx(r"$i_*(x.i^!(y))=i_*(x).y$", r"$i_!(x.i^!(y))=i_!(x).y$"),
    "Lower shriek, twice.")

add(65, "(ii), second line",
    "i_!i^!(y) = ξ y avec ξ = i_!i^!(1) = γ_X(Y) (lower shriek twice)",
    r"$i_*i^!(y)=\xi y$ avec $\xi=i_*i^!(1)",
    "symbol", "high", fx(r"$i_*i^!(y)=\xi y$ avec $\xi=i_*i^!(1)", r"$i_!i^!(y)=\xi y$ avec $\xi=i_!i^!(1)"),
    "Lower shriek, twice.")

add(65, "(iii), first line",
    "i^!(i_!(x)) = x.λ_{-1}(N)",
    r"$i^!(i_*(x))",
    "symbol", "high", fx(r"$i^!(i_*(x))", r"$i^!(i_!(x))"),
    "Lower shriek.")

add(65, "(iii), second line",
    "i^!(ξ) = i^!i_!(1) = λ_{-1}(N)",
    r"i^!i_*(1)",
    "symbol", "high", fx(r"i^!i_*(1)", r"i^!i_!(1)"),
    "Lower shriek.")

add(65, "(iv)",
    "i_!(x) i_!(x') = i_!(xx' λ_{-1}(N) (lower shriek three times)",
    r"$i_*(x)i_*(x')=i_*",
    "symbol", "high", fx(r"$i_*(x)i_*(x')=i_*", r"$i_!(x)i_!(x')=i_!"),
    "Lower shriek, three times. Does not overlap the misprint entry that follows.")

add(65, "(iv), closing parenthesis",
    "i_!(xx' λ_{-1}(N) , : the parenthesis opened after i_! is not closed (both scans)",
    r"i_*(xx'\lambda_{-1}(N)) (silently corrected)",
    "misprint_in_print", "high", fx(r"(xx'\lambda_{-1}(N))$", r"(xx'\lambda_{-1}(N)$"),
    "Diplomatic layer: one parenthesis, as printed; the corrected layer keeps two.",
    corrected=r"(xx'\lambda_{-1}(N))$")

add(65, "end of page",
    "p. 65 ends with (2.36) '... = O_Y(∧^i N) . )' and the footnote '(*) Non, cf. note de la page 30.'; p. 66 begins"
    " 'La formule (iv) exprime que i_! est' (DjVu witness p. 77)",
    "page_065.tex ends with the line 'La', which belongs to p. 66 (the folio-66 marker stands between 'La' and"
    " 'formule (iv)')",
    "marker", "high", None,
    "Move the folio-66 marker above 'La': python -I move_marker.py 6 66 'La' --before (the last 'La' before the"
    " marker is that line; simulated on both layers: ')' / marker / 'La' / 'formule (iv) exprime ...'). The checker"
    " of pp. 66-70 may report the same move: apply once.")

# ---------------------------------------------------------------- checks
orig = {p: (B / f"page_{p:03d}.tex").read_text(encoding="utf-8") for p in range(61, 66)}
cur = dict(orig)
MARK = re.compile(r"%%%%%%%%%%  scan idx")
bad = 0
for d in F:
    fix = d["fix"]
    if not fix:
        continue
    p, old, new = d["page"], fix["old"], fix["new"]
    n_orig, n_cur = orig[p].count(old), cur[p].count(old)
    flag = "" if (n_orig == 1 and n_cur == 1) else "  <-- CHECK"
    if n_cur != 1 or MARK.search(old) or MARK.search(new):
        bad += 1
    print(f"p.{p} {d['kind']:<17} orig={n_orig} seq={n_cur}{flag}  {old[:60]!r}")
    cur[p] = cur[p].replace(old, new, 1)
for p in cur:
    for ch in cur[p]:
        if ord(ch) < 32 and ch != "\n":
            print("control character in result of page", p, repr(ch))
            bad += 1
    if cur[p].count("{") != cur[p].count("}"):
        print("brace count changed on page", p, orig[p].count("{") - orig[p].count("}"),
              cur[p].count("{") - cur[p].count("}"))
s = json.dumps(F, ensure_ascii=False)
for ch in s:
    if 0x80 <= ord(ch) <= 0x9f or ch == "\u00a0":
        print("odd character in JSON", repr(ch))
        bad += 1
counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0])
    c[1 if d["kind"] == "misprint_in_print" else 0] += 1
print("counts (normal/misprint):", counts, "total", len(F))
if bad:
    sys.exit(f"{bad} problems; JSON not written")
out = RUN / "findings_061_065.json"
out.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print("written", out)
print("---- p. 61 after all fixes, around the display (*):")
i = cur[61].find("on a}")
print(cur[61][i - 20:i + 420])
