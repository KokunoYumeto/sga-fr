import json, os, sys

RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_5"
BATCH = os.path.join(RUN, "b111_115")
OUT = os.path.join(RUN, "findings_111_115.json")

F = []

def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "confidence": confidence, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)

# ---------------- page 111 ----------------
add(111, "4.11, paragraph after the display: 'sa d-ième classe de Chern'",
    "sa d-ième classe de Chern",
    "sa $d$-<line break>ième classe de Chern",
    "other", "medium",
    {"old": "sa $d$-\nième", "new": "sa $d$-ième"},
    "The source line break after '$d$-' typesets as a space ('d- ième'); the print has the one word 'd-ième'.")

add(111, "4.11, 'par la formule de Gauss-Bonnet (SGA 5 VII 4.9)'",
    "Gauss-Bonnet",
    "Gauss--Bonnet",
    "punctuation", "high",
    {"old": "Gauss--Bonnet", "new": "Gauss-Bonnet"},
    "The print has a hyphen; the TeX adds an en dash.")

add(111, "4.11, sentence after (4.11.3): 'caractéristique d'Euler-Poincaré'",
    "d'Euler-Poincaré",
    "d'Euler--Poincaré",
    "punctuation", "high",
    {"old": "Euler--Poincaré", "new": "Euler-Poincaré"},
    "The print has a hyphen; the TeX adds an en dash.")

add(111, "4.11, sentence after (4.11.3): '... de T^F_s pour s un point géométrique au-dessus de s'",
    "de T^F_s pour s un point géométrique au-dessus de s (no bar on either s)",
    "de $T_s^F$ pour $s$ un point géométrique au-dessus de $s$",
    "misprint_in_print", "medium",
    None,
    "No bar is printed over the index s or the first s (the scan is clean there); a geometric point 's' above 's' must be s-bar. The TeX keeps the printed reading.",
    corrected=r"de $T_{\bar s}^F$ pour $\bar s$ un point géométrique au-dessus de $s$")

add(111, "4.11, end: '(loc.cit).'",
    "au-dessus de s (loc.cit).",
    "au-dessus de $s$ (loc. cit.).",
    "punctuation", "high",
    {"old": "(loc. cit.)", "new": "(loc.cit)"},
    "The print has no period after 'cit' (and no space after 'loc.'); the TeX adds them.")

add(111, "4.12, 'Notons s_z ... (resp. t_Z ∈ Hom(L_{2z_2},L_{1z_1}))'",
    "(resp. t_{\\bar Z} ∈ Hom(L_{2\\bar z_2},L_{1\\bar z_1})) — the index of t is a capital Z under the bar",
    "(resp. $t_{\\bar z}\\in\\Hom(L_{2\\bar z_2},L_{1\\bar z_1})$)",
    "misprint_in_print", "medium",
    {"old": r"$t_{\bar z}\in", "new": r"$t_{\bar Z}\in"},
    "The index of t is typed at capital height (a capital Z), unlike the small z of s_{\\bar z} on the same line; the TeX silently corrects it.",
    corrected=r"$t_{\bar z}\in")

add(111, "4.12, 'Notons encore ...': 'définie, au voisinage de a' (resp. a'') par c'_2'",
    "au voisinage de a' (resp. a'') par c'_2 (resp. c''_1)",
    "au voisinage de $a'$ (resp. $a''$), par $c_2'$ (resp. $c_1''$)",
    "punctuation", "high",
    {"old": "(resp. $a''$), par", "new": "(resp. $a''$) par"},
    "No comma after '(resp. a'')' in the print; the TeX adds one.")

add(111, "4.12, 'et (C'.C'')_z le terme local'",
    "(C'.C'')_z — a typed baseline period between C' and C''",
    "$(C'\\!\\cdot C'')_z$",
    "symbol", "low",
    {"old": r"$(C'\!\cdot C'')_z$", "new": r"$(C'.C'')_z$"},
    "The print has a period, the TeX a centred dot (same on page 112, 4.12.1). Drop both if the typed period is treated as the typewriter's substitute for \\cdot.")

