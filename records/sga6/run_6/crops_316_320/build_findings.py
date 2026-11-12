"""Build findings_316_320.json; check that every fix's old occurs exactly once in its page file (in the text left by
the fixes listed before it on the same page) and that applying the page's fixes in order succeeds."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b316_320"
OUT = RUN / "findings_316_320.json"
NL = "\u23ce"  # placeholder for a line break in old/new


def fx(old, new):
    return {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}


F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- p. 316
add(316, "page start: 'F^pΛ^n(E) = Λ^n(E), et si p < 0, F^pΛ^n(E) = 0. Ceci définit bien une filtration finie sur Λ^n(E).'",
    "the page's first line is running text at the left margin, continued on the same line by 'Ceci définit bien une filtra-'; p. 315 ends with the one-line display 'Λ^{n-p}(E')⊗_AΛ^p(E) → Λ^n(E)  pour 0 ≤ p ≤ n ; si p ≥ n ,' (both scans)",
    r"the second line of a gathered display opened on p. 315 (its first line ends '\text{si } p\geq n,\\' just above the folio-316 marker), closed by \end{gathered} \] before 'Ceci définit'",
    "other", "medium",
    fx(r"  F^p\Lambda^n(E)=\Lambda^n(E),\quad \text{et si } p<0,\quad F^p\Lambda^n(E)=0.⏎\end{gathered}⏎\]⏎Ceci définit",
       r"\(F^p\Lambda^n(E)=\Lambda^n(E)\), et si \(p<0\), \(F^p\Lambda^n(E)=0\). Ceci définit"),
    r"APPLY TOGETHER with its p. 315 half, which lies above the marker: in both layers of main.tex replace '\text{si } p\geq n,\\\n%%%%%%%%%%  scan idx 329  |  folio 316  %%%%%%%%%%' by '\text{si } p\geq n,\n\end{gathered}\n\]\n%%%%%%%%%%  scan idx 329  |  folio 316  %%%%%%%%%%' (once in each layer). Simulated on both layers with this page's edit: the display closes on p. 315 and p. 316 opens with the sentence in the running text, same paragraph. Either half alone breaks the gathered environment.")

add(316, "'Dans le cas ou E', E, E'' sont localement facteurs directs'",
    "ou, without the grave accent (both scans)",
    "Dans le cas ou",
    "misprint_in_print", "high", None,
    "The TeX keeps the printed reading; the corrected layer also still reads 'ou'.",
    corrected="Dans le cas où")

add(316, "'f : (T,A) → (T',A') un morphisme de topos annelés', the second A'",
    "(T',A!): after the underlined A an exclamation mark (a tapering stroke with a dot at its foot, taller than the primes of T' on the same line and of (T',A') on the line above); clear in the witness, the lower part fainter in the main scan (crops_316_320/c316_Aprime2.png, w316_Aprime.png)",
    r"\longrightarrow(T',A')\)",
    "misprint_in_print", "medium",
    fx(r"\longrightarrow(T',A')\) un morphisme", r"\longrightarrow(T',A!)\) un morphisme"),
    "The typist struck '!' for the prime; the TeX silently corrects. The diplomatic layer keeps A! as printed.",
    corrected=r"\longrightarrow(T',A')\) un morphisme")

add(316, "'Signalons deux cas particuliers :', the list markers (pp. 316-317)",
    "each item begins with a typed hyphen: '- Soit X un schéma ;' (p. 316), '- Soit A un anneau' (p. 317) (both scans)",
    r"\begin{itemize} with the default label (a bullet)",
    "symbol", "medium",
    fx(r"\begin{itemize}", r"\begin{itemize}[label=-]"),
    r"main.tex writes the typed hyphen of a list as \begin{itemize}[label=-] (Exemples 3.6 of Exposé I, line 2611, after the p. 116 fix).")

add(316, "'c'est ce cas qui servira dans la suite du séminaire'",
    "c'èst: a thin accent stroke over the e in both scans (grave-like in the main scan, a small tick in the witness), smaller and lighter than the typed accents of 'pré' and 'modèle' on the same lines (crops_316_320/c316_cest3.png, w316_cest2.png)",
    "c'est",
    "misprint_in_print", "low",
    fx("c'est ce cas", "c'èst ce cas"),
    "If the mark is what remains of an accent the typist erased, the TeX's c'est stands and this entry is to be dropped; the size of the mark leaves that open.",
    corrected="c'est ce cas")

add(316, "Module letters and the ring of the topos, pp. 316 and 320 (convention of the Exposé V transcription, reported once)",
    "E, E', E'', F (Modules) and A (the ring of the ringed topos) are underlined, the underline under the letter only, the primes after it: p. 316 'F^pΛ^n(E̲) = Λ^n(E̲)', 'Dans le cas ou E̲', E̲, E̲''', '(T,A̲), (T',A̲') deux topos'; p. 320 'pour tous A-Modules E̲, F̲', 'au cas où E̲ et F̲ sont des modules inversibles' (both scans). Left plain in the print: the classes in K (λ^n(E), λ^{n-p}(E').λ^p(E'') on p. 316, the display λ_t(EF) = ... on p. 320), the index A of ⊗_A, the A of 'A-Modules', and (T,A) on p. 317",
    "plain E, E', E'', F, A",
    "underline", "high", None,
    r"Not itemized: 24 places on p. 316 (every Λ^n(E), Λ^p(E'), Λ^q(E''), Gr^pΛ^n(E), F^pΛ^n(E), E', E, E'', x''_i de E'', and the six A of (T,A), (T',A')), 4 on p. 320. One decision for Exposé V: \underline{E}', \underline{E}'', \underline{F}, \underline{A} where the print underlines; not a blind replacement, since the K-classes and the displays keep plain letters. Exposé 0 already writes the underlined Module as \underline E (p. 6).")

# ---------------------------------------------------------------- p. 317
add(317, "page start",
    "p. 317 begins 'λ-anneaux.' and then the second item '- Soit A un anneau, X = Spec A ; ...'; p. 316 ends '... considéré comme \"modèle\" pour la théorie générale des' (both scans)",
    r"'\(\lambda\)-anneaux.' ends the first \item line of page_316.tex and the second '\item' stands alone on the line above the folio-317 marker; page_317.tex begins 'Soit \(A\) un anneau'",
    "marker", "high", None,
    r"Page 317 really begins with '\(\lambda\)-anneaux.'. Exact fix in main.tex (both layers, once each): replace 'pour la théorie générale des \(\lambda\)-anneaux.\n\item\n%%%%%%%%%%  scan idx 330  |  folio 317  %%%%%%%%%%\nSoit \(A\)' by 'pour la théorie générale des\n%%%%%%%%%%  scan idx 330  |  folio 317  %%%%%%%%%%\n\(\lambda\)-anneaux.\n\item\nSoit \(A\)' (simulated on both layers; the line end after 'des' keeps the space). Equivalent: python -I move_marker.py 6 317 '\(\lambda\)-anneaux.' --before.")

add(317, "'On définit d'abord la multiplication en se donnant un morphisme de Z-bilinéaire de foncteurs'",
    "'un morphisme de' at the end of the line, 'ℤ-bilinéaire de foncteurs' on the next (both scans)",
    r"un morphisme de \(\mathbb Z\)-bilinéaire de foncteurs",
    "misprint_in_print", "medium", None,
    "A stray 'de' at the line end: the morphism Ĝ x Ĝ → Ĝ is Z-bilinear. The TeX keeps the printed reading; the corrected layer also.",
    corrected=r"un morphisme \(\mathbb Z\)-bilinéaire de foncteurs")

add(317, "same sentence, 'par élément 1+XYt de Ĝ(Z[X,Y])'",
    "par élément 1+XYt, without article (both scans)",
    r"par élément \(1+XYt\)",
    "misprint_in_print", "low", None,
    "The exposé writes 'déterminés par l'élément Φ(...)' in §1 (main.tex line 7577). The TeX keeps the printed reading; the corrected layer also.",
    corrected=r"par l'élément \(1+XYt\)")

add(317, "second diagram after 'associative et commutative par les diagrammes :', lower horizontal arrow",
    "the label Id stands above the lower arrow Ĝ → Ĝ, at its head (both scans; crops_316_320/c317_diag2.png, w317_id.png)",
    "\\arrow[r,\"\\id\"'] (label set below the arrow)",
    "formula", "medium",
    fx("\\arrow[r,\"\\id\"']", "\\arrow[r,\"\\id\"]"),
    r"Label on the wrong side of the arrow; \id prints Id in Exposé V (\renewcommand at main.tex line 7187), as printed. Apply before the next entry.")

add(317, "same label",
    "Id: a typed colon after Id, two dots one above the other right of the d (both scans; crops_316_320/c317_id.png, w317_id.png)",
    r"\id, no colon",
    "misprint_in_print", "low",
    fx("\\id\"", "\\id:\""),
    "A stray colon in the label; the TeX drops it silently. The old string is in the text the previous entry leaves (and also before it); the corrected layer takes only the previous entry.",
    corrected="\\arrow[r,\"\\id\"]")

# ---------------------------------------------------------------- p. 318
add(318, "'(resp. 1+Xt, 1+Xt de Ĝ(Z[X,Y]))'",
    "1+Xt, 1+Xt (both scans)",
    r"(resp. \(1+Xt,1+Xt\) de",
    "misprint_in_print", "high", None,
    "The commutativity is checked on the two elements 1+Xt, 1+Yt of Ĝ(Z[X,Y]), as on 1+Xt,1+Yt,1+Zt of Ĝ(Z[X,Y,Z]) just before. The TeX keeps the printed reading; the corrected layer also still reads 1+Xt,1+Xt.",
    corrected=r"(resp. \(1+Xt,1+Yt\) de")

add(318, "'Donnons à titre d'exemple la valeur de p_2 :'",
    "a small p with its stem below the line (p_2), unlike the capital P of 'sera noté P_n' above and of the display P_2(X_1,X_2;Y_1,Y_2) below (both scans; crops_316_320/c318_p2.png, c318_Pn.png)",
    r"la valeur de \(P_2\) :",
    "misprint_in_print", "medium",
    fx(r"valeur de \(P_2\)", r"valeur de \(p_2\)"),
    "The TeX silently corrects; the diplomatic layer keeps the printed small p.",
    corrected=r"valeur de \(P_2\)")

add(318, "after the display of P_2",
    "On a également la relation suivante : ... begins a new, indented paragraph (both scans)",
    r"\]\nOn a également (same paragraph)",
    "other", "high",
    fx(r"\]⏎On a également", r"\]⏎⏎On a également"),
    "Missing paragraph break.")

add(318, "'nous le noterons parfois 1, ou encore 1_∘ .'",
    "both 1 underlined (1̲ and 1̲_∘, the underline under the 1 only; both scans; crops_316_320/w318_unit.png, w318_unit2.png)",
    r"\(1\), ou encore \(1_\circ\)",
    "underline", "high",
    fx(r"parfois \(1\), ou encore \(1_\circ\)", r"parfois \(\underline{1}\), ou encore \(\underline{1}_\circ\)"),
    "The underlined 1 names the unit 1+t of Ĝ(K); it recurs twice on p. 319 (entries there).")

add(318, "'et par conséquent être composé avec lui même'",
    "lui même, without hyphen (both scans); p. 319 has 'lui-même'",
    "lui même",
    "misprint_in_print", "medium", None,
    "The TeX keeps the printed reading.",
    corrected="lui-même")

# ---------------------------------------------------------------- p. 319
add(319, "page start",
    "p. 319 begins 'choisirons des indéterminées différentes pour chacun des facteurs'; p. 318 ends '... pour éviter des confusions, nous' (both scans)",
    "page_319.tex begins 'nous choisirons': 'nous', the last word of p. 318, stands under the folio-319 marker",
    "marker", "high", None,
    r"Page 319 really begins with 'choisirons'. Exact fix in main.tex (both layers, once each): replace 'pour éviter des confusions,\n%%%%%%%%%%  scan idx 332  |  folio 319  %%%%%%%%%%\nnous choisirons' by 'pour éviter des confusions, nous\n%%%%%%%%%%  scan idx 332  |  folio 319  %%%%%%%%%%\nchoisirons' (simulated on both layers). Equivalent: python -I move_marker.py 6 319 'choisirons'.")

add(319, "'L'élément définissant le morphisme λ_u est 1 + {1+Xt}u'",
    "the first 1 underlined (1̲ + {1+Xt}u; both scans)",
    r"\(1+\{1+Xt\}u\)",
    "underline", "high",
    fx(r"est \(1+\{1+Xt\}u\)", r"est \(\underline{1}+\{1+Xt\}u\)"),
    "The unit 1̲ of p. 318.")

add(319, "display (2.3.3)",
    "λ_u(1 + Xt) = 1̲ + {1 + Xt} u. : the first 1 of the right side underlined (both scans)",
    r"\lambda_u(1+Xt)=1+\{1+Xt\}u.",
    "underline", "high",
    fx(r"=1+\{1+Xt\}u.", r"=\underline{1}+\{1+Xt\}u."),
    "As the previous entry.")

add(319, "after (2.3.3)",
    "Donnons à titre d'exemple la valeur de Q_{2,2} : begins a new, indented paragraph (both scans)",
    r"\end{equation}\nDonnons (same paragraph)",
    "other", "high",
    fx(r"\end{equation}⏎Donnons", r"\end{equation}⏎⏎Donnons"),
    "Missing paragraph break. Independent of the folio-320 marker fix (no common text).")

add(319, "series with the typed dots on the line (convention, reported once)",
    "'...' typed on the line: '1+ψ_1u+...+ψ_iu^i+...', 'λ_u(1+...+X_nt^n+...)', 'λ^i(1+...+X_nt^n+...)' (both scans)",
    r"\cdots: 1+\psi_1u+\cdots+\psi_i u^i+\cdots, \lambda_u(1+\cdots+X_nt^n+\cdots), \lambda^i(1+\cdots+X_nt^n+\cdots)",
    "symbol", "medium", None,
    r"GLOBAL_ISSUES 87 (volume decision for the closing pass), not itemized. The dots between the lowered wedges on p. 316 (x'_1∧...∧x'_{n-p}) stand at the height of the wedge tops and may stay \cdots.")

# ---------------------------------------------------------------- p. 320
add(320, "page start",
    "p. 320 begins with the display 'Q_{2,2}(X_1,X_2,X_3,X_4) = X_1X_3 - X_4 .'; p. 319 ends 'Donnons à titre d'exemple la valeur de Q_{2,2} :' (both scans)",
    r"the display \[ Q_{2,2}(X_1,X_2,X_3,X_4)=X_1X_3-X_4. \] ends page_319.tex, above the folio-320 marker; page_320.tex begins 'Indiquons'",
    "marker", "high", None,
    r"Page 320 really begins with the display. Exact fix in main.tex (both layers, once each): replace 'la valeur de \(Q_{2,2}\) :\n\[\n  Q_{2,2}(X_1,X_2,X_3,X_4)=X_1X_3-X_4.\n\]\n\n%%%%%%%%%%  scan idx 333  |  folio 320  %%%%%%%%%%\nIndiquons' by 'la valeur de \(Q_{2,2}\) :\n%%%%%%%%%%  scan idx 333  |  folio 320  %%%%%%%%%%\n\[\n  Q_{2,2}(X_1,X_2,X_3,X_4)=X_1X_3-X_4.\n\]\n\nIndiquons' (simulated on both layers). Equivalent: python -I move_marker.py 6 320 '\[' --before.")

add(320, "Définition 2.4, the statement",
    "underlined word group by word group: 'Un pré-', 'anneau', 'sera appelé un', 'anneau si l'homomor-phisme de groupes abéliens', 'est un', 'homomorphisme', 'pour la structure de pré-', 'anneau sur le deuxième membre définie en'; λ, K, the formula and '2.3.' plain (both scans)",
    "the statement in roman",
    "underline", "high", None,
    r"The GLOBAL_ISSUES 82 pattern, which Exposé V continues (findings_296_300, p. 298): not itemized. No \emph on defined terms and no category L on pp. 316-320.")

add(320, "after Définition 2.4",
    "Cela signifie donc qu'on a les relations : ∀x,y ∈ K, begins a new, indented paragraph (both scans)",
    "définie en 2.3. Cela signifie (same paragraph as the definition)",
    "other", "high",
    fx("définie en 2.3. Cela signifie", "définie en 2.3.⏎⏎Cela signifie"),
    "Missing paragraph break.")

add(320, "after (2.4.1)",
    "En termes des applications λ^i, ... begins a new, indented paragraph (both scans)",
    r"\end{equation}\nEn termes (same paragraph)",
    "other", "high",
    fx(r"\end{equation}⏎En termes", r"\end{equation}⏎⏎En termes"),
    "Missing paragraph break.")

add(320, "'les deux dernières relations équivalent à : x,y ∈ K, i.j ∈ ℕ,'",
    "i.j with a full stop on the line (both scans; crops_316_320/c320_ij.png)",
    r"\(i.j\in\mathbb N\)",
    "misprint_in_print", "high", None,
    "The TeX keeps the printed reading; the corrected layer also still reads i.j.",
    corrected=r"\(i,j\in\mathbb N\)")

add(320, "display (2.4.2), end of the first line",
    "λ^i(xy) = P_i(λ^1(x),...,λ^i(x); λ^1(y),..., λ^i(y)) with no punctuation after it (both scans)",
    r"\lambda^i(y)), \tag{2.4.2}",
    "punctuation", "high",
    fx(r"\lambda^i(y)),", r"\lambda^i(y))"),
    "The TeX adds a comma at the end of the display line.")

add(320, "display (2.4.2), end of the second line",
    "λ^j(λ^i(x)) = Q_{i,j}(λ^1(x),...,λ^{ij}(x)) with no punctuation after it (both scans)",
    r"\lambda^{ij}(x)). \tag{2.4.3}",
    "punctuation", "high",
    fx(r"\lambda^{ij}(x)).", r"\lambda^{ij}(x))"),
    "The TeX adds a full stop at the end of the display. Independent of the next entry (adjacent texts, no overlap).")

add(320, "display (2.4.2), the equation numbers",
    "one number, (2.4.2), at the left between the two lines; no (2.4.3) (both scans)",
    r"\tag{2.4.2} on the first line and \tag{2.4.3} on the second",
    "number", "high",
    fx(r"\tag{2.4.3}", r"\notag"),
    r"The TeX adds the number (2.4.3). The two relations share the number 2.4.2, and the text cites them so ('les relations 2.4.2', main.tex line 7845; 'V 2.4.2' in Exp. VI). With \notag the one number stays on the first line; a single number centred between the lines would need equation+aligned.")

# ---------------------------------------------------------------- checks
ok = True
texts = {}
for d in F:
    p = d["page"]
    if p not in texts:
        texts[p] = (B / f"page_{p}.tex").read_text(encoding="utf-8")
    fix = d["fix"]
    if not fix:
        continue
    orig = (B / f"page_{p}.tex").read_text(encoding="utf-8")
    n_orig = orig.count(fix["old"])
    n_now = texts[p].count(fix["old"])
    mark = "%%%%%%%%%%" in fix["old"]
    print(p, d["kind"], repr(fix["old"][:50]), "orig:", n_orig, "after earlier fixes:", n_now, "MARKER!" if mark else "")
    if n_now != 1 or mark:
        ok = False
    texts[p] = texts[p].replace(fix["old"], fix["new"], 1)
print("all fixes apply once:", ok)
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print("wrote", OUT, len(F), "entries")
from collections import Counter
c = Counter((d["page"], d["kind"] == "misprint_in_print") for d in F)
for p in sorted({d["page"] for d in F}):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
