"""Build findings_381_385.json; check that every fix's old string occurs exactly once in its page file."""
import json, pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:/Users/user/Documents/sga_scan_check_20261105/run_6")
B = RUN / "b381_385"
NL = "\u23ce"  # placeholder for a line break inside raw strings


def T(s):
    return s.replace(NL, "\n")


F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if fix is None else {"old": T(fix[0]), "new": T(fix[1])}}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 381 ----------------
add(381, "display after 'De l'isomorphisme :' (2.3.1)",
    "A ⥲ f_*(O_Y): a tilde over a short right arrow with its head (both scans; crops_381_385/c381_iso.png, w381_iso.png)",
    r"A\simeq f_*(\mathcal O_Y)", "symbol", "high",
    (r"A\simeq f_*(\mathcal O_Y)", r"A\xrightarrow{\sim} f_*(\mathcal O_Y)"),
    r"\xrightarrow{\sim} is the file's form for the printed ⥲ (as p. 367). The ≃ of 'D_+(U,s) ≃ Spec' (p. 382) and the six ≃ of p. 383 have a plain bar and stand.")
add(381, "(2.3.1.1)",
    "f^{-1}(A) → O_Y with nothing after it (both scans; w381_top.png)",
    r"f^{-1}(A)\longrightarrow \mathcal O_Y,", "punctuation", "high",
    (r"\longrightarrow \mathcal O_Y,", r"\longrightarrow \mathcal O_Y"),
    "Comma added at the end of a display.")
add(381, "(2.3.1.2)",
    "f̄ : (Y,O_Y) → (S,A) with nothing after it (both scans; w381_top.png)",
    r"\bar f:(Y,\mathcal O_Y)\longrightarrow (S,A).", "punctuation", "high",
    (r"\longrightarrow (S,A).", r"\longrightarrow (S,A)"),
    "Full stop added at the end of a display.")
add(381, "after (2.3.1.3): 'Comme l'homomorphisme (2.3.1.1) est plat'",
    "'Comme l'homomorphisme' begins a new, indented paragraph after 'pour tout A-Module M.' (both scans)",
    r"'pour tout \(A\)-Module \(M\).' and 'Comme l'homomorphisme' in one paragraph", "other", "high",
    (r"Module \(M\)." + NL + "Comme", r"Module \(M\)." + NL + NL + "Comme"),
    "Missing paragraph break.")
add(381, "'Si M est un A-Module quasi-cohérent, cette construction donne le Module M̃'",
    "'Si M est un A-Module' begins a new, indented paragraph after '(cf [4], p. 164).' (both scans)",
    r"'... (cf [4], p. 164). Si \(M\) est un ...' in one paragraph", "other", "high",
    (r"p. 164). Si", r"p. 164)." + NL + NL + "Si"),
    "Missing paragraph break; independent of the entry above.")
add(381, "display at the top of printed p. 382 (it stands in page_381.tex, above the folio-382 marker)",
    "M ⥲ f_*(M̃) = f̄_*(M̃): a tilde over a short right arrow with its head (both scans; crops_381_385/c382_iso1z.png, w382_iso1z.png)",
    r"M\simeq f_*(\widetilde M)=\bar f_*(\widetilde M)", "symbol", "high",
    (r"M\simeq f_*(\widetilde M)", r"M\xrightarrow{\sim} f_*(\widetilde M)"),
    "Printed on p. 382 (see the marker entry of p. 382). The old string occurs once in main.tex: if the marker is moved first, it is found under the folio-382 marker.")
