"""Build findings_156_160.json (SGA 6, pp. 156-160) and check that every fix's old occurs exactly once in its page file
and contains no marker line."""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b156_160"
OUT = RUN / "findings_156_160.json"
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
NL = "\n"
F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, confidence=confidence, fix=fix)
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def fx(old, new):
    return {"old": old, "new": new}


RHOM_NEW = r"\mathbb{R}\underline{\Hom}"
RHOM_TEX = r"\RHom = \mathrm R\!\operatorname{Hom} (main.tex line 1847): plain R, Hom not underlined"

# ---------------------------------------------------------------- page 156
add(156, "paragraph before Proposition 8.3, 'Le lien entre trace et cup-produit s'exprime dans la'",
    "the sentence stops at 'dans la' and runs into the label 'Proposition 8.3.' of the next line; nothing else on the "
    "line (both scans)",
    "s'exprime dans la proposition suivante.",
    "extra", "high", fx("s'exprime dans la proposition suivante.", "s'exprime dans la"),
    "The words 'proposition suivante.' are not in the print. With the fix the paragraph ends 'dans la' and the next "
    "paragraph is \\textbf{Proposition 8.3.}, as printed.")
add(156, "first paragraph, 'dans RHom(E,F)|U'",
    "double-struck R and Hom underlined (both scans; crops_156_160/p156_RHom.png)", RHOM_TEX,
    "font", "high", fx(r"\RHom(E,F)|U", RHOM_NEW + "(E,F)|U"),
    "Same form as main.tex line 2622 (f^*\\mathbb{R}\\underline{\\Hom}(F,G)).")
add(156, "first paragraph, '(resp. RHom(F,E)|U)'",
    "double-struck R and Hom underlined (both scans)", RHOM_TEX,
    "font", "high", fx(r"\RHom(F,E)|U", RHOM_NEW + "(F,E)|U"), "As the entry before.")
add(156, "display 'u (x)L v : A|U --> (RHom(E,F) (x)L RHom(F,E))|U .', first factor",
    "double-struck R and Hom underlined (both scans)", RHOM_TEX,
    "font", "high", fx(r"(\RHom(E,F)\otL", "(" + RHOM_NEW + r"(E,F)\otL"), "As above.")
add(156, "same display, second factor",
    "double-struck R and Hom underlined (both scans)", RHOM_TEX,
    "font", "high", fx(r"\RHom(F,E))|U", RHOM_NEW + "(F,E))|U"), "As above.")
add(156, "Proposition 8.3, first sentence",
    "underlined: 'Dans la situation de', 'pour', 'et', 'on a'; '(8.2),' and the formulas not (both scans)",
    "no emphasis (the statements of Exposé I up to 7.3 have \\emph)",
    "underline", "high",
    fx(r"Dans la situation de (8.2), pour \(u\in\Hom(E|U,F|U)\) et \(v\in\Hom(F|U,E|U)\), on a",
       r"\emph{Dans la situation de} (8.2), \emph{pour} \(u\in\Hom(E|U,F|U)\) \emph{et} \(v\in\Hom(F|U,E|U)\), "
       r"\emph{on a}"),
    "Statements are in roman in main.tex from Lemme 7.4 (line 3499) to the end of Exposé I (7.4-7.8 lie on pp. "
    "152-155); here fixed singly, by the print's word groups.")
add(156, "Proposition 8.3, 'En particulier, si E = F, on a'",
    "underlined: 'En particulier', 'si', 'on a' (both scans)", "no emphasis",
    "underline", "high",
    fx(r"En particulier, si \(E=F\), on a", r"\emph{En particulier}, \emph{si} \(E=F\), \emph{on a}"),
    "Part of the statement of 8.3.")
add(156, "diagrams printed at the top of p. 157 (in the TeX under the folio-156 marker): left triangle, vertical arrow",
    "label Id (x)^L tau_F: an L over the tensor sign (both scans; crops_156_160/p157_tri_labels.png)",
    r'\arrow[d,"\Id\otimes\tau_F"]',
    "formula", "high", fx(r'\arrow[d,"\Id\otimes\tau_F"]', r'\arrow[d,"\Id\otL\tau_F"]'),
    "Filed under p. 156 because the diagram stands in page_156.tex now: apply before the folio-157 marker move. The "
    "old string is also unique in pp. 156-157 together (the square's arrow has \"'] ).")
add(156, "diagrams printed at the top of p. 157: right triangle, vertical arrow",
    "label tau_E (x)^L Id: an L over the tensor sign (both scans; crops_156_160/p157_tri_labels.png)",
    r'\arrow[d,"\tau_E\otimes\Id"]',
    "formula", "high", fx(r'\arrow[d,"\tau_E\otimes\Id"]', r'\arrow[d,"\tau_E\otL\Id"]'),
    "As the entry before (filed under p. 156; apply before the marker move).")

