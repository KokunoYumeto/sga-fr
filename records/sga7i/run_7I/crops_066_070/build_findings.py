import json

BASE = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I"
OUT = BASE + r"\findings_066_070.json"

F = []


def add(**kw):
    F.append(kw)


# ---------------- page 66 ----------------
add(page=66,
    where="Proof of 2.14, 'Since h_(R_0,R_1,...)(k[ε]) is totally disconnected, [h_(α_0,α_1)(k[ε]) and [ε(k[ε])] are both bijections'",
    scan="[h_(α_0,α_1)(k[ε])  and  [ε(k[ε])] : the first square bracket (faint but present) is opened and never closed",
    tex=r"[\underline{h}_{(\alpha_0,\alpha_1)}(k[\epsilon])",
    kind="misprint_in_print", confidence="medium",
    fix=None,
    corrected=r"[\underline{h}_{(\alpha_0,\alpha_1)}(k[\epsilon])]",
    note="Closing bracket missing: [ ] is the map induced on isomorphism classes, as in the parallel [ε(k[ε])] and in '[h_(R_0,R_1,...)(k[ε])]' in the proof of 2.12(b) (p. 65). The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.")

add(page=66,
    where="Diagram of the proof of 2.14, left vertical arrow h_{R_0} → h_(R_0,R_1,...) labelled ε",
    scan="ε to the LEFT of the shaft (outside the square)",
    tex=r'\arrow[u, "\epsilon"' + "'" + ']',
    kind="other", confidence="low",
    fix={"old": r'\arrow[u, "\epsilon"' + "'" + r'] \arrow[r', "new": r'\arrow[u, "\epsilon"] \arrow[r'},
    note="For an upward arrow the swap mark ' puts the label to the right of the shaft (inside the square); without it tikz-cd sets it to the left, as printed (checked by compiling a test diagram; the file's own comment block also records ε to the LEFT). Independent of the next fix.")

add(page=66,
    where="Same diagram, right vertical arrow h_{R_0} → h_(R_0,R_1,...) labelled ε",
    scan="ε to the RIGHT of the shaft (outside the square)",
    tex=r'& \underline{h}_{R_0} \arrow[u, "\epsilon"]',
    kind="other", confidence="low",
    fix={"old": r'& \underline{h}_{R_0} \arrow[u, "\epsilon"]', "new": r'& \underline{h}_{R_0} \arrow[u, "\epsilon"' + "'" + ']'},
    note="Without the swap mark an upward arrow gets its label on the left of the shaft (inside the square); the print, and the file's comment block, have ε on the right.")

add(page=66,
    where="First lines, end of Proposition 2.14, 'a normalized prorepresentation, if it exists, is unique'",
    scan="prorepresenta- | tion : the word is divided at the line end",
    tex=r"\underline{a normalized prorepresenta-} \underline{tion, if it exists,",
    kind="other", confidence="medium",
    fix={"old": r"prorepresenta-} \underline{tion", "new": r"prorepresentation"},
    note="The TeX keeps the print's line-end hyphen, so the word is set mid-line as 'prorepresenta- tion' (as 'equi- valence' on p. 65); the file joins the other divided words.")

add(page=66,
    where="Lemma 2.15, 'φ : A → B a minimally smooth functor'",
    scan="a mini- | mally : the word is divided at the line end",
    tex=r"\underline{a mini-} \underline{mally smooth functor. If}",
    kind="other", confidence="medium",
    fix={"old": r"\underline{a mini-} \underline{mally", "new": r"\underline{a minimally"},
    note="Line-end hyphen kept mid-line ('mini- mally'), as above. Does not overlap the underline fix on 'functor. If' below.")

add(page=66,
    where="Lemma 2.15, 'a minimally smooth functor. If A, B are homogeneous'",
    scan="the underline stops after 'functor'; the full stop and the space are not underlined; 'If' has its own underline",
    tex=r"\underline{mally smooth functor. If}",
    kind="underline", confidence="low",
    fix={"old": r"smooth functor. If}", "new": r"smooth functor}. \underline{If}"},
    note="Underline extent only. The full stop sits inside the \\underline, not at its end, so the global pass on final punctuation does not reach it.")

