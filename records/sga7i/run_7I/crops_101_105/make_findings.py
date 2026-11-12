import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
base = "C:/Users/user/Documents/sga_scan_check_20261105/run_7I/b101_105"
out = "C:/Users/user/Documents/sga_scan_check_20261105/run_7I/findings_101_105.json"

F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "confidence": confidence, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 101 ----------------
add(101,
    "Proof of (a), first sentence: 'it suffices to see that [M(k[\u03b5])] is a finite-dimensional vector space over k'",
    "[M(k[\u03b5])]: M underlined, with no subscript (checked in a crop)",
    "$[\\underline{M}(k[\\epsilon])]$",
    "misprint_in_print", "low", None,
    "The category of the statement is M_{X_0}; the same vector space is written [M_{X_0}(k[\u03b5])] in (*) and at the end of the proof. The TeX keeps the printed reading. Low: the bare M may be meant loosely, for the general homogeneous category of 1.11 and 2.9(b).",
    corrected="$[\\underline{M}_{X_{0}}(k[\\epsilon])]$")

add(101,
    "Remark 4.6(a), last sentence: 'There are affine schemes X_0 over k having a non-isolated non-smooth point'",
    "over k: only a faint speck before k, no typed character (checked in a crop)",
    "over \u02d9$k$",
    "extra", "high",
    {"old": "over \u02d9$k$", "new": "over $k$"},
    "The TeX carries a stray U+02D9 (dot above) before $k$, which would print as a mark; it renders a speck of the scan.")

# ---------------- page 102 ----------------
add(102,
    "Diagram of a deformation of (X_0, Y_0) to R: label 'flat' of the vertical X \u2192 Spec(R)",
    "'flat' typed to the RIGHT of the vertical stroke, between it and the Y \u2192 Spec(R) diagonal (which crosses its 'l')",
    "X \\arrow[d, \"\\text{flat}\"']",
    "other", "low",
    {"old": "\"\\text{flat}\"']", "new": "\"\\text{flat}\"]"},
    "The swap mark ' sets the label to the left of a downward arrow (inside the square); without it tikz-cd sets it to the right, as printed (the file's comment block also records it to the right). Does not overlap the arrowhead edit below.")

add(102,
    "Same diagram, vertical X \u2192 Spec(R)",
    "a plain stroke with no arrowhead, ending cleanly just above Spec(R) (checked in a crop); the other eight arrows have heads",
    "X \\arrow[d, \"\\text{flat}\"']",
    "misprint_in_print", "medium",
    {"old": "X \\arrow[d,", "new": "X \\arrow[d, no head,"},
    "X \u2192 Spec(R) is the flat structure morphism of the deformation; its head was not drawn. The TeX silently supplies it (its comment block records the missing head). The fix restores the printed headless stroke with the tikz-cd key 'no head'; 'corrected' is the current TeX.",
    corrected="X \\arrow[d,")

# ---------------- page 103 ----------------
add(103,
    "Proof of Lemma 4.7, first sentence: 'whose objects are of the form (k[\u03b5]; X \u00d7_{Spec(k)} Spec(k[\u03b5]), Y)'",
    "(k[\u03b5]; X \u00d7_{Spec(k)} Spec(k[\u03b5]), Y): plain X, no subscript 0 (checked in a crop)",
    "(k[\\epsilon]; X \\times_{\\mathrm{Spec}(k)}",
    "misprint_in_print", "medium", None,
    "The objects of B are the deformations whose underlying scheme is the trivial deformation X_0 \u00d7_{Spec(k)} Spec(k[\u03b5]), as the next sentence says ('inside X_0 \u00d7_{Spec(k)} Spec(k[\u03b5])'). The TeX keeps the printed reading.",
    corrected="(k[\\epsilon]; X_0 \\times_{\\mathrm{Spec}(k)}")

add(103,
    "Diagram of the association (Y, j_Y) \u21a6 ..., label of the middle vertical arrow O_{X_0} \u2192 O_Y",
    "\U0001d50d_Y: a Fraktur capital J with subscript Y (checked in a crop)",
    "\\arrow[d, \"j_Y\"]",
    "misprint_in_print", "medium",
    {"old": "\\arrow[d, \"j_Y\"]", "new": "\\arrow[d, \"\\mathfrak{J}_Y\"]"},
    "The map is the one induced by j_Y : Y \u2192 X_0; the display below calls it j (label j|I, a typewriter j). The Fraktur letter is a wrong glyph. The TeX silently writes j_Y (its comment block records the Fraktur J). The fix restores the printed letter (\\mathfrak is used in the file, e.g. \\mathfrak{X} on p. 102); 'corrected' is the current TeX.",
    corrected="\\arrow[d, \"j_Y\"]")

