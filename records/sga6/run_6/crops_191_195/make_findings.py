r"""Build findings_191_195.json; check that every fix's old occurs exactly once in its page file.
usage: python -I make_findings.py"""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b191_195"
NL = "⏎"  # placeholder for a line break in old/new


def fx(old, new):
    return {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}


F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


FN = (r"Condition réalisée, d'après (Tohoku 3.6.5), si l'espace sous-jacent à $S$ est noethérien et de "
      r"dimension de Krull $\leq N$.")

# ---------------- p. 191
add(191, "display after 'Le composé'", "E ⟶ RQE ⟶ E with the R double-underlined (both scans)",
    r"E\longrightarrow RQE\longrightarrow E (plain R)", "font", "high",
    fx(r"E\longrightarrow RQE\longrightarrow E", r"E\longrightarrow \mathbb RQE\longrightarrow E"),
    r"Double-struck derived-functor R written plain; \mathbb R is the file's form (main.tex lines 3986, 4170; "
    r"applied on pp. 167, 175-176).")
add(191, "Proposition 3.7, display and footnote (1)",
    "the call (1) stands in the display, after the formula and before its full stop: 'H^i(U,F) = 0 pour i > N  (1)  .' "
    "(both scans)",
    r"\footnote attached to 'ouvert quasi-compact $U$ de $S$,' before the display", "other", "medium",
    fx(r"$S$,\footnote{" + FN + r"}⏎\[⏎ H^i(U,F)=0\quad\text{pour }i>N.⏎\]",
       r"$S$,⏎\[⏎ H^i(U,F)=0\quad\text{pour }i>N\qquad\text{\footnotemark}\ .⏎\]⏎\footnotetext{" + FN + "}"),
    r"Position of the footnote call only; the footnote text is unchanged. Same form as the applied p. 61 fix "
    r"(\text{\footnotemark} in the display, \footnotetext after it).")
add(191, "Preuve de a), first line", "Q = Γ̃_S: the hand-drawn tilde stands over Γ only, S is its subscript (both scans)",
    r"Q=\widetilde{\Gamma_S} (tilde over Γ_S)", "formula", "low",
    fx(r"Q=\widetilde{\Gamma_S}", r"Q=\widetilde{\Gamma}_S"),
    "Low: extent of a hand-drawn tilde. The same TeX formula stands on p. 190 (main.tex line 4500).")
add(191, "'Preuve de a).'", "'Preuve de' underlined, 'a).' plain (both scans)", r"\emph{Preuve de a).}",
    "underline", "high", fx(r"\emph{Preuve de a).}", r"\emph{Preuve de} a)."),
    r"As \emph{Preuve de (5.8).} on p. 136 and 'Preuve de 2.2.7.' on p. 172.")
add(191, "Preuve de a), 'une résolution finie droite E˙ de longueur N'",
    "E˙: raised dot of a complex (both scans; N' on the same page has the vertical prime)", r"$E'$ (prime)",
    "symbol", "high", fx(r"droite $E'$ de", r"droite $E^\bullet$ de"),
    r"The dot is read as a prime; the file writes the raised dot ^\bullet (E^\bullet, F^\bullet in Appendix II). "
    "Same misreading as C'(E) four times on p. 192.")
add(191, "last line, '(On pourra alors prendre a = b + N). Soit (U_i)'",
    "'Soit (U_i) un recouvrement ...' runs on in the same line: no new paragraph", r"blank line before 'Soit $(U_i)$'",
    "other", "medium", fx(r"$a=b+N$).⏎⏎Soit", r"$a=b+N$). Soit"),
    "Paragraph break added by the TeX.")

# ---------------- p. 192
for where, old, new in [
        ("line 2, 'considérons la résolution C˙(E)'", r"la résolution $C'(E)$", r"la résolution $C^\bullet(E)$"),
        ("1°), 'Alors les composantes de C˙(E)'", r"les composantes de $C'(E)$", r"les composantes de $C^\bullet(E)$"),
        ("'Comme C˙(E) est de longueur N''", r"Comme $C'(E)$", r"Comme $C^\bullet(E)$"),
        ("2°), 'Les composantes de C˙(E)'", r"Les composantes de $C'(E)$", r"Les composantes de $C^\bullet(E)$")]:
    add(192, where, "C˙(E): raised dot (both scans)", r"$C'(E)$ (prime)", "symbol", "high", fx(old, new),
        "Raised dot read as a prime, as E˙ on p. 191. Four separate entries on this page.")
