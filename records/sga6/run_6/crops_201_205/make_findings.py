r"""Write findings_201_205.json (SGA 6, pp. 201-205) and check that every fix's old occurs exactly once in its
page_NNN.tex (LF) and in the same page of the present diplomatic main.tex."""
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_6"
MAIN = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex"
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
N = "\n"

F = []


def add(**kw):
    F.append(kw)


# ---------------------------------------------------------------- p. 201
add(page=201, where="start of page (folio-201 marker)",
    scan="p. 201 begins with the display 'P^o_{X/S} ≃ O_X ,' / 'P^1_{X/S} ≃ O_X ⊕ Ω^1_{X/S} ,'; p. 200 ends "
         "'... On a des isomorphis-mes canoniques' (both scans; witness pp. 200-201)",
    tex="'\\[', '\\begin{aligned}' and both rows of the display are the last lines of page_200.tex (under the "
        "folio-200 marker); the folio-201 marker stands inside the display, page_201.tex begins '\\end{aligned}'",
    kind="marker", confidence="high", fix=None,
    note="Page 201 really begins with the '\\[' that opens the aligned display, right after 'On a des isomorphismes "
         "canoniques'. python -I move_marker.py 6 201 '\\[' --before (single quotes; simulated in memory on both "
         "layers with crops_201_205/sim_markers.py: '... On a des isomorphismes canoniques' / the marker / '\\[' / "
         "'\\begin{aligned}' / 'P^0_{X/S}&\\simeq\\cO_X,\\\\' ... / '\\]' / 'où $\\Omega^1_{X/S}$ ...'). Apply once: "
         "the checker of p. 200 may report the same boundary, and a second run would take the '\\[' of p. 200.")

add(page=201, where="1.2.1, after the display: 'par rapport à S où faisceau cotangent relatif'",
    scan="'à S où faisceau cotangent relatif': où with a grave accent (both scans; crops_201_205/c201_ou.png)",
    tex="par rapport à $S$ où \\emph{faisceau cotangent relatif} (printed reading kept)",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"par rapport à $S$ ou \emph{faisceau cotangent relatif}",
    note="'ou' (or) introduces the second name of Ω^1_{X/S}. The TeX keeps the printed reading; the corrected layer "
         "already reads 'ou' (Codex SGA-SRC-001561).")

add(page=201, where="1.2.2, 'Par définition, un opérateur différentiel ... est un homomorphisme f^{-1}(O_X)-linéaire'",
    scan="f^{-1}(O_X)-linéaire: index X (both scans; crops_201_205/c201_fOX.png)",
    tex="$f^{-1}(\\cO_X)$-linéaire (printed reading kept)",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"$f^{-1}(\cO_S)$-linéaire",
    note="For f : X -> S the operators are f^{-1}(O_S)-linear, as d^n_{X/S} in 1.2.1 and f^{-1}(O_S ⊗ C) in 1.2.3. "
         "The TeX keeps the printed reading; the corrected layer already reads \\cO_S (SGA-SRC-001562).")

add(page=201, where="1.2.2, 'le faisceau P^n_{X/S}(E) = P^n_{X/S} ⊗_{O_X} E des parties principales'",
    scan="P^n_{X/S} ⊕ _{O_X} E: the sign is the typed ⊕ (circle with a vertical and a horizontal bar), the same glyph "
         "as the direct sum in 'O_X ⊕ Ω^1_{X/S}' at the top of the page (both scans; crops_201_205/c201_tens.png, "
         "w201_sym_zoom.png). This typeface writes ⊗ as a slashed circle ('O_X ⊗ C', witness p. 209, "
         "crops_201_205/w209_tens.png)",
    tex="P^n_{X/S}\\otimes_{\\cO_X}E (silently corrected)",
    kind="misprint_in_print", confidence="high",
    fix={"old": r"P^n_{X/S}\otimes_{\cO_X}E", "new": r"P^n_{X/S}\oplus_{\cO_X}E"},
    corrected=r"P^n_{X/S}\otimes_{\cO_X}E",
    note="The sentence goes on '(le produit tensoriel étant défini ...)', so ⊗ is meant. The TeX silently corrects; "
         "the fix restores the printed sign in the diplomatic layer.")

