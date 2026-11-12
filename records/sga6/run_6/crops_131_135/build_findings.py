"""Build, check and write findings_131_135.json (olds unique in the original page files; JSON-order replay)."""
import json
import pathlib

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
PAGES = RUN / "b131_135"
OUT = RUN / "findings_131_135.json"


def nl(s):
    return None if s is None else s.replace("<NL>", "\n")


def F(page, where, scan, tex, kind, confidence, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": confidence,
         "fix": None if old is None else {"old": nl(old), "new": nl(new)}}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    return d


L = []

# ---------------- page 131 ----------------
L.append(F(131, "Proposition 5.1, opening sentence",
           "Soient (S,A) un topos annelé, ... tels que m<n. Conditions équivalentes : (word groups underlined)",
           "statement in roman",
           "underline", "high",
           r"Soient \((S,A)\) un topos annelé, \(X\in\Ob S\), \(F\in\Ob\Dpx^-({}_A X)\), \(m,n\in\mathbb Z\) tels que \(m<n\). Conditions équivalentes :",
           r"\emph{Soient \((S,A)\) un topos annelé, \(X\in\Ob S\), \(F\in\Ob\Dpx^-({}_A X)\), \(m,n\in\mathbb Z\) tels que \(m<n\). Conditions équivalentes} :",
           "Statement of a proposition in roman (Lemme 5.1.1 on the same page is in \\emph). The colon stays in roman."))
L.append(F(131, "Proposition 5.1 (i)",
           "est isomorphe, dans, à un complexe, tel que, soit plat pour tout, et nul pour: underlined",
           "item in roman",
           "underline", "high",
           r"\item \(F\) est isomorphe, dans \(\Dpx^-({}_A X)\), à un complexe \(F'\) tel que \(F'^i\) soit plat pour tout \(i\) et nul pour \(i\notin[m,n]\);",
           r"\item \emph{\(F\) est isomorphe, dans \(\Dpx^-({}_A X)\), à un complexe \(F'\) tel que \(F'^i\) soit plat pour tout \(i\) et nul pour \(i\notin[m,n]\)};",
           "Part of the statement of 5.1 (file form: \\item \\emph{...})."))
L.append(F(131, "Proposition 5.1 (ii)",
           "pour tout, -Module à droite, on a, pour: underlined",
           "item in roman",
           "underline", "high",
           r"\item pour tout \(A_X\)-Module à droite \(E\), on a \(\Ho^i(E\overset{\mathrm L}{\otimes}_A F)=0\) pour \(i\notin[m,n]\).",
           r"\item \emph{pour tout \(A_X\)-Module à droite \(E\), on a \(\Ho^i(E\overset{\mathrm L}{\otimes}_A F)=0\) pour \(i\notin[m,n]\)}.",
           "Part of the statement of 5.1. Apply before the next entry (this old contains \\Ho^i; JSON order)."))
L.append(F(131, "Proposition 5.1 (ii), cohomology sheaf",
           "H̲^i(E ⊗^L_A F) (the H underlined on its own)",
           r"\Ho^i (\Ho = \mathrm H)",
           "underline", "high",
           r"\Ho^i(E\overset",
           r"\underline{\Ho}^i(E\overset",
           "The print's underlined H of the cohomology sheaf; the TeX has no underlined H anywhere in Exposé I. (The plain H^i of the abstract S-category on p. 128 is right as \\Ho.)"))
L.append(F(131, "after the triangle of Lemme 5.1.1's proof",
           "comma after the diagram (right of F)",
           "no punctuation",
           "punctuation", "high",
           r"&& F \arrow[ul]<NL>\end{tikzcd}",
           r"&& F \arrow[ul] & ,<NL>\end{tikzcd}",
           "Same form as the punctuation added after the triangles of pp. 98-99."))
