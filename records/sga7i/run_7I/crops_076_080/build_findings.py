import json

OUT = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\findings_076_080.json"

TOR_NOTE = (
    "In math mode $Tor$ sets three italic variables T, o, r; the print has the upright operator name, "
    "as everywhere in the exposé, and the rest of the file writes \\mathrm{Tor} (pp. 77-78, 81-82, 86) "
    "or \\operatorname{Tor} (p. 79). p. 76 is the only page with $Tor$: five times (this entry and the next four font entries)."
)

F = []

def add(**kw):
    F.append(kw)

# ---------------- page 76 ----------------
add(page=76,
    where="Remark 3.4, 'every presheaf on P_{A|R} is actually a sheaf i.e., P̃_{A|R} = P_{A|R} .'",
    scan="P̃_{A|R} = P_{A|R} : no check on the right-hand P (clean in a crop); the next line types the check on P̌_{A|R}",
    tex=r"\widetilde{\underline{P}}_{A|R} = \underline{P}_{A|R}",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"\widetilde{\underline{P}}_{A|R} = \check{\underline{P}}_{A|R}",
    note="'Every presheaf is a sheaf' says that the category of sheaves is that of presheaves, P̃ = P̌; "
         "the next sentence, 'the restriction functor C̃_{A|R} → P̌_{A|R} is an equivalence', uses exactly this. "
         "The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.")

add(page=76,
    where="Lemma 3.5 (i), 'If Tor^R_1(B,S) = 0 , then the canonical map'",
    scan="Tor (upright operator name)",
    tex=r"$Tor^{R}_{1}(B,S)",
    kind="font", confidence="medium",
    fix={"old": r"$Tor^{R}_{1}(B,S)", "new": r"$\mathrm{Tor}^{R}_{1}(B,S)"},
    note=TOR_NOTE)

add(page=76,
    where="Lemma 3.5 (ii), 'If Tor^R_i(C,S) = 0 for all 0 < i < n'",
    scan="Tor (upright)",
    tex=r"$Tor^{R}_{i}(C,S)",
    kind="font", confidence="medium",
    fix={"old": r"$Tor^{R}_{i}(C,S)", "new": r"$\mathrm{Tor}^{R}_{i}(C,S)"},
    note="Same as the entry for 3.5 (i).")

add(page=76,
    where="Lemma 3.5 (ii), 'and Tor^R_i(B,S) = 0 for all 0 < i < n'",
    scan="Tor (upright)",
    tex=r"$Tor^{R}_{i}(B,S)",
    kind="font", confidence="medium",
    fix={"old": r"$Tor^{R}_{i}(B,S)", "new": r"$\mathrm{Tor}^{R}_{i}(B,S)"},
    note="Same as the entry for 3.5 (i). Does not overlap the misprint entry for the inequality of this clause.")

add(page=76,
    where="Lemma 3.5 (ii), 'then Tor^R_i(B' ×_B C, S) = 0 for all 0 < i < n'",
    scan="Tor (upright)",
    tex=r"$Tor^{R}_{i}(B'",
    kind="font", confidence="medium",
    fix={"old": r"$Tor^{R}_{i}(B'", "new": r"$\mathrm{Tor}^{R}_{i}(B'"},
    note="Same as the entry for 3.5 (i).")

add(page=76,
    where="Lemma 3.5 (ii), 'and Tor^R_i(B,S) = 0 for all 0 < i < n , then'",
    scan="0 < i < n : a plain < before n, no bar under it (checked in a crop)",
    tex=r"\underline{for all}  $0 < i < n$  , \underline{then}",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"\underline{for all}  $0 < i \leq n$  , \underline{then}",
    note="The hypothesis on B must reach i = n: B' being flat, Tor_i(J,S) ≅ Tor_{i+1}(B,S), and the proof on p. 77 says "
         "'Tor^R_i(B, S) = 0 for all 0 < i ≤ n by hypothesis'; 3.6 (b) applies 3.5 (ii) under exactly 0 < i ≤ n. "
         "The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.")

