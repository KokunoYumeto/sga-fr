"""Build findings_391_395.json (pages 391-395, SGA 6 Exposé VI §§ 3-4)."""
import json
import pathlib

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
NL = "\n"
F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def fx(old, new):
    return {"old": old, "new": new}


STMT_NOTE = ("Exposé II pattern (GLOBAL_ISSUES 82), as on pp. 367-390: not itemized; the word groups are listed "
             "for the scripted pass.")

# ---------------------------------------------------------------- p. 391
add(391, "display after 'en posant :': X_k = P(F_{k-1})",
    "P with two underlines; F_{k-1}, F_k singly underlined (both scans; crops_391_395/w391_top.png)",
    r"X_k=\mathbb P(F_{k-1}) (double-struck P)",
    "font", "high",
    fx(r"X_k=\mathbb P(F_{k-1})", r"X_k=\mathbf P(F_{k-1})"),
    r"The file writes the doubly underlined letters \mathbf (X = \mathbf P(E) in Proposition 2.6, p. 385; "
    r"\mathbf D, \mathbf L, \mathbf R on pp. 389-390). The P of p. 394 is a separate entry.")

add(391, "'où f_k est le morphisme structural X_k → X_{k-1}.' / 'On voit alors qu'il suffit'",
    "'On voit alors' begins a new, indented paragraph; the line ending 'X_{k-1}.' is short (both scans)",
    r"one paragraph: '... \(X_k\to X_{k-1}\). On voit alors ...'",
    "other", "high",
    fx(r"\). On voit alors", r"\)." + NL + NL + "On voit alors"),
    "Missing paragraph break.")

add(391, "'L'homomorphisme λ_t : K˙(S) → 1 + K˙(S)[[t]]^+ étant additif'",
    "a hand-drawn wide hat (a ^-shaped arc) spans K˙(S)[[t]]; the typed + stands as exponent at its right end "
    "(both scans; crops_391_395/m391_arc.png, w391_mid.png)",
    r"1+K^{\bullet}(S)[[t]]^+ (no hat)",
    "symbol", "high",
    fx(r"1+K^{\bullet}(S)[[t]]^+", r"1+\widehat{K^{\bullet}(S)[[t]]}^{+}"),
    r"\widehat is the file's form for printed hats (\Ghat, \widehat{\operatorname{Gr}}^{+} in Exposé V). Same hat "
    r"on p. 392 (separate entry); p. 379 prints 1+K˙(S)[[t]]^+ without it (witness checked), so no pass.")

add(391, "after the second display of V 2.4.2: 'Comme S est un quasi-compact'",
    "'Comme S est un quasi-compact' begins a new, indented paragraph (both scans)",
    r"'\]' followed directly by 'Comme \(S\)' (the paragraph runs on)",
    "other", "high",
    fx(r"\]" + NL + r"Comme \(S\)", r"\]" + NL + NL + r"Comme \(S\)"),
    "Missing paragraph break.")

add(391, "Théorème 3.2",
    "underlined word groups: 'Soit', 'un schéma quasi-compact', 'Le pré', 'anneau', 'défini à partir des', "
    "'-Modules localement libres de type fini', 'est un', 'anneau'; plain: S, the full stops, '-λ-', K˙(S), "
    "the commas, 'λ-' and '(V 2.4).'; O_S carries its own underline; the label underlines only 'Théorème' "
    "(both scans; w391_mid.png)",
    r"the statement in roman (no \underline, no \emph)",
    "underline", "high", None, STMT_NOTE)