L.append(F(131, "Proposition 5.1 '(S,A)', 'X ∈ ob S' (and pp. 132-135)",
           "S̲ underlined (the topos)",
           "plain S",
           "underline", "high",
           None, None,
           "Convention of the transcription, as reported for pp. 84-85, 93-95 and 100: the print underlines the topos letter S̲ "
           "(here also p. 132 D⁻(_A S̲), 'ob S̲', 'sous-S̲-catégorie'; p. 133 S̲_{/X}, S̲'; p. 134 (S̲',A'), (S̲,A); p. 135 'anneau de S̲' "
           "and both footnotes), the TeX writes plain S. One decision for the exposé, not a page fix."))

# ---------------- page 132 ----------------
L.append(F(132, "Définition 5.2, first sentence",
           "Un objet, de, satisfaisant aux conditions équivalentes, de, sera dit d', contenue dans l'intervalle, et nous écrirons: "
           "underlined; 'amplitude plate' (the defined term) not underlined",
           "statement in roman",
           "underline", "high",
           r"Un objet \(F\) de \(\Dpx^-({}_A S)\) satisfaisant aux conditions équivalentes de (5.1) sera dit d'amplitude plate contenue dans l'intervalle \([m,n]\), et nous écrirons",
           r"\emph{Un objet \(F\) de \(\Dpx^-({}_A S)\) satisfaisant aux conditions équivalentes de (5.1) sera dit d'}amplitude plate \emph{contenue dans l'intervalle \([m,n]\), et nous écrirons}",
           "Statement of a definition in roman; the defined term is left out of the underline (as Définitions 1.4.3 and 2.1)."))
L.append(F(132, "Définition 5.2, last sentence",
           "Nous dirons que ... soit vérifiée. (word groups underlined, the underline runs under the full stop)",
           "in roman",
           "underline", "high",
           r"Nous dirons que \(F\) est d'amplitude plate finie (ou de tor-dimension finie) s'il existe des entiers \(m\) et \(n\) tels que la condition précédente soit vérifiée.",
           r"\emph{Nous dirons que \(F\) est d'amplitude plate finie (ou de tor-dimension finie) s'il existe des entiers \(m\) et \(n\) tels que la condition précédente soit vérifiée.}",
           "Part of the definition; here the print underlines 'amplitude plate finie' too."))

# ---------------- page 133 ----------------
L.append(F(133, "top of the page",
           "the page begins with the heading '5.5. Soient X ∈ ob S̲, ...'",
           r"\textbf{5.5.} stands above the folio-133 marker (last line of page_132.tex)",
           "marker", "high",
           None, None,
           "Page 133 really begins with \\textbf{5.5.} (p. 132 ends with 'A-Modules plats.'). Move the marker above the heading: "
           "python -I move_marker.py 6 133 '\\textbf{5.5.}' --before (dry run: anchor found in both layers). A heading at the top of a page, "
           "which the 10 Nov script did not move."))
L.append(F(133, "5.5, 'si S/X est de type fini'",
           "S̲_{/X}: '/X' lowered as an index (both scans)",
           "S/X on the line",
           "formula", "high",
           r"si \(S/X\) est",
           r"si \(S_{/X}\) est",
           "The localized topos, written \\(S_{/X}\\) elsewhere in the TeX (main.tex line 3215); as the \\Ob S_{/S} fix of p. 90."))
L.append(F(133, "Corollaire 5.6.1 a), first formula",
           "'Le foncteur 𝕃f* : D⁻(_AS̲) → D⁻(_{A'}S̲') induit un' in the text line",
           "set as a display",
           "other", "medium",
           r"Le foncteur<NL>\[<NL>  \mathrm L f^*:\Dpx^-({}_A S)\longrightarrow \Dpx^-({}_A, S')<NL>\]<NL>induit",
           r"Le foncteur \(\mathrm L f^*:\Dpx^-({}_A S)\longrightarrow \Dpx^-({}_A, S')\) induit",
           "The print sets the functor inline; the TeX makes it a display (same kind of fix as pp. 21, 34-35, 42, 80). "
           "The formula is left unchanged here: apply before the \\emph, 𝕃 and A' entries of this corollary (JSON order)."))
