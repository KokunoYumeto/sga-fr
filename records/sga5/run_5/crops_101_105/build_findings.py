"""Build findings_101_105.json (pages 101-105 of SGA 5) and check that every fix's old occurs once in its page."""
import json
import pathlib

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
B = RUN / "b101_105"
OUT = RUN / "findings_101_105.json"

F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": confidence,
         "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- p. 101
add(101, "end of diagram (4.2.6)",
    "a comma stands to the right of the diagram, after H^o(E',K_{E'}) of the lower row",
    "no punctuation after the tikzcd",
    "punctuation", "high",
    {"old": "\\end{tikzcd}\n\\end{equation}", "new": "\\end{tikzcd}\\quad,\n\\end{equation}"},
    "The sentence runs on after the diagram ('où les flèches verticales ...').")

add(101, "'et de la restriction H^0(E'',K_{E''}) -> H^0(E',K_{E'})'",
    "H^o(E',K_E), : the subscript of the second K is a plain E, no prime (sharp; the primes of E'' and of the "
    "first E' on the line are clear)",
    "\\H^0(E',K_{E'}),",
    "misprint_in_print", "high",
    {"old": "\\longrightarrow \\H^0(E',K_{E'}),", "new": "\\longrightarrow \\H^0(E',K_E),"},
    "The TeX silently corrects. The restriction goes to H^0(E',K_{E'}), the lower right corner of 4.2.6.",
    corrected="\\H^0(E',K_{E'})")

add(101, "'avec E'' = C' x_{X'} D''",
    "C' x_{X'} D': a typed prime after the subscript X, the same stroke as the primes of C' and D' (checked "
    "magnified)",
    "C'\\times_{X}D'",
    "misprint_in_print", "medium",
    {"old": "C'\\times_{X}D'", "new": "C'\\times_{X'}D'"},
    "The TeX silently corrects (or drops the prime). No X' is defined here: on p. 100 C' and D' lie over X "
    "(c', d' are the composites C' -> C -> X, D' -> D -> X), so E'' is C' x_X D', the analogue of E = C x_X D.",
    corrected="C'\\times_{X}D'")

add(101, "label of Exemple 4.3",
    "'Exemple 4.3 - On suppose ...': 'Exemple' underlined, then the number and a typewriter dash, the text run in",
    "\\begin{statement}{Exemple 4.3} (the environment prints 'Exemple 4.3.')",
    "punctuation", "high",
    {"old": "\\begin{statement}{Exemple 4.3}", "new": "\\begin{statement}{Exemple 4.3 -}"},
    "Exposé III label form. The statement environment appends a full stop (\\textbf{#1.}), so the label then "
    "renders 'Exemple 4.3 -.'; the environment's full stop needs one decision (see message).")

add(101, "display 'A_X(r_1)[2r_1] (x)^L A_X(r_2)[2r_2] -> A_X(r)[2r]'",
    "no punctuation after A_X(r)[2r]; the next line begins '(où r = r_1 + r_2) ,'",
    "A_X(r)[2r],",
    "extra", "high",
    {"old": "A_X(r)[2r],", "new": "A_X(r)[2r]"},
    "The comma the TeX puts at the end of the display stands in the print after the parenthesis that follows "
    "(next finding).")

add(101, "'(où r = r_1 + r_2) , et par suite'",
    "(où r = r_1 + r_2) , : the clause in parentheses, the comma after the closing parenthesis",
    "où $r=r_1+r_2$, et par suite",
    "punctuation", "high",
    {"old": "où $r=r_1+r_2$,", "new": "(où $r=r_1+r_2$),"},
    "Parentheses left out by the TeX.")

add(101, "'la classe de c (resp. d) (3.2.a))'",
    "(3.2.a)) : a full stop between 2 and a",
    "(3.2 a))",
    "punctuation", "high",
    {"old": "(3.2 a))", "new": "(3.2.a))"},
    "Stays on p. 101 after the folio-102 marker move.")

# ---------------------------------------------------------------- p. 102
add(102, "top of the page",
    "p. 102 begins 'z de C ∩ D , < cl(c), cl(d) >_z n'est autre que l'image dans A de la multiplicité'; "
    "p. 101 ends '(SGA 4^{1/2} Cycle 2.3.8) qu'en un point isolé' (blank below)",
    "'$z$ de $C\\cap D$, $\\langle \\cl(c),\\cl(d)\\rangle_z$ n'est' ends s5.tex line 3034 (diplomatic; 3035 in "
    "current), the last line of page_101.tex; the folio-102 marker follows it",
    "marker", "high", None,
    "Page 102 really begins at '$z$ de $C\\cap D$' near the end of s5.tex line 3034. Exact fix: "
    "python -I move_marker.py 5 102 '$z$ de $C' --before (single quotes: the anchor contains $; it occurs twice "
    "in s5.tex and rfind takes the one just before the marker; simulated in memory on both layers: the marker "
    "then splits line 3034 after 'qu'en un point isolé ', and page 102 begins '$z$ de $C\\cap D$, ... n'est' + "
    "'autre que l'image'). Text not moved; it agrees with the print. No fix of this batch touches the anchor.")

