"""Build findings_581_585.json and check that every fix's old text occurs exactly once in its page file."""
import json, pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b581_585"
OUT = RUN / "findings_581_585.json"
NL = "\\n"  # a literal backslash-n inside notes, as in earlier batches
M = "%%%%%%%%%%  scan idx {}  |  folio {}  %%%%%%%%%%"


def marker_note(folio, idx, late, begins, old_before, old_after, new_before, new_after, anchor):
    return (f"The folio-{folio} marker stands {late} late: page {folio} really begins at '{begins}'. "
            f"Exact fix in main.tex (both layers, diplomatic and current): replace "
            f"'{old_before}{NL}{M.format(idx, folio)}{NL}{old_after}' by "
            f"'{new_before}{NL}{M.format(idx, folio)}{NL}{new_after}' "
            f"(old occurs once in each layer, checked 13 Nov 16:32; main.tex was being edited, so no line numbers). "
            f"Equivalent: python -I move_marker.py 6 {folio} {anchor} --before.")


F = []

# ---------------- page 581 ----------------
F.append({
    "page": 581, "where": "start of page (folio-581 marker)",
    "scan": "p. 581 begins 'on peut dans ce diagramme remplacer les Z^i par les A^i' (both scans)",
    "tex": r"'on' ends the last line of page_580.tex ('... (\(X\) étant projectif sur \(S\)), on'), above the folio-581 marker; page_581.tex begins 'peut dans ce diagramme'",
    "kind": "marker", "confidence": "high", "fix": None,
    "note": marker_note(581, 594, "one word", "on peut dans ce diagramme",
                        r"projectif sur \(S\)), on", "peut dans ce diagramme",
                        r"projectif sur \(S\)),", "on peut dans ce diagramme", "'on'"),
})
F.append({
    "page": 581, "where": "Remarque 7.13.13, 'Ceci posé, il résulte immédiatement de la commutativité de (7.13.10)'",
    "scan": "'Ceci posé, ...' begins a new, indented paragraph after the line ending 'dans les H^{2i}(T,Q_l(i)).' (both scans)",
    "tex": r"'... dans les \(H^{2i}(T,\mathbb Q_\ell(i))\). Ceci posé, il résulte ...' runs on in the same paragraph",
    "kind": "other", "confidence": "high",
    "fix": {"old": ". Ceci posé", "new": ".\n\nCeci posé"},
    "note": "Missing paragraph break.",
})

# ---------------- page 582 ----------------
F.append({
    "page": 582, "where": "start of page (folio-582 marker)",
    "scan": "p. 582 begins 'un homomorphisme de spécialisation :'; p. 581 ends '... Lorsque f: X --> S est de type fini, on définit alors' (both scans)",
    "tex": "'un' ends the last line of page_581.tex ('... on définit alors un'), above the folio-582 marker; page_582.tex begins 'homomorphisme de spécialisation :'",
    "kind": "marker", "confidence": "high", "fix": None,
    "note": marker_note(582, 595, "one word", "un homomorphisme de spécialisation :",
                        "on définit alors un", "homomorphisme de spécialisation :",
                        "on définit alors", "un homomorphisme de spécialisation :", "'un'"),
})

# ---------------- page 583 ----------------
F.append({
    "page": 583, "where": "start of page (folio-583 marker)",
    "scan": "p. 583 begins \"au cas d'un corps résiduel algébriquement clos deviendraient inutiles,\"; p. 582 ends '... la résolution des singularités et la réduction' (both scans)",
    "tex": "\"au cas d'un\" ends the last line of page_582.tex (\"... et la réduction au cas d'un\"), above the folio-583 marker; page_583.tex begins 'corps résiduel algébriquement clos'",
    "kind": "marker", "confidence": "high", "fix": None,
    "note": marker_note(583, 596, "three words", "au cas d'un corps résiduel",
                        "et la réduction au cas d'un", "corps résiduel",
                        "et la réduction", "au cas d'un corps résiduel", "\"au cas d'un\""),
})
F.append({
    "page": 583, "where": "first paragraph, 'E devra maintenant désigner un cycle sur P^1_S x_S X tel que'",
    "scan": "plain typed P (no overstrike) in 'P^1_S x_S X'; two lines above, 'C = P^1_S' has the overstruck double-struck P (both scans)",
    "tex": r"\(\mathbb P^1_S\times_SX\)",
    "kind": "font", "confidence": "medium",
    "fix": {"old": r"\(\mathbb P^1_S\times_SX\)", "new": r"\(P^1_S\times_SX\)"},
    "note": r"The typist's plain P where the TeX has \mathbb P (same class as the plain-Q volume decision, SGA 7 II issue 61). The first P^1_S of the page (C = P^1_S) is double-struck in the print and right in the TeX.",
})
F.append({
    "page": 583, "where": "second paragraph, 'ainsi, si Z est quasi-projectif et lisse sur un corps'",
    "scan": "'ainsi, si Z est quasi-projectif et lisse sur un corps' (both scans)",
    "tex": r"ainsi, si \(Z\) est quasi-projectif",
    "kind": "misprint_in_print", "confidence": "medium", "fix": None,
    "corrected": r"ainsi, si \(T\) est quasi-projectif",
    "note": "The TeX keeps the printed reading. The scheme meant is the T of Z.(T) --> Gr.(T) in the same sentence: the relation on cycles on T differs from linear equivalence only by torsion when T is quasi-projective and smooth over a field (XIV 4.1, 4.2); Z names the cycle groups, not a scheme. Correct reading T.",
})

