"""write_findings.py: build findings_531_535.json, check that every fix's old string occurs exactly once
in its page_NNN.tex (and that the new string differs), then write the JSON."""
import json, pathlib, sys
sys.stdout.reconfigure(encoding='utf-8')
HERE = pathlib.Path(__file__).resolve().parent
B = HERE.parent / "b531_535"
OUT = HERE.parent / "findings_531_535.json"

M532 = "%%%%%%%%%%  scan idx 545  |  folio 532  %%%%%%%%%%"
M534 = "%%%%%%%%%%  scan idx 547  |  folio 534  %%%%%%%%%%"
M536 = "%%%%%%%%%%  scan idx 549  |  folio 536  %%%%%%%%%%"


def nl(s):
    """write line breaks of a main.tex string as the two characters \\n, for the notes"""
    return s.replace("\n", "\\n")


F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    e = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "confidence": confidence, "fix": fix}
    if kind == "misprint_in_print":
        e["corrected"] = corrected
    e["note"] = note
    F.append(e)


# ---------------------------------------------------------------- page 531
add(531, "paragraph number 2.1",
    "'2.1.' with a full stop, run into 'Rappelons d'abord' (both scans)",
    r"\subsection*{2.1}", "punctuation", "high",
    {"old": r"\subsection*{2.1}", "new": r"\subsection*{2.1.}"},
    r"The printed paragraph number ends with a full stop, as 2.2. (p. 534) and 2.3. (p. 535) and as the "
    r"paragraph-number fixes of pp. 3-12, 394-402, 429-430, 449 and this exposé's 1.2., 1.3., 1.6. (already "
    r"with the stop in main.tex); the run-in heading set as its own paragraph is accepted.")

add(531, "Définition 2.1.1, 'pour toute suite x_1 ...,x_r (r ≥ 1)'",
    "x₁ ....,x_r: four typed dots right after x₁, no comma between x₁ and the dots, a comma before x_r "
    "(both scans; crops_531_535/c531_x1.png, w531_x1.png)",
    r"$x_1,\ldots,x_r$ ($r\geq1$)", "misprint_in_print", "medium",
    {"old": r"$x_1,\ldots,x_r$ ($r\geq1$)", "new": r"$x_1\ldots,x_r$ ($r\geq1$)"},
    r"Typing slip: every other list on pp. 531-535 has the comma after the first term (x_1, ...,x_r in the "
    r"next line of the definition). The TeX silently supplies it; the fix restores the printed reading.",
    corrected=r"$x_1,\ldots,x_r$ ($r\geq1$)")

add(531, "statements of pp. 531-535: Définition 2.1.1, Lemmes 2.1.2 and 2.1.3 (pp. 531-532), Lemme 2.1.4 "
         "(pp. 533-534), Proposition 2.2.1 (p. 535)",
    "underlined word group by word group, formulas and most punctuation not underlined (both scans). "
    "Déf. 2.1.1: 'Soit', 'une application d'un groupe abélien', 'dans un groupe abélien', 'On dit que', "
    "'est une', 's'il existe', 'pour toute suite', 'd'éléments de', 'une famille', 'presque tous nuls', "
    "'et satisfaisant à la condition suivante', ...; Lemme 2.1.3: 'Soit', 'une suite exacte de groupes "
    "abéliens telle que', 'est divisible par', 'un nombre premier', 'et', 'est un groupe de torsion', "
    "'Alors toute application polynôme', 'qui se factorise par', 'est constante'; Prop. 2.2.1: 'Pour tout "
    "schéma noethérien', 'et', 'pour tout', 'l'application composée', 'définie par', 'est une application "
    "polynôme de degré'",
    "statements set in roman (no underline, no \\emph)", "underline", "high", None,
    r"Same pattern as Exposé II (GLOBAL_ISSUES 82, pending volume decision) and Exposé IX (findings_501_505, "
    r"findings_506_510): not itemized. These pages have no \emph on defined terms and no category L.")

# ---------------------------------------------------------------- page 532
add(532, "start of page (folio-532 marker)",
    "p. 531 ends '... telle que G' est divisible par'; p. 532 begins 'un nombre premier p et G'' est un "
    "groupe de torsion.' (both scans; b531_535/page_531_s4.png, page_532_s1.png; "
    "crops_531_535/wit_531_small.png, wit_532_small.png)",
    "page_531.tex ends 'est divisible par un' above the folio-532 marker; page_532.tex begins "
    "'nombre premier $p$'",
    "marker", "high", None,
    "Page 532 really begins at 'un nombre premier'. Exact edit in main.tex, both layers (diplomatic lines "
    "13711-13713, current 13717-13719 at 16:2x on 13 Nov; main.tex is being edited, so use the string): "
    "replace '" + nl("divisible par un\n" + M532 + "\nnombre premier") + "' by '"
    + nl("divisible par\n" + M532 + "\nun nombre premier")
    + "' (old string once per layer; simulated in memory: crops_531_535/marker_check.py).")

