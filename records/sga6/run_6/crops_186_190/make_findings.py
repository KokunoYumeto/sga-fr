"""Build findings_186_190.json for SGA 6 pp. 186-190, check that every fix's 'old' occurs exactly once in its page file,
that the fixes of a page do not overlap, and that they apply in sequence."""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_6"
B = RUN + r"\b186_190"
OUT = RUN + r"\findings_186_190.json"
BS = chr(92)
NL = chr(10)
LB = BS + BS  # LaTeX line break

FN3 = (r"$\Mod(S)$ (resp. $\Qcoh(S)$) désigne la catégorie des $\mathcal O_S$-Modules (resp. "
       r"$\mathcal O_S$-Modules quasi-cohérents).")
FN188 = r"L'indice $\Mod$ (resp. $\Qcoh$) est une abréviation pour $\mathrm D(S)$ (resp. $\mathrm D(\Qcoh(S))$)."

F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def fx(old, new):
    return {"old": old, "new": new}


PHI_NOTE = ("Closed form (a circle with a stroke), which TeX sets as \\phi; same fix as pp. 3, 12 and 165 (applied).")

# ---------------- p. 186
add(186, "3.0, display of the inclusion functor", "ø : Qcoh(S) ⟶ Mod(S): hand-drawn closed phi (both scans)",
    r"\varphi:\Qcoh(S)", "symbol", "medium", fx(r"\varphi:\Qcoh(S)", r"\phi:\Qcoh(S)"),
    PHI_NOTE + " Two more entries on this page (the same letter in the text and in footnote 4); also pp. 187, 189.")
add(186, "3.0, 's'étend en un foncteur, encore noté φ'", "encore noté ø: closed phi (both scans)",
    r"encore noté $\varphi$", "symbol", "medium", fx(r"noté $\varphi$", r"noté $\phi$"), "As the display entry.")
add(186, "footnote (4)", "Nous omettrons de noter ø: closed phi (both scans)",
    r"Nous omettrons de noter $\varphi$", "symbol", "medium", fx(r"noter $\varphi$", r"noter $\phi$"),
    "As the display entry.")
add(186, "3.0, first sentence", "'quasi-compact et quasi-séparé' underlined (quasi- / compact et quasi- / séparé, across the line break; both scans)",
    r"un schéma quasi-compact et quasi-séparé $S$ (no emphasis)", "underline", "medium",
    fx(r"un schéma quasi-compact et quasi-séparé $S$", r"un schéma \emph{quasi-compact et quasi-séparé} $S$"),
    "Running text of 3.0 (the standing hypothesis of the section), not a numbered statement; the file writes underlined "
    "words as \\emph on these pages (\\emph{Preuve.}; \\emph{réduit}, \\emph{normal} on p. 185). If the coordinator takes "
    "3.0 into the Exposé II statement pass (GLOBAL_ISSUES 82), apply it there instead.")
add(186, "3.0, footnote (3) call", "the call (³) stands at the right of the display ø : Qcoh(S) ⟶ Mod(S), not after "
    "'(pleinement fidèle)' (both scans; crops_186_190/w186_mid.png)",
    r"(pleinement fidèle)\footnote{...} before the display", "other", "medium",
    fx(r"(pleinement fidèle)\footnote{" + FN3 + "}", r"(pleinement fidèle)"),
    "Footnote call misplaced. Apply together with the next entry, which sets the call in the display with the "
    "\\footnotemark/\\footnotetext pair already used in main.tex (as the p. 61 fix) and restores the note text.")
add(186, "3.0, footnote (3) call (second edit)", "(³) at the right of the display (both scans)",
    r"\longrightarrow\Mod(S) (display without the call)", "other", "medium",
    fx(r"\longrightarrow\Mod(S)" + NL + BS + "]",
       r"\longrightarrow\Mod(S)\qquad\text{\footnotemark}" + NL + BS + "]" + r"\footnotetext{" + FN3 + "}"),
    "Goes with the previous entry: apply both or neither. Disjoint from the \\varphi entry of the same display.")
P_NOTE = ("The typescript underlines the p of the prime ideal in all three places (both scans); nothing Fraktur. "
          "Batch 181-185 wrote the underlined p of p. 185 as \\underline{p}_i and the plain p_i as p. Low: tied to the "
          "pending decision on the typist's underlined letters (O̲ written \\mathcal O); drop the three entries if the "
          "volume keeps \\mathfrak for the underlined p.")
