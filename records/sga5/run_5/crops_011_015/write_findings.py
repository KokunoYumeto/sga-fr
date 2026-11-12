# Writes findings_011_015.json. LaTeX backslashes are written as the section sign and converted with chr(92).
import json
import pathlib

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
B = chr(92)


def L(s):
    return None if s is None else s.replace("\u00a7", B)


def F(page, where, scan, tex, kind, conf, old, new, note, corrected=None):
    d = {"page": page, "where": L(where), "scan": L(scan), "tex": L(tex), "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": L(old), "new": L(new)}}
    if kind == "misprint_in_print":
        d["corrected"] = L(corrected)
    d["note"] = L(note)
    return d


LABEL_SCAN = ("'Preuve' underlined, then ' :', the text running on; no end-of-proof sign at the end of the proof")
out = [
    # ---------------- page 11
    F(11, "top of the page: Proposition 1.11 b), 'b) Si K satisfait aux conditions (i) et (ii) de (1.7)'",
      "The page begins with 'b) Si K satisfait aux conditions (i) et (ii) de (1.7), on a l'implication'; "
      "p. 10 ends with the display of a).",
      "'§item[b)] Si $K$' (s5.tex line 496) is the last line of page_010.tex; the folio-11 marker (line 497) "
      "stands between 'Si $K$' and 'satisfait'.",
      "marker", "high", None, None,
      "Page 11 really begins at s5.tex line 496 '§item[b)] Si $K$'. Exact fix: move the folio-11 marker line from "
      "line 497 to just before line 496 (python -I move_marker.py 5 11 \"§item[b)] Si\" --before; simulated in "
      "memory on both layers: the anchor found is line 496). Text not moved; it agrees with the print."),
    F(11, "c), the display after 'On a en outre l'implication', its last words",
      "'G satisfait / à (1.7. (ii).' with one closing parenthesis only; the display of b) at the top of the page "
      "prints 'à (1.7. (ii)).' with two.",
      "G §text{ satisfait à (1.7.(ii)).}",
      "misprint_in_print", "high",
      "G §text{ satisfait à (1.7.(ii)).}", "G §text{ satisfait à (1.7.(ii).}",
      "Unbalanced parenthesis of the print; the TeX silently corrects it, the fix restores the printed reading.",
      corrected="G §text{ satisfait à (1.7.(ii)).}"),
    F(11, "proof of Proposition 1.11, its label",
      "'Preuve : a) n'est autre que la formule d'adjonction chère à Cartan': " + LABEL_SCAN + " (p. 12).",
      "§begin{proof}[Preuve] (amsthm: italic 'Preuve.', and a square at the §end{proof} on p. 12)",
      "other", "high",
      "§begin{proof}[Preuve]\n", "§emph{Preuve} : ",
      "The form the global pass gave to '§emph{Preuve.}'. Apply together with the removal of '§end{proof}' on "
      "p. 12 (LaTeX fails otherwise). Exposé I writes §begin{proof}[Preuve] 16 times (s5.tex lines 478-1006; also "
      "§begin{proof}[Démonstration] at line 959): one pass may be simpler. The later §begin{prooftext}[Preuve] "
      "(from line 1087) also prints 'Preuve.': to check against the print there."),
    # ---------------- page 12
    F(12, "top of the page: 'd) Prouvons par exemple l'implication réciproque de b)'",
      "The page begins with 'd) Prouvons par exemple ...'; p. 11 ends with 'raisonnement analogue à b).'",
      "'d)' (s5.tex line 520) is the last line of page_011.tex; the folio-12 marker (line 521) stands between "
      "'d)' and 'Prouvons'.",
      "marker", "high", None, None,
      "Page 12 really begins at s5.tex line 520 'd)'. Exact fix: python -I move_marker.py 5 12 \"d)\" --before "
      "(marker to just before line 520; simulated on both layers). Text not moved."),
    F(12, "end of the proof of 1.11, after 'se démontre de manière analogue.'",
      "No end-of-proof sign; 'Remarques 1.11.1' follows.",
      "§end{proof} (prints a square)",
      "extra", "high",
      "§end{proof}\n", "",
      "Apply together with the p. 11 label fix (§begin{proof}[Preuve] -> §emph{Preuve} : )."),
    F(12, "Proposition 1.12, first sentence: 'K ∈ ob D^+(Y)'",
      "'K ∈ ob D^+(Y)' with no subscript, while the same sentence goes on 'posons K_X = R^!f(K_Y) ..., "
      "D_Y = D_{K_Y}'.",
      "$K §in §ob §D^{+}(Y)$",
      "misprint_in_print", "medium",
      None, None,
      "The TeX keeps the printed K. K_Y is not introduced otherwise; Corollaire 1.15 (p. 15) restates the setting "
      "as 'Soit K_Y ∈ ob D^+(Y), et posons, comme en 1.12, K_X = R^!f(K_Y)'.",
      corrected="K_Y §in §ob §D^{+}(Y)"),
    # ---------------- page 13
    F(13, "top of the page: 'Si en outre K_X et K_Y sont dualisants (1)'",
      "The page begins with 'Si en outre K_X et K_Y sont dualisants (1), il existe, pour F ∈ ob D_c^b(X),'; "
      "p. 12 ends with display (i) of a).",
      "'Si en' (s5.tex line 538) is the last line of page_012.tex; the folio-13 marker (line 539) stands between "
      "'Si en' and 'outre'.",
      "marker", "high", None, None,
      "Page 13 really begins at s5.tex line 538 'Si en'. Exact fix: python -I move_marker.py 5 13 \"Si en\" "
      "--before (simulated on both layers). Text not moved."),
    F(13, "proof of Proposition 1.12, its label",
      "'Preuve : a) (i) n'est autre que l'isomorphisme de dualité': " + LABEL_SCAN + " ('utilisant (1.9. b)).').",
      "§begin{proof}[Preuve] ... §end{proof}",
      "other", "high",
      "§begin{proof}[Preuve]\n", "§emph{Preuve} : ",
      "Apply together with the next finding (the §end{proof} of the same proof)."),
    F(13, "end of the proof of 1.12, before 'Scholie'",
      "No end-of-proof sign.",
      "§end{proof} (prints a square)",
      "extra", "high",
      "§end{proof}\n", "",
      "Apply together with the previous finding."),
    # ---------------- page 14
    F(14, "top of the page: 'D_X et D_Y échangent les notions d'image directe'",
      "The page begins with 'D_X et D_Y échangent ...'; the text of p. 13 ends with 'que les foncteurs "
      "dualisants' (the footnotes follow).",
      "'$§underline{D}_X$ et $§underline{D}_Y$' ends s5.tex line 564, the last line of page_013.tex; the "
      "folio-14 marker (line 565) follows it.",
      "marker", "high", None, None,
      "Page 14 really begins at '$§underline{D}_X$ et $§underline{D}_Y$' at the end of s5.tex line 564. Exact "
      "fix: python -I move_marker.py 5 14 '$§underline{D}_X$ et $§underline{D}_Y$' --before (single quotes: the "
      "anchor contains $); the marker then splits line 564 after 'dualisants' (simulated on both layers)."),
    F(14, "proof of Corollaire 1.13, its label",
      "'Preuve : Supposons (F,K_X) bidualisant.': " + LABEL_SCAN + " ('ce qui achève la démonstration.').",
      "§begin{proof}[Preuve] ... §end{proof}",
      "other", "high",
      "§begin{proof}[Preuve]\n", "§emph{Preuve} : ",
      "Apply together with the next finding."),
    F(14, "end of the proof of 1.13, before 'Lemme 1.14'",
      "No end-of-proof sign.",
      "§end{proof} (prints a square)",
      "extra", "high",
      "§end{proof}\n", "",
      "Apply together with the previous finding."),
    # ---------------- page 15
    F(15, "top of the page: Lemme 1.14 b)",
      "The page begins with 'b) Soit F ∈ ob D(X).'; p. 14 ends with a), '... il faut et il suffit que f_*u le "
      "soit.'",
      "'§item[b)]' (s5.tex line 587) is the last line of page_014.tex; the folio-15 marker (line 588) follows it.",
      "marker", "high", None, None,
      "Page 15 really begins at s5.tex line 587 '§item[b)]'. Exact fix: python -I move_marker.py 5 15 "
      "\"§item[b)]\" --before (simulated on both layers). Text not moved."),
    F(15, "Lemme 1.14 b), end of the statement: 'il suffit que f_*F ∈ ob D_c(F)'",
      "'f_*F ∈ ob D_c(F).': a clearly typed F inside the parentheses.",
      "f_{*}F §in §ob §D_c(Y)",
      "misprint_in_print", "high",
      "f_{*}F §in §ob §D_c(Y)", "f_{*}F §in §ob §D_c(F)",
      "f_*F is a complex on Y. The TeX silently corrects; the fix restores the printed reading.",
      corrected="f_{*}F §in §ob §D_c(Y)"),
    F(15, "proof of 1.14 b), 'on a f_{i*}(F_i) -> (f_*F)|Y_i' (base change for a finite morphism)",
      "A plain long arrow, with no tilde and no trace of one (the tildes of the isomorphism arrows on pp. 11-14 "
      "are crisp).",
      "f_{i*}(F_i) §xrightarrow{§sim} (f_{*}F)|Y_i",
      "symbol", "high",
      "f_{i*}(F_i) §xrightarrow{§sim}", "f_{i*}(F_i) §to",
      "The base-change map is an isomorphism, but the print's plain arrow is not an error; the TeX added the "
      "tilde."),
    F(15, "proof of Lemme 1.14, its label",
      "'Preuve : a) Le foncteur f_* étant exact': " + LABEL_SCAN + " ('d'où la conclusion voulue.').",
      "§begin{proof}[Preuve] ... §end{proof}",
      "other", "high",
      "§begin{proof}[Preuve]\n", "§emph{Preuve} : ",
      "Apply together with the next finding."),
    F(15, "end of the proof of 1.14, before 'Corollaire 1.15'",
      "No end-of-proof sign.",
      "§end{proof} (prints a square)",
      "extra", "high",
      "§end{proof}\n", "",
      "Apply together with the previous finding."),
    F(15, "end of the page: the label of the proof of Corollaire 1.15 (folio-16 marker)",
      "p. 15 ends with the statement of 1.15, '... K_X est dualisant.'; the proof's label 'Preuve' is on p. 16.",
      "page_015.tex ends with '§begin{proof}[' (s5.tex line 601); the folio-16 marker (line 602) splits the "
      "command, and 'Preuve]' (line 603) stands under page 16.",
      "marker", "high", None, None,
      "Page 16 really begins at s5.tex line 601 '§begin{proof}['. Exact fix: python -I move_marker.py 5 16 "
      "\"§begin{proof}[\" --before (simulated on both layers). After the move, '§begin{proof}[' and 'Preuve]' are "
      "adjacent lines of page 16: rejoin them, or give that proof the label fix of this report (its §end{proof} "
      "is line 605): page 16."),
]

for d in out:
    for k in ("where", "scan", "tex", "note"):
        assert "\u00a7" not in (d[k] or ""), d
(RUN / "findings_011_015.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8",
                                          newline="\n")
print(len(out), "findings written")
