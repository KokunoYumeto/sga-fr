"""Build findings_301_305.json and check that every fix's old string occurs exactly once on its page.
Line breaks inside old/new are written as the placeholder NL and turned into real newlines."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
BATCH = HERE.parent / "b301_305"
OUT = HERE.parent / "findings_301_305.json"
NL = "⏎"


def fx(old, new):
    return {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}


F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 301 ----------------
add(301, "page start: end of the sentence begun on p. 300 ('qui par suite prend ses valeurs dans')",
    "H(K[X_1,...,X_n]) d'après (1.3.ii)). : the page's first line, in the running text at the left margin; "
    "p. 300 ends '... le morphisme u^n_H, qui par suite prend ses valeurs dans' (both scans). Neither page has "
    "H(K[T_1,...,T_n])^{S_n} ≃ here.",
    r"\[ H(K[T_1,\ldots,T_n])^{\mathfrak S_n} \simeq H(K[X_1,\ldots,X_n]) \] d'après (1.3.ii)).",
    "extra", "high",
    fx(r"\[" + NL + r"  H(K[T_1,\ldots,T_n])^{\mathfrak S_n}" + NL + r"  \simeq H(K[X_1,\ldots,X_n])" + NL + r"\]" + NL + "d'après",
       r"\(H(K[X_1,\ldots,X_n])\) d'après"),
    "The TeX interpolates 'H(K[T_1,…,T_n])^{S_n} ≃' and turns the end of the sentence into a display; the print reads "
    "'prend ses valeurs dans H(K[X_1,…,X_n]) d'après (1.3.ii)).' (H(K[X_1,…,X_n]) identified with the invariants as in 1.5). "
    "Not a misprint: the same fix applies to the corrected layer. The folio-301 marker itself is right.")

add(301, "after 'd'après (1.3.ii)).'",
    "Remarquons enfin que si H = Ĝ, ... begins a new, indented paragraph (both scans)",
    "d'après (1.3.ii)).\\nRemarquons enfin (same paragraph)",
    "other", "high",
    fx("(1.3.ii))." + NL + "Remarquons", "(1.3.ii))." + NL + NL + "Remarquons"),
    "Missing paragraph break. Independent of the entry above (the two old strings do not overlap).")

add(301, "Théorème 1.6, line 3",
    "son image est le sous groupe de H(K[X]): 'sous groupe' without hyphen, inside the underlined word group "
    "(both scans); the typist writes 'sous-groupe' on pp. 299 and 300",
    "son image est le sous-groupe de",
    "misprint_in_print", "high",
    fx("sous-groupe", "sous groupe"),
    "The TeX silently supplies the hyphen; the diplomatic layer should keep the printed 'sous groupe'.",
    corrected="sous-groupe")

add(301, "Théorème 1.6, index of Hom (convention of the Exposé V transcription, reported once)",
    "Hom with the index 'Ab fil', 'Ab' and 'fil' each underlined (both scans)",
    r"\Hom_{\Abfil}(\Ghat_K,H), with \providecommand{\Abfil}{\mathrm{Ab\,fil}} (plain)",
    "underline", "high", None,
    "The print underlines the name of the category of filtered abelian groups wherever it occurs, inside statements "
    "and outside them; the macro \\Abfil prints it plain. Three examples: p. 299 (1.3) 'à valeurs dans Ab fil' "
    "underlined (and 'la catégorie Ab.fil.', printed with stops); p. 301 Théorème 1.6 'Hom_{Ab fil}(Ĝ_K,H)'; "
    "p. 306 Lemme 1.9 'H : 𝒞_o → Ab fil' and the display 'Hom_{Ab fil}(Ĝ,H∘g) → Hom_{Ab fil}(Ĝ∘i,H)' "
    "(witness). Global fix, both layers: replace '\\providecommand{\\Abfil}{\\mathrm{Ab\\,fil}}' by "
    "'\\providecommand{\\Abfil}{\\underline{\\mathrm{Ab}}\\,\\underline{\\mathrm{fil}}}' (14 uses, all in "
    "Exposé V §1, folios 299-311); p. 299's 'Ab.fil.' needs its own fix for the stops.")

add(301, "proof of injectivity: 'est nul sur φ = ...'",
    "φ = 1+X_1t + ... + X_nt^n + .... Le diagramme commutatif : , all on one line of the running text at the "
    "left margin (both scans)",
    r"est nul sur \[ \varphi=1+X_1t+\cdots+X_nt^n+\cdots . \] Le diagramme commutatif",
    "other", "medium",
    fx(r"est nul sur" + NL + r"\[" + NL + r"  \varphi=1+X_1t+\cdots+X_nt^n+\cdots ." + NL + r"\]" + NL,
       r"est nul sur \(\varphi=1+X_1t+\cdots+X_nt^n+\cdots\). "),
    "The print sets the series inline, the sentence 'Le diagramme commutatif :' following on the same line; "
    "the TeX makes it a display (same kind of fix as pp. 21, 34, 42, 80, 105, 277). Independent of the colon entry below.")

add(301, "'Le diagramme commutatif' before (1.6.1)",
    "Le diagramme commutatif : (colon; both scans)",
    "Le diagramme commutatif (no colon) followed by the diagram",
    "punctuation", "high",
    fx("Le diagramme commutatif" + NL + r"\[", "Le diagramme commutatif~:" + NL + r"\["),
    "Missing colon.")

add(301, "diagram (1.6.1), lower horizontal arrow",
    "u^n_H stands above the lower arrow H(K[X]) → H(K[X_1,...,X_n]) (both scans)",
    r"""\arrow[r,"u_H^n"'] (label set below the arrow)""",
    "formula", "medium",
    fx(r"""\arrow[r,"u_H^n"']""", r"""\arrow[r,"u_H^n"]"""),
    "Label on the wrong side of the arrow; the other three labels stand as printed (u^n_Ĝ above, Φ left, Φ right).")