add(186, "Preuve of 2.4.8.2, 'Soit p un idéal premier'", "p̲: a typed p, underlined (both scans)",
    r"Soit $\mathfrak p$ un idéal", "font", "low", fx(r"Soit $\mathfrak p$ un idéal", r"Soit $\underline{p}$ un idéal"),
    P_NOTE)
add(186, "Preuve of 2.4.8.2, dim(O_{Y,x})_p", "index p̲, underlined (both scans)",
    r"(\mathcal O_{Y,x})_{\mathfrak p}", "font", "low",
    fx(r"(\mathcal O_{Y,x})_{\mathfrak p}", r"(\mathcal O_{Y,x})_{\underline{p}}"), "As the previous entry.")
add(186, "Preuve of 2.4.8.2, 'on aurait p = 0'", "p̲ = 0 (both scans)",
    r"aurait $\mathfrak p=0$", "font", "low", fx(r"aurait $\mathfrak p=0$", r"aurait $\underline{p}=0$"),
    "As the previous entries.")

# ---------------- p. 187
add(187, "Lemme 3.2, 'Le foncteur φ : Qcoh(S) → Mod(S)'", "ø: closed phi (both scans)",
    r"$\varphi:\Qcoh(S)", "symbol", "medium", fx(r"$\varphi:\Qcoh(S)", r"$\phi:\Qcoh(S)"), PHI_NOTE)
add(187, "Preuve of 3.2, display (1)", "Hom(E,f_*(F)) ≃ Hom(E,f_*Q(F)) .: a hand-drawn tilde over a straight stroke, "
    "no arrowhead (both scans; crops_186_190/c187_iso.png, w187_top.png)",
    r"\Hom(E,f_*(F))\xrightarrow{\sim} \Hom(E,f_*Q(F)).", "symbol", "high",
    fx(r"f_*(F))\xrightarrow{\sim}", r"f_*(F))\simeq"),
    "Headless ≃, as the signs fixed on pp. 110, 118, 146, 150, 153. All nine isomorphism signs of pp. 187-190 are "
    "headless; one entry per sign.")
add(187, "Preuve of 3.2, 'on a une flèche naturelle évidente Q(F|U) → g_*Q(F|V).'",
    "the map is set inline in the running text: 'évidente Q(F|U) ⟶ g_*Q(F|V). Par suite, on déduit de (2) une flèche' (both scans)",
    r"a display \[ Q(F|U)\longrightarrow g_*Q(F|V). \]", "other", "medium",
    fx(r"évidente" + NL + BS + "[" + NL + r" Q(F|U)\longrightarrow g_*Q(F|V)." + NL + BS + "]" + NL + "Par suite",
       r"évidente $Q(F|U)\longrightarrow g_*Q(F|V)$. Par suite"),
    "The TeX makes an inline formula a display (same kind of fix as pp. 21, 34, 42, 80, 105).")
add(187, "Preuve of 3.2, 'on prend Q = Γ̃_S'", "Γ̃_S: the hand-drawn tilde stands over the Γ, the S is its index "
    "(both scans; crops_186_190/c187_gamma.png)",
    r"Q=\widetilde{\Gamma_S}", "formula", "low", fx(r"Q=\widetilde{\Gamma_S}", r"Q=\widetilde{\Gamma}_S"),
    "Scope of the tilde; the same notation recurs on p. 189 (clearer there). Low: the tilde is drawn wide here.")

# ---------------- p. 188
add(188, "top display", "Hom(E,F) ≃ Hom(E,QF) .: tilde over a straight stroke, no arrowhead (both scans)",
    r"\Hom(E,F)\xrightarrow{\sim}\Hom(E,QF).", "symbol", "high",
    fx(r"\Hom(E,F)\xrightarrow{\sim}\Hom(E,QF)", r"\Hom(E,F)\simeq\Hom(E,QF)"), "Headless ≃ (as p. 187).")
add(188, "Lemme 3.3 b), display", "R̳Q : D⁺(S) ⟶ D⁺(Qcoh(S)): R with a double underline (both scans; crops_186_190/w188_main.png)",
    r"RQ:\mathrm D^+(S)", "font", "high", fx(r"RQ:\mathrm D^+(S)", r"\mathbb RQ:\mathrm D^+(S)"),
    "Double-struck derived-functor R written plain; same form as the applied fixes of pp. 175-176 and 181-182 "
    "(\\mathbb R). Five places on this page, two on p. 189; the R of R^iQ, R^qQ, R^nQ, R^pQ, R^*Q on pp. 189-190 is "
    "plain in the print, as in the TeX.")
