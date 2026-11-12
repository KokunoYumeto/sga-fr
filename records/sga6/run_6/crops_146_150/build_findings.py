"""Build findings_146_150.json, check every fix (old occurs once in its page file, olds disjoint, braces balanced),
and simulate the two marker moves in memory on both layers of main.tex (nothing is written except the JSON)."""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
PAGES = RUN / "b146_150"
OUT = RUN / "findings_146_150.json"
VOL = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
NL = "<NL>"


def s(x):
    return None if x is None else x.replace(NL, "\n")


def fx(old, new):
    return {"old": s(old), "new": s(new)}


F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


RHOM = r"\(\RHom(E,F)\) (\RHom = \mathrm R\!\operatorname{Hom}: plain R, Hom not underlined)"
RHOM_NOTE = r"The same edit underlines Hom (the sheaf Hom). Forms already applied on pp. 116-118: \mathbb{R}\underline{\Hom}."

# ---------------------------------------------------------------- page 146
add(146, "start of page",
    "p. 146 begins '(les deux de gauche étant des homomorphismes de préfaisceaux d'anneaux)' (both scans)",
    "page_146.tex begins 'deux de gauche'; the line '(les' stood above the folio-146 marker (end of page_145.tex)",
    "marker", "high", None,
    "Already reported by batch 141-145 (findings_141_145, p. 145 'end of page') and already applied: in the current "
    "main.tex (both layers) the folio-146 marker stands before '(les'. No action; do not run the move again.")
add(146, "Définition 6.11, statement",
    "underlined by word groups: 'On appelle', 'et l'on note', 'la', 'S-fonction additive', 'de', 'dans', "
    "'définie par'; the defined term 'rang,' and its notation 'rg' are not underlined (both scans; "
    "crops_146_150/p146_s2_def611.png)",
    "no emphasis: the definition is in roman",
    "underline", "high",
    fx(r"On appelle rang, et l'on note \(\rg\) la \(S\)-fonction additive de \(\mathcal C_1\) dans \(\mathbb Z_S\) définie par",
       r"\emph{On appelle} rang, \emph{et l'on note} \(\rg\) \emph{la \(S\)-fonction additive de \(\mathcal C_1\) dans \(\mathbb Z_S\) définie par}"),
    "Defined term and notation left out of the emphasis, as Définitions 2.8 and 6.1 (findings_101_105, "
    "findings_136_140). One edit (balanced braces).")
add(146, "Proposition 6.12 a)",
    "'Pour' and 'on a' underlined; L, M ∈ ob D⁻(X)_parf (X ∈ ob S) not (both scans; crops_146_150/p146_s3_prop612a.png)",
    "no emphasis",
    "underline", "high",
    fx(r"Pour \(L,M\in\Ob\Dpx^-(X)_{\mathrm{parf}}\) (\(X\in\Ob S\)), on a",
       r"\emph{Pour} \(L,M\in\Ob\Dpx^-(X)_{\mathrm{parf}}\) (\(X\in\Ob S\)), \emph{on a}"),
    "")
add(146, "Proposition 6.12 b), first sentence and 'Pour'",
    "underlined: 'Soit', 'un morphisme de topos localement annelés.', 'Pour'; the 'on a' of the next clause is not "
    "underlined (both scans; crops_146_150/p146_s3_prop612b.png)",
    "no emphasis",
    "underline", "high",
    fx(r"Soit \(u:(S',A')\longrightarrow(S,A)\) un morphisme de topos localement annelés. Pour",
       r"\emph{Soit \(u:(S',A')\longrightarrow(S,A)\) un morphisme de topos localement annelés. Pour}"),
    "Block over the formula, as the file's other statements; 'on a' stays roman as printed.")
add(146, "Proposition 6.12 b), 'rg(Lu*(M)) = u*(rg(M))'",
    "𝕃u*: an L with a doubled stem, double-struck (both scans; crops_146_150/p146_s3_Lu.png)",
    r"\(\rg(\mathrm L u^*(M))=u^*(\rg(M))\) (plain L)",
    "font", "high",
    fx(r"\mathrm L u^*", r"\mathbb L u^*"),
    "Same functor and form as p. 145 (findings_141_145, applied as \\mathbb L u^*). The L over the tensor sign in a) "
    "is a plain typed L (\\overset{\\mathrm L}{\\otimes} right).")
