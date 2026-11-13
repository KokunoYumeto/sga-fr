"""Build findings_676_680.json and check every fix 'old' (and every kept-misprint 'tex') against page_NNN.tex."""
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_6"
B = RUN + r"\b676_680"
OUT = RUN + r"\findings_676_680.json"
MAIN = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex"


def J(*parts):
    return "\n".join(parts)


def fx(old, new):
    return {"old": old, "new": new}


F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None, check_tex=False):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    d["_check_tex"] = check_tex
    F.append(d)


FR = "Second reading (Codex fr_r1, 5 Aug)"

# ---------------------------------------------------------------- page 676
add(676, "page start (first line under the running head '- 10 -')",
    "The page begins 'résolu de façon satisfaisante la question soulevée au n° 1.' (both scans).",
    "page_676.tex begins 'façon satisfaisante'; 'résolu de' ended page_675.tex ('... une fois résolu de').",
    "marker", "high", None,
    "Page 676 really begins at 'résolu de'. ALREADY DONE: main.tex (both layers, 13 Nov 17:11) now has '... une fois', "
    "the folio-676 marker, 'résolu de', 'façon satisfaisante' (the move reported in findings_671_675.json, p. 675 end). "
    "Nothing to apply; do not run move_marker.py for 676 again.")

add(676, "first line, 'la question soulevée au n° 1.'",
    "n° 1: n with the raised degree ring (both scans).",
    "au no 1.", "symbol", "high", fx("au no 1.", r"au n\textsuperscript{o} 1."),
    "As the n° fixes of pp. 671-675 (findings_671_675.json). " + FR + r": n\textsuperscript{o}~1: the print agrees with it.")

add(676, "throughout pp. 676-680: the ten phi",
    "the typed slashed o ø (straight phi) at all ten places: p. 676 'le noyau de ø^i', 'que ø^2', '(Que ø^1', 'le fait que ø^2'; "
    "p. 677 'l'homomorphisme ø n'est pas'; p. 678 'l'homomorphisme ø : A(X)->Gr_top(X)'; p. 680 display 'ø : A(G)->Gr_top(G)', "
    "'d'un ø non bijectif', 'pas par ø, donc', 'pas par ø lorsque' (both scans; crops_676_680/m676_phi.png, w678_phi.png)",
    r"\varphi at all ten places", "symbol", "medium", None,
    r"Convention of the transcription, already reported for Exposé XIV in findings_671_675.json (p. 671 entry: one "
    r"replacement \varphi -> \phi over the exposé); pp. 676-680 print the same letter. Three examples: p. 676 "
    r"'\varphi^i:A^i(X)', p. 678 '\varphi:A(X)', p. 680 'd'un $\varphi$ non bijectif'. " + FR + r": also \varphi.")

add(676, "every cℓ of pp. 676 and 679 (the typed cl of (4.7), p. 677, is right)",
    "cℓ with the hand-drawn script ℓ (the ℓ of ℓ-adique): p. 676 'multiple entier de cℓ(Y):', the display "
    "'c_i(Y) = n(Y) cℓ(Y) .', 'lorsque cℓ(Y)'; p. 679 'cℓ˙(Y)', 'cℓ˙(Y')', 'cℓ˙(L)'. On p. 677 (4.7) the print types "
    "'cl(Y)' with a typed l (both scans; crops_676_680/m676_cl.png, m677_cl.png, m679_clY.png)",
    r"\cl (= \operatorname{cl}, upright cl) at all seven places", "symbol", "medium", None,
    r"Convention of the transcription, reported once (as for pp. 579-580, findings_576_580.json): \cl prints an upright "
    r"cl. Suggested: \operatorname{c\ell} at the six cℓ places (p. 676: 'multiple entier de $\cl(Y)$:', 'n(Y)\cl(Y).', "
    r"'lorsque $\cl(Y)$'; p. 679: the three \cl of the entries below), keeping \cl in (4.7). No blanket change of the "
    r"macro: the typescript also types cl.")