add(381, "Proj_o throughout pp. 381-385 (15 places)",
    "the 'Proj' of Proj_o is underlined in all 15 places (both scans): p. 381 'le foncteur Proj_o à des'; p. 382 the display 'Proj_o(M)_{U,s} = ...', 'les Proj_o(M)_{U,s}', 'noté Proj_o(M)', 'la restriction de Proj_o(M)_{U,s}', 'isomorphe à Proj_o(M)_{U,st}'; p. 383 'le Module Proj_o(M)', 'le foncteur Proj_o est exact', 'noté Proj_o :', the display 'Proj_o : D^+(𝒞) → D^+(𝒜)'; p. 384 'Proj_o sur la catégorie', (2.5.1), 'Proj_o(M)|D_+(U,s)'; p. 385 'Proj_o∘F_k', (2.5.3). Only 'X = Proj(B)' (p. 382) is plain",
    r"\Proj_0 (11 times, pp. 381-384) and \operatorname{Proj}_0 (4 times, pp. 384-385): both print a plain Proj; the underlined form is \Projz (\underline{\operatorname{Proj}}_0, main.tex line 9132), which § 1 uses",
    "underline", "high", None,
    r"Convention of the § 2 transcription, reported once. One scripted pass, both layers: \Proj_0 -> \Projz and \operatorname{Proj}_0 -> \Projz on folios 381-389 (main.tex has no other \Proj_0; \operatorname{Proj}_0 also on lines 9738, 9754, 9802, 9804, folios 386-389, for that batch to confirm); leave \Proj(B) on p. 382. Three examples: p. 381 'le foncteur \(\Proj_0\) à des' -> 'le foncteur \(\Projz\) à des'; p. 383 '\Proj_0:D^+(\mathcal C)' -> '\Projz:D^+(\mathcal C)'; p. 385 '\operatorname{Proj}_0\circ\mathbf R F_k' -> '\Projz\circ\mathbf R F_k'. No other fix in this file contains a Proj, so the pass can run before or after them.")
add(381, "letters of sheaves and Modules on pp. 381-385",
    "underlined in the print: A, B, M, M̃ (p. 381); M, M̃, B, M_{(s),U}, M_s, M|U, B|U, M_{(s),V} (p. 382); M_{(s),U}, M_{(st),U}, M, and B except in the first two lines of the first display, where (B|U)_{(s)} is typed without underline (p. 383); B, L, F, M (p. 384; the first L of 'L ⤳ f_*(L(n))' is plain); M, F, M_{nd}, B_d, E, L (p. 385). Plain in the print: S, U, V, X, Y, f, s, t, z and the integers (both scans)",
    r"all plain (Exposé VI has no \underline outside the \Projz macro and the title)",
    "underline", "high", None,
    r"Convention of the Exposé VI transcription, already reported for pp. 366-380: not itemized. Three examples, in the form to use if the diplomatic layer reproduces it: p. 381 '\(Y=\Spec(A)\)' -> '\(Y=\Spec(\underline{A})\)'; p. 382 '\(M\) un \(B\)-Module gradué' -> '\(\underline{M}\) un \(\underline{B}\)-Module gradué'; p. 385 '$z\in\Gamma(V,M_{nd})=\Gamma\bigl(D_+(V,s),F(nd)\bigr)$' -> '$z\in\Gamma(V,\underline{M}_{nd})=\Gamma\bigl(D_+(V,s),\underline{F}(nd)\bigr)$'. The underlined structure sheaf O is \mathcal O, as the pending volume decision.")

# ---------------- page 382 ----------------
add(382, "start of page (folio-382 marker)",
    "p. 381 ends 'En effet, l'isomorphisme :' and blank space; p. 382 begins with the display 'M ⥲ f_*(M̃) = f̄_*(M̃)', then 'donne par adjonction un homomorphisme :' (both scans; w381_bot.png, w382_top.png)",
    r"the display '\[ M\simeq f_*(\widetilde M)=\bar f_*(\widetilde M) \]' ends page_381.tex, above the folio-382 marker; page_382.tex begins 'donne par adjonction'",
    "marker", "high", None,
    r"Page 382 really begins with that display (three TeX lines). Move the marker up above its '\[': python -I move_marker.py 6 382 '\[' --before (simulated in memory: the last '\[' before the marker is this display's). Exact edit in main.tex, both layers (diplomatic lines 9594-9598, current 9600-9604): replace 'l'isomorphisme~:\n\[\n  M\simeq f_*(\widetilde M)=\bar f_*(\widetilde M)\n\]\n%%%%%%%%%%  scan idx 395  |  folio 382  %%%%%%%%%%\n' by 'l'isomorphisme~:\n%%%%%%%%%%  scan idx 395  |  folio 382  %%%%%%%%%%\n\[\n  M\simeq f_*(\widetilde M)=\bar f_*(\widetilde M)\n\]\n' (\xrightarrow{\sim} for \simeq if the symbol fix of the page_381 entry is applied first).")
