import json
import pathlib

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b446_450"
OUT = RUN / "findings_446_450.json"
NL = "\n"


def F(old, new):
    return {"old": old, "new": new}


items = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    items.append(d)


# ---------------- page 446 ----------------
add(446, "start of the page (end of page_445.tex)",
    "p. 446 begins with the display 'j_*(y') + f^*(x) = 0 .' and then 'Il faut trouver y ∈ K˙(Y) tel que :'; "
    "p. 445 ends '... y' ∈ K˙(Y'), tels que :' (b441_445/page_445_s4.png)",
    r"page_445.tex ends 'tels que:' + '\[ j_*(y')+f^*(x)=0. \]' + 'Il' above the folio-446 marker; page_446.tex begins 'faut trouver'",
    "marker", "high", None,
    r"Move the folio-446 marker line up four lines, to directly after 'tels que:' at the end of page_445.tex, "
    r"i.e. before '\[' + newline + 'j_*(y')+f^*(x)=0.' + newline + '\]' + newline + 'Il'. The page then begins with that display "
    r"and 'Il faut trouver'.")

add(446, "last paragraph, '(voir EGA 0_IV 17.1.8)'",
    "'(voir EGA O_IV 17.1.8).' with no comma after O_IV (both scans; crops_446_450/c446_ega.png)",
    r"(voir EGA \(0_{\mathrm{IV}}\), 17.1.8)",
    "punctuation", "high",
    F(r"\(0_{\mathrm{IV}}\), 17", r"\(0_{\mathrm{IV}}\) 17"),
    "Comma added by the transcription.")

add(446, "end of page_446.tex: the word 'On' before the folio-447 marker",
    "p. 446 ends with the short line '... (voir EGA O_IV 17.1.8).'; p. 447 begins with the indented new paragraph "
    "'On sait que pour tout schéma régulier ...'",
    r"'... 17.1.8). On' + folio-447 marker + 'sait que ...': one paragraph",
    "other", "high",
    F("1.8). On", "1.8)." + NL + NL + "On"),
    "Paragraph break of the print; goes with the folio-447 marker finding (p. 447): once the marker is moved "
    "before 'On', the blank line before it keeps the new paragraph. Does not overlap the comma fix above.")

add(446, "'on a nécéssairement'",
    "'nécéssairement' with an acute accent on the second e as well (both scans)",
    "nécéssairement (printed reading kept)",
    "misprint_in_print", "high", None,
    "The TeX keeps the printed reading (as 'nécéssaire', p. 419).",
    corrected="nécessairement")

add(446, "'ceci entraine z' = g_*(z) = 0'",
    "'entraine' without circumflex: the i has its plain typed dot (both scans; crops_446_450/c446_entr2.png, w446_entr2.png)",
    "entraine (printed reading kept)",
    "misprint_in_print", "high", None,
    "The TeX keeps the printed reading (as 'd'entrainer', p. 8, findings_006_010.json).",
    corrected="entraîne")

add(446, "'D'autre part, on a par hypothèse : j_*(y') = f^*(x)'",
    "'j_*(y') = f^*(x)' with no minus sign (both scans); the hypothesis is j_*(y') + f^*(x) = 0 (top of the page), "
    "and the page itself writes 'f^*(x) =-j_*(y')' above",
    r"\(j_*(y')=f^*(x)\) (printed reading kept)",
    "misprint_in_print", "medium", None,
    "Sign dropped in the print: the next relation, j_*(y') = f^*(i_*(y)), follows from x = -i_*(y) only with "
    "j_*(y') = -f^*(x). The TeX keeps the printed reading.",
    corrected=r"j_*(y')=-f^*(x)")

add(446, r"K^\circ(Y) twice on this page; also pp. 447-449",
    "K with a raised dot (K˙), the K˙ of Exposés IV and VI (both scans)",
    r"K^\circ: p. 446 two, p. 447 three, p. 448 nine (with the §4 title), p. 449 three, p. 450 none",
    "symbol", "high", None,
    r"Convention of the Exposé VII TeX (also reported on pp. 416 and 435), not itemized: to be done by script as "
    r"in Exposé VI (K^\circ -> K^{\bullet}).")

