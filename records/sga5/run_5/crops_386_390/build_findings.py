"""Build findings_386_390.json, check every fix's old once per page file, simulate the fixes (in order and reversed)
and then the marker moves in memory on both layers of s5.tex. Writes only the findings JSON."""
import json
import pathlib
import re

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
B = RUN / "b386_390"
OUT = RUN / "findings_386_390.json"
S5 = {e: pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5") / e / "s5.tex"
      for e in ("diplomatic", "current")}
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")

F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    r = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if fix is None else {"old": fix[0], "new": fix[1]}}
    if kind == "misprint_in_print":
        r["corrected"] = corrected
    r["note"] = note
    F.append(r)


# ---------------------------------------------------------------- p. 386
add(386, "top of the page: paragraph number 4.3",
    "p. 386 begins with '4.3. Notons que les modules ainsi obtenus ...'; p. 385 ends with '... sont notés σ_{y'}, σ'_{y'}, a_{y'}.'",
    "'\\subsubsection*{4.3}' ends page_385.tex; the folio-386 marker follows it, before 'Notons que'",
    "marker", "high", None,
    "Page 386 really begins at '\\subsubsection*{4.3}' (<<L386>>, at the time of the check). "
    "Exact fix: python -I move_marker.py 5 386 '\\subsubsection*{4.3' --before (simulated in memory on both layers: the marker "
    "then stands on its own line directly before '\\subsubsection*{4.3}'). Text not moved. The heading also lacks the print's "
    "full stop ('4.3.'): '\\subsubsection*{4.3}' -> '\\subsubsection*{4.3.}' (in page_385.tex until the move; not filed here).")
add(386, "4.3, line 1", "ne dépendent - à isomorphisme près -que du point y ∈ C",
    "ne dépendent, à isomorphisme près, que du point", "punctuation", "high",
    ("dépendent, à isomorphisme près, que", "dépendent - à isomorphisme près - que"),
    "The print sets the incise between typewriter dashes (spaced hyphens), not commas.")
add(386, "4.3, line 2", "et non du choix du point y' et C' au dessus de y",
    "du point $y'$ et $C'$", "misprint_in_print", "medium", None,
    "y' is a point of C' over y (C' is fixed with the situation (C', y', G)); 'et' makes no sense. The TeX keeps the printed reading.",
    corrected="du point $y'$ de $C'$")
add(386, "4.3, line 2-3", "au dessus de y (no hyphen)", "au-dessus de $y$", "misprint_in_print", "medium",
    ("au-dessus de $y$", "au dessus de $y$"),
    "The typescript drops the hyphen of 'au-dessus'; the TeX silently restores it.",
    corrected="au-dessus de $y$")
add(386, "4.3, 'Il existe donc g ∈ G tel que'", "y\" = g·y' (a raised dot between g and y')", "$y''=g y'$",
    "symbol", "high", ("$y''=g y'$", "$y''=g\\cdot y'$"),
    "The TeX drops the printed dot of the action.")
add(386, "4.3, 'se déduit donc de la situation'", "(C , y' , G) (no prime on C; the C' of 'sur C'' just after is primed)",
    "$(C,y',G)$", "misprint_in_print", "medium", None,
    "The situation (C', y'', G) is obtained from (C', y', G) by g acting on C'; the print drops the prime. The TeX keeps the printed reading.",
    corrected="$(C',y',G)$")
add(386, "4.3, int(g) on G", "int(g) : h ⇝ gh g^{-1} (a wavy arrow)", "h\\mapsto ghg^{-1}", "symbol", "high",
    ("h\\mapsto ghg^{-1}", "h\\rightsquigarrow ghg^{-1}"),
    "The print draws the wavy 'maps to' arrow, not a barred arrow.")
add(386, "4.3, 'On en conclut par transport de structure'", "'transport de structure' underlined",
    "transport de structure", "underline", "high",
    ("transport de structure", "\\emph{transport de structure}"),
    "Exposé X has no underline markup; \\emph as in the rest of the volume (III B, V, VII).")