add(146, "Proposition 6.12 b), 'En d'autres termes, ...'",
    "underlined: 'En d'autres termes,', 'l'homomorphisme rang', 'est un homomorphisme de préfaisceaux d'anneaux, "
    "compatible avec les images inverses'; the colon, k(D⁻(S)_parf) → Z_S and the final stop not (both scans)",
    "no emphasis",
    "underline", "high",
    fx(r"En d'autres termes, l'homomorphisme rang : \(k(\Dpx^-(S)_{\mathrm{parf}})\longrightarrow \mathbb Z_S\) est un homomorphisme de préfaisceaux d'anneaux, compatible avec les images inverses.",
       r"\emph{En d'autres termes, l'homomorphisme rang} : \(k(\Dpx^-(S)_{\mathrm{parf}})\longrightarrow \mathbb Z_S\) \emph{est un homomorphisme de préfaisceaux d'anneaux, compatible avec les images inverses}."),
    "One edit (balanced braces).")
add(146, "'Preuve.' (pp. 146, 147, 148, 149 twice, 150)",
    "only the word underlined, the full stop after the underline (both scans; crops_146_150/p146_s2_preuve.png)",
    r"\emph{Preuve.} (stop inside the emphasis)",
    "underline", "medium", None,
    r"Convention, as reported for pp. 138-139 (findings_136_140): one scripted pass \emph{Preuve.} -> \emph{Preuve}. "
    "Not itemized.")

# ---------------------------------------------------------------- page 147
add(147, "6.13, 'L'application i_X : ...'",
    "'L'application i_X : H⁰(X, Z_S) → k(Parf(X)), ...' continues the paragraph of 6.13: no indent, ordinary line "
    "spacing after '... ⊗ L .).' (both scans)",
    "blank line (new paragraph) before 'L'application'",
    "other", "low",
    fx(r"\otimes L\).).<NL><NL>L'application", r"\otimes L\).).<NL>L'application"),
    "New paragraphs of this exposé are indented (p. 146 'En vertu de (6.7)', p. 148 'On en déduit'); this line is not.")
add(147, "Proposition 6.14, first line",
    "'Sous les hypothèses de' and 'on a' underlined; '(6.13),' not (both scans; witness w147_bot.png)",
    "no emphasis: the statement is in roman",
    "underline", "high",
    fx(r"Sous les hypothèses de (6.13), on a", r"\emph{Sous les hypothèses de} (6.13), \emph{on a}"),
    "")
add(147, "Proposition 6.14, '(autrement dit, ...). En outre le rang'",
    "underlined by word groups: 'autrement dit,', 'considéré comme préfaisceau de', '-algèbres au', 'moyen de', "
    "'est augmenté vers', 'par le rang', 'En outre le rang'; the parentheses and the stop not (both scans)",
    "no emphasis",
    "underline", "high",
    fx(r"(autrement dit, \(k(\Parf(S))\), considéré comme préfaisceau de \(\mathbb Z_S\)-algèbres au moyen de \(i\), est augmenté vers \(\mathbb Z_S\) par le rang). En outre le rang",
       r"(\emph{autrement dit, \(k(\Parf(S))\), considéré comme préfaisceau de \(\mathbb Z_S\)-algèbres au moyen de \(i\), est augmenté vers \(\mathbb Z_S\) par le rang}). \emph{En outre le rang}"),
    "One edit (balanced braces).")
add(147, "Proposition 6.14, last line",
    "'définit un isomorphisme sur les faisceaux associés' underlined (both scans)",
    "no emphasis",
    "underline", "high",
    fx(r"définit un isomorphisme sur les faisceaux associés.", r"\emph{définit un isomorphisme sur les faisceaux associés}."),
    "End of the statement 6.14.")

