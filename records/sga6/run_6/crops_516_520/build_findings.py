"""Write findings_516_520.json and check that every fix's old string occurs exactly once in its page file."""
import json, pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
OUT = RUN / "findings_516_520.json"
PAGEFILE = {515: RUN / "b511_515" / "page_515.tex"}
for p in range(516, 521):
    PAGEFILE[p] = RUN / "b516_520" / f"page_{p}.tex"
M516 = "%%%%%%%%%%  scan idx 529  |  folio 516  %%%%%%%%%%"

F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


DISP1 = ("printed on p. 516 (above the folio-516 marker): first display "
         "'A_o = ∐_{k_i∈ℤ} F_o^{(1)⊗k_1} ⊗F_o^{(2)⊗k_2} ⊗...⊗ F_o^{(n)⊗k_n} .'")

# ---------------- page 515 file: the display printed at the top of p. 516 ----------------
add(515, DISP1 + ", the sign before F",
    "a hand-drawn coproduct sign ∐ (two stems standing on a base line) with k_i∈ℤ below it, the same sign as in the "
    "display A = ∐ ... lower on p. 516 (both scans; crops_516_520/m516_A0.png, wit_516_half.png)",
    r"A_0=\bigoplus_{k_i\in\mathbb Z}", "symbol", "high",
    {"old": r"A_0=\bigoplus", "new": r"A_0=\coprod"},
    "The display stands in page_515.tex until the folio-516 marker is moved (marker entry of p. 516); "
    "Exposé IX has six \\bigoplus, only the two of p. 516 are checked here.")
add(515, DISP1 + ", the factors",
    "three factors: F_o^{(1)⊗k_1} ⊗F_o^{(2)⊗k_2} ⊗...⊗ F_o^{(n)⊗k_n} (both scans; crops_516_520/m516_A0.png)",
    r"(F_0^{(1)})^{\otimes k_1}\otimes\cdots\otimes(F_0^{(n)})^{\otimes k_n}: the factor with (2) is left out",
    "missing", "high",
    {"old": r"^{\otimes k_1}\otimes\cdots", "new": r"^{\otimes k_1}\otimes {F_0^{(2)}}^{\otimes k_2}\otimes\cdots"},
    "The factor is given without the parentheses the print does not have (next two entries). The second display of "
    "p. 516 (A = ∐ ...) has only the factors (1) and (n), as its TeX.")
add(515, DISP1 + ", first factor",
    "F_o^{(1)⊗k_1}: the power ⊗k_1 is raised after the superscript (1); no parentheses round F_o^{(1)} (both scans)",
    r"(F_0^{(1)})^{\otimes k_1}", "formula", "medium",
    {"old": r"(F_0^{(1)})", "new": r"{F_0^{(1)}}"},
    "Parentheses added by the TeX; the same for the last factor (next entry) and in the second display of p. 516.")
add(515, DISP1 + ", last factor",
    "F_o^{(n)} ⊗k_n: no parentheses round F_o^{(n)} (both scans)",
    r"(F_0^{(n)})^{\otimes k_n}", "formula", "medium",
    {"old": r"(F_0^{(n)})", "new": r"{F_0^{(n)}}"},
    "As the previous entry.")

# ---------------- page 516 ----------------
add(516, "start of page (folio-516 marker)",
    "p. 515 ends 'que Y_o est le X_o-schéma affine défini par l'algèbre :'; p. 516 begins with the display "
    "'A_o = ∐_{k_i∈ℤ} F_o^{(1)⊗k_1} ⊗F_o^{(2)⊗k_2} ⊗...⊗ F_o^{(n)⊗k_n} .', then 'Le groupe G opère sur E_o, ...' "
    "(both scans; b511_515/page_515_s4.png, crops_516_520/wit_516_half.png)",
    "page_515.tex ends with that display (\\[ A_0=\\bigoplus... \\]) above the folio-516 marker; page_516.tex begins "
    "'Le groupe'",
    "marker", "high", None,
    "Page 516 really begins at the display's '\\[' after 'défini par l'algèbre :' (about diplomatic main.tex line 13334, "
    "current 13340 at 16:20; main.tex was being edited while I checked, so lines shift). Exact edit in main.tex, both "
    "layers, two parts applied together: replace '\\]\\n" + M516 + "\\nLe\\ngroupe' by '\\]\\nLe\\ngroupe', and "
    "'défini par l'algèbre :\\n\\[\\n' by 'défini par l'algèbre :\\n" + M516 + "\\n\\[\\n' (each old string once per "
    "layer). Same result: python -I move_marker.py 6 516 \"\\[\" --before (simulated in memory, identical in both "
    "layers: crops_516_520/sim_markers.py). The edit does not touch the display, so the four fixes of the display "
    "listed under page 515 can be applied before it (their old strings stand under the folio-515 marker until the move).")
