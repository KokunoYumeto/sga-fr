"""Build findings_496_500.json and check that every fix's old string occurs exactly once in its page file."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b496_500"
OUT = RUN / "findings_496_500.json"

F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": confidence, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- p. 496 (Exposé VIII, folio 31) ----------------
add(496, "display (5.4.3)",
    "f_gr(exp(kx). x^{r+1}/(1-exp(-x))^{r+1}) with no punctuation after the closing parenthesis (both scans)",
    r"f_{\mathrm{gr}}\left(\exp(kx)\cdot \frac{x^{r+1}}{(1-\exp(-x))^{r+1}}\right).",
    "punctuation", "high",
    {"old": r"\right).", "new": r"\right)"},
    "The TeX adds a full stop at the end of the display.")

add(496, "'On peut alors écrire la serie φ_k = ...'",
    "serie: no accent on the first e (both scans; crops_496_500/c496_serie.png, w496_serie.png), while 'écrire' on the same line has its accent",
    r"la serie \(\varphi_k=...\) (printed reading kept)",
    "misprint_in_print", "high", None,
    "Typing slip of the typescript (lower-case e without its accent). The TeX keeps the printed reading.",
    corrected="la série")

add(496, "end of the sentence 'et que 1,...,x^r sont linéairement indépendants sur GrK˙(Y)', before the paragraph 'On peut alors écrire'",
    "no full stop after GrK˙(Y): nothing on the line after the closing parenthesis (both scans; crops_496_500/c496_GrKY.png, w496_GrKY.png)",
    r"indépendants sur \(\Gr K^{\bullet}(Y)\).",
    "misprint_in_print", "medium",
    {"old": r"indépendants sur \(\Gr K^{\bullet}(Y)\).", "new": r"indépendants sur \(\Gr K^{\bullet}(Y)\)"},
    "The sentence ends without its full stop in the print; the TeX silently adds it. The fix restores the printed reading.",
    corrected=r"indépendants sur \(\Gr K^{\bullet}(Y)\).")

add(496, "'combinaison linéaire à coefficients dans GrK˙(Y)_Q des éléments 1,...,x^r'",
    "a hand-drawn wide hat over GrK˙(Y)_Q, from the G to past the double-struck Q: the completion (both scans; crops_496_500/c496_hat.png, w496_hat.png)",
    r"\(\Gr K^{\bullet}(Y)_{\mathbb Q}\) (no hat)",
    "formula", "high",
    {"old": r"\(\Gr K^{\bullet}(Y)_{\mathbb Q}\)", "new": r"\(\widehat{\Gr K^{\bullet}(Y)_{\mathbb Q}}\)"},
    "The TeX drops the completion hat (the series φ_k has its coefficients in the completed ring).")

add(496, "(RR), first line 'pour -r ≤ k < 0, le coefficient de x^r dans φ_k est 0 ;'",
    "est 0 ; (semicolon; both scans)",
    r"\text{ est }0,\\",
    "punctuation", "high",
    {"old": r"\text{ est }0,\\", "new": r"\text{ est }0~;\\"},
    "Comma for the print's semicolon; '~;' is the file's form (5.4.4).")

add(496, "product dot of pp. 496-500 (convention, reported once)",
    "the typescript types the product as a full stop on the line: exp(kx). (twice, (5.4.3) and φ_k), exp(kx).dx (p. 496), (1-y)^{-k-1}.dy (p. 497), I^m.H, I^n.K (p. 499), ξ_i.f*(x_i) (p. 500) (both scans)",
    r"\cdot in all seven places",
    "symbol", "low", None,
    r"Convention of the transcription, not itemized: \cdot raises the typed stop to mid-height (same kind as the low entries for '1.u' p. 321 and λ^n(x).t^n p. 325, findings_321_325). Exposé IX has 21 \cdot. Three examples in the form to use if the diplomatic layer keeps the typed stop: p. 496 '\exp(kx)\cdot dx' -> '\exp(kx).dx'; p. 497 '(1-y)^{-k-1}\cdot dy' -> '(1-y)^{-k-1}.dy'; p. 499 'I^m\cdot H=0' -> 'I^m.H=0'.")

# ---------------- p. 497 (Exposé VIII, folio 32) ----------------
add(497, "display after 'on se ramène à calculer le résidu de :', followed by 'c'est-à-dire le coefficient ...'",
    "(1-y)^{-k-1}.dy / y^{r+1}, then a full stop, no comma tail (both scans; crops_496_500/c497_dot.png, w497_dot.png)",
    r"\frac{(1-y)^{-k-1}\cdot dy}{y^{r+1}},",
    "misprint_in_print", "medium",
    {"old": r"{y^{r+1}},", "new": r"{y^{r+1}}."},
    "A full stop before the lower-case 'c'est-à-dire' that continues the sentence: a slip for a comma. The TeX silently writes the comma; the fix restores the printed stop.",
    corrected=r"{y^{r+1}},")

add(497, "heading of the bibliography",
    "BIBLIOGRAPHIE: typed capitals, underlined (both scans)",
    r"\subsection*{Bibliographie}",
    "word", "medium",
    {"old": r"\subsection*{Bibliographie}", "new": r"\subsection*{BIBLIOGRAPHIE}"},
    "As the headings fixed on pp. 19, 159, 220, 273, 296 and 364; the missing underline of a section title is accepted.")

add(497, "bibliography [1] Borel-Serre, title",
    "'Le théorème de Riemann-Roch,' typed plain, not underlined (both scans)",
    r"\emph{Le théorème de Riemann--Roch}",
    "font", "high",
    {"old": r"\emph{Le théorème de Riemann--Roch}", "new": r"Le théorème de Riemann--Roch"},
    "The typescript neither underlines nor italicizes the titles of this bibliography; same fix as the bibliographies of pp. 19, 159, 273, 296, 364.")

add(497, "bibliography [2] Grothendieck, title",
    "'Techniques de construction et théorèmes d'existence en Géométrie Algébrique,' typed plain, not underlined (both scans)",
    r"\emph{Techniques de construction et théorèmes d'existence en Géométrie Algébrique}",
    "font", "high",
    {"old": r"\emph{Techniques de construction et théorèmes d'existence en Géométrie Algébrique}",
     "new": r"Techniques de construction et théorèmes d'existence en Géométrie Algébrique"},
    "As entry [1].")

add(497, "bibliography [2], 'Sém. Bourbaki, 1960-61.'",
    "1960-61: typed hyphen (both scans)",
    r"1960--61",
    "punctuation", "high",
    {"old": r"1960--61", "new": r"1960-61"},
    "En dash added by the transcription, as the bibliography ranges fixed on pp. 220-221.")

# ---------------- p. 498 (Exposé IX, folio 1) ----------------
add(498, "heading and title of Exposé IX",
    "two blocks: 'E X P O S E  IX' (typed capitals, letter-spaced, single underline, no full stop) at the left; then the centred title 'QUELQUES CALCULS DE GROUPES K' in typed capitals with a double underline, the K with no dot below or above (both scans; crops_496_500/c498_K.png, w498_K.png)",
    r"\section*{Exposé IX. Quelques calculs de groupes $K_\bullet$}",
    "word", "medium",
    {"old": r"\section*{Exposé IX. Quelques calculs de groupes $K_\bullet$}",
     "new": r"\section*{\underline{EXPOSÉ IX}\\[3pt] \underline{\underline{QUELQUES CALCULS DE GROUPES $K$}}}"},
    r"The TeX joins the two lines with an added full stop, sets the title in small letters and adds a subscript bullet to the title's K (the text writes K. with its dot from the first paragraph on). Same form as the applied headings of Exposés III and IV (\section*{\underline{EXPOSÉ III}\\[3pt] \underline{\underline{...}}}); É keeps the TeX's accent (rule for typed capitals).")

add(498, "author line of the heading",
    "'par P. BERTHELOT': the name in capitals, the line underlined (both scans)",
    r"par P. Berthelot",
    "word", "medium",
    {"old": r"par P. Berthelot", "new": r"\underline{par P. BERTHELOT}"},
    "As the applied author lines of Exposés I-VI (\\underline{par P. BERTHELOT}, p. 297).")

add(498, "label of Proposition 1.1",
    "'Proposition 1.1. (Suite exacte d'homotopie).': a full stop after 1.1 (both scans; crops_496_500/c498_prop.png)",
    r"\textbf{Proposition 1.1 (suite exacte d'homotopie).}",
    "punctuation", "medium",
    {"old": r"Proposition 1.1 (", "new": r"Proposition 1.1. ("},
    "The label's number has its full stop in the print (as 'Proposition 1.2.' on p. 500). Independent of the next entry (disjoint strings).")

add(498, "label of Proposition 1.1, the title in parentheses",
    "(Suite exacte d'homotopie): capital S (both scans)",
    r"(suite exacte d'homotopie).}",
    "word", "high",
    {"old": r"suite exacte d'homotopie).}", "new": r"Suite exacte d'homotopie).}"},
    "Capital against small. The running-text mention in the second paragraph ('la proposition 1.1 (suite exacte d'homotopie) qui') has a small s in the print and stays.")

add(498, "statements of Exposé IX on these pages: Proposition 1.1 (pp. 498-499) and Proposition 1.2 (p. 500)",
    "underlined word group by word group: p. 498 'Soient', 'un schéma noethé-rien', 'un sous-schéma fermé de', 'l'ouvert complémentaire de', 'dans', 'l'immersion de', 'et', 'Alors la suite'; p. 499 'est exacte'; p. 500 'Soient', 'deux schémas noethérien', 'et', 'un morphisme' ('plat' left plain), 'de', 'dans', 'On se donne une famille d'éléments', 'et on considère l'homomorphisme', 'défini par', 'où', 'est l'homomorphisme', 'image inverse', 'défini d'après', 'est considéré comme', '-module par', 'On suppose que pour tout point', 'les images des', 'par', 'l'homomorphisme', 'engendrent', 'comme groupe abélien', 'Alors', 'est surjective' (both scans)",
    r"the statements in roman (Exposé IX has no \underline or \emph in its statements)",
    "underline", "high", None,
    "Exposé IX follows the Exposé II pattern of GLOBAL_ISSUES 82: not itemized, for the scripted per-exposé decision. No \\emph on defined terms the print leaves plain and no category L on these pages.")

# ---------------- p. 499 (Exposé IX, folio 2) ----------------
add(499, "letters of the Modules and the ideal, pp. 499-500 (convention of the Exposé IX transcription, reported once)",
    "F, F', F'', G, G', G'', H, K (Modules) and I (the ideal of X') are underlined, the underline under the letter only, the primes after it: p. 499 'Si F̲' est un', 'i_*(F̲')', 'cl(F̲')', 'Soit G̲', 'cl(F̲) - cl(F̲')', 'j*(F̲ ⊕ F̲')', 'F̲'' → F̲ ⊕ F̲' → F̲', 'Soient alors H̲ et K̲', 'Si I̲ est l'idéal', 'I̲^m.H̲ = 0, I̲^n.K̲ = 0'; p. 500 'annulés par I̲', 'cl(H̲)', 'cl(K̲)', '0 → G̲' → G̲ → G̲'' → 0', 'F̲/F̲'' (both scans). Plain in the print: the schemes X, X', U, S and the K of K.(X)",
    r"plain F, F', F'', G, G', G'', H, K, I throughout",
    "underline", "high", None,
    "Not itemized: 37 places on p. 499 and 14 on p. 500; the exposé's TeX has no \\underline on these letters. One decision for Exposé IX, \\underline{F}', \\underline{G}'' etc. where the print underlines (Exposé 0 writes the underlined Module as \\underline E, p. 6; Exposé V has the same open question, findings_311_315 and 316_320). Three examples in that form: p. 499 'Si $F'$ est un' -> 'Si $\\underline{F}'$ est un'; p. 499 'F''\\longrightarrow F\\oplus F'\\longrightarrow F ;' -> '\\underline{F}''\\longrightarrow \\underline{F}\\oplus \\underline{F}'\\longrightarrow \\underline{F} ;'; p. 500 '\\cl(H)\\in' -> '\\cl(\\underline{H})\\in'. Not for a blind script: the K of K_\\bullet is the same letter as the cokernel K.")

# ---------------- p. 500 (Exposé IX, folio 3) ----------------
add(500, "'une suite exacte de O_U-Module cohérents'",
    "O_U-Module cohérents: Module without its s (both scans; crops_496_500/c500_Module.png)",
    r"$\mathcal O_U$-Module cohérents (printed reading kept)",
    "misprint_in_print", "high", None,
    "Agreement slip of the typescript (Module singular, cohérents plural). The TeX keeps the printed reading.",
    corrected=r"$\mathcal O_U$-Modules cohérents")

add(500, "Proposition 1.2, 'Soient X, S deux schémas noethérien'",
    "noethérien: no final s, a comma follows (both scans; crops_496_500/c500_noeth.png)",
    r"deux schémas noethérien (printed reading kept)",
    "misprint_in_print", "high", None,
    "Agreement slip (deux schémas ... noethériens). The TeX keeps the printed reading.",
    corrected=r"deux schémas noethériens")

add(500, "Proposition 1.2, 'les images des ξ_i dans K.(X_s) par l'homomorphisme :'",
    "l'homomorphisme : (colon before the display; both scans)",
    r"par l'homomorphisme (no colon before \[)",
    "punctuation", "high",
    {"old": r"par l'homomorphisme", "new": r"par l'homomorphisme :"},
    "The TeX drops the colon.")

add(500, "K with a raised dot in Proposition 1.2: 'de K˙(X),', 'comme K˙(X)-module', display 'K˙(X) → K˙(X_s) → K.(X_s)' (convention of the Exposé IX transcription, reported once)",
    "K followed by a filled raised dot (K˙, the K^• of the volume), not a ring (both scans; crops_496_500/c500_Kdot.png, c500_Kdot2.png)",
    r"K^\circ(X), K^\circ(X_s) (four places on p. 500)",
    "symbol", "high", None,
    r"Exposé IX writes K^\circ for the print's raised-dot K: 88 times in main.tex, folios 500-518, and never K^{\bullet} (as Exposé VI § 1 before the 10 Nov script; findings_366_370). Examples in that script's form: 'de $K^\circ(X)$,' -> 'de $K^{\bullet}(X)$,'; 'comme $K^\circ(X)$-module' -> 'comme $K^{\bullet}(X)$-module'; 'K^\circ(X)\longrightarrow K^\circ(X_s)' -> 'K^{\bullet}(X)\longrightarrow K^{\bullet}(X_s)'. Folios 501-518 not checked here.")

# ---------------- checks ----------------
ok = True
for d in F:
    fx = d["fix"]
    if fx is None:
        continue
    t = (B / f"page_{d['page']}.tex").read_text(encoding="utf-8")
    n = t.count(fx["old"])
    marker_hit = "%%%%%%%%%%" in fx["old"]
    if n != 1 or marker_hit:
        ok = False
    print(d["page"], n, "MARKER!" if marker_hit else "", repr(fx["old"])[:90])
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0])
    c[1 if d["kind"] == "misprint_in_print" else 0] += 1
print("all unique:", ok)
print("counts (normal/misprint):", {p: f"{a}/{b}" for p, (a, b) in sorted(counts.items())})
print("written", OUT, len(F))
