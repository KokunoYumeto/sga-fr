"""Build findings_031_035.json and check every fix's 'old' against its page file (read-only on the .tex files)."""
import json
import pathlib

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
PAGES = RUN / "b031_035"
OUT = RUN / "findings_031_035.json"
NL = "\n"

F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None, tex_locator=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": confidence, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    d["_loc"] = tex_locator
    F.append(d)


# ---------------------------------------------------------------- page 31
add(31, "top of the page: the first words 'j : V ⟶ U un ouvert non vide de U'",
    "p. 31 begins with 'j : V ⟶ U un ouvert non vide de U tel que j*(F) soit localement'; "
    "p. 30 ends with 'On peut supposer U ≠ ∅, donc il existe'.",
    r"'$j : V \to U$ un' ends s5.tex line 902, the last line of page_030.tex; the folio-31 marker (line 903) "
    r"follows it, so page_031.tex begins with 'ouvert non vide de $U$'.",
    "marker", "high", None,
    r"Page 31 really begins at '$j : V \to U$ un' at the end of s5.tex line 902. Exact fix: "
    r"python -I move_marker.py 5 31 '$j : V \to U$ un' --before (single quotes: the anchor contains $ and a "
    r"backslash); the marker then splits line 902 after 'donc il existe' (simulated in memory on both layers, same "
    r"place). Text not moved; it agrees with the print.")

add(31, "first display, after 'La condition (ii ter) implique que l'on a'",
    "R i_* R j_* j^*(F) ≃ R(ij)_* j^*(F) ∈ ob D_c^+(X) . : the sign is a hand-drawn tilde over a straight bar, "
    "with no arrowhead at either end",
    r"\R i_{*} \R j_{*} j^{*}(F) \xrightarrow{\sim} \R(ij)_{*} j^{*}(F)",
    "symbol", "high",
    {"old": r"\xrightarrow{\sim} \R(ij)_{*}", "new": r"\simeq \R(ij)_{*}"},
    r"The TeX writes the same printed sign as \simeq on pp. 34-35 ('\R^{!}f(A_S) \simeq \R^{!}i', "
    r"'f^{!}(A_S) \simeq A_X[2d]'); the print's tilde arrows with a drawn head (e.g. p. 7) are a different sign.")

add(31, "second display, after 'On a par suite'",
    "R j_*j^*(F) ≃ i^* R (ij)_* j^*(F) ∈ ob D_c^+(U) . : tilde over a straight bar, no arrowhead",
    r"\R j_{*}j^{*}(F) \xrightarrow{\sim} i^{*} \R(ij)_{*} j^{*}(F)",
    "symbol", "high",
    {"old": r"\xrightarrow{\sim} i^{*}", "new": r"\simeq i^{*}"},
    "")

add(31, "the distinguished triangle, after its bottom right vertex",
    "a full stop after the bottom right vertex: 'R i_* R j_* j^*(F)  .'",
    r"no full stop after the tikzcd diagram",
    "punctuation", "high",
    {"old": r"\arrow[ul]" + NL + r"\end{tikzcd}", "new": r"\arrow[ul]" + NL + r"\end{tikzcd}\quad ."},
    r"Global issue 2 (punctuation after diagrams, reported page by page); \end{tikzcd}\quad . is the form used "
    r"for the same fix in SGA 7 II.")

# ---------------------------------------------------------------- page 32
add(32, "section heading 3.4",
    "'3.4 : Le théorème de bidualité sur les préschémas réguliers.': no other number",
    r"\subsubsection{3.4. Le théorème ...} is unstarred: LaTeX (article class, secnumdepth 3) prints its own "
    r"number 1.2.4 before '3.4.' (section 1 from \section{Définition et propriétés formelles ...} at s5.tex line "
    r"331, subsection 1.2 from \subsection{3. Existence de complexes dualisants} at line 701).",
    "extra", "high",
    {"old": r"\subsubsection{", "new": r"\subsubsection*{"},
    r"Convention of the file, reported once: all 11 unstarred \section/\subsection/\subsubsection of s5.tex "
    r"print automatic numbers that the print does not have (Exposé I lines 331, 595, 701, 703, 791, 847, 928, "
    r"giving e.g. '1.1 2. Unicité ...', '1.2 3. Existence ...', '1.2.1 3.1. Préliminaires.'; the later \section "
    r"at lines 1945, 2082, 2413, 2864 print 2-5): star them in one pass, both layers. The accepted setting of "
    r"underlined titles as \section is not in question, only the automatic number.")

