import json
import pathlib

NL = "\n"
OUT = pathlib.Path(r"C:/Users/user/Documents/sga_scan_check_20261105/run_5/findings_301_305.json")
B = pathlib.Path(r"C:/Users/user/Documents/sga_scan_check_20261105/run_5/b301_305")

F = []


def add(page, where, scan, tex, kind, conf, old, new, note="", corrected=None):
    it = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
          "fix": None if old is None else {"old": old, "new": new}}
    if corrected is not None:
        it["corrected"] = corrected
    it["note"] = note
    F.append(it)


# ---------------- page 301 ----------------
add(301, "'au-dessus de U = X - Y, qui est évidente'",
    "a typed minus with a crisp dot centred above it (∸) between X and Y",
    "$U=X-Y$", "symbol", "high",
    r"$U=X-Y$", r"$U=X\mathbin{\dot{-}}Y$",
    "The typescript's set-difference sign of Exposé VII, written as the applied fix of p. 285 "
    r"('\mathbb C^r\mathbin{\dot{-}}0'). Two occurrences on this page (see the next item), so not a stray mark.")
add(301, "'un isomorphisme de U' = X' - Y' sur U'",
    "the same dotted minus (∸) between X' and Y'",
    "$U'=X'-Y'$", "symbol", "high",
    r"$U'=X'-Y'$", r"$U'=X'\mathbin{\dot{-}}Y'$",
    "As the previous item.")
add(301, "'Comme f*i_*(1_Y) ∈ H^{2d}_{Y'}(X',μ_{X'}^{⊗d}) et le morphisme de Gysin'",
    "no comma after the closing parenthesis, 'et le morphisme' follows directly",
    r"\mu_{X'}^{\otimes d})$, et le morphisme", "punctuation", "high",
    r"\mu_{X'}^{\otimes d})$, et le morphisme", r"\mu_{X'}^{\otimes d})$ et le morphisme",
    "The TeX adds a comma.")
add(301, "display after 'Appliquant j* aux deux membres de 4.1.1, il vient'",
    "'j*f*   (1_Y) = j*j_*(u) .': a clean blank of about two typewriter characters between f* and (1_Y); no i_* (nothing faint in the gap)",
    r"j^*f^*i_*(1_Y)=j^*j_*(u).", "misprint_in_print", "high",
    r"j^*f^*i_*(1_Y)", r"j^*f^*(1_Y)",
    "The typist left out i_* (j* applied to (4.1.1) f*i_*(1_Y) = j_*(u)); the TeX silently supplies it.",
    corrected=r"j^*f^*i_*(1_Y)")
add(301, "display (4.1.3), after ξ^{d-1}",
    "'a_{d-1}ξ^{d-1} (a_i ∈ ...' with no comma (a speck far smaller than the line's typed commas is not one)",
    r"u=a_0+a_1\xi+\cdots+a_{d-1}\xi^{d-1},", "punctuation", "high",
    r"\xi^{d-1}," + NL + r"\qquad", r"\xi^{d-1}" + NL + r"\qquad",
    "The TeX adds a comma inside the display.")
add(301, "display (4.1.3), the clause on a_i",
    "'(a_i ∈ H^{2d-2-2i}(Y,μ_Y^{⊗(d-1-i)}))' in parentheses, no full stop at the end",
    r"a_i\in H^{2d-2-2i}(Y,\mu_Y^{\otimes(d-1-i)}).", "formula", "high",
    r"a_i\in H^{2d-2-2i}(Y,\mu_Y^{\otimes(d-1-i)}).", r"(a_i\in H^{2d-2-2i}(Y,\mu_Y^{\otimes(d-1-i)}))",
    "The TeX drops the parentheses and adds a full stop at the end of the display (one edit).")