add(532, "a), '(m ∈ Z , m ≠ 0)'",
    "a plain typed Z, without the hand stroke or the double underline of the other Z on pp. 531-532 "
    "(both scans; crops_531_535/c532_mZ.png, w532_mZ.png)",
    r"($m\in\mathbb Z$, $m\ne0$)", "font", "low",
    {"old": r"($m\in\mathbb Z$", "new": r"($m\in Z$"},
    r"The typist's plain letter, reported as the plain Q (volume decision with SGA 7 II issue 61; "
    r"GLOBAL_ISSUES 78 keeps \mathbb in SGA 7). Same on p. 534 'n_1,...,n_r ∈ Z :'.")

add(532, "display 'P_k(n) = P_{k+1}(pn)' after 'Pour tout n ∈ Z on a l'identité'",
    "no punctuation after P_{k+1}(pn); the next line is 'i.e.' (both scans)",
    r"P_k(n)=P_{k+1}(pn),", "punctuation", "high",
    {"old": r"P_k(n)=P_{k+1}(pn),", "new": r"P_k(n)=P_{k+1}(pn)"},
    "The TeX adds a comma at the end of the display.")

add(532, "'Démonstration :' (proof of Lemme 2.1.3)",
    "only the word 'Démonstration' is underlined; the colon after it is not (both scans)",
    r"\emph{Démonstration :}", "underline", "low",
    {"old": r"\emph{Démonstration :}", "new": r"\emph{Démonstration} :"},
    r"The colon stands inside the emphasis. The global rule keeps a comma or full stop inside the emphasis "
    r"(\emph{Preuve.}); if it covers the colon, drop this entry and the one of p. 534. main.tex has "
    r"\emph{Démonstration :} 8 times, all in Exposé X, and '\emph{Démonstration de} 1.1.2 :' with the colon "
    r"outside.")

# ---------------------------------------------------------------- page 533
add(533, "'Mais tout polynôme P : Q → Q'",
    "the first Q is a plain typed Q, the second is hand-struck (both scans; crops_531_535/w533_PQQ.png)",
    r"$P:\mathbb Q\to\mathbb Q$", "font", "low",
    {"old": r"$P:\mathbb Q\to\mathbb Q$", "new": r"$P:Q\to\mathbb Q$"},
    "The typist's plain Q (volume decision with SGA 7 II issue 61).")

add(533, "'on désigne par g_b : G' → Q l'application définie par'",
    "a typed Q with a single underline (one line, where the typed double-struck letters of these pages have "
    "two: Z on p. 531, N on p. 532); both scans (crops_531_535/c533_gbQ_z.png, w533_gbQ_z.png, "
    "c532_N_z.png)",
    r"$g_b:G'\to\mathbb Q$", "font", "low",
    {"old": r"g_b:G'\to\mathbb Q$", "new": r"g_b:G'\to\underline{Q}$"},
    "The typist's underlined Q; decide with the plain Q (SGA 7 II issue 61).")

add(533, "'d'où l'assertion que f soit constante sur les classes de G suivant G''.'",
    "G followed by a prime and a second, more weakly struck prime, then the full stop (both scans; "
    "crops_531_535/c533_Gpp.png, w533_Gpp.png)",
    r"suivant $G''$", "misprint_in_print", "medium", None,
    r"Wrong index: the classes are those of G modulo G' ('constante sur chaque classe de G suivant G'' two "
    r"sentences earlier; g_b is defined on G'). The TeX keeps the printed G'' in both layers.",
    corrected=r"suivant $G'$")

add(533, "'où h : G' → Q est une application polynôme'",
    "h : G' → Q with a single prime (both scans; crops_531_535/c533_hG.png, w533_vant_line.png)",
    r"$h:G'\to\mathbb Q$", "misprint_in_print", "high", None,
    r"Wrong index: f = h∘j with j : G → G'', so h is defined on G'' (and is constant because G'' is a "
    r"torsion group). The TeX keeps the printed G' in both layers.",
    corrected=r"$h:G''\to\mathbb Q$")

add(533, "'Mais par hypothèse C'' est un groupe de torsion'",
    "a typed C with the double prime (both scans; crops_531_535/c533_C.png, w533_C.png)",
    r"$C''$", "misprint_in_print", "high", None,
    r"Typing error for G'' (the hypothesis of Lemme 2.1.3). The diplomatic TeX keeps C''; the corrected "
    r"layer already has G''.",
    corrected=r"$G''$")