add(676, "'alors deg(Y.ξ^i)>0' (polarisation argument)",
    "deg(Y.ξ^i)>0, exponent i (both scans; crops_676_680/m676_Yxi.png)",
    r"\deg(Y\cdot\xi^i)>0", "misprint_in_print", "low", None,
    r"Y has codimension i (cl(Y) in A^i(X)); Y.ξ^k is a 0-cycle, with a degree, only for k = dim Y. The TeX keeps the "
    r"printed reading. Codex's claim on this place (SGA-SRC-001450) was rejected in RECONCILE_CODEX_6 as inference; the "
    r"scan confirms the printed ξ^i. " + FR + r": \xi^{\dim Y} (silent correction).",
    corrected=r"\deg(Y\cdot\xi^{\dim Y})>0", check_tex=True)

add(676, "'le noyau de ø^i : A^i(X) -> Gr^i_top(X) est annulé par (i-1)!'",
    "the map stands in the running text: 'le noyau de ø^i : A^i(X)->Gr^i_top(X) est annulé par (i-1)! , et en particulier' "
    "is one line (both scans)",
    r"a display \[ \varphi^i:A^i(X)\longrightarrow \Gtop^i(X) \]", "other", "medium",
    fx(J(r"le noyau de", r"\[", r" \varphi^i:A^i(X)\longrightarrow \Gtop^i(X)", r"\]", r"est annulé"),
       r"le noyau de $\varphi^i:A^i(X)\longrightarrow \Gtop^i(X)$ est annulé"),
    "The print sets the map inline; the TeX makes it a display (same kind of fix as SGA 6 p. 21, applied). Apply before "
    r"an exposé-wide \varphi -> \phi replacement (its 'old' contains \varphi). " + FR + ": also a display (the print "
    "agrees with neither).")

add(676, "end of 4.3, 'dans [9, n°4, 3°]'",
    "[9 , n°4, 3°] with raised degree rings after n and after 3 (both scans)",
    "[9, no 4, 3o]", "symbol", "high",
    fx("[9, no 4, 3o]", r"[9, n\textsuperscript{o}~4, 3\textsuperscript{o}]"),
    FR + r": [9, n\textsuperscript{o}~4, 3\textsuperscript{o}]: the print agrees with it.")

add(676, "4.4, 'pour une immersion fermée f: Y   X'",
    "f: Y, an empty space, X: no arrow and no trace of ink between Y and X, while the other hand-drawn arrows of the page "
    "are complete (main scan and witness; crops_676_680/m676_fYX.png, w687_small.png)",
    r"immersion fermée $f:Y\to X$ de (arrow silently supplied)", "misprint_in_print", "high",
    fx(r"immersion fermée $f:Y\to X$ de", r"immersion fermée $f:Y\qquad X$ de"),
    "The hand-drawn arrow was never drawn; the TeX silently supplies it. The fix restores the printed reading (as SGA 7 I "
    "p. 193 (3.4.5)). " + FR + ": has the arrow (silent correction).",
    corrected=r"immersion fermée $f:Y\to X$ de")

add(676, "(4.6), 'f^*f_*(y) = y c_d(N)'",
    "N underlined (N̲), both scans", r"y\,c_d(N),", "underline", "high",
    fx(r"y\,c_d(N),", r"y\,c_d(\underline{N}),"),
    FR + r": c_d(\underline N): the print agrees with it. Same N̲ in the next line and in (4.7), p. 677.")

