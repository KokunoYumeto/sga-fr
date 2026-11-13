"""Build findings_601_605.json and check every fix against the page files (helper of the 601-605 check).

'⏎' in fix strings and marker edits stands for a line break (LF).
"""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b601_605"
OUT = RUN / "findings_601_605.json"
MAIN = [pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6") / L / "main.tex"
        for L in ("diplomatic", "current")]
NL = "\n"


def nl(s):
    return s.replace("⏎", NL)


def fx(old, new):
    return {"old": nl(old), "new": nl(new)}


M601 = "%%%%%%%%%%  scan idx 614  |  folio 601  %%%%%%%%%%"
M602 = "%%%%%%%%%%  scan idx 615  |  folio 602  %%%%%%%%%%"
M604 = "%%%%%%%%%%  scan idx 617  |  folio 604  %%%%%%%%%%"
SEQ604 = (r"\(\mathcal O_{Y_i}\longrightarrow (f_i)_*(\mathcal O_{Y_{i-1}})\rightrightarrows (g_i)_*\bigl("
          r"\mathcal O_{Y_{i-1}}\otimes_{\mathcal O_{Y_i}}\mathcal O_{Y_{i-1}}\bigr)\)")
MARKER_EDITS = {
    601: (r"si et seulement si \((X_i)_\eta\cap(X_j)_\eta=\varnothing\).⏎" + M601 + "⏎Soient",
          "si et seulement si⏎" + M601 + r"⏎\((X_i)_\eta\cap(X_j)_\eta=\varnothing\). Soient"),
    602: (r"un sous-foncteur de \(\Pic_{Y/S}\) qui est⏎" + M602 + "⏎représentable",
          "un sous-foncteur de⏎" + M602 + r"⏎\(\Pic_{Y/S}\) qui est représentable"),
    604: ("(i.e. tel que la suite " + SEQ604 + "⏎" + M604 + "⏎soit exacte).",
          "(i.e. tel que la suite⏎" + M604 + "⏎" + SEQ604 + " soit exacte)."),
}


def edit_note(p):
    old, new = MARKER_EDITS[p]
    return "replace '" + old.replace("⏎", r"\n") + "' with '" + new.replace("⏎", r"\n") + "'"


F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- page 601
add(601, "start of page (folio-601 marker)",
    "p. 600 ends '... on peut supposer que X_i∩X_j = ∅ si et seulement si'; p. 601 begins "
    "'(X_i)_η∩(X_j)_η = ∅. Soient Y_k = ...' on one line (both scans; b596_600/page_600_s4.png, "
    "page_601_s1.png, witness DjVu p. 612)",
    r"'\((X_i)_\eta\cap(X_j)_\eta=\varnothing\).' stands at the end of page_600.tex, above the folio-601 marker; "
    "page_601.tex begins 'Soient'",
    "marker", "high", None,
    r"Page 601 really begins at '\((X_i)_\eta\cap(X_j)_\eta=\varnothing\).', in the paragraph that continues with "
    "'Soient' (main.tex has no blank line there). Exact edit in main.tex, both layers (each string occurs once in "
    "each layer): " + edit_note(601) + ".")
add(601, "end of the first paragraph, before Proposition 2.3",
    "'... quitte à restreindre S d'après (EGA III 7.8.6), de la' and, after a blank line, 'Proposition 2.3.': "
    "the sentence runs into the heading (both scans)",
    "'(EGA III 7.8.6), de la proposition suivante.'",
    "extra", "high", fx("(EGA III 7.8.6), de la proposition suivante.", "(EGA III 7.8.6), de la"),
    "The words 'proposition suivante.' are not in the print: its sentence ends with the heading 'Proposition 2.3.'.")
add(601, "Proposition 2.3 b)",
    "(où g_i=g|Y_i, i=1,2), Y_i on the line (both scans)",
    r"\(g_i=g|_{Y_i}\)",
    "formula", "high", fx(r"\(g_i=g|_{Y_i}\)", r"\(g_i=g|Y_i\)"),
    "Restriction written with a subscript; the print has g|Y_i.")
