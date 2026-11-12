import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I"
FOLDER = os.path.join(RUN, "b106_110")
OUT = os.path.join(RUN, "findings_106_110.json")

DOTS_NOTE = ("The typescript has comma, three dots, comma (dot runs measured on the scan; "
             "every comma-delimited ellipsis on pp. 109-110 has three dots). The TeX has four dots. "
             "The '\\times .... \\times' on p. 109 has four printed dots and is right as it stands.")


def dots(page, where, old, new):
    return {
        "page": page,
        "where": where,
        "scan": "',...,' (three dots between the commas)",
        "tex": old,
        "kind": "punctuation",
        "confidence": "high",
        "fix": {"old": old, "new": new},
        "note": DOTS_NOTE,
    }


F = []

# ---------------- page 106 ----------------
F.append({
    "page": 106,
    "where": "proof of (a), 'Since R' -> R is a small extension, D^1(R'|R, k) is 1-dimensional vector space over k'",
    "scan": "D^1(R'|R, k) : R' before the bar, R after it (checked in a crop)",
    "tex": r"$D^1(R'|R,\ k)$",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": r"$D^1(R|R',\ k)$",
    "note": ("The class [R'] of the extension 0 -> k -> R' -> R -> 0 lies in D^1(R|R', k), the group of the "
             "exact sequences just above and below (D^1(R|R', k) (x)_k A_0, and [A'] -> [R'] (x) 1). "
             "The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring."),
})

# ---------------- page 108 ----------------
F.append({
    "page": 108,
    "where": "proof of 4.11, 'defines a cohomology class in H^2(X_0 D^0_{X_0}) given by ...'",
    "scan": "H^2(X_0 D^0_{X_0}) : no comma after X_0 (checked in a crop)",
    "tex": r"$H^2(X_0\ \underline{D}^0_{X_0})$",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": r"$H^2(X_0,\ \underline{D}^0_{X_0})$",
    "note": ("Every other H^2(X_0, D^0_{X_0}) on pp. 107-108 has the comma. The TeX keeps the printed "
             "reading. 'corrected' replaces the 'tex' substring."),
})
F.append({
    "page": 108,
    "where": "Remark 4.12, 'for a fixed deformation (R, X) of X_0 and deformations (R', U'^j) of U_0^i , the deformations ...'",
    "scan": "U_0^i : superscript i (dotted, checked in a crop)",
    "tex": r"of $U_0^i$ , the deformations",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": r"of $U_0^j$ , the deformations",
    "note": ("(R', U'^j) is a deformation of U_0^j (proof of 4.11: 'deformations (R', U'^j) of U_0^j to R''); "
             "the remark speaks of the U'^j throughout. The TeX keeps the printed reading. "
             "'corrected' replaces the 'tex' substring."),
})
F.append({
    "page": 108,
    "where": "Corollary 4.13 (a), 'In particular, dim M_{X_0} = dim H^1(X_0, D^0_{X_0}) + Sum_{c=1}^{r} dim M_{Spec(O^_{X_0,x_0})} .'",
    "scan": "summation index c=1 under the Sigma, r above; the summand's point is x with the same round subscript as X_0 (checked in a crop)",
    "tex": r"\widehat{\underline{O}}_{X_0,x_0}",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": r"\widehat{\underline{O}}_{X_0,x_c}",
    "note": ("The summand must run over the singular points x_1,...,x_r with the summation index; x_0 is not "
             "one of them. The proof on p. 109 writes the same sum as Sum_{i=1}^{r} dim M_{Spec(O^_{X_0,x_i})}. "
             "The TeX keeps the printed reading (index c and x_0). 'corrected' replaces the 'tex' substring."),
})

# ---------------- page 109 ----------------
F.append(dots(109, "proof of 4.13 (a), 'let (R, X) and (R_1, X_1),...,(R_r, X_r) be formal versal deformations'",
              r"\mathfrak{X}_1),....,(R_r", r"\mathfrak{X}_1),...,(R_r"))
F.append(dots(109, "proof of 4.13 (a), 'Spec(O_{X_0,x_1}),...,Spec(O_{X_0,x_r}) respectively'",
              r"x_1}),....,\mathrm{Spec}", r"x_1}),...,\mathrm{Spec}"))
F.append({
    "page": 109,
    "where": "proof of 4.13 (a), exact sequence '0 -> H^1(X_0,D^0_{X_0}) -> [M_{X_0}(k[e])] -> [M_{Spec(O^_{X_0,x_1})}(k[e])] ... [M_{Spec(O^_{X_0,x_r})}(k[e])]' ('is exact by 4.4')",
    "scan": "the last two terms are separated only by three dots; no product signs are typed or written in",
    "tex": r"(k[\epsilon])] ... [\underline{M}",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": r"(k[\epsilon])] \times ... \times [\underline{M}",
    "note": ("The target is the product of the [M_{Spec(O^_{X_0,x_i})}(k[e])], as in the functor of 4.13 (a) and in "
             "the Hom form of the same sequence on the next line (Hom(R_1 (x)^ ... (x)^ R_r, k[e])). The TeX keeps the "
             "printed reading. 'corrected' replaces the 'tex' substring."),
})

# ---------------- page 110 ----------------
F.append({
    "page": 110,
    "where": "4.14, 'it is trivial to write down explicitely'",
    "scan": "explicitely",
    "tex": "explicitely",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "explicitly",
    "note": "Spelling slip of the typescript. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
})
F.append({
    "page": 110,
    "where": "4.14, display 'A_0 = k[x_1,...,x_n]/(f_1,...,f_r)   S/J'",
    "scan": "blank space between (f_1,...,f_r) and S/J: the equality sign was never typed or written in (checked in a crop)",
    "tex": r"(f_1,...,f_r) \qquad S/J",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": r"(f_1,...,f_r) = S/J",
    "note": ("The next line defines S = k[x_1,...,x_n] and J = (f_1,...,f_r), so A_0 = S/J. The TeX keeps the printed "
             "gap (\\qquad). 'corrected' replaces the 'tex' substring."),
})
F.append(dots(110, "4.14, 'and f_1,...,f_r is an S-regular sequence. We then obtain'",
              r"and  $f_1,....,f_r$", r"and  $f_1,...,f_r$"))
F.append(dots(110, "4.14, 'generated by f_1(mod J^2),...,f_r(mod J^2)'",
              r"J^2),....,f_r(", r"J^2),...,f_r("))
F.append(dots(110, "4.14, ', since f_1,...,f_r is an S-regular sequence. We now'",
              r"since  $f_1,....,f_r$", r"since  $f_1,...,f_r$"))
F.append({
    "page": 110,
    "where": "4.14, 'is a finite-dimensional vector space over k , say A has isolated non-smooth points only'",
    "scan": "A without a subscript (end of the line; nothing below it, checked in a crop)",
    "tex": r"say  $A$ has isolated",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": r"say  $A_0$ has isolated",
    "note": ("Only A_0 is defined in 4.14 (A_0 = S/J); the condition on D^1(A_0|k, A_0) is about A_0. The TeX keeps the "
             "printed reading. 'corrected' replaces the 'tex' substring."),
})
F.append(dots(110, "4.14, 'choose p_j : J/J^2 -> A_0 (j = 1, 2,...,d)'",
              r"2,....,d", r"2,...,d"))
F.append(dots(110, "4.14, 'Now choose P_{jk} in Lambda[x_1,...,x_n]'",
              r"\Lambda[x_1,....,x_n]", r"\Lambda[x_1,...,x_n]"))
F.append(dots(110, "4.14, display 'R = Lambda[[t_1,...,t_d]]'",
              r"t_1,....,t_d", r"t_1,...,t_d"))
F.append(dots(110, "4.14, display 'B = R[x_1,...,x_n]/(G_1,...,G_r)' (two ellipses)",
              r"R[x_1,....,x_n]/(G_1,....,G_r)", r"R[x_1,...,x_n]/(G_1,...,G_r)"))
F.append({
    "page": 110,
    "where": "4.14, 'where G_j = F_j - Sum_{i=1}^{d} t_i P_{ji}'",
    "scan": "t_i P_{ji} : subscript j then i",
    "tex": r"t_i P_{ji}",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": r"t_i P_{ij}",
    "note": ("By the definition a few lines up, P_{ji} lifts p_j(f_i): first index a basis index (1..d), second a "
             "generator index (1..r). In G_j (j = 1..r) summed over i = 1..d the indices must be P_{ij} "
             "(lift of p_i(f_j)). The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring."),
})
F.append(dots(110, "4.14, 'Since R[x_1,...,x_n] is R-flat'",
              r"Since $R[x_1,....,x_n]$", r"Since $R[x_1,...,x_n]$"))
F.append(dots(110, "4.14, 'and G_1,...,G_r modulo m_R'",
              r"$G_1,....,G_r$  modulo", r"$G_1,...,G_r$  modulo"))
F.append(dots(110, "4.14, '(which becomes f_1,...,f_r)'",
              r"becomes  $f_1,....,f_r$)", r"becomes  $f_1,...,f_r$)"))
F.append(dots(110, "4.14, 'is a regular sequence in k (x)_R R[x_1,...,x_n]'",
              r"\otimes_R R[x_1,....,x_n]", r"\otimes_R R[x_1,...,x_n]"))

# ---------------- checks ----------------
ok = True
texts = {}
for f in F:
    p = f["page"]
    if p not in texts:
        with open(os.path.join(FOLDER, f"page_{p:03d}.tex"), encoding="utf-8", newline="") as fh:
            texts[p] = fh.read()
    t = texts[p]
    if f["fix"] is not None:
        n = t.count(f["fix"]["old"])
        if n != 1:
            ok = False
            print("FIX OLD COUNT", n, p, repr(f["fix"]["old"]))
        if "%%%%%%%%%%" in f["fix"]["old"]:
            ok = False
            print("MARKER IN OLD", p)
    if f["kind"] == "misprint_in_print":
        n = t.count(f["tex"])
        if n != 1:
            ok = False
            print("TEX COUNT", n, p, repr(f["tex"]))

# applying all fixes in order must leave each later 'old' still unique
for p, t in texts.items():
    cur = t
    for f in [g for g in F if g["page"] == p and g["fix"] is not None]:
        n = cur.count(f["fix"]["old"])
        if n != 1:
            ok = False
            print("SEQUENTIAL COUNT", n, p, repr(f["fix"]["old"]))
        cur = cur.replace(f["fix"]["old"], f["fix"]["new"], 1)
    print(p, "remaining ',....,':", cur.count(",....,"))

if ok:
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(F, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("written", OUT, len(F))
    for p in sorted(texts):
        norm = sum(1 for f in F if f["page"] == p and f["kind"] != "misprint_in_print")
        mis = sum(1 for f in F if f["page"] == p and f["kind"] == "misprint_in_print")
        print(p, norm, mis)
else:
    print("NOT WRITTEN")
