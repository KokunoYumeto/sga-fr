import json
import sys

OUT = sys.argv[1]

F = []


def add(**kw):
    F.append(kw)


# ---------------- page 426 ----------------
add(page=426,
    where="after (4.6.9): 'Que c' une base'",
    scan="Que c'    une base \"orthonormale\" (a blank of about three letters after c')",
    tex="Que c' une base \\og orthonormale\\fg{}",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected="Que c'est une base",
    note="The typescript leaves a blank where 'est' belongs. The TeX keeps the printed reading.")

add(page=426,
    where="(4.6.11)",
    scan="bold R_B = le 𝒪-sous-module de ... (a heavy bold R)",
    tex="R_B=\\text{le $\\mathcal O$-sous-module de",
    kind="font", confidence="medium",
    fix={"old": "R_B=\\text{le", "new": "\\mathbf R_B=\\text{le"},
    note="Only this defining R is typed bold; the later R_B ((4.6.12)-(4.6.19)) have the plain typewriter R.")

add(page=426,
    where="end of (4.6.11) and the next sentence",
    scan="the text of (4.6.11) runs on to the next line: 'd'ordinal ≥ 0. Pour démontrer le lemme, il suffit de démontrer' on one line",
    tex="d'ordinal $\\geq0$}.\n\\end{equation}\n\nPour démontrer le lemme",
    kind="other", confidence="low",
    fix={"old": "\\end{equation}\n\nPour démontrer", "new": "\\end{equation}\nPour démontrer"},
    note="'Pour démontrer ...' continues the paragraph in the print; the TeX's blank line starts a new one.")

# ---------------- page 427 ----------------
add(page=427,
    where="(4.6.19), first row",
    scan="Ψ_p(π^{U_o} X^{U_o} ... X_{n+2}^{U_{n+2}}) = 0: the first X has no index o",
    tex="\\psi_p\\!\\left(\\pi^{U_0}X^{U_0}\\cdots X_{n+2}^{U_{n+2}}\\right)=0,",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected="X_0^{U_0}",
    note="The print drops the index of the first X (the second row has X_o^{pU_o}). The TeX keeps the printed reading.")

# ---------------- page 428 ----------------
add(page=428,
    where="heading of section 5",
    scan="5. Un théorème d'AX [1], (cf. aussi [4], section 7). with 'Un théorème d'AX' underlined",
    tex="\\section*{5. Un théorème d'AX [1], (cf. aussi [4], section 7).}",
    kind="underline", confidence="high",
    fix={"old": "\\section*{5. Un théorème d'AX [1]",
         "new": "\\section*{5. \\underline{Un théorème d'AX} [1]"},
    note="Sections 1-4 of this exposé are plain lines '1. \\underline{...}' without \\section* (which sets the "
         "heading in bold). The heading of section 6 (p. 431) is also underlined in the print and is also a "
         "\\section* without underline.")

add(page=428,
    where="Théorème 5.0.bis, number of the display jd<n+2",
    scan="(5.0.7)",
    tex="\\tag{5.0.7}",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected="\\tag{5.0.4}",
    note="The numbers run (5.0.3), (5.0.7), (5.0.5): (5.0.4) is missing and (5.0.7) is used again on p. 429. "
         "The TeX keeps the printed number. Goes with the reference (5.0.4) -> (5.0.5) on p. 429.")

# ---------------- page 429 ----------------
add(page=429,
    where="Démonstration, second sentence",
    scan="Les assertions (5.0.4) et (5.0.2) sont équivalentes",
    tex="Les assertions (5.0.4) et (5.0.2)",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected="(5.0.5)",
    note="(5.0.7)-(5.0.9) show the equivalence of the affine statement (5.0.5) with (5.0.2); (5.0.4) would be the "
         "hypothesis jd<n+2 (printed (5.0.7) on p. 428). The TeX keeps the printed reference.")