add(601, "'Après un changement de base convenable'",
    "begins a new, indented paragraph after '... et β de Y.' (both scans)",
    "runs on in the paragraph 'L'assertion est locale ...'",
    "other", "high", fx(r"de \(Y\). Après", r"de \(Y\).⏎⏎Après"),
    "Missing paragraph break.")
add(601, "Proposition 2.3, conclusion 'Alors Pic_{Y/S} ⟶ Pic_{(Y_1∐Y_2)/S}'",
    "both Pic underlined (both scans)",
    r"\(\Pic_{Y/S}\longrightarrow \Pic_{(Y_1\amalg Y_2)/S}\), \Pic = \operatorname{Pic} (plain)",
    "underline", "high",
    fx(r"Alors \(\Pic_{Y/S}\longrightarrow \Pic_{(Y_1\amalg Y_2)/S}\)",
       r"Alors \(\underline{\Pic}_{Y/S}\longrightarrow \underline{\Pic}_{(Y_1\amalg Y_2)/S}\)"),
    r"In Exposé XII \Pic prints a plain Pic (\providecommand at main.tex line 32; the one before Exposé XII does "
    r"not change it); Exposé XIII writes \underline{\Pic}. The print underlines Pic in most places of pp. 601-605 "
    "but not all (plain at p. 602 'dans Pic_{Y_1∐Y_2/S}' and three times on p. 605), so each place is itemized.")
add(601, "last line, 'tout point μ : S ⟶ Pic_{(Y_1∐Y_2)/S}'",
    "Pic underlined (both scans)",
    r"\(\mu:S\to\Pic_{(Y_1\amalg Y_2)/S}\)",
    "underline", "high",
    fx(r"\(\mu:S\to\Pic_{(Y_1\amalg Y_2)/S}\)", r"\(\mu:S\to\underline{\Pic}_{(Y_1\amalg Y_2)/S}\)"),
    "")
add(601, r"end of page_601.tex, '\(\Pic_{Y/S}\) qui est' (printed at the top of p. 602)",
    "p. 602, first line: Pic_{Y/S} with Pic underlined (both scans)",
    r"\(\Pic_{Y/S}\) qui est",
    "underline", "high",
    fx(r"\(\Pic_{Y/S}\) qui est", r"\(\underline{\Pic}_{Y/S}\) qui est"),
    "This text belongs to p. 602 (folio-602 marker finding). The old string is unique in page_601.tex, and in "
    "page 602 after the marker move; apply this fix after the marker edit given there.")
add(601, "Proposition 2.3 (and every statement on pp. 601-605)",
    "the typescript underlines the statement's word groups: 'Soient', 'un schéma,', 'un morphisme propre et', "
    "'deux sous-schémas fermés définis par les idéaux', 'On suppose que', 'sont fidèlement plats et de "
    "présentation finie sur', 'universellement', 'où', 'Alors', 'est représentable par un morphisme affine', "
    "'de présentation finie'",
    r"statement set in roman (no \underline)",
    "underline", "high", None,
    "Convention of the transcription in Exposé XII, reported once: the same pattern as Exposé II (GLOBAL_ISSUES 82). "
    "Also Lemme 2.4 (p. 602), II* and Lemme 2.6 (p. 603), Proposition 3.1 (pp. 604-605). Not itemized.")
add(601, "first paragraph, 'f = ∐_k f_k : ∐_k(∐_{i∈I(k)} X_i) ⟶ Y_k'",
    "target Y_k (both scans)",
    r"\longrightarrow Y_k (printed reading kept)",
    "misprint_in_print", "medium", None,
    "The target of ∐_k f_k is X = ∐_k Y_k. The TeX keeps the printed Y_k; the corrected layer already reads "
    r"\coprod_kY_k.",
    corrected=r"\coprod_kY_k")
