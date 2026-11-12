"""Write findings_181_185.json (SGA 6, pp. 181-185) from the entries below."""
import json

OUT = r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\findings_181_185.json"
NL = "\n"

F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": confidence, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- p. 181
add(181, "start of page",
    "p. 181 begins 'où Lib(A) désigne la catégorie des A-modules libres de type fini et (*)'; p. 180 ends with the "
    "display K⁻(Lib(S)) --(*)--> K⁻(Lib(A)) --(**)--> D(A) (both scans; OCR of p. 181)",
    r"'où $\Lib(A)$' is the last line of page_180.tex (under the folio-180 marker); page_181.tex begins 'désigne la "
    r"catégorie'",
    "marker", "high", None,
    r"Page 181 really begins with 'où $\Lib(A)$'. Already done in main.tex: both layers now have the folio-181 "
    r"marker above that line (the snapshot page_181.tex predates the move; checked at the end of this check with "
    r"crops_181_185/sim_markers.py and chk_main.py: the live span differs from the snapshot only by this line). "
    r"Nothing to do: python -I move_marker.py 6 181 'où $\Lib(A)$' --before now reports 'anchor not found' and "
    r"changes nothing.")

add(181, "Preuve of Lemme 2.4.4, 'avec A = Coh(S), B = Mod(S), φ : A → B'",
    "plain typed capitals A and B, neither underlined nor script (both scans; crops_181_185/p181_AB.png, w181_AB.png)",
    r"$\mathcal A=\Coh(S)$, $\mathcal B=\Mod(S)$, $\varphi:\mathcal A\to\mathcal B$",
    "font", "high",
    {"old": r"$\mathcal A=\Coh(S)$, $\mathcal B=\Mod(S)$, $\varphi:\mathcal A\to\mathcal B$",
     "new": r"$A=\Coh(S)$, $B=\Mod(S)$, $\varphi:A\to B$"},
    r"The cited Lemme 2.1.3 prints the same plain A and B; its statement on p. 165 was fixed the same way "
    r"(findings_161_165.json, applied: 'Soient $A$ et $B$'), pp. 166-167 are a convention entry of "
    r"findings_166_170.json.")

add(181, "Proposition 2.4.5 a), 'En outre le foncteur RΓ_S : D⁺(S) → D⁺(A)'",
    "R with a double underline, R̳Γ_S (both scans; crops_181_185/p181_RGamma.png)",
    r"$R\Gamma_S:\mathrm D^+(S)\to\mathrm D^+(A)$ (plain R)",
    "font", "high",
    {"old": r"le foncteur $R\Gamma_S:", "new": r"le foncteur $\mathbb R\Gamma_S:"},
    r"The typist's double underline of the derived functor; same form as the applied p. 175 entry "
    r"($\mathbb R\Gamma_S$, findings_171_175.json) and the p. 176 diagram entries; the TeX also writes the same "
    r"double underline as \mathbb under Z (p. 182) and R^n (p. 184). Five places on pp. 181-182.")

add(181, "Proposition 2.4.5 a), display 'RΓ_S = D^b(S)_coh → D⁺(A) ,'",
    "R̳Γ_S: R with a double underline (both scans; crops_181_185/p181_RGamma.png)",
    r"R\Gamma_S=\mathrm D^b(S)_{\coh}\longrightarrow\mathrm D^+(A), (plain R)",
    "font", "high",
    {"old": r"R\Gamma_S=\mathrm D^b", "new": r"\mathbb R\Gamma_S=\mathrm D^b"},
    "As the previous entry. Listed before the misprint entry for the same display (that one has no fix).")

