"""Build findings_211_215.json for SGA 6 pp. 211-215 and check that every fix's "old" occurs exactly once in its page."""
import json
import pathlib

B = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\b211_215")
OUT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\findings_211_215.json")
NL = "\n"


def L(*lines):
    """Join raw lines with LF."""
    return NL.join(lines)


F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": confidence, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- p. 211
add(211, "top of the page",
    "p. 211 begins with '(loc.cit.)' on its own line, followed by the display C^oo(X,E) = lim_r C^r_2(X,E) .",
    "'(loc.cit.)' ends the last line of page_210.tex ('... d'image dense, et l'on a (loc.cit.)'), under the folio-210 "
    "marker; page_211.tex begins with the display.",
    "marker", "high", None,
    "Page 211 really begins with '(loc.cit.)'. Move the folio-211 marker up: python -I move_marker.py 6 211 "
    "'(loc.cit.)' --before (simulated in memory on both layers: '... et l'on a ' / marker / '(loc.cit.)' / "
    "'\\[ C^\\infty(X,E)=...'). Not a whole TeX line, so the 10 Nov script could not move it.")

add(211, "3.0.5, 'dans celle des O_S rep. O_S (x) C -Modules'",
    "des O_S rep. O_S(x)C -Modules: 'rep.' for 'resp.' (the same sentence has 'reels resp. complexes').",
    r"des $\cO_S$ rep. $\cO_S\otimes\mathbb C$-Modules",
    "misprint_in_print", "high", None,
    "Typing slip of the print; the TeX keeps the printed reading.",
    corrected="resp.")

# ---------------- p. 212
add(212, "3.1.3, item (i), 'les phi_r sont continues'",
    "(i) les phi_r sont continues (l'espace d'arrivee est un espace de Banach: the single word 'continues' is "
    "underlined.",
    r"\item les $\varphi_r$ sont continues (l'espace",
    "underline", "medium",
    {"old": r"sont continues (l'espace", "new": r"sont \emph{continues} (l'espace"},
    "An emphasized word in the running text of 3.1.3, not a statement underlined word group by word group "
    "(GLOBAL_ISSUES 82), so a script for the statements would not catch it. \\emph is the file's command for "
    "underlined words (\\emph{Preuve.}).")

# ---------------- p. 213
add(213, "top of the page",
    "p. 213 begins with '(3.0.2)) ;' (the end of item (i)), then '(ii) phi = lim phi_r (i.e. pour u in "
    "Diff^n_C(E,F), ...'; p. 212 ends with '(i) les phi_r sont continues (l'espace d'arrivee est un espace de "
    "Banach' and the footnote.",
    "'(3.0.2))~;' (end of the \\item line) and the line '\\item $\\varphi=\\varprojlim\\varphi_r$ (i.e.' stand at the "
    "end of page_212.tex, above the folio-213 marker; page_213.tex begins with 'pour $u\\in...'.",
    "marker", "high", None,
    "Page 213 really begins with '(3.0.2))~;'. Move the folio-213 marker up: python -I move_marker.py 6 213 "
    "'(3.0.2))~;' --before (simulated in memory on both layers: '\\item les $\\varphi_r$ sont continues "
    "(l'espace d'arrivée est un espace de Banach ' / marker / '(3.0.2))~;' / '\\item $\\varphi=\\varprojlim"
    "\\varphi_r$ (i.e.' / 'pour $u\\in ...'). The marker stood two TeX lines too late.")

add(213, "Lemme 3.1.4, 'V une variete compacte, E et F des fibres vectoriels complexes'",
    "Soient S un espace topologique, V une variete compacte, E et F des fibres vectoriels complexes de rang fini "
    "sur V, et n in N.",
    r"$V$ une variété compacte, et $E,F$ des fibrés vectoriels complexes",
    "word", "high",
    {"old": r"compacte, et $E,F$ des fibrés", "new": r"compacte, $E$ et $F$ des fibrés"},
    "The TeX adds 'et' before E and writes 'E,F' for the printed 'E et F'.")

add(213, "Lemme 3.1.4, 'Pour u in Diff^n_C(pr_2^*(E),pr_2^*(F)), l'application'",
    "the formula stands in the running text: 'Notons X la S-variete mixte S x V. Pour u in "
    "Diff^n_C(pr_2^*(E),pr_2^*(F)),' is one line, followed by 'l'application s |-> i_s^*(u) de S dans ...'.",
    r"a display \[ u\in\Diff^n_\mathbb C(\pr_2^*(E),\pr_2^*(F)), \]",
    "other", "medium",
    {"old": L(r"Pour", r"\[", r"  u\in\Diff^n_\mathbb C(\pr_2^*(E),\pr_2^*(F)),", r"\]", r"l'application"),
     "new": r"Pour $u\in\Diff^n_\mathbb C(\pr_2^*(E),\pr_2^*(F))$, l'application"},
    "The print sets the formula inline; the TeX makes it a display (same kind of fix as SGA 6 pp. 21, 34, 42).")

add(213, "Preuve of 3.1.4, 'on est alors ramene a montrer que pour u in Gamma(X,pr_2^*(G))'",
    "montrer que pour (no comma after 'que').",
    r"montrer que, pour",
    "punctuation", "high",
    {"old": r"montrer que, pour", "new": r"montrer que pour"},
    "The TeX adds a comma.")