# ---------------------------------------------------------------- page 157
add(157, "start of page",
    "p. 157 begins with the two triangle diagrams (A --u(x)v--> E^v(x)F(x)F^v(x)E, with vu and uv), then the square; "
    "p. 156 ends '... (laquelle est de vérification \"purement mécanique\") :' and its footnote (both scans)",
    "the display of the two triangles and the opening '\\[' '\\begin{tikzcd}[column sep=' of the square are the last "
    "lines of page_156.tex (under the folio-156 marker); the folio-157 marker stands inside the square's option list, "
    "page_157.tex begins 'large,row sep=large]'",
    "marker", "high", None,
    "Page 157 really begins with the '\\[' that opens the two triangles, right after '«~purement mécanique~») :'. "
    "Move the folio-157 marker up past two '\\[': python -I move_marker.py 6 157 '\\[' --before, run twice (the first "
    "run sets it above the square's '\\[', the second above the triangles' '\\['). Simulated on both layers, before and "
    "after this batch's fixes (crops_156_160/sim_markers2.py): '... mécanique~») :', the marker, '\\[', "
    "'\\begin{tikzcd}[column sep=large,row sep=large]', ' A \\arrow[r,\"u\\otL v\"] ...'; page 156 then ends with "
    "' :' and holds no tikzcd. The square's options stay split as 'column sep=' / 'large,row sep=large]' (compiles).")
add(157, "square diagram, top arrow",
    "label Id (x)^L tau_E: an L over the tensor sign (both scans; crops_156_160/p157_square_top.png, w157_square.png)",
    r'\arrow[r,"\Id\otimes\tau_E"]',
    "formula", "high", fx(r'\arrow[r,"\Id\otimes\tau_E"]', r'\arrow[r,"\Id\otL\tau_E"]'),
    "The other labels with L: the two triangles (p. 156 entries).")
add(157, "square diagram, left vertical arrow",
    "label Id (x) tau_F: plain tensor sign, no L (both scans; crops_156_160/w157_square.png)",
    r'\arrow[d,"\Id\otimes\tau_F"' + "']" + " (keeps the printed reading)",
    "misprint_in_print", "low", None,
    "The same arrow is labelled Id (x)^L tau_F in the left triangle, and the three other tensor labels of the "
    "diagrams carry the L: the typist left out the L here.",
    corrected=r"\Id\otL\tau_F")
add(157, "Corollaire 8.4, statement",
    "underlined: 'étant donnés comme en', 'soient', 'un isomorphisme', 'd'où', 'On a alors'; 'E, F, U', '(8.2),' "
    "and the formulas not (both scans)",
    "no emphasis",
    "underline", "high",
    fx(r"\(E,F,U\) étant donnés comme en (8.2), soient \(u\in\Hom(E|U,E|U)\), \(s:E|U\to F|U\) un isomorphisme, "
       r"d'où \(sus^{-1}\in\Hom(F|U,F|U)\). On a alors",
       r"\(E,F,U\) \emph{étant donnés comme en} (8.2), \emph{soient} \(u\in\Hom(E|U,E|U)\), \(s:E|U\to F|U\) "
       r"\emph{un isomorphisme}, \emph{d'où} \(sus^{-1}\in\Hom(F|U,F|U)\). \emph{On a alors}"),
    "As Proposition 8.3 (p. 156).")
add(157, "Remarque 8.5, 'notons E(C) la S-catégorie fibrée'",
    "plain typed capital E, not underlined (both scans; crops_156_160/w157_rem_lines.png)",
    r"\mathcal E", "font", "high", fx(r"\(\mathcal E(\mathcal C)\)", r"\(E(\mathcal C)\)"),
    "The five \\mathcal E of main.tex that stand for this E (pp. 157-158) are each listed; the print types E like the "
    "complex E elsewhere on the page.")
add(157, "Remarque 8.5, 'S-foncteur de E(D(S)_parf)^is dans A'",
    "plain typed E (both scans)", r"\mathcal E", "font", "high",
    fx(r"de \(\mathcal E(", r"de \(E("), "As the entry before.")
add(157, "Remarque 8.5, same formula, index of D(S)",
    "the index 'parf' underlined (both scans; witness p. 157)", r"\Dpx(S)_{\parf} (no underline)",
    "underline", "high", fx(r"\parf})^{\mathrm{is}}\)", r"\underline{\parf}})^{\mathrm{is}}\)"),
    "The underlined index is the notation of 5.8.4 b) (perfect and of finite tor-dimension), as fixed on pp. 137-138 "
    "(\\Dpx({}_A S)_{\\underline{\\mathrm{parf}}}); 8.1 refers to it. The target of the forgetful functor in the "
    "display and the index on p. 158 are plain parf in the print.")
