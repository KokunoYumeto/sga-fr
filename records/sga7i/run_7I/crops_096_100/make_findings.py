import json, os, sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I"
FOLDER = os.path.join(RUN, "b096_100")
OUT = os.path.join(RUN, "findings_096_100.json")

HEADLESS = r"\relbar\joinrel\relbar\joinrel\relbar"

F = []

# ---------------- page 98 ----------------
F.append({
    "page": 98,
    "where": "Proof of Lemma 4.2, 'Set S = R ×_R̄ R . Since I is nilpotent, ...'",
    "scan": "S = R ×_R̄ R : the second factor is R without a prime (checked in a crop)",
    "tex": r"$S = R \times_{\bar{R}} R$",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": r"$S = R \times_{\bar{R}} R'$",
    "note": "S is the ring R ×_R̄ R' of the lemma (E ×_Ē E' flat over R ×_R̄ R'); the next sentence uses R' as an S-module, and the proof of 4.3 writes S = R ×_R̄ R'. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
})
F.append({
    "page": 98,
    "where": "Proof of Corollary 4.3, 'the morphism i_X ∐_{i_X̄} i_{X'} : X_0 → X ∐_X̄ X' induces an isomorphism'",
    "scan": "X_0 → X   X' with X̄ typed under an empty space: the hand-written ∐ was never inserted (clean in a crop); every other amalgamated sum on the page has it",
    "tex": r"X \underset{\bar{X}}{\phantom{\amalg}} X'",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": r"X \underset{\bar{X}}{\amalg} X'",
    "note": "The target of i_X ∐ i_{X'} is the amalgamated sum X ∐_X̄ X'. The TeX keeps the printed gap with \\phantom. 'corrected' replaces the 'tex' substring.",
})

# ---------------- page 99 ----------------
F.append({
    "page": 99,
    "where": "Proof of Lemma 4.4 (special case), 'inducing the isomorphism k ⊗_{k[ε]} j_A : k ⊗_{k[ε]} A --~-- A_0'",
    "scan": "A —~— A_0 : a plain rule with ~ above it and no arrowhead; the rule ends cleanly (checked in a crop)",
    "tex": r"A \overset{\sim}{\longrightarrow} A_{0}",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": {"old": r"A \overset{\sim}{\longrightarrow} A_{0}",
            "new": r"A \overset{\sim}{" + HEADLESS + r"} A_{0}"},
    "corrected": r"A \overset{\sim}{\longrightarrow} A_{0}",
    "note": "The head was never typed (p. 96 has it in the same situation: A ⊗_R k --~--> A_0). The TeX silently supplies it; the fix restores the printed headless rule in the form used for the earlier headless rules of this exposé (\\relbar\\joinrel...). 'corrected' is the current TeX.",
})
F.append({
    "page": 99,
    "where": "Proof of Lemma 4.4, 'an exact sequence 0 → A_0 --ε-- A --j_A-- A_0 → 0 in which ε(A_0)^2 = 0'",
    "scan": "A_0 —ε— A —j_A— A_0 : two plain rules with ε and j_A above them, no arrowheads (checked in a crop); the outer 0 → A_0 and A_0 → 0 are typed arrows",
    "tex": r"\overset{\varepsilon}{\longrightarrow} A \overset{j_{A}}{\longrightarrow}",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": {"old": r"\overset{\varepsilon}{\longrightarrow} A \overset{j_{A}}{\longrightarrow}",
            "new": r"\overset{\varepsilon}{" + HEADLESS + r"} A \overset{j_{A}}{" + HEADLESS + r"}"},
    "corrected": r"\overset{\varepsilon}{\longrightarrow} A \overset{j_{A}}{\longrightarrow}",
    "note": "The heads were never typed; the same maps have heads in the diagram lower on the page (A_0 --ε--> A_1 --j_{A_1}--> A_0). The TeX silently supplies them; the fix restores the two printed headless rules. 'corrected' is the current TeX.",
})
F.append({
    "page": 99,
    "where": "diagram of an arrow A_1 → A_2 in E (0 → A_0 → A_1 → A_0 → 0 over 0 → A_0 → A_2 → A_0 → 0), end of the bottom row",
    "scan": "a full stop typed to the right of the bottom row, after the final 0",
    "tex": "no full stop (the STRUCTURE comment records it; the tikzcd omits it)",
    "kind": "punctuation",
    "confidence": "high",
    "fix": {"old": r"\end{tikzcd}", "new": r"\end{tikzcd}\quad ."},
    "note": "Sentence-final full stop of '... yielding a commutative diagram'. Placed after the tikzcd as in the earlier diagram fixes of this volume (p. 21).",
})
F.append({
    "page": 99,
    "where": "end of the special case, 'a canonical bijection [M_{X_0}(k[ε])] --~-- H^0(X_0, D^1_{X_0}) via Γ(X_0, -)'",
    "scan": "[M_{X_0}(k[ε])] —~— H^0(...) : a plain rule with ~ above it, no arrowhead (checked in a crop)",
    "tex": r"\overset{\sim}{\longrightarrow} H^{0}",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": {"old": r"\overset{\sim}{\longrightarrow} H^{0}",
            "new": r"\overset{\sim}{" + HEADLESS + r"} H^{0}"},
    "corrected": r"\overset{\sim}{\longrightarrow} H^{0}",
    "note": "Same headless rule as in 'k ⊗ A --~-- A_0' above. The TeX silently supplies the head; the fix restores the printed rule. 'corrected' is the current TeX.",
})

