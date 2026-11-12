"""Build findings_321_325.json and check every fix: each 'old' must occur exactly once in its page_NNN.tex at the
moment it is applied (edits applied in the listed order); items marked dep=True take their 'old' from the text
after the edit(s) listed before them (misprint fixes inside an underline edit); all others must also occur
exactly once in the original file. Writes only the JSON named below."""
import json
import pathlib

B = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\b321_325")
OUT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\findings_321_325.json")
NL = "<NL>"

UL = ("Exposé VII: the TeX has no underline markup for statements; \\emph as in the applied statements of "
      "pp. 283-295.")
TENSOR_SEEN = "see the message on \\otimes^L"

F = []


def add(page, where, scan, tex, kind, conf, old=None, new=None, note="", corrected=None, dep=False):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, confidence=conf,
             fix=None if old is None else {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")})
    if kind == "misprint_in_print":
        d["corrected"] = corrected.replace(NL, "\n") if corrected is not None else None
    d["note"] = note
    d["_dep"] = dep
    F.append(d)


# ---------------------------------------------------------------- p. 321
add(321, "top of the page: label (ii) of Lemme 7.2.1",
    "p. 321 begins with '(ii) Pour tout V-module N , le morphisme'; p. 320 ends with item (i) "
    "'H^p(M) = 0 pour p ≤ m-1, et H^m(M) est sans torsion.'",
    "the '\\item' of (ii) is the last line of page_320.tex (diplomatic s5.tex line 10812, current 10808); "
    "page_321.tex begins with 'pour tout $V$-module $N$, le morphisme'",
    "marker", "high",
    note="Page 321 really begins at that '\\item' (the label (ii)). Exact fix: python -I move_marker.py 5 321 "
         "'\\item' --before (simulated in memory on both layers: the folio-321 marker lands just before the "
         "'\\item' line, diplomatic 10812, current 10808). Text not moved; independent of the edits below.")
add(321, "Lemme 7.2.1 (ii), 'Pour tout V-module N , le morphisme'",
    "'Pour' with a capital P; underlined: 'Pour tout' | 'module' | 'le morphisme' (V-, N and the comma not)",
    "pour tout $V$-module $N$, le morphisme", "word", "high",
    r"pour tout $V$-module $N$, le morphisme",
    r"\emph{Pour tout} $V$-\emph{module} $N$, \emph{le morphisme}",
    "Capital P as printed. One edit: it also gives the underline. " + UL)
add(321, "Lemme 7.2.1 (ii), 'est un isomorphisme pour p ≤ m-1 et un monomorphisme pour p = m .'",
    "full stop at the end; underlined: 'est un isomorphisme pour' | 'et un monomorphisme pour'",
    "est un isomorphisme pour $p\\le m-1$ et un monomorphisme pour $p=m$;", "punctuation", "high",
    r"N)<NL>\]<NL>est un isomorphisme pour $p\le m-1$ et un monomorphisme pour $p=m$;",
    r"N)<NL>\]<NL>\emph{est un isomorphisme pour} $p\le m-1$ \emph{et un monomorphisme pour} $p=m$.",
    "The TeX has a semicolon for the print's full stop. One edit: it also gives the underline.")
add(321, "Lemme 7.2.1 (ii bis), 'Pour tout V-module N on a'",
    "capital P; no comma after N; underlined: 'Pour tout' | 'module' | 'on a'",
    "pour tout $V$-module $N$, on a", "word", "high",
    r"pour tout $V$-module $N$, on a",
    r"\emph{Pour tout} $V$-\emph{module} $N$ \emph{on a}",
    "Capital P as printed. One edit: it also drops the TeX's comma after N (punctuation) and gives the underline.")
add(321, "Lemme 7.2.1 (ii bis), display H^p(M ⊗ N) = 0 (p ≤ m-1).",
    "full stop after the parenthesis", "(p\\le m-1);", "punctuation", "high",
    r"(p\le m-1);", r"(p\le m-1).",
    "The TeX has a semicolon for the print's full stop.")
add(321, "Lemme 7.2.1 (iii), 'Le morphisme'",
    "'Le' with a capital L; underlined", "\\item le morphisme", "word", "high",
    r"\]<NL>\item le morphisme", r"\]<NL>\item \emph{Le morphisme}",
    "One edit: it also gives the underline.")
add(321, "Lemme 7.2.1 (iii), display H^p(u ⊗ id) : H^p(K ⊗ k_V) → H^p(K ⊗ k_V)",
    "the target is printed H^p(K ⊗ k_V), with K as in the source (clear in the scan)",
    "H^p(u\\otimes^L\\operatorname{id}):H^p(K\\otimes^L k_V)\\to H^p(L\\otimes^L k_V)",
    "misprint_in_print", "high",
    r"k_V)\to H^p(L", r"k_V)\to H^p(K",
    "Typing error: u : K → L, so the target is H^p(L ⊗ k_V), as in (ii) and (i bis). The TeX silently corrects "
    "it. Changes only the letter; the old leaves out the tensor sign (" + TENSOR_SEEN + ").",
    corrected=r"k_V)\to H^p(L")
add(321, "Lemme 7.2.1 (iii), 'est un isomorphisme pour p ≤ m-1 est un monomorphisme pour p = m .'",
    "full stop at the end; underlined: 'est un isomorphisme pour' | 'est un monomorphisme pour'",
    "est un isomorphisme pour $p\\le m-1$ et un monomorphisme pour $p=m$;", "punctuation", "high",
    r"k_V)<NL>\]<NL>est un isomorphisme pour $p\le m-1$ et un monomorphisme pour $p=m$;",
    r"k_V)<NL>\]<NL>\emph{est un isomorphisme pour} $p\le m-1$ \emph{et un monomorphisme pour} $p=m$.",
    "The TeX has a semicolon for the print's full stop. One edit: it also gives the underline. The print's "
    "'est' for 'et' in this line is the misprint item below, applied after this edit.")
add(321, "Lemme 7.2.1 (iii bis), 'H^p(M ⊗ k_V) = 0 pour p ≤ m-1 .'",
    "no 'on a': the label is followed directly by the formula",
    "\\item[(iii bis)] on a", "extra", "high",
    r"\item[(iii bis)] on a", r"\item[(iii bis)]",
    "The TeX adds 'on a' (which the print has in (ii bis) only).")
add(321, "Lemme 7.2.1 (iii), 'est un monomorphisme pour p = m'",
    "'est un monomorphisme pour' (typed 'est', no comma before it; (ii) has 'et un monomorphisme')",
    "et un monomorphisme pour $p=m$;", "misprint_in_print", "medium",
    r"\emph{et un monomorphisme pour} $p=m$.<NL>\item[(iii",
    r"\emph{est un monomorphisme pour} $p=m$.<NL>\item[(iii",
    "Typing error for 'et' (the parallel line of (ii) has 'et'; without a comma 'est ... est' does not "
    "construe); the TeX silently corrects it. Medium only for the classification: (i bis) has ', est un "
    "monomorphisme', which construes (word item below). The old is taken from the text after the underline "
    "edit of this line and the 'on a' edit (listed before).",
    corrected=r"\emph{et un monomorphisme pour} $p=m$.<NL>\item[(iii", dep=True)
add(321, "Lemme 7.2.1 (iii bis), 'pour p ≤ m-1 .'",
    "'= 0  pour  p≤m-1 .' with 'pour' underlined; no parentheses",
    "=0\\qquad(p\\le m-1).", "word", "high",
    r"k_V)=0\qquad(p\le m-1).", r"k_V)=0\quad\text{\emph{pour}}\quad p\le m-1.",
    "The TeX replaces the printed 'pour' by parentheses. One edit: it also gives the underline.")
add(321, "Lemme 7.2.1, 'De plus, ces conditions équivalentes impliquent :'",
    "the whole phrase underlined (not the colon)",
    "De plus, ces conditions équivalentes impliquent:", "underline", "high",
    r"De plus, ces conditions équivalentes impliquent:",
    r"\emph{De plus, ces conditions équivalentes impliquent}:", UL)
add(321, "Lemme 7.2.1 (i bis), 'Le morphisme'",
    "'Le' with a capital L; underlined", "\\item le morphisme", "word", "high",
    r"bis)]<NL>\item le morphisme", r"bis)]<NL>\item \emph{Le morphisme}",
    "One edit: it also gives the underline.")
add(321, "Lemme 7.2.1 (i bis), 'p ≤ m-1, est un monomorphisme de conoyau libre pour p = m .'",
    "', est un monomorphisme de conoyau libre pour'; underlined: 'est un isomorphisme pour' | "
    "'est un monomorphisme de conoyau libre pour'",
    "$p\\le m-1$, et un monomorphisme de conoyau libre pour", "word", "high",
    r"est un isomorphisme pour $p\le m-1$, et un monomorphisme de conoyau libre pour",
    r"\emph{est un isomorphisme pour} $p\le m-1$, \emph{est un monomorphisme de conoyau libre pour}",
    "The TeX writes 'et' for the printed 'est' (with the comma the printed sentence construes, so not a "
    "misprint). One edit: it also gives the underline.")
add(321, "proof, 'Le diagramme d'implications suivant est évident'",
    "no colon after 'évident'", "suivant est évident:", "punctuation", "high",
    r"suivant est évident:", r"suivant est évident",
    "The TeX adds a colon.")
add(321, "proof, diagram, '(i) ⇒ (i bis)'",
    "no full stop after '(i bis)'", "\\text{(i bis).}", "punctuation", "high",
    r"\text{(i bis).}", r"\text{(i bis)}",
    "The TeX adds a full stop.")
add(321, "last display, 'H^p(V) ⊗ k_V = 0 (p ≤ m-1)'",
    "'H^p(V) ⊗ k_V' with V (clear in the scan)", "H^p(M)\\otimes k_V=0", "misprint_in_print", "high",
    r"H^p(M)\otimes k_V", r"H^p(V)\otimes k_V",
    "Typing error: the Künneth sequence for N = k_V gives H^p(M) ⊗ k_V = 0. The TeX silently corrects it.",
    corrected=r"H^p(M)\otimes k_V")
add(321, "last display, '(p ≤ m-1) et Tor_1^V(H^m(M),k_V) = 0 .'",
    "the two formulas joined by the word 'et'", "(p\\le m-1),\\qquad", "word", "high",
    r"(p\le m-1),\qquad<NL>\operatorname{Tor}", r"(p\le m-1)\quad\text{et}\quad<NL>\operatorname{Tor}",
    "The TeX replaces the printed 'et' by a comma.")
add(321, "derived tensor products of the page (9 places)",
    "the tensor sign with two short bars under it, no letter L (H^p(u ⊗ id_N), H^p(K ⊗ N), H^p(M ⊗ N) = 0, "
    "H^p(M ⊗ k_V), Künneth H^p(M ⊗ N))",
    "\\otimes^L (lines 5 three times, 10, 14 three times, 19, 44)", "symbol", "high",
    note="Convention, not itemized: one global decision with the logged pp. 285 and 289 (GLOBAL_ISSUES 89(g)); "
         "those items write \\mathbin{\\underline{\\underline{\\otimes}}}. Replacing every '\\otimes^L' of "
         "page_321.tex (9) does it for these pages; pp. 322-325 have no derived tensor. The misprint item above "
         "(K for L) avoids the tensor in its old.")

# ---------------------------------------------------------------- p. 322
add(322, "Proposition 7.3, 'Soient X un k-schéma propre, lisse, connexe, de dimension n,'",
    "underlined: 'Soient' | 'un' | 'schéma propre, lisse, connexe, de dimension'",
    "no underline markup", "underline", "high",
    r"Soient $X$ un $k$-schéma propre, lisse, connexe, de dimension $n$,",
    r"\emph{Soient} $X$ \emph{un} $k$-\emph{schéma propre, lisse, connexe, de dimension} $n$,", UL)
add(322, "Proposition 7.3, 'E un O_X-Module localement libre de rang constant r'",
    "'Module' with a capital M; underlined: 'un' | 'Module localement libre de rang constant'",
    "$E$ un $\\mathcal O_X$-module localement libre de rang constant $r$", "word", "high",
    r"$E$ un $\mathcal O_X$-module localement libre de rang constant $r$",
    r"$E$ \emph{un} $\mathcal O_X$-\emph{Module localement libre de rang constant} $r$",
    "The typescript's capital M (sheaf of modules), as the applied 'Module' of pp. 282-295. One edit: it also "
    "gives the underline.")
add(322, "Proposition 7.3, 'et Y le lieu des zéros d'une section de V(Ě) transversale à la section nulle. Notant'",
    "underlined: 'et' | 'le lieu des zéros d'une' / 'section' 'de' | 'transversale à la section nulle. Notant'",
    "no underline markup", "underline", "high",
    r", et $Y$ le lieu des zéros d'une section de $V(\check E)$ transversale à la section nulle. Notant",
    r", \emph{et} $Y$ \emph{le lieu des zéros d'une section de} $V(\check E)$ "
    r"\emph{transversale à la section nulle. Notant}", "")
add(322, "Proposition 7.3, 'le morphisme de Gysin correspondant on a l'égalité'",
    "no comma after 'correspondant'; underlined: 'le morphisme canonique et' | 'le morphisme de Gysin "
    "correspondant on a l'égalité'",
    "correspondant, on a l'égalité", "punctuation", "high",
    r"le morphisme canonique et $p_*$ le morphisme de Gysin correspondant, on a l'égalité",
    r"\emph{le morphisme canonique et} $p_*$ \emph{le morphisme de Gysin correspondant on a l'égalité}",
    "The TeX adds a comma. One edit: it also gives the underline.")
add(322, "Proposition 7.3, 'dans H^0(k,Q_ℓ) = Q_ℓ .'",
    "'dans' underlined", "dans $H^0(k,\\mathbb Q_\\ell)=\\mathbb Q_\\ell$.", "underline", "high",
    r"dans $H^0(k", r"\emph{dans} $H^0(k", "")
add(322, "display (7.3.1)",
    "no punctuation after '→ 0'", "\\to\\Omega_Y^1\\to0,", "punctuation", "high",
    r"\to\Omega_Y^1\to0,", r"\to\Omega_Y^1\to0",
    "The TeX adds a comma at the end of the display.")
add(322, "display (7.3.2)",
    "no punctuation at the end", "c(E)^{-1}\\bigr).", "punctuation", "high",
    r"c(E)^{-1}\bigr).<NL>\tag{7.3.2}", r"c(E)^{-1}\bigr)<NL>\tag{7.3.2}",
    "The TeX adds a full stop at the end of the display.")
add(322, "'On en déduit par (3.10) l'expression suivante pour EP(Y)'",
    "no colon after EP(Y)", "pour $\\operatorname{EP}(Y)$:", "punctuation", "high",
    r"pour $\operatorname{EP}(Y)$:", r"pour $\operatorname{EP}(Y)$",
    "The TeX adds a colon.")
add(322, "display EP(Y) = p_*i_*i^*(c(Ω̌_X^1)c(E)^{-1})",
    "no punctuation at the end", "c(E)^{-1}\\bigr),", "punctuation", "high",
    r"c(E)^{-1}\bigr),<NL>\]", r"c(E)^{-1}\bigr)<NL>\]",
    "The TeX adds a comma at the end of the display.")

# ---------------------------------------------------------------- p. 323
add(323, "Corollaire 7.4, 'Soient X un k-schéma propre, lisse, connexe, de dimension n et Y'",
    "no comma after n; underlined: 'Soient' | 'un' | 'schéma propre, lisse, connexe, de dimension' | 'et'",
    "de dimension $n$, et $Y$", "punctuation", "high",
    r"Soient $X$ un $k$-schéma propre, lisse, connexe, de dimension $n$, et $Y$",
    r"\emph{Soient} $X$ \emph{un} $k$-\emph{schéma propre, lisse, connexe, de dimension} $n$ \emph{et} $Y$",
    "The TeX adds a comma. One edit: it also gives the underline. " + UL)
add(323, "Corollaire 7.4, 'un sous-schéma fermé lisse de dimension n-1 de X , défini donc par une section d'un'",
    "underlined: 'un sous-schéma fermé lisse de dimension' | 'de' | 'défini donc par une section' / 'd'un'",
    "no underline markup", "underline", "high",
    r" un sous-schéma fermé lisse de dimension $n-1$ de $X$, défini donc par une section d'un",
    r" \emph{un sous-schéma fermé lisse de dimension} $n-1$ \emph{de} $X$, "
    r"\emph{défini donc par une section d'un}", "")
add(323, "Corollaire 7.4, 'O_X- Module inversible L . Notant'",
    "'Module' with a capital M; underlined: 'Module inversible' | 'Notant'",
    "$\\mathcal O_X$-module inversible $L$. Notant", "word", "high",
    r"$\mathcal O_X$-module inversible $L$. Notant",
    r"$\mathcal O_X$-\emph{Module inversible} $L$. \emph{Notant}",
    "The typescript's capital M. One edit: it also gives the underline.")
add(323, "Corollaire 7.4, 'p le morphisme canonique de X dans k et'",
    "underlined: 'le morphisme canonique de' | 'dans' | 'et'", "no underline markup", "underline", "high",
    r" $p$ le morphisme canonique de $X$ dans $k$ et",
    r" $p$ \emph{le morphisme canonique de} $X$ \emph{dans} $k$ \emph{et}",
    "List before the misprint item on p_* below.")
add(323, "Corollaire 7.4, 'le morphisme de Gysin correspondant, on a l'égalité'",
    "underlined (the comma is printed)", "no underline markup", "underline", "high",
    r"le morphisme de Gysin correspondant, on a l'égalité",
    r"\emph{le morphisme de Gysin correspondant, on a l'égalité}", "")
add(323, "Corollaire 7.4, 'et p le morphisme de Gysin correspondant'",
    "a plain p at the end of the line, no star (the scan is clean white after it)",
    "$p_*$", "misprint_in_print", "high",
    r"\emph{et} $p_*$", r"\emph{et} $p$",
    "Typing error: the Gysin morphism is p_* (as in Proposition 7.3). The TeX silently corrects it. The old is "
    "taken from the text after the underline edit 'le morphisme canonique de X dans k et' (listed before).",
    corrected=r"\emph{et} $p_*$", dep=True)
add(323, "Corollaire 7.4, 'dans H^0(k,Q_ℓ) = Q_ℓ .'",
    "'dans' underlined", "no underline markup", "underline", "high",
    r"dans $H^0", r"\emph{dans} $H^0", "")
add(323, "Corollaire 7.4, 'H^0(k,Q_ℓ) = Q_ℓ'",
    "both Q are plain typed capitals: no hand-drawn second stroke, crisp letters with no trace of one "
    "(p. 322 has the double-struck Q in the same formula)",
    "(k,\\mathbb Q_\\ell)=\\mathbb Q_\\ell$.", "font", "medium",
    r"(k,\mathbb Q_\ell)=\mathbb Q_\ell$.", r"(k,\mathrm{Q}_\ell)=\mathrm{Q}_\ell$.",
    "Plain Q where the TeX writes \\mathbb Q (written \\mathrm{Q} as the applied plain R, pp. 283-289). The "
    "other Q_ℓ of pp. 322-325 are double-struck except H^2(X,Q_ℓ(1)) on p. 325. One decision with GLOBAL_ISSUES "
    "77(f) (plain for double-struck); drop if the volume keeps \\mathbb there.")
add(323, "Corollaire 7.4, 'De plus' before (7.4.2)",
    "no comma after 'De plus'; underlined", "De plus,", "punctuation", "high",
    r"De plus,", r"\emph{De plus}",
    "The TeX adds a comma. One edit: it also gives the underline.")
add(323, "display (7.4.2)",
    "no punctuation at the end", "c(L)^{-1}\\bigr).", "punctuation", "high",
    r"c(L)^{-1}\bigr).<NL>\tag{7.4.2}", r"c(L)^{-1}\bigr)<NL>\tag{7.4.2}",
    "The TeX adds a full stop at the end of the display.")
add(323, "proof of 7.4, 'provient de 7.3 et de 4.2 compte tenu de'",
    "no comma after 4.2", "de 4.2, compte tenu", "punctuation", "high",
    r"de 4.2, compte tenu", r"de 4.2 compte tenu", "The TeX adds a comma.")
add(323, "proof of 7.4, display 1 - c(L)^{-1}c_1(L) = c(L)^{-1}",
    "no punctuation at the end", "=c(L)^{-1}.", "punctuation", "high",
    r"=c(L)^{-1}.<NL>\]", r"=c(L)^{-1}<NL>\]",
    "The TeX adds a full stop at the end of the display.")
add(323, "Corollaire 7.5, first sentence",
    "underlined: 'Soit' | 'un sous-schéma lisse, connexe et de dimension' | 'de' | 'intersection complète "
    "globale de' | 'diviseurs de'", "no underline markup", "underline", "high",
    r"Soit $X$ un sous-schéma lisse, connexe et de dimension $n$ de $\mathbb P_k^{\,n+r}$, intersection "
    r"complète globale de $r$ diviseurs de",
    r"\emph{Soit} $X$ \emph{un sous-schéma lisse, connexe et de dimension} $n$ \emph{de} $\mathbb P_k^{\,n+r}$, "
    r"\emph{intersection complète globale de} $r$ \emph{diviseurs de}",
    "(The plain typed P of P_k^{n+r} is GLOBAL_ISSUES 89(c), not itemized.)")
add(323, "Corollaire 7.5, 'soient X_1,X_2,...,X_r.'",
    "'soient' underlined", "no underline markup", "underline", "high",
    r"$, soient $X_1", r"$, \emph{soient} $X_1", "")
add(323, "Corollaire 7.5, 'Pour tout entier i ∈ (1,r) , on note d_i le degré de X_i . Alors :'",
    "'i ∈ (1,r)' with parentheses; underlined: 'Pour tout entier' | 'on note' | 'le degré de' | 'Alors'",
    "$i\\in\\{1,\\ldots,r\\}$", "formula", "high",
    r"Pour tout entier $i\in\{1,\ldots,r\}$, on note $d_i$ le degré de $X_i$. Alors:",
    r"\emph{Pour tout entier} $i\in(1,r)$, \emph{on note} $d_i$ \emph{le degré de} $X_i$. \emph{Alors}:",
    "The TeX writes the set {1,...,r} for the printed (1,r). One edit: it also gives the underline. The same "
    "(1,r) on p. 324 (item filed under p. 323 below).")
add(323, "Corollaire 7.5 (i), 'Les groupes de cohomologie'",
    "'Les' with a capital L; underlined", "\\item les groupes de cohomologie", "word", "high",
    r"\item les groupes de cohomologie", r"\item \emph{Les groupes de cohomologie}",
    "One edit: it also gives the underline.")
add(323, "Corollaire 7.5 (i), 'sont des Z_ℓ-modules libres de type fini.'",
    "full stop at the end; underlined: 'sont des' | 'modules libres de type fini'",
    "...de type fini;", "punctuation", "high",
    r"sont des $\mathbb Z_\ell$-modules libres de type fini;",
    r"\emph{sont des} $\mathbb Z_\ell$-\emph{modules libres de type fini}.",
    "The TeX has a semicolon for the print's full stop. One edit: it also gives the underline.")
add(323, "Corollaire 7.5 (ii), 'Si p est un entier ≤ 2n et ≠ n ,'",
    "'Si' with a capital S; underlined: 'Si' | 'est un entier' | 'et'", "\\item si $p$ est un entier",
    "word", "high",
    r"\item si $p$ est un entier $\le 2n$ et", r"\item \emph{Si} $p$ \emph{est un entier} $\le 2n$ \emph{et}",
    "One edit: it also gives the underline.")
add(323, "Corollaire 7.5 (ii), '≠ n ,' before the display",
    "no 'alors'", "$\\ne n$, alors", "extra", "high",
    r"$\ne n$, alors", r"$\ne n$,", "The TeX adds 'alors'.")
add(323, "Corollaire 7.5 (ii), display H^p(X,Z_ℓ) ≃ {...",
    "the relation sign is ≃ (a tilde over one bar)", "H^p(X,\\mathbb Z_\\ell)=", "symbol", "high",
    r"\mathbb Z_\ell)=<NL>\begin{cases}", r"\mathbb Z_\ell)\simeq<NL>\begin{cases}", "")
add(323, "Corollaire 7.5 (ii), first case '0 si p est impair'",
    "no commas; underlined: 'si' | 'est impair'", "0,&\\text{si }p\\text{ est impair},\\\\",
    "punctuation", "high",
    r"0,&\text{si }p\text{ est impair},\\", r"0&\text{\emph{si} }p\text{ \emph{est impair}}\\",
    "The TeX adds two commas. One edit: it also gives the underline.")
add(323, "Corollaire 7.5 (ii), second case 'Z_ℓ si p est pair.'",
    "no comma after Z_ℓ; full stop at the end; underlined: 'si' | 'est pair'",
    "\\mathbb Z_\\ell,&\\text{si }p\\text{ est pair};", "punctuation", "high",
    r"\mathbb Z_\ell,&\text{si }p\text{ est pair};", r"\mathbb Z_\ell&\text{\emph{si} }p\text{ \emph{est pair}}.",
    "The TeX adds a comma and has a semicolon for the print's full stop. One edit: it also gives the underline.")
add(323, "Corollaire 7.5 (iii), 'La caractéristique d'Euler-Poincaré de X est donnée par la formule'",
    "'La' with a capital L; underlined: 'La caractéristique d'Euler-Poincaré de' | 'est donnée par la formule'",
    "\\item la caractéristique", "word", "high",
    r"\item la caractéristique d'Euler-Poincaré de $X$ est donnée par la formule",
    r"\item \emph{La caractéristique d'Euler-Poincaré de} $X$ \emph{est donnée par la formule}",
    "One edit: it also gives the underline.")
add(323, "proof of 7.5, 'correspondant et ξ la classe de O_P(1)' (printed at the top of p. 324)",
    "no comma after 'correspondant'", "correspondant, et $\\xi$", "punctuation", "high",
    r"correspondant, et $\xi$", r"correspondant et $\xi$",
    "Printed on p. 324; filed under p. 323, where the line stands until the marker move of p. 324. The edit "
    "does not touch the move's anchor 'correspondant'.")
add(323, "proof of 7.5, 'Pour tout i ∈ (1,r), le schéma X_i' (printed on p. 324)",
    "'i ∈ (1,r)' with parentheses", "$i\\in\\{1,\\ldots,r\\}$", "formula", "high",
    r"Pour tout $i\in\{1,\ldots,r\}$, le schéma", r"Pour tout $i\in(1,r)$, le schéma",
    "As the (1,r) of Corollaire 7.5. Printed on p. 324; filed under p. 323 until the marker move of p. 324.")

# ---------------------------------------------------------------- p. 324
add(324, "top of the page: 'correspondant et ξ la classe de O_P(1). Pour tout i ∈ (1,r), le schéma X_i est dé-'",
    "p. 324 begins with 'correspondant et ξ la classe de O_P(1).'; p. 323 ends with 'p_* le morphisme de Gysin'",
    "'correspondant, et $\\xi$ ... est défini par une' is the end of the last line of page_323.tex (diplomatic "
    "s5.tex line 10944, current 10940); page_324.tex begins with 'section d'un'",
    "marker", "high",
    note="Page 324 really begins at 'correspondant' in the last line of page_323.tex. Exact fix: python -I "
         "move_marker.py 5 324 'correspondant' --before (simulated in memory on both layers: the last "
         "'correspondant' before the marker is that one; the line is split there and the marker set before "
         "'correspondant, et $\\xi$'). Text not moved. The two items filed under p. 323 for this text keep the "
         "anchor 'correspondant' intact.")
add(324, "'section d'un O_P-Module inversible L_i'",
    "'Module' with a capital M", "$\\mathcal O_P$-module", "word", "high",
    r"$\mathcal O_P$-module", r"$\mathcal O_P$-Module",
    "The typescript's capital M, as the applied 'Module' of pp. 282-295.")
add(324, "Euler sequence 0 → Ω_P^1 ⊗ C_p(1) → O_P^{n+r+1} → O_P(1) → 0 , the second term",
    "a typed capital C (serifed terminals, open right side), not an O",
    "\\Omega_P^1\\otimes\\mathcal O_P(1)", "misprint_in_print", "high",
    r"\Omega_P^1\otimes\mathcal O", r"\Omega_P^1\otimes C",
    "Typing error for O_P(1) (the Euler sequence twisted by O_P(1)); the TeX silently corrects it. Changes only "
    "the letter; independent of the small-p item that follows (adjacent olds, no overlap).",
    corrected=r"\Omega_P^1\otimes\mathcal O")
add(324, "Euler sequence, subscript of C_p(1)",
    "a small p: 21 rows, bowl 14 rows, stem 7 rows below it, top 4 rows below the foot of the C; the capital P "
    "subscripts of O_P^{n+r+1} and O_P(1) in the same display: 21-22 rows, bowl 12, stem 9, top at the foot of "
    "the O",
    "\\mathcal O_P(1)", "misprint_in_print", "medium",
    r"_P(1)\to\mathcal O_P^{\,n+r+1}", r"_p(1)\to\mathcal O_P^{\,n+r+1}",
    "As the small-p subscripts of pp. 286-295 (GLOBAL_ISSUES 89(h), all or none). The TeX silently corrects it.",
    corrected=r"_P(1)\to\mathcal O_P^{\,n+r+1}")
add(324, "display c(Ω̌_P^1) = (1+ξ)^{n+r+1}",
    "no punctuation at the end", "(1+\\xi)^{\\,n+r+1}.", "punctuation", "high",
    r"(1+\xi)^{\,n+r+1}.", r"(1+\xi)^{\,n+r+1}",
    "The TeX adds a full stop at the end of the display.")
add(324, "'On déduit alors de (7.3) l'expression suivante pour EP(X).'",
    "full stop after EP(X)", "pour $\\operatorname{EP}(X)$:", "punctuation", "high",
    r"pour $\operatorname{EP}(X)$:", r"pour $\operatorname{EP}(X)$.",
    "The TeX has a colon for the print's full stop.")
add(324, "Remarque 7.6, 'calculs de Hirzebruch (3, p.160-161)'",
    "'(3, p.160-161)': no brackets around 3, a hyphen between the pages", "([3], p. 160--161)",
    "punctuation", "high",
    r"([3], p. 160--161)", r"(3, p. 160-161)",
    "The TeX adds brackets and writes an en dash (the print has '([4])' with brackets in 7.7).")
add(324, "7.7, footnote call after 'l'énoncé suivant.'",
    "'l'énoncé suivant.(*)' with a raised (*); the conjecture 'Si X est ...' begins a new indented paragraph",
    "'l'énoncé suivant. Si $X$ est' (no call, same paragraph)", "missing", "high",
    r"l'énoncé suivant.", r"l'énoncé suivant.$^{(*)}$<NL><NL>",
    "The footnote call; the edit also starts the conjecture's paragraph, as printed (drop the blank line if "
    "paragraphing is left to a global pass). Apply together with the footnote item below.")
add(324, "7.7, 'Si X est un k-schéma projectif, lisse et connexe de dimension n et ξ la classe dans'",
    "no comma after n; underlined: 'Si' | 'est un' | 'schéma projectif, lisse et connexe de dimension' | 'et' "
    "| 'la classe dans'",
    "de dimension $n$, et $\\xi$", "punctuation", "high",
    r"Si $X$ est un $k$-schéma projectif, lisse et connexe de dimension $n$, et $\xi$ la classe dans",
    r"\emph{Si} $X$ \emph{est un} $k$-\emph{schéma projectif, lisse et connexe de dimension} $n$ \emph{et} "
    r"$\xi$ \emph{la classe dans}",
    "The TeX adds a comma. One edit: it also gives the underline of the conjecture (printed as a statement). " + UL)
add(324, "7.7, 'd'un O_X-Module inversible très ample, ... la multiplication par ξ^{n-p} :'",
    "'Module' with a capital M (the O is hand-drawn script); underlined: 'd'un' | 'Module inversible très "
    "ample, alors pour tout' | 'faisceau constant tordu' | 'et tout entier' | 'la multiplication par'",
    "$\\mathcal O_X$-module inversible très ample", "word", "high",
    r"d'un $\mathcal O_X$-module inversible très ample, alors pour tout $\mathbb Q_\ell$-faisceau constant tordu "
    r"$L$ et tout entier $p\le n$, la multiplication par",
    r"\emph{d'un} $\mathcal O_X$-\emph{Module inversible très ample, alors pour tout} $\mathbb Q_\ell$-"
    r"\emph{faisceau constant tordu} $L$ \emph{et tout entier} $p\le n$, \emph{la multiplication par}",
    "The typescript's capital M. One edit: it also gives the underline.")
add(324, "7.7, 'est un isomorphisme.' after the display",
    "underlined", "no underline markup", "underline", "high",
    r"\]<NL>est un isomorphisme", r"\]<NL>\emph{est un isomorphisme}", "")
add(324, "footnote at the foot of the page, '(*) Comme Deligne l'a observé, ...'",
    "below a short rule, a footnote beginning with '(*)'",
    "'Comme Deligne l'a observé, ...' runs on in the paragraph after 'est un isomorphisme.', without the mark",
    "missing", "high",
    r". Comme Deligne", r".<NL><NL>\(\quad (*)\) Comme Deligne",
    "The footnote mark, written as the file writes the footnotes of Exposé VII (p. 281; applied p. 284). Apply "
    "together with the call above.")
add(324, "footnote, 'lorsque de plus L est \"pur\".'",
    "straight typewriter double quotes", "«pur»", "punctuation", "high",
    r"«pur»", r"``pur''",
    "The TeX adds guillemets; ``...'' as the file writes the print's straight quotes.")

# ---------------------------------------------------------------- p. 325
add(325, "statement after 7.7, 'Soient X un k-schéma projectif lisse, connexe, de dimension n , Y une section "
         "hyperplane lisse de X ,'",
    "underlined: 'Soient' | 'un' | 'schéma projectif lisse, connexe, de dimension' | 'une section hyperplane "
    "lisse de'", "no underline markup", "underline", "high",
    r"Soient $X$ un $k$-schéma projectif lisse, connexe, de dimension $n$, $Y$ une section hyperplane lisse de $X$,",
    r"\emph{Soient} $X$ \emph{un} $k$-\emph{schéma projectif lisse, connexe, de dimension} $n$, $Y$ "
    r"\emph{une section hyperplane lisse de} $X$,", UL)
add(325, "statement after 7.7, 'X , L un Q_ℓ-faisceau constant tordu sur X .'",
    "no 'et' before L; underlined: 'un' | 'faisceau constant tordu sur'",
    "de $X$, et $L$ un", "extra", "high",
    r" et $L$ un $\mathbb Q_\ell$-faisceau constant tordu sur $X$.",
    r" $L$ \emph{un} $\mathbb Q_\ell$-\emph{faisceau constant tordu sur} $X$.",
    "The TeX adds 'et'. One edit: it also gives the underline.")
add(325, "(i), 'Le morphisme image réciproque'", "underlined", "no underline markup", "underline", "high",
    r"\item Le morphisme image réciproque", r"\item \emph{Le morphisme image réciproque}", "")
add(325, "(i), 'est un épimorphisme pour p ≥ n .'", "'est un épimorphisme pour' underlined",
    "no underline markup", "underline", "high",
    r"est un épimorphisme pour", r"\emph{est un épimorphisme pour}", "")
add(325, "(ii), 'Le morphisme de Gysin'", "underlined", "no underline markup", "underline", "high",
    r"\item Le morphisme de Gysin", r"\item \emph{Le morphisme de Gysin}", "")
add(325, "(ii), 'est un monomorphisme pour p ≤ n-2 .'", "'est un monomorphisme pour' underlined",
    "no underline markup", "underline", "high",
    r"est un monomorphisme pour", r"\emph{est un monomorphisme pour}", "")
add(325, "proof, 'la classe dans H^2(X,Q_ℓ(1))'",
    "a plain typed Q, no hand-drawn second stroke (the Q of 'H^2(Y,Q_ℓ(1))' in the same line has it)",
    "H^2(X,\\mathbb Q_\\ell(1))", "font", "medium",
    r"H^2(X,\mathbb Q_\ell(1))", r"H^2(X,\mathrm{Q}_\ell(1))",
    "As the two plain Q of p. 323 (Corollaire 7.4); one decision with GLOBAL_ISSUES 77(f).")
add(325, "diagram, bottom right H^{2n-2-q}(Y,(L|Y)(n-1-q)",
    "only one closing parenthesis at the end: the parenthesis opened by '(Y,' is not closed",
    "H^{2n-2-q}(Y,(L|Y)(n-1-q))", "misprint_in_print", "high",
    r"(Y,(L|Y)(n-1-q))", r"(Y,(L|Y)(n-1-q)",
    "A closing parenthesis is missing in the print; the TeX silently adds it.",
    corrected=r"(Y,(L|Y)(n-1-q))")
add(325, "last line, 'diagramme suivant, avec p ≤ n-1 .'",
    "full stop at the end (the page ends here)", "avec $p\\le n-1$:", "punctuation", "high",
    r"avec $p\le n-1$:", r"avec $p\le n-1$.",
    "The TeX has a colon for the print's full stop.")
add(325, "end of the page: the second diagram",
    "p. 325 ends with 'diagramme suivant, avec p ≤ n-1 .'; the diagram H^p(Y,(L|Y)(-1)) → H^{p+2}(X,L) ... is "
    "printed on p. 326",
    "page_325.tex ends with the opening of that display ('\\[', '\\begin{array}{ccc}', 'H^p(Y,(L|Y)(-1))&'; "
    "diplomatic s5.tex lines 11006-11008, current 11002-11004); page_326.tex begins inside the array",
    "marker", "high",
    note="Page 326 really begins at that '\\[' (page_325.tex line 30). Exact fix: python -I move_marker.py 5 326 "
         "'\\[' --before (simulated in memory on both layers: the marker lands just before that line, diplomatic "
         "11006, current 11002). Text not moved; the same move as the top of p. 326 (batch 326-330).")

# ---------------------------------------------------------------- checks and output
problems = []
for page in sorted({f["page"] for f in F}):
    orig = (B / f"page_{page}.tex").read_text(encoding="utf-8")
    assert "\r" not in orig
    cur = orig
    for f in [f for f in F if f["page"] == page]:
        fx = f["fix"]
        if fx is None:
            continue
        o, n = fx["old"], fx["new"]
        c_now = cur.count(o)
        c_orig = orig.count(o)
        if c_now != 1:
            problems.append((page, "not unique at application", c_now, o[:70]))
        if not f["_dep"] and c_orig != 1:
            problems.append((page, "not unique in original", c_orig, o[:70]))
        if f["_dep"] and c_orig != 0:
            problems.append((page, "dependent item found in original", c_orig, o[:70]))
        if "%%%%%%%%%%" in o or "%%%%%%%%%%" in n:
            problems.append((page, "touches a marker line", 0, o[:70]))
        cur = cur.replace(o, n, 1)
    # corrected edition: skip misprint fixes; every other old must still apply
    cur2 = orig
    for f in [f for f in F if f["page"] == page]:
        fx = f["fix"]
        if fx is None or f["kind"] == "misprint_in_print":
            continue
        if cur2.count(fx["old"]) != 1:
            problems.append((page, "corrected edition: not unique", cur2.count(fx["old"]), fx["old"][:70]))
        cur2 = cur2.replace(fx["old"], fx["new"], 1)
print("problems:", problems if problems else "none")
for f in F:
    del f["_dep"]
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
counts = {}
for f in F:
    k = counts.setdefault(f["page"], [0, 0])
    k[1 if f["kind"] == "misprint_in_print" else 0] += 1
print("counts (normal/misprint):", counts, "total", len(F))