# ---------------------------------------------------------------- p. 202
OLD_FN = (r"canonique\footnote{$S^n(\ )$ désigne la puissance symétrique $n$-ième.}" + N + r"\[" + N
          + r"  0\longrightarrow S^n(\Omega^1_{X/S})" + N + r"  \longrightarrow P^n_{X/S}" + N
          + r"  \longrightarrow P^{n-1}_{X/S}" + N + r"  \longrightarrow 0." + N + r"\]" + N)
NEW_FN = (r"canonique" + N + r"\[" + N
          + r"  0\longrightarrow S^n(\Omega^1_{X/S})" + N + r"  \longrightarrow P^n_{X/S}" + N
          + r"  \longrightarrow P^{n-1}_{X/S}" + N + r"  \longrightarrow 0.\text{\footnotemark}" + N + r"\]" + N
          + r"\footnotetext{$S^n(\ )$ désigne la puissance symétrique $n$-ième.}%" + N)
add(page=202, where="1.2.4, call of footnote (1) 'S^n( ) désigne la puissance symétrique n-ième.'",
    scan="the call (1) stands after the display and its full stop: '... -> P^{n-1}_{X/S} -> 0  . (1)'; nothing "
         "after 'on a une suite exacte canonique' (both scans)",
    tex="canonique\\footnote{$S^n(\\ )$ désigne ...} before the display",
    kind="other", confidence="medium", fix={"old": OLD_FN, "new": NEW_FN},
    note="Moves the call to the place of the printed (1), with the \\text{\\footnotemark} / \\footnotetext pair "
         "main.tex already uses for calls in displays (p. 61). The % after \\footnotetext keeps 'D'où' from "
         "starting with a space.")

add(page=202, where="'Appliquant à (1.2.4.1) le foncteur Hom_{O_X}(.,F)'",
    scan="Hom_{O_X}(.,F): the empty argument is a typed full stop on the line (both scans; "
         "crops_201_205/c202_dot1.png, w202_dots.png)",
    tex="\\Homop_{\\cO_X}(\\cdot,F)",
    kind="symbol", confidence="medium",
    fix={"old": r"\Homop_{\cO_X}(\cdot,F)", "new": r"\Homop_{\cO_X}(.,F)"},
    note="\\cdot raises the typed stop to mid-height; as the typed place-holders applied on pp. 89, 136, 141, 154, "
         "165. Same decision as the next entry: both or neither.")

add(page=202, where="same sentence, '(resp. Hom_{O_X⊗C}(.,F))'",
    scan="Hom_{O_X⊗C}(.,F): typed full stop as place-holder (both scans; crops_201_205/c202_dot2.png)",
    tex="\\Homop_{\\cO_X\\otimes\\mathbb C}(\\cdot,F)",
    kind="symbol", confidence="medium",
    fix={"old": r"\Homop_{\cO_X\otimes\mathbb C}(\cdot,F)", "new": r"\Homop_{\cO_X\otimes\mathbb C}(.,F)"},
    note="As the previous entry: both or neither.")

add(page=202, where="'compte tenu des identifications (1.2.2.1) et (1.2.4.1), une suite exacte'",
    scan="(1.2.2.1) et (1.2.4.1) (both scans; crops_201_205/c202_ident.png)",
    tex="identifications (1.2.2.1) et (1.2.4.1) (printed reading kept)",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected="identifications (1.2.2.1) et (1.2.3.1)",
    note="The identifications are the bijections (1.2.2.1) and (1.2.3.1); (1.2.4.1) is the sequence the functor is "
         "applied to. The TeX keeps the printed reading; the corrected layer already reads (1.2.3.1) "
         "(SGA-SRC-001563).")

# ---------------------------------------------------------------- p. 203
add(page=203, where="'... homogène de degré n de Ω^1_{X/S} dans Hom_{O_X}(E,F)'",
    scan="Hom underlined (the sheaf Hom), apart from the underline of the index O_X (both scans; "
         "crops_201_205/c203_hom.png)",
    tex="$\\Homop_{\\cO_X}(E,F)$ (\\Homop = \\operatorname{Hom}, plain)",
    kind="underline", confidence="high",
    fix={"old": r"dans $\Homop_{\cO_X}(E,F)$", "new": r"dans $\underline{\Homop}_{\cO_X}(E,F)$"},
    note="The file writes \\underline{\\Homop} for the underlined Hom on pp. 204-205.")