add(page=66,
    where="Lemma 2.15, 'If A, B are homogeneous, then φ is a C_Λ-equivalence'",
    scan="'are homogeneous' and 'then' are underlined separately; the comma is not underlined",
    tex=r"\underline{are homogeneous, then}",
    kind="underline", confidence="low",
    fix={"old": r"\underline{are homogeneous, then}", "new": r"\underline{are homogeneous}, \underline{then}"},
    note="Underline extent only, as above.")

# ---------------- page 67 ----------------
add(page=67,
    where="Corollary 2.16, 'the functor Isom_ξ : C_{R ⊗̂_Λ R} → (Ens) is prorepresentable'",
    scan="C underlined with the subscript R ⊗ R; the caret is typed directly above the ⊗ (Λ under it), i.e. the completed tensor product R ⊗̂_Λ R; no hat on C",
    tex=r"\underline{C}^{\wedge}_{R \otimes_{\wedge} R}",
    kind="symbol", confidence="high",
    fix={"old": r"\underline{C}^{\wedge}_{R \otimes_{\wedge} R} \longrightarrow (\mathrm{Ens})",
         "new": r"\underline{C}_{R \hat{\otimes}_{\wedge} R} \longrightarrow (\mathrm{Ens})"},
    note="The TeX moves the hat from the ⊗ to the C (a superscript ∧ on C). The caret stands over the ⊗ in all three places on this page, exactly as in C_{R_0 ⊗̂_Λ R_0} on pp. 68-69, which the file writes with \\hat{\\otimes} (also R_0 ⊗̂_Λ R_0 on p. 65). This answers the open question on 'p. 67 \\underline{C}^{\\wedge}' in the global issues list.")

add(page=67,
    where="Proof of 2.16, 'a minimally smooth functor Φ : h_{R_1} → Isom_ξ , which is a C_{R ⊗̂_Λ R}-equivalence by 2.15'",
    scan="caret above the ⊗ of the subscript, as in the statement",
    tex=r"\underline{C}^{\wedge}_{R \otimes_{\wedge} R}$-equivalence",
    kind="symbol", confidence="high",
    fix={"old": r"\underline{C}^{\wedge}_{R \otimes_{\wedge} R}$-equivalence",
         "new": r"\underline{C}_{R \hat{\otimes}_{\wedge} R}$-equivalence"},
    note="Same reading as in the statement of 2.16.")

add(page=67,
    where="Proof of 2.16, after the diagram T_1 → T ← T_2, 'in C_{R ⊗̂_Λ R} where T_2 → T is surjective'",
    scan="caret centred above the ⊗ of the subscript",
    tex=r"in  $\underline{C}^{\wedge}_{R \otimes_{\wedge} R}$",
    kind="symbol", confidence="high",
    fix={"old": r"in  $\underline{C}^{\wedge}_{R \otimes_{\wedge} R}$",
         "new": r"in  $\underline{C}_{R \hat{\otimes}_{\wedge} R}$"},
    note="Same reading as in the statement of 2.16.")

add(page=67,
    where="Corollary 2.16, 'such that Aut_{A(k[ε])}(1_ε) is of finite-dimensional'",
    scan="is of finite-dimensional",
    tex=r"is of finite-dimensional",
    kind="misprint_in_print", confidence="low",
    fix=None,
    corrected=r"is finite-dimensional",
    note="Two constructions run together ('is of finite dimension' / 'is finite-dimensional'); Theorem 2.17 (2) has 'are both finite-dimensional vector spaces'. Low: possibly the author's own wording. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.")

add(page=67,
    where="Theorem 2.17, 'Then it is prorepresentable by a (normalized) smooth cogroupoid'",
    scan="prorepresen- | table : the word is divided at the line end",
    tex=r"prorepresen-table",
    kind="other", confidence="medium",
    fix={"old": r"prorepresen-table", "new": r"prorepresentable"},
    note="The TeX keeps the line-end hyphen inside the word ('prorepresen-table'); as on p. 66.")

# ---------------- page 68 ----------------
add(page=68,
    where="Theorem 2.17 (2), '[A(k[ε])] and [Aut(1_ε)] are both finite-dimensional vector spaces over k'",
    scan="[A(k[ε])] with A not underlined",
    tex=r"$[A(k[\epsilon])]$",
    kind="misprint_in_print", confidence="medium",
    fix=None,
    corrected=r"$[\underline{A}(k[\epsilon])]$",
    note="Category letter without its underline (A is underlined in (1) and in '[A(k[ε])] is a finite-dimensional vector space' in the proof). The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.")

