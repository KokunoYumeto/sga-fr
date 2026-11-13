"""Build findings_631_635.json, check that every fix's old occurs exactly once in its page file,
and simulate the three marker moves (move_marker.py logic) on an in-memory copy of pages 630-634."""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b631_635"
OUT = RUN / "findings_631_635.json"
NL = "\n"

F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 631 ----------------
add(631, "start of page (page_631.tex lines 3-7: the display before 'on ait :')",
    "p. 631 begins 'on ait : a_i^{(m)} = P_i^{(m,r)} (a_r,...,a_i).' under the running head; the display "
    "Σ_{i=0}^r a_i^{(m)}(n+i over i) = Σ_{j=0}^r a_j(mn+j over j) is the last line of p. 630 (both scans; "
    "b626_630/page_630_s4.png)",
    r"page_631.tex opens with the display \[\sum_{i=0}^{r}a_i^{(m)}\binom{n+i}{i}=\sum_{j=0}^{r}a_j\binom{mn+j}{j},\]"
    r" under the folio-631 marker; page_630.tex ends 'tel que dans l'égalité suivante :'",
    "marker", "high", None,
    "Page 631 really begins with 'on ait :'. Move the folio-631 marker down below the display: "
    "python -I move_marker.py 6 631 \"on ait\" (simulated on a copy: '... l'égalité suivante :', the display, "
    "the marker, then 'on ait : ...'). Apply this page's display-comma fix first (its old is the display's last "
    "line), or look that old up under folio 630 after the move.")

add(631, "end of the display Σ a_i^{(m)} binom(n+i,i) = Σ a_j binom(mn+j,j) (printed at the foot of p. 630)",
    "no punctuation after the last binomial (mn+j over j) (both scans; crops_631_635/p630_disp_end.png)",
    r"\binom{mn+j}{j},",
    "punctuation", "high",
    {"old": r"\binom{mn+j}{j},", "new": r"\binom{mn+j}{j}"},
    "Comma added at the end of the display. The display stands under the folio-631 marker but is printed on "
    "p. 630 (marker finding above).")

add(631, "Lemme 2.11, 'et X un S schéma projectif'",
    "'un S schéma projectif': no hyphen after S (both scans; crops_631_635/p631_Ssch.png, w631_Ssch.png)",
    r"un \(S\) schéma projectif",
    "misprint_in_print", "medium", None,
    "Typing slip for S-schéma (as in Lemme 3.1 'un S-schéma quasi-compact'). The TeX keeps the printed reading.",
    corrected=r"un \(S\)-schéma projectif")

add(631, "proof of 2.11, 'En effet, soit δ = supp {d(L_K)}'",
    "'supp' (both scans; crops_631_635/p631_supp.png)",
    r"\(\delta=\operatorname{supp}\{d(L_K)\}\)",
    "misprint_in_print", "medium", None,
    "δ is the supremum of the integers d(L_K) ('Si δ>0, on peut remplacer ... par les L_K(-δ) ... supposer "
    "δ≤0'); 'supp' is a typing slip for 'sup'. The TeX keeps the printed reading.",
    corrected=r"\(\delta=\sup\{d(L_K)\}\)")

add(631, "Lemme 3.1, 'topologie f.p.p.f.)(*). Alors pour tout système projectif'",
    "a full stop after the footnote mark: 'f.p.p.f.)(*). Alors' (both scans; crops_631_635/p631_fppf.png)",
    r"'f.p.p.f.)}\footnote{... topologie fppf.}' with no full stop after the footnote; page_632.tex goes on "
    r"with '\emph{Alors pour tout'",
    "punctuation", "high",
    {"old": "topologie fppf.}", "new": "topologie fppf.}."},
    "Missing full stop ending the sentence before 'Alors'; it is printed on p. 631, after the footnote mark, "
    "outside the underline.")