# ---------------- page 104 ----------------
add(104,
    "Remark 4.8, display: 'H^0(Y_0, Hom_{Y_0}(I/I^2, O_{Y_0})) = H^0(Y_0, D^1_{Y_0|X})'",
    "D^1_{Y_0|X}: X without subscript 0 (checked in a crop)",
    "\\underline{D}^1_{Y_0|X})",
    "misprint_in_print", "low", None,
    "Y_0 is the closed subscheme of X_0 defined by I (the 'where' clause 0 \u2192 I \u2192 O_{X_0} \u2192 O_{Y_0} \u2192 0), and Hom(I/I^2, O_{Y_0}) is D^1 of Y_0 over X_0. The TeX keeps the printed reading. Low: the bare X could be read as the general S-scheme of the preceding sentences.",
    corrected="\\underline{D}^1_{Y_0|X_0})")

add(104,
    "Theorem 4.9, first line: 'Let X_0 be k-scheme of finite type and'",
    "'be' underlined; 'k-' not underlined; 'scheme of finite type and' underlined (checked in a crop)",
    "\\underline{be $k$-scheme of finite type and}",
    "underline", "high",
    {"old": "\\underline{be $k$-scheme of finite type and}",
     "new": "\\underline{be} $k$-\\underline{scheme of finite type and}"},
    "The TeX underlines the letter k and its hyphen; the print leaves them plain, as it does the other math letters of the statement.")

add(104,
    "Theorem 4.9(a), display: 'Aut_{R'}((X', Y')|X_0) \u2192 Aut_R(X' \u2297_{R'} R, Y', \u2297_{R'} R)|X_0)'",
    "right-hand side: Aut_R( with a single opening parenthesis, and a comma after Y' before \u2297_{R'} R (checked in a crop)",
    "\\mathrm{Aut}_R(X' \\otimes_{R'} R,\\, Y',\\, \\otimes_{R'} R)|X_0)",
    "misprint_in_print", "high", None,
    "The target is the automorphism group of the restricted pair (X' \u2297_{R'} R, Y' \u2297_{R'} R) over X_0, written like the source ((X', Y')|X_0): the opening parenthesis of the pair is missing and the comma after Y' is stray. The TeX keeps both printed readings.",
    corrected="\\mathrm{Aut}_R((X' \\otimes_{R'} R,\\, Y' \\otimes_{R'} R)|X_0)")

# ---------------- page 105 ----------------
add(105,
    "'the images of (R, \U0001d51b) under M_{X_0} \u2192 M_{Spec(O_{X_0,x_0})} and M_{X_0} \u2192 M_{Spec(O_{X_0,x_0})}': the second functor",
    "the second functor is printed identical to the first, with a plain O (no hat; checked in a crop)",
    "and  $\\underline{M}_{X_0} \\to \\underline{M}_{\\mathrm{Spec}(\\underline{O}_{X_0,\\ x_0})}$  by",
    "misprint_in_print", "medium", None,
    "'respectively' pairs the localization and the completion functors of the display above with their two images; the second functor goes to M_{Spec(\u00d4_{X_0,x_0})}. The TeX keeps the printed reading.",
    corrected="and  $\\underline{M}_{X_0} \\to \\underline{M}_{\\mathrm{Spec}(\\widehat{\\underline{O}}_{X_0,\\ x_0})}$  by")

add(105,
    "Same sentence: 'by (R, \U0001d51b_{(x_0)}) and (R, \U0001d51b_{(x_0)}) respectively'",
    "(R, \U0001d51b_{(x_0)}) printed twice, with no hat in the second (checked in a crop)",
    "and  $(R,\\ \\mathfrak{X}_{(x_0)})$ respectively",
    "misprint_in_print", "medium", None,
    "The image under the completion functor is \U0001d51b_{(x\u0302_0)}, defined in the second display below; Theorem 4.10(b) likewise pairs (R, \U0001d51b_{(x)}) with (R, \U0001d51b_{(x\u0302)}). The TeX keeps the printed reading.",
    corrected="and  $(R,\\ \\mathfrak{X}_{(\\hat{x}_0)})$ respectively")