add(page=429,
    where="(5.0.8) and (5.0.9)",
    scan="Z(t,V_aff/𝔽_q) = Z(t,V/𝔽_q) / (Z(qt,V/𝔽_q)(1-t)) ;  Z(t,V/𝔽_q) = ∏_{i≥0} [(1-q^i f) Z(q^i t,V_aff/𝔽_q)]",
    tex="=\\frac{Z(t,V/\\mathbb F_q)}{Z(qt,V/\\mathbb F_q)(1-t)} ;  "
        "=\\prod_{i\\geq0}\\left[(1-q^if)Z(q^it,V_{\\mathrm{aff}}/\\mathbb F_q)\\right].",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected="(5.0.8): \\frac{Z(qt,V/\\mathbb F_q)}{Z(t,V/\\mathbb F_q)(1-t)} ;  "
              "(5.0.9): \\prod_{i\\geq0}\\left[(1-q^it)Z(q^it,V_{\\mathrm{aff}}/\\mathbb F_q)\\right]^{-1}",
    note="An error of substance in the print, not a misreading: by (5.0.7), log Z(t,V_aff) = log Z(qt,V) - "
         "log Z(t,V) - log(1-t), so (5.0.8) has Z(t,V) and Z(qt,V) interchanged, and (5.0.9), derived from it, "
         "is the reciprocal of the right product. Check: V a point of P^1, V_aff = A^1: Z(t,V_aff) = 1/(1-qt), "
         "while the printed right side of (5.0.8) gives (1-qt)/(1-t)^2. Harmless for the proof (1+q^jtZ[[q^jt]] "
         "is a multiplicative group). Corrected edition: both formulas or neither, or an editorial note; the TeX "
         "follows the print. Independent of the misprint f for t in (5.0.9).")

add(page=429,
    where="(5.0.9)",
    scan="(1-q^i f)",
    tex="(1-q^if)",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected="(1-q^it)",
    note="'f' is a slip for 't'. The TeX keeps the printed reading.")

add(page=429,
    where="(5.0.12)",
    scan="Λ_B(t) ∈ F^{j+card(B)-(n+2)} . (capital Lambda: two strokes, no base)",
    tex="\\Delta_B(t)\\in F^{j+\\operatorname{card}(B)-(n+2)}.",
    kind="misprint_in_print", confidence="medium",
    fix={"old": "\\Delta_B(t)", "new": "\\Lambda_B(t)"},
    corrected="\\Delta_B(t)",
    note="The series is Δ_B of 4.5-4.6; the TeX silently corrects. The six Δ_B of pp. 424-425 (the display "
         "before (4.5.28), (4.5.28), (4.5.23), the 4.6 text, Lemme 4.6.6, (4.6.8)) are printed as a true Δ with "
         "its base (checked on the scans), so only this one is a Λ (global item 64: no all-or-none question).")

add(page=429,
    where="before (5.0.13)",
    scan="en appliquant le lemme (4.4.6),",
    tex="en appliquant le lemme (4.4.6), une",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected="(4.6.6)",
    note="(4.4.6) is the formula for (q^ν-1) Card V^*(𝔽_{q^ν}) (p. 419); the lemma applied, with "
         "j+card(B)-(n+2) for j, is Lemme 4.6.6 (p. 425), which p. 431 cites as (4.6.6). The TeX keeps the printed "
         "reference.")

# ---------------- page 430 ----------------
add(page=430,
    where="Remarque 5.1, before (5.1.2)",
    scan="Posons, comme dans XI 2.1, pour a+b = n (no comma)",
    tex="pour $a+b=n$,",
    kind="punctuation", confidence="high",
    fix={"old": "pour $a+b=n$,", "new": "pour $a+b=n$"},
    note="The TeX adds a comma.")

add(page=430,
    where="(5.1.3)",
    scan="E^{a,b}(V) = Coker (H^b(ℙ^{n+1}, Ω^a_{ℙ^{n+1}}) ↪ H^b(V,Ω^a_V)  . (the parenthesis opened after Coker is never closed)",
    tex="\\operatorname{Coker}\\!\\left(...\\hookrightarrow H^b(V,\\underline{\\Omega}_V^a)\\right..",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected="\\right).",
    note="The TeX keeps the printed reading (\\right. leaves the parenthesis open).")

with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    json.dump(F, f, ensure_ascii=False, indent=1)
    f.write("\n")
print(len(F), "findings written to", OUT)
