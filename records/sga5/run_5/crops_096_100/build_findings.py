"""Build findings_096_100.json and check that every fix's old occurs exactly once in its page file.
usage: python -I -B build_findings.py"""
import json
import pathlib

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
NL = "\n"
F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": confidence,
         "fix": None if fix is None else {"old": fix[0], "new": fix[1]}}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


EMPH = (r"\emph is this file's command for the print's underline in Exposé III (\emph{La flèche 1.7.3 est un "
        r"isomorphisme}, \emph{flèche de Künneth}). The items a), b) continue the underlined statement of "
        "Corollaire 3.5 (p. 95), which the TeX closes before the list.")

# ---------------------------------------------------------------- page 96
add(96, "top of the page: the list a), b) of Corollaire 3.5",
    "p. 96 begins 'a). On s'identifie u , par dualité triviale , à une flèche'; p. 95 ends 'lentes suivantes :'",
    r"page_096.tex begins at 'identifie $u$'; '\begin{enumerate}[label=\alph*)]' and '\item On s'%' stand at "
    "the end of page_095.tex, under the folio-95 marker",
    "marker", "high", None,
    r"Page 96 really begins at '\begin{enumerate}[label=\alph*)]' (s5.tex line 2727 in both layers "
    "at 19:54). Exact fix: python -I move_marker.py 5 96 '\\begin{enumerate}' --before (simulated in "
    r"memory on both layers: the marker then stands between '\end{statement}' and the list; the '%' after "
    "'s'' keeps 's'identifie' joined). The faint dot after 'a)' is smaller and lighter than the typed full "
    "stops (probably a speck): not reported.")
add(96, "a), first words: 'On s'identifie u'",
    "'a). On s'identifie u , par dualité triviale , à une flèche'",
    r"'\item On s'%' (last line of page_095.tex) + 'identifie $u$': the printed reading",
    "misprint_in_print", "high", None,
    "Stray reflexive s': b) reads 'On identifie u , par adjonction, à une flèche'. The TeX keeps the printed "
    "reading (both layers). The 's'' stands at the end of page_095.tex until the folio-96 marker is moved.",
    corrected="On identifie $u$")
add(96, "a), first line",
    "'On s'identifie', 'par dualité triviale', 'à une flèche' underlined (three runs; u and the commas not)",
    "no underline", "underline", "high",
    ("identifie $u$, par dualité triviale, à une flèche",
     r"\emph{identifie} $u$, \emph{par dualité triviale}, \emph{à une flèche}"),
    EMPH + r" The run 'On s'identifie' begins with 'On s'' on the last line of page_095.tex: apply together "
    r"with '\item On s'%' -> '\item \emph{On s'}%' there.")
add(96, "a), second line: 'on compose avec l'isomorphisme de changement de base'",
    "'on compose avec l'isomorphisme de changement de base' underlined (one run)", "no underline",
    "underline", "high",
    ("on compose avec l'isomorphisme de changement de base" + NL + r"\[" + NL + r"p_{1*}",
     r"\emph{on compose avec l'isomorphisme de changement de base}" + NL + r"\[" + NL + r"p_{1*}"),
    EMPH)
add(96, "a), end: 'f_*u est l'adjointe de cette flèche composée.'",
    "'est l'adjointe de cette flèche composée' underlined; f_*u and the full stop not", "no underline",
    "underline", "high",
    ("L_2;" + NL + r"\]" + NL + r"$f_*u$ est l'adjointe de cette flèche composée.",
     "L_2;" + NL + r"\]" + NL + r"$f_*u$ \emph{est l'adjointe de cette flèche composée}."),
    EMPH)
add(96, "b), first line",
    "'On identifie' and 'par adjonction, à une flèche' underlined (the second run goes through the inner comma)",
    "no underline", "underline", "high",
    (r"\item On identifie $u$, par adjonction, à une flèche",
     r"\item \emph{On identifie} $u$, \emph{par adjonction, à une flèche}"),
    EMPH)
