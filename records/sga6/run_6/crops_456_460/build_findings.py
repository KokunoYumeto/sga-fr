"""Build findings_456_460.json, check every fix against the page files (applied in list order per page,
each 'old' exactly once at its turn, never across a marker line), and simulate the three marker moves in
both main.tex layers in memory (main.tex is only read)."""
import json, pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")
NL = "\n"
HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
B = RUN / "b456_460"
SGA6 = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
OUT = RUN / "findings_456_460.json"

M456 = "%%%%%%%%%%  scan idx 469  |  folio 456  %%%%%%%%%%"
M460 = "%%%%%%%%%%  scan idx 473  |  folio 460  %%%%%%%%%%"
M461 = "%%%%%%%%%%  scan idx 474  |  folio 461  %%%%%%%%%%"

pages = {n: (B / f"page_{n}.tex").read_text(encoding="utf-8") for n in range(456, 461)}
layers = {L: (SGA6 / L / "main.tex").read_text(encoding="utf-8") for L in ("diplomatic", "current")}
import datetime
STAMP = max(datetime.datetime.fromtimestamp((SGA6 / L / "main.tex").stat().st_mtime) for L in ("diplomatic", "current")).strftime("%H:%M:%S")
print("main.tex time:", STAMP)

def esc(s):
    """Quote a TeX string for a note: newlines as \\n."""
    return s.replace(NL, r"\n")

def line_of(text, i):
    return text.count(NL, 0, i) + 1

# ---- marker moves in main.tex (exact strings, same in both layers) ----
A_old = r"\subsection*{4.7}" + NL + NL + "On" + NL + M456 + NL
A_new = M456 + NL + r"\subsection*{4.7}" + NL + NL + "On" + NL
B_old = "la suite" + NL + M460 + NL + "exacte :" + NL
B_new = "la suite" + NL + "exacte :" + NL + M460 + NL
# C: taken from the snapshot (page_461.tex of batch 461-465 begins with 'donc :' and the display)
p461 = (RUN / "b461_465" / "page_461.tex").read_text(encoding="utf-8")
k0 = p461.index(M461 + NL) + len(M461 + NL)
k1 = p461.index(NL + "\\]" + NL, k0) + len(NL + "\\]" + NL)
C_disp = p461[k0:k1]
assert C_disp.startswith("donc :" + NL)
C_old = "et définissent" + NL + M461 + NL + C_disp
C_new = "et définissent" + NL + C_disp + M461 + NL
H_old = r"\subsection*{4.7}"
H_new = r"\subsection*{4.7.}"

sim = {}
for L, txt in layers.items():
    info = {}
    for name, old, new in (("A", A_old, A_new), ("B", B_old, B_new), ("C", C_old, C_new), ("H", H_old, H_new)):
        c = txt.count(old)
        i = txt.find(old)
        info[name] = (c, line_of(txt, i), line_of(txt, i + len(old) - 1))
    c_new = txt.count(C_new); i_new = txt.find(C_new)
    info["C_applied"] = (c_new, line_of(txt, i_new) if i_new >= 0 else None, line_of(txt, i_new + len(C_new) - 1) if i_new >= 0 else None)
    t2 = txt.replace(A_old, A_new).replace(B_old, B_new).replace(C_old, C_new).replace(H_old, H_new)
    for mk in (M456, M460, M461):
        k = t2.find(mk)
        info["after_" + mk[29:38].strip()] = repr(t2[max(0, k - 90):k + len(mk) + 90])
    sim[L] = info
    print(L, {k: v for k, v in info.items() if not k.startswith("after")})
    for k, v in info.items():
        if k.startswith("after"):
            print("   ", k, v)

dA, cA = sim["diplomatic"]["A"], sim["current"]["A"]
dB, cB = sim["diplomatic"]["B"], sim["current"]["B"]
dC, cC = sim["diplomatic"]["C_applied"], sim["current"]["C_applied"]
C_APPLIED = sim["diplomatic"]["C"][0] == 0 and sim["current"]["C"][0] == 0 and dC[0] == 1 and cC[0] == 1
print("folio-461 move already in main.tex:", C_APPLIED)
dH, cH = sim["diplomatic"]["H"], sim["current"]["H"]

F = []
def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": confidence, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)