add(516, "second display 'A = ∐_{k_i∈ℤ} F^{(1)⊗k_1} ⊗...⊗ F^{(n)⊗k_n} .', the sign before F",
    "the hand-drawn coproduct sign ∐, as in the first display (both scans)",
    r"A=\bigoplus_{k_i\in\mathbb Z}", "symbol", "high",
    {"old": r"A=\bigoplus", "new": r"A=\coprod"}, "As the first display (page-515 entry).")
add(516, "second display 'A = ∐_{k_i∈ℤ} F^{(1)⊗k_1} ⊗...⊗ F^{(n)⊗k_n} .', the factors",
    "F^{(1)⊗k_1} and F^{(n)⊗k_n} with the powers raised after the superscripts; no parentheses (both scans)",
    r"(F^{(1)})^{\otimes k_1}\otimes\cdots\otimes(F^{(n)})^{\otimes k_n}", "formula", "medium",
    {"old": r"(F^{(1)})^{\otimes k_1}\otimes\cdots\otimes(F^{(n)})^{\otimes k_n}",
     "new": r"{F^{(1)}}^{\otimes k_1}\otimes\cdots\otimes{F^{(n)}}^{\otimes k_n}"},
    "Parentheses added by the TeX, as in the first display.")
add(516, "'le schéma X = 𝔻(E) = P/B des drapeaux de E'",
    "double-struck 𝔻 (doubled stem) for the flag scheme (both scans; crops_516_520/m516_DE.png)",
    r"$X=D(E)=P/B$", "font", "high",
    {"old": r"$X=D(E)=P/B$", "new": r"$X=\mathbb D(E)=P/B$"},
    "Exposé IX writes D(E) plain 11 times; the other nine (proof with the complete flag bundle D(E)) are on other "
    "pages: check them there.")
add(516, "diagram, right-hand vertex 'X = P/B = 𝔻(E)'",
    "double-struck 𝔻, as in the text above (both scans; crops_516_520/m516_diag_dot.png)",
    r"X=P/B=D(E)", "font", "high",
    {"old": r"X=P/B=D(E)", "new": r"X=P/B=\mathbb D(E)"}, "As the previous entry.")
add(516, "end of the diagram (P, Y = P/U, X = P/B = 𝔻(E), S)",
    "a full stop at the right of the diagram's last row, where the typist puts the stop of a display (both scans; "
    "crops_516_520/m516_diag_dot.png, wit_516_half.png)",
    "\\end{array} \\] with no full stop", "punctuation", "medium",
    {"old": "\\end{array}\n\\]", "new": "\\end{array}.\n\\]"}, "")
add(516, "K with a raised dot on pp. 516-518 (14 places): 'D'après 3.1, on a K.(X) = K.(S)⊗_{K˙(S)}K˙(X)', "
         "'Soit ξ_i la classe de F^{(i)} dans K˙(X)', ...",
    "a solid raised typed dot after K, the same mark as Exposé VI's K˙ (both scans; crops_516_520/m516_Kdot.png, "
    "m516_Kdot2.png, m518_arrow.png)",
    r"K^\circ (105 places in Exposé IX)", "symbol", "high", None,
    "Convention of the Exposé IX TeX, not itemized: one pass K^\\circ -> K^{\\bullet} over the exposé, both layers, as "
    "done for Exposés IV, VI and VII. Three examples: p. 516 'la classe de $F^{(i)}$ dans $K^\\circ(X)$' -> '... dans "
    "$K^{\\bullet}(X)$'; p. 517 'Donc $K^\\circ(X)/I=K^\\circ(S)/J$' -> 'Donc $K^{\\bullet}(X)/I=K^{\\bullet}(S)/J$'; "
    "p. 518 'K^\\circ(S)/J\\xrightarrow{\\sim}K^\\circ(P).' -> 'K^{\\bullet}(S)/J\\xrightarrow{\\sim}K^{\\bullet}(P).'. "
    "No old string of this file contains K^\\circ except the p. 519 entry (Exposé X, itemized there).")