L.append(F(133, "Corollaire 5.6.1 b), first formula",
           "'le foncteur ⊗^L_A : D⁻(S̲) x_S̲ D⁻(S̲) → D⁻(S̲) induit un' in the text line",
           "set as a display",
           "other", "medium",
           r"le foncteur<NL>\[<NL>  \overset{\mathrm L}{\otimes}_A:<NL>  \Dpx^-(S)\times_S\Dpx^-(S)<NL>  \longrightarrow \Dpx^-(S)<NL>\]<NL>induit",
           r"le foncteur \(\overset{\mathrm L}{\otimes}_A:\Dpx^-(S)\times_S\Dpx^-(S)\longrightarrow \Dpx^-(S)\) induit",
           "As a). Apply before the \\emph entries of b) (JSON order)."))
L.append(F(133, "Corollaire 5.6.1 a), 'Le foncteur'",
           "Le foncteur: underlined",
           "statement in roman",
           "underline", "high",
           r"\textbf{a)} Le foncteur",
           r"\textbf{a)} \emph{Le foncteur}",
           "The corollary's statement is in roman; the print underlines 'Le foncteur', 'induit un foncteur' (a) and 'Si', 'est commutatif,', "
           "'le foncteur', 'induit un foncteur' (b), not the formulas. Apply after the inline entry for a) (JSON order)."))
L.append(F(133, "Corollaire 5.6.1 a), 'induit un foncteur'",
           "induit un / foncteur: underlined",
           "roman",
           "underline", "high",
           r"induit un foncteur<NL>\[<NL>  \mathrm L",
           r"\emph{induit un foncteur}<NL>\[<NL>  \mathrm L",
           "After the inline entry for a), before the 𝕃 entry of the second display (JSON order)."))
L.append(F(133, "Corollaire 5.6.1 b), 'Si A est commutatif, le foncteur'",
           "Si, est commutatif,, le foncteur: underlined",
           "roman",
           "underline", "high",
           r"\textbf{b)} Si \(A\) est commutatif, le foncteur",
           r"\textbf{b)} \emph{Si \(A\) est commutatif, le foncteur}",
           "After the inline entry for b) (JSON order)."))
L.append(F(133, "Corollaire 5.6.1 b), 'induit un foncteur'",
           "induit un / foncteur: underlined",
           "roman",
           "underline", "high",
           r"induit un foncteur<NL>\[<NL>  \overset",
           r"\emph{induit un foncteur}<NL>\[<NL>  \overset",
           "After the inline entry for b) (JSON order)."))
L.append(F(133, "Corollaire 5.6.1 a), first formula, 𝕃f*",
           "heavy inked L (𝕃), the gap of the double stroke filled",
           r"\mathrm L",
           "font", "medium",
           r"\mathrm L f^*:\Dpx^-",
           r"\mathbb L f^*:\Dpx^-",
           "The same symbol is clearly double-struck in the display below; medium because this one could be read as bold. "
           "After the inline entry for a) (JSON order)."))
L.append(F(133, "Corollaire 5.6.1 a), second display, 𝕃f*",
           "double-struck 𝕃 (both scans)",
           r"\mathrm L",
           "font", "high",
           r"\mathrm L f^*:\Dpx({}",
           r"\mathbb L f^*:\Dpx({}",
           "After the 'induit un foncteur' entry of a) (JSON order)."))
L.append(F(133, "Proposition 5.6, 'en tant qu'objet de D⁻(_{A'}S̲')'",
           "left index A' (a prime, like the one on S̲')",
           r"{}_A, (a comma)",
           "symbol", "high",
           r"objet de \(\Dpx^-({}_A,",
           r"objet de \(\Dpx^-({}_{A'}",
           "The ring A' of S' (2.16 defines D(_{A'}S'_A)); the mark sits at the top of the lowered A in both scans, the shape of the prime of S'. "
           "The TeX reads it as a comma, also on pp. 129-130 (see the message)."))