add(181, "Proposition 2.4.5 a), display 'RΓ_S = D^b(S)_coh → D⁺(A) ,'",
    "an equals sign between RΓ_S and D^b(S)_coh (both scans; crops_181_185/p181_RGamma.png, w181_small.png)",
    r"R\Gamma_S=\mathrm D^b(S)_{\coh} (printed reading kept)",
    "misprint_in_print", "high", None,
    r"The display names the induced fully faithful functor, as in c) on p. 182 ('RΓ_S : D(S)_parf → D⁺(A)'): a "
    r"colon is meant. The TeX keeps the printed reading; the corrected layer already has ':'. The corrected reading "
    r"assumes the R entry above.",
    corrected=r"\mathbb R\Gamma_S:\mathrm D^b(S)_{\coh}\longrightarrow\mathrm D^+(A)")

add(181, "statements of Exposé II on pp. 181-185 (convention)",
    "the statements are underlined by word groups: Lemme 2.4.4 'Sous les hypothèses de', 'le foncteur canonique', "
    "'est pleinement fidèle et a pour image essentielle' (p. 181); Proposition 2.4.5 a)-c) (pp. 181-182); "
    "Définition 2.4.7 and its two following sentences, where 'de Stein' is left out of the underline (p. 183); "
    "Proposition 2.4.8 and Lemme 2.4.8.1 (p. 184) (both scans)",
    r"all in roman; only the defined term of 2.4.7 is in \emph ('On appelle \emph{espace pseudo-analytique "
    r"complexe} tout espace annelé ...')",
    "underline", "high", None,
    r"Convention of the transcription, not a page fix, as reported for pp. 160-165 and 177-180 "
    r"(findings_156_160, 161_165, 176_180): the TeX sets Exposé II's statements in roman (pp. 166-170 were "
    r"itemized and applied, so main.tex now mixes both). One pass for the exposé (block or word-group form: the "
    r"pending decision of items 48/73). See the message.")

# ---------------------------------------------------------------- p. 182
add(182, "Proposition 2.4.5 c), 'En outre, le foncteur RΓ_S : D⁺(S) → D⁺(A)'",
    "R̳Γ_S: R with a double underline (both scans)",
    r"$R\Gamma_S:\mathrm D^+(S)\to\mathrm D^+(A)$ (plain R)",
    "font", "high",
    {"old": r"le foncteur $R\Gamma_S:", "new": r"le foncteur $\mathbb R\Gamma_S:"},
    "As p. 181.")

add(182, "Proposition 2.4.5 c), display 'RΓ_S : D(S)_parf → D⁺(A) ,'",
    "R̳Γ_S: R with a double underline (both scans)",
    r"R\Gamma_S:\mathrm D(S)_{\parf}\longrightarrow\mathrm D^+(A), (plain R)",
    "font", "high",
    {"old": r"R\Gamma_S:\mathrm D(S)", "new": r"\mathbb R\Gamma_S:\mathrm D(S)"},
    "As p. 181.")

add(182, "Preuve of 2.4.5 a), label of the last arrow of 'D^b(Coh(S)) → D^b(S)_coh --RΓ_S--> D(A) ,'",
    "R̳Γ_S over the arrow: R with a double underline (both scans)",
    r"\xrightarrow{R\Gamma_S} (plain R)",
    "font", "high",
    {"old": r"\xrightarrow{R\Gamma_S}", "new": r"\xrightarrow{\mathbb R\Gamma_S}"},
    "As p. 181. The arrow of the display above is labelled Γ_S without R in the print, as in the TeX.")

add(182, "Proposition 2.4.5 b), 'F tel que F^i = 0 pour i ∈ [m,n]'",
    "i ∈ [m,n]: the plain membership sign (both scans; crops_181_185/p182_Fi.png, w182_top.png)",
    r"pour $i\in[m,n]$ (printed reading kept)",
    "misprint_in_print", "high", None,
    r"F is to vanish outside [m,n] (it has F^i ∈ ob Lib(S) for i > m and F^m ∈ ob Loclib(S)): ∉ is meant. The TeX "
    r"keeps the printed reading; the corrected layer already has \notin.",
    corrected=r"pour $i\notin[m,n]$")

