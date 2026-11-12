import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

BASE = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I"
OUT = BASE + r"\findings_071_075.json"

F = []


def add(**kw):
    F.append(kw)


MIS = "The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring."

# ---------------- page 71 ----------------
add(page=71,
    where="Definition of a C-valued sheaf, 'such that, for any surjective arrow B' \u2192 B in C_{A|R} ,' just before the display 0 \u2192 F(B) \u2192 F(B') \u21c9 F(B' \u00d7_B B') and 'is exact'",
    scan="C_{A|R} , : a comma with a tail after C_{A|R} (checked in a crop); the sentence runs on through the display to 'is exact'",
    tex="$B' \\to B$  in  $\\underline{C}_{A|R}$ .",
    kind="punctuation", confidence="high",
    fix={"old": "$B' \\to B$  in  $\\underline{C}_{A|R}$ .",
         "new": "$B' \\to B$  in  $\\underline{C}_{A|R}$ ,"},
    note="The TeX's full stop cuts the sentence 'such that, for any surjective arrow B' \u2192 B in C_{A|R}, [display] is exact.' in two.")

# ---------------- page 72 ----------------
RING = ("On pp. 73-75 the typescript types the degree 0 as a tall 0 (\u0048\u030c^0_{A|R}, H^0({B' \u2192 B},F), H^0({P \u2192 B},F)) "
        "and the total degree as this small ring or an inked dot (p. 73 'denoted by \u0048\u030c\u00b0_{A|R}', p. 74 H\u00b0({P \u2192 B},G)); "
        "on p. 72 all eight superscripts are the small ring.")

add(page=72,
    where="3.1(b), 'For any B' \u2192 B in Cov(B) , let us define the functor H\u00b0((B' \u2192 B),-) : C^\u2228_{A|R} \u2192 (A-mod)'",
    scan="H\u00b0 with the small typed ring \u00b0 (checked in a crop), the glyph the page also uses for the total degree",
    tex="define the functor  $H^{\\circ}((B' \\to B),-)",
    kind="misprint_in_print", confidence="medium",
    fix=None,
    corrected="define the functor  $H^{0}((B' \\to B),-)",
    note="The functor defined here, by H\u00b0((B'\u2192B),F) = Ker(F(B') \u21c9 F(B' \u00d7_B B')), is the degree-0 functor; its right derived functors are named in the next sentence. " + RING + " " + MIS + " Depends on the rule for the ring/dot superscript (convention entry on p. 74).")

add(page=72,
    where="3.1(b), same sentence, 'by H\u00b0((B'\u2192 B),F) = Ker(F(B') \u21c9 F(B'\u00d7_B B'))'",
    scan="H\u00b0 with the small typed ring \u00b0 (checked in a crop)",
    tex="$H^{\\circ}((B'\\to B),F) = Ker",
    kind="misprint_in_print", confidence="medium",
    fix=None,
    corrected="$H^{0}((B'\\to B),F) = Ker",
    note="A kernel of the two restriction maps: degree 0, as in the definition just before. " + MIS)

add(page=72,
    where="3.1(b), 'The right derived functors of H\u00b0((B' \u2192 B),-) will be denoted by H\u00b0((B'\u2192 B),-)'",
    scan="both H\u00b0 typed with the same small ring \u00b0 (checked in a crop)",
    tex="The right derived functors of  $H^{\\circ}((B' \\to B),-)",
    kind="misprint_in_print", confidence="medium",
    fix=None,
    corrected="The right derived functors of  $H^{0}((B' \\to B),-)",
    note="The functor being derived is the degree-0 functor just defined; the second H\u00b0 (the derived functors, total degree) is right as printed. " + MIS)