add(601, "'Pour (c), celà résulte des deux suites exactes'",
    "celà (both scans)",
    "celà (printed reading kept)",
    "misprint_in_print", "medium", None,
    "Spelling slip of the typescript; the TeX keeps it; the corrected layer already reads 'cela'.",
    corrected="cela")

# ---------------------------------------------------------------- page 602
add(602, "start of page (folio-602 marker)",
    "p. 601 ends '... a comme image réciproque un sous-foncteur de'; p. 602 begins 'Pic_{Y/S} qui est "
    "représentable par un schéma affine sur S.' (both scans; page_601_s4.png, page_602_s1.png, witness DjVu p. 613)",
    r"'\(\Pic_{Y/S}\) qui est' stands at the end of page_601.tex, above the folio-602 marker; page_602.tex begins "
    "'représentable'",
    "marker", "high", None,
    r"Page 602 really begins at '\(\Pic_{Y/S}\) qui est'. Exact edit in main.tex, both layers (each string occurs "
    "once in each layer), to be made before the p. 601 underline fix of this Pic: " + edit_note(602) + ".")
add(602, "'un point λ : S ⟶ Pic_{Y/S} correspond à un faisceau'",
    "Pic underlined (both scans)",
    r"\(\lambda:S\to\Pic_{Y/S}\)",
    "underline", "high",
    fx(r"\(\lambda:S\to\Pic_{Y/S}\)", r"\(\lambda:S\to\underline{\Pic}_{Y/S}\)"),
    "The next Pic ('dans Pic_{Y_1∐Y_2/S} est μ') is plain in the print, as in the TeX.")
add(602, "'Ce L correspond alors à un point λ de Pic_{Y/S}'",
    "Pic underlined (both scans)",
    r"\(\Pic_{Y/S}\) qui va sur",
    "underline", "high",
    fx(r"point \(\lambda\) de \(\Pic_{Y/S}\)", r"point \(\lambda\) de \(\underline{\Pic}_{Y/S}\)"),
    "")
add(602, "'l'image réciproque de μ dans Pic_{Y/S} et le foncteur I'",
    "Pic underlined (both scans)",
    r"dans \(\Pic_{Y/S}\) et le foncteur",
    "underline", "high",
    fx(r"dans \(\Pic_{Y/S}\) et le foncteur", r"dans \(\underline{\Pic}_{Y/S}\) et le foncteur"),
    "")
add(602, "Lemme 2.4, 'Isom(L,M) le foncteur des isomorphismes'",
    "Isom underlined (both scans)",
    r"\(\Isom(L,M)\), \Isom = \operatorname{Isom} (plain)",
    "underline", "high",
    fx(r"\(\Isom(L,M)\) le foncteur", r"\(\underline{\Isom}(L,M)\) le foncteur"),
    "The print underlines Isom wherever it occurs on pp. 602-603.")
add(602, "Lemme 2.4 i)",
    "i) Isom(L,M) with Isom underlined (both scans)",
    r"\item \(\Isom(L,M)\) est",
    "underline", "high",
    fx(r"\item \(\Isom(L,M)\) est", r"\item \(\underline{\Isom}(L,M)\) est"),
    "")
add(602, "'Remarquons ... un isomorphisme φ : L_1|Y_1∩Y_2 ⥲ L_2|Y_1∩Y_2'",
    "restrictions written L_1|Y_1∩Y_2, L_2|Y_1∩Y_2, on the line (both scans)",
    r"\(\varphi:L_1|_{Y_1\cap Y_2}\xrightarrow{\sim}L_2|_{Y_1\cap Y_2}\)",
    "formula", "high",
    fx(r"\(\varphi:L_1|_{Y_1\cap Y_2}\xrightarrow{\sim}L_2|_{Y_1\cap Y_2}\)",
       r"\(\varphi:L_1|Y_1\cap Y_2\xrightarrow{\sim}L_2|Y_1\cap Y_2\)"),
    "Restriction written with a subscript.")