add(676, "after (4.6), 'formule valable dans Gr˙_top(X), y étant dans Gr˙_top(Y)'",
    "Gr˙_top(X) (both scans)", r"formule valable dans $\Gtop^\bullet(X)$", "misprint_in_print", "medium", None,
    "f^*f_*(y) and y c_d(N) lie in Gr_top(Y) (f: Y -> X, y in Gr_top(Y)); the next page speaks of 'la même formule dans "
    "A(Y)'. The TeX keeps the printed reading. " + FR + r": \operatorname{Gr}'_{\mathrm{top}}(Y) (silent correction).",
    corrected=r"formule valable dans $\Gtop^\bullet(Y)$", check_tex=True)

add(676, "last line, 'N le faisceau conormal'",
    "N underlined (N̲), both scans", r"$N$ le faisceau conormal", "underline", "high",
    fx(r"$N$ le faisceau conormal", r"$\underline{N}$ le faisceau conormal"),
    FR + r": \underline N: the print agrees with it.")

# ---------------------------------------------------------------- page 677
add(677, "page start (first line under the running head '- 11 -')",
    "The page begins 'de Y dans X , supposé partout de rang d .' (both scans).",
    "page_677.tex begins 'dans $X$, supposé'; 'de $Y$' ends page_676.tex ('$N$ le faisceau conormal de $Y$').",
    "marker", "high", None,
    "Page 677 really begins at 'de $Y$'. Exact fix: python -I move_marker.py 6 677 'de $Y$' --before (the marker then "
    "stands between 'le faisceau conormal' and 'de $Y$', in both layers; checked by a read-only simulation on the "
    "17:11 main.tex). The split falls inside a TeX line, so the 10 Nov script did not move it.")

add(677, "'mais seulement modulo torsion.'",
    "'modulo torsion' underlined (both scans)", "seulement modulo torsion.", "underline", "high",
    fx("mais seulement modulo torsion.", r"mais seulement \emph{modulo torsion}."),
    r"The exposé writes the underline \emph (pp. 676, 678, 679). " + FR + ": plain too (the print agrees with neither).")

add(677, "footnote area",
    "two marks, '(*)' above and '(**)' below, with the one text 'cf. note de la page 23.' typed between them (in the later "
    "typeface of the inserted references); the text has only the call (*) after 'à l'heure actuelle', no call (**) "
    "anywhere on the page (both scans; crops_676_680/m677_foot.png, w688_small.png)",
    r"\footnote{cf. note de la page 23.} only; no (**)", "missing", "low",
    fx(r"actuelle\footnote{cf. note de la page 23.}", r"actuelle\footnote{cf. note de la page 23.\newline (**)}"),
    "The printed orphan mark (**) is lost. The fix keeps it as text after the note, in reading order; the coordinator may "
    "prefer another form. " + FR + ": no (**) either.")

add(677, "(4.7), 'f^*(cl(Y)) = c_d(N)'",
    "N underlined (N̲), both scans; cl typed here (\\cl right)", "=c_d(N),", "underline", "high",
    fx("=c_d(N),", r"=c_d(\underline{N}),"),
    FR + r": c_d(\underline N): the print agrees with it.")

add(677, "'même si k est le corps des complexes ! On se heurte'",
    "'On se heurte à un problème analogue' begins a new, indented paragraph (both scans)",
    "runs on in the same paragraph", "other", "high",
    fx("complexes ! On se heurte", J("complexes !", "", "On se heurte")),
    "Missing paragraph break. " + FR + ": runs on too.")

add(677, "Dans le cas où K˙(X) est engendré comme algébre sur Z",
    "algébre, with an acute accent (both scans; crops_676_680/m677_alg.png)", "comme algébre sur",
    "misprint_in_print", "high", None,
    "Typing error (wrong accent). The TeX keeps the printed reading. " + FR + ": algèbre (silent correction).",
    corrected="comme algèbre sur", check_tex=True)