add(page=76,
    where="Proof of 3.5 (i), 'If Tor^R_i(B, S) = 0 , then' (font of Tor)",
    scan="Tor (upright)",
    tex=r"(i)  If  $Tor",
    kind="font", confidence="medium",
    fix={"old": r"(i)  If  $Tor", "new": r"(i)  If  $\mathrm{Tor}"},
    note="Same as the entry for 3.5 (i). Listed before the misprint entry for the index of this Tor; the two edits do not overlap.")

add(page=76,
    where="Proof of 3.5 (i), 'If Tor^R_i(B, S) = 0 , then' (index)",
    scan="Tor^R_i(B, S): the index is a dotted i (checked in a crop against the 1 of the statement (i))",
    tex=r"^{R}_{1}(B,\ S)",
    kind="misprint_in_print", confidence="high",
    fix={"old": r"^{R}_{1}(B,\ S)", "new": r"^{R}_{i}(B,\ S)"},
    corrected=r"^{R}_{1}(B,\ S)",
    note="The exactness of 0 → J⊗_R S → B'⊗_R S → B⊗_R S → 0 needs Tor_1, the hypothesis of the statement (i); "
         "the proof of 3.6 (a) reads 'If Tor^R_1(B, S) = 0'. The TeX silently corrects it; the fix restores the printed i. "
         "'corrected' is the current TeX.")

# ---------------- page 77 ----------------
add(page=77,
    where="First line, 'and therefore (B' ×_B C) ⊗_R S → (B'⊗_R S) ×_{(B⊗_R S)} (C⊗_R S) is an isomorphism'",
    scan="(B'⊗_B C)⊗_R S : the first operator is a circled ⊗ with B under it (checked in a crop)",
    tex=r"(B'\times_B C)\otimes_R S",
    kind="misprint_in_print", confidence="high",
    fix={"old": r"(B'\times_B C)\otimes_R S", "new": r"(B'\otimes_B C)\otimes_R S"},
    corrected=r"(B'\times_B C)\otimes_R S",
    note="The fibre product B' ×_B C, as in the statement 3.5 (i) and the diagram on p. 76. "
         "The TeX silently corrects it; the fix restores the printed ⊗. 'corrected' is the current TeX.")

add(page=77,
    where="Corollary 3.6 (a), 'Let A, S be R-algebras. If'",
    scan="'be' and 'algebras. If' are underlined; the underline breaks under 'R-' (checked in a crop)",
    tex=r"\underline{be R-algebras. If}",
    kind="underline", confidence="high",
    fix={"old": r"\underline{be R-algebras. If}", "new": r"\underline{be} R-\underline{algebras. If}"},
    note="Underline extent only. On pp. 77-78 the typist leaves 'R-' out of the underline (here, 'is R-flat', "
         "'R-algebra map', p. 78 'be R-algebras'); p. 76 underlines through it ('be an R-algebra.', 'is R-flat.'). "
         "The file writes the same pattern on p. 81 as \\underline{are} $R$\\underline{-algebras ...}.")

add(page=77,
    where="Corollary 3.6 (a), 'the canonical map Ȟ˙(A⊗_R S|S, G) → Ȟ˙(A|R, SG)'",
    scan="SG with no check on the S (clean in a crop); the check is typed over the H only",
    tex=r"\check{H}^{\cdot}(A|R,\ SG)",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"\check{H}^{\cdot}(A|R,\ \check{S}G)",
    note="The presheaf is ŠG (X ↦ G(X⊗_R S)), written ŠG in the next sentence ('Ȟ(ŠG)') and in the proof "
         "('Ȟ˙(B|R, ŠG)'). The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.")

add(page=77,
    where="Corollary 3.6 (a), 'In particular if S is R-flat, then the canonical map'",
    scan="'is' and 'flat, then the canonical map' are underlined; the underline breaks under 'R-' (checked in a crop)",
    tex=r"\underline{is R-flat, then the canonical map}",
    kind="underline", confidence="high",
    fix={"old": r"\underline{is R-flat, then the canonical map}", "new": r"\underline{is} R-\underline{flat, then the canonical map}"},
    note="Underline extent only, as above.")