# ---------------------------------------------------------------- page 148
add(148, "Corollaire 6.15, statement",
    "underlined by word groups from 'Sous les hypothèses de' to 'canoniquement à' ('(6.13),' not), then 'objet final de', "
    "'la fonction rang correspondant à', 'et à la section unité de'; H⁰(S,F), '(S =' and the final Z_S . not (both scans)",
    "no emphasis: the statement is in roman",
    "underline", "high",
    fx(r"Sous les hypothèses de (6.13), pour tout faisceau abélien \(F\) sur \(S\), le groupe des \(S\)-fonctions additives de \(\Parf(S)\) dans \(F\) s'identifie canoniquement à \(H^0(S,F)\) (\(S\) = objet final de \(S\)), la fonction rang correspondant à \(F=\mathbb Z_S\) et à la section unité de \(\mathbb Z_S\).",
       r"\emph{Sous les hypothèses de} (6.13), \emph{pour tout faisceau abélien \(F\) sur \(S\), le groupe des \(S\)-fonctions additives de \(\Parf(S)\) dans \(F\) s'identifie canoniquement à} \(H^0(S,F)\) (\(S\) = \emph{objet final de \(S\)}), \emph{la fonction rang correspondant à \(F=\mathbb Z_S\) et à la section unité de} \(\mathbb Z_S\)."),
    "One edit (balanced braces).")
add(148, "Proposition 7.1, 'Soient E ∈ ob D(S)_parf, ...'",
    "'Soient' underlined (both scans; witness w148_bot.png)",
    "no emphasis",
    "underline", "high",
    fx(r"Soient \(E\in\Ob\Dpx(S)_", r"\emph{Soient} \(E\in\Ob\Dpx(S)_"),
    "")
add(148, "Proposition 7.1 a), first sentence",
    "underlined: 'Si', 'est à cohomologie localement bornée,', 'il en est de même de' (both scans)",
    "no emphasis",
    "underline", "high",
    fx(r"Si \(F\) est à cohomologie localement bornée, il en est de même de",
       r"\emph{Si \(F\) est à cohomologie localement bornée, il en est de même de}"),
    "")
add(148, "Proposition 7.1 a), 'R Hom(E,F). Si' at the start of the line",
    "ℝ Hom̲(E,F): double-struck R (doubled stem, thick at the margin), Hom underlined; the following 'Si' underlined "
    "(both scans; crops_146_150/p148_s3_RHom1.png, w148_bot.png)",
    RHOM, "font", "high",
    fx(r"\(\RHom(E,F)\). Si", r"\(\mathbb{R}\underline{\Hom}(E,F)\). \emph{Si}"),
    RHOM_NOTE + " The edit also sets the underlined 'Si' that opens the second sentence (the entry below covers the rest).")
add(148, "Proposition 7.1 a), second sentence",
    "underlined: 'est pseudo-cohérent', 'resp.', 'localement de tor-dimension finie,', 'resp. parfait),', "
    "'il en est de même de'; F ∈ ob D(S) not (both scans)",
    "no emphasis",
    "underline", "high",
    fx(r"est pseudo-cohérent (resp. localement de tor-dimension finie, resp. parfait), il en est de même de",
       r"\emph{est pseudo-cohérent (resp. localement de tor-dimension finie, resp. parfait), il en est de même de}"),
    "")
add(148, "Proposition 7.1 a), last formula 'R Hom(E,F).'",
    "ℝHom̲(E,F): double-struck R, Hom underlined (both scans)",
    RHOM, "font", "high",
    fx(r"\(\RHom(E,F)\).<NL>", r"\(\mathbb{R}\underline{\Hom}(E,F)\).<NL>"),
    RHOM_NOTE)

# ---------------------------------------------------------------- page 149
add(149, "start of page",
    "p. 149 begins 'b) Supposons que E soit en outre de tor-dimension finie'; p. 148 ends '... il en est de même de "
    "ℝHom(E,F).' (both scans; witness DjVu p. 160)",
    r"'\textbf{b)}' is the last line of page_148.tex (above the folio-149 marker); page_149.tex begins 'Supposons que'",
    "marker", "high", None,
    "Page 149 really begins with the item letter b). Move the folio-149 marker above it: "
    r"python -I move_marker.py 6 149 '\textbf{b)}' --before (simulated on both layers: '... de \(\RHom(E,F)\).', "
    r"blank line, the marker, '\textbf{b)}', 'Supposons que ...'). If the bold item-letter pass has already turned it "
    "into 'b)', use the anchor 'b)'.")