add(677, "end of page_677.tex: the blank line before 'Or' (first line of p. 678)",
    "p. 678 begins 'Or prenons pour X une variété de drapeaux' at the left margin, not indented, whereas every new paragraph "
    "of pp. 676-677 is indented ('La validité', 'On se heurte', 'Signalons'): the paragraph of p. 677 runs on (both scans)",
    "a blank line, so 'Or' starts a new paragraph", "other", "low",
    fx(J(r"la composante de degré $1$ de $\Gtop^\bullet(X)$.", "", ""),
       J(r"la composante de degré $1$ de $\Gtop^\bullet(X)$.", "")),
    "Extra paragraph break (low: the break falls at the turn of the page). The 'old' works before and after the folio-678 "
    "marker move. " + FR + ": also a new paragraph.")

# ---------------------------------------------------------------- page 678
add(678, "page start (first line under the running head '- 12 -')",
    "The page begins 'Or prenons pour X une variété de drapeaux' (both scans).",
    "page_678.tex begins 'prenons pour $X$'; 'Or' is the last line of page_677.tex.",
    "marker", "high", None,
    "Page 678 really begins at 'Or'. Exact fix: python -I move_marker.py 6 678 'Or' --before (the line starts with the "
    "anchor, so the marker gets its own line before 'Or', in both layers; checked by a read-only simulation on the 17:11 "
    "main.tex). The paragraph break before 'Or' is a separate entry (p. 677).")

add(678, "throughout pp. 678 and 680: H^* and H^{2*}(G, Z_ℓ(*))",
    "the typewriter asterisk (the six-armed star of f^*, f_*) in every degree and twist: p. 678 (**) 'A(X) -> H^*(X(C),Z)'; "
    "p. 680 (4.9) 'H^{2*}(G,Z_ℓ(*))' (both stars), (4.10) 'A(G) -> H^*(G(C),Z)', the display 'A(G/B) = H^*(G/B(C),Z) -> "
    "H^*(G(C),Z)' (both scans; crops_676_680/w678_H.png, m680_49.png, w680_49.png, m680_410.png, m680_disp.png)",
    r"\bullet at all six places: p. 678 'A(X)\longrightarrow H^\bullet(X(\C),\Z),'; p. 680 'H^{2\bullet}(G,\Zell(\bullet))', "
    r"'A(G)\longrightarrow H^\bullet(G(\C),\Z),', 'A(G/B)\simeq H^\bullet(G/B(\C),\Z)\longrightarrow H^\bullet(G(\C),\Z).'",
    "symbol", "high", None,
    r"Convention of the transcription, already reported for Exposé XIV in findings_671_675.json (p. 673: H^{2\bullet} -> "
    r"H^{2*}, twist (\bullet) -> (*)) and findings_681_685.json (p. 681: also H^\bullet -> H^*); these six places fall under "
    r"it. Three examples: p. 678 'H^\bullet(X(\C),\Z)', p. 680 'H^{2\bullet}(G,\Zell(\bullet))', p. 680 "
    r"'H^\bullet(G/B(\C),\Z)'. " + FR + ": H^*, H^{2*}, (*) at all six: the print agrees with it.")

add(678, "'il a été prouvé par L. HODGKIN [12]'",
    "HODGKIN in capitals (both scans; crops_676_680/w678_hodgkin.png)", "par L. Hodgkin [12]", "word", "high",
    fx("par L. Hodgkin [12]", "par L. HODGKIN [12]"),
    "As 'P. JOUANOLOU' (pp. 671, 675). Again on p. 679. " + FR + ": L. Hodgkin here (the print agrees with neither).")

add(678, "'donc grâce à 4.2 l'homomorphisme ø : A(X) -> Gr˙_top(X) est un isomorphisme.'",
    "the map stands in the running text: 'momorphisme ø : A(X)->Gr_top(X) est un isomorphisme. De ces faits il résulte' is "
    "one line (both scans; crops_676_680/w678_phi.png)",
    r"a display \[ \varphi:A(X)\longrightarrow\Gtop^\bullet(X) \]", "other", "medium",
    fx(J(r"4.2 l'homomorphisme", r"\[", r" \varphi:A(X)\longrightarrow\Gtop^\bullet(X)", r"\]", r"est un isomorphisme."),
       r"4.2 l'homomorphisme $\varphi:A(X)\longrightarrow\Gtop^\bullet(X)$ est un isomorphisme."),
    r"The print sets the map inline. Apply before an exposé-wide \varphi -> \phi replacement (its 'old' contains "
    r"\varphi). " + FR + ": also a display.")