# ---------------- page 100 ----------------
F.append({
    "page": 100,
    "where": "(General case), 'the composite map [M_{X_0}(k[ε])] → [M_{U_0}(k[ε])] --~-- H^0(U_0, D^1_{X_0})'",
    "scan": "[M_{U_0}(k[ε])] —~— H^0(U_0, ...) : a plain rule with ~ above it, no arrowhead (checked in a crop); the first arrow of the composite is a typed →",
    "tex": r"\overset{\sim}{\longrightarrow}",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": {"old": r"\overset{\sim}{\longrightarrow}",
            "new": r"\overset{\sim}{" + HEADLESS + r"}"},
    "corrected": r"\overset{\sim}{\longrightarrow}",
    "note": "The second map of a composite, so an arrow; the head was never typed (as on p. 99). The TeX silently supplies it; the fix restores the printed rule. 'corrected' is the current TeX.",
})
F.append({
    "page": 100,
    "where": "Theorem 4.5(a), cartesian square Y → X over Spf(S) → Spf(R), end of the bottom row",
    "scan": "a full stop typed to the right of Spf(R)",
    "tex": "no full stop (the STRUCTURE comment records it; the tikzcd omits it)",
    "kind": "punctuation",
    "confidence": "high",
    "fix": {"old": r"\end{tikzcd}", "new": r"\end{tikzcd}\quad ."},
    "note": "Sentence-final full stop of '... such that the diagram below is cartesian'. Placed after the tikzcd as for p. 99.",
})
FRAK_NOTE = ("The formal schemes of Theorem 4.5 are typed with the same Fraktur letters as the formal scheme 𝔛 of 4.1(c) on p. 96 "
             "(compared in crops), which the TeX writes \\mathfrak{X} there and on pp. 102, 105, 109 ((R, \\mathfrak{X}) formal versal deformation). "
             "Page 100 alone writes \\mathcal{X}, \\mathcal{Y}. Apply with the other four \\mathcal fixes on this page; the STRUCTURE comment below the diagram also says 'script'.")