add(386, "4.3, 'les modules Sw_y etc.'", "Sw_y etc. associés (no commas)", "$Sw_y$, etc., associés",
    "punctuation", "high", ("$Sw_y$, etc., associés", "$Sw_y$ etc. associés"),
    "The TeX adds two commas.")
add(386, "4.3, last sentence but one", "int(g) = G ⟶ G (an equals sign: two horizontal bars as in 'Λ = Z_ℓ', unlike the colon of 'int(g) : h' three lines up)",
    "\\operatorname{int}(g):G\\to G", "misprint_in_print", "high",
    ("\\operatorname{int}(g):G\\to G", "\\operatorname{int}(g)=G\\to G"),
    "Typist's '=' for ':'; the TeX silently corrects it.",
    corrected="\\operatorname{int}(g):G\\to G")
add(386, "Proposition 4.4, statement line 1", "'Les notations étant celles de', 'avec' underlined; '3.7' not",
    "Les notations étant celles de 3.7 avec", "underline", "high",
    ("Les notations étant celles de 3.7 avec", "\\emph{Les notations étant celles de} 3.7 \\emph{avec}"),
    "The statement is underlined word group by word group (formulas and numbers not). Independent of the next items.")
add(386, "Proposition 4.4, '(Λ = Z_ℓ'", "(Λ = Z_ℓ   et M° ... : the parenthesis is opened and never closed",
    "$(\\Lambda=\\mathbb Z_\\ell)$", "misprint_in_print", "high",
    ("\\mathbb Z_\\ell)$", "\\mathbb Z_\\ell$"),
    "Unbalanced parenthesis in the print; the TeX silently closes it after Z_ℓ.",
    corrected="\\mathbb Z_\\ell)$")
add(386, "Proposition 4.4, statement lines 1-2", "'et' and 'étant un objet de' underlined; M° not",
    " et $M^\\bullet$ étant un objet de", "underline", "high",
    (" et $M^\\bullet$ étant un objet de", " \\emph{et} $M^\\bullet$ \\emph{étant un objet de}"),
    "Statement underline.")
add(386, "Proposition 4.4, after D^+(A[G])", "D^+(A[G]) on a des isomorphismes (no comma)", "$D^+(A[G])$, on a",
    "punctuation", "high", ("$D^+(A[G])$,", "$D^+(A[G])$"), "The TeX adds a comma.")
add(386, "Proposition 4.4, 'on a des isomorphismes'", "'on a des isomorphismes' underlined (the colon not)",
    "on a des isomorphismes:", "underline", "high",
    ("on a des isomorphismes:", "\\emph{on a des isomorphismes}:"), "Statement underline.")
add(386, "display (*)", "(*)   Sw_y ≃ Sw̌_y   (no punctuation)", "(*)\\qquad Sw_y\\simeq \\check{Sw}_y,",
    "punctuation", "high", ("\\simeq \\check{Sw}_y,", "\\simeq \\check{Sw}_y"),
    "The TeX adds a comma at the end of the display.")
add(386, "proof label", "'Démonstration.' with 'Démonstration' underlined", "Démonstration. Pour que",
    "underline", "high", ("Démonstration. Pour que", "\\emph{Démonstration}. Pour que"),
    "Plain text in the TeX; elsewhere in Exposé X the prooftext environment prints \\emph{Démonstration.}.")
add(386, "proof, line 2", "soient isomorphes il suffit (no comma)", "soient isomorphes, il suffit",
    "punctuation", "high", ("soient isomorphes, il suffit", "soient isomorphes il suffit"), "The TeX adds a comma.")
add(386, "proof, line 3", "le caractère de Sw̌_y on a (3.7.2) : (no comma)", "$\\check{Sw}_y$, on a (3.7.2):",
    "punctuation", "high", ("$\\check{Sw}_y$, on a", "$\\check{Sw}_y$ on a"), "The TeX adds a comma.")
add(386, "proof, before the display of valuations", "D'autre part on a :", "D'autre part on a",
    "punctuation", "high", ("D'autre part on a", "D'autre part on a:"), "The TeX drops the colon.")