add(391, "letters of sheaves, Modules and torsors on pp. 391-395",
    "underlined in the print: F_i, F_{k-1} (twice), F_k, E of cl(E) and 'où E est', E, F of 'de type fini E, F', "
    "E et F (twice) (p. 391); E, F of D(E), D(F), A of (T,A) and of 'classes de A-Modules' (twice), E et F "
    "(twice), the last E , F (p. 392); every A and P, every E outside λ^i(E), and the F of 'E, F de rangs' and 'pour F' (p. 393); every E, "
    "L_{k-1}, L_1, L_i, L_{i+1}, L_1,...,L_{k-1}, L_i, L_{i-1}, F (p. 394); E, F of the display "
    "D_{π'}(E) ≃ D_{π\"}(F) (top of p. 395, in page_394.tex). Plain in the print: S, T, X, X_k, f, f_k, K, K˙, "
    "n, p, ξ, η, ρ, G, the A of 'des A-Modules' in Théorème 3.3, the E, F that are elements of K˙(S), K˙(X) "
    "or K, and the letters of Lemme 4.3 (A, B, C, ξ, c, σ, α) (both scans)",
    "all plain",
    "underline", "high", None,
    r"Convention of the Exposé VI transcription, reported for pp. 366-390 (findings_381_385.json, "
    r"findings_386_390.json): not itemized. Three examples, in the form to use if the diplomatic layer "
    r"reproduces it: p. 391 'de type fini \(F_i\) en posant' -> 'de type fini \(\underline{F}_i\) en posant'; "
    r"p. 393 'Soit \(E\) un \(A\)-Module' -> 'Soit \(\underline{E}\) un \(\underline{A}\)-Module'; p. 394 "
    r"'le noyau de \(L_i\to L_{i-1}\)' -> 'le noyau de \(\underline{L}_i\to \underline{L}_{i-1}\)'. The "
    r"underlined structure sheaf O stays \mathcal O (pending volume decision). The underlined Gl of Gl(n,A) "
    r"(p. 393) is a separate entry.")

# ---------------------------------------------------------------- p. 392
add(392, "'Soit alors X = D(E) x_S D(F).'",
    "both D doubly underlined, E and F singly underlined (both scans; crops_391_395/w392_top.png)",
    r"\(X=D(E)\times_S D(F)\) (plain D)",
    "font", "high",
    fx(r"\(X=D(E)\times_S D(F)\)", r"\(X=\mathbf D(E)\times_S \mathbf D(F)\)"),
    r"As the D of Proposition 3.1 (p. 390, \mathbf D). The typed x for the product is handled globally.")

add(392, "'qui définissent la structure de λ-anneau de 1 + K˙(S)[[t]]^+.'",
    "the same hand-drawn hat over K˙(S)[[t]], the + at its right end (both scans; crops_391_395/m392_arc.png, "
    "w392_mid.png)",
    r"1+K^{\bullet}(S)[[t]]^+ (no hat)",
    "symbol", "high",
    fx(r"1+K^{\bullet}(S)[[t]]^+", r"1+\widehat{K^{\bullet}(S)[[t]]}^{+}"),
    "As p. 391.")

add(392, "label 'Théorème 3.3'",
    "'Théorème 3.3  Soit': no full stop after 3.3 (both scans; crops_391_395/m392_th33.png, w392_mid.png), "
    "where 3.2, 4.2 and 4.3 have one",
    r"\textbf{Théorème 3.3.} (silently corrected)",
    "misprint_in_print", "high",
    fx(r"\textbf{Théorème 3.3.}", r"\textbf{Théorème 3.3}"),
    "The typist left out the stop: the diplomatic layer should drop it, the corrected edition keeps it.",
    corrected=r"\textbf{Théorème 3.3.}")

add(392, "Théorème 3.3",
    "underlined word groups: 'Soit', 'un topos commutativement annelé', 'on désigne par', 'le groupe de "
    "Grothendieck des', 'Modules localement libres', 'Alors', 'muni de sa pré', 'structure canonique', 'est', "
    "'un', 'anneau'; plain: (T,A) (A with its own underline), ';', K, the 'A-' of 'des A-Modules', 'de rang "
    "borné sur T .', ', K ,', '-λ-', '(V 2.2 b)) ,', 'λ-' and the full stop; the label underlines only "
    "'Théorème' (both scans; w392_mid.png, crops_391_395/m392_desA.png)",
    r"the statement in roman (no \underline, no \emph)",
    "underline", "high", None, STMT_NOTE)

# ---------------------------------------------------------------- p. 393
GL_NOTE = (r"The group scheme Gl(n) is doubly underlined (the file's \mathbf), the sheaf of groups Gl(n,A) singly "
           r"(separate entry). \mathbf{Gl}, because \GL is \operatorname{Gl}, which \mathbf does not embolden.")
add(393, "'un λ-homomorphisme de R_Z(Gl(n)) dans K'",
    "the Gl of Gl(n) doubly underlined (both scans; crops_391_395/w393_top.png)",
    r"\(R_{\mathbb Z}(\GL(n))\) (plain Gl)",
    "font", "high",
    fx(r"\(R_{\mathbb Z}(\GL(n))\) dans \(K\), en", r"\(R_{\mathbb Z}(\mathbf{Gl}(n))\) dans \(K\), en"),
    GL_NOTE)