add(96, "b), second line: 'on compose avec l'isomorphisme de changement de base'",
    "'on compose avec l'isomorphisme de changement de base' underlined (one run)", "no underline",
    "underline", "high",
    ("on compose avec l'isomorphisme de changement de base" + NL + r"\[" + NL + r"f_2^*",
     r"\emph{on compose avec l'isomorphisme de changement de base}" + NL + r"\[" + NL + r"f_2^*"),
    EMPH)
add(96, "b), end: 'est l'adjointe de cette flèche composée.'",
    "'est l'adjointe de cette flèche composée.' underlined, here with the full stop", "no underline",
    "underline", "high",
    ("est l'adjointe de cette flèche composée." + NL + r"\end{enumerate}",
     r"\emph{est l'adjointe de cette flèche composée.}" + NL + r"\end{enumerate}"),
    EMPH + " In b) the underline runs under the full stop (in a) it stops before it).")
add(96, "3.6, 'puis l'on applique la flèche a : H^i(X_2,p_{2!}p_2^!L_2) -> H^i(X_2,L_2)'",
    "a underlined", "plain a", "underline", "high",
    (r"a:\H^i(X_2,p_{2!}", r"\underline{a}:\H^i(X_2,p_{2!}"),
    "The arrow a is underlined at all four places of the page.")
add(96, "(3.6.1) 'u_*(x) = a(u.p_1^*x) .'", "a underlined", "plain a", "underline", "high",
    (r"=a(u\cdot p_1^*x)", r"=\underline{a}(u\cdot p_1^*x)"), "As in the line above.")
add(96, "after (3.6.1): new paragraph 'Soient c : C -> X un morphisme propre'",
    "'Soient' indented: a new paragraph after (3.6.1)",
    r"'Soient' follows \end{equation} without a blank line (the paragraph runs on)", "other", "high",
    (r"\end{equation}" + NL + "Soient", r"\end{equation}" + NL + NL + "Soient"),
    "As the paragraph breaks added on p. 62.")
add(96, "(3.6.2) 'u_*(x) = a(u.c_1^*x) ,'", "a underlined", "plain a", "underline", "high",
    (r"=a(u\cdot c_1^*x)", r"=\underline{a}(u\cdot c_1^*x)"), "As in (3.6.1).")
add(96, "'et a : H^i(X_2,c_{2!}c_2^!L_2) -> H^i(X_2,L_2) est la flèche déduite'", "a underlined", "plain a",
    "underline", "high",
    (r"a:\H^i(X_2,c_{2!}", r"\underline{a}:\H^i(X_2,c_{2!}"), "As in (3.6.1).")
add(96, "'est la flèche déduite de l'adjonction c_{2!}c_2^!L_2 -> Id'",
    "c_{2!}c_2^!L_2 ⟶ Id", r"$c_{2!}c_2^!L_2\to\Id$ (as printed)", "misprint_in_print", "low", None,
    "The adjunction arrow is c_{2!}c_2^! -> Id (as 'p_{2!}p_2^! -> Id' before (3.6.1)), or c_{2!}c_2^!L_2 -> L_2 "
    "with L_2; the stray L_2 repeats the source of the arrow a in the line above. An author's slip rather than a "
    "typing error; the TeX keeps the printed reading. For review before the corrected edition.",
    corrected=r"$c_{2!}c_2^!\to\Id$")
add(96, "(3.6.3) 'cℓ(c,N)_*(x)'; also p. 97: 'cℓ(c)_*', (3.6.4) twice, 'où cℓ(C) ∈ H_C^{2(r_1-N)}'",
    "cℓ with the typewriter's script ℓ (the typed l of 'classe' is a different letter)",
    r"\operatorname{cl} (roman l), five times on pp. 96-97", "font", "high", None,
    r"Convention of the transcription (\operatorname{cl} and \cl throughout Exposé III); not listed per "
    r"occurrence. One decision: c\ell (e.g. \mathrm{c}\ell) where the print has the script ℓ.")