# ---------------- page 447 ----------------
add(447, "start of the page (end of page_446.tex)",
    "p. 447 begins with the indented paragraph 'On sait que pour tout schéma régulier ayant un faisceau ample, ...'; "
    "p. 446 ends '(voir EGA O_IV 17.1.8).'",
    "page_446.tex ends '... 17.1.8). On' above the folio-447 marker; page_447.tex begins 'sait que'",
    "marker", "high", None,
    "Move the folio-447 marker line one word up, before 'On' at the end of page_446.tex. Together with the "
    "paragraph-break fix listed under p. 446 ('1.8). On' -> '1.8).' + blank line + 'On'), p. 447 then begins the "
    "new paragraph 'On sait que' as printed.")

add(447, "triangle diagram, right-hand vertex",
    "L and R each underlined twice (the double-struck derived functors), M underlined once: "
    "'L̲̲f^*(R̲̲f_*(M̲˙))' (both scans; crops_446_450/w447_diag2.png)",
    r"Lf^*(Rf_*(M^\bullet))",
    "font", "high",
    F(r"Lf^*(Rf_*(M^\bullet))", r"\mathbb Lf^*(\mathbb Rf_*(M^\bullet))"),
    r"As \mathbb Ri_* on p. 435. The single underline of M belongs to the underline convention (next finding).")

add(447, "throughout the page",
    "underlined in the print (both scans): the sheaf E in 'Soit E un', 'alors E est un', 'la classe de E dans', "
    "'filtrer E par', and in 'J'^n.E' and 'J'^{n_o}.E = 0' (there the J of J' as well); M˙ in 'un complexe parfait M˙' "
    "and both M˙ of the diagram; N˙ in the diagram and in 'cohomologie de N˙'. The class E ('Si E est la classe', "
    "'E appartient', 'Comme E est', 'E y appartient') is plain",
    r"all plain (no \underline in Exposé VII); 'Si \(E\) est la classe de \(E\)' loses the print's distinction "
    r"between the class E and the sheaf E",
    "underline", "high", None,
    "Convention of the Exposé VII TeX (underlined letters written plain, as on pp. 418-435); places listed for "
    "the closing pass, not itemized.")

# ---------------- page 448 ----------------
add(448, "heading 'Remarque 3.8'",
    "'Remarque 3.8.' with a full stop, run into the text (both scans)",
    r"\subsection*{Remarque 3.8}",
    "punctuation", "high",
    F(r"\subsection*{Remarque 3.8}", r"\subsection*{Remarque 3.8.}"),
    r"The only Remarque set as \subsection* in main.tex; every other one is \textbf{Remarque N.} run into the "
    r"text, which would also match the print here.")

add(448, "'Dans le cas X noethérien'",
    "a typed diaeresis over the t: 'noeẗhérien' (both scans; crops_446_450/c448_noeth.png, w448_noeth.png)",
    "noethérien (silently corrected)",
    "misprint_in_print", "medium",
    F("noethérien", "noe\\\"{t}hérien"),
    "The typist's diaeresis stands one letter late, over the t. The TeX silently drops it; the corrected "
    "reading is the volume's spelling (pp. 446-447: noethérien).",
    corrected="noethérien")

add(448, "display of Lemme 4.1",
    "'λ_{-1}(F) ≡ 0 mod.(1-L) .' with a plain 'mod.' and the parentheses around 1-L only (both scans)",
    r"\lambda_{-1}(F)\equiv 0 \pmod{1-L}.",
    "formula", "high",
    F(r"0 \pmod{1-L}.", r"0 \ \mathrm{mod.}(1-L)."),
    r"\pmod for the print's plain 'mod.'.")

add(448, "last display, first line",
    "'≡ (-1)^{d-1}λ^{d-1}(N-2)      mod.(1-L)' (both scans)",
    r"(-1)^{d-1}\lambda^{d-1}(N-2) \pmod{1-L}",
    "formula", "high",
    F(r"(N-2) \pmod{1-L}", r"(N-2) \qquad\mathrm{mod.}(1-L)"),
    r"\pmod for the print's plain 'mod.'.")

