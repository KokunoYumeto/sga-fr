"""Build findings_406_410.json and check that every fix's old occurs exactly once in its page file."""
import json, pathlib, sys
from collections import Counter
sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
B = RUN / "b406_410"
OUT = RUN / "findings_406_410.json"
M407 = "%%%%%%%%%%  scan idx 420  |  folio 407  %%%%%%%%%%"
M408 = "%%%%%%%%%%  scan idx 421  |  folio 408  %%%%%%%%%%"
F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 406 ----------------
add(406, "first display: 'f̄ (λ_t(F)) = f̄_*(λ_t(E)λ_t(-ξ)) = ...'",
    "the first f̄ has no lower star, a blank where it would stand; the two other members and the display 'f̄_*(λ_t(F)) = 1' below have it (both scans; crops_406_410/wit_406.png)",
    r"\bar f(\lambda_t(F))= (printed reading kept)",
    "misprint_in_print", "high", None,
    "The map is f̄_*. Same entry as findings_401_405 (filed under p. 405 while this display stood above the folio-406 marker, since moved). The current layer already reads \\bar f_*.",
    r"\bar f_*(\lambda_t(F))=")
add(406, "'Or f̄(λ_t(-ξ)) = Σ_{i≥0} (-1)^i f_*(ξ^i)t^i = σ_{-t}(E)'",
    "f̄ without the lower star (both scans; crops_406_410/wit_406.png)",
    r"Or $\bar f(\lambda_t(-\xi))= (printed reading kept)",
    "misprint_in_print", "high", None,
    "As the entry above; also in findings_401_405 as a p. 405 entry. The current layer already reads \\bar f_*.",
    r"Or $\bar f_*(\lambda_t(-\xi))=")
add(406, "same line: '= σ_{-t}(E) d'après (4.2.3)'",
    "'(4.2.3)' (both scans)",
    "d'après (4.2.3) (printed reading kept)",
    "misprint_in_print", "high", None,
    "f_*(ξ^n) = σ_n is (5.2.3) on p. 402; main.tex has no formula (4.2.3) (this line holds its only '4.2.3'). Also in findings_401_405 as a p. 405 entry. The current layer already reads (5.2.3).",
    "d'après (5.2.3)")
add(406, "'d'où les relations cherchées' (end of the paragraph before Proposition 5.10)",
    "no full stop after 'cherchées' (both scans; crops_406_410/w406_dou.png)",
    "d'où les relations cherchées. (silently corrected)",
    "misprint_in_print", "high",
    {"old": "d'où les relations cherchées.", "new": "d'où les relations cherchées"},
    "The typist left out the sentence's full stop; the diplomatic layer should drop it, the corrected edition keeps 'cherchées.'.",
    "d'où les relations cherchées.")
add(406, "display 'z = Σ_{i=0}^r a_i x'^i' after 'tels que :'",
    "no punctuation after the display (both scans; crops_406_410/w406_zdisp.png)",
    r"z=\sum_{i=0}^{r}a_i{x'}^i .",
    "punctuation", "high",
    {"old": "a_i{x'}^i .", "new": "a_i{x'}^i"},
    "Full stop added by the TeX.")
add(406, "statements of pp. 406-410: Propositions 5.10, 5.11, 6.1, Corollaires 6.2, 6.3, 6.4",
    "the print underlines the statements word group by word group, e.g. Proposition 5.10: 'Avec les notations et les hypothèses de' 5.1, 'soit' z ∈ K˙(X). 'Pour que' z(1-ξ) = 0, 'il faut et il suffit qu'il existe' y ∈ K˙(S), 'tel que' :",
    "the statements in roman (no \\underline, no \\emph)",
    "underline", "high", None,
    "Exposé VI follows the Exposé II pattern of GLOBAL_ISSUES 82 (pending volume decision), as findings_401_405 reports for pp. 403-405: not itemized.")

# ---------------- page 407 ----------------
add(407, "start of page (folio-407 marker)",
    "p. 406 ends with the display 'a_r c_o = 0 ; pour 0 ≤ i < r, a_i = a_r c_{i+1}.'; p. 407 begins 'Donc :' and the display 'z = a_r.( Σ_{i=0}^{r-1} c_{i+1}x'^i + x'^r ) .', then 'Or : ...' (both scans; crops_406_410/wit_407.png)",
    "page_406.tex ends with 'Donc :', the display for z, 'Or :' and '\\[' above the folio-407 marker; the marker stands inside the 'Or :' display, between '\\[' and '\\begin{aligned}'",
    "marker", "high", None,
    "Page 407 really begins at 'Donc :' (diplomatic main.tex line 10273, current 10279). Exact edit in main.tex, both layers: move the marker line '" + M407 + "' (diplomatic line 10279, current 10285) up to stand directly before the line 'Donc :', i.e. replace 'Donc :\\n\\[\\n  z=a_r.\\left(\\sum_{i=0}^{r-1}c_{i+1}{x'}^i+{x'}^r\\right).\\n\\]\\nOr :\\n\\[\\n" + M407 + "\\n' by '" + M407 + "\\nDonc :\\n\\[\\n  z=a_r.\\left(\\sum_{i=0}^{r-1}c_{i+1}{x'}^i+{x'}^r\\right).\\n\\]\\nOr :\\n\\[\\n' (each old string occurs once per layer; simulated in memory: crops_406_410/sim_markers.py). This also takes the marker out of the display.")
