"""Write findings_296_300.json and check that every fix's old string occurs exactly once in its page file.

Backslashes are written as BS (chr(92)) placeholders in the source strings below and expanded by X(), so that no
tool or shell layer can alter them."""
import json
import pathlib
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b296_300"
OUT = RUN / "findings_296_300.json"
BS = chr(92)


def X(s):
    """Expand the placeholder @ to one backslash."""
    return s.replace("@", BS)


F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": X(where), "scan": X(scan), "tex": X(tex), "kind": kind, "confidence": confidence,
         "fix": None if fix is None else {"old": X(fix[0]), "new": X(fix[1])}}
    if corrected is not None:
        d["corrected"] = X(corrected)
    d["note"] = X(note)
    F.append(d)


# ---------------- p. 296
add(296, "start of page",
    "p. 296 begins '(Bien entendu, pour X_i = Y_i = S, on retrouve ...'; p. 295 ends with the display "
    "K˙(f_1) ⊗ K˙(f_2) ⟶ K˙(f) . (both scans)",
    "the opening '(' stands alone on the last line of page 295's text, just above the folio-296 marker; "
    "page_296.tex begins 'Bien entendu'",
    "marker", "high", None,
    "Page 296 really begins with '('. Same finding as the p. 295 entry of findings_291_295.json: apply once. "
    "In both layers of main.tex replace '(@n%%%%%%%%%%  scan idx 309  |  folio 296  %%%%%%%%%%@nBien entendu' "
    "by '%%%%%%%%%%  scan idx 309  |  folio 296  %%%%%%%%%%@n(Bien entendu' (once in each layer): this moves the "
    "marker and joins the '(' to its word. python -I move_marker.py 6 296 \"(\" --before alone (simulated on both "
    "layers) leaves '(' on its own line, which prints '( Bien entendu'.")

add(296, "first line, '(Bien entendu, pour X_i = Y_i = S'",
    "X_i = Y_i = S: subscript i, a dotted i with a foot serif, unlike the flagged 1 of 'n ≥ 1' (both scans; "
    "witness clear, crops_296_300/w296_xi.png)",
    "@(X_1=Y_1=S@)",
    "symbol", "high",
    ("@(X_1=Y_1=S@)", "@(X_i=Y_i=S@)"),
    "Transcription error that changes the sense: with X_i = Y_i = S (i = 1, 2) the pairing K˙(f_1) ⊗ K.(f_2) → "
    "K.(f) of 3.3.3 gives the K˙(S)-module structure of K.(S); X_1 = Y_1 = S alone would give that of K.(f_2). "
    "The corrected layer has the same X_1=Y_1.")

add(296, "'K˙(S)-module de K.(S)', display 'K˙(X/S)^{⊗n} → K˙((X/S)^n)', 'sur K˙(X/S)'",
    "K with a raised round dot (K^•) in all four places; the apostrophe of 'd'anneau' on the same page is a "
    "vertical tick (both scans; crops_296_300/c296_kdot.png, c296_apos.png)",
    "K'(S), K'(X/S)^{@otimes n}, K'@bigl((X/S)^n@bigr), K'(X/S)",
    "symbol", "high", None,
    "Belongs to the Exposé IV convention already reported at p. 278 (findings_276_280.json: the raised-dot K "
    "written K' throughout Exposé IV, folios 278-296). Not itemized: one decision for the exposé. The lower-dot "
    "K_{@bullet}(S) is right.")

add(296, "heading of the bibliography",
    "BIBLIOGRAPHIE: typed capitals, underlined (both scans)",
    "@subsection*{Bibliographie}",
    "word", "medium",
    ("@subsection*{Bibliographie}", "@subsection*{BIBLIOGRAPHIE}"),
    "Typed in capitals, as the headings fixed on pp. 19, 159, 220 and 273 (findings_216_220, findings_271_275); "
    "the missing underline of a section title is accepted.")