add(188, "Lemme 3.3 b), (i), first member", "R̳ Hom_Mod(E,F): R double-underlined (both scans)",
    r"R\Hom_{\Mod}(E,F)", "font", "high", fx(r"R\Hom_{\Mod}", r"\mathbb R\Hom_{\Mod}"), "As the RQ entry.")
add(188, "Lemme 3.3 b), (i), sign and second member", "≃ without arrowhead, then R̳ Hom_Qcoh (both scans)",
    r"&\xrightarrow{\sim} R\Hom_{\Qcoh}", "formula", "high",
    fx(r"&\xrightarrow{\sim} R\Hom_{\Qcoh}", r"&\simeq \mathbb R\Hom_{\Qcoh}"),
    "Two changes in one edit (headless ≃ and double-struck R): the arrow of (i) has no unique anchor on the page "
    "without the R next to it, since (ii) repeats '\\Hom_{\\Mod}(E,F)&\\xrightarrow{\\sim} '.")
add(188, "Lemme 3.3 b), (i), R̳Q(F)", "E,R̳Q(F): R double-underlined (both scans)",
    r"(E,RQ(F)) \tag{i}", "font", "high", fx(r"(E,RQ(F)) ", r"(E,\mathbb RQ(F)) "),
    "The 'old' ends with the space before \\tag{i} (unique: (ii) has '(E,RQ(F)).'); disjoint from the footnote edit at \\tag{i}.")
add(188, "Lemme 3.3 b), (ii), sign", "Hom_Mod(E,F) ≃ Hom_Qcoh: no arrowhead (both scans)",
    r"&\xrightarrow{\sim} \Hom_{\Qcoh}", "symbol", "high",
    fx(r"&\xrightarrow{\sim} \Hom_{\Qcoh}", r"&\simeq \Hom_{\Qcoh}"), "Headless ≃.")
add(188, "Lemme 3.3 b), (ii), R̳Q(F)", "E,R̳Q(F)) .: R double-underlined (both scans)",
    r"(E,RQ(F)).", "font", "high", fx(r"(E,RQ(F)).", r"(E,\mathbb RQ(F))."), "As the RQ entry.")
add(188, "Lemme 3.3 b), footnote (1) call", "the call (¹) stands at the right of formula (i), not after 'canoniques' "
    "(both scans; crops_186_190/w188_main.png)",
    r"canoniques\footnote{L'indice ...}", "other", "medium",
    fx(r"canoniques\footnote{" + FN188 + "}", r"canoniques"),
    "The note explains the indices Mod and Qcoh of (i). First of three edits that go together: this one removes the "
    "call, the next sets \\footnotemark in (i), the third puts the \\footnotetext after the align.")
add(188, "Lemme 3.3 b), footnote (1) call (second edit)", "(¹) after (i) (both scans)",
    r"\tag{i}" + LB, "other", "medium",
    fx(r"\tag{i}" + LB, r"\qquad\text{\footnotemark}\tag{i}" + LB),
    "Goes with the previous and the next entry: apply all three or none.")
add(188, "Lemme 3.3 b), footnote (1) call (third edit)", "footnote text of (¹) (both scans)",
    r"\end{align}", "other", "medium",
    fx(r"\end{align}", r"\end{align}\footnotetext{" + FN188 + "}"),
    "Goes with the two previous entries.")
add(188, "Lemme 3.4, display", "Qf_*(E) ≃ f_*Q(E) .: tilde over a straight stroke, no arrowhead (both scans; crops_186_190/c188_Qf.png)",
    r"Qf_*(E)\xrightarrow{\sim} f_*Q(E).", "symbol", "high",
    fx(r"Qf_*(E)\xrightarrow{\sim} f_*Q(E)", r"Qf_*(E)\simeq f_*Q(E)"), "Headless ≃.")

# ---------------- p. 189
add(189, "Proposition 3.5, display (3.0)", "ø : D⁺(Qcoh(S)) ⟶ D⁺(S): closed phi (both scans)",
    r"\varphi:\mathrm D^+(\Qcoh(S))", "symbol", "medium",
    fx(r"\varphi:\mathrm D^+(\Qcoh(S))", r"\phi:\mathrm D^+(\Qcoh(S))"), PHI_NOTE)
add(189, "(3.5.1), display", "E ⟶ R̳Q(E): R double-underlined (both scans)",
    r"E\longrightarrow RQ(E)", "font", "high", fx(r"E\longrightarrow RQ(E)", r"E\longrightarrow \mathbb RQ(E)"),
    "As p. 188.")
