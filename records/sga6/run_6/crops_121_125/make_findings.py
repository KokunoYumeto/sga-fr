"""Build findings_121_125.json for SGA 6 pp. 121-125: check that every fix's old occurs exactly once in its
page_NNN.tex, and that the fixes of a page still apply one after another in JSON order.
usage: python -I make_findings.py [--write]"""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
B = RUN / "b121_125"
OUT = RUN / "findings_121_125.json"


def F(page, where, scan, tex, kind, conf, old=None, new=None, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    return d


L = []
# ---------------------------------------------------------------- p. 121
L.append(F(121, "first line, 'localement cofinale dans (Qis/F).'",
           "'Qis/F' underlined inside the parentheses (both scans; crops_121_125/p121_top.png, w121_top.png): the "
           "fibred category of Scholie 4.4, underlined there too on p. 120 ('une catégorie (Qis/F) fibrée'), while "
           "its fibre (Qis/F_X)° is not",
           r"\((\Qis/F)\)", "underline", "high",
           r"\((\Qis/F)\)", r"\((\underline{\Qis/F})\)",
           r"Same reading as the p. 120 entry of findings_116_120.json ('une catégorie \((\Qis/F)\) fibrée', "
           r"applied)."))
L.append(F(121, "Notation 4.5, 'le faisceau sur S/X associé au préfaisceau'",
           "S̲ followed by '/X' lowered as an index, S̲_{/X} (both scans; crops_121_125/p121_SX.png, w121_SX.png)",
           r"\(S/X\) on the line", "formula", "high",
           r"sur \(S/X\)", r"sur \(S_{/X}\)",
           r"The TeX writes \(S_{/X}\) for the same notation elsewhere in Exposé I (main.tex lines 1868, 1871, 1898, "
           r"2477)."))
L.append(F(121, "Corollaire 4.6, statement before the display",
           "underlined by word groups: 'Soient', 'étant strictement parfait', 'La flèche canonique' (both scans)",
           r"no emphasis: the statement is in roman (Corollaire 4.3 on p. 120 has \emph)", "underline", "high",
           r"Soient \(E,F\in\Ob\Cpx(\mathcal C_S)\), \(E\) étant strictement parfait. La flèche canonique",
           r"\emph{Soient \(E,F\in\Ob\Cpx(\mathcal C_S)\), \(E\) étant strictement parfait. La flèche canonique}",
           "The display between the two parts is not underlined."))
L.append(F(121, "Corollaire 4.6, after the display: 'est un isomorphisme.'",
           "'est un isomorphisme' underlined, the full stop not (both scans)",
           "est un isomorphisme. in roman", "underline", "high",
           "est un isomorphisme.", r"\emph{est un isomorphisme}.",
           "Second part of the statement."))
L.append(F(121, "Preuve of 4.6, display 'Hom_{D(C_X)}(E_X,F_X) = lim_{(Qis/E_X)°} Hom_{K(C_X)}(· , F_X)'",
           "both Hom typed without underline, unlike the underlined Hom of the corollary's display just above (both "
           "scans; crops_121_125/p121_proofformula.png, p121_cor46formula.png)",
           r"\underline{\Hom} twice", "underline", "high",
           "\\underline{\\Hom}_{\\Dpx(\\mathcal C_X)}(E_X,F_X)\n  = \\varinjlim_{(\\Qis/E_X)^\\circ}"
           "\\underline{\\Hom}_{\\Kpx(\\mathcal C_X)}",
           "\\Hom_{\\Dpx(\\mathcal C_X)}(E_X,F_X)\n  = \\varinjlim_{(\\Qis/E_X)^\\circ}\\Hom_{\\Kpx(\\mathcal C_X)}",
           "The formula is the one for the Hom groups at each X (4.6 follows by passing to the associated sheaves); "
           "the print is right, the TeX adds the sheaf-Hom underline."))
L.append(F(121, "Définition 4.7, opening 'Soit F ∈ ob D(C_S) et soient a, b ∈ Z tels que a ≤ b. Nous dirons que F "
                "est d'amplitude ...'",
           "underlined: 'Soit', 'et soient', 'tels que', 'Nous dirons que', 'est d'; the defined term 'amplitude "
           "C_o-parfaite contenue dans l'intervalle [a,b]' is not underlined (both scans; crops_121_125/p121_def47.png)",
           "no emphasis: the definition is in roman", "underline", "high",
           r"Soit \(F\in\Ob\Dpx(\mathcal C_S)\) et soient \(a,b\in\mathbb Z\) tels que \(a\leq b\). Nous dirons que "
           r"\(F\) est d'amplitude",
           r"\emph{Soit \(F\in\Ob\Dpx(\mathcal C_S)\) et soient \(a,b\in\mathbb Z\) tels que \(a\leq b\). Nous dirons "
           r"que \(F\) est d'}amplitude",
           "The defined term stays in roman, as in Définitions 1.4.3, 2.1 and 2.3 (pp. 93-98)."))
L.append(F(121, "Définition 4.7, 'et nous écrirons'",
           "underlined (both scans)", "roman", "underline", "high",
           "et nous écrirons", r"\emph{et nous écrirons}"))
L.append(F(121, "Définition 4.7, display 'C_o-parf-amp(F) ⊂ [a,b] ,'",
           "'parf' in small letters (both scans)",
           r"\Parf, defined as \operatorname{Parf} (main.tex line 26): renders 'Parf' with a capital P",
           "formula", "high",
           r"\mathcal C_0\text{-}\Parf\text{-}\amp(F)", r"\mathcal C_0\text{-}\mathrm{parf}\text{-}\amp(F)",
           r"The print capitalizes Parf only in the category name Parf(C,C_o); the index '-parf' and the name "
           r"'C_o-parf-amp' are small (pp. 122, 124 likewise). These five are the only \Parf of main.tex in such "
           r"places."))
L.append(F(121, "Définition 4.7, 'si l'ensemble des X au-dessus de S tels qu'il existe un quasi-isomorphisme'",
           "underlined: 'si l'ensemble des', 'au-dessus de', 'tels qu'il existe un quasi-isomorphisme' (both scans)",
           "roman", "underline", "high",
           r"si l'ensemble des \(X\) au-dessus de \(S\) tels qu'il existe un quasi-isomorphisme",
           r"\emph{si l'ensemble des \(X\) au-dessus de \(S\) tels qu'il existe un quasi-isomorphisme}",
           "Ends where p. 121 ends; the next words are printed on p. 122 (next entry)."))
L.append(F(121, "Définition 4.7, 'F' → F de C(C_X)' (printed at the top of p. 122)",
           "'de' underlined (p. 122, first line; both scans)",
           r"\(F'\to F\) de \(\Cpx(\mathcal C_X)\) in roman, at the end of page_121.tex", "underline", "high",
           r"\(F'\to F\) de \(\Cpx(\mathcal C_X)\)", r"\(F'\to F\) \emph{de} \(\Cpx(\mathcal C_X)\)",
           r"These words belong to p. 122 (marker entry there); the fix is given here, where the text stands now: "
           r"if the folio-122 marker is moved first, apply this edit on p. 122 (its old is then unique there). "
           r"The p. 122 anchor '\(F'\to F\)' works before or after this fix."))
L.append(F(121, "pp. 121-125: the site S̲",
           "S underlined where it names the site: p. 121 'une S̲-catégorie fibrée', 'X ∈ ob S̲'; p. 122 '(S̲,A) un "
           "topos annelé', 'dans D(S̲)'; p. 125 'Supposons que S̲ soit un site ponctuel' (both scans)",
           r"plain \(S\) throughout", "underline", "high",
           note="Convention of the transcription, as reported for pp. 84-85, 93-95 and 100: one decision for the "
                "exposé, not a page fix."))
# ---------------------------------------------------------------- p. 122
L.append(F(122, "start of page",
           "p. 122 begins 'F' → F de C(C_X) avec F' strictement C_o-parfait (2.1)'; p. 121 ends '... tels qu'il "
           "existe un quasi-isomorphisme' (both scans)",
           r"'\(F'\to F\) de \(\Cpx(\mathcal C_X)\)' ends the last line of page_121.tex (under the folio-121 "
           r"marker); page_122.tex begins 'avec \(F'\) strictement'",
           "marker", "high",
           note=r"""Page 122 really begins with '\(F'\to F\)'. python -I move_marker.py 6 122 "\(F'\to F\)" --before """
                r"(the last occurrence before the marker is this one, before or after the p. 121 entries; simulated "
                r"on both layers: '... un quasi-isomorphisme ', the marker, '\(F'\to F\) de \(\Cpx(\mathcal C_X)\)', "
                r"'avec \(F'\) strictement ...')."))
L.append(F(122, "Définition 4.7 continued, 'avec F' strictement C_o-parfait (2.1), et tel que F'^i = 0 pour i ∉ "
                "[a,b], est un raffinement de S.'",
           "underlined: 'avec', 'strictement', '-parfait', 'et tel que', 'pour', 'est un raffinement de'; 'S.' not "
           "(both scans)",
           "roman", "underline", "high",
           r"avec \(F'\) strictement \(\mathcal C_0\)-parfait (2.1), et tel que \(F'^i=0\) pour \(i\notin[a,b]\), "
           r"est un raffinement de",
           r"\emph{avec \(F'\) strictement \(\mathcal C_0\)-parfait (2.1), et tel que \(F'^i=0\) pour "
           r"\(i\notin[a,b]\), est un raffinement de}"))
L.append(F(122, "'(En vertu de (4.3) cette condition équivaut ... par \"isomorphisme de D(C_X)\".) Nous dirons que F "
                "est d'amplitude C_o-parfaite finie'",
           "the parenthesis is underlined by word groups ('En vertu de', 'cette condition équivaut à celle obtenue en "
           "remplaçant l'expression', 'quasi-isomorphisme de', 'par', 'isomorphisme de'), then 'Nous dirons que', "
           "'est d'; the defined term 'amplitude C_o-parfaite finie' is not (both scans; crops_121_125/w122_top.png)",
           "roman", "underline", "high",
           r"(En vertu de (4.3) cette condition équivaut à celle obtenue en remplaçant l'expression « "
           r"quasi-isomorphisme de \(\Cpx(\mathcal C_X)\) » par « isomorphisme de \(\Dpx(\mathcal C_X)\) ».) Nous "
           r"dirons que \(F\) est d'amplitude",
           r"(\emph{En vertu de (4.3) cette condition équivaut à celle obtenue en remplaçant l'expression « "
           r"quasi-isomorphisme de \(\Cpx(\mathcal C_X)\) » par « isomorphisme de \(\Dpx(\mathcal C_X)\) ».}) "
           r"\emph{Nous dirons que \(F\) est d'}amplitude"))
L.append(F(122, "'s'il existe des entiers a et b tels que'",
           "underlined: 's'il existe des entiers', 'et', 'tels que' (both scans)", "roman", "underline", "high",
           r"s'il existe des entiers \(a\) et \(b\) tels que",
           r"\emph{s'il existe des entiers \(a\) et \(b\) tels que}"))
L.append(F(122, "'tels que C_o-parf-amp(F) ⊂ [a,b].'",
           "'parf' in small letters (both scans)", r"\(\Parf\): renders 'Parf'", "formula", "high",
           r"\(\Parf\)-\(\amp(F)", r"\(\mathrm{parf}\)-\(\amp(F)",
           "As the display of p. 121."))
L.append(F(122, "'Nous dirons que F est C_o-parfait si F est localement d'amplitude C_o-parfaite finie (*).'",
           "underlined: 'Nous dirons que', 'est', 'si', 'est localement', 'd'amplitude', '-parfaite finie'; the defined "
           "term 'C_o-parfait' is not (both scans; crops_121_125/p122_lines5to7.png)",
           "roman", "underline", "high",
           r"Nous dirons que \(F\) est \(\mathcal C_0\)-parfait si \(F\) est localement d'amplitude "
           r"\(\mathcal C_0\)-parfaite finie\footnote",
           r"\emph{Nous dirons que \(F\) est} \(\mathcal C_0\)-parfait \emph{si \(F\) est localement d'amplitude "
           r"\(\mathcal C_0\)-parfaite finie}\footnote",
           "The footnote mark stays outside, as in the print."))
L.append(F(122, "Exemple 4.8, 'C la S-catégorie définie par U ↦ (catégorie des A_U-Modules à gauche), C_o la "
                "sous-S-catégorie'",
           "the map stands in the running text: 'U ⊢→ (catégorie des A_U -Modules à gauche), C_o la sous-S-catégorie "
           "définie' is one line (both scans)",
           r"a display \[ U\longmapsto (\text{catégorie des }A_U\text{-Modules à gauche}), \]", "other", "medium",
           "définie par\n\\[\n  U\\longmapsto (\\text{catégorie des }A_U\\text{-Modules à gauche}),\n\\]\n"
           "\\(\\mathcal C_0\\)",
           r"définie par \(U\longmapsto\) (catégorie des \(A_U\)-Modules à gauche), \(\mathcal C_0\)",
           "The TeX makes an inline formula a display (same kind of fix as pp. 21 and 80). The words in parentheses "
           "are set as text so that the line can break."))
L.append(F(122, "Exemple 4.8, 'définie par U ↦ (catégorie des A_U-Modules à gauche facteurs directs de Modules libres "
                "de type fini). Le couple'",
           "in the running text, over two lines (both scans)",
           r"a display \[ U\longmapsto (\text{catégorie des }A_U\text{-Modules à gauche facteurs directs de Modules "
           r"libres de type fini}). \]", "other", "medium",
           "définie par\n\\[\n  U\\longmapsto (\\text{catégorie des }A_U\\text{-Modules à gauche facteurs directs de "
           "Modules libres de type fini}).\n\\]\nLe couple",
           r"définie par \(U\longmapsto\) (catégorie des \(A_U\)-Modules à gauche facteurs directs de Modules libres "
           r"de type fini). Le couple",
           "As the entry before."))
L.append(F(122, "Notation 4.9, 'D(C)_{C_o-parf}'",
           "index '-parf' in small letters (both scans)", r"_{\mathcal C_0\text{-}\Parf}: renders 'Parf'",
           "formula", "high",
           r"\mathcal C_0\text{-}\Parf}", r"\mathcal C_0\text{-}\mathrm{parf}}",
           r"As p. 121; the following Parf(C,C_o) is capital in the print and stays \Parf."))
L.append(F(122, "Notation 4.9, 'nous écrirons D(_A S)_parf , ou Parf(_A S)'",
           "index 'parf' in small letters (both scans)", r"_{\Parf}: renders 'Parf'", "formula", "high",
           r"(_A S)_{\Parf}", r"(_A S)_{\mathrm{parf}}",
           "As the entry before; Parf(_A S) and Parf(S) are capital in the print."))
# ---------------------------------------------------------------- p. 123
L.append(F(123, "label 'Proposition 4.10'",
           "'Proposition 4.10' with no full stop after the number (both scans; crops_121_125/p123_label.png, "
           "w123_full.png); the other labels of pp. 121-125 have one",
           r"\textbf{Proposition 4.10.} (silently supplied)", "misprint_in_print", "high",
           r"\textbf{Proposition 4.10.}", r"\textbf{Proposition 4.10}",
           "The typist left out the label's full stop; the TeX silently supplies it (as Proposition 2.7, p. 100).",
           corrected=r"\textbf{Proposition 4.10.}"))
L.append(F(123, "Proposition 4.10, 'La catégorie Parf(C,C_o) est une sous-S-catégorie triangulée de D(C) (1.1.4). "
                "Le foncteur canonique'",
           "underlined: 'La catégorie Parf', 'est une sous-', '-catégorie triangulée', 'de', 'Le foncteur canonique' "
           "(both scans)",
           "no emphasis: the statement is in roman", "underline", "high",
           r"La catégorie \(\Parf(\mathcal C,\mathcal C_0)\) est une sous-\(S\)-catégorie triangulée de "
           r"\(\Dpx(\mathcal C)\) (1.1.4). Le foncteur canonique",
           r"\emph{La catégorie \(\Parf(\mathcal C,\mathcal C_0)\) est une sous-\(S\)-catégorie triangulée de "
           r"\(\Dpx(\mathcal C)\) (1.1.4). Le foncteur canonique}"))
L.append(F(123, "Proposition 4.10, 'induit une S-équivalence sur les champs associés ([G] II 2.2.4), ce qui signifie :'",
           "underlined: 'induit une', '-équivalence sur les champs associés', 'ce qui', 'signifie' (both scans); the "
           "line '(resp. Tr(K^b(C_o)) → Tr(Parf(C,C_o)) (1.1.3))' before it is not underlined",
           "roman", "underline", "high",
           r"induit une \(S\)-équivalence sur les champs associés ([G] II 2.2.4), ce qui signifie",
           r"\emph{induit une \(S\)-équivalence sur les champs associés ([G] II 2.2.4), ce qui signifie}"))
L.append(F(123, "Proposition 4.10 (i), 'pour tout X ∈ ob S et tous'",
           "underlined: 'pour tout', 'et tous' (both scans)",
           "roman", "underline", "high",
           r"pour tout \(X\in\Ob S\) et tous", r"\emph{pour tout \(X\in\Ob S\) et tous}",
           "The rest of the line 'E,F ∈ ob K^b(C_oX) (resp. Tr(K^b(C_oX))),' is not underlined."))
L.append(F(123, "Proposition 4.10 (i), 'la flèche canonique'",
           "underlined (both scans)", "roman", "underline", "high",
           "la flèche canonique", r"\emph{la flèche canonique}"))
L.append(F(123, "Proposition 4.10 (i), 'E,F ∈ ob K^b(C_oX)'",
           "C̲ with the indices o and X side by side, no comma (both scans)",
           r"\mathcal C_{0,X}", "punctuation", "high",
           r"\Ob\Kpx^b(\mathcal C_{0,X})", r"\Ob\Kpx^b(\mathcal C_{0X})",
           "As pp. 91-92, 95 and 100: the TeX adds a comma between the indices."))
L.append(F(123, "Proposition 4.10 (i), '(resp. Tr(K^b(C_oX)))'",
           "C̲_oX, no comma (both scans)", r"\mathcal C_{0,X}", "punctuation", "high",
           r"\Tr(\Kpx^b(\mathcal C_{0,X}))", r"\Tr(\Kpx^b(\mathcal C_{0X}))",
           "As the entry before."))
L.append(F(123, "Proposition 4.10 (i), display 'Hom_{K^b(C_o)}(E,F) → Hom_{D(C)}(E,F)'",
           "both Hom underlined, the sheaf Hom of 4.5 (both scans)",
           r"\Hom without underline", "underline", "high",
           "\\Hom_{\\Kpx^b(\\mathcal C_0)}(E,F)\n  \\longrightarrow\n  \\Hom_{\\Dpx(\\mathcal C)}(E,F)",
           "\\underline{\\Hom}_{\\Kpx^b(\\mathcal C_0)}(E,F)\n  \\longrightarrow\n  "
           "\\underline{\\Hom}_{\\Dpx(\\mathcal C)}(E,F)",
           "Assertion (i) is the sheaf statement ('un cas particulier de (4.6)', whose display has the underlined Hom)."))
L.append(F(123, "Proposition 4.10 (i), '(resp. Hom_{Tr(K^b(C_o))}(E,F) → Hom_{Tr(D(C))}(E,F) )'",
           "'resp.' underlined and both Hom underlined (both scans)",
           r"(resp. \(\Hom_{\Tr(...)}(E,F)\to\Hom_{\Tr(...)}(E,F)\)) without underlines", "underline", "high",
           r"(resp. \(\Hom_{\Tr(\Kpx^b(\mathcal C_0))}(E,F)\to\Hom_{\Tr(\Dpx(\mathcal C))}(E,F)\))",
           r"(\emph{resp.} \(\underline{\Hom}_{\Tr(\Kpx^b(\mathcal C_0))}(E,F)\to"
           r"\underline{\Hom}_{\Tr(\Dpx(\mathcal C))}(E,F)\))",
           "Layout, not given as a fix: the print sets this formula as a display aligned under the one above, with "
           "'(resp.' in the margin and ')' after it; the TeX has it inline."))
L.append(F(123, "Proposition 4.10 (i), 'est un isomorphisme, et'",
           "underlined (both scans)", "roman", "underline", "high",
           "est un isomorphisme, et", r"\emph{est un isomorphisme, et}"))
L.append(F(123, "Proposition 4.10 (ii), 'tout objet de Parf(C,C_o) (resp. ...) est localement isomorphe dans D(C) "
                "(resp.'",
           "underlined: 'tout objet de Parf', 'est localement isomorphe', 'dans', the second 'resp.' (both scans; "
           "crops_121_125/p123_ii_start.png, p123_ii_end.png)",
           "roman", "underline", "high",
           r"tout objet de \(\Parf(\mathcal C,\mathcal C_0)\) (resp. \(\Tr(\Parf(\mathcal C,\mathcal C_0))\)) est "
           r"localement isomorphe dans \(\Dpx(\mathcal C)\) (resp.",
           r"\emph{tout objet de \(\Parf(\mathcal C,\mathcal C_0)\) (resp. \(\Tr(\Parf(\mathcal C,\mathcal C_0))\)) "
           r"est localement isomorphe dans \(\Dpx(\mathcal C)\) (resp.}",
           "The emphasis ends after 'resp.': 'Tr(D(C))' that follows is not underlined. Independent of the misprint "
           "entries below (disjoint texts)."))
L.append(F(123, "Proposition 4.10 (ii), 'à un objet de K^b(C_o) (resp.'",
           "underlined: 'à un objet de', 'resp.'; the final 'Tr(K^b(C_o)).' is not (both scans)",
           "roman", "underline", "high",
           r"à un objet de \(\Kpx^b(\mathcal C_0)\) (resp.", r"\emph{à un objet de \(\Kpx^b(\mathcal C_0)\) (resp.}",
           "Independent of the misprint entries below (disjoint texts)."))
L.append(F(123, "Proposition 4.10 (ii), 'dans D(C) (resp. Tr(D(C)) à un objet de'",
           "'(resp. Tr(D(C))': three opening and two closing parentheses (both scans; crops_121_125/p123_ii_end.png)",
           r"(resp. \(\Tr(\Dpx(\mathcal C))\)): closed (silent correction)", "misprint_in_print", "high",
           r"\(\Tr(\Dpx(\mathcal C))\))", r"\(\Tr(\Dpx(\mathcal C))\)",
           "The typist left out the parenthesis that closes '(resp.'.",
           corrected=r"\(\Tr(\Dpx(\mathcal C))\))"))
L.append(F(123, "Proposition 4.10 (ii), end '(resp. Tr(K^b(C_o)).'",
           "'(resp. Tr(K^b(C_o)).': three opening and two closing parentheses (both scans)",
           r"(resp. \(\Tr(\Kpx^b(\mathcal C_0))\)).: closed (silent correction)", "misprint_in_print", "high",
           r"\Kpx^b(\mathcal C_0))\))", r"\Kpx^b(\mathcal C_0))\)",
           "As the entry before.",
           corrected=r"\Kpx^b(\mathcal C_0))\))"))
# ---------------------------------------------------------------- p. 124
L.append(F(124, "start of page",
           "p. 124 begins 'est parfait. Quitte à localiser'; p. 123 ends '... tel que E et F soient parfaits, alors G' "
           "(both scans)",
           r"'est' ends the last line of page_123.tex ('alors \(G\) est', under the folio-123 marker); page_124.tex "
           r"begins 'parfait.'",
           "marker", "high",
           note=r"""Page 124 really begins with 'est'. python -I move_marker.py 6 124 "est" --before (the last 'est' """
                r"before the marker is this one; simulated on both layers: '... alors \(G\) ', the marker, 'est', "
                r"'parfait. Quitte ...')."))
L.append(F(124, "'Soient donc X ∈ ob S, et E = (E_1 → E_2 → E_3 → E_1), F = (F_1 → F_2 → F_3 → F_1) des triangles "
                "distingués'",
           "both triangles stand in the running text ('X ∈ ob S, et E = (...), F = (F_1 → F_2 →' on one line, 'F_3 → "
           "F_1) des triangles distingués de ...' on the next; both scans)",
           r"a display \[ E=(...), \quad F=(...) \]", "other", "medium",
           "et\n\\[\nE=(E_1\\xrightarrow{a_1}E_2\\xrightarrow{a_2}E_3\\xrightarrow[+1]{a_3}E_1),\n\\quad\n"
           "F=(F_1\\xrightarrow{b_1}F_2\\xrightarrow{b_2}F_3\\xrightarrow[+1]{b_3}F_1)\n\\]\ndes triangles",
           r"et \(E=(E_1\xrightarrow{a_1}E_2\xrightarrow{a_2}E_3\xrightarrow[+1]{a_3}E_1)\), "
           r"\(F=(F_1\xrightarrow{b_1}F_2\xrightarrow{b_2}F_3\xrightarrow[+1]{b_3}F_1)\) des triangles",
           "The TeX makes inline formulas a display (as p. 122)."))
L.append(F(124, "'des triangles distingués de K^b(C_oX)'",
           "C̲_oX, no comma (both scans)", r"\mathcal C_{0,X}", "punctuation", "high",
           r"\Kpx^b(\mathcal C_{0,X})", r"\Kpx^b(\mathcal C_{0X})",
           "As p. 123."))
L.append(F(124, "display (**) 'Hom_{Tr(K^b(C_o))}(E,F) → Hom_{Tr(D(C))}(E,F)'",
           "both Hom underlined (both scans)", r"\Hom without underline", "underline", "high",
           "\\Hom_{\\Tr(\\Kpx^b(\\mathcal C_0))}(E,F)\n  \\longrightarrow\n  \\Hom_{\\Tr(\\Dpx(\\mathcal C))}(E,F)",
           "\\underline{\\Hom}_{\\Tr(\\Kpx^b(\\mathcal C_0))}(E,F)\n  \\longrightarrow\n  "
           "\\underline{\\Hom}_{\\Tr(\\Dpx(\\mathcal C))}(E,F)",
           "The sheaf map of 4.10 (i) resp., as on p. 123."))
L.append(F(124, "Remarque 4.10.1, 'D*(C)_{C_o-parf} = D*(C) ∩ Parf(C,C_o)'",
           "index '-parf' in small letters (both scans; crops_121_125/p124_rem4101.png)",
           r"_{\mathcal C_0\text{-}\Parf}: renders 'Parf'", "formula", "high",
           r"\mathcal C_0\text{-}\Parf}", r"\mathcal C_0\text{-}\mathrm{parf}}",
           "As pp. 121-122; the Parf(C,C_o) after the ∩ is capital in the print."))
# ---------------------------------------------------------------- p. 125
L.append(F(125, "start of page",
           "p. 125 begins with 'Soit' and the triangle E → F → G (+1); p. 124 ends 'E[n] est d'amplitude parfaite "
           "contenue dans [a-n,b-n].' (both scans)",
           "the line 'Soit' and the tikzcd triangle are the last lines of page_124.tex (under the folio-124 marker); "
           "page_125.tex begins 'un' 'triangle distingué'",
           "marker", "high",
           note=r"""Page 125 really begins with 'Soit'. python -I move_marker.py 6 125 "Soit" --before (the last """
                r"'Soit' before the marker is that line; simulated on both layers: '... \([a-n,b-n]\).', a blank line, "
                r"the marker, 'Soit', the diagram, 'un', 'triangle distingué ...')."))
L.append(F(125, "'De (4.10) on déduit aussitôt le'",
           "no colon after 'le' (both scans; crops_121_125/p125_De410.png, w125_full.png)",
           "De (4.10) on déduit aussitôt le :", "punctuation", "high",
           "aussitôt le :", "aussitôt le",
           "The TeX adds the colon."))
L.append(F(125, "Corollaire 4.12, statement before the displays",
           "underlined: 'Supposons que', 'soit un site ponctuel', 'Pour que', 'soit d'amplitude parfaite', 'rel', "
           "'contenue dans', 'il faut et il suffit qu'il existe un quasi-isomorphisme', 'avec', 'strictement parfait "
           "et tel que', 'pour', 'Les foncteurs canoniques' (both scans)",
           "no emphasis: the statement is in roman", "underline", "high",
           r"Supposons que \(S\) soit un site ponctuel. Pour que \(F\in\Ob\Dpx(\mathcal C)\) soit d'amplitude "
           r"parfaite (rel.\ à \(\mathcal C_0\)) contenue dans \([a,b]\), il faut et il suffit qu'il existe un "
           r"quasi-isomorphisme \(F'\to F\), avec \(F'\) strictement parfait et tel que \(F'^i=0\) pour "
           r"\(i\notin[a,b]\). Les foncteurs canoniques",
           r"\emph{Supposons que \(S\) soit un site ponctuel. Pour que \(F\in\Ob\Dpx(\mathcal C)\) soit d'amplitude "
           r"parfaite (rel.\ à \(\mathcal C_0\)) contenue dans \([a,b]\), il faut et il suffit qu'il existe un "
           r"quasi-isomorphisme \(F'\to F\), avec \(F'\) strictement parfait et tel que \(F'^i=0\) pour "
           r"\(i\notin[a,b]\). Les foncteurs canoniques}"))
L.append(F(125, "Corollaire 4.12, 'et' between the two displays",
           "underlined (both scans)", "roman", "underline", "high",
           "\\]\net\n\\[", "\\]\n\\emph{et}\n\\["))
L.append(F(125, "Corollaire 4.12, 'sont des équivalences de catégories.'",
           "underlined, the full stop not (both scans)", "roman", "underline", "high",
           "sont des équivalences de catégories.", r"\emph{sont des équivalences de catégories}."))

# ---------------------------------------------------------------- checks
ok = True
texts = {p: (B / f"page_{p:03d}.tex").read_text(encoding="utf-8") for p in range(121, 126)}
work = dict(texts)
for i, f in enumerate(L):
    fx = f["fix"]
    if fx is None:
        continue
    p = f["page"]
    n0 = texts[p].count(fx["old"])
    if "%%%%%%%%%%" in fx["old"]:
        print("MARKER IN OLD", i, p)
        ok = False
    seq = work[p].count(fx["old"])
    if n0 != 1:
        print(f"[{i}] p.{p} old occurs {n0} times in the original page file: {fx['old'][:60]!r}")
        if not (n0 == 0 and seq == 1):
            ok = False
    if seq != 1:
        print(f"[{i}] p.{p} old occurs {seq} times after the earlier fixes: {fx['old'][:60]!r}")
        ok = False
    else:
        work[p] = work[p].replace(fx["old"], fx["new"])
print("entries:", len(L), "checks ok:", ok)
# pairwise order independence: after applying fix j alone, fix i must still occur exactly once
dep = []
for i, fi in enumerate(L):
    for j, fj in enumerate(L):
        if i == j or not fi["fix"] or not fj["fix"] or fi["page"] != fj["page"]:
            continue
        t = texts[fi["page"]]
        if t.count(fj["fix"]["old"]) != 1:
            continue
        t = t.replace(fj["fix"]["old"], fj["fix"]["new"])
        if t.count(fi["fix"]["old"]) != 1:
            dep.append((i, j))
print("order dependencies (i fails after j):", dep)
for p in range(121, 126):
    n = [f for f in L if f["page"] == p]
    print(p, "normal", sum(f["kind"] != "misprint_in_print" for f in n), "misprint",
          sum(f["kind"] == "misprint_in_print" for f in n))
(HERE / "applied").mkdir(exist_ok=True)
for p, t in work.items():
    (HERE / "applied" / f"page_{p:03d}.tex").write_text(t, encoding="utf-8", newline="\n")
if "--write" in sys.argv and ok:
    OUT.write_text(json.dumps(L, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    print("written", OUT)
