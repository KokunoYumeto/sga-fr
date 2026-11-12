"""Build findings_366_370.json and check that every fix's old occurs exactly once in its page file."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
OUT = RUN / "findings_366_370.json"
NL = "\n"


def page_file(p):
    folder = "b361_365" if p <= 365 else "b366_370"
    return RUN / folder / f"page_{p:03d}.tex"


F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": confidence,
         "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- p. 365 (text printed on p. 366)
add(365,
    "display at the end of page_365.tex, printed at the top of p. 366 (it stands under the folio-365 marker): "
    "D^-(C_A) x D^-(_AC) -> D^-(Ab)",
    "p. 366: 'D^-(C_A) x D^-(_AC) ----> D^-(Ab)' with no punctuation; the same display goes on with "
    "'(X^.,Y^.) ~~> X^. (L-tensor)_A Y^. .'",
    r"D^-(\cC_A)\times D^-({}_A\cC)\longrightarrow D^-(\Ab),",
    "punctuation", "high",
    {"old": r"D^-(\Ab)," + NL + r"\]", "new": r"D^-(\Ab)" + NL + r"\]"},
    "Comma added at the end of the display. Printed on p. 366, filed under p. 365 because the text stands in "
    "page_365.tex until the folio-366 marker is moved (marker finding of p. 366): apply before moving the marker. "
    "The rest of that text ('teur exact' and this display) agrees with the print of p. 366.")

# ---------------------------------------------------------------- p. 366
add(366,
    "top of the page: 'teur exact' and the display D^-(C_A) x D^-(_AC) -> D^-(Ab)",
    "p. 366 begins 'teur exact', then the two-line display 'D^-(C_A) x D^-(_AC) ----> D^-(Ab)' / "
    "'(X^.,Y^.) ~~> X^. (L-tensor)_A Y^. .'; p. 365 ends '... d'où un bifonc-'",
    "'bifoncteur exact' ends the last text line of page_365.tex (s5.tex line 12483 in the diplomatic layer, "
    "12479 in the corrected one), followed by the display D^-(\\cC_A)\\times D^-({}_A\\cC)\\longrightarrow "
    "D^-(\\Ab), ; the folio-366 marker stands after that display, and page_366.tex begins with "
    "(X^\\bullet,Y^\\bullet)\\longmapsto ...",
    "marker", "high", None,
    "Page 366 really begins at 'teur' of 'bifoncteur exact' (the word is divided bifonc-/teur at the page "
    "break). Exact fix, two steps: python -I move_marker.py 5 366 \"bifoncteur exact\" --before, then "
    "python -I marker_split_word.py 5 366 split bifonc teur (simulated in memory on both layers: the lines then "
    "read \"... d'où un \" / \"bifonc%\" / marker / \"teur exact\" / \"\\[\" / \"D^-(\\cC_A)...\"). Text not "
    "moved. Apply the comma fix of that display (filed under p. 365) before the move.")

add(366,
    "first display: (X^.,Y^.) ~~> X^. (L-tensor)_A Y^.",
    "a wavy arrow (~~>), this exposé's maps-to sign",
    r"(X^\bullet,Y^\bullet)\longmapsto",
    "symbol", "high",
    {"old": r"(X^\bullet,Y^\bullet)\longmapsto", "new": r"(X^\bullet,Y^\bullet)\rightsquigarrow"},
    "\\longmapsto for the print's wavy arrow (\\rightsquigarrow is amssymb, loaded by the file). All four "
    "\\longmapsto of Exposé VIII are wavy arrows in the print (pp. 365, 366, 369 twice).")

add(366,
    "first display: the letter over the tensor sign",
    "a double-struck L above the tensor sign",
    r"\overset{\mathbf L}{\otimes}_A",
    "font", "high",
    {"old": r"\overset{\mathbf L}", "new": r"\overset{\mathbb L}"},
    "Derived tensor: the print's L is double-struck here, as both on p. 368.")

add(366,
    "'(cf aussi [1], 6.3)'",
    "(cf aussi - no full stop after cf (the footnote of the page has 'cf.')",
    r"(cf. aussi",
    "punctuation", "high",
    {"old": r"(cf. aussi", "new": r"(cf aussi"},
    "")

add(366,
    "'Dans le cas particulier d'un anneau A commutatif on obtient'",
    "no comma after 'commutatif'",
    r"$A$ commutatif, on obtient",
    "punctuation", "high",
    {"old": r"commutatif, on obtient", "new": r"commutatif on obtient"},
    "")

add(366,
    "'on obtient en fait un bi-foncteur exact'",
    "bi-foncteur, with a hyphen inside the line (not a line-break hyphen)",
    r"un bifoncteur exact",
    "word", "high",
    {"old": r"un bifoncteur exact", "new": r"un bi-foncteur exact"},
    "p. 368 prints 'bifoncteur' without hyphen, as the TeX has it there.")

add(366,
    "Définition: 'est de tor-dimension finie s'il est dans D^-'",
    "'de tor-' (end of the line) and 'dimension finie' underlined: the term being defined",
    r"est de tor-dimension finie s'il (no emphasis)",
    "underline", "high",
    {"old": r"est de tor-dimension finie s'il", "new": r"est \emph{de tor-dimension finie} s'il"},
    "\\emph is this exposé's command for the print's underline (its underlined labels \\emph{Démonstration.}, "
    "\\emph{Remarques.}, \\emph{Exemples.}); the running text of Exposé VIII has no underline markup.")

add(366,
    "Définition: 'Y ∈ Ob(_AC)'",
    "Ob with a capital O (as 'Z^(Ob C)' on p. 354)",
    "\\Ob({}_A\\cC); \\Ob prints 'ob': its first definition, \\providecommand{\\Ob}{\\operatorname{ob}} "
    "(s5.tex line 101), wins over the later \\providecommand{\\Ob}{\\operatorname{Ob}} (lines 226, 300)",
    "formula", "high",
    {"old": r"\Ob({}_A\cC)", "new": r"\operatorname{Ob}({}_A\cC)"},
    "Or one change of the macro for Exposé VIII (see the message).")

add(366,
    "Définition: 'Tor_n^A(X,Y) = 0 quelque soit Y ∈ Ob(_AC)'",
    "quelque soit (one word)",
    r"quel que soit (silent correction)",
    "misprint_in_print", "high",
    {"old": r"quel que soit", "new": r"quelque soit"},
    "The TeX silently corrects the print's spelling; the fix restores the printed reading in the diplomatic "
    "layer.",
    corrected=r"quel que soit")

add(366,
    "Proposition 8.1 a)",
    "a) L^. est parfait.  (full stop)",
    r"\text{a) } L^\bullet\text{ est parfait;}",
    "punctuation", "high",
    {"old": r"est parfait;}", "new": r"est parfait.}"},
    "")

add(366,
    "footnote (*) of Proposition 8.1 b)",
    "(*) cf. (SGA 6 I 5.8.1) .",
    r"\footnote{cf. SGA 6 I 5.8.1.}",
    "punctuation", "high",
    {"old": r"\footnote{cf. SGA 6 I 5.8.1.}", "new": r"\footnote{cf. (SGA 6 I 5.8.1).}"},
    "The parentheses of the reference are left out (the footnote of p. 370, 'cf. (SGA 6 III, IV)', has them).")

add(366,
    "the categories C, C_A, _AC, D(C) of pp. 366-368 (convention, reported once)",
    "a plain typed capital C (not script, not underlined), as throughout the exposé from p. 351 ('Soit C une "
    "catégorie abélienne et soit D une sous-catégorie pleine de C'); p. 364 introduces _AC, C_A and _AD the same way",
    "\\cC (\\mathcal C), \\cD (\\mathcal D): e.g. p. 366 'D^-(\\cC)\\times D^-(\\cC)\\longrightarrow D^-(\\cC)' and "
    "'\\Ob({}_A\\cC)', p. 367 'dans $D(\\cC)$', p. 368 'dans $D(\\cC)$'",
    "font", "high", None,
    "Convention of the transcription for Exposé VIII, not itemized: one decision for the exposé (plain C, D in "
    "the diplomatic layer). The print's abelian group C of p. 351 is the same typed C; the TeX writes it plain.")

# ---------------------------------------------------------------- p. 367
add(367,
    "proof label 'Démonstration du lemme.'",
    "typed plain, not underlined (the label 'Lemme' above it is underlined)",
    r"\emph{Démonstration du lemme.}",
    "underline", "high",
    {"old": r"\emph{Démonstration du lemme.}", "new": r"Démonstration du lemme."},
    "\\emph is the file's command for the print's underline; this label has none. A proof label of another "
    "form than 'Preuve :'.")

add(367,
    "'Il nous suffit de démontrer que pour tout groupe divisible G ,'",
    "no comma after 'que'",
    r"démontrer que, pour",
    "punctuation", "high",
    {"old": r"démontrer que, pour", "new": r"démontrer que pour"},
    "")

add(367,
    "diagram of the lemma: left vertical, Hom_Z(Hom_A(E,F'),G) to Hom_Z(F',G) (x)_A E",
    "a plain vertical line without arrowhead, with a vertical tilde (≀) at its left; the horizontal arrows have "
    "heads",
    r'''\arrow[d,"\sim"'] (an arrow with a head, a horizontal tilde)''',
    "symbol", "high",
    {"old": r'''\arrow[d,"\sim"']''', "new": r'''\arrow[d,dash,"\wr"']'''},
    "dash as in the logged fixes of pp. 68 and 93 (tikz-cd's line without heads); \\wr as the file's "
    "\\arrow[d,\"f'\"',\"\\wr\"] (s5.tex line 11828).")

add(367,
    "diagram of the lemma: right vertical, Hom_Z(Hom_A(E,F),G) to Hom_Z(F,G) (x)_A E",
    "a plain vertical line without arrowhead, with ≀ at its right",
    r'''\arrow[d,"\sim"]''',
    "symbol", "high",
    {"old": r'''\arrow[d,"\sim"]''', "new": r'''\arrow[d,dash,"\wr"]'''},
    "As the left vertical.")

add(367,
    "proof label 'Démonstration de la proposition 5.2.'",
    "typed plain, not underlined",
    r"\emph{Démonstration de la proposition 5.2.}",
    "underline", "high",
    {"old": r"\emph{Démonstration de la proposition 5.2.}", "new": r"Démonstration de la proposition 5.2."},
    "The corrected layer reads 8.1 here (next finding): there the old is "
    "'\\emph{Démonstration de la proposition 8.1.}' and the new 'Démonstration de la proposition 8.1.'.")

add(367,
    "'Démonstration de la proposition 5.2.'",
    "5.2",
    "5.2, the printed reading (the corrected layer already has 8.1)",
    "misprint_in_print", "high", None,
    "Wrong reference number in the print: the proof (a) => b), b) => a) for 'pseudo-cohérent, à cohomologie "
    "bornée, et de tor-dimension finie') is that of Proposition 8.1, which p. 368 closes with 'ce qui prouve "
    "8.1'; the exposé has no Proposition 5.2 (section 5 has only 5.1). The diplomatic layer keeps the printed "
    "reading.",
    corrected=r"8.1")

# ---------------------------------------------------------------- p. 368
add(368,
    "III): the complex 0 -> Ker d_{n_o+1} -> P_{n_o+1} -> ... -> P_i -> 0 ->",
    "the display ends with an arrow after the last 0 and nothing after it (the complex of p. 367 ends "
    "'-> 0 -> ...')",
    r"P_i\longrightarrow0\longrightarrow\cdots (silent correction)",
    "misprint_in_print", "high",
    {"old": r"P_i\longrightarrow0\longrightarrow\cdots", "new": r"P_i\longrightarrow0\longrightarrow"},
    "The print leaves the last arrow dangling; the TeX supplies the dots as on p. 367. The fix restores the "
    "printed reading in the diplomatic layer.",
    corrected=r"P_i\longrightarrow0\longrightarrow\cdots")

add(368,
    "'Si A est un anneau commutatif, et si X^. , Y^.'",
    "'commutatif' underlined (not the comma)",
    r"anneau commutatif, et si (no emphasis)",
    "underline", "high",
    {"old": r"anneau commutatif, et si", "new": r"anneau \emph{commutatif}, et si"},
    "")

add(368,
    "'alors leur produit tensoriel X^. (L-tensor)_A Y^.'",
    "a double-struck L above the tensor sign",
    r"\overset{\mathbf L}{\otimes}_A",
    "font", "high",
    {"old": "leur produit tensoriel" + NL + r"\[" + NL + r"X^\bullet\overset{\mathbf L}",
     "new": "leur produit tensoriel" + NL + r"\[" + NL + r"X^\bullet\overset{\mathbb L}"},
    "As p. 366.")

add(368,
    "'(dans la catégorie dérivée) est encore un complexe parfait'",
    "'(dans la catégorie dérivée)' in parentheses",
    r"dans la catégorie dérivée est encore (no parentheses)",
    "punctuation", "high",
    {"old": r"dans la catégorie dérivée est encore", "new": r"(dans la catégorie dérivée) est encore"},
    "")

add(368,
    "footnote call (*) at 'faisant suite à celui-ci'",
    "celui-ci(*)).  - the call stands inside the parenthesis, before ')' and the full stop",
    r"celui-ci).\footnote{SGA 6 V 2.}",
    "other", "high",
    {"old": r"celui-ci).\footnote{SGA 6 V 2.}", "new": r"celui-ci\footnote{SGA 6 V 2.})."},
    "Position of the footnote call.")

add(368,
    "'Le produit tensoriel X^. (L-tensor)_A Y^. d'un complexe parfait'",
    "a double-struck L above the tensor sign",
    r"\overset{\mathbf L}{\otimes}_A",
    "font", "high",
    {"old": "Le produit tensoriel" + NL + r"\[" + NL + r"X^\bullet\overset{\mathbf L}",
     "new": "Le produit tensoriel" + NL + r"\[" + NL + r"X^\bullet\overset{\mathbb L}"},
    "As p. 366.")

# ---------------------------------------------------------------- p. 369
add(369,
    "heading '9. Propriétés fonctorielles.'",
    "underlined title followed by a full stop",
    r"\subsection*{9. Propriétés fonctorielles}",
    "punctuation", "high",
    {"old": r"\subsection*{9. Propriétés fonctorielles}", "new": r"\subsection*{9. Propriétés fonctorielles.}"},
    "")

add(369,
    "display 'E ~~> B_[u] (x)_A E'",
    "a wavy arrow (~~>)",
    r"E\longmapsto B_{[u]}\otimes_A E",
    "symbol", "high",
    {"old": r"E\longmapsto", "new": r"E\rightsquigarrow"},
    "As p. 366.")

add(369,
    "display 'F ~~> F_[u]'",
    "a wavy arrow (~~>)",
    r"F\longmapsto F_{[u]}",
    "symbol", "high",
    {"old": r"F\longmapsto", "new": r"F\rightsquigarrow"},
    "As p. 366.")

# ---------------------------------------------------------------- p. 370
add(370,
    "'l'identité suivante (\"la formule de projection\") :'",
    "straight typewriter quotes; 'formule de projection' underlined ('la' and the quotes are not)",
    r"(«la formule de projection»): guillemets, no emphasis",
    "underline", "high",
    {"old": r"«la formule de projection»", "new": r"``la \emph{formule de projection}''"},
    "Two differences in one edit (their olds would overlap): the missing underline, and the guillemets for the "
    "print's straight quotes (Exposé VIII writes guillemets throughout, see the message; the global rule allows "
    "``...'' or \"...\"). To keep the guillemets, use the new '«la \\emph{formule de projection}»'.")

add(370,
    "heading '10. Construction relative.(*)'",
    "underlined title, a full stop, then the footnote call (*)",
    r"\subsection*{10. Construction relative\footnote{cf. (SGA 6 III, IV).}}",
    "punctuation", "high",
    {"old": r"Construction relative\footnote", "new": r"Construction relative.\footnote"},
    "The call (*) follows the full stop in the print.")

add(370,
    "'(resp. pseudo-cohérents et bornés relativement à A .'",
    "the parenthesis opened at '(resp.' is never closed: '... et bornés relativement à A . Ces deux'",
    r"(resp. pseudo-cohérents et bornés) relativement à $A$. (silent correction)",
    "misprint_in_print", "high",
    {"old": r"et bornés) relativement", "new": r"et bornés relativement"},
    "The TeX closes the parenthesis; the fix restores the printed reading in the diplomatic layer.",
    corrected=r"et bornés) relativement")

add(370,
    "first of the two displays K^.(B rel A) = K(D(B)_{A-parf})",
    "no punctuation after the first line; a full stop after the second",
    r"K^{\bullet}(B\operatorname{\,rel\,}A)=K(D(B)_{A-\parf}),",
    "punctuation", "high",
    {"old": r"_{A-\parf})," + NL + r"\]", "new": r"_{A-\parf})" + NL + r"\]"},
    "Comma added at the end of the display.")

# ---------------------------------------------------------------- checks
ok = True
for d in F:
    fx = d["fix"]
    if fx is None:
        continue
    t = page_file(d["page"]).read_text(encoding="utf-8")
    n = t.count(fx["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE", d["page"], n, repr(fx["old"]))
    if "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]:
        ok = False
        print("MARKER IN FIX", d["page"], repr(fx["old"]))
# overlapping olds on the same page
for p in sorted({d["page"] for d in F}):
    t = page_file(p).read_text(encoding="utf-8")
    spans = []
    for d in F:
        if d["page"] == p and d["fix"]:
            k = t.find(d["fix"]["old"])
            spans.append((k, k + len(d["fix"]["old"]), d["where"][:40]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            ok = False
            print("OVERLAP", p, a, b)
# apply all fixes in memory to see the result
for p in sorted({d["page"] for d in F}):
    t = page_file(p).read_text(encoding="utf-8")
    for d in F:
        if d["page"] == p and d["fix"]:
            t = t.replace(d["fix"]["old"], d["fix"]["new"], 1)
    (RUN / "crops_366_370" / f"applied_{p:03d}.tex").write_text(t, encoding="utf-8", newline="")
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="")
from collections import Counter
c = Counter((d["page"], d["kind"] == "misprint_in_print") for d in F)
for p in sorted({d["page"] for d in F}):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
print("total", len(F), "all olds unique and disjoint" if ok else "PROBLEMS")
