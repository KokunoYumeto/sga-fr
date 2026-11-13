"""Build findings_461_465.json; check that every fix's old occurs exactly once in its page_NNN.tex.
In the raw strings below, the character ¶ stands for a line break (LF)."""
import json, pathlib, sys
sys.stdout.reconfigure(encoding='utf-8')
HERE = pathlib.Path(__file__).resolve().parent
B = HERE.parent / "b461_465"
OUT = HERE.parent / "findings_461_465.json"


def nl(s):
    return None if s is None else s.replace("¶", "\n")


M461 = "%%%%%%%%%%  scan idx 474  |  folio 461  %%%%%%%%%%"
M462 = "%%%%%%%%%%  scan idx 475  |  folio 462  %%%%%%%%%%"
DISP460 = (r"donc :¶\[¶  i_{\gr}:\operatorname{Gr}^{k-d}K^\circ(Y)_{\mathbb Q}¶  \to \operatorname{Gr}^{k}K^\circ(X)_{\mathbb Q};"
           r"¶  \qquad¶  j_{\gr}:\operatorname{Gr}^{k-1}K^\circ(Y')_{\mathbb Q}¶  \to \operatorname{Gr}^{k}K^\circ(X')_{\mathbb Q}.¶\]")
OLD461 = "et définissent¶" + M461 + "¶" + DISP460 + "¶Enfin, on remarque"
NEW461 = "et définissent¶" + DISP460 + "¶" + M461 + "¶Enfin, on remarque"
OLD462 = "à la relation (4.8.1), on¶" + M462 + "¶obtient :"
NEW462 = "à la relation¶" + M462 + "¶(4.8.1), on obtient :"

F = []