# ================= page 456 =================
add(456, "start of page (folio-456 marker)",
    "p. 456 begins '4.7. On revient à la situation de 3.7, où on avait le diagramme commutatif :'; p. 455 ends with Remarque 4.6.1 ('... Pour un contre-exemple, voir XIV 4.6.') (both scans; crops_456_460/wit_456_half.png, b456_460/page_456_s1.png)",
    "page_455.tex ends '\\subsection*{4.7}', a blank line and 'On' above the folio-456 marker; page_456.tex begins 'revient à la situation de 3.7'",
    "marker", "high", None,
    "Page 456 really begins at '\\subsection*{4.7}' (a heading at the top of the page, which the 10 Nov script did not move). "
    f"Exact edit in main.tex, both layers (diplomatic lines {dA[1]}-{dA[2]}, current {cA[1]}-{cA[2]}): replace '{esc(A_old)}' by '{esc(A_new)}' "
    f"(line numbers as of the {STAMP} main.tex; old string once per layer; simulated in memory: crops_456_460/build_findings.py). The heading's missing full stop is the next entry. "
    "The checker of p. 455 may report the same boundary: apply once.")
add(456, "heading 4.7 (stands above the folio-456 marker, in page_455.tex)",
    "'4.7.' with a full stop, run into 'On revient' (both scans)",
    "\\subsection*{4.7} (no full stop)",
    "punctuation", "high", None,
    f"No page fix possible while the heading sits in page_455.tex. Exact edit in main.tex, both layers (diplomatic line {dH[1]}, current {cH[1]}, as of the {STAMP} main.tex; once per layer): "
    "'\\subsection*{4.7}' -> '\\subsection*{4.7.}', as the paragraph-number fixes of pp. 394, 401, 402, 429, 430 (findings_391_395 to findings_426_430). "
    "Independent of the marker move; the run-in heading set as its own paragraph is accepted.")
add(456, "diagram of 4.7, bottom arrow Y → X",
    "label i above the bottom arrow (both scans; wit_456_half.png)",
    "\\arrow[r,\"i\"'] (the ' sets the label below the arrow)",
    "formula", "medium", {"old": "\\arrow[r,\"i\"']", "new": "\\arrow[r,\"i\"]"},
    "Label on the wrong side of the arrow; j above, g left, f right stand as printed. The same diagram of Théorème 4.8 (p. 459) has the same entry.")
add(456, "hypothesis iii), end: 'i_*(λ^n(N,y)) = λ^n(i_*(y)) (relation (4.3.1)'",
    "'(rela-' / 'tion (4.3.1)': one closing parenthesis and no full stop; the indented paragraph 'On utilise d'abord' follows (both scans; crops_456_460/c456_tion.png, w456_iii.png)",
    "(relation (4.3.1)). (silently corrected)",
    "misprint_in_print", "high", {"old": "(relation (4.3.1)).", "new": "(relation (4.3.1)"},
    "The typist left '(relation' unclosed and the last hypothesis without its full stop (i) and ii) end with ';'); the TeX supplies both. "
    "The current layer also reads '(relation (4.3.1)).' (the corrected edition keeps it).",
    corrected="(relation (4.3.1)).")
add(456, "'On utilise d'abord VI.I.1 pour construire'",
    "'VI.I.1': full stops between the parts of the reference (both scans; crops_456_460/c456_VI11_zoom.png, w456_VI11_zoom.png)",
    "VI 1.1 (a space after VI)",
    "punctuation", "high", {"old": "VI 1.1", "new": "VI.1.1"},
    "The print writes this reference with full stops (the other references of these pages, V 4.9, V 2.4.2, VI 5.9, have the space, as in the TeX). "
    "Apply before the misprint entry that follows (together they give the printed 'VI.I.1').")
add(456, "'On utilise d'abord VI.I.1 pour construire' (second part of the reference)",
    "'VI.I.1': the middle numeral is a capital I with serifs on both sides at top and foot, the same glyph as the I of VI; the last is the typewriter's digit 1 with its flag (both scans; crops_456_460/c456_VI11_zoom.png, w456_VI11_zoom.png)",
    "VI 1.1 (silently corrected)",
    "misprint_in_print", "medium", {"old": "1.1 pour construire", "new": "I.1 pour construire"},
    "Capital I typed for the digit 1 (the typewriter has a 1, used in the same reference; Exposé VI numbers its paragraphs 1, 2, ...). "
    "Apply after the punctuation entry above (VI 1.1 -> VI.1.1); this 'old' is unique before and after it, and the two together give the printed 'VI.I.1'. The current layer also reads 'VI 1.1'.",
    corrected="VI.1.1")