# ---------------- page 112 ----------------
add(112, "4.12, 'lisses). On a alors' before (4.12.1)",
    "lisses). On a alors",
    "lisses). On a alors:",
    "punctuation", "high",
    {"old": "On a alors:", "new": "On a alors"},
    "No colon in the print (only a faint speck at mid-height after 'alors'); the TeX adds one.")

add(112, "(4.12.1)",
    "< u,v >_z = (C'.C'')_z < s_z,t_z >  .",
    "\\langle u,v\\rangle_z=(C'\\!\\cdot C'')_z\\langle s_{\\bar z},t_{\\bar z}\\rangle.",
    "symbol", "low",
    {"old": r"(C'\!\cdot C'')_z\langle", "new": r"(C'.C'')_z\langle"},
    "Baseline period in the print, centred dot in the TeX (see page 111).")

add(112, "4.13, last paragraph: 'on obtient la formule de lefschetz requise dans ([13] 7.11)'",
    "la formule de lefschetz requise",
    "la formule de Lefschetz requise",
    "misprint_in_print", "high",
    {"old": "formule de Lefschetz requise", "new": "formule de lefschetz requise"},
    "The print types a small l; the TeX silently capitalizes it.",
    corrected="formule de Lefschetz requise")

# ---------------- page 113 ----------------
add(113, "top of page",
    "Page 113 begins with the underlined heading '5. Compléments.'; page 112 ends with '... sera donnée dans III B .'",
    "'\\section*{5. Compléments}' is the last line of page_112.tex, before the folio-113 marker",
    "marker", "high",
    None,
    "Move the folio-113 marker up so that it stands before '\\section*{5. Compléments}' (the blank lines after '\\end{statement}' stay on page 112).")

add(113, "5.1, first paragraph: 'dite duale de u'",
    "dite duale de u — only 'duale' is underlined",
    "dite \\emph{duale de $u$}",
    "underline", "high",
    {"old": r"\emph{duale de $u$}", "new": r"\emph{duale} de $u$"},
    "The underline covers 'duale' only.")

add(113, "(5.1.2)",
    "D : RHom(p^*_1L_1,p^!_2L_2) ⟶ RHom(p^*_2DL_2,p^!_1DL_1) — plain arrow, no tilde",
    "D:\\uRHom(p_1^*L_1,p_2^!L_2)\\xrightarrow{\\sim}\\uRHom(p_2^*DL_2,p_1^!DL_1)",
    "symbol", "high",
    {"old": r"p_2^!L_2)\xrightarrow{\sim}\uRHom", "new": r"p_2^!L_2)\longrightarrow\uRHom"},
    "No tilde over the arrow of 5.1.2 (clean scan); the TeX adds one. 5.1.5 does print a tilde.")

add(113, "(5.1.3), bottom right vertex of the square",
    "RHom(p^*_2DL_2,p^!_1DL_1   , — no closing parenthesis",
    "& \\uRHom(p_2^*DL_2,p_1^!DL_1),",
    "misprint_in_print", "high",
    {"old": "p_1^!DL_1),", "new": "p_1^!DL_1,"},
    "The print omits the closing parenthesis; the TeX silently supplies it.",
    corrected="p_1^!DL_1),")

add(113, "(5.1.5)",
    "D : Hom(c^*_1L_1,c^!_2L_1) ⟶~ Hom(c^*_2DL_2,c^!_1DL_1) ,",
    "D:\\Hom(c_1^*L_1,c_2^!L_1)\\xrightarrow{\\sim}\\Hom(c_2^*DL_2,c_1^!DL_1),",
    "misprint_in_print", "high",
    None,
    "The print has c^!_2 L_1 where the correspondence from L_1 to L_2 needs c^!_2 L_2; the TeX keeps the printed reading.",
    corrected=r"D:\Hom(c_1^*L_1,c_2^!L_2)")