add(533, "display 'α : P → A → A ⊗_Z Q' after 'Alors l'application composée' (printed at the top of "
         "p. 534; its TeX stands in page_533.tex above the folio-534 marker)",
    "no punctuation after A ⊗_Z Q (both scans; b531_535/page_534_s1.png, crops_531_535/wit_534_small.png)",
    r"A\otimes_{\mathbb Z}\mathbb Q,", "punctuation", "high",
    {"old": r"A\otimes_{\mathbb Z}\mathbb Q,", "new": r"A\otimes_{\mathbb Z}\mathbb Q"},
    "The TeX adds a comma at the end of the display. Independent of the folio-534 marker move (entry of "
    "p. 534), which does not touch the display line.")

# ---------------------------------------------------------------- page 534
add(534, "start of page (folio-534 marker)",
    "p. 533 ends '... soit i : P → A l'injection naturelle. Alors l'application composée'; p. 534 begins "
    "with the display 'α : P → A → A ⊗_Z Q', then '(où j(x) = x ⊗ 1) est une application polynôme.' "
    "(both scans; b531_535/page_533_s4.png, page_534_s1.png; crops_531_535/wit_533_small.png, "
    "wit_534_small.png)",
    "page_533.tex ends with the display \\alpha and '(où $j(x)=x\\otimes1$) est une' above the folio-534 "
    "marker; page_534.tex begins 'application polynôme.'",
    "marker", "high", None,
    "Page 534 really begins at the display '" + nl("\\[\n\\alpha:P\\xrightarrow{i}A") + "...'. Exact edits "
    "in main.tex, both layers, applied together (diplomatic lines 13749-13755, current 13755-13761 at 16:2x "
    "on 13 Nov; use the strings): (1) replace '"
    + nl("(où $j(x)=x\\otimes1$) est une\n" + M534 + "\napplication polynôme.") + "' by '"
    + "(où $j(x)=x\\otimes1$) est une application polynôme." + "'; (2) replace '"
    + nl("Alors l'application composée\n\\[") + "' by '"
    + nl("Alors l'application composée\n" + M534 + "\n\\[")
    + "'. Each old string occurs once per layer, and neither touches the display line, so the comma fix "
    "of p. 533 applies before or after (simulated in memory: crops_531_535/marker_check.py).")

add(534, "proof of Lemme 2.1.4, 'Soit x_1,...,x_r une suite d'éléments de F avec x_i = 1+y_i'",
    "a typed F: top bar with its end serif, middle bar, no bowl (both scans; crops_531_535/c534_deP.png, "
    "w534_deP.png)",
    r"d'éléments de $F$ avec", "misprint_in_print", "medium", None,
    r"Typing error: the x_i = 1+y_i are elements of the group P of Lemme 2.1.4. The TeX keeps the printed F "
    r"in both layers.",
    corrected=r"d'éléments de $P$ avec")

add(534, "'pour tout n_1,...,n_r ∈ Z :'",
    "a plain typed Z, no hand stroke and no double underline (both scans; crops_531_535/c534_Z.png, "
    "w534_Z.png)",
    r"$n_1,\ldots,n_r\in\mathbb Z$ :", "font", "low",
    {"old": r"n_1,\ldots,n_r\in\mathbb Z$ :", "new": r"n_1,\ldots,n_r\in Z$ :"},
    "As p. 532 '(m ∈ Z': the typist's plain letter (volume decision with SGA 7 II issue 61).")

add(534, "'Démonstration :' (proof of Lemme 2.1.4)",
    "only the word 'Démonstration' is underlined; the colon is not (both scans)",
    r"\emph{Démonstration :}", "underline", "low",
    {"old": r"\emph{Démonstration :}", "new": r"\emph{Démonstration} :"},
    "As p. 532.")

add(534, "paragraph number 2.2",
    "'2.2.' with a full stop, run into 'Considérons maintenant' (both scans)",
    r"\subsection*{2.2}", "punctuation", "high",
    {"old": r"\subsection*{2.2}", "new": r"\subsection*{2.2.}"},
    "As 2.1 (p. 531).")

add(534, "K and cl with a raised dot, pp. 534-535 (7 places: K˙(X) five times on p. 534, cl˙(L) twice on "
         "p. 535)",
    "K˙(X), cl˙(L) with a raised filled dot (both scans; crops_531_535/c534_Theta.png); the lower dot of "
    "K.(X), cl.(F) is right as K_\\bullet, \\cl_\\bullet",
    r"K^\circ(X), \cl^\circ(L) (a raised circle)", "symbol", "high", None,
    r"Convention of the Exposé X TeX in §§ 1-7.6: K^\circ (54) and \cl^\circ (28) for the print's raised "
    r"dot, while its opening display has K^{\bullet} and § 7.7 on has K^\bullet (66); as reported for "
    r"Exposé IX (findings_501_505, findings_506_510); same fix as Exposés IV and VI on 10 Nov, one pass, not "
    r"itemized. Three examples: p. 534 'tout $x\in K^\circ(X)$' -> 'tout $x\in K^{\bullet}(X)$'; p. 534 "
    r"'j:K^\circ(X)\longrightarrow K^\circ(X)/\Filt^{j+1}(X)=A' -> "
    r"'j:K^{\bullet}(X)\longrightarrow K^{\bullet}(X)/\Filt^{j+1}(X)=A'; p. 535 '$j(\cl^\circ(L))$' -> "
    r"'$j(\cl^{\bullet}(L))$'.")