add(page=203, where="same sentence, '(resp. Hom_{O_X⊗C}(E,F))'",
    scan="Hom underlined (both scans; crops_201_205/c203_hom.png)",
    tex="$\\Homop_{\\cO_X\\otimes\\mathbb C}(E,F)$",
    kind="underline", confidence="high",
    fix={"old": r"$\Homop_{\cO_X\otimes\mathbb C}(E,F)$",
         "new": r"$\underline{\Homop}_{\cO_X\otimes\mathbb C}(E,F)$"},
    note="As the previous entry.")

add(page=203, where="1.2.5, 'On dit que E est un complexe elliptique d'ordre n = (n_i)'",
    scan="underlined: 'complexe elliptique' and, separately, the n of 'n = (n_i)' (the sequence n̲); 'd'ordre' is "
         "not underlined (both scans; crops_201_205/c203_ell.png)",
    tex="\\emph{complexe elliptique d'ordre $n$} $=(n_i)$",
    kind="underline", confidence="high",
    fix={"old": r"\emph{complexe elliptique d'ordre $n$} $=(n_i)$",
         "new": r"\emph{complexe elliptique} d'ordre $\underline{n}=(n_i)$"},
    note="The emphasis ends after 'elliptique'; the underlined n is the notation for the sequence (n_i).")

add(page=203, where="1.2.6, '(considérée comme monomorphisme d'espaces annelés) cf.(1.1)).'",
    scan="one closing parenthesis too many: the one after 'annelés' already closes '(considérée', then "
         "'cf.(1.1))' (both scans; crops_201_205/c203_cf.png)",
    tex="d'espaces annelés) cf.~(1.1)). (printed reading kept)",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"(considérée comme monomorphisme d'espaces annelés, cf.~(1.1))",
    note="Unbalanced parentheses; the likely reading puts the reference inside the parenthesis. The TeX keeps the "
         "printed reading, as does the corrected layer.")

# ---------------------------------------------------------------- p. 204
add(page=204, where="2.0, second paragraph, 'Les variétés mixtes dont il sera question'",
    scan="variétes: the last e has no accent (both scans; crops_201_205/c204_varietes.png, w204_varietes.png)",
    tex="Les variétés mixtes (silently corrected)",
    kind="misprint_in_print", confidence="high",
    fix={"old": "Les variétés mixtes", "new": "Les variétes mixtes"},
    corrected="Les variétés mixtes",
    note="A typing slip on a small letter (the rule for unaccented typed capitals does not cover it). The TeX "
         "silently corrects; the fix restores the printed reading in the diplomatic layer.")

# ---------------------------------------------------------------- p. 205
add(page=205, where="Proposition 2.2, 'Soient A un fermé de X_s, et f ∈ H^0(A,Hom(X_s,Y_s)).'",
    scan="the formula stands in the running text at the end of the line 'voisinages paracompacts. Soient A un fermé "
         "de X_s, et f ∈ H^o(A,Hom(X_s,Y_s)).'; 'Le sous-faisceau ...' follows on the next line (both scans)",
    tex="a display \\[ f\\in H^0(A,\\underline{\\Homop}(X_s,Y_s)). \\]",
    kind="other", confidence="medium",
    fix={"old": "et" + N + r"\[" + N + r"  f\in H^0(A,\underline{\Homop}(X_s,Y_s))." + N + r"\]" + N
                + "Le sous-faisceau",
         "new": r"et $f\in H^0(A,\underline{\Homop}(X_s,Y_s))$." + N + "Le sous-faisceau"},
    note="The print sets the formula inline; the TeX makes it a display (same kind of fix as pp. 21, 34, 42, 80, "
         "105, 122-133).")