add(189, "(3.5.2), display", "R̳Q(E) ⟶ E: R double-underlined (both scans)",
    r"RQ(E)\longrightarrow E", "font", "high", fx(r"RQ(E)\longrightarrow E", r"\mathbb RQ(E)\longrightarrow E"),
    "As p. 188.")
add(189, "'Preuve de (3.5.1).'", "only 'Preuve de' is underlined; '(3.5.1).' is plain (both scans; crops_186_190/c189_preuvede.png)",
    r"\emph{Preuve de (3.5.1).}", "underline", "high",
    fx(r"\emph{Preuve de (3.5.1).}", r"\emph{Preuve de} (3.5.1)."),
    "As \\emph{Preuve} de 2.2.7. on p. 172 (batch 171-175). Same on p. 190.")
add(189, "Preuve de (3.5.1), 'cela résulte de la formule Q = Γ̃_S'", "Γ̃_S: a small tilde over the Γ only, the index S "
    "outside it (both scans)",
    r"Q=\widetilde{\Gamma_S}", "formula", "low", fx(r"Q=\widetilde{\Gamma_S}", r"Q=\widetilde{\Gamma}_S"),
    "Scope of the tilde, as on p. 187.")

# ---------------- p. 190
add(190, "start of the page", "p. 190 begins 'ainsi d'ailleurs que les inclusions f_{i_o...i_p} ...'; p. 189 ends "
    "'sont des morphismes affines,' above the footnote (both scans)",
    "'ainsi d'%' stands under the folio-189 marker, at the end of the line '... sont des morphismes affines, ainsi d'%'",
    "marker", "high", None,
    "Page 190 really begins with 'ainsi d'ailleurs'. Fix: python -I move_marker.py 6 190 \"ainsi d'%\" --before "
    "(simulated in memory on both layers of the present main.tex with crops_186_190/sim_marker.py: "
    "'... sont des morphismes affines, ' / the marker / 'ainsi d'%' / 'ailleurs que les inclusions ...', which still "
    "renders 'd'ailleurs'). The page texts of the snapshot match the present main.tex.")
add(190, "first line, U_{i_o} ∩ ... ∩ U_{i_p}", "three typed full stops on the baseline (both scans)",
    r"U_{i_0}\cap\cdots\cap U_{i_p}", "symbol", "medium",
    fx(r"U_{i_0}\cap\cdots\cap U_{i_p}", r"U_{i_0}\cap\ldots\cap U_{i_p}"),
    "\\cdots sets the dots at mid-height (same kind of fix as pp. 161, 162, 166, 184, 185).")
add(190, "display (*), first coproduct", "∐f_{i*}f_i^*(E): no index under the coproduct sign (both scans; "
    "crops_186_190/c190_star.png, w190_main.png)",
    r"\coprod_i f_{i*}f_i^*(E)", "extra", "high", fx(r"\coprod_i f_{i*}", r"\coprod f_{i*}"),
    "Summation index added by the TeX; (**) below has its index i_o...i_p in the print and keeps it.")
add(190, "display (*), dots", "⟶ ... ⟶: three typed full stops on the baseline (both scans)",
    r"\longrightarrow\cdots\longrightarrow", "symbol", "medium",
    fx(r"\longrightarrow\cdots\longrightarrow", r"\longrightarrow\ldots\longrightarrow"), "As the first line.")
add(190, "display (*), second coproduct", "∐f_{i_o...i_p *}f_{i_o...i_p}^*(E): no index under the coproduct sign (both scans)",
    r"\coprod_{i_0\ldots i_p}f_{i_0\ldots i_p*}", "extra", "high",
    fx(r"\coprod_{i_0\ldots i_p}f_{i_0\ldots i_p*}", r"\coprod f_{i_0\ldots i_p*}"), "As the first coproduct.")
add(190, "display (*), end", "'(E) ⟶ .': the last arrow is followed only by the full stop, no dots (both scans; "
    "crops_186_190/c190_star.png, w190_main.png)",
    r"\longrightarrow\cdots .", "extra", "high", fx(r"\longrightarrow\cdots .", r"\longrightarrow ."),
    "The TeX adds \\cdots after the last arrow.")
add(190, "display (***), sign", "(***) R^qQ(...) ≃ f_{...*}R^qQ(...): tilde over a straight stroke, no arrowhead "
    "(both scans; crops_186_190/c190_3star.png)",
    r"\xrightarrow{\sim} f_{i_0\ldots i_p*}R^qQ", "symbol", "high",
    fx(r"\xrightarrow{\sim} f_", r"\simeq f_"), "Headless ≃.")