# ---------------------------------------------------------------- p. 183
add(183, "first sentence, 'on a alors E^m ∈ ob Loclib(S)), d'où l'assertion'",
    "Loclib(S)), with a second closing parenthesis that closes nothing (both scans)",
    r"$E^m\in\Ob\Loclib(S))$ (printed reading kept)",
    "misprint_in_print", "medium", None,
    "No parenthesis is open in the sentence. The TeX keeps the printed reading; the corrected layer already has "
    "one parenthesis.",
    corrected=r"$E^m\in\Ob\Loclib(S)$")

add(183, "Preuve of 2.4.5 c), 'on voit que le foncteur K^b(Loclib(S)) → D(S) induit par Γ_S'",
    "D(S) (both scans; crops_181_185/p183_DS.png, w183_mid.png)",
    r"$\mathrm K^b(\Loclib(S))\to\mathrm D(S)$ induit par $\Gamma_S$ (printed reading kept)",
    "misprint_in_print", "medium", None,
    r"A functor induced by Γ_S lands in D(A) (statement c): 'RΓ_S : D(S)_parf → D⁺(A), dont l'image essentielle est "
    r"D(A)_parf'; in (2.4.3 c)), whose argument is repeated here, Γ_S : D⁻(Coh(S)) → D(A)); with D(S) the sentence "
    r"repeats the one before it. The TeX keeps the printed reading; the corrected layer still has D(S).",
    corrected=r"$\mathrm K^b(\Loclib(S))\to\mathrm D(A)$")

add(183, "Preuve of 2.4.5 c), 'et a pour image essentielle D(S)_parf, et l'on achève'",
    "D(S)_parf (both scans)",
    r"a pour image essentielle $\mathrm D(S)_{\parf}$, et l'on achève (printed reading kept)",
    "misprint_in_print", "medium", None,
    "Same slip as the previous entry: the essential image of the functor induced by Γ_S is D(A)_parf, as stated in "
    "c). The TeX keeps the printed reading; the corrected layer still has D(S).",
    corrected=r"$\mathrm D(A)_{\parf}$")

add(183, "after Définition 2.4.7, 'On dit qu'un espace pseudo-analytique complexe est de Stein ...'",
    "'Le faisceau structural ... est donc cohérent.' and 'On dit qu'un espace pseudo-analytique complexe est de "
    "Stein si le topos correspondant l'est (2.4.1).' are two paragraphs, each with an indented first line (both "
    "scans)",
    "one paragraph: '... est donc cohérent. On dit qu'un espace ...'",
    "other", "high",
    {"old": "est donc cohérent. On dit", "new": "est donc cohérent." + NL + NL + "On dit"},
    "")

add(183, "macro block 'Exposé II continuation macros' at the end of page_183.tex (no text of this page)",
    "the print types 'ob' (small o) throughout Exposé II: pp. 181-183 'M ∈ ob Coh(S)', 'E ∈ ob D(S)', "
    "'E^m ∈ ob Loclib(S))'; the 20 \\Ob of pp. 187-198 that follow this block are all a typed 'ob' (OCR of each "
    "page: 'E ∈ ob Qcoh(S)', 'F ∈ ob Mod(S)', 'E ∈ ob D(Qcoh(S))')",
    r"\renewcommand{\Ob}{\operatorname{Ob}}: from here to the next \renewcommand{\Ob} (p. 221, Appendice II) \Ob "
    r"prints 'Ob'; up to here it printed 'ob' (the \renewcommand{\Ob}{\operatorname{ob}} of p. 159)",
    "word", "high",
    {"old": r"\renewcommand{\Ob}{\operatorname{Ob}}", "new": r"\renewcommand{\Ob}{\operatorname{ob}}"},
    r"One edit instead of 20 on pp. 187-198: per folio the TeX's count of \Ob equals the OCR's count of 'ob', and no "
    r"'Ob' (crops_181_185/ob_range.py). pp. 183-185 use no \Ob after the block. The macro counts as the TeX's own "
    r"text. See the message.")

