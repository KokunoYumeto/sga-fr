import json

base = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\b111_115"
outfile = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\findings_111_115.json"

KEEP = "The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring."

F = []


def m(page, where, scan, tex, corrected, confidence, note):
    F.append({
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": "misprint_in_print",
        "confidence": confidence,
        "fix": None,
        "corrected": corrected,
        "note": note + " " + KEEP,
    })


# ---- page 111 ----
m(111,
  "Remark 4.16, 'L. = L^{X_0/S_0} the relative cotangent complex of X_0 over S_0 , which is an element of the derived category D(X_0, O_X)'",
  "D(X_0, O_X): the underlined O has the subscript X alone, without the index 0 (checked in a crop)",
  r"D(X_0,\ \underline{O}_X)",
  r"D(X_0,\ \underline{O}_{X_0})",
  "medium",
  "Index slip: L^{X_0/S_0} is a complex on X_0, an object of the derived category of O_{X_0}-modules; no X is defined at this point (X is the general object of F, introduced in the next sentence).")

m(111,
  "Remark 4.16 (a), 'For an object X' of F , the group of automorphisms is canonically isomorphic to Ext^0(X_0; L.,I_{X_0})'",
  "For an object X' of F (the prime is clear in a crop)",
  r"For an object  $X'$",
  r"For an object  $X$",
  "medium",
  "The objects of F are the flat S-schemes X extending X'/S' (sentence before); X' is the given scheme over S'. Page 112 restates (a) as 'the sheaf of automorphisms of any object X of F (understood: automorphisms inducing the identity on X')'.")

# ---- page 112 ----
m(112,
  "Remark 4.16, spectral sequence display 'Ext*(X_0  L.,I_{X_0}) <- E_2^{p,q} = H^p(X_0, D^q_{X_0}(I_{X_0}))'",
  "Ext*(X_0  L.,I_{X_0}): blank where the semicolon belongs, no semicolon typed (checked in a crop)",
  r"\mathrm{Ext}^*(X_0 \quad L.,I_{X_0})",
  r"\mathrm{Ext}^*(X_0;\ L.,I_{X_0})",
  "high",
  "The semicolon was never typed; every other Ext(X_0; L.,I_{X_0}) on pp. 111-112 has it. The TeX keeps the printed gap with \\quad.")

m(112,
  "'On the other hand, the standart spectral sequence gives us'",
  "standart",
  "standart",
  "standard",
  "high",
  "Spelling slip.")

m(112,
  "Display after 'and the exact sequence in low degrees'",
  "0 - H^1(X_0,D^0_{X_0}) - Ext^1 - H^0(X_0,D^1_{X_0}) - H^2(X_0,D^0_{X_0}) - Ext^2 : the five maps are short hyphens without heads (checked in a crop)",
  r"0 - H^1(X_0,\underline{D}^0_{X_0}) - \mathrm{Ext}^1 - H^0(X_0,\underline{D}^1_{X_0}) - H^2(X_0,\underline{D}^0_{X_0}) - \mathrm{Ext}^2",
  r"0 \to H^1(X_0,\underline{D}^0_{X_0}) \to \mathrm{Ext}^1 \to H^0(X_0,\underline{D}^1_{X_0}) \to H^2(X_0,\underline{D}^0_{X_0}) \to \mathrm{Ext}^2",
  "medium",
  "The arrowheads were never typed: it is the exact sequence of low degree terms of the spectral sequence above, whose arrow (<-) is typed with a head, as are K -> F -> E -> 0 on pp. 114-115. The TeX keeps the printed hyphens.")

m(112,
  "'More precisely and generally, for a given local deformations (i.e. a section of the \"sheaf of isomorphism classes of local flat deformations\" )'",
  "for a given local deformations",
  "for a given local deformations",
  "for given local deformations",
  "low",
  "Number slip (article with a plural); the sentence before reads 'which corresponds to given local deformations'. Low: possibly the author's own wording.")

# ---- page 113 ----
m(113,
  "'More geometrically, and without using the global theory of the relative cotangentcomplex'",
  "cotangentcomplex (no space)",
  "cotangentcomplex",
  "cotangent complex",
  "high",
  "The space between the words was not typed; p. 111 has 'the relative cotangent complex'.")