# ---------------------------------------------------------------- page 535
add(535, "paragraph number 2.3",
    "'2.3.' with a full stop, run into 'Si X est' (both scans; crops_531_535/c535_SiX.png, w535_SiX.png)",
    r"\subsection*{2.3}", "punctuation", "high",
    {"old": r"\subsection*{2.3}", "new": r"\subsection*{2.3.}"},
    "As 2.1 (p. 531). The small raised dot between 'X' and 'est' on this line (both scans) is a speck, "
    "not a typed stop.")

add(535, "end of page (folio-536 marker)",
    "p. 535 ends '... la caractéristique d'Euler-Poincaré χ (F) ∈ Z de F sur X . / De 2.2.1 on conclut "
    "immédiatement :'; p. 536 begins 'Proposition 2.3.1. Pour tout schéma propre X sur k, ...' (both "
    "scans; b531_535/page_535_s3.png; crops_531_535/wit_535_small.png, wit_536_small.png)",
    "page_535.tex ends 'la caractéristique d'Euler-'; the folio-536 marker stands inside the word, and "
    "'Poincaré $\\chi(F)\\in\\mathbb Z$ de $F$ sur $X$. De 2.2.1 on conclut immédiatement :' is in "
    "page_536.tex",
    "marker", "high", None,
    "Page 536 really begins at '\\textbf{Proposition 2.3.1.}'. Exact edits in main.tex, both layers, applied "
    "together (diplomatic lines 13797-13801, current 13803-13807 at 16:2x on 13 Nov; use the strings): "
    "(1) replace '" + nl("d'Euler-\n" + M536 + "\nPoincaré") + "' by 'd'Euler-Poincaré' (this also removes "
    "the space that the line end after 'Euler-' now puts into the word); (2) replace '"
    + nl("immédiatement :\n\n\\textbf{Proposition 2.3.1.}") + "' by '"
    + nl("immédiatement :\n\n" + M536 + "\n\\textbf{Proposition 2.3.1.}")
    + "'. Each old string occurs once per layer (simulated in memory: crops_531_535/marker_check.py).")

add(535, "the Modules L and F, p. 535 (8 places: 'inversible L', 'j(cl˙(L))', 'cl_P(L)', '(cl˙(L)y)', "
         "'cl.(F)', 'cohérent F', and, under the folio-536 marker, 'χ(F)' and 'de F sur X')",
    "L and F underlined in all eight places (both scans), as L_1, ..., L_n and F on p. 536",
    "plain $L$, $F$", "underline", "high", None,
    r"Convention of the Exposé X TeX: underlined Module letters written plain (outside its title the "
    r"exposé underlines only m, m' on p. 530 and one E in § 7.13), as reported for Exposé IX "
    r"(findings_501_505, findings_506_510): not itemized. The form if the diplomatic layer reproduces it: "
    r"'inversible $L$' -> 'inversible $\underline{L}$'; '\cl_P(L)\rightsquigarrow (\cl^\circ(L)y)' -> "
    r"'\cl_P(\underline{L})\rightsquigarrow (\cl^\circ(\underline{L})y)'; 'cohérent $F$' -> 'cohérent "
    r"$\underline{F}$'. The underlined O of O_X (twice) falls under the pending \cO decision.")

# ---------------------------------------------------------------- checks
ok = True
for e in F:
    fx = e["fix"]
    if fx is None:
        continue
    t = (B / f"page_{e['page']}.tex").read_text(encoding="utf-8")
    n = t.count(fx["old"])
    if n != 1 or fx["old"] == fx["new"] or "%%%%%%%%%%" in fx["old"]:
        ok = False
    print(e["page"], n, "OK" if n == 1 else "BAD", repr(fx["old"]))
for e in F:
    if e["kind"] == "misprint_in_print":
        assert "corrected" in e and e["corrected"], e
    else:
        assert "corrected" not in e, e
counts = {}
for e in F:
    c = counts.setdefault(e["page"], [0, 0])
    c[1 if e["kind"] == "misprint_in_print" else 0] += 1
print("counts (normal/misprint):", counts, "total", len(F))
if not ok:
    sys.exit("a fix failed the check; nothing written")
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("written", OUT)