add(456, "'une K-λ-algèbre K_1 qui joue le rôle de K˙(Y')'",
    "no comma after K_1 (both scans; crops_456_460/c456_VI11.png, w456_VI11.png)",
    "\\(K_1\\), qui joue",
    "punctuation", "high", {"old": "\\(K_1\\), qui joue", "new": "\\(K_1\\) qui joue"},
    "Comma added by the TeX. The two λ of 'K-λ-algèbre' on this line and the next are hand-drawn, with a hooked top stroke: plain λ, as the TeX has them.")
add(456, "'la K-λ-algèbre engendrée par le générateur L soumis aux relations'",
    "no comma after L (both scans)",
    "générateur \\(L\\), soumis",
    "punctuation", "high", {"old": "générateur \\(L\\), soumis", "new": "générateur \\(L\\) soumis"},
    "Comma added by the TeX.")
add(456, "'soumis aux relations λ^i(L) = 0 pour i ≥ 2 (V 4.9)'",
    "a blank before the raised i: no λ, typed or hand-drawn, in either scan (crops_456_460/c456_rel_contrast.png, w456_rel_contrast.png); 'relations   ^i (L) = 0'",
    "\\(\\lambda^i(L)=0\\) (silently corrected)",
    "misprint_in_print", "high", {"old": "\\(\\lambda^i(L)=0\\)", "new": "\\({}^i(L)=0\\)"},
    "The hand-drawn λ (as the two of 'K-λ-algèbre' just above) was never put in; the typist left its space before the superscript i. "
    "A speck above the '(' in the main scan only is not a stroke. The current layer also reads \\lambda^i(L)=0.",
    corrected="\\(\\lambda^i(L)=0\\)")
add(456, "K˙ on pp. 456, 459, 460 (29 places: 9 on p. 456, 5 on p. 459, 15 on p. 460)",
    "K with a raised filled dot in every place (both scans; e.g. crops_456_460/c456_Kdot.png, c456_lamanneaux.png)",
    "K^\\circ",
    "symbol", "high", None,
    "The Exposé VII convention reported in findings_416_420 and findings_431_435 (one script K^\\circ -> K^{\\bullet} for VII, both layers): not itemized. "
    "Three examples: p. 456 'K^\\circ(Y')\\times K^\\circ(X)' -> 'K^{\\bullet}(Y')\\times K^{\\bullet}(X)'; "
    "p. 459 'on voit que \\(K^\\circ(X')\\) se construit' -> 'on voit que \\(K^{\\bullet}(X')\\) se construit'; "
    "p. 460 'f^{\\gr}:\\operatorname{Gr}^kK^\\circ(X)\\to' -> 'f^{\\gr}:\\operatorname{Gr}^kK^{\\bullet}(X)\\to'.")

# ================= page 457 =================
add(457, "first line: 'L'idéal engendré par P est un λ-idéal.'",
    "'λ-idéal' as one word (both scans)",
    "'\\(\\lambda\\)-' ends a source line and 'idéal.' begins the next: the line end prints as a space ('λ- idéal')",
    "other", "medium", {"old": "\\(\\lambda\\)-" + NL + "idéal", "new": "\\(\\lambda\\)-idéal"},
    "Spurious space after the hyphen (the line break next to the old marker position).")
add(457, "'Si on se place dans 1 + K/(P)[[t]]^+'",
    "a wide hand-drawn hat over K/(P)[[t]], the + set after it (both scans; crops_456_460/c457_hat1.png, wit_457_half.png)",
    "\\(1+K/(P)[[t]]^+\\) (no hat)",
    "formula", "high", {"old": "\\(1+K/(P)[[t]]^+\\)", "new": "\\(1+\\widehat{K/(P)[[t]]}^+\\)"},
    "The completion hat is missing; \\widehat as main.tex writes \\widehat{K^{\\bullet}(S)[[t]]}^{+} in Exposé VI (diplomatic line 9865).")
add(457, "'Comme dans 1 + K[[t]]^+ on a λ_t(λ^d(N-L)) = ...'",
    "a hand-drawn hat over K[[t]], the + after it (both scans; crops_456_460/c457_hat2.png, wit_457_half.png)",
    "\\(1+K[[t]]^+\\) (no hat)",
    "formula", "high", {"old": "\\(1+K[[t]]^+\\)", "new": "\\(1+\\widehat{K[[t]]}^+\\)"},
    "As the entry above.")