add(102, "label of Théorème 4.4",
    "'Théorème 4.4 - Soient, ...': 'Théorème' underlined, then the number and a typewriter dash",
    "\\begin{statement}{Théorème 4.4}",
    "punctuation", "high",
    {"old": "\\begin{statement}{Théorème 4.4}", "new": "\\begin{statement}{Théorème 4.4 -}"},
    "As Exemple 4.3 (p. 101); the environment's appended full stop remains.")

add(102, "Théorème 4.4, 'Soient, pour i = 1, 2, f_i : X_i -> Y_i un S-morphisme propre,'",
    "'Soient', 'pour', 'un' and 'morphisme propre' underlined (four rules; the S-, the formulas and the commas "
    "are not underlined)",
    "no underline",
    "underline", "high",
    {"old": "Soient, pour $i=1,2$, $f_i:X_i\\longrightarrow Y_i$ un $S$-morphisme propre,",
     "new": "\\emph{Soient}, \\emph{pour} $i=1,2$, $f_i:X_i\\longrightarrow Y_i$ \\emph{un} "
            "$S$-\\emph{morphisme propre},"},
    "The print underlines the words (not the formulas) of the whole statement of Théorème 4.4, as the statement "
    "of Proposition 1.7.4 (p. 79); \\emph is this file's command for the underline. Six findings for the "
    "statement, one per sentence.")

add(102, "Théorème 4.4, 'les projections. Soit d'autre part'",
    "'les projections' and 'Soit d'autre part' underlined (the full stop not)",
    "no underline",
    "underline", "high",
    {"old": "les projections. Soit d'autre part",
     "new": "\\emph{les projections}. \\emph{Soit d'autre part}"},
    "Underlined statement.")

add(102, "Théorème 4.4, 'un cube commutatif à faces horizontales cartésiennes, avec c', c'', d', d'' propres. "
         "On pose'",
    "'un cube commutatif à faces horizontales cartésiennes', 'avec', 'propres' and 'On pose' underlined; the "
    "formulas and the punctuation not",
    "no underline",
    "underline", "high",
    {"old": "un cube commutatif à faces horizontales cartésiennes, avec $c'$, $c''$, $d'$, $d''$ propres. On pose",
     "new": "\\emph{un cube commutatif à faces horizontales cartésiennes}, \\emph{avec} $c'$, $c''$, $d'$, $d''$ "
            "\\emph{propres}. \\emph{On pose}"},
    "Underlined statement.")

add(102, "Théorème 4.4, 'Enfin, soient L_i ∈ ob D_ctf(X_i). On a alors un carré commutatif'",
    "'Enfin', 'soient' and 'On a alors un carré commutatif' underlined",
    "no underline",
    "underline", "high",
    {"old": "Enfin, soient $L_i\\in\\ob \\Dctf(X_i)$. On a alors un carré commutatif",
     "new": "\\emph{Enfin}, \\emph{soient} $L_i\\in\\ob \\Dctf(X_i)$. \\emph{On a alors un carré commutatif}"},
    "Underlined statement.")

add(102, "Théorème 4.4 after (4.4.1), 'où M_i = f_{i*}L_i , (3) est donné par 4.2.4, (1) déduit de 4.2.4 par "
         "application de f_* et composition avec la flèche canonique'",
    "'où', 'est donné par', 'déduit de', 'par application de' and 'et composition avec la flèche canonique' "
    "underlined; the formulas and the numbers not",
    "no underline",
    "underline", "high",
    {"old": "où $M_i=f_{i*}L_i$, $(3)$ est donné par 4.2.4, $(1)$ déduit de 4.2.4 par application de $f_*$ et "
            "composition avec la flèche canonique",
     "new": "\\emph{où} $M_i=f_{i*}L_i$, $(3)$ \\emph{est donné par} 4.2.4, $(1)$ \\emph{déduit de} 4.2.4 "
            "\\emph{par application de} $f_*$ \\emph{et composition avec la flèche canonique}"},
    "Underlined statement.")