add(149, "Proposition 7.1 b), 'il en est de même de R Hom(E,F)'",
    "ℝHom̲(E,F): double-struck R, Hom underlined (both scans; witness w149_top.png)",
    RHOM, "font", "high",
    fx(r"\(\RHom(E,F)\). Plus", r"\(\mathbb{R}\underline{\Hom}(E,F)\). Plus"),
    RHOM_NOTE + " Part b) of 7.1 is not underlined in the print (TeX right).")
add(149, "Proposition 7.1 b), 'H^i(R Hom(E,F)) = 0'",
    "H^i( ℝHom̲(E,F)): double-struck R, Hom underlined; this H is plain (both scans; crops_146_150/p149_s1_lines56.png)",
    RHOM, "font", "high",
    fx(r"\Ho^i(\RHom(E,F))", r"\Ho^i(\mathbb{R}\underline{\Hom}(E,F))"),
    RHOM_NOTE)
add(149, "Proposition 7.1 b), '(resp. tor.amp(R Hom(E,F)) ⊂ [m-b,n-a])'",
    "R with a thickened, doubled stem (the two strokes overlap closely), Hom underlined (both scans; "
    "crops_146_150/p149_s1_resp_R.png, w149_resp_R.png)",
    RHOM, "font", "medium",
    fx(r"\tamp(\RHom(E,F))", r"\tamp(\mathbb{R}\underline{\Hom}(E,F))"),
    RHOM_NOTE + " Same shape as the first ℝ of p. 148 a); every other R of this paragraph is plainly double-struck.")
add(149, "Lemme 7.1.1, statement",
    "underlined: 'Soit', 'Si', 'est strictement pseudo-cohérent', 'à composantes facteurs directs de Modules libres de "
    "type fini', 'la flèche canonique de'; the formulas, '(i.e. (2.1)', '),' and D⁺(S) not (both scans)",
    "no emphasis: the statement is in roman",
    "underline", "high",
    fx(r"Soit \(E\in\Ob\Dpx^-(S)\), \(F\in\Ob\Dpx^+(S)\). Si \(E\) est strictement pseudo-cohérent (i.e. (2.1) à composantes facteurs directs de Modules libres de type fini), la flèche canonique de",
       r"\emph{Soit} \(E\in\Ob\Dpx^-(S)\), \(F\in\Ob\Dpx^+(S)\). \emph{Si \(E\) est strictement pseudo-cohérent} (i.e. (2.1) \emph{à composantes facteurs directs de Modules libres de type fini}), \emph{la flèche canonique de}"),
    "One edit (balanced braces).")
add(149, "Lemme 7.1.1, display 'Hom(E,F) → R Hom(E,F)'",
    "Hom̲˙(E,F) → ℝHom̲(E,F): both Hom underlined, R double-struck (both scans; witness w149_bot.png)",
    r"\Hom^\bullet(E,F)\longrightarrow\RHom(E,F) (plain Hom, plain R)",
    "font", "high",
    fx(r"\Hom^\bullet(E,F)\longrightarrow\RHom(E,F)",
       r"\underline{\Hom}^\bullet(E,F)\longrightarrow\mathbb{R}\underline{\Hom}(E,F)"),
    "The same edit underlines both Hom. The raised typed dot is \\bullet as in Gr (handled globally).")
add(149, "Lemme 7.1.1, 'est un isomorphisme.'",
    "'est un isomorphisme' underlined (both scans)",
    "no emphasis",
    "underline", "high",
    fx(r"\]<NL>est un isomorphisme.", r"\]<NL>\emph{est un isomorphisme}."),
    "End of the statement 7.1.1.")