def add(page, where, scan, tex, kind, conf, old=None, new=None, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": nl(old), "new": nl(new)}}
    if kind == "misprint_in_print":
        d["corrected"] = nl(corrected)
    d["note"] = nl(note)
    F.append(d)


# ---------------- page 461 ----------------
add(461, "start of page (folio-461 marker)",
    "p. 460 ends '... j_* passent aux gradués associés, et définissent donc : i_gr : Gr^{k-d}K˙(Y)_Q → Gr^kK˙(X)_Q ; "
    "j_gr : Gr^{k-1}K˙(Y')_Q → Gr^kK˙(X')_Q .'; p. 461 begins 'Enfin, on remarque que λ_{-1}(F) = (-1)^{d-1}γ^{d-1}(F)' "
    "(both scans; crops_461_465/wit_460_half.png, wit_461_half.png)",
    "page_461.tex begins with 'donc :' and the display of i_gr and j_gr (8 lines that p. 460 prints), then 'Enfin, on remarque'",
    "marker", "high",
    note="Page 461 really begins at 'Enfin, on remarque que'. Exact edit in main.tex, both layers (diplomatic lines "
         "11766-11776, current 11772-11782): replace '" + OLD461.replace("¶", "\\n") + "' by '" + NEW461.replace("¶", "\\n")
         + "' (the display itself unchanged; old string once per layer; simulated in memory: crops_461_465/sim_markers.py). "
           "Same result: python -I move_marker.py 6 461 \"Enfin, on remarque\" (anchor after the marker; it starts its line).")

add(461, "'D'après VI 5.8, g_*(Fil^{k-1}K˙(Y')) ⊂ Fil^{k-d}K˙(Y) pour tout k, puisque'",
    "the inclusion stands in the running text, on one line with 'D'après VI 5.8,' and 'pour tout k, puisque' (both scans)",
    "a display between 'D'après VI 5.8,' and 'pour tout \\(k\\)'",
    "other", "high",
    r"D'après VI 5.8,¶\[¶  g_*(\Fil^{k-1}K^\circ(Y'))\subset \Fil^{k-d}K^\circ(Y)¶\]¶pour tout",
    r"D'après VI 5.8, \(g_*(\Fil^{k-1}K^\circ(Y'))\subset \Fil^{k-d}K^\circ(Y)\) pour tout",
    "The TeX makes an inline formula a display (same kind of fix as pp. 21, 34, 42, 80, 105).")

add(461, "'Posons :' after ii)",
    "'Posons :' begins a new, indented paragraph (left edge at the paragraph indent of 'D'après VI 5.8' and 'Pour montrer', "
    "both scans; crops_461_465/line_starts.py on the witness: 336 px against the margin's 214)",
    "'\\]' followed directly by 'Posons :' (the paragraph runs on)",
    "other", "high",
    r"\]¶Posons :", r"\]¶¶Posons :",
    "Missing paragraph break. 'Alors d'après VI 5.8' below continues at the left margin, as in the TeX.")

add(461, "label of the display 'j_*(y') + f^*(x) ∈ Fil^{k+1}K˙(X')_Q ,'",
    "(4.6.1) (both scans)",
    "\\tag{4.6.1} (printed reading kept)",
    "misprint_in_print", "medium",
    note="The display belongs to the proof of Théorème 4.8 and is cited as '(4.8.1)' on the first line of p. 462 "
         "('En appliquand f_* à la relation (4.8.1), on obtient'); 4.6.1 is Remarque 4.6.1 (main.tex line 11609). "
         "The 'Compte tenu de (4.6.1)' of p. 462 repeats the wrong number (entry there). The current layer also has \\tag{4.6.1}.",
    corrected=r"\tag{4.8.1}")

add(461, "'Alors d'après VI 5.8, y ∈ Fil^kK˙(Y).'",
    "exponent k alone (both scans; crops_461_465/w461_Filk.png)",
    "\\(y\\in\\Fil^{k}K^\\circ(Y)\\) (printed reading kept)",
    "misprint_in_print", "medium",
    note="y = g_*(y') with y' ∈ Fil^{k-1}K˙(Y')_Q, and VI 5.8 as quoted on this page gives g_*(Fil^{k-1}K˙(Y')) ⊂ "
         "Fil^{k-d}K˙(Y): the claim proved and needed is the 'il existe y ∈ Fil^{k-d}K˙(Y)_Q' above. The current layer also "
         "reads Fil^{k}.",
    corrected=r"\(y\in\Fil^{k-d}K^\circ(Y)\)")

add(461, "'En appliquand f_* à la relation'",
    "'appliquand' (both scans; crops_461_465/w461_appliquand.png)",
    "appliquand (printed reading kept)",
    "misprint_in_print", "high",
    note="The current layer also reads 'appliquand'.",
    corrected="appliquant")

add(461, "letters of sheaves on pp. 461-465",
    "underlined in the print (both scans): the N of P(N) and of 'N étant de rang d' (p. 461; the P doubly underlined, "
    "\\mathbf P as in the TeX); the J of 'Soir J l'Idéal de O_X' (p. 464); both J_z, the J of 'une suite de sections de J' "
    "and of J|U (p. 465). Plain in the print: X, Y, Z, U, F, L, x, y, z and the N of c˙(N) (p. 464)",
    "all plain",
    "underline", "high",
    note="Convention of the Exposé VII transcription (findings_416_420, findings_431_435): not itemized. The underlined O "
         "of O_X, O_Z, O_U, O_{X,z}, O_{Z∩U}, O_{Z''_α}, written \\mathcal O, falls under the pending structure-sheaf decision.")

add(461, "K˙ on pp. 461-465",
    "K with a raised dot in every place (both scans), e.g. 'y' ∈ Fil^{k-1}K˙(Y')_Q' (p. 461), 'la structure de K˙(Y') "
    "comme K˙(Y)-algèbre libre' (p. 462), 'K˙(Z') → K˙(X) → K˙(U) → 0' (p. 465)",
    "K^\\circ (68 on pp. 461-465, and 4 more in the p.-460 display that stands under the folio-461 marker)",
    "symbol", "high",
    note="The Exposé VII convention reported in findings_416_420 (one script K^\\circ -> K^{\\bullet} for VII, both "
         "layers): not itemized. Three examples: 'y'\\in\\Fil^{k-1}K^\\circ(Y')_{\\mathbb Q}' -> "
         "'y'\\in\\Fil^{k-1}K^{\\bullet}(Y')_{\\mathbb Q}' (p. 461); 'structure de \\(K^\\circ(Y')\\) comme "
         "\\(K^\\circ(Y)\\)-algèbre' -> 'structure de \\(K^{\\bullet}(Y')\\) comme \\(K^{\\bullet}(Y)\\)-algèbre' (p. 462); "
         "'K^\\circ(Z')\\xrightarrow{j_*}K^\\circ(X)' -> 'K^{\\bullet}(Z')\\xrightarrow{j_*}K^{\\bullet}(X)' (p. 465). The "
         "c˙(N) of p. 464 is its own entry (the K script does not reach it).")

# ---------------- page 462 ----------------
add(462, "start of page (folio-462 marker)",
    "p. 461 ends '... En appliquand f_* à la relation'; p. 462 begins '(4.8.1), on obtient :' (both scans; "
    "crops_461_465/wit_461_half.png, wit_462_half.png)",
    "page_461.tex ends 'à la relation (4.8.1), on' above the folio-462 marker; page_462.tex begins 'obtient :'",
    "marker", "high",
    note="Page 462 really begins at '(4.8.1), on'. Exact edit in main.tex, both layers (diplomatic lines 11804-11806, "
         "current 11810-11812): replace '" + OLD462.replace("¶", "\\n") + "' by '" + NEW462.replace("¶", "\\n")
         + "' (old string once per layer; simulated in memory: crops_461_465/sim_markers.py). The sentence runs on, so no "
           "blank line.")

add(462, "'Compte tenu de (4.6.1), on obtient donc :'",
    "(4.6.1) (both scans)",
    "(4.6.1) (printed reading kept)",
    "misprint_in_print", "medium",
    note="The relation j_*(y') + f^*(x) ∈ Fil^{k+1}K˙(X')_Q of p. 461, numbered (4.6.1) there by mistake (entry on "
         "p. 461) and cited as (4.8.1) on the first line of this page; it is used here a second time. The current layer "
         "also reads (4.6.1).",
    corrected="(4.8.1)")

add(462, "display 'j_*(z) ∈ Fil^{k+1}K˙(X')_Q ,'",
    "a comma after the display (both scans; crops_461_465/w462_jz_comma.png)",
    "a full stop",
    "punctuation", "high",
    r"j_*(z)\in\Fil^{k+1}K^\circ(X')_{\mathbb Q}.", r"j_*(z)\in\Fil^{k+1}K^\circ(X')_{\mathbb Q},",
    "Goes with the next entry: the sentence runs on into 'd'où :'.")

add(462, "'d'où :' after that display",
    "'d'où :' with a small d, at the left margin, continuing the sentence (both scans)",
    "D'où :",
    "word", "high",
    r"D'où :", r"d'où :",
    "Apply with the comma entry above (the two edits do not overlap).")

add(462, "'Soit z̄ l'image de z dans Gr^{k-1}K˙(Y')_Q'",
    "begins a new, indented paragraph after the display j^*(j_*(z)) = z(1-L) ∈ ... (both scans; witness indent 350 px "
    "against the margin's 228)",
    "'\\]' followed directly by 'Soit \\(\\bar z\\)' (the paragraph runs on)",
    "other", "high",
    r"\]¶Soit \(\bar z\)", r"\]¶¶Soit \(\bar z\)",
    "Missing paragraph break.")

add(462, "'On a donc : z(1-L) = 0.'",
    "one bar over the whole product z(1-L) (both scans; crops_461_465/w462_zbar.png, c462_zbar.png)",
    "\\bar z\\,\\overline{(1-L)}=0 (two bars)",
    "formula", "high",
    r"\(\bar z\,\overline{(1-L)}=0\)", r"\(\overline{z(1-L)}=0\)",
    "The class of the product in Gr^kK˙(Y')_Q; the z̄ and the bar of (1-L) of the sentence before are separate, as in the TeX.")

# ---------------- page 463 ----------------
add(463, "display 'Fil^k(K˙(Y')_Q x K˙(X)_Q) → Fil^kK˙(X')_Q'",
    "the arrow carries the label v (both scans)",
    "\\longrightarrow without label",
    "formula", "high",
    r"\longrightarrow", r"\xrightarrow{v}",
    "The only \\longrightarrow of page_463.tex.")

add(463, "display 'γ^k_*(y'_1,x_1) = (Σ_{p=1}^k γ^{k-p}(x_1)γ^p(L,y'_1), γ^k(x_1))'",
    "no punctuation after the display; the next line opens '(conséquence immédiate de (4.7.2)).' (both scans; "
    "crops_461_465/w463_gamma.png, c463_gamma.png)",
    "'\\right),' (comma added)",
    "extra", "high",
    r"\gamma^k(x_1)\right),¶\]", r"\gamma^k(x_1)\right)¶\]",
    "The TeX adds punctuation at the end of the display.")

# ---------------- page 464 ----------------
add(464, "Remarque 4.9: 'et de l'élément c˙(N) de Gr^*K˙(Y)'",
    "c with a raised dot, the mark of the K˙ (both scans; crops_461_465/w464_cN.png, c464_cN.png)",
    "\\(c^\\circ(N)\\)",
    "symbol", "high",
    r"\(c^\circ(N)\)", r"\(c^{\bullet}(N)\)",
    "The only c^\\circ of main.tex; the K^\\circ -> K^{\\bullet} script for Exposé VII does not reach it. If the K˙ "
    "decision for VII ends in another form, take the same form here.")

add(464, "heading '4.10.'",
    "'4.10.' with a full stop, run into 'Soit X un schéma' (both scans)",
    "\\subsection*{4.10}",
    "punctuation", "high",
    r"\subsection*{4.10}", r"\subsection*{4.10.}",
    "The printed paragraph number ends with a full stop (as the fixes of pp. 394, 396, 399, 401, 429-430); the run-in "
    "heading set as its own paragraph is accepted.")

add(464, "4.10: 'Soit X un schéma régulier ayant un faisceau ample.'",
    "'régulier' underlined, the rest of the sentence plain (both scans)",
    "no emphasis",
    "underline", "high",
    r"un schéma régulier ayant un faisceau ample. On sait", r"un schéma \emph{régulier} ayant un faisceau ample. On sait",
    "\\emph is the file's command for underlined words in running text (as the p. 419 entry of findings_416_420). The same "
    "words in Proposition 4.11 belong to its underlined statement (pending pattern, not itemized).")

add(464, "Proposition 4.11",
    "the statement underlined word group by word group: 'Soit', 'un schéma régulier ayant un faisceau ample', 'Alors', "
    "'pour tout'; X, k ≥ 0, the display and the punctuation plain; the label underlines only the word (both scans)",
    "the statement in roman",
    "underline", "high",
    note="Exposé VII follows the Exposé II pattern of GLOBAL_ISSUES 82 (pending volume decision; findings_416_420): not "
         "itemized. The TeX adds no emphasis on defined terms on pp. 461-465.")

add(464, "'Pour cela, on procède par récurrence noethérienne'",
    "begins a new, indented paragraph after the display cl(O_Z) ∈ Fil^kK˙(X)_Q (both scans; witness indent 346 px against "
    "the margin's 226)",
    "'\\]' followed directly by 'Pour cela' (the paragraph runs on)",
    "other", "high",
    r"\]¶Pour cela, on procède", r"\]¶¶Pour cela, on procède",
    "Missing paragraph break.")

add(464, "'sur les sous-schémas fermés intégres de X. Supposons'",
    "'intégres' with an acute accent; the other four 'intègre(s)' of the page and those of p. 465 have the grave "
    "(both scans; crops_461_465/w464_integres.png, c464_integres.png, w464_integresZ.png)",
    "intègres (silently corrected)",
    "misprint_in_print", "high",
    r"fermés intègres de \(X\). Supposons", r"fermés intégres de \(X\). Supposons",
    "The current layer also reads 'intègres' (the corrected edition keeps it).",
    corrected=r"fermés intègres de \(X\). Supposons")

add(464, "'et montrons la pour Z.'",
    "'montrons la' without a hyphen (both scans; crops_461_465/w464_soir.png)",
    "montrons la (printed reading kept)",
    "misprint_in_print", "medium",
    note="The imperative takes the hyphen (as 'plaçons nous', findings_426_430). The current layer also reads 'montrons la'.",
    corrected="montrons-la")

add(464, "'Soir J l'Idéal de O_X'",
    "'Soir' (both scans; crops_461_465/w464_soir.png)",
    "Soir (printed reading kept)",
    "misprint_in_print", "high",
    note="The current layer also reads 'Soir'.",
    corrected="Soit")

# ---------------- page 465 ----------------
add(465, "'Par ailleurs, on a la suite exacte (IV      :'",
    "'(IV', the blank left for the reference, then ':' with no closing parenthesis (both scans; crops_461_465/w465_IV.png, "
    "c465_IV.png); the blanks of p. 464 ('(IV      )', 'i(X      )', 'dans X      )') close theirs",
    "(IV\\qquad) : (closing parenthesis added, silently corrected)",
    "misprint_in_print", "high",
    r"(IV\qquad) :", r"(IV\qquad :",
    "The current layer also has the parenthesis (the corrected edition keeps it).",
    corrected=r"(IV\qquad) :")

add(465, "'il induit une surjection'",
    "'surjection' underlined (both scans)",
    "no emphasis",
    "underline", "high",
    r"induit une surjection", r"induit une \emph{surjection}",
    "Independent of the next entry (the two edits do not overlap).")

add(465, "'Fil^kK˙(X) → Fil^kK˙(U), donc u^*(1_Z) = u^*(x) avec x ∈ Fil^kK˙(X) ; il'",
    "the map stands in the running text, at the start of the line that goes on ', donc u^*(1_Z) = u^*(x) ...' (both scans)",
    "a display between 'surjection' and 'donc'",
    "other", "high",
    r"¶\[¶  \Fil^kK^\circ(X)\longrightarrow \Fil^kK^\circ(U),¶\]¶donc",
    r" \(\Fil^kK^\circ(X)\longrightarrow \Fil^kK^\circ(U)\), donc",
    "The TeX makes an inline formula a display (as on p. 461).")

add(465, "'Par suite, x peut s'exprimer comme combinaison de classes de faisceaux O_{Z''_α}'",
    "x (both scans)",
    "\\(x\\) peut s'exprimer (printed reading kept)",
    "misprint_in_print", "medium",
    note="The element of j_*(K˙(Z')), hence a combination of classes O_{Z''_α} with Z''_α ⊂ Z' ≠ Z, is y; x is the lift "
         "of u^*(1_Z) in Fil^kK˙(X). With y ∈ Fil^{k+1}K˙(X)_Q one gets cl(O_Z) = (cl(O_Z) - y) + y ∈ Fil^kK˙(X)_Q. The "
         "current layer also reads x.",
    corrected=r"\(y\) peut s'exprimer")

add(465, "'D'après l'hypothèse de récurrence, x ∈ Fil^{k+1}K˙(X)_Q'",
    "x (both scans)",
    "\\(x\\in\\Fil^{k+1}K^\\circ(X)_{\\mathbb Q}\\) (printed reading kept)",
    "misprint_in_print", "medium",
    note="As the entry before: the induction hypothesis applies to the classes O_{Z''_α} that make up y.",
    corrected=r"\(y\in\Fil^{k+1}K^\circ(X)_{\mathbb Q}\)")

add(465, "heading BIBLIOGRAPHIE",
    "'BIBLIOGRAPHIE': typed capitals, underlined (both scans)",
    "\\subsection*{Bibliographie}",
    "word", "high",
    r"\subsection*{Bibliographie}", r"\subsection*{BIBLIOGRAPHIE}",
    "As the headings fixed on pp. 19, 158, 219, 273, 364 and 415; the missing underline of a section title is accepted.")

add(465, "[1] Cartan-Eilenberg, Homological Algebra.",
    "the title in plain type, not underlined (both scans; crops_461_465/w465_biblio.png)",
    "\\emph{Homological Algebra}",
    "font", "high",
    r"\emph{Homological Algebra}", r"Homological Algebra",
    "As the p. 159 entry for the same book (findings_156_160). Cartan--Eilenberg: joint-name dash, handled globally.")

# ---------------- checks ----------------
ok = True
for d in F:
    if d["fix"] is None:
        continue
    t = (B / f"page_{d['page']}.tex").read_text(encoding="utf-8")
    n = t.count(d["fix"]["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE", d["page"], n, repr(d["fix"]["old"]))
    if "%%%%%%%%%%" in d["fix"]["old"] or "%%%%%%%%%%" in d["fix"]["new"]:
        ok = False
        print("MARKER IN FIX", d["page"])
# overlap check per page
for p in range(461, 466):
    t = (B / f"page_{p}.tex").read_text(encoding="utf-8")
    spans = []
    for d in F:
        if d["page"] == p and d["fix"]:
            i = t.find(d["fix"]["old"])
            spans.append((i, i + len(d["fix"]["old"]), d["where"][:40]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            ok = False
            print("OVERLAP", p, a, b)
# simulate applying all fixes per page
for p in range(461, 466):
    t = (B / f"page_{p}.tex").read_text(encoding="utf-8")
    for d in F:
        if d["page"] == p and d["fix"]:
            assert t.count(d["fix"]["old"]) == 1, (p, d["fix"]["old"])
            t = t.replace(d["fix"]["old"], d["fix"]["new"], 1)
    (HERE / f"patched_{p}.tex").write_text(t, encoding="utf-8", newline="")
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
from collections import Counter
c = Counter((d["page"], d["kind"] == "misprint_in_print") for d in F)
for p in range(461, 466):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
print("checks ok" if ok else "CHECKS FAILED", len(F), "entries ->", OUT)