add(96, "17 formulas on pp. 96-100 that the print runs into the text: p. 96 nine (L_1 -> p_{1*}p_2^!L_2 ; "
    "p_{1*}p_2^!L_2 ->~ f_1^!f_{2*}L_2 ; p_{2!}p_1^*L_1 -> L_2 ; f_2^*f_{1!}L_1 ->~ p_{2!}p_1^*L_1 ; "
    "u ∈ Hom_S(L_1,L_2) = ... ; u.p_1^*x ∈ ... ; a : H^i(X_2,p_{2!}p_2^!L_2) -> ... ; u_* ∈ Hom(RΓ_c...) ; "
    "a : H^i(X_2,c_{2!}c_2^!L_2) -> ...), p. 97 six (Tr_{c_2} : ..., Tr_{p_2} : ..., u_* : H_c^i(X_1,L_1) -> ..., "
    "H_c^i(X_1,L_1) -> H^i(X_2,F^*L_1), Rf_{1!}L_1 -> Rf_{2*}F^*L_1, Rf_{1!}L_1 -> Rf_{1*}L_1), p. 99 one "
    "(DL_i ⊗ L_i -> K_{X_i}), p. 100 one (c_*c^!P ⊗ d_*d^!Q -> e_*(c^!P ⊗_X d^!Q))",
    "formulas run into the text lines", r"set as \[ ... \] displays", "other", "high", None,
    "Layout convention of the transcription; the content agrees. Not listed per occurrence.")

# ---------------------------------------------------------------- page 97
add(97, "top of the page: 'où Tr_{c_2} : ...'",
    "p. 97 begins 'où Tr_{c_2} : H^i(X_2,Rc_{2!}A_C) -> ...'; p. 96 ends with the display (3.6.3)",
    "'où' is the last line of page_096.tex, under the folio-96 marker", "marker", "high", None,
    "Page 97 really begins at 'où' (s5.tex line 2787 in both layers at 19:54). Exact fix: "
    "python -I move_marker.py 5 97 'où' --before (simulated in memory on both layers: the marker then stands "
    r"between the \end{equation} of (3.6.3) and 'où').")
add(97, "'noté η_{X_2X_1} dans (loc. cit.)'", "η_{X_2X_1}: no comma between X_2 and X_1",
    r"\eta_{X_2,X_1}", "punctuation", "high",
    (r"\eta_{X_2,X_1}", r"\eta_{X_2X_1}"), "Comma added by the TeX.")
add(97, "'Tr_{p_2} : H^*(X_2,Rp_{2!}A_{X_2}) -> H^{*-2r_1}(X_2,A(-r_1))'", "Rp_{2!}A_{X_2}", r"\R p_{2!}A_{X_2} (as printed)",
    "misprint_in_print", "high", None,
    "p_2 : X -> X_2, so Rp_{2!} applies to a sheaf on X: the constant sheaf A_X (the trace of the smooth p_2 of "
    "relative dimension r_1 goes from R^{2r_1}p_{2!}A_X(r_1) to A_{X_2}). Wrong index; the TeX keeps the printed "
    "reading; the corrected layer already has A_X.",
    corrected=r"\R p_{2!}A_X")
add(97, "heading of no. 3.6.5", "'3.6.5.' with a full stop", r"\subsection*{3.6.5}", "punctuation", "high",
    (r"\subsection*{3.6.5}", r"\subsection*{3.6.5.}"),
    "The other numbers of the page and of p. 96 (3.6, 3.7) have none; 3.6.5 has one.")
