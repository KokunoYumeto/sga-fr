"""Write findings_126_130.json (SGA 6, pp. 126-130). TeX strings are raw; the sign ¶ stands for a line break.
usage: python -I make_findings.py"""
import json
import pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "findings_126_130.json"
NL = "¶"


def t(s):
    return s.replace(NL, "\n") if s is not None else None


def F(page, where, scan, tex, kind, conf, old, new, note, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, confidence=conf,
             fix=(dict(old=t(old), new=t(new)) if old is not None else None))
    if kind == "misprint_in_print":
        d["corrected"] = t(corrected)
    d["note"] = note
    return d


items = [
    # ---------------------------------------------------------------- p. 126
    F(126, "Remarque 4.12.2, 'Supposons C_o stable par noyau d'épimorphisme et quasi-relevable dans C'",
      "'quasi-relevable' underlined (both scans)", "plain 'quasi-relevable'", "underline", "high",
      r"et quasi-relevable dans", r"et \emph{quasi-relevable} dans",
      "The file writes underlined words of the running text with \\emph (as 'localement quasi-relevable' in 1.2)."),
    F(126, "Remarque 4.12.2, 'il n'y a pas d'espoir que le foncteur K^b(C_o) ⟶ D(C) soit fidèle'",
      "the map is set inline in the sentence (both scans)", "a display \\[ ... \\]", "other", "medium",
      r"\[¶  \Kpx^b(\mathcal C_0)\longrightarrow \Dpx(\mathcal C)¶\]¶",
      r"\(\Kpx^b(\mathcal C_0)\longrightarrow \Dpx(\mathcal C)\)¶",
      "The print sets the formula inline; the TeX makes it a display (same kind of fix as pp. 21, 122, 133). "
      "Apply before the next entry, whose old lies inside this one (JSON order)."),
    F(126, "same formula, 'K^b(C_o)'",
      "plain typed C with the index o, without the underline of the category letter; D(C̲) beside it and every "
      "other C_o of the page are underlined (both scans; crops_126_130/p126_inlineC0.png, w137_top.png)",
      "\\Kpx^b(\\mathcal C_0) (silently supplied)", "misprint_in_print", "medium",
      r"\Kpx^b(\mathcal C_0)\longrightarrow", r"\Kpx^b(C_0)\longrightarrow",
      "The typist left out the underline here (as on pp. 89 and 93); the TeX silently writes \\mathcal C. "
      "Listed after the display entry, whose old contains this text.",
      corrected=r"\Kpx^b(\mathcal C_0)\longrightarrow"),
    F(126, "Remarque 4.12.2, 'si K^{b,∅}(C_o) désigne la sous-catégorie épaisse de K^b(C_o) formée des objets "
           "acycliques'",
      "the second index is the hand-drawn empty-set sign, a small loop crossed by a long slash (both scans; "
      "crops_126_130/p126_phi.png)", "\\Kpx^{b,\\mathrm{ac}}", "symbol", "high",
      r"\Kpx^{b,\mathrm{ac}}(\mathcal C_0)\) désigne", r"\Kpx^{b,\varnothing}(\mathcal C_0)\) désigne",
      "The TeX invents an index 'ac'. main.tex writes the same printed sign \\varnothing in 2.7 b) "
      "(K^{-,∅}(C_o), fixed from p. 100) and in Exposé II (K^{b,∅}(C_1S), line 3856)."),
    F(126, "first display 'K^b(C_o)/K^{b,∅}(C_o) ⟶ D(C)'", "the same sign (both scans)",
      "\\Kpx^{b,\\mathrm{ac}}", "symbol", "high",
      r"\Kpx^{b,\mathrm{ac}}(\mathcal C_0)¶  \longrightarrow \Dpx(\mathcal C)",
      r"\Kpx^{b,\varnothing}(\mathcal C_0)¶  \longrightarrow \Dpx(\mathcal C)",
      "As the previous entry."),
    F(126, "Indications, display 'K^-(C_o)/K^{-,∅}(C_o) ⟶ D^-(C)'", "the same sign (both scans)",
      "\\Kpx^{-,\\mathrm{ac}}", "symbol", "high",
      r"\Kpx^{-,\mathrm{ac}}(\mathcal C_0)¶  \longrightarrow \Dpx^-",
      r"\Kpx^{-,\varnothing}(\mathcal C_0)¶  \longrightarrow \Dpx^-",
      "As above; this is the functor of 2.7 b), written \\Kpx^{-,\\varnothing} there."),
    F(126, "Indications, last display, source 'K^b(C_o)K^{b,∅}(C_o)'", "the same sign (both scans)",
      "\\Kpx^{b,\\mathrm{ac}}", "symbol", "high",
      r"\Kpx^{b,\mathrm{ac}}(\mathcal C_0)¶  \longrightarrow¶",
      r"\Kpx^{b,\varnothing}(\mathcal C_0)¶  \longrightarrow¶",
      "As above."),
    F(126, "Indications, last display, target 'K^-(C_o)/K^{-,∅}(C_o)'", "the same sign (both scans)",
      "\\Kpx^{-,\\mathrm{ac}}", "symbol", "high",
      r"\Kpx^{-,\mathrm{ac}}(\mathcal C_0)¶\]", r"\Kpx^{-,\varnothing}(\mathcal C_0)¶\]",
      "As above."),
    F(126, "Indications, last display 'K^b(C_o)K^{b,∅}(C_o) ⟶ K^-(C_o)/K^{-,∅}(C_o)'",
      "no quotient bar between K^b(C_o) and K^{b,∅}(C_o); the target has its '/' (both scans; "
      "crops_126_130/p126_noslash.png, w137_bot.png)",
      "\\Kpx^b(\\mathcal C_0)/\\Kpx^{b,\\mathrm{ac}}(\\mathcal C_0) (bar silently supplied)",
      "misprint_in_print", "high",
      r"que le foncteur¶\[¶  \Kpx^b(\mathcal C_0)/", r"que le foncteur¶\[¶  \Kpx^b(\mathcal C_0)",
      "The quotient K^b(C_o)/K^{b,∅}(C_o) of the first display; the typist left out the bar and the TeX silently "
      "supplies it. The old ends at the bar, clear of the \\varnothing entry of the same display.",
      corrected=r"\Kpx^b(\mathcal C_0)/\Kpx^{b,\varnothing}(\mathcal C_0)"),
    # ---------------------------------------------------------------- p. 127
    F(127, "start of page",
      "p. 127 begins 'F'^i = F^i pour i < b, F'^b = Z^b(F), F'^i = 0 pour i > b.'; p. 126 ends '... Alors F est "
      "isomorphe à son tronqué F' défini par' (both scans)",
      "'\\(F'^i=F^i\\)' ends the last line of page_126.tex (under the folio-126 marker); page_127.tex begins "
      "'pour \\(i<b\\)'", "marker", "high", None, None,
      "Page 127 really begins with '\\(F'^i=F^i\\)'. python -I move_marker.py 6 127 \"\\(F'^i=F^i\\)\" --before "
      "(double quotes because of the prime; the last occurrence before the marker is this one; simulated on both "
      "layers with crops_126_130/sim_markers.py: '... à son tronqué \\(F'\\) défini par ', the marker, "
      "'\\(F'^i=F^i\\)', 'pour \\(i<b\\), \\(F'^b=Z^b(F)\\), ...')."),
    F(127, "Corollaire 4.14, 'Soient F ∈ ob C_S et n ∈ N. Conditions équivalentes :'",
      "underlined: 'Soient', 'et', 'Conditions équivalentes'; in (i) also 'parf.amp' (both scans)",
      "no emphasis", "underline", "high",
      r"Soient \(F\in\Ob\mathcal C_S\) et \(n\in\mathbb N\). Conditions équivalentes :",
      r"\emph{Soient \(F\in\Ob\mathcal C_S\) et \(n\in\mathbb N\). Conditions équivalentes} :",
      "Statement of a corollary in roman (Lemme 4.13 and Proposition 4.15 around it are in \\emph). (i) is a "
      "formula; no change there. The colon stays in roman."),
    F(127, "Corollaire 4.14 (ii), 'F admet localement une résolution gauche ... tels qu'il existe une suite exacte'",
      "underlined by word groups: 'admet localement une résolution gauche de longueur', 'par des objets', 'de', "
      "'i.e.', 'l'ensemble des', 'au-dessus de', 'tels qu'il existe une suite exacte' (both scans)",
      "no emphasis", "underline", "high",
      r"\(F\) admet localement une résolution gauche de longueur \(n\) par des objets de \(\mathcal C_0\), i.e. "
      r"l'ensemble des \(X\) au-dessus de \(S\) tels qu'il existe une suite exacte",
      r"\(F\) \emph{admet localement une résolution gauche de longueur \(n\) par des objets de \(\mathcal C_0\), "
      r"i.e. l'ensemble des \(X\) au-dessus de \(S\) tels qu'il existe une suite exacte}",
      "Part of the statement of 4.14 (entry above)."),
    F(127, "Corollaire 4.14 (ii), display '0 → L^{-n} → L^{-n+1} → ... → L^o → F_X → 0 ,'",
      "three typed full stops on the baseline (both scans; crops_126_130/p127_dots.png)", "\\cdots",
      "symbol", "medium",
      r"L^{-n+1}\longrightarrow \cdots", r"L^{-n+1}\longrightarrow \ldots",
      "\\cdots sets the dots at mid-height (same kind of fix as pp. 49, 79, 80, 86, 95)."),
    F(127, "Corollaire 4.14 (ii), 'avec L^i ∈ ob C_oX'",
      "C̲ with the indices o and X side by side, no comma (both scans; crops_126_130/p127_C0X.png)",
      "\\mathcal C_{0,X}", "punctuation", "high",
      r"\mathcal C_{0,X}", r"\mathcal C_{0X}",
      "As pp. 91-92, 95, 100 and 124: the TeX adds the comma between the indices."),
    F(127, "Corollaire 4.14 (ii), after the display: 'avec'",
      "'avec', 'pour tout', 'est un raffinement de' underlined; L^i ∈ ob C_oX, i and S are not (both scans)",
      "no emphasis", "underline", "high",
      r"avec \(L^i", r"\emph{avec} \(L^i",
      "End of the statement, by word groups so that the edits stay clear of the C_{0X} entry. See the next "
      "entry."),
    F(127, "Corollaire 4.14 (ii), 'pour tout i, est un raffinement de S.'",
      "'pour tout' and 'est un raffinement de' underlined (both scans)", "no emphasis", "underline", "high",
      r"pour tout \(i\), est un raffinement de \(S\).",
      r"\emph{pour tout} \(i\), \emph{est un raffinement de} \(S\).",
      "End of the statement (entry above)."),
    F(127, "Définition 4.14.1, 'Nous appellerons dimension parfaite de F le plus petit entier n'",
      "'Nous appellerons' and 'de' underlined, the defined term 'dimension parfaite' not (both scans; "
      "crops_126_130/p127_dimparf.png, w138_bot.png)",
      "inside the \\emph of the whole definition", "underline", "high",
      r"Nous appellerons dimension parfaite de", r"Nous appellerons} dimension parfaite \emph{de",
      "As Définitions 1.4.3, 2.1, 2.3 and 5.2 (pp. 93, 95, 98, 132): the defined term is left out of the "
      "underline. Close the emphasis before the term and reopen it after."),
    F(127, "pp. 127-130: the site S̲ ('Quand S̲ est le site ponctuel', p. 128 'X ∈ ob S̲', p. 129 'f : S̲' ⟶ S̲')",
      "S underlined where it names the site (both scans)", "plain \\(S\\)", "underline", "high", None, None,
      "Convention of the transcription, as reported for pp. 84-85, 93-95, 100 and 131: one decision for the "
      "exposé, not a page fix."),
    # ---------------------------------------------------------------- p. 128
    F(128, "Proposition 4.17, 'Soient F', F'' ∈ ob D(C_S), et a, b ∈ Z, avec a ≤ b. Considérons les conditions :'",
      "underlined: 'Soient', 'et', 'avec', 'Considérons les conditions' (both scans); (i) and (ii) are not",
      "no emphasis", "underline", "high",
      r"Soient \(F',F''\in\Ob\Dpx(\mathcal C_S)\), et \(a,b\in\mathbb Z\), avec \(a\leq b\). Considérons les "
      r"conditions :",
      r"\emph{Soient \(F',F''\in\Ob\Dpx(\mathcal C_S)\), et \(a,b\in\mathbb Z\), avec \(a\leq b\). Considérons "
      r"les conditions} :",
      "Statement of a proposition in roman (Lemme 4.16 on the same page is in \\emph). The colon stays in roman."),
    F(128, "Proposition 4.17, 'On a (i) ⇒ (ii), et, si C_o est localement stable par facteurs directs (i.e. ...), "
           "alors on a (i) ⟺ (ii).'",
      "underlined by word groups: 'On a', 'et,', 'si', 'est localement stable par facteurs directs', "
      "'la relation', 'pour', 'implique', 'que localement', 'et', 'sont objets de', 'alors on a' (both scans)",
      "no emphasis", "underline", "high",
      r"On a (i) \(\Rightarrow\) (ii), et, si \(\mathcal C_0\) est localement stable par facteurs directs (i.e. "
      r"la relation \(E'+E''\in\Ob\mathcal C_0\), pour \(E',E''\in\Ob\mathcal C_X\) et \(X\in\Ob S\), implique "
      r"que localement \(E'\) et \(E''\) sont objets de \(\mathcal C_0\)), alors on a (i) \(\Leftrightarrow\) "
      r"(ii).",
      r"\emph{On a (i) \(\Rightarrow\) (ii), et, si \(\mathcal C_0\) est localement stable par facteurs directs "
      r"(i.e. la relation \(E'+E''\in\Ob\mathcal C_0\), pour \(E',E''\in\Ob\mathcal C_X\) et \(X\in\Ob S\), "
      r"implique que localement \(E'\) et \(E''\) sont objets de \(\mathcal C_0\)), alors on a (i) "
      r"\(\Leftrightarrow\) (ii)}.",
      "Second part of the statement (entry above)."),
    # ---------------------------------------------------------------- p. 129
    F(129, "start of page",
      "p. 129 begins 'F'^i = F''^i = 0 pour i < a. Comme on a ...'; p. 128 ends '... pour i > b, puis, en "
      "tronquant, que' (both scans)",
      "'\\(F'^i=F''^i=0\\)' ends the last line of page_128.tex (under the folio-128 marker); page_129.tex begins "
      "'pour \\(i<a\\).'", "marker", "high", None, None,
      "Page 129 really begins with '\\(F'^i=F''^i=0\\)'. python -I move_marker.py 6 129 \"\\(F'^i=F''^i=0\\)\" "
      "--before (the last occurrence before the marker is the one after 'en tronquant, que'; simulated on both "
      "layers with crops_126_130/sim_markers.py: '... puis, en tronquant, que ', the marker, "
      "'\\(F'^i=F''^i=0\\)', 'pour \\(i<a\\). Comme on a ...')."),
    F(129, "line 1, 'Comme on a parf.dim(F) ⊂ [a,b], on déduit de (4.16)'",
      "parf.dim(F) ⊂ [a,b] (both scans; crops_126_130/p129_parfdim.png, w140_top.png)",
      "\\perfdim(F)\\subset[a,b] (keeps the printed reading)", "misprint_in_print", "high", None, None,
      "A dimension is a number, not contained in an interval; (4.16) needs parf.amp(F) ⊂ [a,b], which is "
      "condition (ii) of 4.17. The corrected layer already has \\perfamp(F).",
      corrected=r"\perfamp(F)\subset[a,b]"),
    F(129, "line 3, 'sont localement objets de C_o puisque C_o est localement stable'",
      "no comma before 'puisque' (both scans; crops_126_130/p129_puisque.png)",
      "objets de \\(\\mathcal C_0\\), puisque", "punctuation", "high",
      r"objets de \(\mathcal C_0\), puisque", r"objets de \(\mathcal C_0\) puisque",
      "The TeX adds the comma."),
    F(129, "Proposition 4.18, statement up to 'et soit'",
      "underlined: 'Soit', 'un trio satisfaisant aux mêmes hypothèses', 'que', 'Soit', 'un morphisme de sites', "
      "'(défini par', 'et soit' (both scans)", "no emphasis", "underline", "high",
      r"Soit \((S',\mathcal C',\mathcal C'_0)\) un trio satisfaisant aux mêmes hypothèses (4.0) que "
      r"\((S,\mathcal C,\mathcal C_0)\). Soit \(f:S'\to S\) un morphisme de sites (défini par \(f^{-1}:S\to "
      r"S'\)), et soit",
      r"\emph{Soit \((S',\mathcal C',\mathcal C'_0)\) un trio satisfaisant aux mêmes hypothèses (4.0) que "
      r"\((S,\mathcal C,\mathcal C_0)\). Soit \(f:S'\to S\) un morphisme de sites (défini par \(f^{-1}:S\to "
      r"S'\)), et soit}",
      "Statement of a proposition in roman. Two groups (this one and the 'un foncteur ... définit un foncteur' "
      "entry below), so that the edits stay clear of the two display entries."),
    F(129, "Proposition 4.18, 'et soit u : D^*(C) ⟶ D^*(C') (* = -, +, ∅) un foncteur'",
      "inline in the sentence (both scans)", "a display \\[ ... \\]", "other", "medium",
      r"\[¶  u:\Dpx^*(\mathcal C)\longrightarrow \Dpx^*(\mathcal C')\qquad (*=-,+,b)¶\]¶",
      r"\(u:\Dpx^*(\mathcal C)\longrightarrow \Dpx^*(\mathcal C')\qquad (*=-,+,b)\)¶",
      "The print sets the formula inline. Apply before the next entry, whose old lies inside this one "
      "(JSON order)."),
    F(129, "Proposition 4.18, '(* = -, +, ∅)'",
      "the third value is the hand-drawn empty-set sign (loop crossed by a slash), not a typed b (both scans; "
      "crops_126_130/p129_star.png, w140_top.png)", "(*=-,+,b)", "symbol", "high",
      r"(*=-,+,b)", r"(*=-,+,\varnothing)",
      "The same sign as K^{b,∅} on p. 126: D^∅ is D with no condition on degrees, beside D^-, D^+. Proposition "
      "2.13 on p. 106 prints the same '(* = +,-,∅)', where the TeX also has b (main.tex, display after "
      "'Proposition 2.13'). After the display entry above (JSON order)."),
    F(129, "Proposition 4.18, from 'un foncteur au-dessus de f' to 'définit un foncteur'",
      "underlined: 'un foncteur', 'au-dessus de', 'Si', 'transforme les objets de', 'en complexes', '-parfaits', "
      "'alors', 'définit un foncteur'; '(cf. (2.13))' is not (both scans)", "no emphasis", "underline", "high",
      r"un foncteur au-dessus de \(f\) (cf. (2.13)). Si \(u\) transforme les objets de \(\mathcal C_0\) en "
      r"complexes \(\mathcal C'_0\)-parfaits, alors \(u\) définit un foncteur",
      r"\emph{un foncteur au-dessus de} \(f\) (cf. (2.13)). \emph{Si \(u\) transforme les objets de "
      r"\(\mathcal C_0\) en complexes \(\mathcal C'_0\)-parfaits, alors \(u\) définit un foncteur}",
      "Second group of the statement; the reference stays in roman."),
    F(129, "Proposition 4.18, end: 'alors u définit un foncteur D*(C)_{C_o-parf} ⟶ D*(C')_{C'_o-parf} .'",
      "inline at the end of the sentence (both scans)", "a display \\[ ... \\]", "other", "medium",
      r"\[¶  \Dpx^*(\mathcal C)_{\mathcal C_0\text{-}\mathrm{parf}}¶  \longrightarrow¶  "
      r"\Dpx^*(\mathcal C')_{\mathcal C'_0\text{-}\mathrm{parf}}.¶\]",
      r"\(\Dpx^*(\mathcal C)_{\mathcal C_0\text{-}\mathrm{parf}}\longrightarrow"
      r"\Dpx^*(\mathcal C')_{\mathcal C'_0\text{-}\mathrm{parf}}\).",
      "The print sets the formula inline."),
    F(129, "Preuve of 4.18, 'est une sous-catégorie triangulée de D*(C) (4.10)'",
      "D*(C̲) without the prime (both scans; crops_126_130/p129_D410.png, w140_top.png)",
      "\\Dpx^*(\\mathcal C) (keeps the printed reading)", "misprint_in_print", "high", None, None,
      "D*(C')_{C'_o-parf} is a subcategory of D*(C'), not of D*(C). The corrected layer already has "
      "\\Dpx^*(\\mathcal C').",
      corrected=r"\Dpx^*(\mathcal C')"),
    F(129, "Corollaire 4.19, statement up to 'alors'",
      "underlined: 'Sous les hypothèses de', 'si', 'est', 'parfait en tant qu'objet de', 'et', 'est parfait,', "
      "'alors'; '(2.16),' is not (both scans)", "no emphasis", "underline", "high",
      r"Sous les hypothèses de (2.16), si \(E'\in\Ob\Dpx^-({}_A, S'_A)\) est parfait en tant qu'objet de "
      r"\(\Dpx^-({}_A, S')\) et \(E\in\Ob\Dpx^-({}_A S)\) est parfait, alors",
      r"\emph{Sous les hypothèses de} (2.16), \emph{si \(E'\in\Ob\Dpx^-({}_A, S'_A)\) est parfait en tant "
      r"qu'objet de \(\Dpx^-({}_A, S')\) et \(E\in\Ob\Dpx^-({}_A S)\) est parfait, alors}",
      "Statement of a corollary in roman. Apply before the two {}_{A'} entries of the statement, whose olds lie "
      "inside this one (JSON order)."),
    F(129, "Corollaire 4.19, 'alors E' ⊗^L_A E est parfait.'",
      "inline: the formula opens the third line of the statement and 'est parfait.' follows it on the same "
      "line (both scans)", "a display \\[ ... \\]", "other", "medium",
      r"\[¶  E'\overset{\mathrm L}{\otimes}_A E¶\]¶", r"\(E'\overset{\mathrm L}{\otimes}_A E\) ",
      "The print sets the formula inline."),
    F(129, "Corollaire 4.19, last words 'est parfait.'", "'est parfait' underlined (both scans)",
      "no emphasis", "underline", "high",
      r"est parfait.¶", r"\emph{est parfait}.¶",
      "End of the statement of 4.19."),
    F(129, "Corollaire 4.19, 'si E' ∈ ob D⁻(_{A'}S'_A)'",
      "the left index is A' (the prime sits at the top of the lowered A, the shape of the prime of S'), as in "
      "2.16 on p. 110, where the TeX reads D(_{A'}S'_A) (both scans; crops_126_130/p129_cor419a.png)",
      "\\Dpx^-({}_A, S'_A)", "symbol", "high",
      r"({}_A, S'_A)\) est", r"({}_{A'} S'_A)\) est",
      "E' is a complex of A'-A-biModules (Corollaire 2.16); the TeX reads the prime of A' as a comma, here and "
      "in the entries below (pp. 129-130), as on p. 133 (findings_131_135.json). After the underline entry of "
      "the statement (JSON order)."),
    F(129, "Corollaire 4.19, 'parfait en tant qu'objet de D⁻(_{A'}S')'",
      "left index A' (both scans; crops_126_130/p129_cor419b.png)", "\\Dpx^-({}_A, S')", "symbol", "high",
      r"({}_A, S')\) et", r"({}_{A'} S')\) et",
      "As the previous entry."),
    F(129, "Preuve of 4.19, 'On peut supposer que E' ∈ ob D⁻(_{A'}S'_A)'",
      "left index A' (both scans; crops_126_130/p129_preuveA.png)", "\\Dpx^-({}_A, S'_A)", "symbol", "high",
      r"({}_A, S'_A)\) (", r"({}_{A'} S'_A)\) (",
      "As above."),
    F(129, "Preuve of 4.19, 'et l'on applique (4.18) à u = E' ⊗^L_A : D⁻(_AS) ⟶ D⁻(_{A'}S').'",
      "inline at the end of the sentence (both scans)", "a display \\[ ... \\]", "other", "medium",
      r"\[¶  u=E'\overset{\mathrm L}{\otimes}_A:¶  \Dpx^-({}_A S)\longrightarrow \Dpx^-({}_A, S').¶\]¶",
      r"\(u=E'\overset{\mathrm L}{\otimes}_A:\Dpx^-({}_A S)\longrightarrow \Dpx^-({}_A, S')\).¶",
      "The print sets the formula inline. Apply before the next entry, whose old lies inside this one "
      "(JSON order)."),
    F(129, "Preuve of 4.19, target 'D⁻(_{A'}S')'",
      "left index A' (both scans; crops_126_130/p129_preuveB.png)", "\\Dpx^-({}_A, S')", "symbol", "high",
      r"\longrightarrow \Dpx^-({}_A, S')", r"\longrightarrow \Dpx^-({}_{A'} S')",
      "As above; after the display entry (JSON order)."),
    # ---------------------------------------------------------------- p. 130
    F(130, "Corollaire 4.19.1 a), 'Le foncteur'",
      "the statement is underlined by word groups: 'Le foncteur', 'induit un foncteur' (a); 'Si', "
      "'est commutatif,', 'le foncteur', 'induit un foncteur' (b); the formulas are not (both scans)",
      "no emphasis", "underline", "high",
      r"Le foncteur¶", r"\emph{Le foncteur}¶",
      "Same form as Corollaire 5.6.1 on p. 133. The old leaves out the item label, so that it holds whatever "
      "the decision on \\textbf{a)}."),
    F(130, "Corollaire 4.19.1 a), 'Le foncteur 𝕃f* : D⁻(_AS) ⟶ D⁻(_{A'}S') induit un foncteur'",
      "inline in the sentence (both scans)", "a display \\[ ... \\]", "other", "medium",
      r"\[¶  \mathrm L f^*:\Dpx^-({}_A S)\longrightarrow \Dpx^-({}_A, S')¶\]¶",
      r"\(\mathrm L f^*:\Dpx^-({}_A S)\longrightarrow \Dpx^-({}_A, S')\)¶",
      "The print sets the formula inline (as 5.6.1 a) on p. 133). Apply before the 𝕃 and A' entries of this "
      "formula, whose olds lie inside this one (JSON order)."),
    F(130, "Corollaire 4.19.1 a), first formula, '𝕃f*'",
      "double-struck L: a typed L with a second stem (both scans; crops_126_130/p130_Lf1_big.png, "
      "w130_Lf1.png)", "\\mathrm L", "font", "high",
      r"\mathrm L f^*:\Dpx^-({}_A S)\longrightarrow", r"\mathbb L f^*:\Dpx^-({}_A S)\longrightarrow",
      "The derived functor is double-struck in all three places of the page (as 𝕃f* on p. 133 and ℝ on "
      "pp. 83, 134); the L over ⊗ is a plain typed L. After the display entry (JSON order)."),
    F(130, "Corollaire 4.19.1 a), first formula, target 'D⁻(_{A'}S')'",
      "left index A' (both scans; crops_126_130/p130_Lf1.png)", "\\Dpx^-({}_A, S')", "symbol", "high",
      r"\longrightarrow \Dpx^-({}_A, S')", r"\longrightarrow \Dpx^-({}_{A'} S')",
      "As on p. 129. After the display entry (JSON order)."),
    F(130, "Corollaire 4.19.1 a), 'induit un foncteur'", "underlined (both scans)", "no emphasis",
      "underline", "high",
      r"induit un foncteur¶\[¶  \mathrm L", r"\emph{induit un foncteur}¶\[¶  \mathrm L",
      "Part of the statement (first entry of the page). Before the 𝕃 entry of the second display (JSON order)."),
    F(130, "Corollaire 4.19.1 a), display '𝕃f* : D⁻(_AS)_parf ⟶ D⁻(_{A'}S')_parf .'",
      "double-struck L (both scans; crops_126_130/p130_Lf_big.png, w130_Lf2.png)", "\\mathrm L", "font",
      "high",
      r"\mathrm L f^*:\Dpx^-({}_A S)_{\mathrm{parf}}", r"\mathbb L f^*:\Dpx^-({}_A S)_{\mathrm{parf}}",
      "As above."),
    F(130, "Corollaire 4.19.1 a), display, target 'D⁻(_{A'}S')_parf'",
      "left index A' (both scans; crops_126_130/p130_Lf2.png)", "\\Dpx^-({}_A, S')", "symbol", "high",
      r"\Dpx^-({}_A, S')_{\mathrm{parf}}", r"\Dpx^-({}_{A'} S')_{\mathrm{parf}}",
      "As on p. 129."),
    F(130, "Corollaire 4.19.1 b), 'Si A est commutatif, le foncteur'",
      "underlined: 'Si', 'est commutatif,', 'le foncteur' (both scans)", "no emphasis", "underline", "high",
      r"Si \(A\) est commutatif, le foncteur", r"\emph{Si \(A\) est commutatif, le foncteur}",
      "Part of the statement (as 5.6.1 b) on p. 133)."),
    F(130, "Corollaire 4.19.1 b), 'le foncteur ⊗^L_A : D⁻(S) x_S D⁻(S) ⟶ D⁻(S) induit un foncteur'",
      "inline in the sentence (both scans)", "a display \\[ ... \\]", "other", "medium",
      r"\[¶  \overset{\mathrm L}{\otimes}_A:¶  \Dpx^-(S)\times_S\Dpx^-(S)¶  \longrightarrow \Dpx^-(S)¶\]¶",
      r"\(\overset{\mathrm L}{\otimes}_A:\Dpx^-(S)\times_S\Dpx^-(S)\longrightarrow \Dpx^-(S)\)¶",
      "The print sets the formula inline."),
    F(130, "Corollaire 4.19.1 b), 'induit un foncteur'", "underlined (both scans)", "no emphasis", "underline",
      "high",
      r"induit un foncteur¶\[¶  \overset", r"\emph{induit un foncteur}¶\[¶  \overset",
      "Part of the statement."),
    F(130, "Remarque 4.19.2, 'parf.amp(𝕃f*(E)) ⊂ [a,b]'",
      "double-struck L (both scans; crops_126_130/p130_Lf3.png)", "\\mathrm L", "font", "high",
      r"\perfamp(\mathrm L f^*(E))", r"\perfamp(\mathbb L f^*(E))",
      "As in 4.19.1 a)."),
]

OUT.write_text(json.dumps(items, ensure_ascii=False, indent=1), encoding="utf-8")
print(OUT, len(items))