add(382, "2.3.2, display M_{(s),U} = ((M|U) ⊗_{(B|U)} (B|U)_s)_o",
    "(M|U): U on the line (both scans; w382_top.png)",
    r"(M|_U)", "formula", "high",
    (r"\bigl((M|_U)", r"\bigl((M|U)"),
    "Restriction written with a subscript U.")
add(382, "same display, index of ⊗",
    "⊗_{(B|U)}: U on the line of the index (both scans)",
    r"\otimes_{(B|_U)}", "formula", "high",
    (r"\otimes_{(B|_U)}", r"\otimes_{(B|U)}"),
    "Restriction written with a subscript U; independent of the entries before and after (no common text).")
add(382, "same display, (B|U)_s",
    "(B|U)_s: U on the line (both scans)",
    r"(B|_U)_s", "formula", "high",
    (r"(B|_U)_s\bigr)_0", r"(B|U)_s\bigr)_0"),
    "Restriction written with a subscript U.")
add(382, "display D_+(U,s) ≃ Spec((B|U)_{(s)})",
    "Spec((B|U)_{(s)}): U on the line (both scans; c382_iso2.png, w382_iso2.png)",
    r"\Spec\bigl((B|_U)_{(s)}\bigr)", "formula", "high",
    (r"\Spec\bigl((B|_U)_{(s)}\bigr)", r"\Spec\bigl((B|U)_{(s)}\bigr)"),
    "Restriction written with a subscript U.")
add(382, "'homogène de degré e > o, alors la restriction'",
    "e > o with the small letter o (x-height), where 'degré d > 0' and 'degré 0' above have the full-height digit (both scans; crops_381_385/c382_eo.png, c382_d0.png, w382_bot.png)",
    r"\(e>0\)", "symbol", "low",
    (r"\(e>0\)", r"\(e>o\)"),
    "The typist's letter o for a zero on the line (the global rule names only the index zero). Low: drop if that rule is taken to cover it.")

# ---------------- page 383 ----------------
add(383, "diagram at the top of p. 383",
    "a triangle: D_+(st) ↪(i) D_+(s) on top, U centred below, both arrows to U diagonal; f_{U,st} left of the left arrow, f_{U,s} right of the right arrow (both scans; crops_381_385/w383_diag.png)",
    r"U under D_+(s) in the second column: the arrow f_{U,s} is vertical (\arrow[d])", "formula", "low",
    (r'D_+(st) \arrow[r,hook,"i"] \arrow[dr,"f_{U,st}"' + "'" + r'] &' + NL + r'D_+(s) \arrow[d,"f_{U,s}"]\\' + NL + r'& U',
     r'D_+(st) \arrow[rr,hook,"i"] \arrow[dr,"f_{U,st}"' + "'" + r'] & &' + NL + r'D_+(s) \arrow[dl,"f_{U,s}"]\\' + NL + r'& U &'),
    "Labels, hook and arrow directions otherwise as printed; the three-column layout puts U in the middle and makes the f_{U,s} arrow diagonal (its label falls to the right, as printed).")
add(383, "'il s'agit de montrer que les Modules i^*∘f̄^*_{U,s}(M_{(s),U}) et f̄^*_{U,st}(M_{(st),U}) sont canoniquement isomorphes'",
    "both formulas and the 'et' between them stand inline, on the text line that begins 'il s'agit de montrer'; 'sont canoniquement isomorphes.' begins the next line (both scans)",
    r"a display \[ ... \quad\text{et}\quad ... \]", "other", "high",
    (r"les Modules" + NL + r"\[" + NL + r"  i^*\circ\bar f_{U,s}^{\,*}\bigl(M_{(s),U}\bigr)" + NL + r"  \quad\text{et}\quad" + NL + r"  \bar f_{U,st}^{\,*}\bigl(M_{(st),U}\bigr)" + NL + r"\]" + NL + "sont",
     r"les Modules \(i^*\circ\bar f_{U,s}^{\,*}\bigl(M_{(s),U}\bigr)\) et \(\bar f_{U,st}^{\,*}\bigl(M_{(st),U}\bigr)\)" + NL + "sont"),
    "The TeX makes inline formulas a display (as reported on p. 373).")