add(457, "'y' = y_o + y_1L^{-1} + ... + y_{d-1}L^{-d+1}'",
    "three typed full stops on the baseline between the plus signs (both scans; crops_456_460/c457_dots.png)",
    "+\\cdots+",
    "symbol", "low", {"old": "+\\cdots+", "new": "+\\ldots+"},
    "The pattern of GLOBAL_ISSUES 87 (Exposé V: typed baseline '...' in sums written \\cdots, a pending volume decision); the only \\cdots of pp. 456-460. "
    "Drop this entry if that decision is applied to Exposé VII as well.")

# ================= page 458 =================
add(458, "first line: 'et on définit un homomorphisme :'",
    "' :' after 'homomorphisme', before the display u : K → K_1 x K' (both scans; wit_458_half.png)",
    "définit un homomorphisme (no colon)",
    "punctuation", "high", {"old": "définit un homomorphisme" + NL + "\\[", "new": "définit un homomorphisme :" + NL + "\\["},
    "Colon dropped by the TeX.")
add(458, "'la relation i_*(y_1y_2λ_{-1}(N)) = i_*(y_1).i_*(y_2) qui résulte immédiatement des hypothèses'",
    "the formula stands in the running line between 'relation' and 'qui résulte', with no comma after it (both scans)",
    "a display \\[ ... \\] ending with a comma",
    "other", "medium",
    {"old": "la relation" + NL + "\\[" + NL + "  i_*(y_1y_2\\lambda_{-1}(N))=i_*(y_1).i_*(y_2)," + NL + "\\]" + NL + "qui résulte",
     "new": "la relation \\(i_*(y_1y_2\\lambda_{-1}(N))=i_*(y_1).i_*(y_2)\\) qui résulte"},
    "The print sets the formula inline; the TeX makes it a display and adds a comma (same kind of fix as pp. 301, 303, 326, 332, 338, 351).")
add(458, "display 'K'_1 = (K_1 x K') / K'",
    "no punctuation after the display; 'et on note v' follows (both scans)",
    "K'_1=(K_1\\times K')/K,",
    "punctuation", "high", {"old": "K'_1=(K_1\\times K')/K,", "new": "K'_1=(K_1\\times K')/K"},
    "Comma added at the end of the display.")
add(458, "'On définit ensuite des homomorphismes additifs :'",
    "begins a new, indented paragraph after '... grâce à la structure quotient.' (both scans; wit_458_half.png)",
    "continues the paragraph: 'structure quotient. On définit ensuite'",
    "other", "high", {"old": "structure quotient. On définit", "new": "structure quotient." + NL + NL + "On définit"},
    "Missing paragraph break.")
add(458, "display of the four maps j_*, j*, f_*, f*",
    "two rows: 'j_* : K_1 → K'_1 ; j* : K'_1 → K_1 ;' above 'f_* : K'_1 → K' ; f* : K' → K'_1 .' (both scans)",
    "one array row of four columns (the source line break after the second '&' is not a row break): the four maps print on one line",
    "other", "low", {"old": "j^*:K'_1\\to K_1; &" + NL, "new": "j^*:K'_1\\to K_1; \\\\" + NL},
    "Layout of the display: two rows of two, as printed.")
add(458, "'L'homomorphisme j_* est le composé K_1 → K_1 x K' → K'_1.'",
    "begins a new, indented paragraph after the display of the four maps (both scans; wit_458_half.png)",
    "follows '\\]' without a blank line, so it continues the paragraph unindented",
    "other", "medium", {"old": "\\]" + NL + "L'homomorphisme", "new": "\\]" + NL + NL + "L'homomorphisme"},
    "Missing paragraph break.")

# ================= page 459 =================
add(459, "after Proposition 4.7.6: 'Il suffit de faire tourner la machine.'",
    "a new, indented paragraph after item v), indented as 'Si on en revient' below and deeper than the items (both scans; crops_456_460/wit_459_half.png)",
    "follows \\end{enumerate} without a blank line, so it prints unindented as a continuation",
    "other", "medium", {"old": "\\end{enumerate}" + NL + "Il suffit", "new": "\\end{enumerate}" + NL + NL + "Il suffit"},
    "Missing paragraph break.")
add(459, "'Si on en revient à la situation géométrique rappellée plus haut'",
    "'rappellée' (both scans)",
    "rappellée (the printed reading kept)",
    "misprint_in_print", "high", None,
    "The typist's spelling (rappeler: rappelée); the diplomatic TeX keeps it. The current layer also reads 'rappellée': the corrected edition needs 'rappelée'.",
    corrected="rappelée")