# ---------------------------------------------------------------- p. 184
add(184, "footnote (1) of Proposition 2.4.8, 'il a été obtenu indépendamment par J. Frish [5]'",
    "J. Frish (both scans; crops_181_185/p184_fn.png, w184_bot.png)",
    r"J. Frish [5] (printed reading kept)",
    "misprint_in_print", "high", None,
    "The bibliography of the exposé prints 'Frisch, J., Fonctions analytiques sur un ensemble semi-analytique' (OCR "
    "of p. 220; main.tex has \\item Frisch, J.). The TeX keeps the printed reading here; the corrected layer too.",
    corrected="J. Frisch [5]")

add(184, "Preuve of Lemme 2.4.8.1, 'il existe un entier n_o tel (E_n)_s = (E_{n_o})_s'",
    "'tel' at the end of the line, '(E_n)_s = (E_{n_o})_s pour n ≥ n_o.' on the next: no 'que' (both scans)",
    r"il existe un entier $n_0$ tel $(E_n)_s=(E_{n_0})_s$ (printed reading kept)",
    "misprint_in_print", "medium", None,
    "The typist left out 'que'. The TeX keeps the printed reading; the corrected layer too.",
    corrected=r"tel que $(E_n)_s=(E_{n_0})_s$")

add(184, "Preuve of Lemme 2.4.8.1, display 'M = M_o ⊃ M_1 ⊃ ... ⊃ M_q = 0'",
    "three typed full stops on the baseline (both scans; crops_181_185/p184_filt.png)",
    r"M_1\supset\cdots\supset M_q",
    "symbol", "medium",
    {"old": r"M_1\supset\cdots\supset M_q", "new": r"M_1\supset\ldots\supset M_q"},
    r"\cdots sets the dots at mid-height (same kind of fix as pp. 49, 79, 80).")

add(184, "Preuve of Lemme 2.4.8.1, 'telle que M_i/M_{i+1} ≃ O_s/p_i , où p_i est un idéal premier de O_s'",
    "p_i twice: a plain typed p, not Fraktur and not underlined (both scans; crops_181_185/p184_pi_zoom.png)",
    r"\mathcal O_s/\mathfrak p_i$, où $\mathfrak p_i$",
    "font", "high",
    {"old": r"\mathcal O_s/\mathfrak p_i$, où $\mathfrak p_i$", "new": r"\mathcal O_s/p_i$, où $p_i$"},
    "The typescript has no Fraktur p on these pages: the prime ideals of O_s are a plain p (also p. 185 '(resp. "
    "p_i)'), the coherent Ideals of p. 185 an underlined p.")

# ---------------------------------------------------------------- p. 185
add(185, "start of page",
    "p. 184 ends 'on peut supposer, quitte à se loca-'; p. 185 begins 'liser au voisinage de s' (both scans; OCR of "
    "pp. 184-185)",
    "'quitte à se' ends page_184.tex; page_185.tex begins with the whole word 'localiser'",
    "marker", "high", None,
    "Page 185 really begins with 'liser' ('localiser' is divided at the page break). python -I "
    "marker_split_word.py 6 185 split loca liser (simulated on both layers of the present main.tex with "
    "crops_181_185/sim_markers.py: '... quitte à se', 'loca%', the marker, 'liser au voisinage de $s$, ...'). No "
    "other entry touches these lines.")

add(185, "first sentence, 'que les M_i (resp. p_i) sont les fibres en s'",
    "a plain typed p (both scans; crops_181_185/p185_pi1.png)",
    r"(resp. $\mathfrak p_i$) sont",
    "font", "high",
    {"old": r"(resp. $\mathfrak p_i$) sont", "new": r"(resp. $p_i$) sont"},
    "The prime ideals p_i of p. 184 (plain p there too).")