add(386, "proof, last sentence", "donc Sw_{y'} ≃ Sw_{y'} , d'où ... (no check over the second Sw; nothing faint there, while the checks of (*) and of 'le caractère de Sw̌_y' are clear)",
    "$Sw_{y'}\\simeq\\check{Sw}_{y'}$", "misprint_in_print", "medium",
    ("\\simeq\\check{Sw}_{y'}", "\\simeq Sw_{y'}"),
    "The hand-drawn check was left out; the TeX silently supplies it.",
    corrected="\\simeq\\check{Sw}_{y'}")
add(386, "last line of page_386.tex: heading 4.5 (printed at the top of p. 387)", "4.5. Nous aurons besoin ...",
    "\\subsubsection*{4.5}", "punctuation", "high",
    ("\\subsubsection*{4.5}", "\\subsubsection*{4.5.}"),
    "The paragraph number has a full stop in the print (as fixed on earlier pages). Filed under p. 386 because the heading is in "
    "page_386.tex until the folio-387 marker is moved; the marker anchor '\\subsubsection*{4.5' still matches after this fix.")

# ---------------------------------------------------------------- p. 387
add(387, "top of the page: paragraph 4.5",
    "p. 387 begins with '4.5. Nous aurons besoin plus bas ...'; p. 386 ends with '... en résulte grâce à 3.8.'",
    "'\\subsubsection*{4.5}', a blank line and 'Nous' end page_386.tex; page_387.tex begins with 'aurons besoin'",
    "marker", "high", None,
    "Page 387 really begins at '\\subsubsection*{4.5}' (<<L387>>, at the time of the check). "
    "Exact fix: python -I move_marker.py 5 387 '\\subsubsection*{4.5' --before (simulated in memory on both layers, with and "
    "without the '4.5.' fix filed under p. 386: the marker then stands on its own line directly before the heading). Text not moved.")
add(387, "(4.5.1), first case", "(1 - ν_{z'}(s)): a Greek ν (Symbol element), unlike the Latin v of the second case (1+v_{z'}(𝔇...))",
    "\\bigl(1-v_{z'}(s)\\bigr)", "misprint_in_print", "medium",
    ("\\sigma_y(s)=\n\\begin{cases}\n\\displaystyle\\sum_{\\substack{p(z')=y\\\\s(z')=z'}}\\bigl(1-v",
     "\\sigma_y(s)=\n\\begin{cases}\n\\displaystyle\\sum_{\\substack{p(z')=y\\\\s(z')=z'}}\\bigl(1-\\nu"),
    "The valuation is v (p. 386, the second cases); the typist's Greek ν here is reproduced in the diplomatic layer, the TeX's v is "
    "the corrected reading. All four ν items of this page together (all or none).",
    corrected="\\sigma_y(s)=\n\\begin{cases}\n\\displaystyle\\sum_{\\substack{p(z')=y\\\\s(z')=z'}}\\bigl(1-v")
add(387, "(4.5.1), conditions", "... (1 - ν_{z'}(s))   si s ≠ e  /  ... (1+v_{z'}(𝔇_{C'/C}))-n si s = e (no commas)",
    "\\bigr),& s\\ne e,\\\\[0.8em] ... \\bigr)-n,& s=e,", "missing", "high",
    (",& s\\ne e,\\\\[0.8em]\n\\displaystyle\\sum_{p(z')=y}\\bigl(1+v_{z'}(\\mathfrak D_{C'/C})\\bigr)-n,& s=e,",
     "& \\text{si } s\\ne e\\\\[0.8em]\n\\displaystyle\\sum_{p(z')=y}\\bigl(1+v_{z'}(\\mathfrak D_{C'/C})\\bigr)-n& \\text{si } s=e"),
    "The TeX drops the printed 'si' of both cases and adds three commas.")