add(678, "'la cohomologie entière de X(C) est engendré par les éléments de degré 2'",
    "engendré, without the feminine e (both scans; crops_676_680/w678_engendre.png)",
    r"est engendré par les éléments de degré $2$", "misprint_in_print", "medium", None,
    "Agreement slip (la cohomologie). The TeX keeps the printed reading. " + FR + ": engendrée (silent correction).",
    corrected=r"est engendrée par les éléments de degré $2$", check_tex=True)

add(678, "'un produit de groupes Sℓ(n) et Sp(m)'",
    "Sℓ with the hand-drawn script ℓ (both scans; crops_676_680/w678_Sl.png)", r"\operatorname{Sl}(n)", "symbol", "high",
    fx(r"groupes $\operatorname{Sl}(n)$ et $\operatorname{Sp}(m)$. Il suffit", r"groupes $\operatorname{S\ell}(n)$ et $\operatorname{Sp}(m)$. Il suffit"),
    r"The file writes \operatorname{S\ell} elsewhere (5 times). Again on p. 680. " + FR + ": Sl (the print agrees with "
    "neither).")

add(678, "4.6, 'le \"bon\" anneau est l'anneau sans torsion A(X) = Gr˙_top(X), ayant comme base'",
    "A(X) ≃ Gr˙_top(X) in the running text: 'anneau est l'anneau sans torsion A(X)≃Gr_top(X), ayant comme base les cel-' "
    "is one line (both scans; crops_676_680/w678_simeq.png)",
    r"a display \[ A(X)\simeq\Gtop^\bullet(X), \]", "other", "medium",
    fx(J(r"sans torsion", r"\[", r" A(X)\simeq\Gtop^\bullet(X),", r"\]", r"ayant comme"),
       r"sans torsion $A(X)\simeq\Gtop^\bullet(X)$, ayant comme"),
    "The print sets the isomorphism inline. " + FR + ": also a display.")

add(678, "'l'anneau Gr˙(X) apparait comme'",
    "apparait, without circumflex (both scans; crops_676_680/w678_appar.png)", "apparait comme",
    "misprint_in_print", "low", None,
    "Typing slip (the typist types circumflexes elsewhere: même, grâce, hâtivement). The TeX keeps the printed reading. "
    + FR + ": apparaît (silent correction).",
    corrected="apparaît comme", check_tex=True)

# ---------------------------------------------------------------- page 679
add(679, "first paragraph, 'que Gr˙(X) à un caractère covariant'",
    "à with a grave accent (both scans; crops_676_680/m679_a.png)",
    r"$\operatorname{Gr}^\bullet(X)$ à un caractère", "misprint_in_print", "high", None,
    "Typing error: the verb avoir. The TeX keeps the printed reading. " + FR + ": a (silent correction).",
    corrected=r"$\operatorname{Gr}^\bullet(X)$ a un caractère", check_tex=True)

add(679, "'tel que cℓ˙(Y)∈K˙(X) ne soit pas dans Filt^i(X)'",
    "cℓ with the raised typed dot, the same dot as in K˙(X) (both scans; crops_676_680/m679_clY.png, w690_small.png)",
    r"\cl^i(Y)\in K^\bullet(X)", "symbol", "high",
    fx(r"\cl^i(Y)\in K^\bullet(X)", r"\cl^\bullet(Y)\in K^\bullet(X)"),
    r"Written \bullet like the raised dot of K and Gr (as p. 673, cl^i(O_Y) -> \cl^\bullet). This settles "
    r"SGA-SRC-001452 (left to the scan check): the print has cℓ˙(Y), neither cl^i nor cl'. " + FR + r": \cl'(Y) (its "
    "prime is the raised dot).")