add(602, "'Réciproquement si φ est un isomorphisme L_1|Y_1∩Y_2 ⟶ ...', first restriction",
    "L_1|Y_1∩Y_2 on the line (both scans)",
    r"\(L_1|_{Y_1\cap Y_2}\to",
    "formula", "high",
    fx(r"\(L_1|_{Y_1\cap Y_2}", r"\(L_1|Y_1\cap Y_2"),
    "Restriction written with a subscript. Independent of the L_Z misprint fix and of the next fix (no overlap).")
add(602, "'Réciproquement si φ est un isomorphisme ... ⟶ L_Z|Y_1∩Y_2 tel que', second restriction",
    "L_Z|Y_1∩Y_2 on the line (both scans)",
    r"L_2|_{Y_1\cap Y_2}\) tel que \(u_1=u_2\circ\varphi\), il",
    "formula", "high",
    fx(r"|_{Y_1\cap Y_2}\) tel que \(u_1=u_2\circ\varphi\), il", r"|Y_1\cap Y_2\) tel que \(u_1=u_2\circ\varphi\), il"),
    "Restriction written with a subscript.")
add(602, "'Finalement soit I le foncteur ... φ : (L_1)_T|(Y_1∩Y_2)_T ⥲ (L_2)_T|(Y_1∩Y_2)_T'",
    "restrictions on the line (both scans)",
    r"(L_1)_T|_{(Y_1\cap Y_2)_T}\xrightarrow{\sim}(L_2)_T|_{(Y_1\cap Y_2)_T}",
    "formula", "high",
    fx(r"(L_1)_T|_{(Y_1\cap Y_2)_T}\xrightarrow{\sim}(L_2)_T|_{(Y_1\cap Y_2)_T}",
       r"(L_1)_T|(Y_1\cap Y_2)_T\xrightarrow{\sim}(L_2)_T|(Y_1\cap Y_2)_T"),
    "Restriction written with a subscript.")
add(602, "'Réciproquement si φ est un isomorphisme'",
    "begins a new, indented paragraph after '... tel que u_1 = u_2∘φ.' (both scans)",
    "runs on in the paragraph 'représentable par un schéma affine ...'",
    "other", "high",
    fx(r"\circ\varphi\). Réciproquement", r"\circ\varphi\).⏎⏎Réciproquement"),
    "Missing paragraph break.")
add(602, "'(où l'on prend X = Y_1∩Y_2):' before Lemme 2.4",
    "colon after the parenthesis (both scans; witness crop crops_601_605/w602_semicolon.png against the "
    "semicolon of 'suivant φ ; explicitement', w602_cmp_semicolon.png)",
    "semicolon '~;'",
    "punctuation", "medium",
    fx(r"\(X=Y_1\cap Y_2\))~;", r"\(X=Y_1\cap Y_2\))~:"),
    "Two round dots, no comma tail; the colon introduces the lemma.")
add(602, "'Réciproquement si φ est un isomorphisme L_1|Y_1∩Y_2 ⟶ L_Z|Y_1∩Y_2'",
    "the index of the target is a capital Z, not 2 (both scans; crops_601_605/m602_LZ.png: compare the 2 of Y_2 "
    "beside it)",
    r"L_2 (silently corrected)",
    "misprint_in_print", "high",
    fx(r"\to L_2", r"\to L_Z"),
    "Typing error Z for 2 (the target is L_2|Y_1∩Y_2, as in the line before). The TeX silently corrects it; the fix "
    "restores the printed reading. Independent of the two restriction fixes of this formula (no overlap).",
    corrected="L_2")

# ---------------------------------------------------------------- page 603
add(603, "Lemme 2.4 ii), 'le sous-foncteur de Isom(L,M) formée'",
    "Isom underlined (both scans)",
    r"de \(\Isom(L,M)\) formée",
    "underline", "high",
    fx(r"de \(\Isom(L,M)\) formée", r"de \(\underline{\Isom}(L,M)\) formée"),
    "")