add(149, "proof of 7.1.1, spectral sequence display",
    "E_2^{pq} = H̲^p(Ext̲^q(E,F)˙) ⟹ Ext̲^*(E,F): H and both Ext underlined (cohomology and Ext sheaves; both scans)",
    r"\Ho^p, \Ext (plain)",
    "underline", "high",
    fx(r"E_2^{pq}=\Ho^p(\Ext^q(E,F)^\bullet)\Longrightarrow \Ext^*(E,F),",
       r"E_2^{pq}=\underline{\Ho}^p(\underline{\Ext}^q(E,F)^\bullet)\Longrightarrow \underline{\Ext}^*(E,F),"),
    r"Forms main.tex already uses for the underlined sheaves: \underline{\Ext}^i (p. 117), \underline{\Ho}^i (p. 131).")
add(149, "proof of 7.1.1, display 'où Ext^q(E,F)^i = ...'",
    "both Ext underlined (both scans)",
    r"\Ext (plain)",
    "underline", "high",
    fx(r"\Ext^q(E,F)^i=\coprod_{i_2-i_1=i}\Ext^q(E^{i_1},F^{i_2}),",
       r"\underline{\Ext}^q(E,F)^i=\coprod_{i_2-i_1=i}\underline{\Ext}^q(E^{i_1},F^{i_2}),"),
    "")
add(149, "proof of 7.1.1, 'dégénère puisque Ext^q(E,F) = 0'",
    "Ext underlined (both scans)",
    r"\(\Ext^q(E,F)^\bullet=0\)",
    "underline", "high",
    fx(r"puisque \(\Ext^q(E,F)^\bullet=0\)", r"puisque \(\underline{\Ext}^q(E,F)^\bullet=0\)"),
    "")

# ---------------------------------------------------------------- page 150
add(150, "start of page",
    "p. 150 begins with the display 'E_2^{po} = H^p(Hom(E,F)) ⥲ Ext^p(E,F) = H^p(R Hom(E,F)) ,'; 'isomorphismes' is the "
    "last line of p. 149 (both scans; witness DjVu pp. 160-161)",
    "page_150.tex begins 'isomorphismes' (under the folio-150 marker)",
    "marker", "high", None,
    "The marker stands one line too early. Move it below 'isomorphismes': python -I move_marker.py 6 150 '\\[' "
    "(simulated on both layers: '... On en déduit des', 'isomorphismes', the marker, '\\[', 'E_2^{p0}=...').")
add(150, "first display, left side",
    "E_2^{po} = H̲^p(Hom̲˙(E,F)): H and Hom underlined (both scans; witness w150_top.png)",
    r"\Ho^p(\Hom^\bullet(E,F)) (plain)",
    "underline", "high",
    fx(r"E_2^{p0}=\Ho^p(\Hom^\bullet(E,F))", r"E_2^{p0}=\underline{\Ho}^p(\underline{\Hom}^\bullet(E,F))"),
    "")
add(150, "first display, 'Ext^p(E,F) = H^p('",
    "Ext̲^p(E,F) = H̲^p( : Ext and H underlined (both scans)",
    r"\Ext^p(E,F)=\Ho^p( (plain)",
    "underline", "high",
    fx(r"\xrightarrow{\sim}\Ext^p(E,F)=\Ho^p", r"\xrightarrow{\sim}\underline{\Ext}^p(E,F)=\underline{\Ho}^p"),
    "This isomorphism sign has an arrowhead (⥲): \\xrightarrow{\\sim} right here.")
add(150, "first display, 'R Hom(E,F))'",
    "ℝHom̲(E,F): double-struck R, Hom underlined (both scans)",
    RHOM, "font", "high",
    fx(r"(\RHom(E,F)),", r"(\mathbb{R}\underline{\Hom}(E,F)),"),
    RHOM_NOTE)