add(32, "section heading 3.4, after the number",
    "'3.4 :' (space and colon; the number not underlined, the title underlined). p. 21 prints '3.1. Préliminaires.' "
    "with a full stop.",
    r"\subsubsection{3.4. Le théorème de bidualité sur les préschémas réguliers.}",
    "punctuation", "medium",
    {"old": "{3.4. Le", "new": "{3.4 : Le"},
    "The print's own variant, not a misprint. Drop it if heading-number punctuation counts as the accepted "
    "setting of underlined titles (like the '. :' of run-in labels). Independent of the previous fix (different "
    "characters).")

add(32, "label of Théorème 3.4.1, the reference in parentheses",
    "'Théorème 3.4.1. (cf. [H] V 2.2.) :': a full stop after 2.2 inside the parenthesis (clear on the scan)",
    r"\subsection*{Théorème 3.4.1 (cf. [H] V 2.2)}",
    "punctuation", "high",
    {"old": "V 2.2)}", "new": "V 2.2.)}"},
    "The '.' after '3.4.1' and the ' :' after the parenthesis are the accepted label typesetting and are not "
    "reported; the full stop inside the reference belongs to the reference (Lemme 1.9 on p. 10 prints "
    "'(cf. [H] II 4.3) :' without one).")

add(32, "proof of Théorème 3.4.1, its label",
    "'Démonstration : Il s'agit de prouver ...': 'Démonstration' underlined, then ' :', run into the text; no "
    "end-of-proof sign where the argument ends on p. 34 ('par hypothèse de récurrence.', end of the proof of "
    "Lemme 3.4.2).",
    r"\begin{proof}[Démonstration] (amsthm: italic 'Démonstration.'), closed by \end{proof} on p. 34 (a square)",
    "other", "high",
    {"old": r"\begin{proof}[Démonstration]" + NL, "new": r"\emph{Démonstration} : "},
    r"Apply together with the removal of \end{proof} on p. 34 (LaTeX fails otherwise). The environment also "
    r"encloses \subsection*{Lemme 3.4.2} and its proof (p. 33). Same form as the global '\emph{Preuve} :'.")

add(32, "end of the statement of Théorème 3.4.1: 'Alors A_X est dualisant (1.6).'",
    "(1.6), clearly typed",
    "Alors $A_X$ est dualisant (1.6).",
    "misprint_in_print", "medium", None,
    "'Dualisant' is Définition 1.7 (p. 8), whose conditions (i)-(iii) the proof checks; Proposition 1.6 (p. 7) is "
    "the bound for quasi-finite morphisms. The TeX keeps the printed (1.6). Decide together with the next finding "
    "and the three (1.11) of pp. 32-34 (the references of 3.4 seem to follow an older numbering of section 1); "
    "pp. 34-35 cite (1.7) for 'dualisant' correctly.",
    corrected="(1.7)", tex_locator="est dualisant (1.6).")

add(32, "start of the proof of 3.4.1: 'satisfait aux conditions (i) à (iii) de (1.6)'",
    "(1.6), clearly typed",
    "satisfait aux conditions (i) à (iii) de (1.6).",
    "misprint_in_print", "medium", None,
    "Proposition 1.6 has no conditions (i)-(iii); Définition 1.7 has them. The TeX keeps the printed reading. "
    "Both or neither with the previous finding. The '(1.7)' four lines below ('reste à prouver, d'après (1.7), "
    "que, pour tout A_X-Module constructible F ...') fits 1.7 (iii) with Remarques 1.8 c) and is not reported.",
    corrected="(1.7)", tex_locator="(i) à (iii) de (1.6)")

add(32, "'(où l'on a posé D_X = R Hom( ,A_X) )'",
    "Hom not underlined: no trace of a rule under it, while the underlines of the D_X on this line and the line "
    "above are crisp; Hom is underlined on pp. 7, 8 and 30",
    r"$\underline{D}_X = \R\,\underline{\Hom}(\quad, A_X)$",
    "misprint_in_print", "medium",
    {"old": r"\R\,\underline{\Hom}(\quad, A_X)", "new": r"\R\,\Hom(\quad, A_X)"},
    "D_X is the sheaf-Hom functor, underlined everywhere else; the typist left the underline out here. The TeX "
    "silently supplies it; the fix restores the printed reading (diplomatic layer only).",
    corrected=r"\R\,\underline{\Hom}(\quad, A_X)")

add(32, "'et par dévissage (3.1.2 (iii bis), on peut se borner'",
    "one closing parenthesis only: '(3.1.2 (iii bis),'",
    "(3.1.2 (iii~bis)),",
    "misprint_in_print", "high",
    {"old": "(3.1.2 (iii~bis)),", "new": "(3.1.2 (iii~bis),"},
    "Unbalanced parenthesis of the print; the TeX silently closes it, the fix restores the printed reading.",
    corrected="(3.1.2 (iii~bis)),")