add(387, "(4.5.2), left side and first case",
    "σ*_y(s) = σ *_{y\"}(s) = σ_y(s): no prime on any σ and none on the first subscript (handwritten y; nothing faint where the primes would stand); first case (1 - ν_{z'}(s)) with a Greek ν",
    "\\sigma^{\\prime*}_{y'}(s)=\\sigma^{\\prime*}_{y''}(s)=\\sigma'_y(s)= ... \\bigl(1-v_{z'}(s)", "misprint_in_print", "medium",
    ("\\sigma^{\\prime*}_{y'}(s)=\\sigma^{\\prime*}_{y''}(s)=\\sigma'_y(s)=\n\\begin{cases}\n\\displaystyle\\sum_{\\substack{p(z')=y\\\\s(z')=z'}}\\bigl(1-v",
     "\\sigma^{*}_{y}(s)=\\sigma^{*}_{y''}(s)=\\sigma_y(s)=\n\\begin{cases}\n\\displaystyle\\sum_{\\substack{p(z')=y\\\\s(z')=z'}}\\bigl(1-\\nu"),
    "(4.5.2) is the formula for σ' (character of Sw'_y, cf. p. 391); the print repeats the unprimed σ of (4.5.1) and drops the "
    "prime of y'; the TeX silently supplies them. One edit with the ν of the first case, because the case lines of (4.5.1) and "
    "(4.5.2) are identical: if ν is not reproduced, apply it without the final '1-\\nu' (keep '1-v').",
    corrected="\\sigma^{\\prime*}_{y'}(s)=\\sigma^{\\prime*}_{y''}(s)=\\sigma'_y(s)=\n\\begin{cases}\n\\displaystyle\\sum_{\\substack{p(z')=y\\\\s(z')=z'}}\\bigl(1-v")
add(387, "(4.5.2), conditions", "... (1 - ν_{z'}(s))   si s ≠ e  /  ... (1 + v_{z'}(𝔇_{C'/C})) si s = e (no commas)",
    "\\bigr),& s\\ne e,\\\\[0.8em] ... \\bigr),& s=e,", "missing", "high",
    (",& s\\ne e,\\\\[0.8em]\n\\displaystyle\\sum_{p(z')=y}\\bigl(1+v_{z'}(\\mathfrak D_{C'/C})\\bigr),& s=e,",
     "& \\text{si } s\\ne e\\\\[0.8em]\n\\displaystyle\\sum_{p(z')=y}\\bigl(1+v_{z'}(\\mathfrak D_{C'/C})\\bigr)& \\text{si } s=e"),
    "The TeX drops the printed 'si' of both cases and adds three commas.")
add(387, "(4.5.3), first case", "-Σ ν_{z'}(s) (Greek ν)", "-\\sum_{...}v_{z'}(s)", "misprint_in_print", "medium",
    ("}}v_{z'}", "}}\\nu_{z'}"),
    "As (4.5.1): the typist's Greek ν for the valuation v; all four ν items together.",
    corrected="}}v_{z'}")
add(387, "(4.5.3), first condition", "ν_{z'}(s)   si s ≠ e (no commas)", "v_{z'}(s),& s\\ne e,", "missing", "high",
    ("(s),& s\\ne e,", "(s)& \\text{si } s\\ne e"),
    "The TeX drops the printed 'si' and adds two commas.")
add(387, "(4.5.3), second case", "Σ_{p(z')=y} ν_{z'} 𝔇_{C'/C})  (Greek ν; no opening parenthesis before the hand-drawn 𝔇, the closing one is printed)",
    "\\sum_{p(z')=y}v_{z'}(\\mathfrak D_{C'/C})", "misprint_in_print", "medium",
    ("=y}v_{z'}(\\mathfrak", "=y}\\nu_{z'}\\mathfrak"),
    "Two misprints of the same term in one edit (they are adjacent): the Greek ν (all four ν items together) and the missing '(' "
    "that the TeX silently supplies. If ν is not reproduced, apply only the parenthesis: '=y}v_{z'}\\mathfrak'.",
    corrected="=y}v_{z'}(\\mathfrak")
add(387, "(4.5.3), second condition", "... si s = e (no comma, no full stop)", ",& s=e.", "missing", "high",
    (",& s=e.", "& \\text{si } s=e"),
    "The TeX drops 'si' and adds a comma and a full stop at the end of the display.")