# ---------------- page 73 ----------------
add(page=73,
    where="'The right derived functor of \u0048\u030c^0_{A|R} : C_{A|R} \u2192 C_{A|R} will be denoted by \u0048\u030c\u00b0_{A|R}'",
    scan="C_{A|R} \u2192 C_{A|R}: two plain underlined C, no \u2228 over either (checked in a crop)",
    tex="\\check{\\underline{H}}^{0}_{A|R} : \\underline{C}_{A|R} \\to \\underline{C}_{A|R}",
    kind="misprint_in_print", confidence="medium",
    fix=None,
    corrected="\\check{\\underline{H}}^{0}_{A|R} : \\overset{\\vee}{\\underline{C}}_{A|R} \\to \\overset{\\vee}{\\underline{C}}_{A|R}",
    note="\u0048\u030c^0_{A|R} takes a presheaf F to the presheaf B \u21a6 lim H^0({B'\u2192B},F) (display below) and is derived on presheaves ('For each presheaf F on C_{A|R}, we set \u0048\u030c\u2022(A|R,F) = ...'); C_{A|R} is the site and C^\u2228_{A|R} the category of presheaves (3.1(a)). The hand-drawn \u2228 were not added. " + MIS)

add(page=73,
    where="'In particular', first line of the brace, 'H^1(A|R,F) = H^1(A|R,F)'",
    scan="no \u2228 over either H^1 (contrast crop); the second line has its \u2228 over H^2, H^1 and H^3",
    tex="H^{1}(A|R,F) \\;=\\; H^{1}(A|R,F)",
    kind="misprint_in_print", confidence="high",
    fix=None,
    corrected="\\check{H}^{1}(A|R,F) \\;=\\; H^{1}(A|R,F)",
    note="As printed the identity is empty. The spectral sequence \u0048\u030c^p(A|R,H^q(F)) \u21d2 H^{p+q}(A|R,F) with \u0048\u030c^0(A|R,H^q(F)) = 0 for q > 0 gives \u0048\u030c^1 = H^1 and the exact sequence of the second line; the \u010cech group stands on the left there. " + MIS)

add(page=73,
    where="'In particular', second line, '\u2192 \u0048\u030c^1(A|R,H^1_{A R}(F)) \u2192 \u0048\u030c^3(A|R,F)'",
    scan="H^1_{A R}: a blank between A and R, no vertical bar (contrast crop)",
    tex="\\underline{H}^{1}_{A\\ R}(F)",
    kind="misprint_in_print", confidence="high",
    fix=None,
    corrected="\\underline{H}^{1}_{A|R}(F)",
    note="The bar of A|R, present everywhere else, was not put in; the TeX keeps the printed blank. 'corrected' replaces the 'tex' substring.")

add(page=73,
    where="3.1(c), 'If B is an object in C_{A|R} , the commutative diagram (*) in 2.1(a)'",
    scan="in 2.1(a) (checked in a crop)",
    tex="diagram (*) in 2.1(a)",
    kind="misprint_in_print", confidence="high",
    fix=None,
    corrected="diagram (*) in 3.1(a)",
    note="The diagram (*) of j~ and j^\u2228 for an object B is in 3.1(a) (p. 72); 2.1 is Definition 2.1 (smooth functors), whose diagram (*) is a different one, and it has no (**). Goes with '(**) in 2.1(a)' below: correct both or neither. " + MIS)

add(page=73,
    where="3.1(c), 'together with the fact that j~ as well as j^\u2228 are exact functors yields the canonical isomorphism'",
    scan="j^\u2228: the \u2228 at the upper right of the j, as a superscript (checked in a crop), as in '(as well as j^\u2228 )' and the diagram (*) on p. 72",
    tex="$\\check{j}$",
    kind="symbol", confidence="medium",
    fix={"old": "$\\check{j}$", "new": "$j^{\\vee}$"},
    note="\\check{j} sets the \u2228 as an accent over the j; the file writes the same printed j^\u2228 as j^{\\vee} on p. 72, and keeps \\check for the \u2228 that does stand over a letter (\u0048\u030c, \u03b2\u030c).")

