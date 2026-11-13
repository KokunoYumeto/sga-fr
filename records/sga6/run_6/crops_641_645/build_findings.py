import json, sys, pathlib
sys.stdout.reconfigure(encoding='utf-8')
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b641_645"
OUT = RUN / "findings_641_645.json"
NL = "\n"
M643 = "%%%%%%%%%%  scan idx 656  |  folio 643  %%%%%%%%%%"
M646 = "%%%%%%%%%%  scan idx 659  |  folio 646  %%%%%%%%%%"

F = []
def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "confidence": conf, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)

# ---------------- page 641
add(641, "first isomorphism of the page, 'Hom_gr(mu_n, Pic_X/k) ~ H^1(X, Z/n Z); par conséquent'",
    "Hom underlined (the underline under Hom only, not under gr); the Hom_gr of the next line ('on a Hom_gr(mu_n,Pic_X/k) ~ H^1(X,Z/n Z).') is plain (both scans; crops_641_645/m641_hom.png, wit_641_half.png)",
    r"\(\Hom_{\mathrm{gr}}(\mu_n,\underline{\Pic}_{X/k})\simeq H^1(X,\mathbb Z/n\mathbb Z)\);",
    "underline", "high",
    {"old": r"groupes \(\Hom_{\mathrm{gr}}", "new": r"groupes \(\underline{\Hom}_{\mathrm{gr}}"},
    r"The print sets the sheaf Hom of the isomorphism of k-group schemes (underlined) against the group of k-points of the next line (plain). \Hom is \operatorname{Hom} (Exposé XIII macros).")
add(641, "same formula, 'H^1(X, Z/n Z); par conséquent'",
    "H underlined (the H of H^1); the H^1 of the next line is plain (both scans; crops_641_645/m641_hom.png, wit_641_half.png)",
    r"\simeq H^1(X,\mathbb Z/n\mathbb Z)\);",
    "underline", "high",
    {"old": r"\simeq H^1(X,\mathbb Z/n\mathbb Z)\);", "new": r"\simeq \underline{H}^1(X,\mathbb Z/n\mathbb Z)\);"},
    "As the entry above: the cohomology sheaf of the k-group scheme, against the plain H^1 of the second isomorphism.")
add(641, "Théorème 3.13 (iv), last words",
    "'... H_K^{(x)N} (x) L_K et H_K^{(x)N} (x) L_K^{-1} sont ample.' (both scans; wit_641_half.png)",
    r"sont ample.}",
    "misprint_in_print", "high", None,
    "Agreement slip of the print: the subject is the two sheaves H_K^{(x)N} (x) L_K and H_K^{(x)N} (x) L_K^{-1}. The diplomatic TeX keeps the printed reading; both layers of main.tex read 'ample'.",
    corrected=r"sont amples.")

# ---------------- page 642
add(642, "first paragraph, 'le polynôme en m et n, chi(L_t^{(x)m}(n)) ne dépend que de la composante connexe'",
    "no comma after chi(L_t^{(x)m}(n)) (both scans; crops_641_645/m642_chi.png, wit_642_half.png)",
    r"\(\chi(L_t^{\otimes m}(n))\), ne d\'epend",
    "punctuation", "high",
    {"old": r"\(\chi(L_t^{\otimes m}(n))\), ne", "new": r"\(\chi(L_t^{\otimes m}(n))\) ne"},
    "Comma added by the transcription.")
add(642, "third paragraph, first inequality '<[N.c_1(H_K)+c_1(L_K)].c_1(H_K)^{r-1}> > 0'",
    "N.c_1(H_K): a typed full stop between N and c_1(H_K) (both scans; crops_641_645/m642_l1a.png, w642_l1.png); the second inequality '<[N c_1(H_K)+c_1(L_K)]^2. c_1(H_K)^{r-2}> > 0' has none",
    r"\langle [N c_1(H_K)+c_1(L_K)]\cdot c_1(H_K)^{r-1}\rangle",
    "symbol", "high",
    {"old": r"\langle [N c_1(H_K)+c_1(L_K)]\cdot", "new": r"\langle [N\cdot c_1(H_K)+c_1(L_K)]\cdot"},
    r"The TeX drops the printed product dot; written \cdot, the file's form for the print's typed product dots. The second inequality is right without it. The tiny dot between the closing '>' and the '>' of both inequalities ('...>.>0', both scans) is much smaller than a full stop and carries no reading: not reported.")