add(393, "'à toute représentation ρ de Gl(n) dans un Z-module'",
    "the Gl of Gl(n) doubly underlined (both scans; w393_top.png)",
    r"\(\GL(n)\) (plain Gl)",
    "font", "high",
    fx(r"de \(\GL(n)\) dans un", r"de \(\mathbf{Gl}(n)\) dans un"),
    "As the entry above.")

add(393, "'par la représentation standard dans R_Z(Gl(n)).'",
    "the Gl of Gl(n) doubly underlined (both scans; w393_top.png)",
    r"\(R_{\mathbb Z}(\GL(n))\) (plain Gl)",
    "font", "high",
    fx(r"standard dans \(R_{\mathbb Z}(\GL(n))\)", r"standard dans \(R_{\mathbb Z}(\mathbf{Gl}(n))\)"),
    "As the entries above.")

add(393, "'un λ-homomorphisme de R_Z(Gl(n)xGl(p)) dans K'",
    "both Gl doubly underlined (both scans; w393_mid.png)",
    r"\(R_{\mathbb Z}(\GL(n)\times\GL(p))\) (plain Gl)",
    "font", "high",
    fx(r"(\GL(n)\times\GL(p))\) dans", r"(\mathbf{Gl}(n)\times\mathbf{Gl}(p))\) dans"),
    "As the entries above.")

add(393, "'pour les éléments correspondants de R_Z(Gl(n)xGl(p)).'",
    "both Gl doubly underlined (both scans; w393_mid.png)",
    r"\(R_{\mathbb Z}(\GL(n)\times\GL(p))\) (plain Gl)",
    "font", "high",
    fx(r"correspondants de \(R_{\mathbb Z}(\GL(n)\times\GL(p))",
       r"correspondants de \(R_{\mathbb Z}(\mathbf{Gl}(n)\times\mathbf{Gl}(p))"),
    "As the entries above; independent of the paragraph-break entry that follows (its old string begins where "
    "this one ends).")

add(393, "'... correspondants de R_Z(Gl(n)xGl(p)).' / 'On est donc ramené à montrer'",
    "'On est donc ramené' begins a new, indented paragraph (both scans; w393_mid.png)",
    r"one paragraph: '... \(R_{\mathbb Z}(\GL(n)\times\GL(p))\). On est donc ramené ...'",
    "other", "high",
    fx(r"\). On est donc ramené", r"\)." + NL + NL + "On est donc ramené"),
    "Missing paragraph break.")

add(393, "Gl(n,A) and Gl(p,A), 13 places on p. 393",
    "the Gl of every Gl(n,A) and Gl(p,A) is singly underlined (both scans; crops_391_395/w393_top.png, "
    "w393_mid.png): 'torseur P sous Gl(n,A)', the indices of P x_{Gl(n,A)} (twice), 'comme Gl(n,A)-Module', "
    "'comme Gl(n,A)-module', 'sous Gl(n,A)xGl(p,A)', the index x_{Gl(n,A)xGl(p,A)}, "
    "'comme Gl(n,A)xGl(p,A)-Module', 'opérer Gl(n,A)', 'et Gl(p,A)'",
    r"\GL (\providecommand{\GL}{\operatorname{Gl}}, main.tex line 40) prints a plain Gl: \GL(n,A) 9 times, "
    r"\GL(p,A) 4 times",
    "underline", "high", None,
    r"Underlined operator name dropped by the macro, as Proj_o on pp. 381-385: one scripted pass, both layers: "
    r"'\GL(n,A)' -> '\underline{\GL}(n,A)' (9) and '\GL(p,A)' -> '\underline{\GL}(p,A)' (4). main.tex has "
    r"these strings only on folio 393 (diplomatic lines 9888-9891, current 9894-9897). Independent of the five "
    r"\mathbf{Gl} entries (their old strings contain no \GL(n,A), \GL(p,A)). Three examples: "
    r"'sous \(\GL(n,A)\) tel que' -> 'sous \(\underline{\GL}(n,A)\) tel que'; '\(E=P\times_{\GL(n,A)} (A)^n\)' "
    r"-> '\(E=P\times_{\underline{\GL}(n,A)} (A)^n\)'; 'et \(\GL(p,A)\) par' -> 'et \(\underline{\GL}(p,A)\) par'.")

# ---------------------------------------------------------------- p. 394
add(394, "paragraph number 4.1",
    "'4.1.' with a full stop, run into 'Soient S un schéma' (both scans; w394_top.png)",
    r"\subsection*{4.1}",
    "punctuation", "high",
    fx(r"\subsection*{4.1}", r"\subsection*{4.1.}"),
    r"The printed paragraph number ends with a full stop (as the \subsubsection*{2.3} -> {2.3.} fixes of pp. 4-10). "
    "The run-in heading itself is not reported.")