add(516, "underlined letters on pp. 516-520: E, E_o, L_o^{(i)}, F^{(i)}, F_o^{(i)}, A, A_o (Exposé IX); F, F_x, G', G, "
         "G'' (Exposé X)",
    "underlined in the print (both scans)",
    "plain letters (Exposé IX has one \\underline in all)", "underline", "high", None,
    "Convention of the transcription, not itemized. The underlined O written \\mathcal O is the pending volume "
    "decision. Three examples, in the form to use if the diplomatic layer reproduces the underline: p. 516 'on obtient "
    "le faisceau $E$ associé à $P$' -> 'on obtient le faisceau $\\underline{E}$ associé à $P$'; p. 516 'Soit $\\xi_i$ "
    "la classe de $F^{(i)}$' -> '... de $\\underline{F}^{(i)}$'; p. 517 'puisqu'alors $E=\\mathcal O_S^n$' -> "
    "'puisqu'alors $\\underline{E}=\\mathcal O_S^n$'. Same in Exposé X on pp. 519-520 (e.g. p. 520 'les faisceaux "
    "$G'$, $G$ et $G''$', all three underlined in the print).")

# ---------------- page 517 ----------------
add(517, "'Par suite, K.(Y) ≃ K.(S)/JK.(S). On achève la démonstration par le lemme :'",
    "the formula stands in the text: it begins the line at the left margin and 'On achève la démonstration par le "
    "lemme :' follows on the same line (both scans; crops_516_520/m517_inline.png, wit_517_half.png)",
    "a display \\[ K_\\bullet(Y)\\simeq K_\\bullet(S)/J K_\\bullet(S). \\]", "other", "high",
    {"old": "Par suite,\n\\[\nK_\\bullet(Y)\\simeq K_\\bullet(S)/J K_\\bullet(S).\n\\]\nOn achève",
     "new": "Par suite,\n$K_\\bullet(Y)\\simeq K_\\bullet(S)/J K_\\bullet(S)$. On achève"},
    "")
add(517, "Corollaire 4.3: 'Soient S un schéma noethérien, G = Gl(n)_S.'",
    "'Gl(n)_S': capital G, small l (both scans; crops_516_520/m517_Gl.png)",
    r"$G=\mathrm{GL}(n)_S$", "word", "high",
    {"old": r"$G=\mathrm{GL}(n)_S$", "new": r"$G=\mathrm{Gl}(n)_S$"},
    "Capital against small. The heading of § 4 and Proposition 4.1 (GL(n)_S) are on p. 514, not checked here.")

# ---------------- page 519 ----------------
add(519, "heading and title of Exposé X",
    "two blocks: 'EXPOSE X' in typed capitals, single underline, no full stop, at the left; then the title "
    "'FORMALISME DES INTERSECTIONS SUR LES SCHEMAS ALGEBRIQUES PROPRES' in typed capitals with a double underline "
    "(both scans; b516_520/page_519_s1.png, crops_516_520/wit_519_half.png)",
    r"\section*{Exposé X. Formalisme des intersections sur les schémas algébriques propres}", "word", "medium",
    {"old": r"\section*{Exposé X. Formalisme des intersections sur les schémas algébriques propres}",
     "new": r"\section*{\underline{EXPOSÉ X}\\[3pt] \underline{\underline{FORMALISME DES INTERSECTIONS SUR LES SCHÉMAS ALGÉBRIQUES PROPRES}}}"},
    "Same form as the applied headings of Exposés III, IV and IX (main.tex: \\section*{\\underline{EXPOSÉ IX}\\\\[3pt] "
    "\\underline{\\underline{QUELQUES CALCULS DE GROUPES $K$}}}); É keeps the TeX's accents (rule for typed capitals: "
    "the print has EXPOSE, SCHEMAS ALGEBRIQUES). Independent of the author-line entry.")
add(519, "author line of the heading",
    "'par O. Jussila' in mixed case, the whole line underlined; '(avec un appendice par A. Grothendieck)' below it "
    "is not underlined (both scans)",
    "par O. Jussila\\\\ (no underline)", "word", "medium",
    {"old": "par O. Jussila", "new": r"\underline{par O. Jussila}"},
    "As the applied author lines (\\underline{par P. BERTHELOT}); the name is printed in mixed case here.")