add(102, "Théorème 4.4, '(2) est produit tensoriel des flèches 3.7.5 relatives aux faces contenant f , et (4) "
         "est défini par la flèche d'adjonction'",
    "'est produit tensoriel des flèches', 'relatives aux faces contenant', 'et' and 'est défini par la flèche "
    "d'adjonction' underlined",
    "no underline",
    "underline", "high",
    {"old": "$(2)$ est produit tensoriel des flèches 3.7.5 relatives aux faces contenant $f$, et $(4)$ est défini "
            "par la flèche d'adjonction",
     "new": "$(2)$ \\emph{est produit tensoriel des flèches} 3.7.5 \\emph{relatives aux faces contenant} $f$, "
            "\\emph{et} $(4)$ \\emph{est défini par la flèche d'adjonction}"},
    "Underlined statement.")

add(102, "Théorème 4.4, the canonical arrow 'f_*c'_* (x)^L f_*c''_* -> f_*(c'_* (x)^L c''_*)'",
    "f_*c'_* (x)^L f_*c''_* --> f_*(c'_* (x)^L c''_*) , : the functors without arguments, no (-)",
    "f_*c'_*(-)\\otimes^{\\mathbf L} f_*c''_*(-)\\longrightarrow f_*(c'_*(-)\\otimes^{\\mathbf L}c''_*(-)),",
    "extra", "high",
    {"old": "f_*c'_*(-)\\otimes^{\\mathbf L} f_*c''_*(-)\\longrightarrow f_*(c'_*(-)\\otimes^{\\mathbf L}c''_*(-)),",
     "new": "f_*c'_*\\otimes^{\\mathbf L} f_*c''_*\\longrightarrow f_*(c'_*\\otimes^{\\mathbf L}c''_*),"},
    "The TeX adds four (-). The comma is the print's (', (2) est produit ...').")

add(102, "proof label of Théorème 4.4",
    "'Démonstration - Posons ...': 'Démonstration' underlined, then a typewriter dash",
    "\\begin{prooftext}[Démonstration] (the environment prints \\emph{Démonstration.})",
    "punctuation", "high",
    {"old": "\\begin{prooftext}[Démonstration]", "new": "\\begin{prooftext}[Démonstration -]"},
    "A proof label of another form than 'Preuve :'. The prooftext environment appends a full stop "
    "(\\emph{#1.}), so the label then renders 'Démonstration -.'; see message.")

# ---------------------------------------------------------------- p. 103
add(103, "'a) Commutativité de (D). Il suffit de prouver que le carré'",
    "'Commutativité de' underlined; 'a)' and '(D).' not",
    "a) Commutativité de $(D)$. (no underline)",
    "underline", "high",
    {"old": "a) Commutativité de $(D)$.", "new": "a) \\emph{Commutativité de} $(D)$."},
    "Run-in heading of the proof, as 'b) Commutativité de (A)' (p. 104); \\emph is the file's underline.")

# ---------------------------------------------------------------- p. 104
add(104, "top of the page",
    "p. 104 begins with the formula 'f_{i*}DL_i (x)^L f_{i*}L_i --> f_{i*}(DL_i (x)^L L_i) et de la flèche "
    "définie par la flèche d'évaluation,'; p. 103 ends '(1) le composé de la flèche canonique' (blank below)",
    "the display '\\[ f_{i*}DL_i\\otimes^{\\mathbf L} f_{i*}L_i\\longrightarrow f_{i*}(DL_i\\otimes^{\\mathbf L}L_i) "
    "\\]' and 'et de la flèche' (s5.tex lines 3175-3178 diplomatic, 3176-3179 current) end page_103.tex; the "
    "folio-104 marker follows them",
    "marker", "high", None,
    "Page 104 really begins at the '\\[' line of that display (s5.tex line 3175 diplomatic, 3176 current). Exact "
    "fix: python -I move_marker.py 5 104 '\\[' --before (single quotes; rfind takes the last '\\[' before the "
    "marker, the opening of this display; simulated in memory on both layers: the marker then stands between "
    "'... le composé de la flèche canonique' and '\\[', and page 104 begins with the display, 'et de la flèche', "
    "'définie par la flèche d'évaluation'). Text not moved; it agrees with the print. No fix of this batch "
    "touches the moved lines.")

add(104, "'il suffit de voir que le carré suivant commute' before (4.4.5)",
    "'... le carré suivant commute' with no punctuation; the diagram follows",
    "le carré suivant commute:",
    "extra", "high",
    {"old": "le carré suivant commute:", "new": "le carré suivant commute"},
    "Colon added by the TeX.")