add(301, "after 'Φ(1+X_1t+...+X_nt^n) = 0 .'",
    "Or φ ≡ 1+X_1t+...+X_nt^n mod. F^{n+1}Ĝ ; ... begins a new, indented paragraph (both scans)",
    r"...=0\). Or \(\varphi\equiv ... (same paragraph)",
    "other", "high",
    fx(r"=0\). Or \(\varphi", r"=0\)." + NL + NL + r"Or \(\varphi"),
    "Missing paragraph break.")

# ---------------- page 302 ----------------
add(302, "page start",
    "p. 302 begins 'θ = Φ(1+Xt) ; montrons que θ vérifie les conditions i) et ii).'; p. 301 ends "
    "'Soit maintenant Φ un élément quelconque de Hom(Ĝ,H), et soit' (both scans)",
    r"'\(\theta=\Phi(1+Xt)\)~;' ends the last line of page_301.tex, above the folio-302 marker; page_302.tex begins 'montrons que'",
    "marker", "high", None,
    "The folio-302 marker stands one formula late. Page 302 really begins at '\\(\\theta=\\Phi(1+Xt)\\)~; montrons que'. "
    "Exact fix in main.tex (both layers): replace 'et soit \\(\\theta=\\Phi(1+Xt)\\)~;\\n%%%%%%%%%%  scan idx 315  |  folio 302  "
    "%%%%%%%%%%\\nmontrons que' by 'et soit\\n%%%%%%%%%%  scan idx 315  |  folio 302  %%%%%%%%%%\\n\\(\\theta=\\Phi(1+Xt)\\)~; "
    "montrons que' (same paragraph; the comment line keeps the space after 'soit').")

add(302, "after 'tel que θ = Φ(1+Xt).'",
    "On détermine d'abord la valeur de Φ ... begins a new, indented paragraph (both scans)",
    r"tel que \(\theta=\Phi(1+Xt)\).\nOn détermine (same paragraph)",
    "other", "high",
    fx(r"\Phi(1+Xt)\)." + NL + "On détermine", r"\Phi(1+Xt)\)." + NL + NL + "On détermine"),
    "Missing paragraph break.")

add(302, "diagram (1.6.2), right vertical arrow",
    "σ'_n stands to the left of the right vertical arrow (both scans)",
    r"""\arrow[d,"\sigma'_n"] (label set to the right)""",
    "formula", "low",
    fx(r"""\arrow[d,"\sigma'_n"]""", r"""\arrow[d,"\sigma'_n"']"""),
    "Label on the wrong side of the arrow (the σ is hand-drawn, the label clearly left of the shaft).")

add(302, "diagram (1.6.2), lower horizontal arrow",
    "f'_n stands above the lower arrow K[T_1,...,T_n] → K[T_1,...,T_n] (both scans)",
    r"""\arrow[r,"f'_n"'] (label set below the arrow)""",
    "formula", "medium",
    fx(r"""\arrow[r,"f'_n"']""", r"""\arrow[r,"f'_n"]"""),
    "Label on the wrong side of the arrow, as the lower label of (1.6.1) on p. 301; f_n above and σ̃_n left stand as printed.")

# ---------------- page 303 ----------------
add(303, "after '(en se plaçant ... grâce aux identifications 1.4).'",
    "Compte tenu de 1.6.ii), ... begins a new, indented paragraph (both scans)",
    "identifications 1.4). Compte tenu de 1.6.ii), (same paragraph)",
    "other", "high",
    fx("identifications 1.4). Compte tenu", "identifications 1.4)." + NL + NL + "Compte tenu"),
    "Missing paragraph break.")