L.append(F(133, "Corollaire 5.6.1 a), first formula, target",
           "D⁻(_{A'}S̲')",
           r"\Dpx^-({}_A, S')",
           "symbol", "high",
           r"\longrightarrow \Dpx^-({}_A,",
           r"\longrightarrow \Dpx^-({}_{A'}",
           "As in 5.6. After the inline entry for a) (its old contains this text; JSON order)."))
L.append(F(133, "Corollaire 5.6.1 a), second display, target",
           "D(_{A'}S̲')_torf",
           r"\Dpx({}_A, S')_{\torf}",
           "symbol", "high",
           r"\longrightarrow \Dpx({}_A,",
           r"\longrightarrow \Dpx({}_{A'}",
           "As in 5.6."))

# ---------------- page 134 ----------------
L.append(F(134, "Exercices 5.7 b), first ℝHom̲ formula",
           "'ℝHom̲ : D(S)° x D⁺(S) → D(S) induit un foncteur' as a line of text (flush left, the sentence goes on)",
           "set as a display",
           "other", "medium",
           r"le foncteur<NL>\[<NL>  \mathrm R\Hom:\Dpx(S)^\circ\times\Dpx^+(S)\longrightarrow \Dpx(S)<NL>\]<NL>induit",
           r"le foncteur \(\mathrm R\Hom:\Dpx(S)^\circ\times\Dpx^+(S)\longrightarrow \Dpx(S)\) induit",
           "The print sets the formula inline; the TeX makes it a display. The formula is left unchanged here: apply before the ℝ and Hom̲ entries (JSON order)."))
L.append(F(134, "Exercices 5.7 b), first ℝHom̲",
           "double-struck ℝ",
           r"\mathrm R",
           "font", "high",
           r"\mathrm R\Hom:\Dpx(S)^\circ\times",
           r"\mathbb R\Hom:\Dpx(S)^\circ\times",
           "As the ℝ of p. 83. After the inline entry; before the Hom̲ entry (JSON order)."))
L.append(F(134, "Exercices 5.7 b), first ℝHom̲",
           "Hom underlined (Hom̲)",
           r"\Hom",
           "underline", "high",
           r"\Hom:\Dpx(S)^\circ\times",
           r"\underline{\Hom}:\Dpx(S)^\circ\times",
           "The file writes the sheaf Hom \\underline{\\Hom} elsewhere (6 times in Exposé I). After the ℝ entry (JSON order)."))
L.append(F(134, "Exercices 5.7 b), second ℝHom̲ (display)",
           "double-struck ℝ",
           r"\mathrm R",
           "font", "high",
           r"\mathrm R\Hom:\Dpx(S)^\circ_",
           r"\mathbb R\Hom:\Dpx(S)^\circ_",
           "Before the next entry (JSON order)."))
L.append(F(134, "Exercices 5.7 b), second ℝHom̲ (display)",
           "Hom underlined (Hom̲)",
           r"\Hom",
           "underline", "high",
           r"\Hom:\Dpx(S)^\circ_",
           r"\underline{\Hom}:\Dpx(S)^\circ_",
           "After the previous entry (JSON order)."))
L.append(F(134, "Théorème 5.8, opening sentence",
           "Soient, un topos annelé,, avec, Conditions équivalentes: underlined",
           "statement in roman",
           "underline", "high",
           r"Soient \((S,A)\) un topos annelé, \(E\in\Ob\Dpx({}_A S)\), \(m,n\in\mathbb Z\), avec \(m\leq n\). Conditions équivalentes :",
           r"\emph{Soient \((S,A)\) un topos annelé, \(E\in\Ob\Dpx({}_A S)\), \(m,n\in\mathbb Z\), avec \(m\leq n\). Conditions équivalentes} :",
           "Statement of a theorem in roman. (i) is a formula only, not underlined."))