# ---------------- page 643
add(643, "start of page (folio-643 marker)",
    "p. 643 begins '(i). D'autre part, (iii) implique (ii) grâce à 2.3 et 2.8.'; p. 642 ends '... est limitée en vertu de 2.11 ; ainsi (ii) implique' (both scans: b641_645/page_642_s4.png, page_643_s1.png; crops_641_645/wit_642_half.png, wit_643_half.png)",
    "'(i). D'' ends the last line of page_642.tex ('... ainsi (ii) implique (i). D'%', above the folio-643 marker); page_643.tex begins 'autre part,'",
    "marker", "high", None,
    "Page 643 really begins at '(i). D'autre part'. Exact fix in main.tex, both layers (diplomatic and current; the string occurs once per layer at the time of checking): replace "
    + r"'ainsi (ii) implique (i). D'%\n" + M643 + r"\nautre part,'"
    + " by " + r"'ainsi (ii) implique\n" + M643 + r"\n(i). D'autre part,'"
    + ". The end of line after 'implique' gives the space; no word is split at this boundary.")
add(643, "heading '4. Théorèmes de finitude pour Pic^tau_X/S'",
    "'Théorèmes de finitude pour' underlined, and Pic underlined by a separate underline (both scans; wit_643_half.png)",
    r"\subsection*{4. Th\'eor\`emes de finitude pour $\Pic^\tau_{X/S}$}",
    "underline", "medium",
    {"old": r"pour $\Pic^\tau_{X/S}$}", "new": r"pour $\underline{\Pic}^\tau_{X/S}$}"},
    r"The title's own underline is accepted typesetting; the separate underline under Pic is the notation of the Picard functor, which the TeX writes \underline{\Pic}^\tau_{X/S} in the text (Lemme 4.3, p. 644). Medium: it can be read as part of the title underline.")
add(643, "4.1, 'il existe un k-schéma connexe Z, deux K-points z, z_o de Z'",
    "'un k-schéma connexe Z': small k, against the capital K of 'clos K et tout K-point t' and 'deux K-points' (both scans; crops_641_645/m643_kschema.png, wit_643_half.png)",
    r"il existe un \(k\)-sch\'ema connexe \(Z\)",
    "misprint_in_print", "medium", None,
    "4.1 has no field k (S is a scheme): Z is a scheme over the algebraically closed field K, with the two K-points z, z_0. The diplomatic TeX keeps the printed k; the current layer also reads k.",
    corrected=r"il existe un \(K\)-sch\'ema connexe \(Z\)")
add(643, "4.1, after '(resp. il existe un entier non-nul n tel que n.f(t) in G^o(K)).'",
    "'Il est évident que la formation de G^o (resp. G^tau) commute à' begins a new, indented paragraph (both scans; wit_643_half.png)",
    r"\(n.f(t)\in G^0(K)\)). Il est \'evident que ... (runs on in the paragraph of 4.1)",
    "other", "high",
    {"old": r"G^0(K)\)). Il est", "new": r"G^0(K)\))." + NL + NL + r"Il est"},
    "Missing paragraph break.")

# ---------------- page 644
add(644, "first sentence (proof of Lemme 4.2), 'on a déjà noté l'inclusion Phi(G'^tau) contains G^tau'",
    "Phi(G'^tau) > G^tau (superset sign), with no exponent -1 on Phi (both scans; crops_641_645/m644_phi.png, w644_top.png)",
    r"\(\Phi(G'^\tau)\supset G^\tau\)",
    "misprint_in_print", "high", None,
    r"Typing slip: the inclusion noted in 4.1 (a morphism G -> G' maps G^tau into G'^tau) is Phi^{-1}(G'^tau) > G^tau, one half of the lemma's Phi^{-1}(G'^tau) = G^tau; Phi(G'^tau) is not defined (G'^tau is a subfunctor of G'). The diplomatic TeX keeps the printed reading; the current layer already reads \Phi^{-1}(G'^\tau).",
    corrected=r"\(\Phi^{-1}(G'^\tau)\supset G^\tau\)")

# ---------------- page 645
add(645, "label of Proposition 4.5",
    "'Proposition 4.5. (Comportement fonctoriel).': full stop after 4.5 (both scans; crops_641_645/m645_prop45.png)",
    r"\textbf{Proposition 4.5 (Comportement fonctoriel).}",
    "punctuation", "high",
    {"old": r"\textbf{Proposition 4.5 (Comportement", "new": r"\textbf{Proposition 4.5. (Comportement"},
    "The stop after the number is missing (the bold label with its underlined name is accepted typesetting).")
add(645, "number of the projection formula 4.5.1",
    "'4.5.1.' typed at the left margin, without parentheses and with a full stop (both scans; crops_641_645/m645_451.png)",
    r"\tag{4.5.1} (prints '(4.5.1)')",
    "number", "medium",
    {"old": r"\tag{4.5.1}", "new": r"\tag*{4.5.1.}"},
    r"\tag adds parentheses and drops the stop; \tag* as for the printed tags of p. 255 (FIXLOG_6). The left position is layout. Exposé XIII prints its display numbers this way throughout (p. 627 '2.7.1.', p. 628 '2.7.2') and the TeX has \tag{...} for each: convention line in the message.")