add(303, "end of the paragraph 'Compte tenu de 1.6.ii) ...'",
    "... on posera donc / Φ(φ) = ψ . : the formula wraps to the next text line at the left margin, at ordinary "
    "line spacing, and ends the paragraph (both scans)",
    r"on posera donc \[ \Phi(\varphi)=\psi . \]",
    "other", "medium",
    fx("on posera donc" + NL + r"\[" + NL + r"  \Phi(\varphi)=\psi ." + NL + r"\]",
       r"on posera donc \(\Phi(\varphi)=\psi\)."),
    "The print sets the formula inline at the end of the sentence; the TeX makes it a display (as p. 301 above).")

add(303, "'On a donc défini ainsi un système d'application Φ_A'",
    "un système d'application Φ_A: Ĝ(A) → H(A) ; pour vérifier qu'elles constituent ... (both scans)",
    "un système d'application",
    "misprint_in_print", "low", None,
    "The pronoun 'elles' refers to the maps: the typist dropped the plural s. The TeX keeps the printed reading; "
    "the corrected layer also still reads 'application'.",
    corrected="un système d'applications")

add(303, "diagram at the foot of the page, lower horizontal arrow",
    "H(h) stands above the lower arrow H(A) → H(A') (both scans)",
    r"""\arrow[r,"H(h)"'] (label set below the arrow)""",
    "formula", "medium",
    fx(r"""\arrow[r,"H(h)"']""", r"""\arrow[r,"H(h)"]"""),
    "Label on the wrong side of the arrow; Ĝ(h) above, Φ_A left and Φ_{A'} right stand as printed.")

# ---------------- page 304 ----------------
add(304, "display after 'd'où :', second member",
    "H(h)oH(f_χ(ψ)): the closing parenthesis of H( stands after (ψ); no parenthesis between f_χ and (ψ) (both scans)",
    r"H(h)\circ H(f_\chi)(\psi)",
    "misprint_in_print", "high",
    fx(r"H(h)\circ H(f_\chi)(\psi)", r"H(h)\circ H(f_\chi(\psi))"),
    "H(f_χ) is applied to ψ, as in the definition Φ(χ) = H(f_χ)(ψ) on p. 303. The TeX silently corrects; "
    "the diplomatic layer should keep the printed reading. Independent of the next entry.",
    corrected=r"H(h)\circ H(f_\chi)(\psi)")

add(304, "display after 'd'où :', last member",
    "= Φ_{A'}(Ĝ(h)(χ). : one closing parenthesis only (both scans)",
    r"=\Phi_{A'}(\Ghat(h)(\chi)).",
    "misprint_in_print", "high",
    fx(r"\Phi_{A'}(\Ghat(h)(\chi)).", r"\Phi_{A'}(\Ghat(h)(\chi)."),
    "The print leaves the parenthesis after Φ_{A'} unclosed; the TeX silently closes it.",
    corrected=r"\Phi_{A'}(\Ghat(h)(\chi)).")

add(304, "after the display ending 'Φ_{A'}(Ĝ(h)(χ).'",
    "Il reste donc à montrer que le morphisme de foncteurs ... begins a new, indented paragraph (both scans)",
    r"\]\nIl reste donc (same paragraph as the display)",
    "other", "high",
    fx(r"\]" + NL + "Il reste donc", r"\]" + NL + NL + "Il reste donc"),
    "Missing paragraph break.")

add(304, "diagram of the additivity proof, vertical arrow",
    "the vertical arrow K[X_1,...,X_{2n}] → (K[T_1,...,T_{2n}])^{S_n×S_n} has a hook at its tail (top), curling "
    "to the right: an inclusion arrow (both scans)",
    r"\arrow[d] (plain arrow)",
    "symbol", "high",
    fx(r"\arrow[d] && A", r"\arrow[d,hook] && A"),
    "The file writes hooked arrows as \\arrow[r,hook]; the text calls this map the embedding into the ring of invariants (p. 305).")

add(304, "diagram of the additivity proof, diagonal arrow",
    "f'_χ stands on the upper-left side of the diagonal arrow to A (both scans)",
    r"""\arrow[urr,"f'_\chi"'] (label set on the lower-right side)""",
    "formula", "medium",
    fx(r"""\arrow[urr,"f'_\chi"']""", r"""\arrow[urr,"f'_\chi"]"""),
    "Label on the wrong side of the arrow; f_χ above the horizontal arrow stands as printed. Independent of the comma entry below.")