add(394, "'localement libre de rang p_1+...+p_i.'",
    "three typed stops on the baseline, level with the sentence's full stop, between the raised + signs (both "
    "scans; crops_391_395/m394_dots1.png, w394_dots1.png)",
    r"p_1+\cdots+p_i (dots at mid-height)",
    "symbol", "medium",
    fx(r"p_1+\cdots+p_i", r"p_1+\ldots+p_i"),
    r"\cdots sets the dots at mid-height (same kind of fix as pp. 387-390).")

add(394, "'Un tel foncteur est réprésentable'",
    "'Un tel foncteur' begins a new, indented paragraph after 'p_1+...+p_i.' (both scans; w394_mid.png)",
    r"one paragraph: '... \(p_1+\cdots+p_i\). Un tel foncteur ...'",
    "other", "high",
    fx(r"\). Un tel foncteur", r"\)." + NL + NL + "Un tel foncteur"),
    "Missing paragraph break; independent of the dots entry (adjacent strings, no overlap).")

add(394, "'Un tel foncteur est réprésentable par un S-schéma'",
    "'réprésentable', with an acute accent on the first e (both scans; w394_mid.png)",
    "réprésentable (printed reading kept)",
    "misprint_in_print", "high", None,
    "The diplomatic layer is right; the corrected layer already reads 'représentable' (current main.tex line 9911).",
    corrected="représentable")

add(394, "'par un S-schéma D_π(E), qui est muni'",
    "D doubly underlined, E singly (both scans; w394_mid.png)",
    r"\(D_\pi(E)\) (plain D)",
    "font", "high",
    fx(r"\(D_\pi(E)\), qui est muni", r"\(\mathbf D_\pi(E)\), qui est muni"),
    r"Doubly underlined D written plain (\mathbf D on p. 390).")

add(394, "'localement libres de rang p_1,p_1+p_2,...'",
    "three stops after 'p_2,' and nothing after them; the paragraph ends there (both scans; "
    "crops_391_395/m394_dots2.png, w394_dots2.png)",
    r"\(p_1,p_1+p_2,\ldots\). (a full stop added after the dots)",
    "punctuation", "high",
    fx(r"p_1,p_1+p_2,\ldots\).", r"p_1,p_1+p_2,\ldots\)"),
    "The TeX adds a full stop.")

add(394, "'Si π = (r,n-r), alors ...'",
    "'Si π = (r,n-r)' begins a new, indented paragraph after 'D_π(E) = P(E).' (both scans; "
    "crops_391_395/w394_Si.png)",
    r"one paragraph: '... \(D_\pi(E)=\mathbb P(E)\). Si \(\pi=(r,n-r)\) ...'",
    "other", "high",
    fx(r". Si \(\pi=(r,n-r)\)", "." + NL + NL + r"Si \(\pi=(r,n-r)\)"),
    "Missing paragraph break; independent of the two font entries of these lines (adjacent strings, no overlap).")

add(394, "'Si π = (1,n-1), alors D_π(E) = P(E).'",
    "D and P doubly underlined, E singly (both scans; crops_391_395/w394_Si.png)",
    r"\(D_\pi(E)=\mathbb P(E)\) (plain D, double-struck P)",
    "font", "high",
    fx(r"\(D_\pi(E)=\mathbb P(E)\)", r"\(\mathbf D_\pi(E)=\mathbf P(E)\)"),
    "As the D above and the P of p. 391.")

add(394, "'Si π = (r,n-r), alors D_π(E) = G_{r,n}(E)'",
    "D and G doubly underlined, E singly (both scans; w394_Si.png)",
    r"\(D_\pi(E)=G_{r,n}(E)\) (plain D and G)",
    "font", "high",
    fx(r"\(D_\pi(E)=G_{r,n}(E)\)", r"\(\mathbf D_\pi(E)=\mathbf G_{r,n}(E)\)"),
    "As the entry above.")

add(394, "'G_{r,n}(E), grassmanienne de type (r,n-r) de E'",
    "'grassmanienne', one n before '-ienne' (both scans; w394_Si.png)",
    "grassmanienne (printed reading kept)",
    "misprint_in_print", "high", None,
    "The diplomatic layer is right; the corrected layer already reads 'grassmannienne' (current main.tex line "
    "9913).",
    corrected="grassmannienne")