add(407, "'Or :' display, fourth member: '= (-1)^r γ^r(E-r-1-x') = (-1)^r γ^r(F-x')'",
    "'(F-x')' (both scans; crops_406_410/w407_gam.png, m407_gam.png)",
    r"&=(-1)^r\gamma^r(F-x')\\ (printed reading kept)",
    "misprint_in_print", "high", None,
    "With x' = ξ-1 and E = F+ξ (p. 402, 5.9), E-r-1-x' = F-r; the next member λ^r(F-1) = γ^r(F-r) confirms it. The current layer already reads F-r.",
    r"(-1)^r\gamma^r(F-r)")
add(407, "letters of sheaves on pp. 407-410 (first: 'un faisceau ample L.' at the start of § 6)",
    "underlined in the print: L (the ample sheaf) on pp. 407-408, E, E^*, E^*(n), E(-n), L^{⊗n} on p. 408, E_i on p. 409, E in Corollaire 6.3; the plain E, L, E_i stand for their classes",
    "all plain ($L$, $E$, $E^*$, $E_i$)",
    "underline", "high", None,
    "Convention of the Exposé VI transcription (reported for pp. 366-405 in findings_381_385, findings_386_390, findings_401_405): not itemized. Three places where the plain letter merges the sheaf with its class: p. 408 'en notant $L$ la classe de $L$' (print: L ... L underlined); p. 408 'où $E$ est la classe d'un $\\mathcal O_X$-Module localement libre de type fini $E$' (second E underlined); p. 409 'Soient $E_i$, $i=1,\\ldots,k$, les faisceaux ..., $E_i$ leurs classes' (first E_i underlined). The underlined O of O_X written \\mathcal O falls under the pending volume decision.")

# ---------------- page 408 ----------------
add(408, "start of page (folio-408 marker)",
    "p. 407 ends '... sont égaux (IV,2.9). On note'; p. 408 begins 'ε l'homomorphisme d'augmentation : K˙(X) → H°(X,Z).' (both scans; crops_406_410/wit_407.png, wit_408.png)",
    "page_407.tex ends 'On note $\\varepsilon$ l'%' above the folio-408 marker; page_408.tex begins 'homomorphisme d'augmentation'",
    "marker", "high", None,
    "Page 408 really begins at '$\\varepsilon$ l'homomorphisme'; the marker splits the word l'homomorphisme. Exact edit in main.tex, both layers (diplomatic lines 10307-10309, current 10313-10315): replace 'On note $\\varepsilon$ l'%\\n" + M408 + "\\nhomomorphisme d'augmentation' by 'On note\\n" + M408 + "\\n$\\varepsilon$ l'homomorphisme d'augmentation' (old string once per layer; simulated: crops_406_410/sim_markers.py).")
add(408, "first line: 'ε l'homomorphisme d'augmentation : K˙(X) → H°(X,Z).'",
    "the struck Z of H°(X,Z) is underlined (constant sheaf; both scans; crops_406_410/w408_Z1.png)",
    r"\longrightarrow H^0(X,\mathbb Z)",
    "underline", "high",
    {"old": r"\longrightarrow H^0(X,\mathbb Z)", "new": r"\longrightarrow H^0(X,\underline{\mathbb Z})"},
    "The print underlines Z only as the coefficient sheaf of H^0 (pp. 408-409); the ring Z elsewhere (vers Z, Z-module, ⊗_Z, Z[x_i,...]) is not underlined. If the pending decision on underlined sheaf letters is meant to cover constant sheaves, this edit and the three like it (p. 408, p. 409, H^0(X,A) on p. 410) go with it.")
add(408, "'ε: K˙(X) → H^o(X,Z) l'augmentation de K˙(X)'",
    "Z underlined (both scans; crops_406_410/w408_Z2.png)",
    r"\varepsilon:K^{\bullet}(X)\to H^0(X,\mathbb Z)",
    "underline", "high",
    {"old": r"\to H^0(X,\mathbb Z)", "new": r"\to H^0(X,\underline{\mathbb Z})"},
    "As the entry above; independent of it (no common text).")
add(408, "'La quasi-compacité de X, et la commutation du K˙ aux sommes directes finies permet de se ramener ...'",
    "'permet' (both scans)",
    "finies permet de se ramener (printed reading kept)",
    "misprint_in_print", "medium", None,
    "Two subjects joined by 'et': the verb should be plural. The current layer already reads 'permettent'.",
    "finies permettent de se ramener")
add(408, "'et conserve l'hypothèse d'éxistence d'un faisceau ample'",
    "'d'éxistence' with an acute accent (both scans; crops_406_410/w408_exist.png)",
    "d'éxistence (printed reading kept)",
    "misprint_in_print", "high", None,
    "The current layer already reads 'd'existence'.",
    "d'existence")