add(304, "after the diagram of the additivity proof",
    "a comma after the diagram, at the level of its bottom row, right (both scans)",
    "no punctuation after the diagram",
    "punctuation", "high",
    fx("&&" + NL + r"\end{tikzcd}", "&& ," + NL + r"\end{tikzcd}"),
    "Punctuation printed after a diagram; set in the last cell, as on pp. 7 and 59.")

# ---------------- page 305 ----------------
add(305, "page start",
    "p. 305 begins 'de façon que le premier facteur permute T_1,...,T_n'; p. 304 ends '... opère sur K[T_1,...,T_{2n}]' (both scans)",
    r"'de façon que le' ends the last line of page_304.tex, above the folio-305 marker; page_305.tex begins 'premier facteur'",
    "marker", "high", None,
    "The folio-305 marker stands four words late. Page 305 really begins at 'de façon que le premier facteur'. "
    "Exact fix in main.tex (both layers): replace '\\(K[T_1,\\ldots,T_{2n}]\\) de façon que le\\n%%%%%%%%%%  scan idx 318  |  "
    "folio 305  %%%%%%%%%%\\npremier facteur' by '\\(K[T_1,\\ldots,T_{2n}]\\)\\n%%%%%%%%%%  scan idx 318  |  folio 305  "
    "%%%%%%%%%%\\nde façon que le premier facteur'.")

add(305, "first paragraph, 'en envoyant X_j sur le j-ième fonction symétrique'",
    "sur le j-ième fonction symétrique des T_i (both scans)",
    r"sur le \(j\)-ième fonction symétrique",
    "misprint_in_print", "high", None,
    "Gender slip of the typist ('fonction' is feminine). The TeX keeps the printed reading; the corrected layer already reads 'la'.",
    corrected=r"sur la \(j\)-ième fonction symétrique")

add(305, "page end",
    "p. 305 ends 'ils sont déterminés par leur valeur pour l'élément' (both scans); p. 306 begins "
    "'(1+X^{(j)}t)_{j=1,..,k} de (Ĝ(K[(X^{(j)})_j]))^k; un élément θ de H(K[(X^{(j)})_j]) déter-' (witness)",
    r"the last TeX line of page_305.tex, '\((1+X^{(j)}t)_{j=1,\ldots,k}\) de \(\bigl(\Ghat(K[(X^{(j)})_j])\bigr)^k\)~; un', stands above the folio-306 marker",
    "marker", "high", None,
    "The folio-306 marker stands one TeX line late (not moved by the script). Exact fix in main.tex (both layers): replace "
    "'pour l'élément\\n\\((1+X^{(j)}t)_{j=1,\\ldots,k}\\) de \\(\\bigl(\\Ghat(K[(X^{(j)})_j])\\bigr)^k\\)~; un\\n%%%%%%%%%%  "
    "scan idx 319  |  folio 306  %%%%%%%%%%\\n' by 'pour l'élément\\n%%%%%%%%%%  scan idx 319  |  folio 306  %%%%%%%%%%\\n"
    "\\((1+X^{(j)}t)_{j=1,\\ldots,k}\\) de \\(\\bigl(\\Ghat(K[(X^{(j)})_j])\\bigr)^k\\)~; un\\n'. The moved line was "
    "checked here against the witness of p. 306 and agrees with the print.")

# ---------------- checks ----------------
ok = True
for d in F:
    if d["fix"] is None:
        continue
    t = (BATCH / f"page_{d['page']}.tex").read_text(encoding="utf-8")
    n = t.count(d["fix"]["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE", d["page"], n, repr(d["fix"]["old"]))
    if "%%%%%%%%%%" in d["fix"]["old"] or "%%%%%%%%%%" in d["fix"]["new"]:
        ok = False
        print("MARKER IN FIX", d["page"])
# fixes on one page must not overlap
for p in range(301, 306):
    t = (BATCH / f"page_{p}.tex").read_text(encoding="utf-8")
    spans = []
    for d in F:
        if d["page"] == p and d["fix"]:
            i = t.find(d["fix"]["old"])
            spans.append((i, i + len(d["fix"]["old"]), d["where"]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            print("OVERLAP", p, a[2], "|", b[2])
    # apply all fixes in sequence to confirm they compose
    s = t
    for d in F:
        if d["page"] == p and d["fix"]:
            assert s.count(d["fix"]["old"]) == 1, (p, d["fix"]["old"])
            s = s.replace(d["fix"]["old"], d["fix"]["new"])
counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0])
    c[1 if d["kind"] == "misprint_in_print" else 0] += 1
print("all unique" if ok else "PROBLEMS", counts, len(F))
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(OUT)
