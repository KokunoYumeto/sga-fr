import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

BATCH = "C:/Users/user/Documents/sga_scan_check_20261105/run_7I/b041_045"
OUT = "C:/Users/user/Documents/sga_scan_check_20261105/run_7I/findings_041_045.json"

F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "confidence": confidence,
        "fix": fix,
    }
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 41 ----------------
add(41,
    "Proof of 1.10 (i), 'such that α_iφ_i = φ_{i-1} for all i < n'",
    "α_iφ_i = φ_{i-1}: the subscript of φ is a dotted i (the 1 of φ_{i-1} has a flag and is taller)",
    r"$\alpha_i\varphi_1 = \varphi_{i-1}$",
    "formula", "high",
    {"old": r"\alpha_i\varphi_1", "new": r"\alpha_i\varphi_i"},
    "Wrong subscript in the TeX: the print has φ_i, which is also the required reading (φ_i : ξ → a_i in the same sentence).")

add(41,
    "Proposition 1.10 (ii), first line, 'If ξ is an object in Â such that'",
    "Â with its hat but no underline under the A; 'in' before it and 'such that' after it are underlined",
    r"\underline{is an object in} $\hat{\underline{A}}$ \underline{such that}",
    "misprint_in_print", "medium",
    {"old": r"$\hat{\underline{A}}$ \underline{such that}", "new": r"$\hat{A}$ \underline{such that}"},
    "The category letter lost its underline (Â is underlined in its other places on pp. 41-45, e.g. in (i) and two lines later in 'object of Â , if it exists'; the other exceptions are the next finding and the proof of (ii)). The TeX silently supplies the underline; the fix restores the printed plain Â. 'corrected' is the current TeX.",
    corrected=r"$\hat{\underline{A}}$ \underline{such that}")

add(41,
    "Proposition 1.10 (ii), 'then every endomorphism of ξ in Â is an automorphism'",
    "Â with its hat but no underline; 'in' before it and 'is an auto-' after it are underlined",
    r"\underline{in} $\hat{\underline{A}}$ \underline{is an automorphism.",
    "misprint_in_print", "medium",
    {"old": r"\hat{\underline{A}}$ \underline{is an automorphism.", "new": r"\hat{A}$ \underline{is an automorphism."},
    "Same omission of the category underline as in 'is an object in Â' on the same statement. The TeX silently supplies the underline; the fix restores the printed plain Â. 'corrected' is the current TeX.",
    corrected=r"\hat{\underline{A}}$ \underline{is an automorphism.")