L.append(F(134, "Théorème 5.8 (ii)",
           "est, pseudo-cohérent, et l'on a: underlined; the references (2.15), (5.2) not",
           "item in roman",
           "underline", "high",
           r"\item \(E\) est \((m-1)\)-pseudo-cohérent (2.15) et l'on a \(\toramp(E)\subset[m,n]\) (5.2).",
           r"\item \emph{\(E\) est \((m-1)\)-pseudo-cohérent} (2.15) \emph{et l'on a \(\toramp(E)\subset[m,n]\)} (5.2).",
           "Part of the statement of 5.8; the references stay in roman."))
L.append(F(134, "after Théorème 5.8, 'Comme « parfait » ... on en déduit :'",
           "Comme, parfait, implique évidemment, pseudo-cohérent, on en déduit: underlined",
           "in roman",
           "underline", "high",
           r"Comme « parfait » implique évidemment « pseudo-cohérent », on en déduit :",
           r"\emph{Comme « parfait » implique évidemment « pseudo-cohérent », on en déduit} :",
           "The lead-in to Corollaire 5.8.1 is underlined in the print (the quotes themselves are not)."))
L.append(F(134, "Théorème 5.8 (i), 'parf.amp(E)'",
           "parf.amp",
           r"\perfamp, defined as \operatorname{perf.amp}",
           "word", "high",
           None, None,
           "Convention of the transcription (the macro): main.tex line 2852 \\providecommand{\\perfamp}{\\operatorname{perf.amp}} and line 2853 "
           "\\perfdim = perf.dim, where the print types parf.amp and parf.dim (p. 128: parf.amp four times, parf.dim; p. 130 Remarque 4.19.2; "
           "OCR of pp. 121-130, 137, 149 likewise). Change the two definitions to parf.amp / parf.dim (16 + 4 uses); the later exposés already "
           "define \\pamp / \\parfamp as parf.amp."))

# ---------------- page 135 ----------------
L.append(F(135, "Corollaire 5.8.1, reference to the definition of pseudo-coherence",
           "(2,15) with a comma (both scans)",
           "(2.15)",
           "misprint_in_print", "high",
           r"(2.15)",
           r"(2,15)",
           "Typing slip of the print for (2.15); the TeX silently corrects it. Diplomatic: restore the printed comma.",
           corrected=r"(2.15)"))
L.append(F(135, "Lemme 5.8.2, statement before (5.8.2.1)",
           "Soit, un anneau de, Si, est un, -Module à gauche, un, -Module à droite, et, un, -Bimodule, (à gauche sur, à droite sur, "
           "il existe un homomorphisme canonique fonctoriel: underlined",
           "statement in roman",
           "underline", "high",
           r"Soit \(B\) un anneau de \(S\). Si \(E\) est un \(A\)-Module à gauche, \(G\) un \(B\)-Module à droite, et \(F\) un \(A\)-\(B\)-Bimodule (à gauche sur \(A\), à droite sur \(B\)), il existe un homomorphisme canonique fonctoriel",
           r"\emph{Soit \(B\) un anneau de \(S\). Si \(E\) est un \(A\)-Module à gauche, \(G\) un \(B\)-Module à droite, et \(F\) un \(A\)-\(B\)-Bimodule (à gauche sur \(A\), à droite sur \(B\)), il existe un homomorphisme canonique fonctoriel}",
           "Statement of a lemma in roman."))
L.append(F(135, "Lemme 5.8.2, after (5.8.2.1)",
           "Celui-ci est un isomorphisme pour, injectif et, de présentation finie: underlined",
           "in roman",
           "underline", "high",
           r"Celui-ci est un isomorphisme pour \(G\) injectif et \(E\) de présentation finie.",
           r"\emph{Celui-ci est un isomorphisme pour \(G\) injectif et \(E\) de présentation finie}.",
           "Second part of the statement of 5.8.2."))
L.append(F(135, "(5.8.2.1)",
           "Hom̲_B(F,G) ⊗_A E → Hom̲_B(Hom̲_A(E,F),G): the three Hom underlined",
           r"\Hom (three times)",
           "underline", "high",
           r"\Hom_B(F,G)\otimes_A E<NL>  \longrightarrow<NL>  \Hom_B(\Hom_A(E,F),G).",
           r"\underline{\Hom}_B(F,G)\otimes_A E<NL>  \longrightarrow<NL>  \underline{\Hom}_B(\underline{\Hom}_A(E,F),G).",
           "Sheaf Hom, underlined in the print (as \\underline{\\Hom} elsewhere in the file)."))