add(387, "paragraph after (4.5.3), line 2", "si l'on fixe un point y'_o ∈ C , alors (no prime on C)", "$y'_0\\in C'$",
    "misprint_in_print", "high", ("$y'_0\\in C'$", "$y'_0\\in C$"),
    "y'_0 is a point of C' (g'(y') = y'_0 with y' ∈ C'); the print drops the prime, the TeX silently restores it.",
    corrected="$y'_0\\in C'$")
add(387, "same paragraph, 'dans G et on a de plus'", "dans G et on a de plus (no comma)", "dans $G$, et on a de plus",
    "punctuation", "high", ("dans $G$, et on a de plus", "dans $G$ et on a de plus"), "The TeX adds a comma.")
add(387, "last lines of page_387.tex: heading 4.6 (printed at the top of p. 388)", "4.6. Les invariants ...",
    "\\subsubsection*{4.6}", "punctuation", "high",
    ("\\subsubsection*{4.6}", "\\subsubsection*{4.6.}"),
    "Full stop after the paragraph number in the print. Filed under p. 387 because the heading is in page_387.tex until the "
    "folio-388 marker is moved; the anchor '\\subsubsection*{4.6' still matches after this fix.")

# ---------------------------------------------------------------- p. 388
add(388, "top of the page: paragraph 4.6",
    "p. 388 begins with '4.6. Les invariants Sw_y , Sw'_y , Art_y ...'; p. 387 ends with '... on obtient les formules écrites.'",
    "'\\subsubsection*{4.6}', a blank line and 'Les' end page_387.tex; page_388.tex begins with 'invariants'",
    "marker", "high", None,
    "Page 388 really begins at '\\subsubsection*{4.6}' (<<L388>>, at the time of the check). "
    "Exact fix: python -I move_marker.py 5 388 '\\subsubsection*{4.6' --before (simulated in memory on both layers, with and "
    "without the '4.6.' fix filed under p. 387). Text not moved.")
add(388, "4.6, line 4", "un ouvert U de C = C'/G dense dans C ('dense' underlined)", "dense dans", "underline", "high",
    ("dense dans", "\\emph{dense} dans"), "Underlined term.")
add(388, "4.6, '(resp. C_1) alors l'extension'", "(resp. C_1)  alors l'extension (no comma)", "(resp. $C_1$), alors",
    "punctuation", "high", ("(resp. $C_1$), alors", "(resp. $C_1$) alors"), "The TeX adds a comma.")
add(388, "4.6, the extension K'_1 ⊃ K_1",
    "K'_1 = k(η'_1) ⊃ k(    = K_1: a blank of about four characters after 'k(' where η_1) was never written in (nothing faint in the gap)",
    "K'_1=k(\\eta'_1)\\supset k(\\eta_1)=K_1", "misprint_in_print", "high",
    ("\\supset k(\\eta_1)=K_1", "\\supset k(=K_1"),
    "The print leaves η_1) out (a blank meant for it); the TeX silently supplies it.",
    corrected="\\supset k(\\eta_1)=K_1")
add(388, "Remarque 4.6, label", "'Remarque' underlined, '4.6.' not", "Remarque 4.6. Les modules", "underline", "high",
    ("Remarque 4.6. Les modules", "\\emph{Remarque} 4.6. Les modules"),
    "Plain-text label in the TeX (not an environment), so the print's underline is lost.")
add(388, "Remarque 4.6, last sentence", "modérément ramifiée en y'  ou, ce qui revient au même (no comma after y')",
    "en $y'$, ou,", "punctuation", "high", ("en $y'$, ou,", "en $y'$ ou,"), "The TeX adds a comma.")

# ---------------------------------------------------------------- p. 389
add(389, "title of section 5", "5.  La formule de Weil (comparer [3 VI § 4]).  (full stop after the parenthesis)",
    "\\subsection*{5. La formule de Weil (comparer [3 VI §4])}", "punctuation", "high",
    ("(comparer [3 VI §4])}", "(comparer [3 VI §4]).}"),
    "Underlined titles end with a full stop in the print (NOTE_5).")
add(389, "heading 5.0", "5.0. Tous les schémas ...", "\\subsubsection*{5.0}", "punctuation", "high",
    ("\\subsubsection*{5.0}", "\\subsubsection*{5.0.}"), "Full stop after the paragraph number in the print.")