# ---------------- page 409 ----------------
add(409, "Corollaire 6.2: 'R est un module de type fini sur R∩H^o(X,Z) (V 3.9.1)'",
    "Z underlined (both scans; crops_406_410/w409_Z.png); 'vers Z.' further down is not underlined (w409_Z2.png)",
    r"R\cap H^0(X,\mathbb Z)",
    "underline", "high",
    {"old": r"R\cap H^0(X,\mathbb Z)", "new": r"R\cap H^0(X,\underline{\mathbb Z})"},
    "As the H°(X,Z) entries of p. 408.")
add(409, "'... du λ-anneau engendré par les x_i soumis aux relations γ^j(x_i) = 0 pour'",
    "no comma after x_i (both scans; crops_406_410/w409_soumis.png)",
    "les $x_i$, soumis",
    "punctuation", "high",
    {"old": "les $x_i$, soumis", "new": "les $x_i$ soumis"},
    "Comma added by the TeX.")
add(409, "'j > r_i = ε(E_i) c'ést-à-dire Z[x_i,γ^j(x_i)]...'",
    "an accent mark over the e of 'est' (both scans; crops_406_410/w409_cest_zoom.png, w409_e_zoom.png, m409_e_zoom8.png): a small peaked mark, shorter than the typewriter's acute in 'engendré' or grave in 'discrète' (w409_engendre_e.png, w409_discrete_e.png)",
    "c'ést-à-dire (printed reading kept)",
    "misprint_in_print", "medium", None,
    "Typist's accent on 'est'. The TeX's é is a fair reading of the small mark; no edit for the diplomatic layer. The current layer already reads 'c'est-à-dire'.",
    "c'est-à-dire")
add(409, "same line: the index of Z[x_i,γ^j(x_i)]",
    "two ranges stacked under the bracket, '1≤i≤k' over '2≤j≤r_i', without a comma (both scans; crops_406_410/w409_sub.png)",
    r"]_{1\le i\le k,\,2\le j\le r_i}",
    "formula", "low",
    {"old": r"_{1\le i\le k,\,2\le j\le r_i}", "new": r"_{\substack{1\le i\le k\\2\le j\le r_i}}"},
    "The comma is the TeX's; \\substack (amsmath) stacks the ranges as printed.")
add(409, "'Pour n > kp(1+...+m), on voit tout de suite que Fil^nR = 0'",
    "three typed full stops on the baseline between the + signs (both scans; crops_406_410/w409_dots.png)",
    r"1+\cdots+m",
    "symbol", "medium",
    {"old": r"1+\cdots+m", "new": r"1+\ldots+m"},
    "\\cdots sets the dots at mid-height; same kind of fix as pp. 401-404 (findings_401_405).")

# ---------------- page 410 ----------------
add(410, "Corollaire 6.4: 'tel que ε(f_*(x')) ∈ H^o(X,A) soit inversible'",
    "A underlined (constant sheaf; both scans; crops_406_410/w410_A.png), while the ring A elsewhere ('soit A un anneau', ⊗_Z A, Id_A) is plain",
    r"\varepsilon(f_*(x'))\in H^0(X,A)",
    "underline", "high",
    {"old": "H^0(X,A)", "new": r"H^0(X,\underline{A})"},
    "As the H°(X,Z) entries of pp. 408-409.")

# ---------------- checks ----------------
ok = True
ctrl = [chr(c) for c in range(0, 32) if c not in (10,)]
for d in F:
    for k, v in d.items():
        s = json.dumps(v, ensure_ascii=False)
        if any(ch in str(v) for ch in ctrl):
            print("CONTROL CHARACTER in", d["page"], k); ok = False
    fx = d["fix"]
    if fx is None:
        continue
    t = (B / f"page_{d['page']}.tex").read_text(encoding="utf-8")
    n = t.count(fx["old"])
    marker_hit = "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]
    print(d["page"], n, "MARKER!" if marker_hit else "", repr(fx["old"]), "->", repr(fx["new"]))
    if n != 1 or marker_hit:
        ok = False
for i, a in enumerate(F):
    for b in F[i + 1:]:
        if a["page"] != b["page"] or a["fix"] is None or b["fix"] is None:
            continue
        t = (B / f"page_{a['page']}.tex").read_text(encoding="utf-8")
        ia = t.find(a["fix"]["old"]); ib = t.find(b["fix"]["old"])
        if ia < ib + len(b["fix"]["old"]) and ib < ia + len(a["fix"]["old"]):
            print("OVERLAP", a["page"], a["fix"]["old"], b["fix"]["old"]); ok = False
print("all unique, no overlaps, no control characters:", ok)
c = Counter((d["page"], d["kind"] == "misprint_in_print") for d in F)
for p in range(406, 411):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
if ok:
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(F, ensure_ascii=False, indent=1) + "\n")
    print("written", OUT, len(F))