add(page=73,
    where="3.1(c), 'a ring homomorphism S \u2192 R induces the commutative diagram (**) in 2.1(a). Now \u03b2~ is not necessarily an exact functor'",
    scan="in 2.1(a).",
    tex="in 2.1(a). Now",
    kind="misprint_in_print", confidence="high",
    fix=None,
    corrected="in 3.1(a). Now",
    note="The diagram (**) for a ring homomorphism S \u2192 R is in 3.1(a) (p. 72). Goes with the '(*) in 2.1(a)' correction above. " + MIS)

# ---------------- page 74 ----------------
add(page=74,
    where="Proof of Lemma 3.2, 'It suffice to see that the natural map'",
    scan="It suffice to see",
    tex="It suffice to see",
    kind="misprint_in_print", confidence="high",
    fix=None,
    corrected="It suffices to see",
    note="Verb agreement slip (the same page has 'it suffices to show'). " + MIS)

add(page=74,
    where="Corollary 3.3 (a), 'Assume that A is noetherian. If F \u2208 ob(C~_{A|R}) is of finite type,'",
    scan="the underline of 'is noetherian' stops before the full stop; 'If' has its own underline (checked in a crop)",
    tex="\\underline{is noetherian. If}",
    kind="underline", confidence="low",
    fix={"old": "\\underline{is noetherian. If}", "new": "\\underline{is noetherian}. \\underline{If}"},
    note="Underline extent only. The full stop sits inside the \\underline, not at its end, so the global pass on final punctuation does not reach it (as p. 66 'smooth functor. If').")

CT = ("The print's C~ (tilde over the upper right of the C, checked in a crop) is the same glyph as on pp. 71-72 and 75, which the file writes "
      "\\widetilde{\\underline{C}} (also pp. 76-83); this page writes \\underline{C}^{\\sim}, a superscript \u223c beside the C, three times "
      "(p. 88 twice more). Apply the three p. 74 fixes together.")

add(page=74,
    where="Corollary 3.3 (a), 'If F \u2208 ob(C~_{A|R}) is of finite type'",
    scan="C~_{A|R}, tilde over the upper right of the underlined C",
    tex="ob(\\underline{C}^{\\sim}_{A|R})",
    kind="symbol", confidence="low",
    fix={"old": "ob(\\underline{C}^{\\sim}_{A|R})", "new": "ob(\\widetilde{\\underline{C}}_{A|R})"},
    note=CT)

add(page=74,
    where="Corollary 3.3 (b), 'and for all F \u2208 ob(C~_{P|R})'",
    scan="C~_{P|R}, same glyph",
    tex="ob(\\underline{C}^{\\sim}_{P|R})",
    kind="symbol", confidence="low",
    fix={"old": "ob(\\underline{C}^{\\sim}_{P|R})", "new": "ob(\\widetilde{\\underline{C}}_{P|R})"},
    note="Same as the entry for 3.3 (a).")

add(page=74,
    where="Corollary 3.3 (c), 'A diagram 0 \u2192 F' \u2192 F \u2192 F'' \u2192 0 in C~_{A|R} is exact if and only if'",
    scan="C~_{A|R}, same glyph",
    tex="\\underline{in}  $\\underline{C}^{\\sim}_{A|R}$",
    kind="symbol", confidence="low",
    fix={"old": "\\underline{in}  $\\underline{C}^{\\sim}_{A|R}$", "new": "\\underline{in}  $\\widetilde{\\underline{C}}_{A|R}$"},
    note="Same as the entry for 3.3 (a).")

add(page=74,
    where="Proof of 3.3 (a), 'it suffices to show that H^n(G) is of finite type for all n and for all presheaf G of finite type'",
    scan="for all presheaf G",
    tex="for all presheaf  $G$",
    kind="misprint_in_print", confidence="low",
    fix=None,
    corrected="for all presheaves  $G$",
    note="Number agreement slip (p. 75 has 'for all presheaves G on C_{P|R}'). Low: possibly the author's own wording. " + MIS)