add(459, "diagram of Théorème 4.8, bottom arrow Y → X",
    "label i above the bottom arrow (both scans)",
    "\\arrow[r,\"i\"'] (the ' sets the label below the arrow)",
    "formula", "medium", {"old": "\\arrow[r,\"i\"']", "new": "\\arrow[r,\"i\"]"},
    "As the diagram of 4.7 on p. 456; j above, g left, f right stand as printed.")
add(459, "statements on pp. 458-460: Proposition 4.7.5 (p. 458), Proposition 4.7.6 (p. 459), Théorème 4.8 (pp. 459-460)",
    "underlined word group by word group (both scans): 4.7.5 'Les opérations définies par', 'et', 'munissent', 'd'une structure de', 'anneau', 'et', "
    "'est un homomorphisme injectif qui', 'identifie', 'muni des opérations définies par', 'et', 'à un', 'idéal de'; "
    "4.7.6 'et', 'sont des', 'homomorphismes', 'est', 'linéaire et', 'est', 'linéaire', 'est l'homomorphisme', 'multiplication par', 'pour tout', 'et tout'; "
    "4.8 'Soient', 'une immersion fermée régulière de codimension constante', 'le schéma obtenu en faisant éclater', 'et', 'de sorte qu'on a le diagramme commutatif', "
    "'On suppose que', 'est quasi-compact et a un faisceau ample', 'Alors on a pour tout', 'la suite exacte', 'où on pose', 'pour', 'et pour', 'et', "
    "'les notations étant celles de', 'et', 'et', 'désignant la', 'ième', 'classe de Chern de', 'En outre', 'admet un inverse à gauche', 'défini par', "
    "'Si de plus', 'est noethérien et', 'régulier', 'on a la suite exacte'; formulas, letters, numbers and punctuation plain; the labels underline only the word",
    "the statements in roman (no \\underline, no \\emph)",
    "underline", "high", None,
    "Exposé VII follows the Exposé II pattern of GLOBAL_ISSUES 82 (as reported for pp. 416-420): not itemized; the word groups are listed for the scripted pass. "
    "The underlined 'Démonstration' of p. 460 is \\emph{Démonstration.}, the file's form. No category letter and no underlined letters of sheaves on pp. 456-460.")

# ================= page 460 =================
add(460, "start of page (folio-460 marker)",
    "p. 459 ends 'Alors on a pour tout k la suite exacte :'; p. 460 begins with the display '0 → Gr^{k-d}K˙(Y)_Q → Gr^{k-1}K˙(Y')_Q x Gr^kK˙(X)_Q → Gr^kK˙(X')_Q' (both scans; wit_460_half.png, b456_460/page_459_s4.png)",
    "page_460.tex begins with 'exacte :' after the folio-460 marker; page_459.tex ends 'la suite'",
    "marker", "high", None,
    "Page 460 really begins at the display's '\\[' after 'exacte :' (the marker stands one line too early). "
    f"Exact edit in main.tex, both layers (diplomatic lines {dB[1]}-{dB[2]}, current {cB[1]}-{cB[2]}): replace '{esc(B_old)}' by '{esc(B_new)}' "
    f"(line numbers as of the {STAMP} main.tex; old string once per layer; simulated in memory: crops_456_460/build_findings.py).")
add(460, "end of page (folio-461 marker)",
    "p. 460 ends '... passent aux gradués associés, et définissent donc :' and the display 'i_gr : Gr^{k-d}K˙(Y)_Q → Gr^kK˙(X)_Q ; j_gr : Gr^{k-1}K˙(Y')_Q → Gr^kK˙(X')_Q .'; p. 461 begins 'Enfin, on remarque que λ_{-1}(F) = (-1)^{d-1}γ^{d-1}(F)' (both scans; wit_460_half.png, crops_456_460/w461_top.png)",
    "page_460.tex ends 'et définissent'; 'donc :' and the i_gr/j_gr display stand after the folio-461 marker (top of page_461.tex)",
    "marker", "high", None,
    ("ALREADY APPLIED IN MAIN.TEX, NO ACTION. " if C_APPLIED else "") +
    "Page 461 really begins at 'Enfin, on remarque': the folio-461 marker line belongs directly after the '\\]' that closes the i_gr/j_gr display. "
    f"Exact edit: replace '{esc(C_old)}' by '{esc(C_new)}'. " +
    (f"main.tex (both layers, as of {STAMP}) already has the new form (diplomatic lines {dC[1]}-{dC[2]}, current {cC[1]}-{cC[2]}) and no longer the old one, "
     "evidently from the report of batch 461-465; listed because page_460.tex of this batch still ends at 'et définissent'. The moved lines match the print of p. 460."
     if C_APPLIED else
     "(old string once per layer). The moved lines match the print of p. 460. The checker of p. 461 may report the same boundary: apply once."))