add(603, "Lemme 2.4 ii), 'représentable par un fermé de Isom(L,M).'",
    "Isom underlined (both scans)",
    r"fermé de \(\Isom(L,M)\).",
    "underline", "high",
    fx(r"fermé de \(\Isom(L,M)\).", r"fermé de \(\underline{\Isom}(L,M)\)."),
    "")
add(603, "'En effet, ii) est clair.' after Lemme 2.4",
    "begins a new, indented paragraph (both scans)",
    r"follows \end{enumerate} without a blank line, so it is set as a continuation without indent",
    "other", "medium",
    fx(r"\end{enumerate}⏎En effet", r"\end{enumerate}⏎⏎En effet"),
    "Missing paragraph break.")
add(603, "Lemme 2.4 ii), 'le sous-foncteur de Isom(L,M) formée des isomorphismes'",
    "formée (both scans)",
    "formée (printed reading kept)",
    "misprint_in_print", "high", None,
    "Agreement slip (sous-foncteur is masculine). The TeX keeps it; the corrected layer already reads 'formé'.",
    corrected="formé")
add(603, "'un fermé F de V(E)×_s V(F)'",
    "the index of the fibre product is a small s (both scans; crops_601_605/w603_xs.png, m603_xs.png)",
    r"\times_S (silently corrected)",
    "misprint_in_print", "medium",
    fx(r"\times_S\mathbb V(F)", r"\times_s\mathbb V(F)"),
    "Typing error s for S (the base is S, typed as a capital S everywhere else). The TeX silently corrects it; the "
    "fix restores the printed reading.",
    corrected=r"\times_S\mathbb V(F)")
add(603, "display (*), 'O_Y ⟶ f_* O_Y ⇉ g_*(O_{X×_yX})'",
    "f_* O_Y (both scans)",
    r"\longrightarrow f_*\mathcal O_Y (printed reading kept)",
    "misprint_in_print", "high", None,
    "For f: X → Y the middle term is f_*O_X. The TeX keeps the printed O_Y; the corrected layer already reads "
    r"f_*\mathcal O_X.",
    corrected=r"f_*\mathcal O_X")
add(603, "display (*), index of the fibre product",
    "g_*(O_{X×_yX}) with a small y (both scans)",
    r"\mathcal O_{X\times_yX} (printed reading kept)",
    "misprint_in_print", "medium", None,
    r"Fibre product over Y. The TeX keeps the printed y; the corrected layer already reads X\times_YX.",
    corrected=r"\mathcal O_{X\times_YX}")
add(603, "'(où g : X×_yX ⟶ Y est le morphisme structural)'",
    "X×_yX with a small y (both scans)",
    r"\(g:X\times_yX\to Y\) (printed reading kept)",
    "misprint_in_print", "medium", None,
    r"As in (*). The TeX keeps the printed y; the corrected layer already reads X\times_YX.",
    corrected=r"g:X\times_YX\to Y")
add(603, "factorization 'X → Y_o → Y_1 → ... → Y_η = Y' after 'qu'il existe une factorisation de f'",
    "last arrow labelled f_η and last term Y_η: the Greek η of (X_i)_η, not the n of Lemme 2.6 'Y_n = Y' (both scans)",
    r"\xrightarrow{f_\eta}Y_\eta=Y (printed reading kept)",
    "misprint_in_print", "medium", None,
    "The index of the last step of the finite factorization is n (Lemme 2.6: Y_n = Y); η is the generic point "
    "elsewhere in the exposé. The TeX keeps the printed η; the corrected layer also has η.",
    corrected=r"\xrightarrow{f_n}Y_n=Y")