add(104, "(4.4.5), lower left 'RHom(f_{i*}L_i', f_{i*}K_{X_i})'",
    "RHom(f_{i*}L'_i, f_{i*}K_{X_i}) : a small typed prime after the L (sharp, apostrophe-shaped)",
    "\\uRHom(f_{i*}L'_i,f_{i*}K_{X_i})",
    "misprint_in_print", "medium",
    None,
    "The TeX keeps the printed reading. The arrow (3) is the canonical arrow f_{i*}RHom(L_i,K_{X_i}) -> "
    "RHom(f_{i*}L_i,f_{i*}K_{X_i}) tensored with f_{i*}L_i (text below and the display above): L_i, no prime.",
    corrected="\\uRHom(f_{i*}L_i,f_{i*}K_{X_i})")

add(104, "'pour toute flèche N_i -> f_{i*}L_i de D_ctf(X_i)'",
    "de D_ctf(X_i) (clear)",
    "de $\\Dctf(X_i)$",
    "misprint_in_print", "medium",
    None,
    "The TeX keeps the printed reading. N_i lives on Y_i (L_i = f_i^*N_i; RHom(N_i, f_{i*}K_{X_i})), and a type-1 "
    "arrow L -> M over f is an element of Hom(f^*M,L) = Hom(M,f_*L) (1.4), so the arrow N_i -> f_{i*}L_i is one "
    "of D_ctf(Y_i).",
    corrected="\\Dctf(Y_i)")

add(104, "'b) Commutativité de (A). Se reportant à la définition de 3.7.3'",
    "'Commutativité de' underlined; 'b)' and '(A).' not",
    "b) Commutativité de $(A)$. (no underline)",
    "underline", "high",
    {"old": "b) Commutativité de $(A)$.", "new": "b) \\emph{Commutativité de} $(A)$."},
    "As 'a) Commutativité de (D)' (p. 103).")

# ---------------------------------------------------------------- p. 105
add(105, "first diagram, upper right 'c_*c^!(P (x)^L Q)'",
    "c_*c^!(P (x)^L Q): the shriek directly after the c, no prime (magnified; the primes of c'^! in the same "
    "row are clear)",
    "c_*c'^!(P\\otimes^{\\mathbf L} Q)",
    "formula", "high",
    {"old": "c_*c'^!(P\\otimes^{\\mathbf L} Q)", "new": "c_*c^!(P\\otimes^{\\mathbf L} Q)"},
    "c^!, as in the square (A) of 4.4.2 (f_*c_*c^!(P (x)^L Q)).")

add(105, "first diagram, lower right 'd_*d^!(P (x)^L Q)'",
    "d_*d^!(P (x)^L Q): no prime on d, and an L above the tensor sign (as in every other tensor of the diagram)",
    "d_*d'^!(P\\otimes Q)",
    "formula", "high",
    {"old": "d_*d'^!(P\\otimes Q)", "new": "d_*d^!(P\\otimes^{\\mathbf L} Q)"},
    "Two differences in one formula: the TeX adds a prime and drops the derived L (written here in the form the "
    "file uses for the other tensors of the diagram, \\otimes^{\\mathbf L}, for the global derived-tensor pass).")

add(105, "end of the first diagram",
    "no punctuation after d_*d^!(P (x)^L Q); the next line begins 'dans lequel'",
    "d_*d'^!(P\\otimes Q),",
    "extra", "high",
    {"old": ",\n\\arrow[from=1-1", "new": "\n\\arrow[from=1-1"},
    "Comma added by the TeX. Independent of the previous fix (the olds do not overlap).")

add(105, "between the two triangles over C' and C'' ('au-dessus de ... et ...')",
    "the word 'et' stands between the two triangles",
    "\\qquad only",
    "missing", "high",
    {"old": "\\end{tikzcd}\n\\qquad\n\\begin{tikzcd}", "new": "\\end{tikzcd}\n\\qquad\\text{et}\\qquad\n\\begin{tikzcd}"},
    "The TeX leaves out the 'et' that joins the two triangles.")

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

# ---------------------------------------------------------------- checks
bad = 0
for d in F:
    if d["fix"] is None:
        continue
    t = (B / f"page_{d['page']:03d}.tex").read_text(encoding="utf-8")
    n = t.count(d["fix"]["old"])
    if n != 1:
        bad += 1
        print("NOT UNIQUE", d["page"], n, repr(d["fix"]["old"]))
    if "%%%%%%%%%%" in d["fix"]["old"]:
        bad += 1
        print("MARKER IN OLD", d["page"])
counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0])
    c[1 if d["kind"] == "misprint_in_print" else 0] += 1
print("findings", len(F), "bad", bad, counts)
json.loads(OUT.read_text(encoding="utf-8"))
print("json ok")