add(192, "1°) 'S est séparé.'", "'séparé' underlined (both scans)", "plain 'séparé'", "underline", "high",
    fx(r"$S$ est séparé.", r"$S$ est \emph{séparé}."),
    r"Emphasis in the proof, not a statement of the Exposé II pattern; the file writes underlines \emph.")
add(192, "2°) 'S est noethérien.'", "'noethérien' underlined (both scans)", "plain 'noethérien'", "underline", "high",
    fx(r"$S$ est noethérien.", r"$S$ est \emph{noethérien}."), "As 1°).")
add(192, "2°), 'ouvert quasi-compact et séparé.'", "'séparé' underlined (both scans)", "plain 'séparé'", "underline",
    "high", fx(r"et séparé. Comme", r"et \emph{séparé}. Comme"), "As 1°).")
add(192, "first display (two lines in the print, '... puisque f^*E est acyclique.')",
    "R(Qf_*) f^*E ≃ RQ Rf_* f^*E ≃ RQ f_*f^*E: all four R double-underlined; both signs a tilde over a rule, "
    "without arrowhead (both scans)",
    r"plain R; \xrightarrow{\sim}", "formula", "high",
    fx(r"R(Qf_*)f^*E\xrightarrow{\sim} RQ\,Rf_*f^*E\xrightarrow{\sim} RQ\,f_*f^*E,",
       r"\mathbb R(Qf_*)f^*E\simeq \mathbb RQ\,\mathbb Rf_*f^*E\simeq \mathbb RQ\,f_*f^*E,"),
    r"R's and signs interleave, so one edit: \mathbb R as on p. 191; \simeq for the headless sign as applied on "
    "pp. 146, 150, 153.")
add(192, "second display ('... puisque f est affine.')",
    "R(Qf_*) f^*E ≃ R(f_*Q) f^*E ≃ f_* RQ f^*E: three R double-underlined, two headless signs (both scans)",
    r"plain R; \xrightarrow{\sim}", "formula", "high",
    fx(r"R(Qf_*)f^*E\xrightarrow{\sim} R(f_*Q)f^*E\xrightarrow{\sim} f_*RQf^*E,",
       r"\mathbb R(Qf_*)f^*E\simeq \mathbb R(f_*Q)f^*E\simeq f_*\mathbb RQf^*E,"),
    "As the first display.")
add(192, "third display ('pour tout n ≥ 0')", "R^nQ (f_*f^*E) ≃ f_* R^nQ(f^*E): headless sign; R^n plain (both scans)",
    r"\xrightarrow{\sim}", "symbol", "high",
    fx(r"R^nQ(f_*f^*E)\xrightarrow{\sim}", r"R^nQ(f_*f^*E)\simeq"), r"\simeq as above; the R^n stay plain.")

# ---------------- p. 193
add(193, "head of the page: display (*)",
    "p. 193 begins with the display '(*) R(Qf_*) f^*E ≃ ...'; p. 192 ends with 'Comme dans le cas 1°), on a'",
    r"the marker stands inside the display, after '\begin{equation}\tag{*}' (last line of page_192.tex)",
    "marker", "medium", None,
    r"Page 193 really begins with the (*) display, whose tag (*) is printed at its head. Move the folio-193 marker "
    r"above it: python -I move_marker.py 6 193 '\begin{equation}' --before (single quotes; dry run and simulation "
    r"on both layers: '... Comme dans le cas 1°), on a' / marker / '\begin{equation}\tag{*}' / display). "
    "A display at the top of a page, which the 10 Nov script did not move.")
add(193, "display (*)",
    "R(Qf_*) f^*E ≃ RQ f_*f^*E ≃ R(f_*Q) f^*E: three R double-underlined, two headless signs (both scans)",
    r"plain R; \xrightarrow{\sim}", "formula", "high",
    fx(r"R(Qf_*)f^*E\xrightarrow{\sim} RQ\,f_*f^*E\xrightarrow{\sim} R(f_*Q)f^*E.",
       r"\mathbb R(Qf_*)f^*E\simeq \mathbb RQ\,f_*f^*E\simeq \mathbb R(f_*Q)f^*E."),
    "As the displays of p. 192. Independent of the marker move.")