L.append(F(135, "(*)",
           "Hom̲_B(F,G) ⊗_A E ⊗_{ℤ_S} Hom̲_A(E,F): both Hom underlined",
           r"\Hom (twice)",
           "underline", "high",
           r"\Hom_B(F,G)\otimes_A E\otimes_{\mathbb Z_S}\Hom_A(E,F)",
           r"\underline{\Hom}_B(F,G)\otimes_A E\otimes_{\mathbb Z_S}\underline{\Hom}_A(E,F)",
           ""))
L.append(F(135, "(*), end",
           "G (¹) . : footnote call, then the full stop",
           "full stop, then the footnote call",
           "punctuation", "medium",
           r"G.\text{\footnotemark}",
           r"G\text{\footnotemark}.",
           ""))
L.append(F(135, "(**)",
           "Hom̲_A(E,F) underlined",
           r"\Hom_A",
           "underline", "high",
           r"\Hom_A(E,F)<NL>  \longrightarrow F",
           r"\underline{\Hom}_A(E,F)<NL>  \longrightarrow F",
           ""))
L.append(F(135, "'(provenant ... de la flèche identique de Hom̲_A(E,F))'",
           "Hom̲_A(E,F) underlined",
           r"\Hom_A",
           "underline", "high",
           r"identique de \(\Hom_A",
           r"identique de \(\underline{\Hom}_A",
           ""))
L.append(F(135, "(***)",
           "Hom̲_B(F,G) underlined",
           r"\Hom_B",
           "underline", "high",
           r"\Hom_B(F,G)\otimes_A F",
           r"\underline{\Hom}_B(F,G)\otimes_A F",
           ""))

# ---------------- checks ----------------
ok = True
texts = {p: (PAGES / f"page_{p}.tex").read_text(encoding="utf-8") for p in range(131, 136)}
for i, d in enumerate(L):
    fx = d["fix"]
    if fx is None:
        continue
    n = texts[d["page"]].count(fx["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE in original:", i, d["page"], n, repr(fx["old"][:60]))
    if "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]:
        ok = False
        print("touches a marker line:", i)
    if fx["old"] == fx["new"]:
        ok = False
        print("no change:", i)
# JSON-order replay
cur = dict(texts)
for i, d in enumerate(L):
    fx = d["fix"]
    if fx is None:
        continue
    n = cur[d["page"]].count(fx["old"])
    if n != 1:
        ok = False
        print("REPLAY fails:", i, d["page"], n, repr(fx["old"][:60]))
        continue
    cur[d["page"]] = cur[d["page"]].replace(fx["old"], fx["new"], 1)
# brace balance of each fix and of the replayed pages
for i, d in enumerate(L):
    fx = d["fix"]
    if fx is None:
        continue
    for k in ("old", "new"):
        s = fx[k].replace("\\{", "").replace("\\}", "")
        if s.count("{") != s.count("}") and k == "new":
            print("brace imbalance in new:", i, d["page"])
for p in cur:
    s = cur[p].replace("\\{", "").replace("\\}", "")
    print(p, "braces", s.count("{"), s.count("}"), "\\( \\)", cur[p].count("\\("), cur[p].count("\\)"))
counts = {}
for d in L:
    k = "misprint" if d["kind"] == "misprint_in_print" else "normal"
    counts.setdefault(d["page"], {"normal": 0, "misprint": 0})[k] += 1
print(counts)
print("OK" if ok else "PROBLEMS")
if ok and "--write" in __import__("sys").argv:
    OUT.write_text(json.dumps(L, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("written", OUT)
if "--show" in __import__("sys").argv:
    for p in (131, 132, 135):
        print("=" * 30, p)
        print(cur[p])
