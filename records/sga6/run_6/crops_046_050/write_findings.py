"""Build findings_046_050.json and check every fix: 'old' occurs exactly once in its page file, also after the
earlier fixes of the same page are applied, and the braces of each page stay balanced."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b046_050"
OUT = RUN / "findings_046_050.json"

F = []


def add(**kw):
    kw.setdefault("note", "")
    F.append(kw)


# ---------------------------------------------------------------- p. 46
add(page=46, where="start of page",
    scan="p. 46 begins 'brique sur X dont les sections sur un ouvert V' (second half of 'algé-brique', hyphenated "
         "across the page break); p. 45 ends '... Soit F̄ le faisceau algé-' (both scans)",
    tex="page_046.tex begins with the whole word 'algébrique sur $X$' under the folio-46 marker; page_045.tex ends "
        "'le faisceau'",
    kind="marker", confidence="high", fix=None,
    note=r'''Page 46 really begins with 'brique'. Split the word at the marker, as on p. 18 (findings_016_020.json): python -I move_marker.py 6 46 "brique sur" (no --before: the anchor follows the marker), then in both layers replace 'algé\n%%%%%%%%%%  scan idx 59' by 'algé%\n%%%%%%%%%%  scan idx 59' so that 'algébrique' stays one word. Simulated on both layers (crops_046_050/sim_markers.py, nothing written): '... Soit $\overline F$ le faisceau' / 'algé%' / marker / 'brique sur $X$ dont ...'.''')

add(page=46, where="display after 'homomorphisme évident de faisceaux quasi-cohérents'",
    scan="Σ_i (F | U_i with one bar over the whole) ⟶ Σ_{i,j} (F | U_i ∩ U_j with one bar over the whole): the bar "
         "covers F, the vertical bar and U_i (resp. U_i ∩ U_j); U stands on the line after a full-height vertical bar "
         "(both scans; crops_046_050/p46_display.png, w57_display.png)",
    tex=r"\overline F|_{U_i} ... \overline F|_{U_i\cap U_j}",
    kind="formula", confidence="high",
    fix={"old": r"\overline F|_{U_i}\longrightarrow \sum_{i,j}\overline F|_{U_i\cap U_j}",
         "new": r"\overline{F|U_i}\longrightarrow \sum_{i,j}\overline{F|U_i\cap U_j}"},
    note="The print writes the restriction on the line, not as a subscript, and draws the bar over the whole "
         "expression. Independent of the comma fix that follows (the old strings do not overlap).")

add(page=46, where="end of the same display",
    scan="no punctuation after U_j (both scans)",
    tex=r"\overline F|_{U_i\cap U_j},",
    kind="punctuation", confidence="high",
    fix={"old": ",\n" + r"\]", "new": "\n" + r"\]"},
    note="The TeX adds a comma at the end of the display.")

add(page=46, where="'Comme F̄ | U = F est cohérent'",
    scan="F̄ | U = F: the bar over F alone, U on the line after a full-height vertical bar (both scans; "
         "crops_046_050/p46_restr1.png)",
    tex=r"$\overline F|_U=F$",
    kind="formula", confidence="high",
    fix={"old": r"$\overline F|_U=F$", "new": r"$\overline F|U=F$"},
    note=r"As in the display: the print writes the restriction F | U on the line. The Appendix has more |_ "
         r"restrictions at main.tex lines 1275-1283 (later pages: P'_i|_U, R|_U, S|_U, F|_U, \overline{G|_{U_i}}).")

add(page=46, where="'qui engendrent F̄ | U. Ces sections'",
    scan="F̄ | U (both scans; crops_046_050/p46_restr2.png)",
    tex=r"$\overline F|_U$",
    kind="formula", confidence="high",
    fix={"old": r"engendrent $\overline F|_U$", "new": r"engendrent $\overline F|U$"},
    note="Same form as the previous finding.")

add(page=46, where="'Supposons maintenant X quasi-projective non singulière. Alors'",
    scan="'non singulière' underlined as one run, 'non' included (both scans; crops_046_050/p46_nonsing.png)",
    tex=r"non \emph{singulière}",
    kind="underline", confidence="high",
    fix={"old": r"quasi-projective non \emph{singulière}", "new": r"quasi-projective \emph{non singulière}"},
    note="Same on p. 48 ('Supposons maintenant X non singulière').")

add(page=46, where="Corollaire 2 au théorème 2.3, 'les fonctions addtives f de fibrés vectoriels'",
    scan="addtives (both scans)",
    tex="addtives (printed reading kept)",
    kind="misprint_in_print", confidence="high", fix=None, corrected="additives",
    note="Missing i in the print ('les fonctions additives g' two lines lower); the TeX keeps it; the corrected "
         "layer already reads 'additives'.")

# ---------------------------------------------------------------- p. 48
add(page=48, where="start of page",
    scan="p. 48 begins 'non seulement un groupe abélien, mais un λ-anneau'; p. 47 ends '... Comme K(ξ(X)) est' "
         "(both scans)",
    tex=r"'non' is the last word of page_047.tex ('... Comme $\underline{K}(\xi(X))$ est non', under the folio-47 "
        r"marker); page_048.tex begins 'seulement'",
    kind="marker", confidence="high", fix=None,
    note=r'''Page 48 really begins with 'non'. Move the folio-48 marker before that word: python -I move_marker.py 6 48 "non" --before (it takes the last 'non' before the marker, the line's final word; simulated on both layers: '... Comme $\underline{K}(\xi(X))$ est ', marker, 'non', 'seulement un groupe abélien ...').''')

add(page=48, where="'si F est un faisceau algébrique cohérent sur X, γ(F) désigne de même sa classe'",
    scan="γ(Γ): the letter in the parentheses is a Greek capital Gamma (top bar only, the Symbol-element glyph of "
         "Γ(U ∩ V,F) on p. 46), not the typewriter F with its middle bar (both scans; "
         "crops_046_050/p48_gammaF.png, w59_gammaF.png)",
    tex=r"$\gamma(F)$ (silently corrected)",
    kind="misprint_in_print", confidence="high",
    fix={"old": r"$\gamma(F)$ désigne", "new": r"$\gamma(\Gamma)$ désigne"},
    corrected=r"$\gamma(F)$ désigne",
    note=r"The typist stayed on the Greek element after the gamma; the sentence is about the class of the sheaf F. "
         r"The TeX silently corrects; the corrected layer reads \gamma(F).")

add(page=48, where="'Supposons maintenant X non singulière. S'inspirant des développements'",
    scan="'non singulière' underlined as one run (both scans; crops_046_050/p48_nonsing.png)",
    tex=r"$X$ non \emph{singulière}",
    kind="underline", confidence="high",
    fix={"old": r"$X$ non \emph{singulière}", "new": r"$X$ \emph{non singulière}"},
    note="As on p. 46.")

# ---------------------------------------------------------------- p. 49
add(page=49, where="start of page",
    scan="p. 49 begins 'du début du § 2, on définit une multiplication dans K(X)'; p. 48 ends '... S'inspirant des "
         "développements' (both scans)",
    tex=r"'du début du \S 2, on' is the end of page_048.tex (under the folio-48 marker); page_049.tex begins "
        r"'définit'",
    kind="marker", confidence="high", fix=None,
    note=r'''Page 49 really begins with 'du début'. Move the folio-49 marker before it: python -I move_marker.py 6 49 "du début" --before (the ASCII anchor "du d" gives the same result; simulated on both layers: '... des développements ', marker, 'du début du \S 2, on', 'définit une multiplication ...').''')

add(page=49, where="(2.15), end of the display",
    scan="no punctuation after γ(Tor_i(F,G)) (both scans)",
    tex=r"\gamma(\underline{\Tor}_i(F,G)),",
    kind="punctuation", confidence="high",
    fix={"old": "_i(F,G)),", "new": "_i(F,G))"},
    note="The TeX adds a comma at the end of (2.15).")

add(page=49, where="(2.16), left side",
    scan="γ(F_1)....γ(F_p): four typed full stops on the baseline (both scans; crops_046_050/p49_dots.png, "
         "w60_dots.png)",
    tex=r"\gamma(F_1)\cdots\gamma(F_p)",
    kind="symbol", confidence="medium",
    fix={"old": r"\gamma(F_1)\cdots\gamma(F_p)", "new": r"\gamma(F_1)....\gamma(F_p)"},
    note=r"\cdots sets three dots at mid-height (same kind of fix as SGA 7 I p. 247, typed baseline stops written "
         r"\cdots). Independent of the comma fix at the end of the display.")

add(page=49, where="(2.16), end of the display",
    scan="no punctuation after (F_1,...,F_p)) (both scans)",
    tex=r"\underline{\Tor}_i(F_1,\ldots,F_p)),",
    kind="punctuation", confidence="high",
    fix={"old": "F_p)),", "new": "F_p))"},
    note="The TeX adds a comma at the end of (2.16).")

add(page=49, where="'les Tor_i sont des \"Tor simultanés\", calculés'",
    scan="the Tor inside the quotes is underlined (both scans; crops_046_050/p49_torsim.png, w60_216.png)",
    tex=r"«~$\Tor$ simultanés~»",
    kind="underline", confidence="high",
    fix={"old": r"«~$\Tor$ simultanés", "new": r"«~$\underline{\Tor}$ simultanés"},
    note="The underlined Tor of the sheaf Tor, as the Tor_i of the same sentence; 'des Tor multiples' and "
         "'formule des Tor' on this page are plain in the print, as in the TeX.")

add(page=49, where="'l'homomorphisme canonique de K(ξ(X)) dans K(X)'",
    scan="K(ξ(X) dans K(X): one closing parenthesis after ξ(X) (both scans; crops_046_050/p49_kxi.png, "
         "w60_kxi.png)",
    tex=r"$\underline{K}(\xi(X))$ (silently corrected)",
    kind="misprint_in_print", confidence="high",
    fix={"old": r"canonique de $\underline{K}(\xi(X))$", "new": r"canonique de $\underline{K}(\xi(X)$"},
    corrected=r"canonique de $\underline{K}(\xi(X))$",
    note=r"Unbalanced parenthesis in the print; the TeX silently closes it; the corrected layer reads "
         r"\underline{K}(\xi(X)).")

# ---------------------------------------------------------------- p. 50
add(page=50, where="after (2.18), 'On fera attention à ce qu'on n'a pas en général égalité'",
    scan="'On fera attention' is indented at the paragraph indent and the next line starts at the margin: a new "
         "paragraph after the display (both scans)",
    tex=r"no blank line after \end{equation}: 'On fera attention' continues the paragraph of (2.18)",
    kind="other", confidence="medium",
    fix={"old": "\\end{equation}\nOn\nfera", "new": "\\end{equation}\n\nOn\nfera"},
    note="The typescript indents its new paragraphs (p. 50 'Je ne sais définir'); text that continues after a "
         "display starts at the margin (p. 49 '(les Tor_i étant pris', 'où, dans le deuxième membre', "
         "'ce qui montre').")

add(page=50, where="'(ε(s) est la signature de s)'",
    scan="'signature' underlined (both scans; crops_046_050/p50_sign.png)",
    tex="est la signature de $s$",
    kind="underline", confidence="high",
    fix={"old": "est la signature de $s$", "new": r"est la \emph{signature} de $s$"})

add(page=50, where="'lorsque k n'est pas de caractéristique ≠ 0'",
    scan="n'est pas de caractéristique ≠ 0 (both scans)",
    tex=r"n'est pas de caractéristique $\neq0$ (printed reading kept)",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected="n'est pas de caractéristique $0$",
    note=r"Double negation: as printed the clause says 'when k has characteristic 0', against the sentence it "
         r"explains ('que si le corps k est de caractéristique 0'). Either the inequality sign or the negation is "
         r"superfluous; 'lorsque $k$ est de caractéristique $\neq0$' is the other possible correction. The TeX "
         r"keeps the printed reading, and so does the corrected layer.")

add(page=50, where="Théorème 2.8, 'sur le corps k de caractéristique 0. Soit F'",
    scan="'corps' is underlined; 'k de caractéristique 0.' is not; the underline resumes at 'Soit' (both scans; "
         "crops_046_050/p50_car.png, w61_car.png)",
    tex=r"'de caractéristique' inside the single \emph{...} of the statement",
    kind="underline", confidence="high",
    fix={"old": "le corps $k$ de caractéristique $0$. Soit $F$",
         "new": r"le corps} $k$ de caractéristique $0$. \emph{Soit $F$"},
    note="Words the print leaves plain inside the TeX's single emphasis (beyond the formula convention). One edit, "
         "so that the braces stay balanced.")

add(page=50, where="after (2.19), 'N.B. Il est clair que le groupe S_p agit'",
    scan="'N.B.' is indented at the paragraph indent: a new paragraph after the display (both scans)",
    tex=r"no blank line after \end{equation}: 'N.B.' continues the paragraph of the theorem",
    kind="other", confidence="medium",
    fix={"old": "\\end{equation}\nN.B.", "new": "\\end{equation}\n\nN.B."},
    note="As 'On fera attention' above.")

add(page=50, where="N.B., 'agit sur le faisceau Tor_i(F,..,F)'",
    scan="(F,..,F): two dots between the commas (both scans; crops_046_050/p50_FF.png, w61_FF.png)",
    tex=r"(F,\ldots,F) (silently corrected)",
    kind="misprint_in_print", confidence="medium",
    fix={"old": r"_i(F,\ldots,F)$.", "new": "_i(F,..,F)$."},
    corrected=r"_i(F,\ldots,F)$.",
    note="Two-dot ellipsis of the typist, as (1.38) and (1.39) on p. 37 (findings_036_040.json); (2.19) just above "
         "has three dots. The TeX writes three dots.")

# ---------------------------------------------------------------- checks
order = ["page", "where", "scan", "tex", "kind", "confidence", "fix", "corrected", "note"]
F = [{k: f[k] for k in order if k in f} for f in F]
ok = True
texts = {p: (B / f"page_{p:03d}.tex").read_text(encoding="utf-8") for p in range(46, 51)}
for p, t in texts.items():
    assert "\r" not in t
    cur = t
    for f in F:
        if f["page"] != p or not f["fix"]:
            continue
        old, new = f["fix"]["old"], f["fix"]["new"]
        n0, n1 = t.count(old), cur.count(old)
        if n0 != 1 or n1 != 1 or "%%%%%%%%%%" in old:
            ok = False
            print("BAD", p, repr(old), n0, n1)
        cur = cur.replace(old, new)
    for a, b in ("{}", "()", "[]"):
        if cur.count(a) - cur.count(b) != t.count(a) - t.count(b):
            print("NOTE balance changed", p, a + b, t.count(a) - t.count(b), "->", cur.count(a) - cur.count(b))
    if cur.count("$") % 2:
        ok = False
        print("BAD dollar parity", p)
for f in F:
    if f["kind"] == "misprint_in_print":
        assert "corrected" in f
    else:
        assert "corrected" not in f
counts = {p: (sum(1 for f in F if f["page"] == p and f["kind"] != "misprint_in_print"),
              sum(1 for f in F if f["page"] == p and f["kind"] == "misprint_in_print")) for p in range(46, 51)}
print("counts", counts, "total", len(F))
if ok:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("written", OUT)