add(296, "bibliography [2] Grauert, title",
    "'Ein Theorem der Analytischen Garbentheorie ...,' typed plain, not underlined (both scans)",
    "@emph{Ein Theorem der Analytischen Garbentheorie @dots}",
    "font", "high",
    ("@emph{Ein Theorem der Analytischen Garbentheorie @dots}", "Ein Theorem der Analytischen Garbentheorie @dots"),
    "The typescript neither underlines nor italicizes the titles of this bibliography; same fix as the "
    "bibliographies of pp. 19 and 159.")

add(296, "bibliography [3] Grothendieck, title",
    "'Théorèmes de finitude pour la cohomologie des faisceaux' typed plain, not underlined (both scans)",
    "@emph{Théorèmes de finitude pour la cohomologie des faisceaux}",
    "font", "high",
    ("@emph{Théorèmes de finitude pour la cohomologie des faisceaux}",
     "Théorèmes de finitude pour la cohomologie des faisceaux"),
    "As entry [2].")

add(296, "bibliography [V] Verdier, title",
    "'Catégories dérivées' typed plain, not underlined (both scans)",
    "@emph{Catégories dérivées}",
    "font", "high",
    ("@emph{Catégories dérivées}", "Catégories dérivées"),
    "As entry [2].")

# ---------------- p. 297
add(297, "heading of Exposé V",
    "three lines: 'Exposé V' (underlined, no full stop); 'GENERALITES SUR LES λ-ANNEAUX' (typed capitals, double "
    "underline); 'par P. BERTHELOT' (underlined) (both scans)",
    "@section*{Exposé V. Généralités sur les @(@lambda@)-anneaux}",
    "word", "medium",
    ("@section*{Exposé V. Généralités sur les @(@lambda@)-anneaux}",
     "@section*{@underline{Exposé V}@@[3pt] @underline{@underline{GÉNÉRALITÉS SUR LES @(@lambda@)-ANNEAUX}}}"),
    "The TeX joins the two lines with an added full stop and sets the title in small letters. Same form as the "
    "applied headings of Exposés II-IV (@section*{@underline{Exposé II}@@[3pt] @underline{@underline{...}}}); "
    "'Exposé V' is typed in small letters here, as 'Exposé II'; É keeps the TeX's accents (rule for typed "
    "capitals).")

add(297, "author line of the heading",
    "'par P. BERTHELOT': the name in capitals, the line underlined (both scans)",
    "par P. Berthelot",
    "word", "medium",
    ("par P. Berthelot", "@underline{par P. BERTHELOT}"),
    "As the applied author lines of Exposés I-IV (@underline{par L. ILLUSIE}).")

add(297, "second paragraph, 'le point de vue fonctoriel adopté ici à l'avantage'",
    "'adopté ici à l'avantage': a with a grave accent (both scans; crops_296_300/w297_top.png)",
    "adopté ici à l'avantage (printed reading kept)",
    "misprint_in_print", "high", None,
    "The verb avoir: 'le point de vue fonctoriel adopté ici a l'avantage, outre sa généralité, de réduire "
    "notablement les calculs'. The diplomatic TeX keeps the printed reading; the corrected layer still has "
    "'à l'avantage' too.",
    corrected="adopté ici a l'avantage")

# ---------------- p. 298
add(298, "start of page",
    "p. 298 begins 'abéliens, de la façon suivante : si A ∈ Ob(C)'; p. 297 ends '... à valeurs dans la catégorie "
    "des groupes' (both scans)",
    "'abéliens, de la' are the last words of the last line of page_297.tex (under the folio-297 marker); "
    "page_298.tex begins 'façon suivante'",
    "marker", "high", None,
    "Page 298 really begins with 'abéliens'. Move the folio-298 marker before it: python -I move_marker.py 6 298 "
    "\"abéliens, de la\" --before (simulated on both layers: '... dans la catégorie des groupes', the marker, "
    "'abéliens, de la', 'façon suivante : ...'; the output still reads 'groupes abéliens, de la façon').")