add(383, "first display, second line: ≃ i^{-1}(i^{-1}_{U,s}(M_{(s),U}) ⊗ ...",
    "the inner letter is an i (x-height stem with a foot serif and its dot) with a short typed bar across its top; no ascender and no hook of f (both scans; crops_381_385/c383_if.png, c383_if_z.png, w383_if_z.png, w383_line2.png)",
    r"i^{-1}\Bigl(i_{U,s}^{-1}\bigl(M_{(s),U}\bigr) (printed reading kept)", "misprint_in_print", "medium", None,
    "The sense needs f^{-1}_{U,s}: i^{-1}(f^{-1}_{U,s}(M_{(s),U}) ⊗ ...), as f^{-1}_{U,s} in the line above and in the index of the same line. The diplomatic layer is right; corrected edition: f.",
    corrected=r"f_{U,s}^{-1}")
add(383, "first display, first line, index of ⊗",
    "(B|U)_{(s)}: U on the line (both scans; w383_line1.png)",
    r"(B|_U)_{(s)}", "formula", "high",
    (r"(B|_U)_{(s)})}\mathcal O_{D_+(s)}\Bigr)\\", r"(B|U)_{(s)})}\mathcal O_{D_+(s)}\Bigr)\\"),
    "Restriction written with a subscript U.")
add(383, "first display, second line, index of the first ⊗",
    "(B|U)_{(s)}: U on the line (both scans; w383_line2.png)",
    r"(B|_U)_{(s)}", "formula", "high",
    (r"(B|_U)_{(s)})}\mathcal O_{D_+(s)}\Bigr)" + NL + r" \otimes_{i^{-1}", r"(B|U)_{(s)})}\mathcal O_{D_+(s)}\Bigr)" + NL + r" \otimes_{i^{-1}"),
    "Restriction written with a subscript U; does not overlap the entry above (other line).")
add(383, "first display, third line, index of ⊗",
    "(B|U)_{(s)}: U on the line (both scans)",
    r"(B|_U)_{(s)}", "formula", "high",
    (r"f_{U,st}^{-1}((B|_U)_{(s)})", r"f_{U,st}^{-1}((B|U)_{(s)})"),
    "Restriction written with a subscript U.")
add(383, "display after 'D'autre part :'",
    "(B|U)_{(st)}: U on the line (both scans)",
    r"(B|_U)_{(st)}", "formula", "high",
    (r"((B|_U)_{(st)})", r"((B|U)_{(st)})"),
    "Restriction written with a subscript U.")
add(383, "display after 'Enfin, il résulte de EGA II 2.2.2', index of ⊗",
    "⊗_{(B|U)_{(s)}}: U on the line (both scans; w383_bot.png)",
    r"\otimes_{(B|_U)_{(s)}}", "formula", "high",
    (r"\otimes_{(B|_U)_{(s)}}", r"\otimes_{(B|U)_{(s)}}"),
    "Restriction written with a subscript U.")
add(383, "same display, last factor",
    "(B|U)_{(st)} ,: U on the line (both scans)",
    r"(B|_U)_{(st)},", "formula", "high",
    (r"(B|_U)_{(st)},", r"(B|U)_{(st)},"),
    "Restriction written with a subscript U; independent of the entry above.")
add(383, "'On voit également sur les constructions précédentes que le foncteur'",
    "'On voit également' begins a new, indented paragraph after the display of 2.3.3 (both scans)",
    r"'\]' followed directly by 'On voit également' (the paragraph runs on)", "other", "high",
    (r"\]" + NL + "On voit également", r"\]" + NL + NL + "On voit également"),
    "Missing paragraph break.")

# ---------------- page 384 ----------------
add(384, "start of page (folio-384 marker)",
    "p. 383 ends 'On voit également sur les constructions précédentes que le foncteur'; p. 384 begins 'Proj_o sur la catégorie des B-Modules gradués' (both scans; w383_bot.png, w384_top.png)",
    r"page_383.tex ends 'que le'; page_384.tex begins 'foncteur \(\Proj_0\) sur la catégorie'",
    "marker", "high", None,
    r"The folio-384 marker stands one word early: 'foncteur' belongs to p. 383; page 384 really begins at '\(\Proj_0\) sur la catégorie'. Exact edit in main.tex, both layers (diplomatic lines 9680-9682, current 9686-9688): replace 'que le\n%%%%%%%%%%  scan idx 397  |  folio 384  %%%%%%%%%%\nfoncteur ' by 'que le foncteur\n%%%%%%%%%%  scan idx 397  |  folio 384  %%%%%%%%%%\n'. Or python -I move_marker.py 6 384 '\(\Proj' (also after the Proj pass, which writes \(\Projz\)).")