add(394, "'Si tous les p_i sont égaux à 1'",
    "'Si tous les p_i' begins a new, indented paragraph after 'de E.' (both scans; w394_mid.png)",
    r"one paragraph: '... de \(E\). Si tous les \(p_i\) ...'",
    "other", "high",
    fx(r"\). Si tous les", r"\)." + NL + NL + "Si tous les"),
    "Missing paragraph break.")

add(394, "'le fibré en drapeau usuel de E, noté D(E).'",
    "D doubly underlined, E singly (both scans; crops_391_395/w394_DE.png)",
    r"\(D(E)\) (plain D)",
    "font", "high",
    fx(r"noté \(D(E)\)", r"noté \(\mathbf D(E)\)"),
    "As the entries above.")

add(394, "Lemme 4.2, 'avec p_1+...+p_k = n'",
    "three typed stops on the baseline (both scans; crops_391_395/w394_dots3.png)",
    r"p_1+\cdots+p_k (dots at mid-height)",
    "symbol", "medium",
    fx(r"p_1+\cdots+p_k=n", r"p_1+\ldots+p_k=n"),
    "As 'p_1+...+p_i' above.")

add(394, "Lemme 4.2, 'l'image inverse de E sur D_π(E)'",
    "D doubly underlined, E singly (both scans; crops_391_395/w394_surD.png)",
    r"\(D_\pi(E)\) (plain D)",
    "font", "high",
    fx(r"sur \(D_\pi(E)\)", r"sur \(\mathbf D_\pi(E)\)"),
    "As the entries above.")

add(394, "Lemme 4.2",
    "underlined word groups: 'Soient', 'un schéma', 'un', '-Module localement libre de rang', 'avec', 'soient', "
    "'deux entiers', 'tels que', 'posons', 'Soient', 'les quotients canoniques de l'image inver-/se de', 'sur', "
    "'et soit', 'le noyau de', 'Alors on a un', 'isomorphisme canonique'; plain: S, the commas, n, the formulas "
    "π = (...), p_1+...+p_k = n, p', p\", ≥ 1, p'+p\" = p_i, π' = (...), π\" = (p',p\"), the ';', 'S-' and ':' "
    "(E, O_S, L_i, F carry their own underlines, D_π its double one); the label underlines only 'Lemme' (both "
    "scans; w394_mid.png, w394_bot.png)",
    r"the statement in roman (no \underline, no \emph)",
    "underline", "high", None, STMT_NOTE)

add(394, "display of Lemme 4.2, D_{π'}(E) ≃ D_{π\"}(F) (printed at the top of p. 395; it stands in page_394.tex, "
         "above the folio-395 marker)",
    "both D doubly underlined, E and F singly; ≃ with a straight lower bar (both scans; crops_391_395/w395_top.png)",
    r"D_{\pi'}(E)\simeq D_{\pi''}(F) (plain D)",
    "font", "high",
    fx(r"D_{\pi'}(E)\simeq D_{\pi''}(F)", r"\mathbf D_{\pi'}(E)\simeq \mathbf D_{\pi''}(F)"),
    "Printed on p. 395 (see the marker entry of p. 395). The old string occurs once in main.tex; after the marker "
    "move it stands under the folio-395 marker. If the marker is moved with the exact main.tex edit given there, "
    "make the move first (move_marker.py works in either order).")

# ---------------------------------------------------------------- p. 395
add(395, "start of page (folio-395 marker)",
    "p. 394 ends 'Alors on a un S-isomorphisme canonique :' and blank space; p. 395 begins with the display "
    "'D_{π'}(E) ≃ D_{π\"}(F) .', then 'La démonstration, immédiate ...' (both scans; crops_391_395/w394_bot.png, "
    "w395_top.png)",
    r"the display '\[ D_{\pi'}(E)\simeq D_{\pi''}(F). \]' ends page_394.tex, above the folio-395 marker; "
    r"page_395.tex begins 'La'",
    "marker", "high", None,
    r"Page 395 really begins at the display's '\['. Move the marker up three lines: python -I move_marker.py 6 395 "
    r"'\[' --before (the last '\[' before the marker is this display's). Exact edit in main.tex, both layers "
    r"(diplomatic lines 9909-9913, current 9915-9919): replace 'canonique~:\n\[\n  D_{\pi'}(E)\simeq "
    r"D_{\pi''}(F).\n\]\n%%%%%%%%%%  scan idx 408  |  folio 395  %%%%%%%%%%\n' by 'canonique~:\n%%%%%%%%%%  scan "
    r"idx 408  |  folio 395  %%%%%%%%%%\n\[\n  D_{\pi'}(E)\simeq D_{\pi''}(F).\n\]\n' (simulated in memory in "
    r"both layers, one match each: crops_391_395/sim_markers.py). Before the \mathbf D fix of the same display "
    r"(page_394 entry), or with \mathbf D written in both strings.")