add(185, "first sentence, '(resp. Idéaux cohérents p_i) de F (resp. O_S)'",
    "p̲_i: the p underlined, as the typist underlines the sheaf letter O̲ (both scans; crops_181_185/p185_pi3.png, "
    "w185_top.png)",
    r"Idéaux cohérents $\mathfrak p_i$)",
    "font", "medium",
    {"old": r"Idéaux cohérents $\mathfrak p_i$)", "new": r"Idéaux cohérents $\underline{p}_i$)"},
    "The print tells the coherent Ideal p̲_i of O_S from the ideal p_i of O_s, its fibre; \\mathfrak p merges them. "
    "If the volume writes the typist's underlined sheaf letters otherwise (O̲ as \\mathcal O, pending), follow that "
    "form here.")

add(185, "display 'F = F_o ⊃ F_1 ⊃ ... ⊃ F_q = 0'",
    "three typed full stops on the baseline (both scans; crops_181_185/p185_filt.png)",
    r"F_1\supset\cdots\supset F_q",
    "symbol", "medium",
    {"old": r"F_1\supset\cdots\supset F_q", "new": r"F_1\supset\ldots\supset F_q"},
    "As p. 184.")

add(185, "'et F_i/F_{i+1} ≃ O_S/p_i .'",
    "p̲_i: the p underlined (the coherent Ideal) (both scans; crops_181_185/p185_quot2.png)",
    r"\mathcal O_S/\mathfrak p_i$",
    "font", "medium",
    {"old": r"\mathcal O_S/\mathfrak p_i$", "new": r"\mathcal O_S/\underline{p}_i$"},
    "As the entry for 'Idéaux cohérents'.")

add(185, "'tels que (E_n)_s = 0. Comme O_s est intègre'",
    "one paragraph: 'Comme O_s est' follows '(E_n)_s = 0.' on the same line (both scans; witness "
    "crops_181_185/w185_mid.png)",
    r"a new paragraph (blank line) before 'Comme $\mathcal O_s$ est intègre'",
    "other", "high",
    {"old": r"$(E_n)_s=0$." + NL + NL + r"Comme $\mathcal O_s$", "new": r"$(E_n)_s=0$. Comme $\mathcal O_s$"},
    "The TeX adds a paragraph break.")

add(185, "'quitte à se localiser en s, que S est réduit.'",
    "'réduit' underlined (both scans)",
    "que $S$ est réduit. (no emphasis)",
    "underline", "high",
    {"old": "que $S$ est réduit.", "new": r"que $S$ est \emph{réduit}."},
    r"The file writes underlined words as \emph on these pages.")

add(185, "'On sait (loc. cit.) que S est le spectre analytique ([10] II §3) d'une O_S-Algèbre finie Õ_S'",
    "S without tilde (both scans; crops_181_185/p185_spec.png, w185_mid.png)",
    r"que $S$ est le spectre analytique (printed reading kept)",
    "misprint_in_print", "medium", None,
    "The normalisation S̃ introduced in the sentence before is the analytic spectrum of the finite O_S-Algebra Õ_S "
    "(the next sentences use p : S̃ → S); the tilde is missing. The TeX keeps the printed reading; the corrected "
    "layer too.",
    corrected=r"que $\widetilde S$ est le spectre analytique")

add(185, "'Or on a (10 II §3 Prop.8)'",
    "(10 II §3 Prop.8): the reference number without its brackets, where the page has '([10] IV §3)', "
    "'([10] IV §4)', '([10] II §3)' (both scans)",
    r"(10 II \S3 Prop.8) (printed reading kept)",
    "misprint_in_print", "low", None,
    "Typing slip in the citation form. The TeX keeps the printed reading; the corrected layer too.",
    corrected=r"([10] II \S3 Prop.8)")