add(384, "'Si L est un O_X-Module localement libre de type fini'",
    "'Si L est un' begins a new, indented paragraph after (2.4.2) (both scans)",
    r"'\end{equation}' followed directly by 'Si $L$ est un' (the paragraph runs on)", "other", "high",
    (r"\end{equation}" + NL + r"Si $L$ est un", r"\end{equation}" + NL + NL + r"Si $L$ est un"),
    "Missing paragraph break.")
add(384, "display after 'en posant M = F_k(F) :'",
    "Proj_o(M)|D_+(U,s): D_+(U,s) on the line (both scans; w384_bot.png)",
    r"\operatorname{Proj}_0(M)|_{D_+(U,s)}", "formula", "high",
    (r"(M)|_{D_+(U,s)}", r"(M)|D_+(U,s)"),
    "Restriction written as a subscript. The old string leaves out the Proj, so the Proj pass does not touch it.")
add(384, "last display: f̄^*_{U,s}(M_{(s),U}) → F|D_+(U,s) ,",
    "F|D_+(U,s): on the line (both scans; w384_bot.png)",
    r"F|_{D_+(U,s)},", "formula", "high",
    (r"F|_{D_+(U,s)}", r"F|D_+(U,s)"),
    "Restriction written as a subscript.")

# ---------------- page 385 ----------------
add(385, "first display: M_{(s),U} → f_{U,s*}(F|D_+(U,s)) .",
    "F|D_+(U,s): on the line (both scans)",
    r"f_{U,s*}\bigl(F|_{D_+(U,s)}\bigr).", "formula", "high",
    (r"F|_{D_+(U,s)}", r"F|D_+(U,s)"),
    "Restriction written as a subscript.")
add(385, "'en notant α_d l'homomorphisme canonique Γ(V,B_d) → Γ(f^{-1}(V),O_X(d)) (cf. EGA II 2.6.3 et 2.6.4)'",
    "the formula stands inline, at the start of the text line 'Γ(V,B_d) → Γ(f^{-1}(V),O_X(d)) (cf. EGA II 2.6.3 et 2.6.4). On vérifie sans' (both scans; crops_381_385/c385_inline.png)",
    r"a display \[ \Gamma(V,B_d)\longrightarrow ... \]", "other", "high",
    (r"l'homomorphisme canonique" + NL + r"\[" + NL + r"  \Gamma(V,B_d)\longrightarrow \Gamma\bigl(f^{-1}(V),\mathcal O_X(d)\bigr)" + NL + r"\]" + NL + "(cf. EGA",
     r"l'homomorphisme canonique $\Gamma(V,B_d)\longrightarrow \Gamma\bigl(f^{-1}(V),\mathcal O_X(d)\bigr)$ (cf. EGA"),
    "The TeX makes an inline formula a display.")
add(385, "'Il est clair que dans le cas ou F est quasi-cohérent'",
    "'ou' without the grave accent (both scans; crops_381_385/c385_ou.png)",
    "dans le cas ou $F$ (printed reading kept)", "misprint_in_print", "high", None,
    "Missing accent (as 'dans le cas ou S est noethérien', p. 369). The diplomatic layer is right.",
    corrected="où")
add(385, "Proposition 2.6: 'et L. un complexe parfait sur X'",
    "the dot after L sits on the baseline, like a full stop (both scans; crops_381_385/c385_Ldot.png, w385_Ldot_z.png), whereas the complexes of § 2 have the raised dot (L˙ on p. 380 and four times on p. 386, witness)",
    r"et $L^{\bullet}$ un complexe (silently corrected)", "misprint_in_print", "medium",
    (r"et $L^{\bullet}$ un complexe", r"et $L_{\bullet}$ un complexe"),
    "The typist did not raise the dot; the complex is L^• as in 2.6 i), ii). The diplomatic layer should keep the lower dot.",
    corrected=r"L^{\bullet}")