add(460, "first display: '0 → Gr^{k-d}K˙(Y)_Q → ... → Gr^kK˙(X')_Q'",
    "no punctuation after the last term; 'où on pose' follows (both scans; crops_456_460/c460_d1end.png, w460_d1end.png)",
    "\\operatorname{Gr}^{k}K^\\circ(X')_{\\mathbb Q}, (comma at the end of the display)",
    "punctuation", "high", {"old": "K^\\circ(X')_{\\mathbb Q}," + NL + "\\]", "new": "K^\\circ(X')_{\\mathbb Q}" + NL + "\\]"},
    "Comma added at the end of the display.")
add(460, "'En outre, u^gr admet un inverse à gauche u'^gr, défini par u'^gr(y',x) = g_gr(y').' and the next paragraph 'Si de plus ...'",
    "the formula stands in the running line after 'défini par', with the full stop; 'Si de plus X est noethérien' then begins a new, indented paragraph (both scans; wit_460_half.png)",
    "a display \\[ u'^{\\gr}(y',x)=g_{\\gr}(y'). \\] followed without a blank line by 'Si de plus' (which then continues the paragraph unindented)",
    "other", "medium",
    {"old": "défini par" + NL + "\\[" + NL + "  u'^{\\gr}(y',x)=g_{\\gr}(y')." + NL + "\\]" + NL + "Si de plus",
     "new": "défini par \\(u'^{\\gr}(y',x)=g_{\\gr}(y')\\)." + NL + NL + "Si de plus"},
    "The print sets the formula inline (as p. 458) and starts a new paragraph at 'Si de plus'; the one edit does both.")
add(460, "second exact sequence: '... → Gr^kK˙(X')_Q → 0'",
    "no full stop after the final 0; 'Démonstration.' follows (both scans; crops_456_460/c460_d4end.png, w460_d4end.png)",
    "\\longrightarrow0.",
    "punctuation", "high", {"old": "\\longrightarrow0." + NL + "\\]", "new": "\\longrightarrow0" + NL + "\\]"},
    "Full stop added at the end of the display.")
add(460, "display 'f^gr : Gr^kK˙(X) → Gr^kK˙(X') ; g^gr : Gr^{k-d}K˙(Y) → Gr^{k-d}K˙(Y')'",
    "a comma after the last term; 'et les homomorphismes analogues' follows in lower case (both scans; crops_456_460/c460_comma.png, w460_comma.png)",
    "\\operatorname{Gr}^{k-d}K^\\circ(Y'). (full stop)",
    "punctuation", "high", {"old": "K^\\circ(Y')." + NL + "\\]", "new": "K^\\circ(Y')," + NL + "\\]"},
    "The TeX ends the display with a full stop where the print has a comma.")

# ---- validate: apply fixes in order per page ----
ok = True
state = dict(pages)
for f in F:
    fx = f["fix"]
    if fx is None:
        continue
    p = f["page"]; old, new = fx["old"], fx["new"]
    c = state[p].count(old)
    if c != 1:
        ok = False; print("NOT UNIQUE", p, c, repr(old))
    if "%%%%%%%%%%" in old or "%%%%%%%%%%" in new:
        ok = False; print("MARKER IN FIX", p, repr(old))
    state[p] = state[p].replace(old, new, 1)
# also each old once in the original page file, except chained fixes
for f in F:
    fx = f["fix"]
    if fx is None:
        continue
    c0 = pages[f["page"]].count(fx["old"])
    if c0 != 1:
        print("note: old not in original page file (chained):", f["page"], repr(fx["old"]), c0)
for L, info in sim.items():
    for k in (("A", "B", "H") if C_APPLIED else ("A", "B", "C", "H")):
        if info[k][0] != 1:
            ok = False; print("MAIN.TEX OLD NOT UNIQUE", L, k, info[k])
print("validation", "OK" if ok else "FAILED")
counts = {}
for f in F:
    c = counts.setdefault(f["page"], [0, 0])
    c[1 if f["kind"] == "misprint_in_print" else 0] += 1
print("counts (normal/misprint):", counts)
if ok:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + NL, encoding="utf-8", newline=NL)
    print("wrote", OUT, len(F))
    json.loads(OUT.read_text(encoding="utf-8"))