add(157, "Remarque 8.5, 'dans A (où l'exposant is signifie'",
    "A underlined (both scans)", r"\mathcal A",
    "font", "high", fx(r"dans \(\mathcal A\)", r"dans \(\underline A\)"),
    "The discrete S-category defined by the sheaf A (6.6 a)), which the TeX writes \\underline F for a sheaf F "
    "(main.tex lines 3239-3300); the print underlines the typed A.")
add(157, "Remarque 8.5, 'et A est la S-catégorie à fibres discrètes'",
    "A underlined (both scans)", r"\mathcal A",
    "font", "high", fx(r"et \(\mathcal A\) est", r"et \(\underline A\) est"), "As the entry before.")
add(157, "display of the forgetful functor, source",
    "plain typed E (both scans)", r"\mathcal E", "font", "high",
    fx(r"\[" + NL + r"  \mathcal E(", r"\[" + NL + r"  E("), "As above.")
add(157, "display of the forgetful functor, index of the source",
    "'parf' underlined in the source, plain in the target (both scans; witness p. 157)",
    r"\Dpx(S)_{\parf} on both sides", "underline", "high",
    fx(r"\parf})^{\mathrm{is}}" + NL + r"  \longrightarrow", r"\underline{\parf}})^{\mathrm{is}}" + NL + r"  \longrightarrow"),
    "The print maps E(D(S)_parf-underlined)^is to E(D(S)_parf)^is (finite tor-dimension forgotten); the TeX has the same "
    "category on both sides.")
add(157, "display of the forgetful functor, target",
    "plain typed E (both scans)", r"\mathcal E", "font", "high",
    fx(r"  \mathcal E(\Dpx(S)_{\parf})^{\mathrm{is}}" + NL + r"\]", r"  E(\Dpx(S)_{\parf})^{\mathrm{is}}" + NL + r"\]"),
    "As above; the index of the target stays plain.")

# ---------------------------------------------------------------- page 158
add(158, "line 1, 'S-foncteur de E(D(S)_parf)^is dans A.'",
    "plain typed E (both scans)", r"\mathcal E", "font", "high",
    fx(r"de \(\mathcal E(", r"de \(E("), "As p. 157. The index parf is plain here in the print, as in the TeX.")
add(158, "line 1, 'dans A.'",
    "A underlined (both scans)", r"\mathcal A", "font", "high",
    fx(r"dans \(\mathcal A\).", r"dans \(\underline A\)."), "As p. 157.")
add(158, "Proposition 8.6, statement",
    "underlined: 'Soient', 'd'où', 'On a'; the formulas not (both scans)", "no emphasis",
    "underline", "high",
    fx(r"Soient \(U\in\Ob S\), \(E,F\in\Parf(U)\), \(u\in\Hom(E,E)\), \(v\in\Hom(F,F)\), d'où "
       r"\(u\otL v\in\Hom(E\otL F,E\otL F)\). On a",
       r"\emph{Soient} \(U\in\Ob S\), \(E,F\in\Parf(U)\), \(u\in\Hom(E,E)\), \(v\in\Hom(F,F)\), \emph{d'où} "
       r"\(u\otL v\in\Hom(E\otL F,E\otL F)\). \emph{On a}"),
    "As Proposition 8.3 (p. 156).")
add(158, "heading of the bibliography (printed at the top of p. 159; the TeX has it under the folio-158 marker)",
    "BIBLIOGRAPHIE: typed capitals, no underline (both scans)", r"\section*{Bibliographie}",
    "word", "medium", fx(r"\section*{Bibliographie}", r"\section*{BIBLIOGRAPHIE}"),
    "Filed under p. 158 because the line stands in page_158.tex now: apply before the folio-159 marker move (the "
    "marker command's anchor '\\section*{' works before or after this edit). As the p. 19 heading (applied: "
    "\\section*{\\underline{BIBLIOGRAPHIE}}, which the print underlines there).")

# ---------------------------------------------------------------- page 159
add(159, "start of page",
    "p. 159 begins with the heading BIBLIOGRAPHIE; p. 158 ends '... On termine grâce à (8.1.1).' (both scans)",
    "\\section*{Bibliographie}, \\begin{description}[...] and '\\item[{[H]}]' are the last lines of page_158.tex "
    "(under the folio-158 marker); page_159.tex begins 'Hartshorne, R.'",
    "marker", "high", None,
    "Page 159 really begins with the heading. Move the folio-159 marker above it: python -I move_marker.py 6 159 "
    "'\\section*{' --before (the nearest '\\section*{' before the marker is this heading, before or after the "
    "BIBLIOGRAPHIE edit; simulated on both layers, crops_156_160/sim_markers2.py: '... grâce à (8.1.1).', blank line, "
    "the marker, the heading, '\\begin{description}...', '\\item[{[H]}]', 'Hartshorne, R. ...'). A heading at the top "
    "of a page, which the script did not move.")