add(32, "'On a grâce au th. de changement de base (cf. SGAA XVII ) i_!(A'_U) ≃ R h_* i'_!(A'_{U'})'",
    "tilde over a straight bar, no arrowhead",
    r"$i_{!}(A'_U) \xrightarrow{\sim} \R h_{*} i'_{!}(A'_{U'})$",
    "symbol", "high",
    {"old": r"i_{!}(A'_U) \xrightarrow{\sim} \R h_{*}", "new": r"i_{!}(A'_U) \simeq \R h_{*}"},
    "The blank after 'XVII' inside the parenthesis is empty on the scan (spacing, not reported).")

add(32, "display 'f_* i_!(A'_U) ≃ f_* R h_* i'_!(A'_{U'}) ≃ R g_* i'_!(A'_{U'}) ,'",
    "both signs are a tilde over a straight bar, no arrowhead",
    r"f_{*} i_{!}(A'_U) \xrightarrow{\sim} f_{*} \R h_{*} i'_{!}(A'_{U'}) \xrightarrow{\sim} \R g_{*} i'_{!}(A'_{U'}),",
    "symbol", "high",
    {"old": r"\xrightarrow{\sim} f_{*} \R h_{*} i'_{!}(A'_{U'}) \xrightarrow{\sim}",
     "new": r"\simeq f_{*} \R h_{*} i'_{!}(A'_{U'}) \simeq"},
    "")

add(32, "last line: 'En vertu de (1.11), il suffit de prouver que le couple'",
    "(1.11), clearly typed",
    "En vertu de (1.11), il suffit de prouver que le couple",
    "misprint_in_print", "medium", None,
    "The step is Corollaire 1.13 (g = fh proper: if (F, R^!g(A_X)) is bidualisant, so is (Rg_*F, A_X)); "
    "Proposition 1.11 is the exchange of the tensor product and R Hom by D_K. The TeX keeps the printed reading. "
    "The same (1.11) stands on p. 33 ('Par (1.11)') and p. 34 ('Appliquant à nouveau (1.11)'): all three or none, "
    "together with the two (1.6) of this page.",
    corrected="(1.13)", tex_locator="En vertu de (1.11), il suffit")

# ---------------------------------------------------------------- page 33
add(33, "top of the page: '(i'_!(A'_{U'}), R^!g(A_X)) est bidualisant.'",
    "p. 33 begins with '(i'_!(A'_{U'}), R^!g(A_X)) est bidualisant. Plongeant localement Y' dans un'; p. 32 ends "
    "with 'il suffit de prouver que le couple'.",
    r"'$(i'_{!}(A'_{U'}), \R^{!}g(A_X))$ est' ends s5.tex line 940, the last line of page_032.tex; the folio-33 "
    r"marker (line 941) follows it, so page_033.tex begins with 'bidualisant.'",
    "marker", "high", None,
    r"Page 33 really begins at '$(i'_{!}(A'_{U'}), \R^{!}g(A_X))$ est' at the end of s5.tex line 940. Exact fix: "
    r"python -I move_marker.py 5 33 '$(i' --before (the short anchor avoids the quote characters of i'; its last "
    r"occurrence before the marker is this one; simulated in memory on both layers). The marker then splits line "
    r"940 after 'que le couple'. Text not moved; it agrees with the print.")

add(33, "a) p = 1: 'R^!i(A_X) ≃ (μ_n)_Y^{⊗-1}[-2]'",
    "tilde over a straight bar, no arrowhead",
    r"\R^{!}i(A_X) \xrightarrow{\sim} (\mu_n)^{\otimes -1}_Y[-2]",
    "symbol", "high",
    {"old": r"\xrightarrow{\sim} (\mu_n)", "new": r"\simeq (\mu_n)"},
    "")

add(33, "a) p = 1: 'Par (1.11), il suffit de vérifier que (A'_Y, R^!i(A_X)) est bidualisant.'",
    "(1.11), clearly typed",
    "Par (1.11), il suffit de vérifier que",
    "misprint_in_print", "medium", None,
    "As on p. 32: the reduction along the closed immersion i is Corollaire 1.13. The TeX keeps the printed "
    "reading; all three (1.11) of 3.4 or none. Also doubtful, not reported as a finding: Lemme 3.4.2 ends "
    "'est bidualisant (1.4)', but 'bidualisant' is defined in the unnumbered paragraph after Proposition 1.6 "
    "(p. 8) and 1.4 defines the quasi-injective dimension; no certain correction.",
    corrected="(1.13)", tex_locator="Par (1.11), il suffit de vérifier")

# ---------------------------------------------------------------- page 34
add(34, "end of the proof of Lemme 3.4.2 (and of Théorème 3.4.1), before Corollaire 3.4.3",
    "no end-of-proof sign after 'par hypothèse de récurrence.'",
    r"\end{proof} (prints a square)",
    "extra", "high",
    {"old": r"\end{proof}" + NL, "new": ""},
    r"Apply together with the p. 32 label fix (\begin{proof}[Démonstration] -> \emph{Démonstration} : ).")