add(150, "Proposition 7.1.2, 'Soit ... tels que l'on ait'",
    "underlined: 'Soit', 'un morphisme de topos annelés.', 'Soient', 'et', 'tels que l'on ait' (both scans)",
    "no emphasis: the statement is in roman",
    "underline", "high",
    fx(r"Soit \(f:(S',A')\longrightarrow(S,A)\) un morphisme de topos annelés. Soient \(E\in\Ob\Dpx^-(S)\) et \(F\in\Ob\Dpx^b(S)\) tels que l'on ait",
       r"\emph{Soit \(f:(S',A')\longrightarrow(S,A)\) un morphisme de topos annelés. Soient \(E\in\Ob\Dpx^-(S)\) et \(F\in\Ob\Dpx^b(S)\) tels que l'on ait}"),
    "Block over the formulas, as the file's other statements.")
add(150, "Proposition 7.1.2, 'R Hom(E,F) ∈ ob D^b(S)'",
    "ℝHom̲(E,F): double-struck R, Hom underlined (both scans)",
    RHOM, "font", "high",
    fx(r"\(\RHom(E,F)\in", r"\(\mathbb{R}\underline{\Hom}(E,F)\in"),
    RHOM_NOTE)
add(150, "Proposition 7.1.2, 'et Lf*(F) ∈ ob D^b(S')', the word 'et'",
    "'et' underlined (both scans)",
    "no emphasis",
    "underline", "high",
    fx(r"\Dpx^b(S)\) et \(", r"\Dpx^b(S)\) \emph{et} \("),
    "")
add(150, "Proposition 7.1.2, 'Lf*(F)'",
    "𝕃f*(F): double-struck L (both scans)",
    r"\(\mathrm Lf^*(F)\in...\) (plain L)",
    "font", "high",
    fx(r"\mathrm Lf^*(F)", r"\mathbb{L}f^*(F)"),
    "Form as applied on pp. 111 and 118 (\\mathbb{L}f^*).")
add(150, "Proposition 7.1.2, 'Il existe une flèche canonique fonctorielle'",
    "underlined (both scans)",
    "no emphasis",
    "underline", "high",
    fx(r"Il existe une flèche canonique fonctorielle", r"\emph{Il existe une flèche canonique fonctorielle}"),
    "")
add(150, "Proposition 7.1.2, display",
    "𝕃f* ℝHom̲(E,F) → ℝHom̲(𝕃f*E, 𝕃f*F) . : every L and R double-struck, both Hom underlined (both scans; "
    "crops_146_150/p150_s2_disp712.png, w150_disp712.png)",
    r"\mathrm Lf^*\RHom(E,F) ... \RHom(\mathrm Lf^*E,\mathrm Lf^*F). (plain L and R, Hom not underlined)",
    "font", "high",
    fx(r"\mathrm Lf^*\RHom(E,F)<NL>  \longrightarrow<NL>  \RHom(\mathrm Lf^*E,\mathrm Lf^*F).",
       r"\mathbb{L}f^*\mathbb{R}\underline{\Hom}(E,F)<NL>  \longrightarrow<NL>  \mathbb{R}\underline{\Hom}(\mathbb{L}f^*E,\mathbb{L}f^*F)."),
    "The same edit underlines both Hom.")
add(150, "Proposition 7.1.2, 'Celle-ci est un isomorphisme si E est parfait.'",
    "underlined: 'Celle-ci est un isomorphisme si', 'est parfait'; E and the stop not (both scans)",
    "no emphasis",
    "underline", "high",
    fx(r"Celle-ci est un isomorphisme si \(E\) est parfait.", r"\emph{Celle-ci est un isomorphisme si} \(E\) \emph{est parfait}."),
    "")
add(150, "proof of 7.1.2, 'des foncteurs Lf* et Rf_*'",
    "𝕃f* and ℝf_*: double-struck L and R (both scans)",
    r"\(\mathrm Lf^*\) et \(\mathrm Rf_*\)",
    "font", "high",
    fx(r"\(\mathrm Lf^*\) et \(\mathrm Rf_*\)", r"\(\mathbb{L}f^*\) et \(\mathbb{R}f_*\)"),
    "As p. 83 (\\mathbb{R}f_*) and p. 111 (\\mathbb{L}f^*).")
