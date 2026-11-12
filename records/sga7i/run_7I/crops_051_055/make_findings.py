import json
import os

BASE = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I"
FOLDER = os.path.join(BASE, "b051_055")
OUT = os.path.join(BASE, "findings_051_055.json")

KEEP = " The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring."

F = []

def add(**kw):
    d = {
        "page": kw["page"],
        "where": kw["where"],
        "scan": kw["scan"],
        "tex": kw["tex"],
        "kind": kw["kind"],
        "confidence": kw["confidence"],
        "fix": kw.get("fix"),
    }
    if kw["kind"] == "misprint_in_print":
        d["corrected"] = kw["corrected"]
    d["note"] = kw["note"]
    F.append(d)

# ---------------- page 51 ----------------
add(page=51,
    where="Remark 2.2(d), 'We then obtain a functor ξ^# : h_R → A over C_Λ by sitting (R → S) ⟼ ξ(f)'",
    scan="by sitting",
    tex="by sitting",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected="by setting",
    note="Typing error for 'setting' (the functor is defined by f ⟼ ξ(f))." + KEEP)

add(page=51,
    where="Proposition 2.3, 'Let A --φ--> B --φ--> C be functors of cofibered groupoids over C_Λ'",
    scan="both arrows labelled φ (the same loop-and-stroke letter, clear in a crop)",
    tex=r"\underline{B} \xrightarrow{\ \varphi\ } \underline{C}",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"\underline{B} \xrightarrow{\ \psi\ } \underline{C}",
    note="The second functor is ψ: (a) 'If φ, ψ are both smooth, then so is ψ.φ', (b) 'If ψ.φ is smooth ... then ψ is smooth'." + KEEP)

# ---------------- page 52 ----------------
add(page=52,
    where="Remark 2.4, first line, 'Let A be a cofibered groupoids over C_Λ'",
    scan="a cofibered groupoids",
    tex="be a cofibered groupoids over",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected="be a cofibered groupoid over",
    note="Agreement slip after 'a'." + KEEP)

add(page=52,
    where="Remark 2.4, 'This means, by 2.2(d), that ξ̃ : h_R → A is smooth'",
    scan="ξ with a tilde struck over its top (ξ̃); the ξ of 'versal formal object ξ' and of 'R = P(ξ)' on the same lines has none",
    tex=r"$\xi : \underline{h}_R \to",
    kind="symbol", confidence="high",
    fix={"old": r"$\xi : \underline{h}_R \to", "new": r"$\tilde{\xi} : \underline{h}_R \to"},
    note="The functor h_R → A induced by ξ (written ξ^# in 2.2(d)) is printed ξ̃ in both places of Remark 2.4; the TeX drops the tilde. Apply together with the tilde fix on the arrow label below. \\tilde is already used in the file (\\tilde{f}, p. 37).")

add(page=52,
    where="Remark 2.4, '\"A is (formally) smooth over C_Λ (c.f. 1.13) i.e., R is a formal power-series algebra over Λ\"'",
    scan="(c.f. 1.13)",
    tex="(c.f. 1.13)",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected="(c.f. 1.14)",
    note="'(formally) smooth over C_Λ' is defined in Remark 1.14 (p. 44), which also announces this equivalence ('It turns out (cf. 2.4) that ...'); Remark 1.13 is about [A] and minimally versal objects. Wrong reference number." + KEEP)

add(page=52,
    where="Remark 2.4, 'the composite functor h_R --ξ̃--> A --P--> C_Λ (= h_Λ) is smooth'",
    scan="label of the first arrow: ξ with the same tilde over its top",
    tex=r"\xrightarrow{\ \xi\ }",
    kind="symbol", confidence="high",
    fix={"old": r"\xrightarrow{\ \xi\ }", "new": r"\xrightarrow{\ \tilde{\xi}\ }"},
    note="Same ξ̃ as in 'that ξ̃ : h_R → A' two lines up; apply both tilde fixes together.")

add(page=52,
    where="Definition 2.5, display 'P(a' × b') = P(a') ×_{P(a)} P(b') .'",
    scan="P(a' ×b') : nothing under the first × (the second × has P(a) under it)",
    tex=r"P(a' \times b')",
    kind="misprint_in_print", confidence="low", fix=None,
    corrected=r"P(a' \underset{a}{\times} b')",
    note="Low: the fibre product is the a' ×_a b' named in the line above; the display drops its index. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.")