add(105,
    "'Therefore if \U0001d51b = lim_v \U0001d51b_v where \U0001d51b_v = \U0001d51b \u00d7_{Spf(R)} ...'",
    "index typed as a Latin v (the typewriter v with top serifs, as in 'where'; checked in a crop), three times here",
    "\\varinjlim\\limits_{\\nu} \\mathfrak{X}_{\\nu}$  where  $\\mathfrak{X}_{\\nu} =",
    "symbol", "medium",
    {"old": "\\varinjlim\\limits_{\\nu} \\mathfrak{X}_{\\nu}$  where  $\\mathfrak{X}_{\\nu} =",
     "new": "\\varinjlim\\limits_{v} \\mathfrak{X}_{v}$  where  $\\mathfrak{X}_{v} ="},
    "The TeX reads the typed v as Greek \u03bd everywhere on this page (8 places); the print has the Latin letter. Apply together with the three other v edits of this page (all or none).")

add(105,
    "Same sentence: 'Spec(R/m^{v+1})'",
    "m^{v+1} with the typed Latin v",
    "\\underline{m}^{\\nu+1}",
    "symbol", "medium",
    {"old": "\\underline{m}^{\\nu+1}", "new": "\\underline{m}^{v+1}"},
    "As the previous entry; apply with it.")

add(105,
    "First display: '\U0001d51b_{(x_0)} = lim_v Spec(O_{\U0001d51b_v, x_0})'",
    "lim index and subscript of \U0001d51b: the typed Latin v",
    "\\limits_{\\nu} \\mathrm{Spec}(\\underline{O}_{\\mathfrak{X}_{\\nu},",
    "symbol", "medium",
    {"old": "\\limits_{\\nu} \\mathrm{Spec}(\\underline{O}_{\\mathfrak{X}_{\\nu},",
     "new": "\\limits_{v} \\mathrm{Spec}(\\underline{O}_{\\mathfrak{X}_{v},"},
    "As the v entries above; apply with them.")

add(105,
    "Second display: '\U0001d51b_{(X\u0302_0)} = lim_v Spec(\u00d4_{\U0001d51b_v, x_0}) .'",
    "subscript (X\u0302_0) with a CAPITAL X under the hat: 29 px high against 20 px for the small x of (x_0) in the first display (checked in a crop)",
    "\\mathfrak{X}_{(\\hat{x}_0)}",
    "misprint_in_print", "medium",
    {"old": "\\mathfrak{X}_{(\\hat{x}_0)}", "new": "\\mathfrak{X}_{(\\hat{X}_0)}"},
    "The point is x_0, as in \u00d4_{\U0001d51b_v, x_0} on the same line. The TeX silently writes the small x. The fix restores the printed capital; 'corrected' is the current TeX. Does not overlap the v edit of this display.",
    corrected="\\mathfrak{X}_{(\\hat{x}_0)}")

add(105,
    "Same display: lim_v and \U0001d51b_v",
    "the typed Latin v, twice",
    "\\limits_{\\nu} \\mathrm{Spec}(\\widehat{\\underline{O}}_{\\mathfrak{X}_{\\nu},",
    "symbol", "medium",
    {"old": "\\limits_{\\nu} \\mathrm{Spec}(\\widehat{\\underline{O}}_{\\mathfrak{X}_{\\nu},",
     "new": "\\limits_{v} \\mathrm{Spec}(\\widehat{\\underline{O}}_{\\mathfrak{X}_{v},"},
    "As the v entries above; apply with them.")

# ---------------- checks ----------------
ok = True
texts = {n: open(f"{base}/page_{n}.tex", encoding="utf-8").read() for n in range(101, 106)}
for d in F:
    s = texts[d["page"]]
    if d["fix"] is not None:
        c = s.count(d["fix"]["old"])
        if c != 1:
            ok = False
            print("OLD COUNT", c, d["page"], repr(d["fix"]["old"]))
        if "%%%%%%%%%%" in d["fix"]["old"]:
            ok = False
            print("MARKER IN OLD", d["page"])
    if s.count(d["tex"]) < 1:
        print("TEX not found (info)", d["page"], repr(d["tex"]))
# simulate applying all non-misprint fixes then misprint fixes, per page, to check overlaps
for n in range(101, 106):
    s = texts[n]
    fx = [d for d in F if d["page"] == n and d["fix"] is not None]
    for d in fx:
        if s.count(d["fix"]["old"]) != 1:
            ok = False
            print("SEQUENTIAL OLD COUNT problem", n, repr(d["fix"]["old"]))
        s = s.replace(d["fix"]["old"], d["fix"]["new"], 1)
print("all checks ok" if ok else "PROBLEMS")
json.dump(F, open(out, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
from collections import Counter
cnt = Counter((d["page"], d["kind"] == "misprint_in_print") for d in F)
for n in range(101, 106):
    print(n, "normal", cnt[(n, False)], "misprint", cnt[(n, True)])