add(389, "before the display of λ_ν^*", "un homomorphisme de réduction :", "un homomorphisme de réduction",
    "punctuation", "high", ("de réduction\n\\[", "de réduction:\n\\["), "The TeX drops the colon.")
add(389, "'seront désignés par'", "seront désignés par (masculine: the subject is 'Les images')", "seront désignées par",
    "misprint_in_print", "high", ("seront désignées par", "seront désignés par"),
    "Agreement error of the typist; the TeX silently corrects it.", corrected="seront désignées par")
add(389, "'L'homormorphisme de réduction'", "L'homormorphisme (an extra 'r')", "L'homomorphisme de réduction",
    "misprint_in_print", "high", ("L'homomorphisme", "L'homormorphisme"),
    "Typing error; the TeX silently corrects it.", corrected="L'homomorphisme")
add(389, "'sera désigné par Λ_{ν,X}'", "sera désigné par Λ_{ν,X} (no full stop; the next paragraph follows)",
    "$\\Lambda_{\\nu,X}$.", "punctuation", "high", ("$\\Lambda_{\\nu,X}$.", "$\\Lambda_{\\nu,X}$"),
    "The TeX adds a full stop.")

# ---------------------------------------------------------------- p. 390
add(390, "Proposition 5.1, statement lines 1-4",
    "underlined: 'Soient', 'une courbe algébrique', 'lisse et propre sur le corps', 'algébriquement clos', 'un groupe fini opérant sur', 'la projection canonique', 'un ouvert dense de', 'tel que', 'soit un revêtement principal de', 'de groupe' (formulas and commas not)",
    "Soient $C'$ une courbe algébrique, lisse et propre sur le corps $k$ ... de groupe $G$,", "underline", "high",
    ("Soient $C'$ une courbe algébrique, lisse et propre sur le corps $k$ algébriquement clos, $G$ un groupe fini opérant sur $C'$, $C=C'/G$, $p:C'\\to C$ la projection canonique, $U$ un ouvert dense de $C$ tel que $U'=p^{-1}(U)$ soit un revêtement principal de $U$ de groupe $G$,",
     "\\emph{Soient} $C'$ \\emph{une courbe algébrique}, \\emph{lisse et propre sur le corps} $k$ \\emph{algébriquement clos}, $G$ \\emph{un groupe fini opérant sur} $C'$, $C=C'/G$, $p:C'\\to C$ \\emph{la projection canonique}, $U$ \\emph{un ouvert dense de} $C$ \\emph{tel que} $U'=p^{-1}(U)$ \\emph{soit un revêtement principal de} $U$ \\emph{de groupe} $G$,"),
    "Statement underline, word group by word group.")
add(390, "Proposition 5.1, 'Y' = p^{-1}(X)'", "Y = C-U , Y' = p^{-1}(X) = C'-U'", "$X'=p^{-1}(X)=C'-U'$",
    "symbol", "high", ("$X'=p^{-1}", "$Y'=p^{-1}"),
    "The print names the set Y' (as used on pp. 391-393); the TeX's X' is neither the print nor the sense.")
add(390, "Proposition 5.1, 'Y' = p^{-1}(X)'", "p^{-1}(X)", "p^{-1}(X)=C'-U'", "misprint_in_print", "medium", None,
    "Y' = p^{-1}(Y) = C' - U' with Y = C - U; the print has X. The TeX keeps the printed reading.",
    corrected="p^{-1}(Y)=C'-U'")
add(390, "Proposition 5.1, statement line 5-6", "underlined: 'et soit', 'la caractéristique d'Euler-Poincaré de' (EP(C) not)",
    "et soit $\\EP(C)$ la caractéristique d'Euler-Poincaré de", "underline", "high",
    ("et soit $\\EP(C)$ la caractéristique d'Euler-Poincaré de",
     "\\emph{et soit} $\\EP(C)$ \\emph{la caractéristique d'Euler-Poincaré de}"),
    "Statement underline (the underline runs under 'de').")