add(page=205, where="Preuve, second display 'H^0(A_o,i_s^{-1}Hom(X,Y)) = Lim_{U_o ⊃ A_o} Hom(U_o,Y')'",
    scan="Lim with a capital L above the arrow (both scans; crops_201_205/c205_lim2.png); the first display of the "
         "proof has a small 'lim' (c205_lim1.png)",
    tex="\\varinjlim_{U_0\\supset A_0} (prints lim)",
    kind="word", confidence="medium",
    fix={"old": r"=\varinjlim_{U_0\supset A_0}", "new": r"=\mathop{\underrightarrow{\mathrm{Lim}}}\limits_{U_0\supset A_0}"},
    note="The first display (lim, \\varinjlim) is right. \\underrightarrow is amsmath.")

add(page=205, where="Preuve, 'isomorphe à S' x V, ou V est un ouvert convexe de R^n'",
    scan="ou without accent (both scans; crops_201_205/c205_ou.png), two lines below the accented 'où S' est' "
         "(c205_ou2.png)",
    tex="$S'\\times V$, ou $V$ est (printed reading kept)",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"$S'\times V$, où $V$ est",
    note="Relative 'où'. The TeX keeps the printed reading; the corrected layer also still reads 'ou'.")

add(page=205, where="footnotes: the second call, 'on a ([T.F.] II 3.3.1) (1)', and its note",
    scan="both notes of the page are marked (1): 'Proposition (1) 2.2' / '(1) Communiquée au rédacteur par A. "
         "Douady.' and '([T.F.] II 3.3.1) (1)' / '(1) Un fermé d'un espace paracompact ...' (both scans)",
    tex="two \\footnote{...} (automatic numbers)",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"(\textsuperscript{2})",
    note="The typescript numbers its notes per page ((1), (2) on p. 202); the second note of p. 205 should be (2). "
         "No edit: \\footnote numbers automatically (volume convention, findings_016_020 p. 20), so the TeX neither "
         "keeps nor corrects the printed mark.")

add(page=205, where="end of page (folio-206 marker)",
    scan="p. 205 ends '... La proposition sera donc consé-'; p. 206 begins 'quence du lemme suivant :' (both scans)",
    tex="page_205.tex (extracted 20:15) ends 'La proposition sera donc'; 'conséquence' began page_206.tex",
    kind="marker", confidence="high", fix=None,
    note="Already reported by batch 206-210 (findings_206_210, p. 206 'start of page') and already applied: in the "
         "present main.tex (both layers, 20:28) 'consé%' stands before the folio-206 marker and 'quence du lemme "
         "suivant~:' after it. No action; do not run marker_split_word.py again.")

# ---------------------------------------------------------------- checks and output
pages = {}
for n in range(201, 206):
    with open(RUN + r"\b201_205\page_%03d.tex" % n, encoding="utf-8", newline="") as fh:
        pages[n] = fh.read()
with open(MAIN, encoding="utf-8", newline="") as fh:
    main = fh.read()
ms = list(MARK.finditer(main))
segs = {}
for i, m in enumerate(ms):
    f = int(m.group(2))
    if 201 <= f <= 205:
        segs[f] = main[m.start():ms[i + 1].start()]
ok = True
for e in F:
    assert set(e) >= {"page", "where", "scan", "tex", "kind", "confidence", "fix", "note"}, e
    assert (e["kind"] == "misprint_in_print") == ("corrected" in e), e["where"]
    if e["fix"]:
        old = e["fix"]["old"]
        c1 = pages[e["page"]].count(old)
        c2 = segs[e["page"]].count(old)
        bad = "%%%%%%%%%%" in old or "%%%%%%%%%%" in e["fix"]["new"]
        print(e["page"], c1, c2, "MARKER!" if bad else "", repr(old[:60]))
        ok = ok and c1 == 1 and c2 == 1 and not bad
print("all olds unique:", ok)
order = ["page", "where", "scan", "tex", "kind", "confidence", "fix", "corrected", "note"]
out = [{k: e[k] for k in order if k in e} for e in F]
with open(RUN + r"\findings_201_205.json", "w", encoding="utf-8", newline="\n") as fh:
    json.dump(out, fh, ensure_ascii=False, indent=1)
    fh.write("\n")
from collections import Counter
c = Counter((e["page"], e["kind"] == "misprint_in_print") for e in F)
for n in range(201, 206):
    print(n, "normal", c[(n, False)], "misprint", c[(n, True)])