add(page=74,
    where="Total-degree superscript of H, \u0048\u030c, R, pp. 72-75 (convention, reported once)",
    scan=("The typescript types the degree 0 as a tall 0 (p. 73 \u0048\u030c^0_{A|R}, H^0({B' \u2192 B},F); p. 74 H^0({P \u2192 B},F), \u0048\u030c^0(F)(B)) "
          "and the total degree either as a small typed ring \u00b0 (all eight superscripts of p. 72; p. 73 'denoted by \u0048\u030c\u00b0_{A|R}'; "
          "p. 74 \u03b2^#H\u00b0_{A|S}(F) and H\u00b0({P \u2192 B},G) twice) or as an inked dot (p. 73 \u0048\u030c\u2022(A|R,F), [H\u2022_{A|R}(F)](B); "
          "p. 74 R\u2022\u03b2~F, H\u2022({P \u2192 B},F), \u0048\u030c\u2022(F)(B), \u0048\u030c\u2022(B|R,G); p. 75 H\u2022({P \u2192 B},G))"),
    tex=("\\circ on p. 72 (H^{\\circ}, eight times); \\bullet on pp. 73-75 for ring and dot alike (p. 73 \\check{\\underline{H}}^{\\bullet}_{A|R}; "
         "p. 74 \\beta^{\\#}\\underline{H}^{\\bullet}_{A|S}(F), H^{\\bullet}(\\{P \\to B\\},G)); the file has \\cdot on pp. 77-79 (not checked here)"),
    kind="symbol", confidence="low",
    fix=None,
    note=("One rule is needed for the exposé: either \\circ for each typed ring and \\bullet for each inked dot (strictly diplomatic), or one "
          "symbol for both. The three p. 72 rings that stand for the degree 0 are reported separately as misprints (corrected H^{0}); their "
          "'tex' substrings use the present \\circ."))

# ---------------- page 75 ----------------
add(page=75,
    where="Proof of 3.3 (b), 'If B \u2192 P is any surjective R-algebra map, then it amits a section'",
    scan="it amits a section",
    tex="it amits a section",
    kind="misprint_in_print", confidence="high",
    fix=None,
    corrected="it admits a section",
    note="Typing error for 'admits'. " + MIS)

add(page=75,
    where="Proof of 3.3 (c), display '0 \u2192 F'(B) \u2192 F(B) \u2192 F''(B) \u2192 H'(B|R, F') \u2192 H'(B|R, F) \u2192 ....'",
    scan="H' twice, with a typed apostrophe identical to the prime of F' (checked in a crop); the next line has H^1(P|R, F') with a typed 1",
    tex="H'(B|R,\\ F') \\to H'(B|R,\\ F)",
    kind="misprint_in_print", confidence="medium",
    fix=None,
    corrected="H^{1}(B|R,\\ F') \\to H^{1}(B|R,\\ F)",
    note="The long exact sequence continues F''(B) \u2192 H^1(B|R,F') \u2192 H^1(B|R,F), and the next sentence concludes from H^1(P|R,F') = 0. " + MIS)

add(page=75,
    where="Proof of 3.3 (c), display after 'then H^1(P|R, F') = 0 by 3.3(b) and hence'",
    scan="0 \u2192 F' \u2192 F \u2192 F'' \u2192 0, without (P)",
    tex="0 \\to F' \\to F \\to F'' \\to 0\n\\end{equation*}",
    kind="misprint_in_print", confidence="medium",
    fix=None,
    corrected="0 \\to F'(P) \\to F(P) \\to F''(P) \\to 0\n\\end{equation*}",
    note="This direction proves that the values at a polynomial algebra P form an exact sequence (statement of 3.3(c)); as printed the display repeats the hypothesis. " + MIS)

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
print(len(F), "findings written")