add(190, "display (***), end", "no punctuation after (***): the sentence goes on 'pour tout q, d'où en particulier' "
    "(both scans)",
    r"...f_{i_0\ldots i_p}^*(E)\bigr).", "punctuation", "high",
    fx(r"\bigr)." + NL + BS + "end{equation}", r"\bigr)" + NL + BS + "end{equation}"),
    "Full stop added at the end of a display.")
add(190, "display R^nQ(E) ≃ H^n(QE˙), sign", "≃ without arrowhead (both scans; crops_186_190/c190_RnQ.png)",
    r"R^nQ(E)\xrightarrow{\sim}", "symbol", "high",
    fx(r"R^nQ(E)\xrightarrow{\sim}", r"R^nQ(E)\simeq"), "Headless ≃.")
add(190, "display R^nQ(E) ≃ H^n(QE˙)", "QE˙: E with a typed raised dot (the complex E˙), not a prime; the "
    "apostrophes of the page (d'après, d'où) are taller ticks (both scans; crops_186_190/c190_RnQ.png, w190_low.png)",
    r"H^n(QE')", "symbol", "high", fx(r"H^n(QE')", r"H^n(QE^\bullet)"),
    "The resolution complex E˙ = (E^n) of (*), whose terms E^n appear in the next sentence. The file writes the "
    "typed raised dot as ^\\bullet (Gr^\\bullet, K^\\bullet).")
add(190, "'où E˙ est la résolution de E'", "E˙: raised dot (both scans; crops_186_190/c190_Edot.png, w190_low.png)",
    r"où $E'$ est", "symbol", "high", fx(r"où $E'$ est", r"où $E^\bullet$ est"), "As the previous entry.")
add(190, "'on a QE^n ≃ E^n'", "≃ without arrowhead (both scans; crops_186_190/c190_Edot.png)",
    r"QE^n\xrightarrow{\sim} E^n", "symbol", "high",
    fx(r"QE^n\xrightarrow{\sim} E^n", r"QE^n\simeq E^n"), "Headless ≃.")
add(190, "'et Q(E) ≃ E , cqfd.'", "≃ without arrowhead (both scans; crops_186_190/c190_QE.png)",
    r"Q(E)\xrightarrow{\sim} E$", "symbol", "high",
    fx(r"Q(E)\xrightarrow{\sim} E$", r"Q(E)\simeq E$"), "Headless ≃.")
add(190, "'Preuve de (3.5.2).'", "only 'Preuve de' is underlined (both scans)",
    r"\emph{Preuve de (3.5.2).}", "underline", "high",
    fx(r"\emph{Preuve de (3.5.2).}", r"\emph{Preuve de} (3.5.2)."), "As p. 189.")

# ---------------- checks
ok = True
pages = {}
for p in range(186, 191):
    pages[p] = open(B + rf"\page_{p}.tex", encoding="utf-8").read()
spans = {}
for i, d in enumerate(F):
    if not d["fix"]:
        continue
    t = pages[d["page"]]
    old = d["fix"]["old"]
    n = t.count(old)
    if n != 1:
        ok = False
        print("NOT UNIQUE", d["page"], n, repr(old[:80]))
        continue
    if "%%%%%%%%%%" in old or "%%%%%%%%%%" in d["fix"]["new"]:
        ok = False
        print("MARKER TOUCHED", d["page"], repr(old[:60]))
    k = t.find(old)
    spans.setdefault(d["page"], []).append((k, k + len(old), i))
for p, ss in spans.items():
    ss.sort()
    for (a1, b1, i1), (a2, b2, i2) in zip(ss, ss[1:]):
        if a2 < b1:
            ok = False
            print("OVERLAP", p, i1, i2)
# apply in sequence
for p in range(186, 191):
    t = pages[p]
    for d in F:
        if d["page"] == p and d["fix"]:
            if t.count(d["fix"]["old"]) != 1:
                ok = False
                print("SEQUENTIAL FAIL", p, repr(d["fix"]["old"][:60]))
            t = t.replace(d["fix"]["old"], d["fix"]["new"], 1)
    open(RUN + rf"\crops_186_190\applied_{p}.tex", "w", encoding="utf-8", newline="").write(t)
json.dump(F, open(OUT, "w", encoding="utf-8", newline=""), ensure_ascii=False, indent=1)
from collections import Counter
c = Counter((d["page"], d["kind"] == "misprint_in_print") for d in F)
for p in range(186, 191):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
print("total", len(F), "ok" if ok else "PROBLEMS")
