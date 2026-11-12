"""Build findings_411_415.json and check that every fix's 'old' occurs exactly once in its page file."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:/Users/user/Documents/sga_scan_check_20261105/run_5")
B = RUN / "b411_415"
OUT = RUN / "findings_411_415.json"


def F(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, confidence=confidence, fix=fix)
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


findings = [
    # ---------------- page 411 ----------------
    F(411, "top of the page: the display alpha_{m,n} (folio-411 marker)",
      "p. 411 begins with the display 'α_{m,n} : Λ_m ⟶ Λ_n', then 'engendrent les homomorphismes de faisceaux "
      "d'anneaux sur X' :'; p. 410 ends '... Les homomorphismes d'anneaux :'.",
      r"page_411.tex begins 'engendrent les homomorphismes'; the display '\[ \alpha_{m,n} : \La_m \longrightarrow "
      r"\La_n \]' (s5.tex lines 13867-13869) ends page_410.tex, above the folio-411 marker (line 13870).",
      "marker", "high", None,
      r"Page 411 really begins at s5.tex line 13867 '\['. Exact fix: python -I move_marker.py 5 411 \"\[\" --before "
      r"(the nearest '\[' above the marker; simulated in memory on both layers: the marker then stands between "
      r"'Les homomorphismes d'anneaux :' and '\['). Text not moved."),
    F(411, "formula (2.5), the tensor sign",
      "...,Λ_m) ⊗_{Λ_m} Λ_n ≃ R Hom_{Λ_n}(...): a plain ⊗ with nothing above it (the space above is clean), "
      "while (2.1)-(2.4) and (2.6) carry the hand-drawn double-struck L over ⊗.",
      r"\La_m) \otimes_{\La_m}^{\mathbb{L}} \La_n",
      "misprint_in_print", "high",
      {"old": r"\La_m) \otimes_{\La_m}^{\mathbb{L}} \La_n", "new": r"\La_m) \otimes_{\La_m} \La_n"},
      "The L was left out by hand in (2.5) only; the TeX silently supplies it. The derived tensor product is meant "
      "((2.5) is the dual of (2.2)), so the corrected reading keeps the L.",
      corrected=r"\La_m) \otimes_{\La_m}^{\mathbb{L}} \La_n"),
    F(411, "(2.6) and the paragraph below it; throughout Exposé XII",
      "The hand-drawn script ℋ: f'^∨_{ℋ_{m,U',X'}}, f'^∨_{ℋ_{n,U',X'}} (the same letter as at its definition on "
      "p. 408, 'son dual ℋ^∨_{n,U',X'} = RΓ_{X'}(Λ_{n,U',X'})^∨'), distinct from the typed H of 'Hom' in (2.5).",
      r"plain H: f'^\vee_{H_{m,U',X'}}, f'^\vee_{H_{n,U',X'}}",
      "font", "high", None,
      r"Convention of Exposé XII, reported once: s5.tex writes the print's script ℋ as plain H in all 45 'H_{' of "
      r"lines 13801-14567 (H_{n,U',X'}, H_{m,U',X'}, H_{n,U'}, H_{U',X'}(\ell)); 9 on these pages (p. 411: 4, "
      r"p. 412: 5). Examples: p. 411 (2.6) 'f'^\vee_{H_{m,U',X'}}', p. 412 (2.8) 'f'^\vee_{H_{n,U',X'}}', "
      r"p. 412 'f'^\vee_{H_{U',X'}(\ell)}'. One pass over those lines: 'H_{' -> '\mathcal{H}_{' (the file writes "
      r"\mathcal{F} for the print's script F, p. 412)."),
    # ---------------- page 412 ----------------
    F(412, "top of the page: 'à l'' (folio-412 marker)",
      "p. 412 begins 'à l'aide des morphismes α_{m,n} (resp. ...'; p. 411 ends '... ,f'^∨_{ℋ_{m,U',X'}})'.",
      r"page_411.tex ends with 'à l'%' (end of s5.tex line 13891); the folio-412 marker (line 13892) splits "
      r"'à l'aide', and page_412.tex begins 'aide des morphismes'.",
      "marker", "high", None,
      r"Page 412 really begins at 'à l'' at the end of s5.tex line 13891. Exact fix: python -I move_marker.py 5 412 "
      r"\"à l'\" --before (simulated in memory on both layers: the marker then stands between "
      r"'$f'^\vee_{H_{m,U',X'}}$) ' and 'à l'%'; 'à l'%' and 'aide' can then be rejoined as 'à l'aide'). "
      r"Text not moved."),
    F(412, "heading of no. 3",
      "3. L'invariant local de Nielsen-Wecken (cf. [1] ). Supposons ... (title underlined; a full stop after "
      "the parenthesis).",
      r"\section*{3. L'invariant local de Nielsen-Wecken (cf. [1])}",
      "punctuation", "high",
      {"old": r"Nielsen-Wecken (cf. [1])}", "new": r"Nielsen-Wecken (cf. [1]).}"},
      "The TeX drops the full stop that ends the run-in title."),
    F(412, "'De même les éléments ...'",
      "Tr^*_{Λ_n}( RΓ_{X'}(f'_{n,X'})) , n ≥ 1: the subscript of f' is 'n,X'' without Λ.",
      r"\Tr^*_{\La_n}(\R\Gamma_{X'}(f'_{\La_{n,X'}}))",
      "misprint_in_print", "high",
      {"old": r"(f'_{\La_{n,X'}}))$ , $n", "new": r"(f'_{n,X'}))$ , $n"},
      "The print drops the Λ (as written in (2.7): f'_{Λ_{n,X'}}); the TeX silently corrects it.",
      corrected=r"(f'_{\La_{n,X'}}))$ , $n"),
    # ---------------- page 413 ----------------
    F(413, r"top of the page: '\begin{align*}' (folio-413 marker)",
      "p. 413 begins with the display 'p : X' ⟶ X = X'/G pour la projection canonique, ...'; p. 412 ends "
      "'On va utiliser dans la suite les notations suivantes :'.",
      r"page_412.tex ends with '\begin{align*}' (s5.tex line 13919); the folio-413 marker (line 13920) stands inside "
      r"the align* environment, so page_413.tex begins 'p &: X' ...'.",
      "marker", "high", None,
      r"Only the environment opener lies on the wrong side; no printed text is misplaced. Page 413 really begins at "
      r"s5.tex line 13919. Exact fix: python -I move_marker.py 5 413 \"\begin{align*}\" --before (simulated in "
      r"memory on both layers: the marker then stands between 'notations suivantes :' and '\begin{align*}')."),
    F(413, "first display, third line",
      "U = X - Y (nothing after it; the line above ends with ' ,').",
      r"U &= X - Y \quad .",
      "punctuation", "high",
      {"old": r"U &= X - Y \quad .", "new": r"U &= X - Y"},
      "Full stop added by the TeX at the end of the display."),
    # ---------------- page 414 ----------------
    F(414, "top of the page: formula (3.1) (folio-414 marker)",
      "p. 414 begins with formula (3.1) 'NW^{G,φ}_f(x)(g) = { 1 s'il existe ...'; p. 413 ends 'à valeurs "
      "entières,caractérisée par les relations suivantes :'.",
      r"'\begin{equation}\tag{3.1}' and '\mathrm{NW}_{f}^{G,\varphi}(x)(g) = \begin{cases} 1 &' (s5.tex lines "
      r"13942-13943) end page_413.tex; the folio-414 marker (line 13944) splits the cases environment.",
      "marker", "high", None,
      r"Page 414 really begins at s5.tex line 13942 '\begin{equation}\tag{3.1}'. Exact fix: python -I "
      r"move_marker.py 5 414 \"\begin{equation}\tag{3.1}\" --before (simulated in memory on both layers: the marker "
      r"then stands between 'les relations suivantes :' and '\begin{equation}'). Text not moved."),
    F(414, "(3.1), second line of the cases",
      "et p(x') = x (nothing after it).",
      r"\text{et } p(x') = x \quad ;",
      "punctuation", "high",
      {"old": "p(x') = x \\quad ; \\\\", "new": "p(x') = x \\\\"},
      "Semicolon added by the TeX."),
    F(414, "heading of no. 4",
      "4. Supposons X' lisse sur k ...: the number '4.' alone, no title.",
      r"\section*{4. Généralités sur les termes locaux}",
      "extra", "high",
      {"old": r"\section*{4. Généralités sur les termes locaux}", "new": r"\section*{4.}"},
      r"The title 'Généralités sur les termes locaux' is not in the print. '\section*{4.}' as the file's "
      r"'\section*{2.}' (p. 410)."),
    F(414, "(4.1), summation index",
      "Σ_{x'∈X'^{g^{-1}f}_x}: no prime on the f of the index (the space after it is clean); (4.3) defines "
      "X'^{g^{-1}f'}_x.",
      r"\sum_{x' \in {X'_x}^{g^{-1}f'}}",
      "misprint_in_print", "high",
      {"old": r"\in {X'_x}^{g^{-1}f'}}", "new": r"\in {X'_x}^{g^{-1}f}}"},
      "The TeX silently corrects the print's missing prime.",
      corrected=r"\in {X'_x}^{g^{-1}f'}}"),
    F(414, "(4.2)",
      "c^φ(g) = Card G^φ_g (capital C).",
      r"\card G_g^\varphi (\card is \operatorname{card})",
      "word", "high",
      {"old": r"\card G_g^\varphi", "new": r"\operatorname{Card} G_g^\varphi"},
      r"The file writes \operatorname{Card} elsewhere."),
    F(414, "(4.2), set-builder separator",
      "{x ∈ G / φ(x)gx^{-1} = g}",
      r"\{ x \in G \mid \varphi(x)gx^{-1} = g \}",
      "symbol", "medium",
      {"old": r"x \in G \mid \varphi(x)", "new": r"x \in G / \varphi(x)"},
      r"The print separates with a slash, here and in (4.3); the TeX writes \mid. Medium: the slash may be a "
      r"typewriter stand-in for a bar, though it is not among the listed substitutes."),
    F(414, "(4.3), set-builder separator",
      "{x'∈ X' / p(x') = x , (g^{-1}f')(x') = x'}",
      r"\{ x' \in X' \mid p(x') = x",
      "symbol", "medium",
      {"old": r"x' \in X' \mid p(x')", "new": r"x' \in X' / p(x')"},
      "As (4.2)."),
    F(414, "last line",
      "Par composition, avec les inclusions canoniques",
      "Par composition avec les inclusions canoniques",
      "punctuation", "high",
      {"old": "Par composition avec", "new": "Par composition, avec"},
      "Comma after 'composition' (typed without a space before 'avec')."),
    # ---------------- page 415 ----------------
    F(415, "top of the page: the display Q ↪ Q_ℓ (folio-415 marker)",
      "p. 415 begins with the display 'Q ↪ Q_ℓ', then 'la fonction S_x(f',f,G,φ) engendre ...'; p. 414 ends "
      "'Par composition, avec les inclusions canoniques'.",
      r"the display '\[ \bQ \hookrightarrow \bQ_\ell \]' (s5.tex lines 13977-13979) ends page_414.tex, above the "
      r"folio-415 marker (line 13980); page_415.tex begins 'la'.",
      "marker", "high", None,
      r"Page 415 really begins at s5.tex line 13977 '\['. Exact fix: python -I move_marker.py 5 415 \"\[\" --before "
      r"(the nearest '\[' above the marker; simulated in memory on both layers: the marker then stands between "
      r"'inclusions canoniques' and '\['). Text not moved."),
    F(415, "label of Proposition 4.6",
      "Proposition 4.6  Soient R ... (no full stop after 4.6; 'Conjecture 4.5.' above has one).",
      r"\textbf{Proposition 4.6.}",
      "punctuation", "high",
      {"old": r"\textbf{Proposition 4.6.}", "new": r"\textbf{Proposition 4.6}"},
      "Full stop added by the TeX."),
    F(415, "Proposition 4.6, 'induisent l'... sur k'",
      "induisent l'indentité sur k",
      r"induisent l'identité sur $k$",
      "misprint_in_print", "high",
      {"old": "l'identité", "new": "l'indentité"},
      "Typing error of the print ('indentité'); the TeX silently corrects it.",
      corrected="l'identité"),
]

for f in findings:
    f["note"] = f["note"].replace('\\"', '"')

ok = True
for f in findings:
    fx = f["fix"]
    if fx is None:
        continue
    t = (B / f"page_{f['page']}.tex").read_text(encoding="utf-8")
    n = t.count(fx["old"])
    mk = "%%%%%%%%%%" in fx["old"]
    print(f["page"], f["kind"], n, "MARKER!" if mk else "", repr(fx["old"]))
    if n != 1 or mk:
        ok = False
print("all unique:", ok)
if ok:
    OUT.write_text(json.dumps(findings, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("written", OUT, len(findings))