add(34, "proof of Corollaire 3.4.3: 'dim.q.inj(R^!f(A_S)) ⩽ 2 Sup(dimX'_{ij})'",
    "'Sup' with a capital S",
    r"2\sup(\dim X'_{ij})",
    "word", "high",
    {"old": r"2\sup(\dim X'_{ij})", "new": r"2\operatorname{Sup}(\dim X'_{ij})"},
    r"Capital against small letter (\sup prints 'sup').")

add(34, "'Or R^!f'(A_S) est localement isomorphe à A_X (à translation près de 2d)'",
    "A_X, with no prime on the X",
    "localement isomorphe à $A_X$",
    "misprint_in_print", "high", None,
    "f' : X' -> S is smooth, so R^!f'(A_S) lives on X' and is locally A_{X'} up to the shift 2d. The diplomatic "
    "TeX keeps the printed A_X; the current layer already has A_{X'}.",
    corrected="$A_{X'}$", tex_locator="localement isomorphe à $A_X$")

add(34, "'donc en particulier vérifie les conditions (ii) et (ii) de (1.7), cqfd.'",
    "(ii) et (ii)",
    "les conditions (ii) et (ii) de (1.7)",
    "misprint_in_print", "high", None,
    "The proof set out to check 'les conditions (ii) et (iii) de (1.7)' (same page). The diplomatic TeX keeps the "
    "printed reading; the current layer already has (iii).",
    corrected="(ii) et (iii)", tex_locator="(ii) et (ii) de (1.7)")

add(34, "first paragraph: 'Appliquant à nouveau (1.11) et la pureté'",
    "(1.11), clearly typed",
    "Appliquant à nouveau (1.11) et la pureté",
    "misprint_in_print", "medium", None,
    "As on pp. 32-33 (Corollaire 1.13, for the closed immersion of Y_p); the TeX keeps the printed reading; all "
    "three or none.",
    corrected="(1.13)", tex_locator="Appliquant à nouveau (1.11)")

# ---------------------------------------------------------------- page 35
add(35, "end of 4.1: 'un isomorphisme K_{x} ≃ A.'",
    "tilde over a straight bar, no arrowhead",
    r"K_{\{x\}}\xrightarrow{\sim}A",
    "symbol", "high",
    {"old": r"K_{\{x\}}\xrightarrow{\sim}A", "new": r"K_{\{x\}}\simeq A"},
    r"Earlier on the same page the TeX writes the same printed sign as \simeq ('f^{!}(A_S) \simeq A_X[2d]').")

add(35, "end of the proof of Corollaire 3.4.4: 'car les hypothèses sont bien vérifiées (voir 3.1)).'",
    "two closing parentheses after 3.1; no parenthesis is open earlier in the sentence",
    "bien vérifiées (voir 3.1)).",
    "misprint_in_print", "medium", None,
    "The TeX keeps the printed reading. Another correction would open a parenthesis earlier (e.g. before "
    "'donc f^!(A_S)'), but nothing on the page marks where.",
    corrected="(voir 3.1).", tex_locator="(voir 3.1)).")

# ---------------------------------------------------------------- checks
ok = True
for d in F:
    t = (PAGES / f"page_{d['page']:03d}.tex").read_text(encoding="utf-8")
    fx = d["fix"]
    if fx is not None:
        n = t.count(fx["old"])
        if n != 1 or fx["old"] == fx["new"]:
            ok = False
            print("BAD old", d["page"], n, repr(fx["old"]))
        if "%%%%" in fx["old"]:
            ok = False
            print("marker in old", d["page"])
    loc = d.pop("_loc")
    if loc is not None and t.count(loc) != 1:
        ok = False
        print("locator not unique", d["page"], t.count(loc), repr(loc))
    if d["kind"] == "misprint_in_print" and not d.get("corrected"):
        ok = False
        print("misprint without corrected", d["page"])
# simulate applying all fixes per page, in order, to catch overlaps
for p in range(31, 36):
    t = (PAGES / f"page_{p:03d}.tex").read_text(encoding="utf-8")
    for d in F:
        if d["page"] == p and d["fix"] is not None:
            if t.count(d["fix"]["old"]) != 1:
                ok = False
                print("overlap", p, repr(d["fix"]["old"]))
            t = t.replace(d["fix"]["old"], d["fix"]["new"], 1)
counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0])
    c[1 if d["kind"] == "misprint_in_print" else 0] += 1
print("counts", counts, "total", len(F), "ok", ok)
if ok:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    print("written", OUT)