F.append({
    "page": 100,
    "where": "Theorem 4.5(a), 'If (R, 𝔛) is a formal versal deformation of X_0'",
    "scan": "(R, 𝔛) : the typewriter Fraktur X",
    "tex": r"(R,\ \mathcal{X})",
    "kind": "font",
    "confidence": "medium",
    "fix": {"old": r"(R,\ \mathcal{X})", "new": r"(R,\ \mathfrak{X})"},
    "note": FRAK_NOTE,
})
F.append({
    "page": 100,
    "where": "Theorem 4.5(a), 'then for any (S, 𝔜) ∈ ob(M̂_{X_0})'",
    "scan": "(S, 𝔜) : the typewriter Fraktur Y",
    "tex": r"(S,\ \mathcal{Y})",
    "kind": "font",
    "confidence": "medium",
    "fix": {"old": r"(S,\ \mathcal{Y})", "new": r"(S,\ \mathfrak{Y})"},
    "note": "As the previous entry.",
})
F.append({
    "page": 100,
    "where": "Theorem 4.5(a), 'there is a map (φ,Φ) : (R,𝔛) → (S,𝔜)'",
    "scan": "(R,𝔛) → (S,𝔜) : typewriter Fraktur X and Y",
    "tex": r"(R,\mathcal{X}) \to (S,\mathcal{Y})",
    "kind": "font",
    "confidence": "medium",
    "fix": {"old": r"(R,\mathcal{X}) \to (S,\mathcal{Y})", "new": r"(R,\mathfrak{X}) \to (S,\mathfrak{Y})"},
    "note": "As the previous entries.",
})
F.append({
    "page": 100,
    "where": "Theorem 4.5(a), cartesian square, top row 𝔜 --Φ--> 𝔛",
    "scan": "𝔜 and 𝔛 : typewriter Fraktur Y and X",
    "tex": r"\mathcal{Y} \arrow[r, " + '"' + r"\Phi" + '"' + r"] \arrow[d] & \mathcal{X}",
    "kind": "font",
    "confidence": "medium",
    "fix": {"old": r"\mathcal{Y} \arrow[r, " + '"' + r"\Phi" + '"' + r"] \arrow[d] & \mathcal{X}",
            "new": r"\mathfrak{Y} \arrow[r, " + '"' + r"\Phi" + '"' + r"] \arrow[d] & \mathfrak{X}"},
    "note": "As the previous entries.",
})
F.append({
    "page": 100,
    "where": "Theorem 4.5(a), 'Furthermore a formal versal deformation (R,𝔛) of X_0 prorepresents the functor'",
    "scan": "(R,𝔛) : typewriter Fraktur X",
    "tex": r"deformation}  $(R,\mathcal{X})$",
    "kind": "font",
    "confidence": "medium",
    "fix": {"old": r"deformation}  $(R,\mathcal{X})$", "new": r"deformation}  $(R,\mathfrak{X})$"},
    "note": "As the previous entries.",
})

# ---------------- checks ----------------
ok = True
for e in F:
    path = os.path.join(FOLDER, "page_%03d.tex" % e["page"])
    with open(path, encoding="utf-8", newline="") as fh:
        text = fh.read()
    if e["fix"] is not None:
        n = text.count(e["fix"]["old"])
        if n != 1:
            ok = False
            print("FIX OLD COUNT", n, e["page"], e["fix"]["old"])
        if "%%%%%%%%%%" in e["fix"]["old"]:
            ok = False
            print("MARKER IN OLD", e["page"])
    if e["kind"] == "misprint_in_print" and not e["tex"].startswith("no "):
        if e["tex"] not in text:
            ok = False
            print("TEX NOT FOUND", e["page"], e["tex"])
    if e["kind"] != "misprint_in_print" and "corrected" in e:
        ok = False
        print("corrected on non-misprint", e["page"])

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

from collections import Counter
c = Counter((e["page"], e["kind"] == "misprint_in_print") for e in F)
for p in range(96, 101):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
print("checks ok" if ok else "CHECKS FAILED", len(F), "entries ->", OUT)