# ---------------- page 302 ----------------
add(302, "top of the page: display (4.1.4)",
    "p. 302 begins with '(4.1.4) ξ^d + c_1(Ň)ξ^{d-1} +...+ c_{d-1}(Ň)ξ + c_d(Ň) = 0 ,' then 'on en déduit l'égalité'; p. 301 ends with '... des classes de Chern de Ň' (rest of the page blank)",
    "the display (4.1.4) ends page_301.tex; the folio-302 marker follows its '\\]', before 'on en déduit l'%'",
    "marker", "high", None, None,
    "Page 302 really begins at the '\\[' that opens the display (4.1.4) (the line after 'Compte tenu de la relation de définition des classes de Chern de $\\check N$'; diplomatic s5.tex line 10192, current 10187, at the time of the check). "
    "Exact fix: python -I move_marker.py 5 302 '\\[' --before (simulated in memory on both layers: the marker then stands on its own line between '... de Chern de $\\check N$' and '\\[', and '\\]' is followed directly by 'on en déduit l'%'). Text not moved; the display matches the print.")

# ---------------- page 303 ----------------
add(303, "end of Remarques 4.4 b), 'a été établi par MUMFORD (cf. 9.2)'",
    "MUMFORD in capitals",
    "par Mumford", "word", "high",
    "par Mumford", "par MUMFORD",
    "Capitals as printed (as 'GYSIN' in the label of Corollaire 1.5, p. 285).")
add(303, "Corollaire 4.5, 'Sous les hypothèses de 4.1, soient x et y ∈ A•(Y).'",
    "underlined: 'Sous les hypothèses de' | 'soient' | 'et'; 4.1, x, y not",
    "Sous les hypothèses de 4.1, soient $x$ et $y", "underline", "high",
    r"Sous les hypothèses de 4.1, soient $x$ et $y", r"\emph{Sous les hypothèses de} 4.1, \emph{soient} $x$ \emph{et} $y",
    "Exposé VII: the TeX has no underline markup for statements; \\emph is the file's command (as the applied statements of pp. 283-300).")
add(303, "Corollaire 4.5, 'y ∈ A•(Y)'",
    "A with a small raised dot",
    "A^*(Y)", "symbol", "high",
    r"A^*(Y)", r"A^\bullet(Y)",
    "The TeX has a star; written A^\\bullet as the itemized A• of pp. 290-295 (global issue 89 (d)).")
add(303, "Corollaire 4.5, 'On a :'",
    "'On a' underlined",
    ". On a", "underline", "high",
    ". On a", r". \emph{On a}",
    "")
add(303, "Corollaire 4.5, 'On a :' before the display",
    "'On a :' (colon before the display)",
    "On a, then the display", "punctuation", "high",
    NL + r"\[" + NL + r"i_*(x)i_*(y)=i_*(xy", " :" + NL + r"\[" + NL + r"i_*(x)i_*(y)=i_*(xy",
    "The TeX drops the colon before the display. Independent of the underline edit of 'On a' (the two olds are adjacent, not overlapping).")
add(303, "Corollaire 4.6, first line and 'constant r et'",
    "underlined: 'Soient' | 'un' | 'schéma' | 'un' | '-Module localement libre de rang' / 'constant r et' (one line under 'constant r et', r included); S, E, O_S not",
    "Soient $S$ un schéma, $E$ un $\\mathcal O_S$-Module localement libre de rang constant $r$ et $g", "underline", "high",
    r"Soient $S$ un schéma, $E$ un $\mathcal O_S$-Module localement libre de rang constant $r$ et $g",
    r"\emph{Soient} $S$ \emph{un} \emph{schéma}, $E$ \emph{un} $\mathcal O_S$-\emph{Module localement libre de rang constant $r$ et} $g",
    "")
add(303, "Corollaire 4.6, 'le fibré vectoriel dont E est le faisceau des sections. Pour toute section f de X au-dessus de S , on a'",
    "underlined: 'le fibré vectoriel dont' | 'est le faisceau des sections. Pour toute section' | 'de' | 'au-dessus de' | 'on a'; E, f, X, S not",
    "le fibré vectoriel dont $E$ est le faisceau des sections. Pour toute section $f$ de $X$ au-dessus de $S$, on a", "underline", "high",
    r"le fibré vectoriel dont $E$ est le faisceau des sections. Pour toute section $f$ de $X$ au-dessus de $S$, on a",
    r"\emph{le fibré vectoriel dont} $E$ \emph{est le faisceau des sections. Pour toute section} $f$ \emph{de} $X$ \emph{au-dessus de} $S$, \emph{on a}",
    "")