add(213, "3.1.5, display u in Diff^n(pr_2^*(E),pr_2^*(F)) and the call of footnote (1)",
    "the call (1) stands after the display and its full stop: 'u in Diff^n(pr_2^*(E),pr_2^*(F))  . (1)'; "
    "nothing follows 'soit' in the text line.",
    r"soit\footnote{On omet l'indice $\mathbb C$ pour abréger.} followed by the display",
    "other", "medium",
    {"old": L(r"soit\footnote{On omet l'indice $\mathbb C$ pour abréger.}", r"\[",
              r"  u\in\Diff^n(\pr_2^*(E),\pr_2^*(F)).", r"\]"),
     "new": L(r"soit", r"\[", r"  u\in\Diff^n(\pr_2^*(E),\pr_2^*(F)).\text{\footnotemark}", r"\]",
              r"\footnotetext{On omet l'indice $\mathbb C$ pour abréger.}")},
    "Puts the call where the print has it, with \\text{\\footnotemark} in the display and \\footnotetext after it, "
    "as main.tex does elsewhere (e.g. '\\longrightarrow G\\text{\\footnotemark}.' and its \\footnotetext).")

add(213, "parenthesis after item (ii), '(loc.cit) : on se ramene aussitot a n = 0'",
    "(loc.cit) : no full stop after 'cit' (p. 211 prints '(loc.cit.)').",
    r"(loc.cit)~:",
    "misprint_in_print", "low", None,
    "Typing slip (abbreviation stop left out); the TeX keeps the printed reading.",
    corrected="(loc.cit.)")

# ---------------- p. 214
add(214, "display u_r : C'(S,C^r_2(V,E)) -> C'(S,C^r_2(V,F)) .",
    "u_r : C'(S,C^r_2(V,E)) --> C'(S,C^r_2(V,F))  . : the target has C^r_2, superscript r (main scan clear).",
    r"u_r:\underline C'(S,C^r_2(V,E)) \longrightarrow \underline C'(S,C^r_2(V,F)).",
    "misprint_in_print", "medium", None,
    "u_r is defined by phi_r u : S --> L(C^r_2(V,E),C^{r-n}_2(V,F)) (display just above; also the morphism "
    "S x C^r_2(V,E) --> S x C^{r-n}_2(V,F) at the foot of the page, and d^i_{r-m_i} on p. 215), so its target is "
    "C'(S,C^{r-n}_2(V,F)). The TeX keeps the printed reading; in the corrected layer replace "
    "'\\underline C'(S,C^r_2(V,F))' (once on the page).",
    corrected=r"\underline C'(S,C^{r-n}_2(V,F))")

# ---------------- p. 215
add(215, "Theoreme 3.2.1, 'Alors le complexe Rp_*(E^.)'",
    "R with a double underline (the typescript's double-struck R of the derived functor), then p_*(E^.).",
    r"$Rp_*(E^\bullet)$ (plain R)",
    "font", "high",
    {"old": r"$Rp_*(E^\bullet)$", "new": r"$\mathbb{R}p_*(E^\bullet)$"},
    "Double-struck derived-functor R written plain (reported singly as asked); main.tex writes "
    "\\mathbb{R}f_* elsewhere.")

add(215, "Preuve of 3.2.1, 'un complexe de prefaisceaux (C'(S,C_2^{r-m_i}(V,F^i)),d^i_{r-m_i}), que nous "
    "noterons C'(S,C^r_2(V,F^.)).'",
    "the formula and 'que nous noterons C'(S,C^r_2(V,F^.)).' are one line of running text at the left margin, "
    "followed by 'Les C'(S,C^r_2(V,F^.)) forment un systeme projectif'.",
    r"a display \[ \bigl(\underline C'(S,C_2^{r-m_i}(V,F^i)),d_{r-m_i}^i\bigr),\quad\text{que nous noterons } "
    r"\underline C'(S,C_2^r(V,F^\bullet)). \]",
    "other", "medium",
    {"old": L(r"un complexe de préfaisceaux", r"\[",
              r"  \bigl(\underline C'(S,C_2^{r-m_i}(V,F^i)),d_{r-m_i}^i\bigr),\quad\text{que nous noterons } "
              r"\underline C'(S,C_2^r(V,F^\bullet)).",
              r"\]", r"Les"),
     "new": L(r"un complexe de préfaisceaux $\bigl(\underline C'(S,C_2^{r-m_i}(V,F^i)),d_{r-m_i}^i\bigr)$, "
              r"que nous noterons $\underline C'(S,C_2^r(V,F^\bullet))$.", r"Les")},
    "The print sets this in the running text; the TeX makes it a display with the words in \\text.")

add(215, "Preuve of 3.2.1, 'que le complexe de faisceaux associes a C'(S,C^r_2(V,F^.))'",
    "associés (plural, as 'le morphisme de faisceaux associés à u_r' at the top of the page).",
    r"que le complexe de faisceaux associé à",
    "word", "high",
    {"old": r"de faisceaux associé à", "new": r"de faisceaux associés à"},
    "The TeX changes the printed plural (agreeing with 'faisceaux') to the singular (agreeing with 'complexe'); "
    "the printed reading is good French and stands.")

# ---------------- checks
ok = True
texts = {p: (B / f"page_{p:03d}.tex").read_text(encoding="utf-8") for p in range(211, 216)}
for d in F:
    fx = d["fix"]
    if fx is None:
        continue
    n = texts[d["page"]].count(fx["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE", d["page"], n, repr(fx["old"][:60]))
    if "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]:
        ok = False
        print("MARKER IN FIX", d["page"])
counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0])
    c[1 if d["kind"] == "misprint_in_print" else 0] += 1
print("all olds unique:", ok)
print("counts (normal/misprint):", {p: f"{a}/{b}" for p, (a, b) in sorted(counts.items())})
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print("written", OUT, len(F), "findings")