add(150, "proof of 7.1.2, first display",
    "ℝHom̲(E,F) → ℝf_* ℝHom̲(𝕃f*E , 𝕃f*F) . : every L and R double-struck, both Hom underlined (both scans; "
    "crops_146_150/p150_s2_disp_fleche.png, w150_disp_fleche.png)",
    r"\RHom(E,F) ... \mathrm Rf_*\RHom(\mathrm Lf^*E,\mathrm Lf^*F).",
    "font", "high",
    fx(r"\RHom(E,F)<NL>  \longrightarrow<NL>  \mathrm Rf_*\RHom(\mathrm Lf^*E,\mathrm Lf^*F).",
       r"\mathbb{R}\underline{\Hom}(E,F)<NL>  \longrightarrow<NL>  \mathbb{R}f_*\mathbb{R}\underline{\Hom}(\mathbb{L}f^*E,\mathbb{L}f^*F)."),
    "The same edit underlines both Hom.")
add(150, "proof of 7.1.2, 'la flèche d'adjonction F → Rf_* Lf*F'",
    "ℝf_* 𝕃f*F: double-struck R and L (both scans)",
    r"\(F\to\mathrm Rf_*\mathrm Lf^*F\)",
    "font", "high",
    fx(r"\(F\to\mathrm Rf_*\mathrm Lf^*F\)", r"\(F\to\mathbb{R}f_*\mathbb{L}f^*F\)"),
    "")
add(150, "proof of 7.1.2, duality display, left side",
    "ℝf_* ℝHom̲(𝕃f*E, 𝕃f*F): double-struck R and L, Hom underlined (both scans)",
    r"\mathrm Rf_*\RHom(\mathrm Lf^*E,\mathrm Lf^*F)",
    "font", "high",
    fx(r"\mathrm Rf_*\RHom(\mathrm Lf^*E,\mathrm Lf^*F)<NL>",
       r"\mathbb{R}f_*\mathbb{R}\underline{\Hom}(\mathbb{L}f^*E,\mathbb{L}f^*F)<NL>"),
    "The same edit underlines Hom. Disjoint from the entry for the first display (that one ends with a full stop).")
add(150, "proof of 7.1.2, duality display, the isomorphism sign",
    "≃: a tilde over a long plain line, no arrowhead (both scans; crops_146_150/p150_s2_simeq.png, w150_simeq.png); "
    "the isomorphism of the first display of the page has an arrowhead",
    r"\xrightarrow{\sim}",
    "symbol", "high",
    fx(r"\xrightarrow{\sim}<NL>", r"\simeq<NL>"),
    "\\simeq as for the same sign on p. 146 (A_U^p ≃ A_U^q); its length is not significant.")
add(150, "proof of 7.1.2, duality display, right side",
    "ℝHom̲(E, ℝf_*𝕃f*F) . : double-struck R and L, Hom underlined (both scans)",
    r"\RHom(E,\mathrm Rf_*\mathrm Lf^*F).",
    "font", "high",
    fx(r"\RHom(E,\mathrm Rf_*\mathrm Lf^*F).", r"\mathbb{R}\underline{\Hom}(E,\mathbb{R}f_*\mathbb{L}f^*F)."),
    "The same edit underlines Hom.")
add(150, "Proposition 7.2, statement before the display",
    "underlined: 'Il existe', 'pour', 'et', 'une flèche canonique fonctorielle'; '(cf. SGA 5 I 1.6),' and the formulas "
    "not (both scans)",
    "no emphasis: the statement is in roman",
    "underline", "high",
    fx(r"Il existe (cf. SGA 5 I 1.6), pour \(E\in\Ob\Dpx(S)\) et \(F\in\Ob\Dpx^+(S)\), une flèche canonique fonctorielle",
       r"\emph{Il existe} (cf. SGA 5 I 1.6), \emph{pour \(E\in\Ob\Dpx(S)\) et \(F\in\Ob\Dpx^+(S)\), une flèche canonique fonctorielle}"),
    "The reference stays roman as printed. One edit (balanced braces).")