# ---------------------------------------------------------------- page 604
add(604, "start of page (folio-604 marker)",
    "p. 603 ends '... qui sont des épimorphismes effectifs (i.e. tel que la suite'; p. 604 begins with the formula "
    "'O_{Y_i} ⟶ (f_i)_*(O_{Y_{i-1}}) ⇉ (g_i)_*(O_{Y_{i-1}} ⊗_{O_{Y_i}} O_{Y_{i-1}}) soit exacte).' (both scans; "
    "page_603_s4.png, page_604_s1.png, witness DjVu p. 615)",
    r"the formula '\(\mathcal O_{Y_i}\longrightarrow ...\bigr)\)' stands at the end of page_603.tex, above the "
    "folio-604 marker; page_604.tex begins 'soit exacte).'",
    "marker", "high", None,
    "Page 604 really begins at the formula after 'tel que la suite'. Exact edit in main.tex, both layers (each "
    "string occurs once in each layer): " + edit_note(604) + ".")
add(604, "Proposition 3.1, '(Oort, Bull. soc. math. France, t. 90-1962)'",
    "the journal title is not underlined (both scans)",
    r"\emph{Bull. soc. math. France}",
    "underline", "high",
    fx(r"\emph{Bull. soc. math. France}", "Bull. soc. math. France"),
    r"Emphasis the print does not have (\emph is this file's command for the typescript's underline).")
add(604, "'Montrons que S = ∅. Sinons soit s un point maximal de S.'",
    "Sinons (both scans)",
    "Sinon (silently corrected)",
    "misprint_in_print", "high",
    fx("Sinon soit", "Sinons soit"),
    "Typing error. The TeX silently corrects it; the fix restores the printed reading.",
    corrected="Sinon")

# ---------------------------------------------------------------- page 605
add(605, "first display, iii) of Proposition 3.1, 'R^2f_*(I⊗f^*M) ≃ Hom_{O_S}(Q,M)'",
    "Hom underlined (both scans; crops_601_605/m605_hom.png)",
    r"\Hom_{\mathcal O_S}(Q,M)",
    "underline", "high",
    fx(r"\Hom_{\mathcal O_S}(Q,M)", r"\underline{\Hom}_{\mathcal O_S}(Q,M)"),
    "")
add(605, "'Alors le morphisme canonique Pic_{X/S} ⟶ Pic_{X'/S}'",
    "both Pic underlined (both scans)",
    r"\(\Pic_{X/S}\longrightarrow \Pic_{X'/S}\)",
    "underline", "high",
    fx(r"canonique \(\Pic_{X/S}\longrightarrow \Pic_{X'/S}\)",
       r"canonique \(\underline{\Pic}_{X/S}\longrightarrow \underline{\Pic}_{X'/S}\)"),
    "")
add(605, "display '0 ⟶ V(E^∨) ⟶ Pic_{X/S} ⟶ Pic_{X'/S} --u--> V(Q)'",
    "both Pic underlined (both scans)",
    r"\Pic_{X/S} ... \Pic_{X'/S}",
    "underline", "high",
    fx(r"\mathbb V(E^\vee)\longrightarrow \Pic_{X/S}⏎  \longrightarrow\Pic_{X'/S}",
       r"\mathbb V(E^\vee)\longrightarrow \underline{\Pic}_{X/S}⏎  \longrightarrow\underline{\Pic}_{X'/S}"),
    "The three later Pic of the page ('P ↪ Pic_{X'/S}', 'et Pic_{X/S} est un torseur', the display "
    "'0 ⟶ V(Ě) ⟶ Pic_{X/S} ⟶ P ⟶ 0') are plain in the print, as in the TeX.")
add(605, "'est un torseur sur P sous le groupe V(Ě)'",
    "a plain typed V; the two displays have the double-struck V (both scans; crops_601_605/m605_VE.png, "
    "m605_VE_disp.png)",
    r"\(\mathbb V(\check E)\)",
    "font", "high",
    fx(r"groupe \(\mathbb V(\check E)\)", r"groupe \(V(\check E)\)"),
    "")