add(41,
    "Proof of 1.10 (ii), 'Let ξ --α--> ξ be a map in Â .'",
    "Â with its hat but no underline",
    r"be a map in $\hat{A}$",
    "misprint_in_print", "medium",
    None,
    "Category letter without its underline (cf. the two places in the statement of (ii)). The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    corrected=r"be a map in $\hat{\underline{A}}$")

add(41,
    "Proof of 1.10 (i), sequence '--- → a_n --α_n--> a_{n-1} → --- → a_1 --α_1-- a_0'",
    "a_1 —α_1— a_0: a plain rule with α_1 above it and no arrowhead (all the other arrows of the sequence have heads)",
    r"a_1 \overset{\alpha_1}{\relbar\joinrel\relbar} a_0",
    "misprint_in_print", "medium",
    None,
    "The rule ends cleanly (not a lost stroke); α_1 : a_1 → a_0 is one of the surjective maps of the sequence. The TeX keeps the printed headless rule. 'corrected' replaces the 'tex' substring.",
    corrected=r"a_1 \xrightarrow{\ \alpha_1\ } a_0")

add(41,
    "Proof of 1.10 (i), 'Assume that there exists maps φ_i : ξ → a_i'",
    "Assume that there exists maps",
    r"Assume that there exists maps",
    "misprint_in_print", "low",
    None,
    "Agreement slip (plural subject). The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    corrected=r"Assume that there exist maps")

# ---------------- page 42 ----------------
add(42,
    "Proof of Theorem 1.11, first word, 'Proof; (Necessity)'",
    "Proof; : a semicolon after the underlined 'Proof' (the proofs on p. 41 have 'Proof:')",
    r"\underline{Proof};",
    "misprint_in_print", "low",
    None,
    "Shift slip on the typewriter's ;/: key. The TeX keeps the printed semicolon. 'corrected' replaces the 'tex' substring.",
    corrected=r"\underline{Proof}:")

add(42,
    "Proof of 1.11 (Necessity), 'the composit map ξ → a_1 → a can be lifted to a_2'",
    "the composit map",
    r"the composit map",
    "misprint_in_print", "medium",
    None,
    "Misspelling of 'composite', as in 'A composit of' (Ax. 2, p. 32). The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    corrected=r"the composite map")

# ---------------- page 43 ----------------
add(43,
    "Proof of 1.11 (Sufficiency), 'Then ã(k[ε]) : Hom_{Λ-alg}(R_1,k[ε]) → [A(k[ε])] is bijective, where R_1 = P(a_1)'",
    "ã(k[ε]) : a tilde over a, no subscript",
    r"$\tilde{a}(k[\epsilon])",
    "misprint_in_print", "medium",
    None,
    "The map is the one induced by the object a_1 (its source is Hom(R_1,k[ε]) with R_1 = P(a_1)), so the index 1 is missing. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    corrected=r"$\tilde{a}_1(k[\epsilon])")

add(43,
    "Proof of 1.11 (Sufficiency), 'such that Ω̄_{a_3} → Ω̄_{a_2} , is bijective etc.'",
    "Ω̄_{a_3} → Ω̄_{a_2} , is bijective : a stray comma before 'is'",
    r"\overline{\Omega}_{a_2}$  , is bijective",
    "misprint_in_print", "low",
    None,
    "The comma splits subject and verb (the parallel clause one line up, 'such that Ω̄_{a_2} → Ω̄_{a_1} is bijective', has none). The TeX keeps the printed comma. 'corrected' replaces the 'tex' substring.",
    corrected=r"\overline{\Omega}_{a_2}$  is bijective")

add(43,
    "Proof of 1.11 (Sufficiency), 'so that ξ(k[ε]) : Hom_{Λ-alg}(R,k[ε] → [A(k[ε])] is bijective'",
    "Hom_{Λ-alg}(R,k[ε] → : the closing parenthesis after k[ε] is not printed",
    r"(R,k[\epsilon] \to",
    "misprint_in_print", "high",
    None,
    "Unbalanced parenthesis (cf. 'Hom_{Λ-alg}(R_1,k[ε]) →' six lines up). The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    corrected=r"(R,k[\epsilon]) \to")

add(43,
    "Proof of 1.11 (Sufficiency), 'h : ξ → a is factored as a composit map'",
    "a composit map",
    r"a composit map",
    "misprint_in_print", "medium",
    None,
    "Misspelling of 'composite' (as on p. 42). The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    corrected=r"a composite map")

# ---------------- page 44 ----------------
add(44,
    "Remark 1.12, line after the sequence, 'be an infinite sequences of arrows in A such that'",
    "be an infinite sequences of arrows",
    r"an infinite sequences of arrows",
    "misprint_in_print", "high",
    None,
    "Singular needed after 'an'. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    corrected=r"an infinite sequence of arrows")

# ---------------- page 45 ----------------
add(45,
    "1.15, first line, 'we biefly explain'",
    "biefly",
    r"biefly",
    "misprint_in_print", "high",
    None,
    "Typing error for 'briefly'. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    corrected=r"briefly")

add(45,
    "1.15, second line, 'the preceeding theory'",
    "preceeding",
    r"preceeding",
    "misprint_in_print", "high",
    None,
    "Typing error for 'preceding'. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    corrected=r"preceding")

add(45,
    "last paragraph, 'the corresponding homomorphism of algebras in C_{Λ,k} or in Ĉ_{Λ,K} is'",
    "C_{Λ,k} : small k in the subscript (every other C_{Λ,K} on the page has a capital K)",
    r"$C_{\Lambda,k}$",
    "misprint_in_print", "high",
    None,
    "A is a cofibered groupoid over C_{Λ,K} (same sentence group), so the maps are in C_{Λ,K}. The TeX keeps the printed small k. 'corrected' replaces the 'tex' substring.",
    corrected=r"$C_{\Lambda,K}$")


# ---------------- checks ----------------
ok = True
texts = {}
for p in sorted({f["page"] for f in F}):
    with open(f"{BATCH}/page_{p:03d}.tex", encoding="utf-8", newline="") as fh:
        texts[p] = fh.read()
for f in F:
    t = texts[f["page"]]
    n_tex = t.count(f["tex"])
    if n_tex < 1:
        print("TEX NOT FOUND", f["page"], repr(f["tex"]))
        ok = False
    if f["fix"] is not None:
        old = f["fix"]["old"]
        n = t.count(old)
        if n != 1:
            print("FIX OLD COUNT", n, f["page"], repr(old))
            ok = False
        if "%%%%%%%%%%" in old:
            print("MARKER IN OLD", f["page"])
            ok = False
    if f["kind"] == "misprint_in_print" and f["fix"] is None:
        # kept misprint: the tex substring should be unique so 'corrected' can replace it
        if n_tex != 1:
            print("KEPT-MISPRINT TEX NOT UNIQUE", n_tex, f["page"], repr(f["tex"]))
            ok = False

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

from collections import Counter
c = Counter((f["page"], f["kind"] == "misprint_in_print") for f in F)
for p in range(41, 46):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
print("checks ok" if ok else "CHECKS FAILED", len(F))