add(631, "footnote (*), 'et FGA n° 232 pour la définition de Pic_{X/S}'",
    "n with a raised small o (the numéro sign), in both scans (crops_631_635/p631_no.png, w631_no.png)",
    "FGA no 232",
    "symbol", "medium",
    {"old": "FGA no 232", "new": r"FGA n\textsuperscript{o} 232"},
    r"The file writes the numéro sign n\textsuperscript{o} (22 times across the volume) or n° (bibliography); "
    "plain 'no' loses the raised o.")

add(631, "the structure sheaf O on pp. 631-632 (3 places; the witness of p. 636 the same: O_X(1), O_Y(1))",
    "a plain typed O, not underlined (both scans): 'H = O_X(1)' p. 631 (crops_631_635/p631_OX.png); "
    "'soit ≃ O_{X_{Z\"}}' and 'soit ≃ O_{X_{Z\"_β}}' p. 632 (crops_631_635/p632_OX.png, p632_La2.png)",
    r"\mathcal O_X(1); \mathcal O_{X_{Z''}}; \mathcal O_{X_{Z''_\beta}} (Exposé XIII, folios 616-671, writes "
    r"\mathcal O 128 times, never \underline{O} or \cO)",
    "font", "medium", None,
    "Convention of the Exposé XIII TeX, reported once, not itemized: this typescript types the structure "
    "sheaf as a plain O, which differs from the underlined O of the pending NOTE_6 decision (\\cO / "
    "\\underline O); the same case as SGA 5 global item 89 (f). One decision for the exposé.")

# ---------------- page 632 ----------------
add(632, "start of page",
    "p. 631 ends 'f.p.p.f.)(*). Alors pour tout système projectif filtrant (Z_α) de S-schémas'; p. 632 begins "
    "'quasi-compacts et quasi-séparés, à morphismes de transition affines,' (both scans)",
    r"page_632.tex begins '\emph{Alors pour tout syst\`eme projectif filtrant \((Z_\alpha)\) de "
    r"\(S\)-sch\'emas quasi-compacts ...': the last line of p. 631 stands under the folio-632 marker",
    "marker", "high", None,
    "Page 632 really begins with 'quasi-compacts'. Move the folio-632 marker into the line, before it: "
    "python -I move_marker.py 6 632 \"quasi-compacts et quasi-s\" (simulated on a copy: '... de "
    "\\(S\\)-sch\\'emas ', the marker, then 'quasi-compacts et quasi-s\\'epar\\'es, ...'; the \\emph group "
    "then runs across the marker comment line, which LaTeX accepts).")

add(632, "display 3.1.1, left member 'lim→ Pic_{X/S} (Z_α)'",
    "lim with the arrow under it and no index (both scans; crops_631_635/p632_disp.png)",
    r"\varinjlim_\alpha",
    "formula", "high",
    {"old": r"\varinjlim_\alpha", "new": r"\varinjlim"},
    "Index α added by the TeX under the inductive limit.")

add(632, "display 3.1.1, right member 'Pic_{X/S}(lim← Z_α)'",
    "lim with the arrow under it and no index (both scans; crops_631_635/p632_disp.png)",
    r"\varprojlim_\alpha Z_\alpha",
    "formula", "high",
    {"old": r"\varprojlim_\alpha Z_\alpha", "new": r"\varprojlim Z_\alpha"},
    "Index α added by the TeX under the projective limit (the print's 'Posons Z = lim← Z_α' below has none "
    "either, and the TeX has none there).")

add(632, "'le faisceau inversible L' sur X_{Z'}, image inverse de L_α, où Z' = Z'_α ×_{Z_α} Z'",
    "L_α without prime (both scans; crops_631_635/p632_La.png)",
    r"image inverse de \(L_\alpha\)",
    "misprint_in_print", "medium", None,
    "λ_α is represented by L'_α on X_{Z'_α}, so L' on X_{Z'} is the inverse image of L'_α (as in the next "
    "paragraph, 'l'image inverse de L'_α sur X_{Z\"_β}'). The TeX keeps the printed reading.",
    corrected=r"image inverse de \(L'_\alpha\)")