add(448, "last display, second line",
    "'≡ (-1)^{d-1}λ^{d-1}(N')      mod.(1-L).' (both scans)",
    r"(-1)^{d-1}\lambda^{d-1}(N') \pmod{1-L}.",
    "formula", "high",
    F(r"(N') \pmod{1-L}", r"(N') \qquad\mathrm{mod.}(1-L)"),
    r"\pmod for the print's plain 'mod.'.")

add(448, "Lemme 4.1 and its proof",
    "underlined in the print (both scans): N' in 'de type fini N'', both letters of 'de N, N'' (the sheaves; the "
    "classes in 'si N,N' sont' and 'N = N' + 2' are plain), N in 'le rang de N', F in 'celui de F'",
    "all plain",
    "underline", "high", None,
    "Convention of the Exposé VII TeX (underlined letters written plain); places listed for the closing pass. "
    "The word-group underlines of the statement of Lemme 4.1 are the pending statement pattern, not listed.")

# ---------------- page 449 ----------------
add(449, "heading 4.2",
    "'4.2.' with a full stop, run into the text (both scans)",
    r"\subsection*{4.2}",
    "punctuation", "high",
    F(r"\subsection*{4.2}", r"\subsection*{4.2.}"),
    "As 2.1 and 2.2 (pp. 429-430).")

add(449, "4.2, 'les sections T_1,...,T_r, donc I/I^2'",
    "'T_1,...,T_r, donc' with a comma and a small d (both scans; crops_446_450/c449_donc.png)",
    r"\(T_1,\ldots,T_r\). Donc \(I/I^2\)",
    "punctuation", "high",
    F(r"T_r\). Donc", r"T_r\), donc"),
    "Full stop and capital for the print's comma.")

add(449, "(4.3.1)",
    "'mod. torsion,' with 'mod' and 'torsion' underlined like the rest of the statement (both scans)",
    r"\pmod{\text{torsion}},",
    "formula", "high",
    F(r"\pmod{\text{torsion}}", r"\qquad\text{mod. torsion}"),
    r"\pmod for the print's plain 'mod.'; the underlines are the statement's word groups (pending pattern, not itemized).")

add(449, "throughout the page",
    "underlined in the print (both scans): N' in 'Or N' est de rang', I in 'l'idéal I définissant', both I of 'I/I^2', "
    "N in 'en notant N le faisceau conormal', N_1 in 'et N_1 le faisceau conormal'",
    "all plain",
    "underline", "high", None,
    "Convention of the Exposé VII TeX (underlined letters written plain); places listed for the closing pass. "
    "The word-group underlines of Théorème 4.3 are the pending statement pattern, not listed.")

# ---------------- page 450 ----------------
add(450, "first line",
    "'relation est équivalente à la relation :' with a colon (both scans)",
    "relation est équivalente à la relation (no colon)",
    "punctuation", "high",
    F("équivalente à la relation" + NL + r"\[", "équivalente à la relation :" + NL + r"\["),
    "Colon of the print missing.")

add(450, "display after 'Or on a :', second line",
    "'= λ^p(j_*(g^*(y)λ_{-1}(F)))   (3.4)' with no comma (both scans)",
    r"&=\lambda^p\bigl(j_*(g^*(y)\lambda_{-1}(F))\bigr),",
    "punctuation", "high",
    F(r"\lambda_{-1}(F))\bigr),", r"\lambda_{-1}(F))\bigr)"),
    "Comma added at the end of the display.")

add(450, "display after 'Or on a :'",
    "'(3.4)' stands on the second line just after the formula, a reference to Proposition 3.4, not an equation "
    "number (both scans)",
    r"\end{aligned} \tag{3.4}",
    "other", "high",
    F(r"\end{aligned}" + NL + r"\tag{3.4}", r"\qquad(3.4)" + NL + r"\end{aligned}"),
    r"\tag turns the reference into an equation number (3.4), which clashes with Proposition 3.4; the "
    r"typescript's equation numbers stand at the left margin ((3.7.1), (4.3.1), (4.3.2)). Does not overlap the "
    r"comma fix just above.")