add(page=77,
    where="Corollary 3.6 (a), 'then the canonical map ŠȞ˙(G) → Ȟ(ŠG) is an isomorphism'",
    scan="ŠȞ˙(G) → Ȟ(ŠG): neither H is underlined, and the second H has no degree mark (checked in a crop)",
    tex=r"\check{S}\check{H}^{\cdot}(G) \to \check{H}(\check{S}G)",
    kind="misprint_in_print", confidence="low", fix=None,
    corrected=r"\check{S}\underline{\check{H}}^{\cdot}(G) \to \underline{\check{H}}^{\cdot}(\check{S}G)",
    note="The map is one of Čech cohomology presheaves, as the proof concludes: 'i.e. Š H̲ˇ˙(G) → H̲ˇ˙(ŠG) is an "
         "isomorphism', with both H underlined and both degree marks. Low: a notation slip rather than a typing error. "
         "The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring (with the file's present \\cdot).")

add(page=77,
    where="Corollary 3.6 (b), 'Let P → B be a surjective R-algebra map, where'",
    scan="'be a surjective' and 'algebra map, where' are underlined; the underline breaks under 'R-' (checked in a crop)",
    tex=r"\underline{be a surjective R-algebra map, where}",
    kind="underline", confidence="high",
    fix={"old": r"\underline{be a surjective R-algebra map, where}", "new": r"\underline{be a surjective} R-\underline{algebra map, where}"},
    note="Underline extent only, as above.")

# ---------------- page 78 ----------------
add(page=78,
    where="Proposition 3.7 (a), 'Let A, S be R-algebras. If'",
    scan="'be' and 'algebras. If' are underlined; the underline breaks under 'R-' (checked in a crop)",
    tex=r"\underline{be R-algebras. If}",
    kind="underline", confidence="high",
    fix={"old": r"\underline{be R-algebras. If}", "new": r"\underline{be} R-\underline{algebras. If}"},
    note="Underline extent only, as in 3.6 (a) on p. 77.")

add(page=78,
    where="Proposition 3.7 (b), 'the canonical map ... is an isomorphism for all n > 0'",
    scan="is an iso- | morphism : the word is divided at the line end",
    tex=r"\underline{is an iso-morphism for all}",
    kind="other", confidence="high",
    fix={"old": r"iso-morphism", "new": r"isomorphism"},
    note="The TeX keeps the print's line-end hyphen inside the word.")

add(page=78,
    where="Proof of 3.7 (a), 'Since the functor S sends a polynomial algebras over R to polynomial algebras over S'",
    scan="sends a polynomial algebras over R",
    tex=r"sends a polynomial algebras over",
    kind="misprint_in_print", confidence="low", fix=None,
    corrected=r"sends polynomial algebras over",
    note="Agreement slip ('a' with a plural); the parallel sentence on p. 79 reads 'f sends polynomial algebras over R to "
         "polynomial algebras over R'. Low: possibly the author's own wording. The TeX keeps the printed reading. "
         "'corrected' replaces the 'tex' substring.")

# ---------------- page 79 ----------------
add(page=79,
    where="Proof of 3.7 (a), induction hypothesis, 'for all X ∈ ob(C_{A|R}) such that Tor^R_i(X, S) = 0 for all 0 i n .'",
    scan="0   i   n : blank spaces, no inequality signs typed or written (clean in a crop)",
    tex=r"for all  $0\ \ \ i\ \ \ n$",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"for all  $0 < i < n$",
    note="The signs were never filled in. The induction hypothesis must read 0 < i < n: it is applied to the fibre products "
         "P ×_X ... ×_X P, which by 3.6 (b) only have Tor_i = 0 for 0 < i < n when Tor_i(X, S) = 0 for 0 < i ≤ n "
         "(the next sentence). The TeX keeps the printed blanks. 'corrected' replaces the 'tex' substring.")