add(632, "'tel que l'image inverse de L'_α. sur X_{Z\"_β} soit ≃ O_{X_{Z\"_β}}'",
    "a typed dot right after the subscript α, at its level and in the same grey as the α, the size of the "
    "stops of 'f.p.p.f.' on the line above (both scans; crops_631_635/p632_dot_cmp.png, w632_La.png)",
    r"de \(L'_\alpha\) sur",
    "misprint_in_print", "low",
    {"old": r"de \(L'_\alpha\) sur", "new": r"de \(L'_\alpha\). sur"},
    "Stray stop inside the sentence; the TeX silently drops it. Low: it could be a mark on the master rather "
    "than a typed stop.",
    corrected=r"de \(L'_\alpha\) sur")

# ---------------- page 633 ----------------
add(633, "start of page, label (ii) of Proposition 3.2",
    "p. 633 begins '(ii) Les parties Λ de Pic_{X/S} correspondent biunivoquement ...'; p. 632 ends with item "
    "(i) (both scans)",
    r"the bare \item that prints (ii) is the last line of page_632.tex, above the folio-633 marker; "
    r"page_633.tex begins with the item's text '\emph{Les parties ...'",
    "marker", "high", None,
    "Page 633 really begins with the item (ii). Move the folio-633 marker up one line, above that \\item: "
    "python -I move_marker.py 6 633 \"\\item\" --before (simulated on a copy: '... de type fini sur "
    "\\(S\\).}', the marker, '\\item', '\\emph{Les parties ...').")

add(633, "proof of 3.2, before 'Quant à (iii), supposons que la partie Λ'",
    "'Quant à (iii)' starts a new, indented paragraph (both scans)",
    r"'... inversibles sur \(X_K\). Quant \`a (iii)' in one paragraph",
    "other", "medium",
    {"old": r"sur \(X_K\). Quant", "new": r"sur \(X_K\)." + NL + NL + "Quant"},
    "Missing paragraph break (the typescript indents its new paragraphs).")

add(633, "proof of 3.2, before 'Réciproquement supposons que 𝓛 soit limitée'",
    "'Réciproquement' starts a new, indented paragraph (both scans)",
    r"'... donc \(L\) limite \(\mathscr L\). R\'eciproquement' in one paragraph",
    "other", "medium",
    {"old": r"limite \(\mathscr L\). R\'eciproquement",
     "new": r"limite \(\mathscr L\)." + NL + NL + r"R\'eciproquement"},
    "Missing paragraph break.")

# ---------------- page 634 ----------------
add(634, "end of Définition 3.3, 'est dit de type fini si toute famille limitée ...'",
    "'est dit' underlined, the defined term 'de type fini' plain, then 'si toute famille limitée de classes de "
    "faisceaux' underlined (both scans)",
    r"\emph{est dit de type fini si toute ...}: the defined term inside the emphasis",
    "underline", "low",
    {"old": r"\emph{est dit de type fini si", "new": r"\emph{est dit} de type fini \emph{si"},
    "The typescript marks the defined term by leaving it out of the statement's underline; the block \\emph "
    "loses that. It is a word group, not a formula or punctuation; drop this item if the block-underline "
    "decision is to cover defined terms as well.")

add(634, "proof of 3.4, 'limitée par un L sur un X_R. Ia famille 𝓛_T = 𝓛 ×_S T'",
    "'Ia': a capital I with serifs on both sides at top and bottom, unlike the L of 'un L sur' on the same "
    "line, which has its long foot (both scans; crops_631_635/p634_la_zoom.png, w634_la_zoom.png, p634_L.png)",
    "La famille",
    "misprint_in_print", "medium",
    {"old": "La famille", "new": "Ia famille"},
    "Typing slip I for L; the TeX silently corrects it.",
    corrected="La famille")

add(634, "proof of 3.4, before 'La réciproque de (i) et l'assertion (ii)'",
    "'La réciproque de (i)' starts a new, indented paragraph (both scans)",
    r"'... aussi \(\Phi^{-1}(\mathscr L)\). La r\'eciproque' in one paragraph",
    "other", "medium",
    {"old": r"\(\Phi^{-1}(\mathscr L)\). La r\'eciproque",
     "new": r"\(\Phi^{-1}(\mathscr L)\)." + NL + NL + r"La r\'eciproque"},
    "Missing paragraph break.")