add(645, "end of display 4.5.1",
    "no punctuation after '<c_1(L).Y>' (both scans; crops_641_645/m645_451.png)",
    r"=[k(Y'):k(Y)]\,\langle c_1(L)\cdot Y\rangle,",
    "punctuation", "high",
    {"old": r"\langle c_1(L)\cdot Y\rangle,", "new": r"\langle c_1(L)\cdot Y\rangle"},
    "Comma added at the end of the display.")
add(645, "paragraph 'Réciproquement, lorsque f est surjective, étant donnée une courbe intègre fermée Y'",
    "'lorsque f est surjective' (both scans)",
    r"lorsque \(f\) est surjective,",
    "misprint_in_print", "low", None,
    "Agreement with 'morphisme', as in 4.5 (ii) on the same page ('lorsque f est surjectif'). Low: 'f est surjective' (f as an application) is common usage. The diplomatic TeX keeps the printed reading; the current layer reads 'surjectif'.",
    corrected=r"lorsque \(f\) est surjectif,")
add(645, "label of Théorème 4.6",
    "'Théorème 4.6.(La caractérisation numérique de Pic^tau_X/k).': full stop after 4.6 (both scans; crops_641_645/m645_thm46.png)",
    r"\textbf{Th\'eor\`eme 4.6 (La caract\'erisation num\'erique de \(\Pic^\tau_{X/k}\)).}",
    "punctuation", "high",
    {"old": r"\textbf{Th\'eor\`eme 4.6 (La", "new": r"\textbf{Th\'eor\`eme 4.6. (La"},
    "As Proposition 4.5 (the print has no space before the parenthesis: spacing).")
add(645, "label of Théorème 4.6, 'Pic^tau_X/k'",
    "Pic underlined by its own underline, after the underline of 'La caractérisation numérique de' (both scans; crops_641_645/m645_thm46.png)",
    r"\(\Pic^\tau_{X/k}\)",
    "underline", "medium",
    {"old": r"num\'erique de \(\Pic^\tau_{X/k}\))", "new": r"num\'erique de \(\underline{\Pic}^\tau_{X/k}\))"},
    r"As the heading of § 4 (p. 643): the notation's underline (\underline{\Pic} in the text); the underline of the label words is accepted typesetting.")
add(645, "Théorème 4.6 (ii), display chi(F (x) L) = chi(F) (printed at the top of p. 646; its TeX stands above the folio-646 marker)",
    "chi(F (x) L) = chi(F) with no punctuation (both scans: b646_650/page_646_s1.png, crops_641_645/w646_top.png)",
    r"\chi(F\otimes L)=\chi(F);",
    "punctuation", "high",
    {"old": r"\chi(F\otimes L)=\chi(F);", "new": r"\chi(F\otimes L)=\chi(F)"},
    "Semicolon added at the end of the display. The display is printed on p. 646 (marker entry below); listed here because its TeX is in page_645.tex.")
add(645, "end of page (folio-646 marker)",
    "p. 645 ends '(ii) Pour tout faisceau cohérent F sur X, on a'; p. 646 begins with the display 'chi(F (x) L) = chi(F)', then '(iii) L est numériquement équivalent à 0.' (both scans: b641_645/page_645_s4.png, b646_650/page_646_s1.png, crops_641_645/w646_top.png)",
    r"the display \[ \chi(F\otimes L)=\chi(F); \] and the \item that prints '(iii)' stand above the folio-646 marker, at the end of page_645.tex",
    "marker", "high", None,
    "Page 646 really begins with the display chi(F (x) L) = chi(F). Exact fix in main.tex, both layers (diplomatic and current; the string occurs once per layer at the time of checking): replace "
    + r"'on a}\n\[\n  \chi(F\otimes L)=\chi(F);\n\]\n\item\n" + M646 + r"\n'"
    + " by " + r"'on a}\n" + M646 + r"\n\[\n  \chi(F\otimes L)=\chi(F);\n\]\n\item\n'"
    + ". If the semicolon entry above is applied first, read \\chi(F) without ';' in both strings. The same boundary is the start of p. 646 (batch 646-650): apply once.")

# ---------------- checks
ok = True
for i, f in enumerate(F):
    fx = f["fix"]
    if fx is None:
        continue
    txt = (B / ("page_%d.tex" % f["page"])).read_text(encoding="utf-8")
    n = txt.count(fx["old"])
    if n != 1 or "%%%%%%%%%%" in fx["old"]:
        ok = False
    print(i, f["page"], f["kind"], "old count", n)
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
print("written", OUT, len(F), "ok" if ok else "PROBLEM")
from collections import Counter
c = Counter((f["page"], f["kind"] == "misprint_in_print") for f in F)
for p in range(641, 646):
    print(p, c[(p, False)], "/", c[(p, True)])