add(193, "line 3, 'par Rf_* : D^+(U) ⟶ D^+(S)'", "R double-underlined (both scans)", r"$Rf_*$", "font", "high",
    fx(r"par $Rf_*:", r"par $\mathbb Rf_*:"), r"As p. 191.")
add(193, "display after 'Par suite, on a'",
    "R(f_*Q) f^*E ≃ Rf_* RQ f^*E: three R double-underlined, headless sign (both scans)",
    r"plain R; \xrightarrow{\sim}", "formula", "high",
    fx(r"R(f_*Q)f^*E\xrightarrow{\sim} Rf_*RQf^*E.", r"\mathbb R(f_*Q)f^*E\simeq \mathbb Rf_*\mathbb RQf^*E."),
    "As the displays of p. 192.")
add(193, "spectral sequence display", "E_2^{pq} = R^pf_* R^qQ f^*E ⟹ R^*(f_*Q) f^*E: no parentheses round f^*E (both scans)",
    r"R^qQ(f^*E)", "extra", "high", fx(r"R^qQ(f^*E)\Longrightarrow", r"R^qQf^*E\Longrightarrow"),
    "Parentheses added by the TeX; the R's of this display are plain in the print, as in the TeX.")
add(193, "'l'ensemble des intersections U_{i_o} ∩ ... ∩ U_{i_p}'", "typed baseline stops '...' between the two ∩",
    r"\cdots", "symbol", "medium", fx(r"\cap\cdots\cap", r"\cap\ldots\cap"),
    r"\cdots sets the stops at mid-height (same kind of fix as pp. 49, 79, 80, 86, 95).")

# ---------------- p. 194
add(194, "'Preuve de b).'", "'Preuve de' underlined, 'b).' plain (both scans)", r"\emph{Preuve de b).}",
    "underline", "high", fx(r"\emph{Preuve de b).}", r"\emph{Preuve de} b)."), "As 'Preuve de a).' on p. 191.")
add(194, "display after 'un dérivé droit'", "RQ : D(S) ⟶ D(Qcoh(S)), R double-underlined (both scans)", r"RQ",
    "font", "high", fx(r"droit⏎\[⏎ RQ:", r"droit⏎\[⏎ \mathbb RQ:"), r"As p. 191.")
add(194, "'coïncide avec le foncteur RQ défini plus haut'", "R double-underlined (both scans)", r"$RQ$", "font",
    "high", fx(r"le foncteur $RQ$ défini", r"le foncteur $\mathbb RQ$ défini"), r"As p. 191.")
add(194, "display (1)", "E ⥲ RQ(E) , R double-underlined; this arrow has its head (both scans)", r"RQ(E)", "font",
    "high", fx(r"\xrightarrow{\sim}RQ(E),", r"\xrightarrow{\sim}\mathbb RQ(E),"),
    r"\xrightarrow{\sim} is right here.")
add(194, "display (2)", "RQ(E) ⟶ E, R double-underlined (both scans)", r"RQ(E)", "font", "high",
    fx(r"RQ(E)\longrightarrow E", r"\mathbb RQ(E)\longrightarrow E"), r"As p. 191.")
add(194, "'font de RQ : D(S) ⟶ D(Qcoh(S)) un adjoint à droite de φ : D(Qcoh(S)) ⟶ D(S). Le fait que'",
    "both maps set inline in the running text; the R of RQ double-underlined (both scans)",
    r"two displays \[...\]; plain R", "other", "medium",
    fx(r"font de⏎\[⏎ RQ:\mathrm D(S)\longrightarrow\mathrm D(\Qcoh(S))⏎\]⏎un adjoint à droite de⏎\[⏎ "
       r"\varphi:\mathrm D(\Qcoh(S))\longrightarrow\mathrm D(S).⏎\]⏎Le fait",
       r"font de $\mathbb RQ:\mathrm D(S)\longrightarrow\mathrm D(\Qcoh(S))$ un adjoint à droite de "
       r"$\varphi:\mathrm D(\Qcoh(S))\longrightarrow\mathrm D(S)$. Le fait"),
    r"The TeX makes inline formulas displays (same kind of fix as pp. 21, 34, 42, 80). This edit also writes the "
    r"double-struck R of this RQ (\mathbb R); the R cannot be fixed in a separate non-overlapping edit.")

