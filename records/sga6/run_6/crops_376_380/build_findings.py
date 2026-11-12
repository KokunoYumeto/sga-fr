"""Build findings_376_380.json and check that every fix's 'old' occurs exactly once in its page_NNN.tex."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
NL = "\n"
F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": confidence, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def para(page, where, old_end, start, scan_extra=""):
    label = start.replace(NL, " ")
    add(page, where,
        f"'{label}' begins a new, indented paragraph after the display (both scans{scan_extra})",
        f"'{old_end}' followed directly by '{label}' (no blank line: the paragraph runs on)",
        "other", "high", {"old": old_end + NL + start, "new": old_end + NL + NL + start},
        "Missing paragraph break.")


# ---------------- p. 376 ----------------
add(376, "first display: (f_*(F(n))) - (f_*(G(n))) = Σ_i n_i((f_*(L_i(n)) - (f_*(M_i(n))) + (f_*(N_i(n)))).",
    "n_i((f_*(L_i(n))-(f_*(M_i(n))) / +(f_*(N_i(n)))). : two closing parentheses after L_i(n), three after M_i(n), "
    "four after N_i(n), so the bracket of the first class is never closed and the formula has one '(' more than ')' "
    "(both scans; crops_376_380/c376_disp1.png, w376_top.png)",
    r"\bigl((f_*(L_i(n)))-(f_*(M_i(n)))\\ ... +(f_*(N_i(n)))\bigr). : balanced (silently corrected)",
    "misprint_in_print", "high",
    {"old": r"\bigl((f_*(L_i(n)))-", "new": r"\bigl((f_*(L_i(n))-"},
    "Typing error of the print (a ')' left out); the diplomatic layer should reproduce the unbalanced printed formula.",
    corrected=r"\bigl((f_*(L_i(n)))-")
para(376, "after the first display: 'D'après 1.2, pour n assez grand'", r"\]", "D'après 1.2,")
para(376, "after '... sont localement libres de type fini.': 'Il en résulte que'", r"\]", "Il en résulte")
para(376, "after (1.11.1): 'On peut écrire chacun des x_j'", r"\end{equation}", "On peut écrire")
para(376, "after the display F = ⊕ f^*(E_j)(j), F' = ⊕ f^*(E'_j)(j): 'L'égalité (1.11.1) s'écrit alors'", r"\]",
     "L'égalité (1.11.1)")
para(376, "after cl_{K˙(X)}(F) = cl_{K˙(X)}(F'): 'D'après le lemme 1.10'", r"\]", "D'après le lemme 1.10")
add(376, "letters of sheaves and Modules on pp. 376-380",
    "underlined in the print: F, G, L_i, M_i, N_i, F', E_j, E'_j (p. 376); F, E_j, the E of S(E), of ∧^r(E) and of "
    "E⊗, 'où E est libre' (p. 377); E in 'Or E est de rang', 'de type fini E', 'symétrique de E' (p. 378); F, E, F̌, Ě "
    "of the two exact sequences and E in 'si E = (O_S)^{r+1}' (p. 379); E, B, L˙ (p. 380). Plain in the print: the E "
    "of λ^i(E) (pp. 377-378), λ^{r+1}(E), σ_i(E), σ_t(E) (p. 378), λ_t(E), σ_{-t}(E), the F̌, Ě of γ^{r+1}(F̌-r), "
    "γ^{r+1}(Ě-r-1+x) and (1.13.1), and 'on a E = r+1' (p. 379); S, X throughout (both scans; c378_sigmaE.png, "
    "c379_gamma.png, c377_1113.png)",
    "all plain: Exposé VI has one \\underline (folio 365)",
    "underline", "high", None,
    "Convention of the Exposé VI transcription, already reported on p. 366 (findings_366_370): not itemized. Three "
    "examples, in the form to use if the diplomatic layer reproduces it: p. 376 'f_*(F(n))\\bigr)-\\bigl(f_*(G(n))' "
    "-> 'f_*(\\underline{F}(n))\\bigr)-\\bigl(f_*(\\underline{G}(n))'; p. 378 'Or \\(E\\) est de rang' -> "
    "'Or \\(\\underline{E}\\) est de rang'; p. 380 'des \\(B\\)-Modules gradués avec' -> "
    "'des \\(\\underline{B}\\)-Modules gradués avec'. Not for a blind script: the E inside λ, σ, γ and 'on a E = r+1' "
    "are plain in the print. The underlined O of O_X, O_S is \\mathcal O here (pending volume decision).")

# ---------------- p. 377 ----------------
add(377, "display 'Or f_*(F(n)) = ⊕ f_*(f^*(E_j) ⊗_{O_X} O_X(n+j))', first line",
    "the direct-sum sign has no index, in both lines of the display (both scans; crops_376_380/c377_oplus.png, "
    "w377_top.png)",
    r"&=\bigoplus_j f_*\bigl(...", "formula", "high",
    {"old": r"&=\bigoplus_j f_*", "new": r"&=\bigoplus f_*"},
    "Summation index added by the transcription.")
add(377, "same display, second line '= ⊕ E_j ⊗_{O_S} f_*(O_X(n+j)) .'",
    "⊕ without index (both scans; c377_oplus.png, w377_top.png)",
    r"&=\bigoplus_j E_j\otimes_{\mathcal O_S} ...", "formula", "high",
    {"old": r"&=\bigoplus_j E_j", "new": r"&=\bigoplus E_j"},
    "Summation index added by the transcription; independent of the entry above.")
para(377, "after the display of f_*(F(n)): 'Par ailleurs, f_*(O_X(n+j)) = S(E)^{n+j}'", r"\]", "Par" + NL + "ailleurs")
add(377, "the formula defining the arrows: '(x_1∧...∧x_n)⊗(y_1⊗...⊗y_p) ⤳ Σ(-1)^{i-1}(...)'",
    "Σ(-1)^{i-1}: the sum sign has no index (both scans; crops_376_380/c377_arrow.png, w377_top.png)",
    r"\sum_i(-1)^{i-1}", "formula", "high",
    {"old": r"\sum_i(-1)^{i-1}", "new": r"\sum(-1)^{i-1}"},
    "Summation index added by the transcription.")
add(377, "end of the same formula: '...⊗(x_i⊗y_1⊗...⊗y_p)'",
    "the display ends '⊗y_p)' with no full stop; 'Si on considère' follows at the margin (both scans; c377_arrow.png, "
    "w377_top.png)",
    r"\otimes y_p).", "punctuation", "high",
    {"old": r"\otimes y_p).", "new": r"\otimes y_p)"},
    "Full stop added at the end of the display.")
add(377, "(1.11.3): Σ_{i=0}^{r+1}(-1)^i λ^i(E) σ_{p-i} = 0",
    "σ_{ρ-i}: the first letter of the index is a Greek rho, from the same type element as σ and λ, not the Latin "
    "serif p of 'pour tout p ⩾ 1' on the same line (both scans; crops_376_380/c377_1113.png, w377_rho.png)",
    r"\sigma_{p-i} (silently corrected)", "misprint_in_print", "high",
    {"old": r"\sigma_{p-i}", "new": r"\sigma_{\rho-i}"},
    "Typing error: the typist stayed on the Greek element for the index; p is meant ('pour tout p ⩾ 1').",
    corrected=r"\sigma_{p-i}")
add(377, "typed dots in formulas, pp. 376-377",
    "'...' typed on the baseline: (1.11.1) '+ ... +' (p. 376); the complex '→ ... →' and "
    "'(x_1∧...∧x_n)⊗(y_1⊗...⊗y_p) ⤳ Σ(-1)^{i-1}(x_1∧...∧x̂_i∧...∧x_n)⊗(x_i⊗y_1⊗...⊗y_p)' (p. 377) "
    "(both scans; crops_376_380/c376_dots.png, c377_dots1.png)",
    "\\cdots (7 on these pages: p. 376 one, p. 377 six); lists such as 1,ξ,...,ξ^r have \\ldots",
    "symbol", "medium", None,
    "Convention, as in Exposé V (GLOBAL_ISSUES 87): Exposé VI has 32 \\cdots (folios 365-414) and 66 \\ldots; not "
    "itemized. Three examples: p. 376 'f^*(x_1)\\xi+\\cdots+f^*(x_r)' -> 'f^*(x_1)\\xi+\\ldots+f^*(x_r)'; p. 377 "
    "'\\longrightarrow\\cdots\\longrightarrow' -> '\\longrightarrow\\ldots\\longrightarrow'; p. 377 "
    "'(y_1\\otimes\\cdots\\otimes y_p)\\rightsquigarrow' -> '(y_1\\otimes\\ldots\\otimes y_p)\\rightsquigarrow'. "
    "For the closing pass with Exposé V.")

# ---------------- p. 378 ----------------
OLD_EQ = (r"\begin{equation}\tag{1.11.4}" + NL
          + r"  \sum_{j=0}^r x_j\left(\sum_{i=0}^{r+1}(-1)^i\lambda^i(E)\sigma_{p(j)-i}\right)=0," + NL
          + r"\end{equation}")
NEW_EQ = (r"\[" + NL
          + r"  \sum_{j=0}^r x_j\left(\sum_{i=0}^{r+1}(-1)^i\lambda^i(E)\sigma_{p(j)-i}\right)=0," + NL
          + r"\]")
add(378, "the display after 'D'après (1.11.3), on peut écrire'",
    "no formula number: nothing stands left of the display (both scans; w378_top.png), and no formula on pp. 377-378 "
    "carries (1.11.4), although the text cites it twice below ('la relation (1.11.4) se réduit à :', 'Par suite, la "
    "relation (1.11.4) se réduit à la relation (1.11.2)')",
    r"\begin{equation}\tag{1.11.4} ... \end{equation} (number added: silently corrected)",
    "misprint_in_print", "high", {"old": OLD_EQ, "new": NEW_EQ},
    "The typist left out the number (1.11.4) that the text refers to; the TeX's placement is the right one (this is "
    "the relation that reduces to λ^{r+1}(E).(Σ x_jσ_{n_o-1+j}) = 0). The fix changes only the numbering.",
    corrected=OLD_EQ)
para(378, "after the display Σ_j x_j(Σ_i ...) = Σ_i (-1)^i λ^i(E)(Σ_j ...): 'Pour i ≠ r+1'", r"\]",
     r"Pour \(i\neq r+1\)")
para(378, "after Σ_j x_jσ_{n_o+r+j-i} = 0: 'Par conséquent, la relation (1.11.4)'", r"\]", "Par conséquent")
para(378, "after λ^{r+1}(E).(Σ_j x_jσ_{n_o-1+j}) = 0: 'Or E est de rang r+1'", r"\]", r"Or \(E\) est de rang")

# ---------------- p. 379 ----------------
para(379, "after (1.12.1): 'Cette relation elle-même montre'", r"\end{equation}", "Cette relation")
add(379, "'qui peut donc être prolongée en un homomorphisme de K˙(S)'",
    "'homomorpnisme': n for h, a complete n with its serifs and no trace of an ascender, while the h of 'homo' in the "
    "same word is whole (both scans; crops_376_380/c379_pn.png, w379_pn.png)",
    "homomorphisme (silently corrected)", "misprint_in_print", "high",
    {"old": "homomorphisme", "new": "homomorpnisme"},
    "Typing error (h and n are neighbouring keys); the diplomatic layer should keep the printed reading.",
    corrected="homomorphisme")
add(379, "Remarque 1.13: 'n'importe quelle suite de puissances de ξ ; ξ^k,...,ξ^{k+r+1}'",
    "ξ^k,...,ξ^{k+r+1} (both scans; w379_top.png)",
    r"\(\xi^k,\ldots,\xi^{k+r+1}\) (printed reading kept)", "misprint_in_print", "medium", None,
    "Author's slip: a basis of K˙(X) over K˙(S) has r+1 elements (1,ξ,...,ξ^r in 1.1; 1,x,...,x^r a few lines "
    "below), and r+2 consecutive powers satisfy (1.9.1), so they are not linearly independent. The diplomatic layer is "
    "right; corrected edition: ξ^{k+r}.",
    corrected=r"\(\xi^k,\ldots,\xi^{k+r}\)")
add(379, "Remarque 1.13: 'composée d'éléments linéairement indépendant sur K˙(S)'",
    "'indépen-dant' without s (both scans; w379_top.png)",
    "linéairement indépendant sur (printed reading kept)", "misprint_in_print", "high", None,
    "Agreement error; the diplomatic layer is right.",
    corrected="linéairement indépendants")
add(379, "'Pour obtenir l'équation de dépendance de 1,...,x^{r+1} on considère la suite exacte'",
    "no comma after x^{r+1} at the end of the line; the next line begins 'on considère' (both scans; "
    "crops_376_380/c379_xr1.png, w379_xr1.png)",
    r"\(1,\ldots,x^{r+1}\), on considère", "punctuation", "high",
    {"old": r"x^{r+1}\), on considère", "new": r"x^{r+1}\) on considère"},
    "Comma added by the transcription.")
para(379, "after (1.13.1): 'On obtient un résultat analogue en introduisant x' = ξ-1'", r"\end{equation}",
     "On obtient un résultat")

# ---------------- p. 380 ----------------
add(380, "2.2: the categories of B-Modules gradués, 𝒞_o and of O_S-Modules (six places on p. 380)",
    "a hand-drawn script C: a top loop and a C-shaped bowl ending in a small curl on the baseline, no descender "
    "(both scans; crops_376_380/c380_C0.png, c380_C.png, c380_Cp.png, c380_ACC.png, w380_C.png); the same letter "
    "throughout § 2 (witness p. 387: 'Sur 𝒞', 'D^+(𝒞)', 'D^+(𝒞')', '𝒞_o-parfait'; w387_a.png). The volume's script G "
    "has a long descender (Exposé V p. 308, crops_306_310/c308_notera.png). Its first use ('·· la catégorie des "
    "B-Modules gradués') is lost in both scans except two dots; 𝒜 is right",
    "\\mathcal G, \\mathcal G_0, \\mathcal G' (six on p. 380; 30 \\mathcal G in Exposé VI, all in § 2: folios 380 (6), "
    "383, 384 (2), 386 (6), 387 (10), 388 (2), 389 (3), both layers)",
    "symbol", "high", None,
    "Convention of the § 2 transcription, reported once: \\mathcal G -> \\mathcal C in all 30 places (Exposé VI has "
    "no \\mathcal C and no other \\mathcal G; let the checkers of 381-389 confirm before the pass). Three examples: "
    "p. 380 '\\(\\mathcal G\\) la catégorie des \\(B\\)-Modules' -> '\\(\\mathcal C\\) la catégorie des "
    "\\(B\\)-Modules'; '\\(\\mathcal G_0\\) la sous-catégorie pleine de \\(\\mathcal G\\)' -> '\\(\\mathcal C_0\\) la "
    "sous-catégorie pleine de \\(\\mathcal C\\)'; 'Les catégories \\(\\mathcal A\\), \\(\\mathcal G\\), et "
    "\\(\\mathcal G'\\)' -> 'Les catégories \\(\\mathcal A\\), \\(\\mathcal C\\), et \\(\\mathcal C'\\)'.")
add(380, "'... dans la suite du séminaire. La notation K˙(X) désignera ...'",
    "'La notation' begins a new, indented paragraph (both scans)",
    "one paragraph", "other", "high",
    {"old": "du séminaire. La notation", "new": "du séminaire." + NL + NL + "La notation"},
    "Missing paragraph break.")
add(380, "'... sont abéliennes. Pour tout n, et tout complexe L˙ de D^+(𝒜)'",
    "'Pour tout n' begins a new, indented paragraph (both scans)",
    "one paragraph", "other", "high",
    {"old": "sont abéliennes. Pour tout", "new": "sont abéliennes." + NL + NL + "Pour tout"},
    "Missing paragraph break; independent of the category-letter convention above (no common text).")
add(380, "end of page 380 / start of page 381 (folio-381 marker)",
    "p. 380 ends with 'complexe L˙⊗_{O_X}O_X(n).'; p. 381 begins '2.3. Nous aurons besoin d'appliquer le foncteur "
    "Proj_o' (main scan page_380_s4.png; witness w381_top.png)",
    "page_380.tex ends with the line '\\textbf{2.3.}', above the folio-381 marker; 'Nous aurons besoin ...' follows "
    "the marker",
    "marker", "high", None,
    "The number of 2.3 (a heading at the top of p. 381, not moved by the script) stands one line above the "
    "folio-381 marker. Page 381 really begins with '\\textbf{2.3.}'. Exact fix in main.tex (both layers; the old "
    "string occurs once in each): replace '\\textbf{2.3.}\\n%%%%%%%%%%  scan idx 394  |  folio 381  %%%%%%%%%%\\n' "
    "by '%%%%%%%%%%  scan idx 394  |  folio 381  %%%%%%%%%%\\n\\textbf{2.3.}\\n' (simulated in memory on both layers, "
    "crops_376_380/sim_markers.py). Equivalent: python -I move_marker.py 6 381 '\\textbf{2.3.}' --before. The typeset "
    "text does not change (2.3 stays run in).")
add(380, "Théorème 2.1",
    "the statement is underlined word group by word group: 'Soient', 'un schéma quasi-compact', 'un', "
    "'-Module localement', 'libre de rang', 'le fibré projectif associé', 'soit', 'la classe', 'dans', "
    "'du complexe égal à', 'en degré nul', 'et nul pour les autres', 'degrés', 'Alors', "
    "'muni de sa structure naturelle de', 'algèbre est', 'un', 'module libre admettant pour base' (S, r+1, "
    "X = P(E), ξ, K˙(X), K˙(S)-, the punctuation and 1,ξ,...,ξ^r plain; E, O_S, O_X carry their own underlines; "
    "both scans)",
    "the statement in roman (no \\underline, no \\emph)",
    "underline", "high", None,
    "Exposé VI follows the Exposé II pattern of GLOBAL_ISSUES 82 (as on pp. 367-370): not itemized; the word groups "
    "are listed for the scripted pass. No emphasized defined terms on pp. 376-380; Remarques 1.12-1.14 underline "
    "only the label word.")

# ---------------- checks ----------------
bad = 0
for d in F:
    fx = d["fix"]
    if fx is None:
        continue
    t = (RUN / "b376_380" / f"page_{d['page']}.tex").read_text(encoding="utf-8")
    c = t.count(fx["old"])
    mk = "%%%%%%%%%%" in fx["old"]
    if c != 1 or mk:
        bad += 1
        print("BAD", d["page"], c, mk, repr(fx["old"][:60]))
# overlap check per page
for p in range(376, 381):
    t = (RUN / "b376_380" / f"page_{p}.tex").read_text(encoding="utf-8")
    spans = []
    for d in F:
        if d["page"] == p and d["fix"]:
            i = t.find(d["fix"]["old"])
            spans.append((i, i + len(d["fix"]["old"]), d["kind"]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            bad += 1
            print("OVERLAP", p, a, b)
    # apply all fixes in sequence to check each stays unique
    t2 = t
    for d in F:
        if d["page"] == p and d["fix"]:
            if t2.count(d["fix"]["old"]) != 1:
                bad += 1
                print("SEQ", p, repr(d["fix"]["old"][:50]))
            t2 = t2.replace(d["fix"]["old"], d["fix"]["new"], 1)
from collections import Counter
cnt = Counter((d["page"], d["kind"] == "misprint_in_print") for d in F)
for p in range(376, 381):
    print(p, "normal", cnt[(p, False)], "misprint", cnt[(p, True)])
print("entries", len(F), "bad", bad)
if not bad:
    (RUN / "findings_376_380.json").write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("written")