add(page=68,
    where="Proof of 2.17, display '[h(k[ε])] = Coker (Hom_{Λ-alg}(R_1,k[ε] ⇉ Hom_{Λ-alg}(R_0,k[ε])) as well as'",
    scan="no closing parenthesis after k[ε] in the first Hom",
    tex=r"(R_{1},k[\epsilon] \ \underset",
    kind="misprint_in_print", confidence="high",
    fix=None,
    corrected=r"(R_{1},k[\epsilon]) \ \underset",
    note="Hom_{Λ-alg}(R_1,k[ε]) is never closed, so the line's parentheses do not balance; the two Ker lines below close the same Hom. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.")

add(page=68,
    where="'where ξ_i(T) = ξ(f_i) and f_i : R_0 → T denotes the composit maps'",
    scan="the composit maps",
    tex=r"the composit maps",
    kind="misprint_in_print", confidence="high",
    fix=None,
    corrected=r"the composite maps",
    note="Misspelling of 'composite' (as on pp. 32, 42, 43, 62). The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.")

add(page=68,
    where="'Since ξ is a minimally versal formal object of A , the composit functor h_(R_0,R_0,...) → h_(R_0,R_1,...) → A'",
    scan="the composit functor",
    tex=r"the composit functor",
    kind="misprint_in_print", confidence="high",
    fix=None,
    corrected=r"the composite functor",
    note="Misspelling of 'composite', as above. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.")

# ---------------- page 69 ----------------
add(page=69,
    where="Corollary 2.20, 'Let A be a homogeneous cogroupoid over C_Λ prorepresented by a normalized smooth cogroupoid'",
    scan="be a homogeneous cogroupoid over",
    tex=r"\underline{be a homogeneous cogroupoid over}",
    kind="misprint_in_print", confidence="medium",
    fix=None,
    corrected=r"\underline{be a homogeneous groupoid over}",
    note="A is the cofibered groupoid over C_Λ of the paragraph just above ('Now let A be a cofibered groupoid over C_Λ prorepresented by a normalized smooth cogroupoid (R_0,R_1,...) via (ξ,φ)'); homogeneity and prorepresentation are properties of cofibered groupoids (cf. 'Let A be a homogeneous groupoid over C_Λ', Corollary 2.16), while a cogroupoid lives in Ĉ_Λ. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.")

# ---------------- page 70 ----------------
add(page=70,
    where="Remark 2.21, 'k ⊗_Λ φ = the image of φ under Isom_{A(R_0)}(ξ(s_1), ξ(s_2)) → Isom_{A(k ⊗_Λ R_1)}(k ⊗_Λ ξ(s_1), k ⊗_Λ ξ(s_2))'",
    scan="Isom_{A(R_0)}(ξ(s_1), ξ(s_2))",
    tex=r"\mathrm{Isom}_{\underline{A}(R_0)}",
    kind="misprint_in_print", confidence="high",
    fix=None,
    corrected=r"\mathrm{Isom}_{\underline{A}(R_1)}",
    note="ξ(s_1), ξ(s_2) are the direct images of ξ under s_1, s_2 : R_0 → R_1, objects over R_1, and φ : ξ_1(R_1) → ξ_2(R_1) (p. 68) is an isomorphism over R_1; the target of the map is correspondingly over k ⊗_Λ R_1. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.")

add(page=70,
    where="Remark 2.21, 'where k ⊗_Λ ξ = its direct image of ξ under the map R_0 → k ⊗_Λ R_0'",
    scan="its direct image of ξ",
    tex=r"its direct image of",
    kind="misprint_in_print", confidence="low",
    fix=None,
    corrected=r"the direct image of",
    note="'its ... of ξ' runs two constructions together; cf. '1_S = the direct image of 1 ∈ A(k) under the map k → S' (p. 69). Low: possibly the author's own wording. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.")

# ---------------- write ----------------
ORDER = ["page", "where", "scan", "tex", "kind", "confidence", "fix", "corrected", "note"]
out = []
for f in F:
    d = {k: f[k] for k in ORDER if k in f}
    out.append(d)
with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(out, fh, ensure_ascii=False, indent=1)
    fh.write("\n")
print("wrote", len(out))