# ---------------- page 584 ----------------
F.append({
    "page": 584, "where": "first diagram of 7.15, hooked arrow X'_{t'} --> X'",
    "scan": "label i'_{X'} on X'_{t'} --> X' (both scans); in the X square the corresponding arrow X_t --> X is labelled j_X",
    "tex": "X'_{t'} \\arrow[l,hook,\"i'_{X'}\"]",
    "kind": "misprint_in_print", "confidence": "medium", "fix": None,
    "corrected": "X'_{t'} \\arrow[l,hook,\"j_{X'}\"]",
    "note": "The TeX keeps the printed reading. The labels of the X' square are swapped against the X square (j_X: X_t --> X generic fibre, i_X: X_s --> X closed fibre): X'_{t'} --> X' should be j_{X'} and X'_{s'} --> X' should be i_{X'}. Apply together with the next entry (the pair swaps the two labels).",
})
F.append({
    "page": 584, "where": "first diagram of 7.15, hooked vertical arrow X'_{s'} --> X'",
    "scan": "label j_{X'} on X'_{s'} --> X' (both scans); in the X square the corresponding arrow X_s --> X is labelled i_X",
    "tex": "X'_{s'} \\arrow[uu,hook,\"j_{X'}\"']",
    "kind": "misprint_in_print", "confidence": "medium", "fix": None,
    "corrected": "X'_{s'} \\arrow[uu,hook,\"i_{X'}\"']",
    "note": "The TeX keeps the printed reading. Second half of the label swap of the previous entry; apply the two together.",
})
F.append({
    "page": 584, "where": "diagram (7.15.1), lower horizontal arrow K.(X'_{t'}) --> K.(X'_{s'})",
    "scan": "the lower arrow is labelled sigma_X like the upper one, without a prime (both scans)",
    "tex": "K_\\bullet(X'_{t'}) \\arrow[r,\"\\sigma_X\"]",
    "kind": "misprint_in_print", "confidence": "medium", "fix": None,
    "corrected": "K_\\bullet(X'_{t'}) \\arrow[r,\"\\sigma_{X'}\"]",
    "note": "The TeX keeps the printed reading. The lower arrow is the specialization homomorphism of X' over S' (definition 7.3 applied to X'), sigma_{X'}; sigma_X is the upper arrow K.(X_t) --> K.(X_s).",
})

# ---------------- page 585 ----------------
F.append({
    "page": 585, "where": "first paragraph, 'et soit A-bar = lim A-bar_i le normalisé de A dans K-bar'",
    "scan": "plain 'lim' with no arrow under it (both scans); only the display further down has lim with an arrow and index i under it",
    "tex": r"\bar A=\varinjlim \bar A_i",
    "kind": "formula", "confidence": "high",
    "fix": {"old": r"\bar A=\varinjlim \bar A_i", "new": r"\bar A=\lim \bar A_i"},
    "note": r"The TeX adds the inductive-limit arrow that this inline formula does not have; the two \varinjlim_i of the display below are right.",
})
F.append({
    "page": 585, "where": "first paragraph, 'et soit B_i = A_i m_i, qui par Krull-Akizuki'",
    "scan": "'B_i = A_i m_i': A with subscript i followed by the lower subscript m_i (underlined m), no parentheses (both scans)",
    "tex": r"B_i=(A_i)_{\mathfrak m_i}",
    "kind": "formula", "confidence": "medium",
    "fix": {"old": r"B_i=(A_i)_{\mathfrak m_i}", "new": r"B_i=A_{i\,\mathfrak m_i}"},
    "note": "The TeX adds parentheses that the print does not have. Apply before the misprint entry for the same formula (missing bar), whose reading is that of the text after this fix.",
})
F.append({
    "page": 585, "where": "first paragraph, 'B_i = A_i m_i'",
    "scan": "A without the bar (both scans), whereas the ring meant is the normalization A-bar_i of the preceding sentence",
    "tex": r"B_i=A_{i\,\mathfrak m_i} (after the parenthesis fix above; now B_i=(A_i)_{\mathfrak m_i})",
    "kind": "misprint_in_print", "confidence": "medium", "fix": None,
    "corrected": r"B_i=\bar A_{i\,\mathfrak m_i}",
    "note": "The TeX keeps the printed reading (no bar). A_i is not defined in 7.16: m_i is a maximal ideal of A-bar_i ('induisant donc sur chaque A-bar_i un idéal maximal m_i') and Krull-Akizuki applies to the normalization A-bar_i, so B_i is the localization of A-bar_i at m_i.",
})
F.append({
    "page": 585, "where": "first paragraph, 'k_i = A_i/m_i = k(s_i) des B_i'",
    "scan": "A without the bar (both scans)",
    "tex": r"k_i=A_i/\mathfrak m_i",
    "kind": "misprint_in_print", "confidence": "medium", "fix": None,
    "corrected": r"k_i=\bar A_i/\mathfrak m_i",
    "note": "The TeX keeps the printed reading. As for B_i: m_i is a maximal ideal of A-bar_i, so the residue field is A-bar_i/m_i (compare k-bar = A-bar/m-bar in the same sentence).",
})

# ---------------- checks ----------------
ok = True
for x in F:
    t = (B / f"page_{x['page']}.tex").read_text(encoding="utf-8")
    if x["fix"]:
        old = x["fix"]["old"]
        n = t.count(old)
        marker_cross = "%%%%%%%%%%" in old
        print(x["page"], x["kind"], "old count", n, "CROSSES MARKER" if marker_cross else "")
        ok = ok and n == 1 and not marker_cross
    elif x["kind"] == "misprint_in_print":
        tex = x["tex"].split(" (after")[0]
        print(x["page"], x["kind"], "tex count", t.count(tex), repr(tex))
    assert ("corrected" in x) == (x["kind"] == "misprint_in_print")
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
json.loads(OUT.read_text(encoding="utf-8"))
print("written", OUT, len(F), "findings; all fix olds unique:", ok)