add(390, "Proposition 5.1, 'de C , (égale à'", "d'Euler-Poincaré de C , (égale à (comma before the parenthesis)",
    "de $C$ (égale", "punctuation", "high", ("$C$ (", "$C$, ("), "The TeX drops the comma.")
add(390, "Proposition 5.1, statement line 6", "underlined: 'égale à', 'si', 'est connexe de genre' (the parenthesis, 2 - 2g, C, g not)",
    "égale à $2-2g$ si $C$ est connexe de genre", "underline", "high",
    ("égale à $2-2g$ si $C$ est connexe de genre",
     "\\emph{égale à} $2-2g$ \\emph{si} $C$ \\emph{est connexe de genre}"), "Statement underline.")
add(390, "'Dans ces conditions on a la formule de Weil :'", "'formule de Weil' underlined", "la formule de Weil:",
    "underline", "high", ("la formule de Weil:", "la \\emph{formule de Weil}:"), "Underlined term.")
add(390, "(5.2), first member", "cl_{K°(Λ_ν[G])}(R Γ_{C'}(Λ_{ν,U',C'})): a plain typed R before the hand-drawn Γ",
    "\\RG_{C'} (\\RG = \\R\\Gamma, \\R = \\mathbb{R} in Exposé X)", "font", "high",
    ("\\RG_{C'}", "\\mathrm{R}\\Gamma_{C'}"),
    "The print's derived-functor R is plain here (also on p. 391), the macro gives a double-struck R.")
add(390, "(5.2), second member", "EP(C) cl_{K°(Λ_ν[G]}(Λ_ν[G]) - ...: the subscript K°(Λ_ν[G] has no closing parenthesis",
    "\\clKstar{\\Lambda_\\nu[G]}(\\Lambda_\\nu[G])", "misprint_in_print", "high",
    ("\\clKstar{\\Lambda_\\nu[G]}(\\Lambda_\\nu[G])", "\\operatorname{cl}_{K^{\\bullet}(\\Lambda_\\nu[G]}(\\Lambda_\\nu[G])"),
    "Unbalanced parenthesis in the subscript; \\clKstar silently closes it. The fix writes the macro out without the ')'.",
    corrected="\\clKstar{\\Lambda_\\nu[G]}(\\Lambda_\\nu[G])")
add(390, "after (5.2)", "où le premier membre de (6.2) est défini grâce à 2.1.", "le premier membre de (6.2)",
    "misprint_in_print", "medium", None,
    "The first member defined thanks to 2.1 is that of the formula just displayed, (5.2). The TeX keeps the printed reading.",
    corrected="le premier membre de (5.2)")
add(390, "proof label", "'Démonstration.' with 'Démonstration' underlined", "Démonstration. Désignons",
    "underline", "high", ("Démonstration. Désignons", "\\emph{Démonstration}. Désignons"),
    "Plain text in the TeX; the prooftext environment of Exposé X prints \\emph{Démonstration.}.")
add(390, "'D'autre part (3.3.1) l'homomorphisme trace :'", "D'autre part (3.3.1) l'homomorphisme trace : (no comma, colon)",
    "D'autre part (3.3.1), l'homomorphisme trace", "punctuation", "high",
    ("(3.3.1), l'homomorphisme trace", "(3.3.1) l'homomorphisme trace:"),
    "The TeX adds a comma after (3.3.1) and drops the colon after 'trace'.")
add(390, "display K°(Z_ℓ[G]) -> F(G, Z_ℓ)", "label 'tv' over the arrow", "\\xrightarrow{\\ tv\\ }",
    "misprint_in_print", "medium", None,
    "The trace homomorphism is 'tr' (the next display: tr(μ_ν(S_1)) = tr(μ_ν(S_2))). The TeX keeps the printed 'tv'.",
    corrected="\\xrightarrow{\\ tr\\ }")