add(679, "'ne soit pas dans Filt^i(X), où i = codim(Y,X)'",
    "Filt (both scans)", r"$\Fil^i(X)$ (\Fil is \operatorname{Fil}: prints Fil)", "word", "high",
    fx(r"pas dans $\Fil^i(X)$, où", r"pas dans $\operatorname{Filt}^i(X)$, où"),
    r"The print types Filt; as the Filt fixes of pp. 15, 16 and 673 (\Filt is not usable, findings_671_675.json). One "
    "of seven Filt entries on this page.")

add(679, "'de sorte que Filt^{i+1}(X) = Filt^{i+1}_top(X)'",
    "Filt, twice (both scans)", r"$\Fil^{i+1}(X)=\Fil_{\mathrm{top}}^{i+1}(X)$", "word", "high",
    fx(r"$\Fil^{i+1}(X)=\Fil_{\mathrm{top}}^{i+1}(X)$. Si", r"$\operatorname{Filt}^{i+1}(X)=\operatorname{Filt}_{\mathrm{top}}^{i+1}(X)$. Si"),
    "As above.")

add(679, "'on en conclut que cℓ˙(Y')∈K˙(X')'",
    "cℓ with the raised dot (both scans; crops_676_680/m679_clYp.png)", r"\cl(Y')\in K^\bullet(X')", "symbol", "high",
    fx(r"\cl(Y')\in K^\bullet(X')", r"\cl^\bullet(Y')\in K^\bullet(X')"),
    r"The dot is missing in the TeX. " + FR + r": \cl'(Y').")

add(679, "'n'est pas dans Filt^i(X') (compte tenu'",
    "Filt (both scans)", r"$\Fil^i(X')$", "word", "high",
    fx(r"pas dans $\Fil^i(X')$ (compte", r"pas dans $\operatorname{Filt}^i(X')$ (compte"),
    "As above.")

add(679, "'son noyau est Im(K(Z)->K(X)) ⊂ Filt^{i+1}_top(X) = Filt^{i+1}_top(X) ).'",
    "Filt, twice (both scans; crops_676_680/m679_filt.png)",
    r"\subset\Fil_{\mathrm{top}}^{i+1}(X)=\Fil_{\mathrm{top}}^{i+1}(X)$)", "word", "high",
    fx(r"\subset\Fil_{\mathrm{top}}^{i+1}(X)=\Fil_{\mathrm{top}}^{i+1}(X)$)",
       r"\subset\operatorname{Filt}_{\mathrm{top}}^{i+1}(X)=\operatorname{Filt}_{\mathrm{top}}^{i+1}(X)$)"),
    "As above; apply before the misprint entry that follows (its 'tex' is the text after this fix).")

add(679, "same place: '= Filt^{i+1}_top(X) )'",
    "the second Filt also carries the index top (both scans; crops_676_680/m679_filt.png, w690_small.png)",
    r"=\operatorname{Filt}_{\mathrm{top}}^{i+1}(X)$).",
    "misprint_in_print", "high", None,
    "Z, the singular set of Y, has codimension > i, so the kernel lies in Filt^{i+1}_top(X), which equals Filt^{i+1}(X) by "
    "the choice of Y one sentence earlier; the printed equality of Filt_top with itself says nothing. The TeX keeps the "
    "printed reading (the 'tex' is the text after the previous fix; before it: =\\Fil_{\\mathrm{top}}^{i+1}(X)$).). The print reads Im(K(Z)->K(X)) as our TeX does. " + FR + r": \Filt^{i+1}(X) (silent correction) "
    "and K'(Z)->K'(X) (SGA-SRC-001453; the print has plain K).",
    corrected=r"=\operatorname{Filt}^{i+1}(X)$).")