add(519, "line under the title of § 1: 'K˙(X) x K.(X) ⟶ K.(X).'",
    "K with a solid raised dot (both scans; crops_516_520/m519_Kprod.png)",
    r"K^\circ(X)\times K_\bullet(X)", "symbol", "high",
    {"old": r"K^\circ(X)\times", "new": r"K^{\bullet}(X)\times"},
    "Itemized because Exposé X writes this K both ways (55 K^\\circ and 66 K^\\bullet in main.tex at 16:15); the "
    "Exposé IX convention entry (p. 516) covers only Exposé IX.")

# ---------------- page 520 ----------------
add(520, "(1.1.3) 'cl.(F) = Σ_{x∈X(n)} long(F_x)cl.(O_{Z(x)}) + w'",
    "nothing after w; the next line is 'où w∈Filt_{n-1}(X) .' (both scans; crops_516_520/m520_w.png, w520_w.png)",
    r"\cl_\bullet(\mathcal O_{Z(x)})+w,", "punctuation", "high",
    {"old": "+w,", "new": "+w"}, "Comma added by the TeX at the end of the display.")
add(520, "label 'Corrollaire 1.1.4.'",
    "'Corrollaire' (double r, both scans)",
    r"\textbf{Corrollaire 1.1.4.} (printed reading kept)", "misprint_in_print", "high", None,
    "Typing error of the print; the TeX keeps it.", corrected="Corollaire")
add(520, "'Démonstration de 1.1.2 : Soit X' = Supp(F).'",
    "the underline covers 'Démonstration de' only; '1.1.2 :' is plain (both scans; crops_516_520/m520_demo.png)",
    r"\emph{Démonstration de 1.1.2 :}", "underline", "high",
    {"old": r"\emph{Démonstration de 1.1.2 :}", "new": r"\emph{Démonstration de} 1.1.2 :"},
    "As \\emph{Preuve de} (3.5.1). on pp. 189-190 (findings_186_190).")
add(520, "'Evidemment K' contient les faisceaux O_{Z(x)} avec x∈X'.'",
    "no comma between O_{Z(x)} and 'avec' (both scans; crops_516_520/m520_OZx.png, wit_520_half.png)",
    r"$\mathcal O_{Z(x)}$, avec", "punctuation", "high",
    {"old": r"$\mathcal O_{Z(x)}$, avec", "new": r"$\mathcal O_{Z(x)}$ avec"}, "Comma added by the TeX.")
add(520, "'Il suffit donc de montrer que K' est un sous-ensemble \"exact\" de Ob(K)'",
    "'exact' in straight double quotes (both scans; crops_516_520/m520_exact.png)",
    "sous-ensemble exact de (no quotes)", "punctuation", "high",
    {"old": "sous-ensemble exact de", "new": "sous-ensemble «~exact~» de"},
    "The file's form for the print's straight quotes (Exposé X: «~nombre d'intersection~», «~additif~»).")
add(520, "(1.1.5) '0 ⟶ G' ⟶ G ⟶ G' ⟶ 0'",
    "the fourth term is G' with one tick, like the second; this typewriter's double prime is two ticks (G'', ℓ''_x "
    "three lines below) (both scans; crops_516_520/m520_115.png, w520_115.png)",
    r"0\longrightarrow G'\longrightarrow G\longrightarrow G''\longrightarrow0 (silently corrected)",
    "misprint_in_print", "high",
    {"old": r"G\longrightarrow G''\longrightarrow0", "new": r"G\longrightarrow G'\longrightarrow0"},
    "The sequence is G' -> G -> G'' (the text then names G', G and G''); the TeX corrects the print silently. The fix "
    "restores the printed G'.", corrected=r"G\longrightarrow G''\longrightarrow0")

# ---------------- checks ----------------
ok = True
for f in F:
    fx = f["fix"]
    if fx is None:
        continue
    t = PAGEFILE[f["page"]].read_text(encoding="utf-8")
    n = t.count(fx["old"])
    bad_marker = "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]
    print(f["page"], f["kind"], "count", n, "marker-in-fix" if bad_marker else "", repr(fx["old"][:60]))
    if n != 1 or bad_marker:
        ok = False
print("all olds unique:", ok, "| findings:", len(F))
if ok:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("written", OUT)