add(303, "Corollaire 4.6, 'on a :' before the display f_*(1_S) = g*(c_r(E))",
    "'on a :' (colon before the display)",
    "on a, then the display", "punctuation", "high",
    NL + r"\[" + NL + r"f_*(1_S)=g^*(c_r(E))", " :" + NL + r"\[" + NL + r"f_*(1_S)=g^*(c_r(E))",
    "The TeX drops the colon before the display. Independent of the underline edit above (adjacent olds).")
add(303, "proof of 4.6, 'la suite exacte de (EGA IV 17.2.5) appliqué à la situation'",
    "no comma after '(EGA IV 17.2.5)'",
    "(EGA IV 17.2.5), appliquée", "punctuation", "high",
    "17.2.5),", "17.2.5)",
    "The TeX adds a comma. Listed before the misprint item 'appliqué' (the two olds do not overlap).")
add(303, "proof of 4.6, 'appliqué à la situation'",
    "'appliqué' (no final e)",
    "appliquée", "misprint_in_print", "high",
    "appliquée", "appliqué",
    "Agreement error of the typist (the subject is 'la suite exacte'); the TeX silently corrects it.",
    corrected="appliquée")
add(303, "proof of 4.6, the situation S → X → S, label of the first arrow",
    "'S --b--> X --g--> S': the first arrow is labelled with a typed b (closed bowl, short ascender), not f",
    r"S\xrightarrow{f} X\xrightarrow{g} S,", "misprint_in_print", "high",
    r"\xrightarrow{f}", r"\xrightarrow{b}",
    "The arrow is the section f of Corollaire 4.6; typing error, the TeX silently corrects it.",
    corrected=r"\xrightarrow{f}")
add(303, "proof of 4.6, end of the situation S → X → S",
    "no comma after the second S ('S  fournit un isomorphisme')",
    r"X\xrightarrow{g} S,", "punctuation", "high",
    r"\xrightarrow{g} S,", r"\xrightarrow{g} S",
    "The TeX adds a comma at the end of the display (inline in the print). Independent of the arrow-label misprint.")
add(303, "proof of 4.6, 'N ≃ f*Ω^1_{X/S} et par ailleurs'",
    "no comma before 'et par ailleurs'",
    r"\Omega^1_{X/S}$, et par ailleurs", "punctuation", "high",
    r"\Omega^1_{X/S}$, et par ailleurs", r"\Omega^1_{X/S}$ et par ailleurs",
    "The TeX adds a comma.")
add(303, "Corollaire 4.7, first sentence",
    "underlined: 'Sous les hypothèses de' | 'on suppose de plus' | 'lisse et quasi-' / 'projectif sur un corps séparablement clos.' (continuing under 'Alors notant'); 4.6, S not",
    "Sous les hypothèses de 4.6, on suppose de plus $S$ lisse et quasi-projectif sur un corps séparablement clos.", "underline", "high",
    r"Sous les hypothèses de 4.6, on suppose de plus $S$ lisse et quasi-projectif sur un corps séparablement clos.",
    r"\emph{Sous les hypothèses de} 4.6, \emph{on suppose de plus} $S$ \emph{lisse et quasi-projectif sur un corps séparablement clos.}",
    "")
add(303, "Corollaire 4.7, 'Alors notant σ_X'",
    "'Alors notant' with no comma, underlined",
    "Alors, notant", "punctuation", "high",
    "Alors, notant", r"\emph{Alors notant}",
    "The TeX adds a comma; the edit also gives the underline of 'Alors notant'.")
add(303, "Corollaire 4.7, 'le cycle section nulle de X et Y = f^{-1}(σ_X) le cycle des zéros de f , on a'",
    "underlined: 'le cycle section nulle' / 'de' | 'et' | 'le cycle des zéros de' | 'on a'; X, Y = f^{-1}(σ_X), f not",
    "le cycle section nulle de $X$ et $Y=f^{-1}(\\sigma_X)$ le cycle des zéros de $f$, on a", "underline", "high",
    r"le cycle section nulle de $X$ et $Y=f^{-1}(\sigma_X)$ le cycle des zéros de $f$, on a",
    r"\emph{le cycle section nulle de} $X$ \emph{et} $Y=f^{-1}(\sigma_X)$ \emph{le cycle des zéros de} $f$, \emph{on a}",
    "")