add(150, "Proposition 7.2, display",
    "E → ℝHom̲( ℝHom̲(E,F),F) . : both R double-struck, both Hom underlined (both scans)",
    r"E\longrightarrow\RHom(\RHom(E,F),F).",
    "font", "high",
    fx(r"E\longrightarrow\RHom(\RHom(E,F),F).", r"E\longrightarrow\mathbb{R}\underline{\Hom}(\mathbb{R}\underline{\Hom}(E,F),F)."),
    "The same edit underlines both Hom.")
add(150, "Proposition 7.2, 'Celle-ci est un isomorphisme si ...'",
    "'Celle-ci est un isomorphisme si' underlined; the rest of the line not (both scans)",
    "no emphasis",
    "underline", "high",
    fx(r"Celle-ci est un isomorphisme si \(E\in", r"\emph{Celle-ci est un isomorphisme si} \(E\in"),
    "")


# ---------------------------------------------------------------- checks
def balanced(x):
    d = 0
    for i, c in enumerate(x):
        if c == "{" and (i == 0 or x[i - 1] != "\\"):
            d += 1
        elif c == "}" and (i == 0 or x[i - 1] != "\\"):
            d -= 1
            if d < 0:
                return False
    return d == 0


ok = True
texts = {p: (PAGES / f"page_{p}.tex").read_text(encoding="utf-8") for p in range(146, 151)}
spans = {}
for f in F:
    if not f["fix"]:
        continue
    t = texts[f["page"]]
    old, new = f["fix"]["old"], f["fix"]["new"]
    n = t.count(old)
    if n != 1:
        ok = False
        print("COUNT", n, f["page"], repr(old[:60]))
    if "%%%%%%%%%%" in old:
        ok = False
        print("MARKER IN OLD", f["page"])
    if balanced(old) != balanced(new) or not balanced(new):
        ok = False
        print("BRACES", f["page"], repr(new[:60]))
    k = t.find(old)
    spans.setdefault(f["page"], []).append((k, k + len(old), old[:40]))
for p, sp in spans.items():
    sp.sort()
    for a, b in zip(sp, sp[1:]):
        if a[1] > b[0]:
            ok = False
            print("OVERLAP", p, a, b)
# apply all fixes of each page in sequence
for p in range(146, 151):
    t = texts[p]
    for f in F:
        if f["page"] == p and f["fix"]:
            assert t.count(f["fix"]["old"]) == 1, (p, f["fix"]["old"])
            t = t.replace(f["fix"]["old"], f["fix"]["new"])
print("all checks passed" if ok else "CHECKS FAILED")

# informational: do the olds also occur once in the current main.tex (both layers)?
MARK = re.compile(r"%{10}\s+scan idx \d+\s+\|\s+folio (\d+)\s+%{10}")
for layer in ("diplomatic", "current"):
    mt = (VOL / layer / "main.tex").read_text(encoding="utf-8")
    ms = {int(m.group(1)): m for m in MARK.finditer(mt)}
    lo, hi = ms[146].start(), ms[152].start()
    seg = mt[lo:hi]
    bad = [(f["page"], f["fix"]["old"][:50]) for f in F if f["fix"] and seg.count(f["fix"]["old"]) != 1]
    print(layer, "olds not unique in folios 146-151 of main.tex:", bad)
    # state of the 146 marker
    m = ms[146]
    print(layer, "after 146 marker:", repr(mt[m.end():m.end() + 25]))


# simulate the two marker moves (logic of move_marker.py), in memory only
def simulate(t, folio, anchor, before):
    m = next(m for m in MARK.finditer(t) if int(m.group(1)) == folio)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    j = t2.find(line)
    return t2[j - 120:j + len(line) + 60]


for layer in ("diplomatic", "current"):
    mt = (VOL / layer / "main.tex").read_text(encoding="utf-8")
    print("----", layer, "149:")
    print(simulate(mt, 149, r"\textbf{b)}", True))
    print("----", layer, "150:")
    print(simulate(mt, 150, r"\[", False))

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
from collections import Counter
c = Counter((f["page"], f["kind"] == "misprint_in_print") for f in F)
print({p: (c[(p, False)], c[(p, True)]) for p in range(146, 151)}, len(F))