add(390, "end of the page: display (5.2.1)",
    "p. 390 ends with '... donné par la for-/mule' and the display '(5.2.1) σ_2 = EP(C)r_G - Σ_{y∈Y} σ'_y ,'; p. 391 begins with 'où σ'_y est le caractère de Sw'_y ((4.2.7) et (4.2.3)), ...'",
    "'formule' and the display (5.2.1) open page_391.tex, under the folio-391 marker",
    "marker", "high", None,
    "Page 391 really begins at 'où $\\sigma'_y$ est le caractère' (the line after the '\\]' of (5.2.1); <<L391>>, at the time of the check). Exact fix: python -I move_marker.py 5 391 'où $\\sigma' (no --before; the anchor's "
    "first occurrence after the marker is that line; simulated in memory on both layers). Text not moved. 'formule' and (5.2.1) "
    "agree with the print of p. 390 (the double-struck EP aside, see the message).")

# ---------------------------------------------------------------- checks
pages = {p: (B / f"page_{p}.tex").read_text(encoding="utf-8") for p in range(386, 391)}
bad = 0
for r in F:
    if r["fix"]:
        n = pages[r["page"]].count(r["fix"]["old"])
        if n != 1:
            print("NOT UNIQUE", r["page"], n, repr(r["fix"]["old"][:60]))
            bad += 1
        if MARK.search(r["fix"]["old"]):
            print("CROSSES MARKER", r["page"])
            bad += 1
# sequential application, forward and reversed, on each page file
for order in ("forward", "reversed"):
    for p, t in pages.items():
        fx = [r["fix"] for r in F if r["page"] == p and r["fix"]]
        if order == "reversed":
            fx = fx[::-1]
        for f in fx:
            n = t.count(f["old"])
            if n != 1:
                print("SEQ", order, p, n, repr(f["old"][:60]))
                bad += 1
            t = t.replace(f["old"], f["new"], 1)
print("uniqueness/sequence problems:", bad)


# simulate on s5.tex: fixes of each page inside its span (diplomatic), then the marker moves on both layers
def spans(t):
    ms = list(MARK.finditer(t))
    out = {}
    for i, m in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
        out[int(m.group(2))] = (m.start(), end)
    return out


def move(t, folio, anchor, before):
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    assert k >= 0, (folio, anchor)
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2


MOVES = [(386, "\\subsubsection*{4.3", True), (387, "\\subsubsection*{4.5", True),
         (388, "\\subsubsection*{4.6", True), (391, "où $\\sigma", False)]
LINES = {}
for ed, path in S5.items():
    t = path.read_text(encoding="utf-8")
    for folio, anchor, before in MOVES:
        m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
        ln = t.count("\n", 0, m.start()) + 1
        if before:
            k = t.rfind(anchor, 0, m.start())
        else:
            k = t.find(anchor, m.start())
        print(ed, "marker", folio, "at line", ln, "; anchor at line", t.count("\n", 0, k) + 1)
        LINES.setdefault(folio, {})[ed] = t.count("\n", 0, k) + 1
    if ed == "diplomatic":
        for p in range(386, 391):
            a, e = spans(t)[p]
            seg = t[a:e]
            for r in F:
                if r["page"] == p and r["fix"]:
                    assert seg.count(r["fix"]["old"]) == 1, (p, r["fix"]["old"][:40])
                    seg = seg.replace(r["fix"]["old"], r["fix"]["new"], 1)
            t = t[:a] + seg + t[e:]
    for folio, anchor, before in MOVES:
        t = move(t, folio, anchor, before)
    sp = spans(t)
    for folio in (386, 387, 388, 391):
        a, e = sp[folio]
        head = t[a:e].split("\n")[1:3]
        print(ed, "after moves, page", folio, "starts:", [h[:50] for h in head])
    a, e = sp[390]
    print(ed, "page 390 ends:", [h[:50] for h in t[a:e].rstrip("\n").split("\n")[-3:]])

for r in F:
    for folio, d in LINES.items():
        ph = "<<L%d>>" % folio
        if ph in r["note"]:
            r["note"] = r["note"].replace(ph, "diplomatic s5.tex line %d, current %d" % (d["diplomatic"], d["current"]))
    assert "<<L" not in r["note"], r["note"][:80]
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
cnt = {}
for r in F:
    k = "misprint" if r["kind"] == "misprint_in_print" else "normal"
    cnt.setdefault(r["page"], {"normal": 0, "misprint": 0})[k] += 1
print("written", OUT, len(F), cnt)
