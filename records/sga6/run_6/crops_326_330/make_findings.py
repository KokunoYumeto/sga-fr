"""Write findings_326_330.json (run folder) and check that every fix's old string occurs exactly once in its
page file. '<NL>' in old/new stands for a line break (the page files use LF)."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
BATCH = RUN / "b326_330"
OUT = RUN / "findings_326_330.json"


def fx(old, new):
    return {"old": old.replace("<NL>", "\n"), "new": new.replace("<NL>", "\n")}


F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex.replace(chr(92) + chr(34), chr(34)), "kind": kind, "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- p. 326
add(326, "start of page (folio-326 marker)",
    "p. 326 begins with the heading '3.3. Soient K, K' deux λ-anneaux, f : K → K' un homomorphisme d'anneaux.' (both scans)",
    r"'\textbf{3.3.}' is the last line of page_325.tex, above the folio-326 marker; page_326.tex begins 'Soient \(K\), \(K'\) deux'",
    "marker", "high", None,
    r"Page 326 really begins with the heading '\textbf{3.3.}' (a heading at the top of a page, not moved by the 10 Nov script). "
    r"python -I move_marker.py 6 326 '\textbf{3.3.}' --before (simulated in memory on both layers with crops_326_330/sim_markers.py: "
    r"'\]' / blank / marker / '\textbf{3.3.}' / 'Soient \(K\), ...'). The checker of p. 325 may report the same boundary: apply once.")

add(326, "3.3, end: 'ou encore γ_t(f(x)) = Ĝ_g(f)∘γ_t(x).'",
    "the formula stands in the running text, at the left margin of the line after '... γ^i(f(x)), ou encore', at ordinary line spacing; the blank before 3.4 follows (both scans)",
    r"display \[ \gamma_t(f(x))=\Gg(f)\circ\gamma_t(x). \]",
    "other", "medium",
    fx(r"ou encore<NL>\[<NL>  \gamma_t(f(x))=\Gg(f)\circ\gamma_t(x).<NL>\]", r"ou encore \(\gamma_t(f(x))=\Gg(f)\circ\gamma_t(x)\)."),
    "The TeX makes an inline formula a display (same kind of fix as pp. 21, 34, 42, 80, 277, 301, 303).")

add(326, "3.3, 'D'après le définition 3.2.ii)'",
    "D'après le définition (both scans)",
    "D'après le définition (printed reading kept)",
    "misprint_in_print", "high", None,
    "Gender slip of the typist ('définition' is feminine), as 'le j-ième fonction' on p. 305. The TeX keeps the printed reading; the corrected layer still reads 'le définition'.",
    corrected="D'après la définition")

add(326, "3.5, label of the first arrow Ĝ×Ĝ → Ĝ×Ĝ",
    "(ρ^{-1}.ρ^{-1}): a round typed full stop on the baseline of the label between the two ρ^{-1} (both scans; crops_326_330/c326_arrow_zoom.png, w326_arrow.png); the comma after the display has its tail (c326_comma_zoom.png)",
    r"\xrightarrow{(\rho^{-1},\rho^{-1})} (silently corrected)",
    "misprint_in_print", "medium",
    fx(r"(\rho^{-1},\rho^{-1})", r"(\rho^{-1}.\rho^{-1})"),
    "The label is the pair of maps (ρ^{-1},ρ^{-1}) on Ĝ×Ĝ; the typist struck a full stop for the comma. The TeX silently corrects; the fix restores the printed reading in the diplomatic layer.",
    corrected=r"(\rho^{-1},\rho^{-1})")

add(326, "3.5, 'Cette nouvelle multiplication sera notée v.'",
    "'notée v' typed on a pasted-in correction (lighter typeface): a Latin v (both scans; crops_326_330/c326_notee.png)",
    r"sera notée \(v\). (printed reading kept)",
    "misprint_in_print", "medium", None,
    "From (3.5.1) on the print writes this law with the hand-drawn ∇: (1+Xt)∇(1+Yt), 'la loi ∇', 1_∇, Ĝ_∇; the typed v of the correction stands for it. The TeX keeps the printed v (the corrected layer too); for the corrected layer.",
    corrected=r"sera notée \(\nabla\).")

# ---------------------------------------------------------------- p. 327
add(327, "after (3.5.1), 'Si K est un λ-anneau, on a donc pour tous x,y ∈ K :'",
    "'Si K est un λ-anneau' begins a new, indented paragraph (both scans)",
    r"\end{align} followed directly by 'Si \(K\) est' (the paragraph runs on)",
    "other", "high",
    fx(r"\end{align}<NL>Si \(K\) est", r"\end{align}<NL><NL>Si \(K\) est"),
    "Missing paragraph break.")

add(327, "after (3.5.2), 'Le n-ième polynôme universel de la loi ∇'",
    "'Le n-ième polynôme universel' begins a new, indented paragraph (both scans)",
    r"\end{equation} followed directly by 'Le \(n\)-ième'",
    "other", "high",
    fx(r"\end{equation}<NL>Le \(n\)-ième", r"\end{equation}<NL><NL>Le \(n\)-ième"),
    "Missing paragraph break.")

add(327, "after (3.5.3), 'Notons enfin que la loi ∇ admet un élément unité'",
    "'Notons enfin' begins a new, indented paragraph (both scans)",
    r"\end{equation} followed directly by 'Notons enfin'",
    "other", "high",
    fx(r"\end{equation}<NL>Notons enfin", r"\end{equation}<NL><NL>Notons enfin"),
    "Missing paragraph break.")

add(327, "the unit elements 1̲_∇ and 1̲_o: 'il sera parfois noté 1̲_∇' (p. 327), the display λ'_u(1+Xt) = ... (printed on p. 328, in page_327.tex now) and (3.6.2) (p. 328)",
    "the 1 of the unit is underlined in all 8 places: noté 1̲_∇; in the display 1̲_o twice, 1̲_∇ + {1+Xt}u/(1̲_∇ + 1̲_∇.u), ρ_u^{-1}(1̲_∇ + {1+Xt}u); (3.6.2) γ'_u(1+Xt) = 1̲_∇ + {1+Xt}u (both scans; crops_326_330/c327_unit.png, c328_denom.png, w328_denom.png)",
    r"1_\nabla, 1_{\nabla'}, 1_o (plain)",
    "underline", "high", None,
    r"Convention of the Exposé V transcription (no underlines; as the underlined letters reported for p. 315), reported once. "
    r"Three examples, in the form to use if the diplomatic layer reproduces them: 'noté \(1_\nabla\)' -> 'noté \(\underline{1}_\nabla\)'; "
    r"'{1_o+\{1+(X+1)t\}u}{1_o+\{1+t\}u}' -> '{\underline{1}_o+\{1+(X+1)t\}u}{\underline{1}_o+\{1+t\}u}'; "
    r"p. 328 '=1_\nabla+\{1+Xt\}u .' -> '=\underline{1}_\nabla+\{1+Xt\}u .'. "
    r"Safe for a script, unlike the sheaf letters: every 1_\nabla, 1_{\nabla'} and 1_o of main.tex (8, all on folios 327-328) is underlined in the print. "
    r"The underline is part of the notation defined here (the unit 1̲_∇ against the integer 1 of 1+Xt).")

add(327, "3.6, 'Les \"opérations λ\" sont définies par le diagramme commutatif'",
    "opérations λ \" : λ without a prime, a space before the closing quote (both scans; crops_326_330/c327_lambda_zoom.png, w327_lambda.png)",
    r"«~opérations \(\lambda'\)~»",
    "symbol", "high",
    fx(r"«~opérations \(\lambda'\)~»", r"«~opérations \(\lambda\)~»"),
    "The sentence names the λ-operations of the new structure and ends 'et seront notées λ'' (last line of the page): the unprimed λ is the printed and intended reading.")

add(327, "diagram (3.6.1), bottom arrow 1+K[[t]]^+ → 1+{1+K[[t]]^+}[[u]]^+",
    "λ'_u above the bottom arrow (both scans)",
    r"\arrow[r,\"\lambda'_u\"'] (the ' sets the label below the arrow)",
    "formula", "medium",
    fx(r"\arrow[r,\"\lambda'_u\"']".replace('\\"', '"'), r"\arrow[r,\"\lambda'_u\"]".replace('\\"', '"')),
    "Label on the wrong side of the arrow; λ_u (top) and ρ_t (left) stand as printed.")

add(327, "diagram (3.6.1), right vertical arrow",
    "Ĝ(ρ_t) stands to the left of the right vertical arrow (both scans)",
    r"\arrow[d,\"\Ghat(\rho_t)\"] (label set to the right)",
    "formula", "medium",
    fx(r"\arrow[d,\"\Ghat(\rho_t)\"]".replace('\\"', '"'), r"\arrow[d,\"\Ghat(\rho_t)\"']".replace('\\"', '"')),
    "Label on the wrong side of the arrow.")

add(327, "display λ'_u(1+Xt) = ..., third row (printed at the top of p. 328; in page_327.tex now)",
    "= Ĝ ( _t)((1̲_o + {1+(X+1)t}u)/(1̲_o + {1+t}u)): the hand-drawn ρ before the index t is missing, a blank between '(' and 't' (both scans; witness p. 328); the rows above and below have Ĝ(ρ_t)",
    r"\Ghat(\rho_t)\left(\frac{1_o+... (silently corrected)",
    "misprint_in_print", "high",
    fx(r"\Ghat(\rho_t)\left(\frac", r"\Ghat({}_t)\left(\frac"),
    "The ρ was never drawn; the TeX silently supplies it. {}_t keeps the empty place with its index. Filed under p. 327 because the display stands in page_327.tex now (see the p. 328 marker entry); the old string is also unique after the marker move.",
    corrected=r"\Ghat(\rho_t)\left(\frac")

add(327, "same display, fourth row, denominator 1̲_∇ + 1̲_∇.u (printed on p. 328; in page_327.tex now)",
    "after the hand-drawn subscript ∇ of the second 1̲_∇ a typed stop on the baseline of the row, just before u; no prime on ∇ (both scans; crops_326_330/c328_dotu.png, w328_dotu.png, c328_denom.png)",
    r"1_{\nabla'}u",
    "symbol", "medium",
    fx(r"_{\nabla'}u}", r"_\nabla.u}"),
    "The denominator is 1_∇ + 1_∇·u (Ĝ(ρ_t) maps 1_o = 1+t to 1_∇); no ∇' occurs anywhere in the text. Filed under p. 327 because the display stands in page_327.tex now; the old string survives an \\underline{1} edit of the underline convention.")

# ---------------------------------------------------------------- p. 328
add(328, "start of page (folio-328 marker)",
    "p. 328 begins with the display 'λ'_u(1+Xt) = Ĝ(ρ_t)(λ_u(ρ_t^{-1}(1+Xt))) = ... = ρ_u^{-1}(1̲_∇ + {1+Xt}u).'; p. 327 ends '... Elles sont définies par leur valeur pour 1+Xt ; on a :' (both scans)",
    r"'\[', '\begin{aligned}' and the five rows of the display are the last lines of page_327.tex; the folio-328 marker stands inside the display, page_328.tex begins '\end{aligned}'",
    "marker", "high", None,
    r"Page 328 really begins with the '\[' that opens the aligned display, right after 'on a :'. python -I move_marker.py 6 328 '\[' --before "
    r"(simulated in memory on both layers with crops_326_330/sim_markers.py: '... pour \(1+Xt\)~; on a :' / marker / '\[' / '\begin{aligned}' / "
    r"'\lambda'_u(1+Xt) &=...'). The entries for this display filed under p. 327 work before or after the move.")

add(328, "after the display, 'Si on note γ' les opérations γ correspondant aux opérations λ''",
    "'Si on note γ'' begins a new, indented paragraph (both scans)",
    r"\] followed directly by 'Si on note'",
    "other", "high",
    fx(r"\]<NL>Si on note", r"\]<NL><NL>Si on note"),
    "Missing paragraph break.")

add(328, "after (3.6.2), 'On notera Q'_{i,j} le coefficient'",
    "'On notera' begins a new, indented paragraph (both scans)",
    r"\end{equation} followed directly by 'On notera'",
    "other", "high",
    fx(r"\end{equation}<NL>On notera", r"\end{equation}<NL><NL>On notera"),
    "Missing paragraph break.")

add(328, "'le coefficient de t^j dans γ'^i(1+...+X_nt^n+...)'",
    "typed stops on the baseline, twice (both scans; crops_326_330/c328_dots1.png)",
    r"\gamma'^i(1+\cdots+X_nt^n+\cdots)",
    "symbol", "medium",
    fx(r"\gamma'^i(1+\cdots+X_nt^n+\cdots)", r"\gamma'^i(1+\ldots+X_nt^n+\ldots)"),
    r"\cdots sets the dots at mid-height; the typescript has baseline stops (same fix as pp. 298-299, 308, 310).")

add(328, "before 'Soient K un λ-anneau, x ∈ K. Du diagramme (3.6.1)'",
    "'Soient K un λ-anneau' begins a new, indented paragraph after '... de poids variant entre j et ij.' (both scans)",
    r"'et \(ij\). Soient \(K\)' (same paragraph)",
    "other", "high",
    fx(r"et \(ij\). Soient", r"et \(ij\).<NL><NL>Soient"),
    "Missing paragraph break.")

add(328, "after (3.6.4), 'On remarquera enfin que la structure de pré-λ-anneau'",
    "'On remarquera enfin' begins a new, indented paragraph (both scans)",
    r"\end{equation} followed directly by 'On remarquera'",
    "other", "high",
    fx(r"\end{equation}<NL>On remarquera", r"\end{equation}<NL><NL>On remarquera"),
    "Missing paragraph break.")

add(328, "3.7, 'sera noté Ĝ_o (resp. Ĝ_∇)'",
    "Ĝ with the typed letter o as index, x-height o as in 1̲_o (p. 328) and Ĝ(A)_o, Ĝ^u(A)_o (p. 329); the small circle of 'le signe ∘' (p. 326) and Ĝ∘Ĝ (p. 327) is a different sign (both scans; crops_326_330/c328_Go.png)",
    r"\(\Gcirc\) (= \widehat G_{\circ})",
    "symbol", "low",
    fx(r"sera noté \(\Gcirc\)", r"sera noté \(\Ghat_o\)"),
    r"The TeX writes the same typed o as the letter o elsewhere (1_o on p. 328, \Ghat(A)_o and \Ghat^u(A)_o on p. 329); \Gcirc occurs only here and in the index of notations. Low: the o names the law ∘; decide with the index-zero-as-o convention.")

# ---------------------------------------------------------------- p. 329
add(329, "first paragraph, 'tel que le diagramme 3.7.1 soit commumatif'",
    "commumatif (both scans)",
    "commumatif (printed reading kept)",
    "misprint_in_print", "high", None,
    "Typing error; the next line has 'soit commutatif'. The TeX keeps the printed reading (the corrected layer too).",
    corrected="commutatif")

add(329, "between the diagrams (3.7.1) and (3.7.2)",
    "nothing between the two diagrams: (3.7.2) follows (3.7.1) after a blank (both scans)",
    r"'\]' / 'et' / '\['",
    "extra", "high",
    fx(r"\]<NL>et<NL>\[", r"\]<NL>\["),
    "The TeX adds the word 'et'.")

add(329, "diagram (3.7.1), bottom arrow Ĝ^t(A)_o → Ĝ^u(Ĝ^t(A)_o)_o",
    "λ_u above the bottom arrow (both scans)",
    r"\arrow[r,\"\lambda_u\"'] (label set below the arrow)",
    "formula", "medium",
    fx(r"\arrow[r,\"\lambda_u\"']".replace('\\"', '"'), r"\arrow[r,\"\lambda_u\"]".replace('\\"', '"')),
    "Label on the wrong side of the arrow; the other three labels stand as printed.")

add(329, "diagram (3.7.2), left vertical arrow A → Ĝ^t(A)_∇ (label γ_t)",
    "a plain vertical line without arrowhead; the right vertical arrow and both vertical arrows of (3.7.1) have their heads (both scans; crops_326_330/c329_gline.png, w329_gline.png)",
    r"\arrow[d,\"\gamma_t\"'] (with a head)",
    "misprint_in_print", "medium",
    fx(r"\arrow[d,\"\gamma_t\"']".replace('\\"', '"'), r"\arrow[d,\"\gamma_t\"',dash]".replace('\\"', '"')),
    "The head was not drawn; the TeX silently supplies it (same kind of entry as pp. 31, 92, 142). dash is tikz-cd's key for a line without tips.",
    corrected=r"\arrow[d,\"\gamma_t\"']".replace('\\"', '"'))

add(329, "diagram (3.7.2), bottom arrow Ĝ^t(A)_∇ → Ĝ^u(Ĝ^t(A)_∇)_∇",
    "γ'_u above the bottom arrow (both scans)",
    r"\arrow[r,\"\gamma'_u\"'] (label set below the arrow)",
    "formula", "medium",
    fx(r"\arrow[r,\"\gamma'_u\"']".replace('\\"', '"'), r"\arrow[r,\"\gamma'_u\"]".replace('\\"', '"')),
    "Label on the wrong side of the arrow; γ_u (top), γ_t (left) and Ĝ^u(γ_t) (right) stand as printed.")

add(329, "(3.8.1), end",
    "'... = exp(-xLog(1-t))' with no punctuation (both scans; crops_326_330/c329_381end.png)",
    r"=\exp(-x\Log(1-t)).",
    "punctuation", "high",
    fx(r"=\exp(-x\Log(1-t)).", r"=\exp(-x\Log(1-t))"),
    "The TeX adds a full stop at the end of the display.")

add(329, "after (3.8.1), 'Soit a un élément de K'",
    "'Soit a un élément de K' begins a new, indented paragraph (both scans)",
    r"\end{equation} followed directly by 'Soit \(a\)'",
    "other", "high",
    fx(r"\end{equation}<NL>Soit \(a\)", r"\end{equation}<NL><NL>Soit \(a\)"),
    "Missing paragraph break.")

add(329, "display after 'soit :' (γ_t(a)∇(1+Xt) = ρ_t(...) = ρ_t((...)^a)), end",
    "the display ends with the closing parenthesis, no punctuation (both scans; crops_326_330/c329_dispend.png)",
    r"...\right)^a\right).",
    "punctuation", "high",
    fx(r"\right)^a\right).", r"\right)^a\right)"),
    "The TeX adds a full stop at the end of the display.")

# ---------------------------------------------------------------- p. 330
add(330, "Définition 3.9 (the statement)",
    "underlined word group by word group: 'Soit', 'un', 'anneau', 'on appelle', 'la donnée d'une', 'algèbre', 'et d'un', 'homomorphisme de', 'algèbres', 'est un', 'homomorphisme compatible aux augmentations'; the defined terms K-λ-algèbre augmentée and homomorphisme de K-λ-algèbres augmentées are left plain (both scans)",
    r"the statement in roman (no \underline, no \emph)",
    "underline", "high", None,
    "Exposé V continues the Exposé II-IV pattern of GLOBAL_ISSUES 82 (as reported for pp. 298, 306-311, 314): not itemized, for the scripted per-exposé decision. No \\emph on the plain defined terms (as the print).")

add(330, "Exemple 3.9.1: the constant sheaf ℤ̲ (7 places) and the sheaves F̲, F̲' (2 places)",
    "ℤ underlined in H^o(X,ℤ̲) (5 times), 'faisceau constant ℤ̲ sur X', 'une section de ℤ̲'; 'soit alors F̲ le faisceau', 'et soit F̲' le faisceau' (the underline stops before the prime). Plain in the print: 'l'élément F - F'', A, A^n, U_n (both scans; witness p. 330)",
    r"\mathbb Z, F, F' (plain)",
    "underline", "high", None,
    r"Convention of the Exposé V transcription (no underlines), reported once as for the letters of p. 315. Three examples, in the form to use if the diplomatic layer reproduces them: "
    r"'et que \(H^0(X,\mathbb Z)\) est' -> 'et que \(H^0(X,\underline{\mathbb Z})\) est'; 'faisceau constant \(\mathbb Z\) sur' -> 'faisceau constant \(\underline{\mathbb Z}\) sur'; "
    r"'et soit \(F'\) le faisceau' -> 'et soit \(\underline{F}'\) le faisceau'. Not for a blind script on F (plain in F - F'). main.tex has no underlined Z anywhere "
    r"(23 times H^0(X,\mathbb Z)): other pages may have the same omission (not checked).")

add(330, "'l'additivité du rang entraine qu'on définit ainsi'",
    "entraine: a plain dotted i, no circumflex (both scans; crops_326_330/c330_entraine.png, w330_entraine.png; the a is broken)",
    "entraîne (silently corrected)",
    "misprint_in_print", "high",
    fx("entraîne", "entraine"),
    "Missing circumflex (the typescript types its accents: même, être, binômial, polynôme). The TeX silently corrects; the fix restores the printed reading in the diplomatic layer.",
    corrected="entraîne")

add(330, "before 'Il est immédiat de vérifier qu'on obtient bien ainsi'",
    "'Il est immédiat' begins a new, indented paragraph after '... l'élément F - F' de K˙(X).' (both scans)",
    r"'de \(K^\bullet(X)\). Il est immédiat' (same paragraph)",
    "other", "high",
    fx(r"de \(K^\bullet(X)\). Il est immédiat", r"de \(K^\bullet(X)\).<NL><NL>Il est immédiat"),
    "Missing paragraph break.")

add(330, "last line of page_330.tex: the heading '3.10' (printed at the top of p. 331)",
    "'3.10  Soit A une K-λ-algèbre augmentée.': no stop after 3.10 (both scans; crops_326_330/c331_310.png from the main PDF, w331_310.png)",
    r"\textbf{3.10.}",
    "punctuation", "high",
    fx(r"\textbf{3.10.}", r"\textbf{3.10}"),
    r"Filed under p. 330 because the heading stands in page_330.tex now (see the folio-331 marker entry); the marker command's anchor '\textbf{3.10' works before or after this edit. The bold is the pending paragraph-number decision (not reported).")

add(330, "end of page (folio-331 marker)",
    "p. 330 ends '... C'est toujours de celle-ci qu'il sera question dans la suite.'; p. 331 begins '3.10  Soit A une K-λ-algèbre augmentée.' (both scans)",
    r"'\textbf{3.10.}' is the last line of page_330.tex, above the folio-331 marker",
    "marker", "high", None,
    r"Page 331 really begins with the heading '\textbf{3.10.}' (a heading at the top of a page, not moved by the 10 Nov script). "
    r"python -I move_marker.py 6 331 '\textbf{3.10' --before (anchor without the stop, so it works before or after the p. 330 punctuation entry; "
    r"simulated in memory on both layers with crops_326_330/sim_markers.py: '... dans la suite.' / blank / marker / '\textbf{3.10.}' / 'Soit \(A\) une ...'). "
    r"The checker of p. 331 may report the same boundary: apply once.")

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")

# ---------------------------------------------------------------- checks
ok = True
pages = {p: (BATCH / f"page_{p}.tex").read_text(encoding="utf-8") for p in range(326, 331)}
both = pages[327] + pages[328]
for i, d in enumerate(json.loads(OUT.read_text(encoding="utf-8"))):
    f = d["fix"]
    if f is None:
        continue
    t = pages[d["page"]]
    n = t.count(f["old"])
    marks = "%%%%%%%%%%" in f["old"] or "%%%%%%%%%%" in f["new"]
    extra = ""
    if d["page"] == 327 and "page_327.tex now" in d["note"]:
        extra = f" (pp. 327+328 together: {both.count(f['old'])})"
    if n != 1 or marks:
        ok = False
    print(i, d["page"], d["kind"], "count", n, extra, "MARKER!" if marks else "")
from collections import Counter
c = Counter((d["page"], d["kind"] == "misprint_in_print") for d in F)
for p in range(326, 331):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
print("ALL OK" if ok else "PROBLEM", len(F))
