"""Build findings_541_545.json and check that every fix's old (and every misprint's tex) occurs exactly once
in its page_NNN.tex."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
B = HERE.parent / "b541_545"
OUT = HERE.parent / "findings_541_545.json"

F = []


def add(**kw):
    F.append(kw)


# ---------------- page 541 ----------------
add(page=541,
    where="top of the page: display (3.3.1)",
    scan="the page opens with the display '(3.3.1)  f^* : Gr.(X) --> Gr.(X') .'; p. 540 ends with "
         "'d'où un homomorphisme de degré d de groupes abéliens gradués' (scan of p. 540 checked)",
    tex=r"page_541.tex opens with '\end{equation}'; '\begin{equation}\tag{3.3.1}' and ' f^*:\Grb(X)\longrightarrow\Grb(X').' "
        r"stand above the folio-541 marker, at the end of page_540.tex",
    kind="marker", confidence="high", fix=None,
    note=r"Page 541 really begins at '\begin{equation}\tag{3.3.1}' (the marker now splits the equation environment). "
         r"Exact edit in main.tex, both layers: python -I move_marker.py 6 541 '\begin{equation}\tag{3.3.1}' --before; "
         r"that is, replace 'gradués\n\begin{equation}\tag{3.3.1}\n f^*:\Grb(X)\longrightarrow\Grb(X').\n"
         r"%%%%%%%%%%  scan idx 554  |  folio 541  %%%%%%%%%%\n\end{equation}' by 'gradués\n"
         r"%%%%%%%%%%  scan idx 554  |  folio 541  %%%%%%%%%%\n\begin{equation}\tag{3.3.1}\n"
         r" f^*:\Grb(X)\longrightarrow\Grb(X').\n\end{equation}' (diplomatic about line 13976, current about 13982 "
         r"at the time of checking; the files are being edited).")

add(page=541,
    where="3.4, 'et si X' = P_X(E)'",
    scan="plain typed P (no double stroke, no underline) in P_X(E), both scans; the E is underlined",
    tex=r"\(X'=\mathbf P_X(E)\)",
    kind="font", confidence="medium",
    fix={"old": r"\mathbf P_X", "new": r"P_X"},
    note=r"The only \mathbf P of Exposé X; the print types a plain P here (crops_541_545/p541_PXE.png, witness "
         r"wit_541_half.png). Medium: one of the places of the projective-bundle letter if the volume writes it "
         r"uniformly. The underlined E is in the Module-letter convention entry below.")

add(page=541,
    where="4.1, 'on obtient un accouplement appelé \"nombre d'intersection\" :'",
    scan="\"nombre d'intersection\" with both words underlined",
    tex="«~nombre d'intersection~»",
    kind="underline", confidence="high",
    fix={"old": "«~nombre d'intersection~»", "new": r"«~\emph{nombre d'intersection}~»"},
    note=r"Defined term underlined in the print. This exposé writes underlined words with \emph "
         r"(p. 544 '\emph{nombre d'intersection}', p. 542 '\emph{nombre de Chern}').")

add(page=541,
    where="throughout pp. 541-545 (all places listed in the note)",
    scan="letters that name Modules are underlined (E, F, G, L_1,...,L_d, F_x); the same letters are plain where "
         "they name classes (L_i in Pic(X) and in c_1(L_i), F in chi(L_1^{n_1}...F), the left sides of "
         "'L_i = cl°(L_i)', 'F = cl.(F)')",
    tex=r"plain E, F, G, L_i; the TeX underlines only '\cl^\circ(\underline L_i)' and '\cl_\bullet(\underline F)' "
        r"(p. 542)",
    kind="underline", confidence="high", fix=None,
    note=r"CONVENTION of the Exposé X TeX (11 \underline in the whole exposé), not itemized except p. 544 "
         r"'\cl_\bullet(F)=F' (own entry); not a blind script, because the print separates the Module from its "
         r"class (4.3: L_i = cl°(L_i underlined), F = cl.(F underlined)). Three examples: p. 541 'où \(E\) est un' -> "
         r"'où \(\underline E\) est un'; p. 542 '\(\dim(\Supp(F))\leq d\)' -> '\(\dim(\Supp(\underline F))\leq d\)'; "
         r"p. 545 'D'autre part' display '(L_1,\ldots,L_d;\mathcal O_X)' -> "
         r"'(\underline L_1,\ldots,\underline L_d;\mathcal O_X)'. All places on pp. 541-545: p. 541 P_X(E), 'où E est'; "
         r"p. 542 'L_1,...,L_d de O_X-modules', 'cohérent F', 'Supp(F)'; p. 543 '|F|' five times ((4.3.2), 'où |F|', "
         r"the unnumbered display, (4.3.4) twice) and 'la classe de F'; p. 544 'inversibles L_1,...,L_d avec F', "
         r"'(L_1,...,L_d;F) (cf. [3])', 'Supp(F)', '\"additif\" en F', (4.4.1) L_1,...,L_d and F on the left, F_x, "
         r"L_1,...,L_d on the right, 'et G un', 'F = f_*(G)' (F and G), the display "
         r"'(f^*L_1,...,f^*L_d;G) = (L_1,...,L_d;F)', and (4.4.3) (in page_544.tex, printed on p. 545) all L_i; p. 545 "
         r"all L_i of the displays after 'il en découle que' and 'D'autre part 2° donne'.")

# ---------------- page 542 ----------------
add(page=542,
    where="Exemple 4.2, 'par exemple y = cl.(O_Z), ou Z est un sous-schéma intègre'",
    scan="'ou Z' without the grave accent (both scans; the typist's où elsewhere on these pages has a clear accent)",
    tex=r"ou \(Z\)",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"où \(Z\)",
    note="Typing slip: 'où' (where) is meant. The TeX keeps the printed reading.")

add(page=542,
    where="display defining c_i(x)",
    scan="c_i(x) = cl°(γ^i(x-ε(x)) ∈ Gr^i(X): three opening and two closing parentheses before ∈ (both scans)",
    tex=r"(x-\epsilon(x))\in\Gr^i(X)",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"(x-\epsilon(x)))\in\Gr^i(X)",
    note="The parenthesis opened after cl° is never closed in the print. The TeX keeps the printed reading.")

add(page=542,
    where="throughout pp. 542-544 (p. 542: \\cl^\\circ twice, K^\\circ once; p. 543: K^\\circ; p. 544: K^\\circ)",
    scan="K and cl with a raised filled dot (K˙, cl˙), both scans (crops p542_cldot.png, p542_Kdot.png); the "
         "print's degree sign of '2° donne' (p. 545) is a distinct open ring",
    tex=r"K^\circ, \cl^\circ",
    kind="symbol", confidence="high", fix=None,
    note=r"CONVENTION of the Exposé X TeX, not itemized: the raised-dot K and cl are written K^\circ and \cl^\circ on "
         r"folios 519-564 (K^\circ 55, \cl^\circ 28 in the diplomatic main.tex at the time of checking); from folio 564 "
         r"on the exposé writes K^\bullet. Three examples, in the form of the 10 Nov passes of Exposés IV and VI: "
         r"p. 542 '\cl^\circ(\gamma^i(x-\epsilon(x))' -> '\cl^{\bullet}(\gamma^i(x-\epsilon(x))'; p. 543 "
         r"'A=K^\circ(X)/\Filt^{d+1}(X)' -> 'A=K^{\bullet}(X)/\Filt^{d+1}(X)'; p. 544 '(x\in K^\circ(X),\ y\in "
         r"K_\bullet(Y))' -> '(x\in K^{\bullet}(X),\ y\in K_\bullet(Y))'. One script over Exposé X, both layers; the "
         r"2^\circ of p. 545 is a real ring and stays.")

add(page=542,
    where="display 'P(c_1(x),....,c_n(X)) ∈ Gr^n(X)'",
    scan="c_n(X) with a capital X (both scans); the other arguments are small x",
    tex=r"c_n(X))",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"c_n(x))",
    note="The Chern classes c_i(x) of x are substituted (the display of P_y(x) has c_n(x)). The TeX keeps the "
         "printed X.")

add(page=542,
    where="'On appelle nombre de Chern de x relativement à y l'entier'",
    scan="underlined: 'nombre de Chern de' and 'relativement à'; x and y plain",
    tex=r"\emph{nombre de Chern} de \(x\) relativement à \(y\)",
    kind="underline", confidence="high",
    fix={"old": r"\emph{nombre de Chern} de \(x\) relativement à",
         "new": r"\emph{nombre de Chern de} \(x\) \emph{relativement à}"},
    note="The underline runs on under the second 'de', and a second underline covers 'relativement à'.")

add(page=542,
    where="display P_y(x) = < ... >",
    scan="< P(c_1(x)),...,c_n(x), y > : the parenthesis of P closes after c_1(x) (both scans; the second ')' is "
         "heavily struck)",
    tex=r"P(c_1(x)),\ldots,c_n(x),y",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"P(c_1(x),\ldots,c_n(x)),y",
    note="The Chern number is <P(c_1(x),...,c_n(x)), y>, with P(c_1(x),...,c_n(x)) in Gr^n(X) from the display "
         "before. The TeX keeps the printed reading.")

# ---------------- page 543 ----------------
add(page=543,
    where="(4.3.2)",
    scan="< c_1(L_1)^{α_1}....c_d(L_d)^{α_d}, |F| > : c_d (both scans)",
    tex=r"c_d(L_d)",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"c_1(L_d)",
    note="First Chern classes throughout: the next display and (4.3.4) have c_1(L_d). The TeX keeps the printed "
         "c_d.")

add(page=543,
    where="display after 'le coefficient du monôme n_1^{α_1}....n_d^{α_d} est égal à'",
    scan="(1/(α_1 ! ... a_d !)): a typed Latin a in a_d, the handwritten α in α_1 (both scans)",
    tex=r"a_d!",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"\alpha_d!",
    note="Factorials of the exponents α_1, ..., α_d. The TeX keeps the printed a_d.")

add(page=543,
    where="Corollaire 4.3.3, 'dans le polynôme de Snapper χ(...)'",
    scan="χ(L_1^{α_1}...L_d^{α_d} F): exponents α_1, α_d (both scans)",
    tex=r"\chi(L_1^{\alpha_1}\cdots L_d^{\alpha_d}F)",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"\chi(L_1^{n_1}\cdots L_d^{n_d}F)",
    note="The Snapper polynomial is χ(L_1^{n_1}...L_d^{n_d}F) in the variables n_i (Prop. 4.3.1; 'monôme "
         "n_1n_2...n_d' in the same sentence). The TeX keeps the printed α_i.")

add(page=543,
    where="(4.3.5), end",
    scan="'mod.Filt^{d+1}(X) .' (typed 'mod.' with its stop, no parentheses)",
    tex=r"\pmod{\Filt^{d+1}(X)}.",
    kind="symbol", confidence="high",
    fix={"old": r"\pmod{\Filt^{d+1}(X)}", "new": r"\quad\mathrm{mod.}\Filt^{d+1}(X)"},
    note=r"\pmod adds parentheses and drops the stop of the print's 'mod.' (same form as the fixes of pp. 448, 485).")

add(page=543,
    where="Proposition 4.3.1 and Corollaire 4.3.3",
    scan="the statements underlined word group by word group ('Avec les notations ci-dessus,', 'pour toute suite', "
         "'d'entiers positifs avec', 'le coefficient de', 'dans le polynôme de Snapper', 'est égal à', 'où', 'est la "
         "classe de', 'dans', 'Donc dans le développement ordinaire de ce polynôme suivant les monômes en des', 'le "
         "coefficient du monôme', 'est égal à'; Cor. 4.3.3: 'Le coefficient du monôme', 'dans le polynôme de "
         "Snapper', 'est égal à'); formulas plain",
    tex="both statements in roman",
    kind="underline", confidence="high", fix=None,
    note=r"Exposé II pattern (GLOBAL_ISSUES 82, pending volume decision): not itemized. The TeX's \emph on "
         r"'nombre de Chern' (p. 542) and 'nombre d'intersection' (p. 544) marks terms the print underlines; no "
         r"category letter L on these pages.")

# ---------------- page 544 ----------------
add(page=544,
    where="top of the page: heading 4.4",
    scan="the page opens with '4.4. On appelle parfois l'entier (4.3.4)'; p. 543 ends with 'C.Q.F.D.'",
    tex=r"'\subsection*{4.4}' and 'On' stand at the end of page_543.tex, above the folio-544 marker; page_544.tex "
        r"opens with 'appelle parfois'",
    kind="marker", confidence="high", fix=None,
    note=r"Page 544 really begins at '\subsection*{4.4}' (a heading at the top of a page, not moved by the 10 Nov "
         r"script). Exact edit in main.tex, both layers: python -I move_marker.py 6 544 '\subsection*{4.4}' --before; "
         r"that is, replace 'C.Q.F.D.\n\n\subsection*{4.4}\nOn\n%%%%%%%%%%  scan idx 557  |  folio 544  %%%%%%%%%%\n"
         r"appelle' by 'C.Q.F.D.\n\n%%%%%%%%%%  scan idx 557  |  folio 544  %%%%%%%%%%\n\subsection*{4.4}\nOn\n"
         r"appelle' (diplomatic about line 14068, current about 14074 at the time of checking).")

add(page=544,
    where="4.4, '(cf. [3])'",
    scan="'(cf. [3] )' with 'cf.' not underlined (both scans)",
    tex=r"(\emph{cf.} [3])",
    kind="underline", confidence="high",
    fix={"old": r"(\emph{cf.} [3])", "new": r"(cf. [3])"},
    note="Emphasis the print does not have.")

add(page=544,
    where="4.4 1), 'i.e. additif en cl.(F) = F'",
    scan="cl.(F) = F with the Module F underlined inside cl. and the class F plain",
    tex=r"\cl_\bullet(F)=F",
    kind="underline", confidence="high",
    fix={"old": r"\cl_\bullet(F)=F", "new": r"\cl_\bullet(\underline F)=F"},
    note=r"Itemized although plain Module letters are a convention of this TeX (entry p. 541): this restates the "
         r"definition F = cl.(F) of 4.3, which the TeX writes '\(F=\cl_\bullet(\underline F)\)' on p. 542; with a "
         r"plain F the TeX reads cl(F) = F.")

add(page=544,
    where="(4.4.1), long_{O,x}",
    scan="'long' with the subscript O (underlined) followed by ',x' at the lower level, no X; both scans show the "
         "gap where the X would stand",
    tex=r"\mathcal O_{,x}",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"\mathcal O_{X,x}",
    note="The local ring O_{X,x}, printed in full in (4.4.4) on p. 545 (long_{O_{X,x}}). The TeX keeps the printed "
         "reading. Medium: the typist left the space for the X.")

add(page=544,
    where="(4.4.3), left side (in page_544.tex; printed at the top of p. 545)",
    scan="(f^* L_1,...,f^* L_d ;O_Y): this O_Y is typed without its underline (both scans); the O_X on the right "
         "is underlined",
    tex=r"f^*L_d;\mathcal O_Y)",
    kind="underline", confidence="low",
    fix={"old": r"f^*L_d;\mathcal O_Y)", "new": r"f^*L_d;O_Y)"},
    note=r"\mathcal O stands for the typescript's underlined O (pending volume decision); this is the only structure "
         r"sheaf without its underline on pp. 541-545. The string lies in page_544.tex now; after the folio-545 "
         r"marker is moved (entry p. 545) it lies in p. 545's span.")

# ---------------- page 545 ----------------
add(page=545,
    where="top of the page: display (4.4.3)",
    scan="the page opens with '(4.4.3)  (f^* L_1,...,f^* L_d ;O_Y) = n(L_1,...,L_d ;O_X) .'; p. 544 ends with "
         "'alors on a'",
    tex=r"'\begin{equation}\tag{4.4.3}' and the three lines of the display stand at the end of page_544.tex; "
        r"page_545.tex opens with '\end{equation}'",
    kind="marker", confidence="high", fix=None,
    note=r"Page 545 really begins at '\begin{equation}\tag{4.4.3}'. Exact edit in main.tex, both layers: "
         r"python -I move_marker.py 6 545 '\begin{equation}\tag{4.4.3}' --before; that is, replace 'alors on a\n"
         r"\begin{equation}\tag{4.4.3}' by 'alors on a\n%%%%%%%%%%  scan idx 558  |  folio 545  %%%%%%%%%%\n"
         r"\begin{equation}\tag{4.4.3}' and 'n(L_1,\ldots,L_d;\mathcal O_X).\n%%%%%%%%%%  scan idx 558  |  "
         r"folio 545  %%%%%%%%%%\n\end{equation}' by 'n(L_1,\ldots,L_d;\mathcal O_X).\n\end{equation}' (diplomatic "
         r"about line 14099, current about 14105 at the time of checking).")

add(page=545,
    where="end of the page: '\\subsection*{4.5}' and 'On'",
    scan="p. 545 ends with 'd'où l'assertion.'; '4.5  On appelle équivalence numérique ...' opens p. 546 (scan of "
         "p. 546 checked)",
    tex=r"page_545.tex ends with '\subsection*{4.5}' and 'On', above the folio-546 marker",
    kind="marker", confidence="high", fix=None,
    note=r"The folio-546 marker stands two lines too late (heading at the top of a page). Exact edit in main.tex, both "
         r"layers: python -I move_marker.py 6 546 '\subsection*{4.5}' --before; that is, replace 'd'où l'assertion.\n\n"
         r"\subsection*{4.5}\nOn\n%%%%%%%%%%  scan idx 559  |  folio 546  %%%%%%%%%%\nappelle' by 'd'où l'assertion."
         r"\n\n%%%%%%%%%%  scan idx 559  |  folio 546  %%%%%%%%%%\n\subsection*{4.5}\nOn\nappelle' (diplomatic about "
         r"line 14138, current about 14143 at the time of checking).")

add(page=545,
    where="congruence display after 'Alors 1.1.2 donne les congruences'",
    scan="'≡ cl.(f_*(O_Y) ≡ long...': two opening and one closing parenthesis (both scans)",
    tex=r"\cl_\bullet(f_*(\mathcal O_Y)",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"\cl_\bullet(f_*(\mathcal O_Y))",
    note="The parenthesis opened after cl. is not closed in the print. The TeX keeps the printed reading.")

add(page=545,
    where="congruence display, last factor cl.(O_{X_red})",
    scan="subscript 'red' without accent (both scans)",
    tex=r"\cl_\bullet(\mathcal O_{X_{\red}})",
    kind="accent", confidence="high",
    fix={"old": r"\cl_\bullet(\mathcal O_{X_{\red}})", "new": r"\cl_\bullet(\mathcal O_{X_{\mathrm{red}}})"},
    note=r"\red is \text{réd} (main.tex line 44) and adds an accent the typescript does not type here; the same on "
         r"the next two displays. If the print types 'red' wherever \red is used (folios 502, 545, 599, 605-609, 647, "
         r"650, 663), redefine \red instead of these three fixes.")

add(page=545,
    where="display after 'il en découle que', last factor (L_1,...,L_d; O_{Xred})",
    scan="'O_{Xred}' with 'red' unaccented (both scans)",
    tex=r"\mathcal O_{X_{\red}}).",
    kind="accent", confidence="high",
    fix={"old": r"\mathcal O_{X_{\red}}).", "new": r"\mathcal O_{X_{\mathrm{red}}})."},
    note=r"As above (\red prints 'réd').")

add(page=545,
    where="display after 'D'autre part 2° donne', last factor",
    scan="'O_{X_red}' with 'red' unaccented (both scans)",
    tex=r"\mathcal O_{X_{\red}}),",
    kind="accent", confidence="high",
    fix={"old": r"\mathcal O_{X_{\red}}),", "new": r"\mathcal O_{X_{\mathrm{red}}}),"},
    note=r"As above (\red prints 'réd').")

# ---------------- checks ----------------
ok = True
order = ["page", "where", "scan", "tex", "kind", "confidence", "fix", "corrected", "note"]
out = []
for f in F:
    page = f["page"]
    t = (B / f"page_{page}.tex").read_text(encoding="utf-8")
    if f["fix"] is not None:
        n = t.count(f["fix"]["old"])
        if n != 1:
            ok = False
            print("FIX NOT UNIQUE", page, n, repr(f["fix"]["old"]))
        marker_lines = [ln for ln in t.split("\n") if ln.startswith("%%%%%%%%%%")]
        if any(m in f["fix"]["old"] for m in marker_lines):
            ok = False
            print("FIX CROSSES MARKER", page)
    if f["kind"] == "misprint_in_print":
        n = t.count(f["tex"])
        if n != 1:
            ok = False
            print("MISPRINT TEX NOT UNIQUE", page, n, repr(f["tex"]))
        if "corrected" not in f:
            ok = False
            print("MISSING corrected", page)
    else:
        assert "corrected" not in f
    out.append({k: f[k] for k in order if k in f})
OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
counts = {}
for f in F:
    c = counts.setdefault(f["page"], [0, 0])
    c[1 if f["kind"] == "misprint_in_print" else 0] += 1
print("ok" if ok else "PROBLEMS", len(F), counts)