add(298, "'si ψ = a_o + a_1t + ... + a_nt^n + ... , alors'",
    "typed full stops on the baseline, twice (both scans)",
    "@psi=a_0+a_1t+@cdots+a_nt^n+@cdots",
    "symbol", "medium",
    ("@psi=a_0+a_1t+@cdots+a_nt^n+@cdots", "@psi=a_0+a_1t+@ldots+a_nt^n+@ldots"),
    "@cdots sets the dots at mid-height; the typescript has baseline stops (same kind of fix as pp. 49, 79, 80, "
    "86, 238, 251, 255).")

add(298, "display 'Ĝ_K : K-Alg.fil. → Ab .'",
    "'K-Alg.fil.' and 'Ab' each underlined (both scans)",
    "K@text{-Alg.fil.}@longrightarrow @mathrm{Ab}.",
    "underline", "high",
    ("K@text{-Alg.fil.}@longrightarrow @mathrm{Ab}.",
     "@underline{K@text{-Alg.fil.}}@longrightarrow @underline{@mathrm{Ab}}."),
    "Category names underlined in the typescript (the exposé writes @underline{@mathrm{Ens}} a few pages on). "
    "The subscript K-Alg.fil. of Hom in the display after Lemme 1.2 is not underlined in the print, and stays.")

add(298, "Lemme 1.2, 'Le foncteur Ĝ_K est représentable.'",
    "the statement underlined word group by word group: 'Le foncteur', 'est représentable' (both scans)",
    "the statement in roman",
    "underline", "high", None,
    "Exposé V continues the Exposé II-IV pattern of GLOBAL_ISSUES 82 (statements in roman where the typescript "
    "underlines their word groups): not itemized, for the scripted per-exposé decision. No @emph on defined "
    "terms and no category L on pp. 296-300.")

add(298, "'Soit (X_i)_{i∈N, i≥1}'",
    "an ordinary typewriter capital N (serifs, single strokes) with the hand-drawn ∈ touching its left stem "
    "(both scans; crops_296_300/c298_iN2.png, w298_iN.png)",
    "i@in@mathbb N,",
    "font", "low",
    ("i@in@mathbb N,", "i@in N,"),
    "The typist's plain letter for the double-struck N: the same open question as the typist's plain Q "
    "(NOTE_6; SGA 7 II issue 61). Apply only if the diplomatic layer reproduces it.")

add(298, "'en associant à toute série ψ = 1 + a_1t + ... + a_nt^n + ... ∈ Ĝ_K(A)'",
    "typed full stops on the baseline, twice (both scans)",
    "@psi=1+a_1t+@cdots+a_nt^n+@cdots@in",
    "symbol", "medium",
    ("@psi=1+a_1t+@cdots+a_nt^n+@cdots@in", "@psi=1+a_1t+@ldots+a_nt^n+@ldots@in"),
    "As the first series of the page (@cdots for baseline stops).")

add(298, "'On pose φ = 1 + X_1t + ... + X_nt^n + ... ;'",
    "typed full stops on the baseline, twice (both scans)",
    "@varphi=1+X_1t+@cdots+X_nt^n+@cdots",
    "symbol", "medium",
    ("@varphi=1+X_1t+@cdots+X_nt^n+@cdots", "@varphi=1+X_1t+@ldots+X_nt^n+@ldots"),
    "As the first series of the page.")

# ---------------- p. 299
add(299, "start of page",
    "p. 299 begins 'f_ψ de K[X_i]_{i≥1} dans A tel que'; p. 298 ends '... il existe un homomorphisme et un seul' "
    "(both scans)",
    "page_299.tex begins 'seul @(f_@psi@) de ...': 'seul', the last word of p. 298, stands under the folio-299 "
    "marker",
    "marker", "high", None,
    "Page 299 really begins with '@(f_@psi@) de'. Move the folio-299 marker down after 'seul': "
    "python -I move_marker.py 6 299 '@(f_@psi@) de' (without --before: the first occurrence after the marker; "
    "simulated on both layers: '... il existe un homomorphisme et un', 'seul', the marker, '@(f_@psi@) de "
    "@(K[X_i]_{i@geq 1}@) ...'; the output still reads 'et un seul f_ψ de').")