add(303, "Corollaire 4.7, 'on a :' before the display cl_S(Y) = c_r(E)",
    "'on a :' (colon before the display)",
    "on a, then the display", "punctuation", "high",
    NL + r"\[" + NL + r"\cl_S(Y)=c_r(E)", " :" + NL + r"\[" + NL + r"\cl_S(Y)=c_r(E)",
    "The TeX drops the colon before the display. Independent of the underline edit above (adjacent olds).")
add(303, "Corollaire 4.7, 'dans H^{2r}(S,μ_S^{⊗r}) .' after the display",
    "'dans' underlined",
    "dans $H^{2r}(S,", "underline", "high",
    r"dans $H^{2r}(S,", r"\emph{dans} $H^{2r}(S,",
    "The 'dans' after the display of Corollaire 4.6 is not underlined (as the TeX).")

# ---------------- page 304 ----------------
add(304, "'On rappelle (IV) qu'on appelle caractéristique d'Euler-Poincaré ℓ-adique de X l'entier'",
    "underlined: 'caractéristique' | 'd'Euler-Poincaré' | 'adique' (ℓ- not)",
    "qu'on appelle caractéristique d'Euler-Poincaré $\\ell$-adique de $X$ l'entier", "underline", "high",
    r"qu'on appelle caractéristique d'Euler-Poincaré $\ell$-adique de $X$ l'entier",
    r"qu'on appelle \emph{caractéristique} \emph{d'Euler-Poincaré} $\ell$-\emph{adique} de $X$ l'entier",
    "The defined term, underlined in running text; \\emph is the file's command for the print's underline in this exposé.")
add(304, "Corollaire 4.9, first sentence",
    "underlined: 'Soit' | 'un schéma lisse, propre, connexe, de dimension' | 'sur un' / 'corps séparablement clos' | 'avec'; X, n, k, car(k) ≠ ℓ not",
    "Soit $X$ un schéma lisse, propre, connexe, de dimension $n$ sur un corps séparablement clos $k$, avec $", "underline", "high",
    r"Soit $X$ un schéma lisse, propre, connexe, de dimension $n$ sur un corps séparablement clos $k$, avec $",
    r"\emph{Soit} $X$ \emph{un schéma lisse, propre, connexe, de dimension} $n$ \emph{sur un corps séparablement clos} $k$, \emph{avec} $",
    "")
add(304, "Corollaire 4.9, 'Notant p : X → k la projection canonique, on a'",
    "underlined: 'Notant' | 'la projection cano-' / 'nique, on a'; p : X → k not",
    "Notant $p:X\\to k$ la projection canonique, on a", "underline", "high",
    r"Notant $p:X\to k$ la projection canonique, on a",
    r"\emph{Notant} $p:X\to k$ \emph{la projection canonique, on a}",
    "")
add(304, "Corollaire 4.9, 'dans Q_ℓ = H^0(k,Q_ℓ) .' after the display",
    "'dans' underlined",
    "dans $\\mathbb Q_\\ell=", "underline", "high",
    r"dans $\mathbb Q_\ell=", r"\emph{dans} $\mathbb Q_\ell=",
    "")
add(304, "proof of 4.9, display c_n(Ω̌^1_X) = j*j_*(1_X)",
    "no punctuation at the end of the display ('d'où' follows on the next line)",
    r"c_n(\check\Omega^1_X)=j^*j_*(1_X),", "punctuation", "high",
    r"=j^*j_*(1_X)," + NL + r"\]", r"=j^*j_*(1_X)" + NL + r"\]",
    "The TeX adds a comma at the end of the display.")
add(304, "numbered paragraph 4.10 (printed at the top of p. 305)",
    "'4.10.' (with a full stop)",
    r"\subsubsection*{4.10}", "punctuation", "high",
    r"\subsubsection*{4.10}", r"\subsubsection*{4.10.}",
    "Printed on p. 305; filed under p. 304, where the line stands until the marker move of p. 305 (the edit keeps the move's anchor '\\subsubsection*{4.10', so either order works). As the logged '2.1.', '3.3.', '3.8.' of pp. 285-295.")