# ---------------- page 635 ----------------
add(635, "proof of 3.5, 'on peut supposer que le morphisme Pic_{Y_T/T} ⟶ Pic_{X_T/T} induit par f* est de type fini'",
    "the morphism is set inline in the running text: 'morphisme Pic_{Y_T/T} ⟶ Pic_{X_T/T} induit par f* est de "
    "type fini par récur-' (both scans)",
    r"a display \[\underline{\Pic}_{Y_T/T}\longrightarrow\underline{\Pic}_{X_T/T}\]",
    "other", "high",
    {"old": "le morphisme" + NL + r"\[" + NL + r"\underline{\Pic}_{Y_T/T}\longrightarrow\underline{\Pic}_{X_T/T}"
            + NL + r"\]" + NL + "induit par",
     "new": r"le morphisme \(\underline{\Pic}_{Y_T/T}\longrightarrow\underline{\Pic}_{X_T/T}\) induit par"},
    "The TeX makes a display of a formula the print runs in the text.")

add(635, "'il en résulte pour ⨿ X_i/S' par le'",
    "the coproduct sign with no index under it; the i is the subscript of X (both scans; "
    "crops_631_635/p635_Xi.png)",
    r"\coprod_iX_i/S'",
    "formula", "high",
    {"old": r"\coprod_iX_i/S'", "new": r"\coprod X_i/S'"},
    "Index i added by the TeX under the coproduct (the size of the hand-drawn sign is not at issue).")

add(635, "'Si l'on l'admet pour tous les X_i/S''",
    "X_i without prime (both scans; crops_631_635/p635_Xi.png); two lines above the components are named "
    "X'_i, with the prime printed (p635_Xpi.png)",
    r"tous les \(X_i/S'\)",
    "misprint_in_print", "medium", None,
    "The X'_i are the irreducible components of X_{S'}; their sum maps onto X_{S'} (p. 636 'donc pour "
    "X_{S'}/S' en vertu de 3.5 et 3.4 (ii)'). The TeX keeps the printed reading. Correct together with the "
    "next item.",
    corrected=r"tous les \(X'_i/S'\)")

add(635, "'il en résulte pour ⨿ X_i/S''",
    "X_i without prime (both scans; crops_631_635/p635_Xi.png)",
    r"\coprod_iX_i/S' (after the index fix above: \coprod X_i/S')",
    "misprint_in_print", "medium", None,
    "Same slip as the item before; correct both together. The index fix of this place is listed first; "
    "this reading is taken from the text after it.",
    corrected=r"\coprod X'_i/S'")

# ---------------- checks ----------------
ok = True
for d in F:
    fx = d["fix"]
    if fx is None:
        continue
    t = (B / f"page_{d['page']}.tex").read_text(encoding="utf-8")
    n = t.count(fx["old"])
    mk = "%%%%%%%%%%" in fx["old"]
    print(d["page"], n, "MARKER!" if mk else "", repr(fx["old"][:60]))
    if n != 1 or mk:
        ok = False
print("all unique:", ok)

# simulate the marker moves on a copy of pages 630-634 (logic of move_marker.py)
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
parts = [(RUN / "b626_630" / "page_630.tex").read_text(encoding="utf-8")]
parts += [(B / f"page_{p}.tex").read_text(encoding="utf-8") for p in range(631, 635)]
T = "".join(p.replace("% from main.tex\n", "", 1) for p in parts)


def move(t, folio, anchor, before=False):
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        return t2[:ls] + line + "\n" + t2[ls:]
    return t2[:k] + "\n" + line + "\n" + t2[k:]


for folio, anchor, before in ((631, "on ait", False), (632, "quasi-compacts et quasi-s", False),
                              (633, r"\item", True)):
    T = move(T, folio, anchor, before)
    m = next(m for m in MARK.finditer(T) if int(m.group(2)) == folio)
    print("----", folio)
    print(T[max(0, m.start() - 160):m.end() + 90])

if ok:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("written", OUT, len(F))