add(679, "'puisque f_*(1) n'est pas dans Filt^i(X').'",
    "Filt (both scans)", r"$\Fil^i(X')$.", "word", "high",
    fx(r"pas dans $\Fil^i(X')$.", r"pas dans $\operatorname{Filt}^i(X')$."),
    "As above.")

add(679, "4.7, 'le théorème de HODGKIN cité'",
    "HODGKIN in capitals (both scans)", "théorème de Hodgkin cité", "word", "high",
    fx("théorème de Hodgkin cité", "théorème de HODGKIN cité"),
    "As p. 678. " + FR + ": HODGKIN: the print agrees with it.")

add(679, "'l'idéal engendré par les cℓ˙(L) - 1'",
    "cℓ with the raised dot (not a prime), and L underlined (both scans; crops_676_680/m679_clL.png)", r"\cl'(L)-1",
    "symbol", "high", fx(r"\cl'(L)-1", r"\cl^\bullet(\underline{L})-1"),
    "Prime for the raised dot, and the underline of L lost (both in one edit). " + FR + r": \cl'(\underline L): the print "
    "agrees with it on the underline.")

add(679, "'où L parcourt les Modules inversibles'",
    "L underlined (both scans)", "où $L$ parcourt", "underline", "high",
    fx("où $L$ parcourt", r"où $\underline{L}$ parcourt"),
    FR + r": \underline L: the print agrees with it.")

add(679, "'associés aux représentations B -> G_m (qui donnent'",
    "G_m with a typed G, underlined (G̲_m), not double-struck (both scans; crops_676_680/m679_Gm.png)",
    r"$B\to\Gm$ (\Gm is \mathbb G_m)", "font", "low",
    fx(r"$B\to\Gm$ (qui", r"$B\to\underline{G}_m$ (qui"),
    r"The typist's underlined letter, as the underlined Q of p. 674 (\underline{Q}, findings_671_675.json): volume "
    "decision with SGA 7 II issue 61. Apply with the next entry or neither. " + FR + r": \Gm.")

add(679, "'définis par les représentations B -> G_m , donc'",
    "G̲_m, as above (both scans)", r"$B\to\Gm$", "font", "low",
    fx(r"$B\to\Gm$, donc", r"$B\to\underline{G}_m$, donc"),
    "As the previous entry.")

add(679, "last line, 'Cela montre que A(G) est réduit à A^o(X) = Z si et'",
    "A^o(X): X, not G (both scans)", r"réduit à $A^0(X)=\Z$", "misprint_in_print", "high", None,
    "A(G) is reduced to its degree-0 part A^0(G) = Z. The TeX keeps the printed reading; the corrected layer already "
    "reads A^0(G) (SGA-SRC-001454, applied).",
    corrected=r"réduit à $A^0(G)=\Z$", check_tex=True)

# ---------------------------------------------------------------- page 680
add(680, "first lines, 'produit de groupes Sℓ(n) et Sp(m)'",
    "Sℓ with the hand-drawn script ℓ (both scans; crops_676_680/m680_Sl.png)", r"\operatorname{Sl}(n)", "symbol", "high",
    fx(r"groupes $\operatorname{Sl}(n)$ et $\operatorname{Sp}(m)$. Donc", r"groupes $\operatorname{S\ell}(n)$ et $\operatorname{Sp}(m)$. Donc"),
    "As p. 678. " + FR + ": Sl (the print agrees with neither).")

add(680, "(4.9), the coefficient ring Z_ℓ",
    "a typed Z, underlined, with the hand-drawn ℓ (Z̲_ℓ), not double-struck (both scans; crops_676_680/m680_49.png, "
    "w680_49.png)", r"\Zell (= \mathbb Z_\ell)", "underline", "medium", None,
    r"Falls under the Z̲_ℓ convention entry of findings_671_675.json (p. 673); the asterisks of the same formula under "
    r"the H^* entry above (p. 678). " + FR + r": \underline{\Z}_\ell: the print agrees with it on the underline.")