add(97, "square (3.7.1), label of the bottom arrow D -> Y", "d above the arrow (as c above the top arrow)",
    r'\arrow[l,"d"]: tikz-cd sets the label of a leftward arrow below it', "other", "high",
    (r'\arrow[l,"d"]', r'\arrow[l,"d"' + "'" + "]"),
    r'c (\arrow[l,"c"' + "'" + "], above), f (left) and g (right) are right as they stand.")
add(97, "square (3.7.1), after the diagram", "a comma after the square", "no punctuation", "punctuation",
    "high", (r"\end{tikzcd}" + NL + r"\tag{3.7.1}", r"\end{tikzcd}\quad ," + NL + r"\tag{3.7.1}"),
    r"The form the file uses after diagrams (\end{tikzcd}\quad , and \end{tikzcd}\quad . in Exposé I).")

# ---------------------------------------------------------------- page 98
add(98, "after (3.7.2), the full stop", "a full stop after the diagram (far right, at the level of D)",
    "no punctuation", "punctuation", "high",
    (r"\end{tikzpicture}" + NL + r"\tag{3.7.2}", r"\end{tikzpicture}\quad ." + NL + r"\tag{3.7.2}"),
    r"As \end{tikzpicture}\quad , in Exposé I.")
add(98, "diagram (3.7.2), label of the arrow D -> Y", "d above the arrow", r"node[below] {$d$}", "other", "high",
    (r"node[below] {$d$}", r"node[above] {$d$}"),
    "The other labels (c, i, c' above; f left; g', g right) are placed as printed.")
add(98, "'défini par l'isomorphisme canonique g'_*d'^! ->~ d^!f_* (SGA 4 XVIII 3.1.12.3)'",
    "g'_*d'^! (the letter d, as in d^!f_* on the right)", r"$g'_*c'^!\xrightarrow{\sim}d^!f_*$",
    "misprint_in_print", "high",
    (r"g'_*c'^!\xrightarrow", r"g'_*d'^!\xrightarrow"),
    "There is no d' in (3.7.2): for the cartesian square C' = X x_Y D (c' : C' -> X, g' : C' -> D) the base "
    "change isomorphism is g'_*c'^! ->~ d^!f_*, the one used in the display just above (d_*g'_*c'^!K ->~ "
    "d_*d^!f_*K). The TeX silently corrects; the fix restores the printed reading (diplomatic layer only).",
    corrected=r"$g'_*c'^!\xrightarrow{\sim}d^!f_*$")

# ---------------------------------------------------------------- page 99
add(99, "heading of § 4, top of the page",
    "'4. Accouplements de correspondances. Formule de Lefschetz.': the number 4. and a full stop",
    r"\section*{Accouplements de correspondances. Formule de Lefschetz} (no number, no full stop)",
    "number", "high",
    (r"\section*{Accouplements de correspondances. Formule de Lefschetz}",
     r"\section*{4. Accouplements de correspondances. Formule de Lefschetz.}"),
    r"As the heading of § 1 on p. 76; the underline is the accepted \section* setting.")
add(99, "after (4.1.4): new paragraph 'On peut encore considérer 4.1.2'",
    "'On peut encore' indented: a new paragraph",
    r"'On peut encore' follows \end{equation} without a blank line", "other", "high",
    (r"\end{equation}" + NL + "On peut encore", r"\end{equation}" + NL + NL + "On peut encore"),
    "As on p. 96 ('Soient').")
add(99, "every derived tensor of pp. 99-100: p. 99 ten ((4.1.1); (4.1.2) three; (4.1.3); DL_i ⊗ L_i; "
    "DL_1 ⊗_S L_2 and L_1 ⊗_S DL_2; (4.2.1) two), p. 100 thirteen",
    "plain typed L above ⊗ (index S or X below the ⊗)", r"\overset{\mathbf L}{\otimes} (bold L)", "font",
    "high", None,
    r"Not the form of the 11 Nov Exposé III decision (\overset{\mathrm{L}}{\otimes}): that pass converted "
    r"\otimes^L and \otimes^{L} only. The diplomatic s5.tex still has 66 \overset{\mathbf L}{\otimes} in "
    "Exposé III (folios 89: 6, 93: 5, 94: 12, 95: 20, 99: 10, 100: 13). Not listed per occurrence.")