add(185, "'où p : S̃ → S est la projection canonique, et (E_n.Õ_S)~ l'Idéal de O_S̃'",
    "a wide tilde over the whole E_n.Õ_S (the Ideal on S̃ defined by E_n.Õ_S), as in the display above and in "
    "'(E_n.Õ_S)~|U = 0' below (both scans; crops_181_185/p185_ideal.png, p185_OS.png)",
    r"et $E_n\cdot\widetilde{\mathcal O}_S$ l'Idéal (no wide tilde)",
    "formula", "high",
    {"old": r"canonique, et $E_n\cdot\widetilde{\mathcal O}_S$",
     "new": r"canonique, et $\widetilde{E_n\cdot\widetilde{\mathcal O}_S}$"},
    "Without the tilde the sentence defines E_n.Õ_S by itself ('... défini canoniquement par E_n.Õ_S').")

add(185, "'l'Idéal de O_S̃ défini canoniquement par E_n.Õ_S'",
    "O_S̃: underlined O with index S, the tilde over the index S, right of the O (both scans; "
    "crops_181_185/p185_OS.png)",
    r"l'Idéal de $\widetilde{\mathcal O}_S$",
    "formula", "medium",
    {"old": r"l'Idéal de $\widetilde{\mathcal O}_S$", "new": r"l'Idéal de $\mathcal O_{\widetilde S}$"},
    "The structure sheaf of S̃ (the Ideal lives on S̃); everywhere else on the page Õ_S has its tilde over the O. "
    "Independent of the previous entry (disjoint texts).")

add(185, "'un voisinage ouvert V de s dans S̃ tel que (E_n.Õ_S)~|U = 0'",
    "|U (both scans; crops_181_185/p185_ideal.png)",
    r"\widetilde{E_n\cdot\widetilde{\mathcal O}_S}|U=0 (printed reading kept)",
    "misprint_in_print", "medium", None,
    "The neighbourhood just introduced is V (in S̃); U is the neighbourhood in S of the sentence 'Montrons qu'il "
    "existe un voisinage ouvert U'. The TeX keeps the printed reading; the corrected layer already has |V.",
    corrected=r"\widetilde{E_n\cdot\widetilde{\mathcal O}_S}|V=0")

add(185, "'ce qui nous ramène au cas où S est normal, ce que nous supposerons'",
    "'normal' underlined (both scans)",
    "où $S$ est normal, ce que (no emphasis)",
    "underline", "high",
    {"old": "où $S$ est normal, ce que", "new": r"où $S$ est \emph{normal}, ce que"},
    "")

add(185, "'ce que nous supposerons maintenant. Comme (E_n)_s = 0, l'immersion fermée'",
    "one paragraph: 'Comme (E_n)_s = 0' follows 'maintenant.' on the same line (both scans)",
    r"a new paragraph (blank line) before 'Comme $(E_n)_s=0$, l'immersion'",
    "other", "high",
    {"old": "supposerons maintenant." + NL + NL + "Comme", "new": "supposerons maintenant. Comme"},
    "The TeX adds a paragraph break.")

add(185, "'l'immersion fermée i_n : S_n → S définie par E_n est étale en s'",
    "'étale' underlined (both scans)",
    "est étale en $s$ (no emphasis)",
    "underline", "high",
    {"old": "est étale en $s$", "new": r"est \emph{étale} en $s$"},
    "The two later 'étale' of the page are not underlined, as in the TeX.")

add(185, "end of page, 'Il reste donc à établir le'",
    "p. 185 ends 'on a gagné. Il reste donc à établir le'; p. 186 begins with the heading 'Lemme 2.4.8.2. (cf. EGA IV "
    "18.10.3)' (both scans: witness pp. 185-186, crops_181_185/w185_bot.png, w186_top.png; OCR of pp. 185-186)",
    "Il reste donc à établir le lemme suivant :",
    "extra", "high",
    {"old": "établir le lemme suivant :", "new": "établir le"},
    "The words 'lemme suivant :' are printed nowhere: the sentence runs into the heading of the lemma at the top of "
    "p. 186. With them removed, the folio-186 marker stands right.")

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write("\n")
print(len(F), "entries written")