m(113,
  "'Using the fact that the section of F is determined up to adding a section of D^1_{X_0}'",
  "F without underline here (checked in a crop); the same sheaf is underlined twice above in the paragraph ('the sheaf F of isomorphism classes of local solutions', 'choosing arbitrarily a section of F')",
  r"the section of  $F$  is determined",
  r"the section of  $\underline{F}$  is determined",
  "medium",
  "Left-out underline: F is the sheaf of isomorphism classes of local solutions, written underlined F in this paragraph and the category in (a)-(c).")

# ---- page 114 ----
m(114,
  "'We fistly recall the definition of Fitting ideals'",
  "fistly",
  "fistly",
  "firstly",
  "high",
  "Spelling slip.")

m(114,
  "Definition of the Fitting ideals, 'I^P_A(E) = Im(^{n-p}/\\ K (x) ^{n-p}/\\ F* -> A)   for p = 0, 1, 2, ...'",
  "I^P_A(E): a capital P as superscript (checked in a crop; the p of 'for p = 0, 1, 2' and of I^p_A in 5.1 has a descender)",
  r"I^P_A(E) = \mathrm{Im}",
  r"I^p_A(E) = \mathrm{Im}",
  "high",
  "Capital/small slip of the typist: the index is the p of 'for p = 0, 1, 2, ...' on the same line and of n-p.")

m(114,
  "'The ideals I^P_A(E) thus defined does not depend on the choice of a presentation'",
  "I^P_A(E): capital P (checked in a crop)",
  r"The ideals  $I^P_A(E)$",
  r"The ideals  $I^p_A(E)$",
  "high",
  "Capital/small slip, as in the defining display above.")

m(114,
  "'The ideals I^P_A(E) thus defined does not depend on the choice of a presentation and therefore are invariants'",
  "does not depend",
  "does not depend",
  "do not depend",
  "low",
  "Verb agreement slip (subject 'The ideals'; 'therefore are invariants' in the same sentence). Low: possibly the author's own wording.")

m(114,
  "'and therefore are invariants of A-module E , called the Fitting ideals of A-module E'",
  "invariants of A-module E ... Fitting ideals of A-module E (no article, twice)",
  r"invariants of $A$-module  $E$ , called the Fitting ideals of $A$-module  $E$",
  r"invariants of the $A$-module  $E$ , called the Fitting ideals of the $A$-module  $E$",
  "low",
  "Article missing, twice. Low: possibly the author's own wording.")

m(114,
  "5.1 (a), 'is an isomorphism for all P . In particular we have'",
  "for all P: capital P on the base line (checked in a crop); the display just above has I^p_A, I^p_B with small p",
  r"for all  $P$",
  r"for all  $p$",
  "high",
  "Capital/small slip: the quantified index is the p of I^p_A(E) and I^p_B in the display above.")

# ---- page 115 ----
m(115,
  "Globalized Fitting ideals, display 'Gamma(U, I^p_X(E)) ~-> I^p_{Gamma(U, O_x)}(Gamma(U, E))'",
  "O_x: the subscript is a small x (in a crop clearly lower than the capital X of I^p_X in the same display)",
  r"\underline{O}_x",
  r"\underline{O}_X",
  "medium",
  "Capital/small slip: the ring is the ring of sections over U of the structure sheaf O_X of the scheme X (a small x would be a point, and Gamma(U, -) of a stalk makes no sense).")

m(115,
  "End of the paragraph before Definition 5.2, 'and in turn we may consider the ideal sheaves I^p_X(Omega_{X|Y}) ..'",
  "I^p_X(Omega_{X|Y})  .. : two full stops (checked in a crop)",
  r"$\underline{I}_X^p(\underline{\Omega}_{X|Y})$  ..",
  r"$\underline{I}_X^p(\underline{\Omega}_{X|Y})$  .",
  "high",
  "Doubled full stop.")

# ---- checks ----
ok = True
for f in F:
    p = f["page"]
    txt = open(base + "\\page_%03d.tex" % p, encoding="utf-8").read()
    n = txt.count(f["tex"])
    if n != 1:
        ok = False
        print("TEX NOT UNIQUE/ABSENT", p, n, repr(f["tex"]))
    if f["fix"] is not None:
        n = txt.count(f["fix"]["old"])
        if n != 1:
            ok = False
            print("OLD NOT UNIQUE/ABSENT", p, n, repr(f["fix"]["old"]))
print("checks ok" if ok else "CHECK FAILURES")

with open(outfile, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

from collections import Counter
c = Counter((f["page"], f["kind"] == "misprint_in_print") for f in F)
for p in range(111, 116):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