# ---------------- page 114 ----------------
add(114, "top of page",
    "Page 114 begins 'les identifications de Dc^*_1 à c^!_1D ...'; page 113 ends '... application du foncteur D_X et'",
    "'les' is the last word of page_113.tex ('du foncteur $D_X$ et les'); page_114.tex begins 'identifications de'",
    "marker", "high",
    None,
    "The folio-114 marker belongs between 'et' and 'les' (end of page_113.tex).")

add(114, "heading 5.2",
    "5.2 Composition de correspondances. — no period after the number",
    "\\subsection*{5.2. Composition de correspondances}",
    "punctuation", "high",
    {"old": "5.2. Composition", "new": "5.2 Composition"},
    "The print numbers this heading '5.2' without a period (unlike '5.1.').")

# ---------------- page 115 ----------------
add(115, "top of page",
    "Page 115 begins 'l'identification au second membre ...'; page 114 ends with the display (5.2.2)",
    "the line \"l'%\" is the last line of page_114.tex; page_115.tex begins 'identification au second membre'",
    "marker", "high",
    None,
    "The folio-115 marker belongs before the line \"l'%\" (end of page_114.tex).")

add(115, "first sentence: '(SGA 4 XVIII 3.1.12.2)), d'où un accouplement'",
    "(SGA 4 XVIII 3.1.12.2)), d'où",
    "(SGA~4~XVIII 3.1.12.2), d'où",
    "misprint_in_print", "high",
    {"old": "3.1.12.2),", "new": "3.1.12.2)),"},
    "The print doubles the closing parenthesis; the TeX silently drops one.",
    corrected="3.1.12.2),")

add(115, "display after 'par composition de la flèche', second line",
    "⊗ RHom(p^!_{23}p^*_{23,2}L_2,p^!_3L_3 — no closing parenthesis",
    "\\uRHom(p_{23}^!p_{23,2}^*L_2,p_3^!L_3)",
    "misprint_in_print", "high",
    {"old": "p_3^!L_3)\n\\]", "new": "p_3^!L_3\n\\]"},
    "The print omits the closing parenthesis at the end of the display; the TeX silently supplies it.",
    corrected="p_3^!L_3)")

add(115, "'de la flèche définie par la flèche de changement de base ...'",
    "p^*_{12}p^!_{12,2}L_2 ⟶ p^!_{23}p^*_{23,2}L_2",
    "$p_{12}^!p_{12,2}^*L_2\\to p_{23}^!p_{23,2}^*L_2$",
    "formula", "high",
    {"old": "base $p_{12}^!p_{12,2}^*L_2", "new": "base $p_{12}^*p_{12,2}^!L_2"},
    "The TeX swaps * and ! on the source of the base-change arrow; the print has p^*_{12}p^!_{12,2}L_2, as in the display above.")

add(115, "before (5.2.5): 'd'où un accouplement \" composition\" (u,v) ⟶ vu :'",
    "(u,v) ⟶ vu : — plain arrow",
    "$(u,v)\\mapsto vu$:",
    "symbol", "high",
    {"old": r"$(u,v)\mapsto vu$:", "new": r"$(u,v)\longrightarrow vu$:"},
    "Plain arrow here, without the tail bar; the earlier 'que l'on notera (u,v) ⟼ vu' does print a maps-to arrow.")

# ---------------- checks ----------------
ok = True
for f in F:
    fx = f["fix"]
    if fx is None:
        continue
    path = os.path.join(BATCH, "page_%03d.tex" % f["page"])
    with open(path, encoding="utf-8", newline="") as h:
        txt = h.read()
    n = txt.count(fx["old"])
    if n != 1:
        ok = False
        print("COUNT", n, f["page"], repr(fx["old"]))
    # never across or touching a marker line
    if "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]:
        ok = False
        print("MARKER in fix", f["page"], repr(fx["old"]))

with open(OUT, "w", encoding="utf-8", newline="\n") as h:
    json.dump(F, h, ensure_ascii=False, indent=1)
    h.write("\n")

from collections import Counter
c = Counter()
for f in F:
    c[(f["page"], f["kind"] == "misprint_in_print")] += 1
for p in range(111, 116):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
print("all old unique:", ok, "total", len(F))