# ---------------- p. 195
add(195, "title", "'APPENDICE I' / 'UN CONTRE-EXEMPLE DE VERDIER (1)': capitals, two lines, no full stop after I, "
    "no underline (both scans)", r"\section*{Appendice I. Un contre-exemple de Verdier...", "word", "medium",
    fx(r"\section*{Appendice I. Un contre-exemple de Verdier", r"\section*{APPENDICE I\\[3pt] UN CONTRE-EXEMPLE DE VERDIER"),
    r"Capitals against the TeX's small letters, and the TeX's added full stop. \\[3pt] is the file's form for the "
    "two-line titles of Exposés I and II (main.tex lines 1774, 3743); the footnote call stays.")
add(195, "0.2., 'Le foncteur Rf_* : D^+(X) ⟶ D^+(Y)'", "R double-underlined (both scans)", r"$Rf_*$", "font", "high",
    fx(r"Le foncteur $Rf_*:", r"Le foncteur $\mathbb Rf_*:"), r"As p. 191.")
add(195, "end of the page (text of p. 196)",
    "p. 195 ends with '(ii) ... il existe n' ≥ n' and the footnote; p. 196 begins 'tel que H_i(f^{n'},A) ⟶ "
    "H_i(f^n,A) soit nul.' (both scans)",
    "'tel que' and the display H_i(...) stand above the folio-196 marker", "marker", "high", None,
    r"Page 196 really begins with 'tel que'. Move the folio-196 marker up: python -I move_marker.py 6 196 "
    r"'tel que' --before (the last 'tel que' before the marker is this one; dry run and simulation on both layers: "
    r"'... il existe $n'\geq n$ ' / marker / 'tel que' / '\[' / display / '\]' / 'soit nul.'). The checker of "
    "p. 196 may report the same.")
add(195, "'tel que H_i(f^{n'},A) ⟶ H_i(f^n,A) soit nul.' (first line of p. 196)",
    "the map is set inline in the running text (both scans)", r"display \[...\]", "other", "medium",
    fx(r"tel que⏎\[⏎ H_i(\mathbf f^{n'},A)\longrightarrow H_i(\mathbf f^n,A)⏎\]",
       r"tel que $H_i(\mathbf f^{n'},A)\longrightarrow H_i(\mathbf f^n,A)$"),
    "The TeX makes an inline formula a display (same kind of fix as pp. 21, 34, 42, 80). The text belongs to p. 196 "
    "(marker entry above) but stands in page_195.tex, so the fix is given here; it keeps the 'tel que' anchor, so "
    "it works before or after the marker move (apply it before the move if fixes are applied by page span).")
add(195, "Lemme 1.1 ('f = (f_α)', 'f(x) = 0', 'H_i(f^n,A)')",
    "the letter f of the system of elements is underlined (f̲) (both scans)", r"\mathbf f", "font", "low", None,
    r"Convention, not itemized: the TeX writes the print's underlined f̲ as \mathbf f throughout Appendix I "
    r"(27 times in main.tex lines 4651-4800); examples on this page: $\mathbf f=(f_\alpha)$, $\mathbf f(x)=0$, "
    r"H_i(\mathbf f^n,A). The diplomatic form would be \underline f (as \underline K, \underline{\Hom}); one "
    "scripted decision for the appendix.")

# ---------------- check and write
bad = 0
for d in F:
    if d["fix"] is None:
        continue
    t = (B / f"page_{d['page']:03d}.tex").read_text(encoding="utf-8")
    n = t.count(d["fix"]["old"])
    if n != 1:
        bad += 1
        print("NOT UNIQUE", d["page"], n, repr(d["fix"]["old"][:80]))
    if "%%%%%%%%%%" in d["fix"]["old"]:
        bad += 1
        print("MARKER IN OLD", d["page"])
# overlap check between fixes on the same page
for p in range(191, 196):
    t = (B / f"page_{p:03d}.tex").read_text(encoding="utf-8")
    spans = []
    for d in F:
        if d["page"] == p and d["fix"]:
            i = t.find(d["fix"]["old"])
            spans.append((i, i + len(d["fix"]["old"]), d["where"]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            bad += 1
            print("OVERLAP", p, a[2], "|", b[2])
out = RUN / "findings_191_195.json"
out.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
from collections import Counter
c = Counter((d["page"], d["kind"] == "misprint_in_print") for d in F)
print("written", out, len(F), "entries; problems:", bad)
for p in range(191, 196):
    print(p, c[(p, False)], "/", c[(p, True)])