add(385, "Proposition 2.6 (pp. 385-386)",
    "underlined word groups on p. 385: 'Soient', 'un schéma quasi', 'compact' (the hyphen left out), 'un', '-Module locale-/ment libre de type fini', 'et', 'un complexe parfait sur', 'Alors', 'il existe un entier', 'tel que pour', 'les propriétés suivantes soient / vérifiées'; plain: S, X = P(E) (P doubly underlined), k_o, k ⩾ k_o, the commas, the full stops and ':'; E, O_S and L carry their own underlines; the label underlines only 'Proposition' (both scans; w385_prop.png)",
    r"the statement in roman (no \underline, no \emph)", "underline", "high", None,
    "Exposé VI follows the Exposé II pattern of GLOBAL_ISSUES 82 (as on pp. 367-380): not itemized; the word groups are listed for the scripted pass. No emphasized defined terms and no category L on pp. 381-385.")
add(385, "end of page (folio-386 marker)",
    "p. 385 ends with 'vérifiées :'; p. 386 begins with the display 'i) RF_k(L˙) est 𝒞_o-parfait ; ii) Le morphisme canonique (2.5.3) : ...' (both scans; witness p. 386, crops_381_385/w386_top_check.png)",
    r"page_385.tex ends with the display's opening '\[' and '\begin{array}{ll}'; the folio-386 marker stands inside the array, before '\mathrm{i)}'",
    "marker", "medium", None,
    r"Page 386 really begins at the display's '\['; no printed word changes page, but page_385.tex ends with an unclosed display and page_386.tex begins inside an array. Move the marker up two lines: python -I move_marker.py 6 386 '\[' --before (simulated in memory). Exact edit in main.tex, both layers (diplomatic lines 9731-9734, current 9737-9740): replace 'vérifiées :\n\[\n\begin{array}{ll}\n%%%%%%%%%%  scan idx 399  |  folio 386  %%%%%%%%%%\n' by 'vérifiées :\n%%%%%%%%%%  scan idx 399  |  folio 386  %%%%%%%%%%\n\[\n\begin{array}{ll}\n'.")

# ---------------- checks ----------------
ok = True
for d in F:
    if d["fix"] is None:
        continue
    txt = (B / ("page_%d.tex" % d["page"])).read_text(encoding="utf-8")
    n = txt.count(d["fix"]["old"])
    if n != 1 or "%%%%%%%%%%" in d["fix"]["old"] or NL in d["fix"]["old"] or NL in d["fix"]["new"]:
        ok = False
        print("BAD", d["page"], n, repr(d["fix"]["old"][:80]))
for p in range(381, 386):
    txt = (B / ("page_%d.tex" % p)).read_text(encoding="utf-8")
    spans = []
    for d in F:
        if d["page"] == p and d["fix"]:
            i = txt.find(d["fix"]["old"])
            spans.append((i, i + len(d["fix"]["old"]), d["where"][:40]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            ok = False
            print("OVERLAP", p, a, b)
M = pathlib.Path(r"C:/Users/user/Documents/sga_scan_check_20261105/sga6/diplomatic/main.tex").read_text(encoding="utf-8")
C = pathlib.Path(r"C:/Users/user/Documents/sga_scan_check_20261105/sga6/current/main.tex").read_text(encoding="utf-8")
for s in ["l'isomorphisme~:\n\\[\n  M\\simeq f_*(\\widetilde M)=\\bar f_*(\\widetilde M)\n\\]\n%%%%%%%%%%  scan idx 395  |  folio 382  %%%%%%%%%%\n",
          "que le\n%%%%%%%%%%  scan idx 397  |  folio 384  %%%%%%%%%%\nfoncteur ",
          "vérifiées :\n\\[\n\\begin{array}{ll}\n%%%%%%%%%%  scan idx 399  |  folio 386  %%%%%%%%%%\n",
          "M\\simeq f_*(\\widetilde M)"]:
    print("main.tex count dipl/current:", M.count(s), C.count(s), repr(s[:50]))
counts = {}
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else "normal"
    counts.setdefault(d["page"], {"normal": 0, "misprint": 0})[k] += 1
print(counts, len(F), "OK" if ok else "PROBLEMS")
out = RUN / "findings_381_385.json"
out.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", out)