# ---------------- page 305 ----------------
add(305, "top of the page: numbered paragraph 4.10",
    "p. 305 begins with '4.10.  Lorsque X est projectif sur k , ...'; p. 304 ends with '... la caractéristique d'Euler-Poincaré ℓ-adique de X .' (rest of the page blank)",
    "'\\subsubsection*{4.10}' ends page_304.tex; the folio-305 marker follows it, before 'Lorsque'",
    "marker", "high", None, None,
    "Page 305 really begins at '\\subsubsection*{4.10}' (diplomatic s5.tex line 10325, current 10320, at the time of the check). "
    "Exact fix: python -I move_marker.py 5 305 '\\subsubsection*{4.10' --before (simulated in memory on both layers, with and without the '4.10.' fix filed under p. 304: the marker then stands on its own line after the blank line that ends p. 304, directly before '\\subsubsection*{4.10'). Text not moved.")
add(305, "4.10, 'Ceci nous permettra par conséquent de parler'",
    "no commas around 'par conséquent'",
    "permettra, par conséquent, de parler", "punctuation", "high",
    "permettra, par conséquent, de parler", "permettra par conséquent de parler",
    "The TeX adds two commas.")
add(305, "Proposition 4.11, statement",
    "underlined: 'Soit' | 'un schéma lisse, projectif, connexe, de dimension' | 'sur' / 'un corps séparablement clos' | 'Alors on a'; X, n, k not",
    "Soit $X$ un schéma lisse, projectif, connexe, de dimension $n$ sur un corps séparablement clos $k$. Alors on a", "underline", "high",
    r"Soit $X$ un schéma lisse, projectif, connexe, de dimension $n$ sur un corps séparablement clos $k$. Alors on a",
    r"\emph{Soit} $X$ \emph{un schéma lisse, projectif, connexe, de dimension} $n$ \emph{sur un corps séparablement clos} $k$. \emph{Alors on a}",
    "")
add(305, "Proposition 4.11, 'Alors on a :' before the display",
    "'Alors on a :' (colon before the display)",
    "on a, then the display", "punctuation", "high",
    NL + r"\[" + NL + r"\operatorname{EP}(X)=\sum", " :" + NL + r"\[" + NL + r"\operatorname{EP}(X)=\sum",
    "The TeX drops the colon before the display. Independent of the underline edit above (adjacent olds).")
add(305, "proof of 4.11, 'et notons J l'Idéal de l'immersion diagonale'",
    "'Idéal' with a capital I",
    "l'idéal de l'immersion", "word", "high",
    "l'idéal de l'immersion", "l'Idéal de l'immersion",
    "The typescript's capital for a sheaf of ideals, as the logged 'l'Idéal (T^{r+1})' of p. 287.")
add(305, "proof of 4.11, 'Or d'après (SGA 6 VII 2.5), ce dernier carré'",
    "no comma after 'Or'",
    "Or, d'après", "punctuation", "high",
    "Or, d'après", "Or d'après",
    "The TeX adds a comma.")

# ---------------- checks ----------------
bad = 0
for it in F:
    fx = it["fix"]
    if fx is None:
        continue
    page = (B / ("page_%d.tex" % it["page"])).read_text(encoding="utf-8")
    n = page.count(fx["old"])
    if n != 1:
        bad += 1
        print("NOT UNIQUE", it["page"], n, repr(fx["old"]))
    marker = [l for l in page.split(NL) if l.startswith("%%%%%%%%%%")][0]
    if "%%%%" in fx["old"] or "%%%%" in fx["new"]:
        bad += 1
        print("TOUCHES MARKER", it["page"], repr(fx["old"]))
# overlapping olds on the same page
for p in sorted({it["page"] for it in F}):
    page = (B / ("page_%d.tex" % p)).read_text(encoding="utf-8")
    spans = []
    for it in F:
        if it["page"] == p and it["fix"]:
            s = page.find(it["fix"]["old"])
            spans.append((s, s + len(it["fix"]["old"]), it["where"][:50]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            bad += 1
            print("OVERLAP", p, a, b)
print("findings", len(F), "problems", bad)
from collections import Counter
c = Counter((it["page"], it["kind"] == "misprint_in_print") for it in F)
for p in (301, 302, 303, 304, 305):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + NL, encoding="utf-8")
print("written", OUT)