# ---------------------------------------------------------------- page 100
add(100, "top of the page: display (4.2.1)",
    "p. 100 begins with (4.2.1) 'c^!P ⊗_X d^!Q -> e^!(P ⊗ Q) ,'; p. 99 ends '(qui n'est pas un isomorphisme "
    "en général)'",
    "the (4.2.1) equation stands at the end of page_099.tex, under the folio-99 marker", "marker", "high", None,
    r"Page 100 really begins at the '\begin{equation}' of (4.2.1) (s5.tex line 2929 in both layers "
    "at 19:54). Exact fix: python -I move_marker.py 5 100 '\\begin{equation}' --before (simulated "
    "in memory on both layers: the marker then stands between '... en général)' and the equation).")
add(100, "composed arrow after 'comme adjointe de la flèche composée', first arrow",
    "(1) above the arrow, ≃ below it", r"\xrightarrow[(1)]{\sim}: ∼ above, (1) below", "symbol", "high",
    (r"\xrightarrow[(1)]{\sim}", r"\xrightarrow[\simeq]{(1)}"),
    "Label and sign swapped, and the print's sign is ≃ (tilde over a bar), not ∼. The (2) of the second "
    "arrow is right.")
add(100, "number of the second pairing", "(4.2.4)' : the prime after the closing parenthesis",
    r"\tag{4.2.4'} (prints (4.2.4'))", "number", "high",
    (r"\tag{4.2.4'}", r"\tag*{(4.2.4)'}"), r"\tag* is amsmath.")
add(100, "after (4.2.5): new paragraph 'Ces accouplements sont compatibles'",
    "'Ces accouplements' indented: a new paragraph",
    r"'Ces accouplements' follows \end{equation} without a blank line", "other", "high",
    (r"\end{equation}" + NL + "Ces accouplements", r"\end{equation}" + NL + NL + "Ces accouplements"),
    "As on pp. 96 and 99.")
add(100, "the two squares 'E' ... étale au-dessus de E ...', after the diagram",
    "a comma after the right-hand square", "no punctuation", "punctuation", "high",
    (r"\end{tikzcd}" + NL + r"\]" + NL + "si l'on note", r"\end{tikzcd}\quad ," + NL + r"\]" + NL + "si l'on note"),
    "As after (3.7.1).")
add(100, "last line: 'E' -> E -> X , on a un carré commutatif'",
    "no full stop: the page ends with 'commutatif' and the square (4.2.6) follows on p. 101",
    "'on a un carré commutatif.'", "punctuation", "high",
    ("carré commutatif.", "carré commutatif"), "Full stop added by the TeX.")

# ---------------------------------------------------------------- check and write
ok = True
for d in F:
    if d["fix"] is None:
        continue
    text = (RUN / "b096_100" / f"page_{d['page']:03d}.tex").read_text(encoding="utf-8")
    n = text.count(d["fix"]["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE", d["page"], n, repr(d["fix"]["old"]))
    if "%%%%%%%%%%" in d["fix"]["old"] or "%%%%%%%%%%" in d["fix"]["new"]:
        ok = False
        print("MARKER IN FIX", d["page"], repr(d["fix"]["old"]))
    if d["fix"]["old"] == d["fix"]["new"]:
        ok = False
        print("NO CHANGE", d["page"], repr(d["fix"]["old"]))
print("all olds unique:", ok)
counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0])
    c[1 if d["kind"] == "misprint_in_print" else 0] += 1
print("counts (normal/misprint):", counts, "total", len(F))
out = RUN / "findings_096_100.json"
out.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
json.loads(out.read_text(encoding="utf-8"))
print("written", out)