add(680, "'il en serait de même pour (4.9)': 'ℓ coéfficient de torsion de G'",
    "coéfficient, with an acute accent (both scans; crops_676_680/m680_coeff.png)", "coéfficient",
    "misprint_in_print", "high", None,
    "Typing error. The TeX keeps the printed reading. " + FR + ": coefficient (silent correction).",
    corrected="coefficient", check_tex=True)

add(680, "'l'ordre du groupe fini A^+(G) = ⨿_{i⩾0} A^i(G)'",
    "the index reads i⩾0: the typed > with the slanted bar of ⩾ under it (both scans; crops_676_680/m680_Aplus.png, "
    "w691_small.png)", r"\coprod_{i\geq0}", "misprint_in_print", "medium", None,
    "A^+(G) is the part of positive degree: A^0(G) = Z (p. 679, 'A(G) est réduit à A^o = Z') is not finite, and A^+(G) "
    "is called 'le groupe fini'. The TeX keeps the printed reading. " + FR + r": \bigoplus_{i>0}, displayed (silent "
    "correction).",
    corrected=r"\coprod_{i>0}", check_tex=True)

add(680, "'dans le cas du groupe G = G_2 sur le corps C'",
    "G̲_2: the G underlined (both scans; crops_676_680/m680_G2.png)", "$G=G_2$", "underline", "high",
    fx("$G=G_2$", r"$G=\underline{G}_2$"),
    "Again in 'concernant G_2' below. " + FR + ": plain (the print agrees with neither).")

add(680, "'(4.10) n'est pas nul en degré > 0, de façon précise'",
    "a comma after 0 (both scans; crops_676_680/m680_degre.png)", r"degré $>0$; de façon", "punctuation", "high",
    fx(r"degré $>0$; de façon", r"degré $>0$, de façon"),
    "The TeX has a semicolon. " + FR + ": semicolon too.")

add(680, "'Le fait utilisé concernant G_2'",
    "G̲_2, underlined (both scans)", "concernant $G_2$", "underline", "high",
    fx("concernant $G_2$", r"concernant $\underline{G}_2$"),
    "As above.")

add(680, "last line, 'communiqué obligeamment par J.P. SERRE.'",
    "J.P. without hyphen, SERRE in capitals (typed in the later typeface; both scans; crops_676_680/m680_serre.png)",
    "J.-P. Serre", "word", "high", fx("obligeamment par J.-P. Serre", "obligeamment par J.P. SERRE"),
    FR + ": J.P. SERRE: the print agrees with it.")

# ---------------------------------------------------------------- checks
pages = {p: open(B + "\\page_%d.tex" % p, encoding="utf-8").read() for p in range(676, 681)}
main = open(MAIN, encoding="utf-8").read()
ok = True
for d in F:
    t = pages[d["page"]]
    if d["fix"]:
        old = d["fix"]["old"]
        n = t.count(old)
        if n != 1:
            ok = False
            print("FIX OLD COUNT", n, d["page"], repr(old))
        if "%%%%%%%%%%" in old:
            ok = False
            print("MARKER IN OLD", d["page"])
        nm = main.count(old)
        if nm != 1:
            print("  note: main.tex count", nm, d["page"], repr(old[:60]))
    if d["_check_tex"]:
        n = t.count(d["tex"])
        if n != 1:
            ok = False
            print("TEX COUNT", n, d["page"], repr(d["tex"]))
for d in F:
    d.pop("_check_tex")
with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    json.dump(F, f, ensure_ascii=False, indent=1)
print("written", len(F), "ok" if ok else "PROBLEMS")
from collections import Counter
c = Counter((d["page"], d["kind"] == "misprint_in_print") for d in F)
for p in range(676, 681):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