add(450, "'D'autre part :'",
    "'D'autre part :' with a capital D, after the display that ends with '(3.4)' (both scans)",
    "d'autre part :",
    "word", "high",
    F("d'autre part :", "D'autre part :"),
    "Small d for the print's capital.")

add(450, "display after 'D'autre part :'",
    "'f^*(i_*(λ^p(N,y))) = j_*(g^*(λ^p(N,y))λ_{-1}(F)) (3.4).': the reference (3.4) right after the formula, "
    "then a full stop (both scans)",
    r"\tag{3.4} and no full stop",
    "punctuation", "high",
    F(r"\lambda_{-1}(F)\bigr)" + NL + r"  \tag{3.4}", r"\lambda_{-1}(F)\bigr)\ (3.4)."),
    r"The full stop is missing; the same edit sets (3.4) as the in-line reference of the print, as in the "
    r"display above.")

add(450, "'Alors z = j^*(u') avec u' = j_*(z') (2.7) ;'",
    "the relation runs in the text line 'z = z'(1-L). Alors z = j^*(u') avec u' = j_*(z') (2.7) ; comme "
    "L = j^*(J'),' (both scans)",
    r"a display \[ z=j^*(u')\quad\text{avec }u'=j_*(z') \] between 'Alors' and '(2.7) ;'",
    "other", "medium",
    F("Alors" + NL + r"\[" + NL + r"  z=j^*(u')\quad\text{avec }u'=j_*(z')" + NL + r"\]" + NL + "(2.7) ;",
      r"Alors \(z=j^*(u')\) avec \(u'=j_*(z')\) (2.7) ;"),
    "Running text set as a display.")

add(450, "end of the page (start of page_451.tex)",
    "p. 450 ends '... en appliquant la formule de projection :'; p. 451 begins with the display "
    "'λ^p(J',u')(1-J') = λ^p(u'(1-J')) .' (b451_455/page_451_s1.png)",
    "page_450.tex ends '... la formule de'; 'projection :' is the first line after the folio-451 marker",
    "marker", "high", None,
    r"Move the folio-451 marker line one line down, after 'projection :' (before '\[' + newline + "
    r"'\lambda^p(J',u')(1-J')=\lambda^p(u'(1-J')).').")

add(450, "the exact sequence",
    "J' underlined in '0 → J' → O_X' → O_Y' → 0' (both scans); the J' of 'L = j^*(J')', λ^p(J',u') and "
    "'1 - J'' are plain",
    "plain J'",
    "underline", "high", None,
    "Convention of the Exposé VII TeX (underlined letters written plain); listed for the closing pass.")

# ---------------- checks ----------------
ok = True
for d in items:
    fx = d["fix"]
    if fx is None:
        continue
    t = (B / ("page_%d.tex" % d["page"])).read_text(encoding="utf-8")
    n = t.count(fx["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE", d["page"], n, repr(fx["old"]))
    if "%%%%%%%%%%" in fx["old"]:
        ok = False
        print("MARKER IN OLD", d["page"], repr(fx["old"]))

# overlap check per page
for p in (446, 447, 448, 449, 450):
    t = (B / ("page_%d.tex" % p)).read_text(encoding="utf-8")
    spans = []
    for d in items:
        if d["page"] == p and d["fix"] is not None:
            i = t.find(d["fix"]["old"])
            spans.append((i, i + len(d["fix"]["old"]), d["fix"]["old"]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            ok = False
            print("OVERLAP", p, repr(a[2]), repr(b[2]))

# apply all fixes to a copy and show the result per page, to eyeball
for p in (446, 447, 448, 449, 450):
    t = (B / ("page_%d.tex" % p)).read_text(encoding="utf-8")
    for d in items:
        if d["page"] == p and d["fix"] is not None:
            t = t.replace(d["fix"]["old"], d["fix"]["new"], 1)
    (pathlib.Path(__file__).parent / ("applied_%d.tex" % p)).write_bytes(t.encode("utf-8"))

OUT.write_bytes(json.dumps(items, ensure_ascii=False, indent=1).encode("utf-8"))
from collections import Counter
c = Counter((d["page"], d["kind"] == "misprint_in_print") for d in items)
for p in (446, 447, 448, 449, 450):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
print("OK" if ok else "PROBLEMS", len(items))