BIB = [("[H]", r"Residues and Duality"), ("[V]", r"Catégories dérivées"), ("[G]", r"Cohomologie non abélienne"),
       ("SGA 4", r"Cohomologie étale des schémas"), ("SGA 5", r"Cohomologie \(\ell\)-adique et fonctions L"),
       ("[1]", r"Topos annelés et schémas relatifs"), ("[2]", r"Les catégories dérivées des catégories abéliennes"),
       ("[MULT]", r"Homological Algebra")]
for i, (lab, title) in enumerate(BIB):
    add(159, "bibliography entry " + lab + ", title",
        "title in plain type, not underlined (both scans)", r"\emph{" + title + "}",
        "font", "high", fx(r"\emph{" + title + "}", title),
        "The typescript neither underlines nor italicizes the titles; same fix as the p. 19 bibliography (applied)."
        if i == 0 else "As entry [H].")

# ---------------------------------------------------------------- page 160
add(160, "exposé heading",
    "'Exposé II' on a line of its own, underlined, no full stop; the title on the next line (both scans)",
    r"\section*{Exposé II. Existence de résolutions globales}: number and title run together with a full stop",
    "punctuation", "medium", fx(r"\section*{Exposé II. ", r"\section*{\underline{Exposé II}\\[3pt] "),
    "Form of the applied headings of p. 1 (\\section*{\\underline{Exposé 0}}) and p. 78 (two-line title with "
    "\\\\[3pt]). Apply together with the next entry (the two edits make one heading); if exposé headings are to stay "
    "without underline, drop \\underline and keep the line break.")
add(160, "exposé title",
    "EXISTENCE DE RÉSOLUTIONS GLOBALES: capitals (the accent of RÉSOLUTIONS added by hand), double underline (both "
    "scans)",
    "Existence de résolutions globales (small letters, no underline)",
    "word", "medium", fx(r"Existence de résolutions globales}", r"\underline{\underline{EXISTENCE DE RÉSOLUTIONS GLOBALES}}}"),
    "As the applied p. 78 title (\\underline{\\underline{GÉNÉRALITÉS ...}}).")
add(160, "author line",
    "par L. ILLUSIE: the name in capitals, the line underlined (both scans)", "par L. Illusie",
    "word", "medium", fx(r"par L. Illusie", r"\underline{par L. ILLUSIE}"), "As the applied p. 78 author line.")
add(160, "Proposition 1.1 (all statements of Exposé II)",
    "the statement is underlined by word groups: 'Soit', 'et supposons que'; (i) 'est quasi-relevable dans', 'étant "
    "considérée comme catégorie fibrée sur un site ponctuel'; 'Alors'; b) 'Soient', 'et', 'Si', 'est', "
    "'-pseudo-cohérent', 'En d'autres termes', 'on a'; 'En outre', 'le foncteur canonique', 'où', 'désigne la "
    "sous-catégorie épaisse de', 'formée des com-' (both scans)",
    "roman throughout",
    "underline", "high", None,
    "Convention of the transcription: no statement of Exposé II is underlined in main.tex (lines 3744-4778 use \\emph "
    "only for 'Preuve.' and some defined terms: famille ample 4065, divisoriel 4067, mou 4186, Stein 4230). Three "
    "examples on this page: 'Soit S in ob S, et supposons que :', '(i) C_oS est quasi-relevable dans C_S', 'Alors :'. "
    "One pass for the exposé (word groups or one block per statement, see the pending block decision).")

# ---------------------------------------------------------------- checks
texts = {p: (B / f"page_{p}.tex").read_text(encoding="utf-8") for p in range(156, 161)}
bad = 0
for d in F:
    fx_ = d["fix"]
    if not fx_:
        continue
    t = texts[d["page"]]
    n = t.count(fx_["old"])
    if n != 1 or MARK.search(fx_["old"]) or MARK.search(fx_["new"]):
        bad += 1
        print("BAD", d["page"], n, repr(fx_["old"][:60]))
# simulate all fixes per page in order: each old must still occur once when its turn comes
for p in range(156, 161):
    t = texts[p]
    for d in F:
        if d["page"] != p or not d["fix"]:
            continue
        o, nw = d["fix"]["old"], d["fix"]["new"]
        n = t.count(o)
        if n != 1:
            bad += 1
            print("BAD-SEQ", p, n, repr(o[:60]))
        t = t.replace(o, nw, 1)
counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0])
    c[1 if d["kind"] == "misprint_in_print" else 0] += 1
print("counts", counts, "total", len(F), "bad", bad)
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("wrote", OUT)