add(299, "1.3, 'une série ψ = 1 + a_1t + ... sera dite de filtration'",
    "typed full stops on the baseline (both scans)",
    "@psi=1+a_1t+@cdots@)",
    "symbol", "medium",
    ("@psi=1+a_1t+@cdots@)", "@psi=1+a_1t+@ldots@)"),
    "@cdots for baseline stops, as on p. 298.")

add(299, "1.3, 'dans la catégorie Ab.fil. des groupes abéliens filtrés'",
    "'Ab.fil.': Ab and fil each underlined, a full stop after each (both scans; crops_296_300/c299_abfil1.png)",
    "@(@Abfil@) (macro @mathrm{Ab@,fil}, defined in the Exposé V macro block at the end of page_296.tex)",
    "underline", "high",
    ("catégorie @(@Abfil@) des", "catégorie @(@underline{@mathrm{Ab}}.@underline{@mathrm{fil}}.@) des"),
    "The macro prints 'Ab fil' without the underlines and without the two stops. @Abfil has 15 uses in Exposé V: "
    "if the print underlines them all, changing the macro to @underline{@mathrm{Ab}}@,@underline{@mathrm{fil}} "
    "would replace the next fix (the stops of this place would still need this edit).")

add(299, "'Soit H un foncteur sur C à valeurs dans Ab fil ; nous supposerons'",
    "'Ab fil': Ab and fil each underlined, no stops (both scans; crops_296_300/c299_abfil2.png)",
    "@(@Abfil@)~;",
    "underline", "high",
    ("dans @(@Abfil@)~;", "dans @(@underline{@mathrm{Ab}}@,@underline{@mathrm{fil}}@)~;"),
    "As the previous entry (no stops at this place).")

add(299, "condition ii), 'alors H(A^G) ⥲ H(A)^G'",
    "a tilde over a short arrow with a head (isomorphism arrow), not the headless ≃ (both scans; "
    "crops_296_300/c299_iso.png, w299_iso.png)",
    "H(A^G)@simeq H(A)^G",
    "symbol", "high",
    ("H(A^G)@simeq H(A)^G", "H(A^G)@xrightarrow{@sim} H(A)^G"),
    "Same arrow as the bijection of p. 298 (@xrightarrow{@sim} there). The first sign of the display of 1.5 "
    "(p. 300) is headless and stays @simeq.")

add(299, "end of condition ii), '(l'exposant G désignant les invariants sous G)'",
    "no full stop after the closing parenthesis (both scans; crops_296_300/c299_sousG.png, w299_sousG.png)",
    "@text{(l'exposant }G@text{ désignant les invariants sous }G@text{).}",
    "punctuation", "high",
    ("sous }G@text{).}", "sous }G@text{)}"),
    "The TeX adds a full stop.")

# ---------------- p. 300
add(300, "first paragraph, 'et nous permettra d'identifier le permier à un sous-groupe du second'",
    "'le permier' (both scans; crops_296_300/w300_permier.png)",
    "le permier (printed reading kept)",
    "misprint_in_print", "high", None,
    "Transposed letters. The diplomatic TeX keeps the printed reading; the corrected layer has 'premier'.",
    corrected="le premier")

add(300, "display of 1.5, end",
    "'... ⊂ H(K[T_1,...,T_n])' with no punctuation (both scans; crops_296_300/w300_dispend.png)",
    "@subset H(K[T_1,@ldots,T_n]).",
    "punctuation", "high",
    ("@subset H(K[T_1,@ldots,T_n]).", "@subset H(K[T_1,@ldots,T_n])"),
    "The TeX adds a full stop at the end of the display.")

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

# checks
ok = True
for d in F:
    fx = d["fix"]
    if fx is None:
        continue
    t = (B / f"page_{d['page']}.tex").read_text(encoding="utf-8")
    n = t.count(fx["old"])
    if n != 1 or "%%%%%%%%%%" in fx["old"]:
        ok = False
    print(d["page"], n, fx["old"][:70], " -> ", fx["new"][:80])
c = Counter()
for d in F:
    c[(d["page"], d["kind"] == "misprint_in_print")] += 1
for p in range(296, 301):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
print("all unique:", ok, "entries:", len(F))
json.loads(OUT.read_text(encoding="utf-8"))