# ---------------- page 53 ----------------
add(page=53,
    where="Last display, semi-homogeneity criterion '[A(R ×_R R_2)] → [A(R_1) ×^2_{A(R)} A(R_2)]'",
    scan="[A(R ×_R R_2)] : the first R has no subscript 1 (no trace of one in a crop)",
    tex=r"[\underline{A}(R \times_R R_2)]",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"[\underline{A}(R_1 \times_R R_2)]",
    note="It is the map A(R_1 ×_R R_2) → A(R_1) ×^2_{A(R)} A(R_2) of the two preceding formulas, on isomorphism classes; p. 54 goes on 'is surjective whenever R_1 → R is surjective'. R ×_R R_2 would be just R_2." + KEEP)

# ---------------- page 54 ----------------
add(page=54,
    where="'For each map R' → R in C , φ induces a functor ...'",
    scan="in C , : underlined C without the subscript Λ (C_Λ has it three words earlier)",
    tex=r"in  $\underline{C}$  ,",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"in  $\underline{C}_\wedge$  ,",
    note="φ : A → B is a functor of cofibered groupoids over C_Λ (same sentence), so R' → R is a map of C_Λ; the bare C is the general base category of § 1. Lambda written \\wedge as elsewhere in the file." + KEEP)

add(page=54,
    where="'φ is smooth if and only if the functor A(R') → A(R) ×^2_{B(R)} B(R') is surjective on isomorphism classes'",
    scan="first A(R') without underline (A(R), B(R') and B(R) of the same formula are underlined)",
    tex=r"the functor $A(R') \to",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"the functor $\underline{A}(R') \to",
    note="Category letter without its underline (the same functor three lines up has A(R') underlined)." + KEEP)

add(page=54,
    where="Remark 2.6(c), 'the functor A(k[V × W]) → A(k[V]) × A(k[W])'",
    scan="first A without underline (the two A's on the right are underlined)",
    tex=r"$A(k[V \times W])",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"$\underline{A}(k[V \times W])",
    note="Category letter without its underline (the display below has A(k[V×W]) underlined)." + KEEP)

# ---------------- page 55 ----------------
add(page=55,
    where="Proof of 2.7, (i) ⇒ (ii), 'Since [A(R' ×_R R')] → [A(R')] ×_{[A(R)]} [A(R')] is bijective'",
    scan="[A(R' ×_R R')] : the first A without underline (the three other A's of the formula are underlined)",
    tex=r"[A(R' \times_{R} R')]",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"[\underline{A}(R' \times_{R} R')]",
    note="Category letter without its underline (cf. the same map in 2.7 (i))." + KEEP)

add(page=55,
    where="Diagram of (ii) ⇒ (i), arrow a'_1 → a'_2",
    scan="the tilde ~ is typed BELOW the leftward arrow a'_2 <—— a'_1",
    tex="\\arrow[l, \"\\sim\"']",
    kind="other", confidence="low",
    fix={"old": "\\arrow[l, \"\\sim\"']", "new": "\\arrow[l, \"\\sim\"]"},
    note="For a leftward arrow the swap mark ' puts the label above the shaft; without it tikz-cd sets it below, as printed (the file's own comment block also records the tilde BELOW the shaft).")

add(page=55,
    where="After the diagram, 'where τ̄ ; a_1 → a_2 is the induced isomorphism from τ'",
    scan="τ̄ ; a_1 : a semicolon after τ̄",
    tex=r"$\bar{\tau}$ ;",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"$\bar{\tau}$ :",
    note="Shift slip on the ;/: key (as 'i ; V' on p. 47)." + KEEP)

# ---------------- checks ----------------
ok = True
for d in F:
    path = os.path.join(FOLDER, "page_%03d.tex" % d["page"])
    with open(path, encoding="utf-8", newline="") as fh:
        txt = fh.read()
    if d["tex"] not in txt:
        print("TEX NOT FOUND", d["page"], repr(d["tex"]))
        ok = False
    if d["fix"]:
        n = txt.count(d["fix"]["old"])
        if n != 1:
            print("OLD COUNT", n, d["page"], repr(d["fix"]["old"]))
            ok = False
        if "%%%%%%%%%%" in d["fix"]["old"]:
            print("OLD TOUCHES MARKER", d["page"])
            ok = False
    if d["kind"] == "misprint_in_print" and d["fix"] is None:
        # corrected must differ from tex
        if d["corrected"] == d["tex"]:
            print("CORRECTED == TEX", d["page"])
            ok = False

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

# re-read and summarise
with open(OUT, encoding="utf-8") as fh:
    back = json.load(fh)
from collections import Counter
cnt = Counter()
for d in back:
    cnt[(d["page"], d["kind"] == "misprint_in_print")] += 1
for p in range(51, 56):
    print(p, "normal", cnt[(p, False)], "misprint", cnt[(p, True)])
print("OK" if ok else "PROBLEMS", len(back), "findings")