add(395, "'La démonstration, immédiate sur la définition fonctorielle'",
    "'La démonstration' begins a new, indented paragraph after the display (both scans; w395_top.png)",
    r"'La' follows the display's '\]' and the marker line without a blank line (the paragraph runs on)",
    "other", "high",
    fx("La" + NL + "démonstration", NL + "La" + NL + "démonstration"),
    "Missing paragraph break. The blank line goes after the marker line, so the edit also works once the marker "
    "stands above the display.")

add(395, "Lemme 4.3 (pp. 395-396)",
    "underlined word groups on p. 395: 'Soient', 'un anneau commutatif avec unité', 'un entier', 'une famille "
    "d'éléments de', 'soit', 'la', 'algèbre engendrée par / des générateurs', 'soumis aux relations', 'où les', "
    "'désignent les fonctions symétriques élémentaires', 'Soient', 'des entiers', 'de somme', 'et pour', 'avec', "
    "'Posons', 'et soit', 'la sous-algèbre de', 'engendrée par les', 'Alors', 'les éléments de la forme', 'où', "
    "'forment une base de', 'considéré comme', 'module', 'les générateurs', 'de la', 'algèbre', 'satisfont aux', "
    "'relations / isobares déduites de la relation'; plain: the letters A, n, C, B, ξ_i, σ_i, p_j, c_i^{(j)}, "
    "the 'A-' and 'B-' before algèbre, module, the formulas, the commas, ';', ':' and '::', the labels i), ii); "
    "the label underlines only 'Lemme' (both scans; w395_top.png, w395_mid.png, w395_bot.png)",
    r"the statement in roman (no \underline, no \emph)",
    "underline", "high", None, STMT_NOTE)

add(395, "Lemme 4.3 i), display (ξ^{(1)})^{α(1)} ... (ξ^{(k)})^{α(k)}",
    "three typed stops on the baseline (both scans; crops_391_395/m395_xiprod.png, w395_xiprod.png)",
    r"\cdots (dots at mid-height)",
    "symbol", "medium",
    fx(r"^{\alpha(1)}\cdots", r"^{\alpha(1)}\ldots"),
    "As the dots of p. 394; independent of the punctuation entry of the same display (no common text).")

add(395, "same display, its end",
    "a comma after (ξ^{(k)})^{α(k)}, head and tail, in the witness (crops_391_395/w395_xiprod.png); the main scan "
    "shows only a heavy dot, the tail lost (m395_xiprod.png); the sentence goes on 'où α(j) = ...'",
    r"(\xi^{(k)})^{\alpha(k)}. (full stop)",
    "punctuation", "medium",
    fx(r"(\xi^{(k)})^{\alpha(k)}.", r"(\xi^{(k)})^{\alpha(k)},"),
    "Read from the witness, which keeps the thin tail.")

add(395, "Lemme 4.3 ii), 'isobares déduites de la relation ::'",
    "two colons '::' (both scans; w395_bot.png)",
    r"relation~:: (printed reading kept)",
    "misprint_in_print", "high", None,
    "The typist's doubled colon. The diplomatic layer is right; the corrected layer also still has '::' (current "
    "main.tex line 9949).",
    corrected=r"relation~:")

add(395, "Lemme 4.3 ii), display Σ_{i=1}^n c_i = Π_{j=1}^k (Σ_{i=1}^{p_j} c_i^{(j)})",
    "nothing after the closing parenthesis; p. 396 goes on '(c_i et c_i^{(j)} étant effectués du poids i)' (both "
    "scans; w395_bot.png; b396_400/page_396_s1.png)",
    r"\right), (a comma at the end of the display)",
    "punctuation", "high",
    fx(r"c_i^{(j)}\right),", r"c_i^{(j)}\right)"),
    "The TeX adds a comma at the end of a display.")

out = RUN / "findings_391_395.json"
out.write_text(json.dumps(F, ensure_ascii=False, indent=1) + NL, encoding="utf-8", newline=NL)
print("wrote", out, len(F), "entries")