add(605, "first diagram, the two vertical arrows from O*_{X_T}, O*_{X'_T} up to O_{X_T}, O_{X'_T}",
    "hooked arrows (inclusions), hook at the foot (both scans; crops_601_605/m605_hooks.png)",
    r"plain \arrow[u]",
    "symbol", "high",
    fx(r"\mathcal O_{X_T}^{*} \arrow[r] \arrow[u] & \mathcal O_{X'_T}^{*} \arrow[r] \arrow[u]",
       r"\mathcal O_{X_T}^{*} \arrow[r] \arrow[u,hook] & \mathcal O_{X'_T}^{*} \arrow[r] \arrow[u,hook]"),
    "The left vertical arrow of the second diagram is a plain arrow in the print, as in the TeX.")
add(605, "first diagram, end of the bottom row '... ⟶ O*_{X'_T} ⟶ 0'",
    "no comma after the 0; '(α(i) = 1+i)' follows (both scans)",
    "'& 0 ,'",
    "extra", "high",
    fx("& 0 ,", "& 0"),
    "Punctuation the print does not have.")
add(605, "'On fera attention que le carré de gauche'",
    "begins a new, indented paragraph after the second diagram (both scans)",
    r"follows \] without a blank line, so it continues the paragraph",
    "other", "medium",
    fx(r"\]⏎On fera attention", r"\]⏎⏎On fera attention"),
    "Missing paragraph break.")
add(605, "second diagram, bottom row 'R'(f_T)_*(O*_{X'_T})'",
    "R' with a prime for R^1 (both scans)",
    r"R'(f_T)_*(\mathcal O_{X'_T}^{*}) (printed reading kept)",
    "misprint_in_print", "high", None,
    "The long exact sequence reads R^1(f_T)_*(O*_{X_T}) → R^1(f_T)_*(O*_{X'_T}) → R^2(f_T)_*(I_T). The TeX keeps the "
    "printed R'; the corrected layer already reads R^1.",
    corrected=r"R^1(f_T)_*(\mathcal O_{X'_T}^{*})")


# ---------------------------------------------------------------- checks
def check():
    ok = True
    pages = {}
    for p in range(601, 606):
        pages[p] = (B / f"page_{p}.tex").read_text(encoding="utf-8")
    raw = dict(pages)
    for i, d in enumerate(F):
        fix = d["fix"]
        if fix is None:
            continue
        p = d["page"]
        old, new = fix["old"], fix["new"]
        n_raw = raw[p].count(old)
        n_cur = pages[p].count(old)
        if n_raw != 1 or n_cur != 1:
            print("BAD", p, i, repr(old), n_raw, n_cur)
            ok = False
        if "%%%%%%%%%%" in old:
            print("MARKER IN OLD", p, i)
            ok = False
        pages[p] = pages[p].replace(old, new, 1)
    # non-overlap of the fixes on each page: each old must still be found after all the other fixes
    for p in range(601, 606):
        fixes = [d["fix"] for d in F if d["page"] == p and d["fix"]]
        for j, fj in enumerate(fixes):
            t = raw[p]
            for k, fk in enumerate(fixes):
                if k != j:
                    t = t.replace(fk["old"], fk["new"], 1)
            if t.count(fj["old"]) != 1:
                print("ORDER-DEPENDENT", p, repr(fj["old"]))
                ok = False
    for path in MAIN:
        t = path.read_text(encoding="utf-8")
        for p, (old, new) in MARKER_EDITS.items():
            c = t.count(nl(old))
            if c != 1:
                print("MARKER EDIT NOT UNIQUE", path.parent.name, p, c)
                ok = False
    return ok


if __name__ == "__main__":
    good = check()
    print("checks ok" if good else "CHECKS FAILED")
    if good and "--write" in sys.argv:
        OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print("written", OUT, len(F))
    from collections import Counter
    c = Counter((d["page"], d["kind"] == "misprint_in_print") for d in F)
    for p in range(601, 606):
        print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