add(page=79,
    where="Proof of 3.7 (a), 'we get that H^n(X⊗_R S|S, F) → H^n(X|R, S̃F) is an isomorphism'",
    scan="H^n(X_R S|S, F): R under an empty space, no ⊗ (clean in a crop)",
    tex=r"X\underset{R}{\phantom{\otimes}}S",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"X\underset{R}{\otimes}S",
    note="The tensor sign is missing in the print; the TeX keeps the gap with \\phantom. 'corrected' replaces the 'tex' substring.")

add(page=79,
    where="Proof of 3.7 (b), 'Ȟ˙(X|R, f̌G) = H˙({P' → X}, f̌G) = H ({P'⊗_R P → X⊗_R P}, G) = Ȟ˙(X⊗_R P|R, G)'",
    scan="the third H has no degree mark; a blank follows it (clean in a crop)",
    tex=r"= H\ (\{P'",
    kind="misprint_in_print", confidence="low", fix=None,
    corrected=r"= H^{\cdot}(\{P'",
    note="The total degree, as on the other three H of the chain. Low: the inked degree dot may have been left out rather "
         "than mistyped. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring (with the file's present \\cdot).")

add(page=79,
    where="Proof of 3.7 (b), 'It follows that f̃ : C̃_{A⊗_R P|R} → C_{A|R} sends acyclic ones to acyclic ones'",
    scan="target C_{A|R} without a tilde (clean in a crop); the source C̃ has one",
    tex=r"\to \underline{C}_{A|R}$  sends acyclic",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"\to \underline{\widetilde{C}}_{A|R}$  sends acyclic",
    note="f̃ goes between the categories of sheaves, as two lines later ('f̃ : C̃_{A⊗_R P|R} → C̃_{A|R} is an exact "
         "functor'). The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.")

add(page=79,
    where="Proof of 3.7 (b), 'and hence f̃ : C̃_{A⊗_R P|R} → C̃_{A|R} is an exact functor by 3.2(c)'",
    scan="by 3.2(c) (checked in a crop)",
    tex=r"exact functor by 3.2(c)",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"exact functor by 3.3(c)",
    note="Lemma 3.2 (p. 74) has no parts; the exactness criterion on polynomial algebras is Corollary 3.3 (c), which the proof "
         "of 3.7 (a) cites for the same step ('S̃ ... is an exact functor by 3.3(c)', p. 78). The TeX keeps the printed "
         "reading. 'corrected' replaces the 'tex' substring.")

# ---------------- page 80 ----------------
add(page=80,
    where="Proof of 3.7 (c), 'G_{A|R} : Č_{A|R} → C̃_{A|R} is \"associated-sheaf\" functor'",
    scan="is \"associated-sheaf\" functor (no article)",
    tex=r'is "associated-sheaf"  functor',
    kind="misprint_in_print", confidence="low", fix=None,
    corrected=r'is the "associated-sheaf"  functor',
    note="Article missing. Low: possibly the author's own wording. The TeX keeps the printed reading. "
         "'corrected' replaces the 'tex' substring.")

add(page=80,
    where="Last line, 'The exact sequences (*) and (**) combined gives the desired exact sequence.'",
    scan="combined gives",
    tex=r"combined gives the desired",
    kind="misprint_in_print", confidence="low", fix=None,
    corrected=r"combined give the desired",
    note="Verb agreement slip (plural subject). Low: possibly the author's own wording. The TeX keeps the printed reading. "
         "'corrected' replaces the 'tex' substring.")

KEYS = ["page", "where", "scan", "tex", "kind", "confidence", "fix", "corrected", "note"]
out = []
for f in F:
    d = {}
    for k in KEYS:
        if k in f:
            d[k] = f[k]
    out.append(d)

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(out, fh, ensure_ascii=False, indent=1)
    fh.write("\n")
print(len(out), "findings written")
