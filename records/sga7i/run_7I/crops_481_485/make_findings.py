# Helper for the 481-485 recheck: writes the findings JSON and checks it.
# The character ¤ stands for a backslash, so no escape decoding can touch the LaTeX.
import json, sys, os

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BATCH = os.path.join(RUN, "b481_485")
OUT = os.path.join(RUN, "findings_481_485_recheck.json")

def b(s):
    return None if s is None else s.replace("¤", "\\")

F = []
def add(page, where, scan, tex, kind, conf, fix, corrected, note):
    d = {"page": page, "where": where, "scan": scan, "tex": b(tex), "kind": kind,
         "confidence": conf,
         "fix": None if fix is None else {"old": b(fix[0]), "new": b(fix[1])}}
    if corrected is not None:
        d["corrected"] = b(corrected)
    d["note"] = note
    F.append(d)

add(481, "unnumbered display after 'est à valeurs dans un groupe'",
    "(𝔾_m(U)/𝔾_m(S̲) ⊗_ℤ ℤ_ℓ — the opening parenthesis is never closed",
    "(¤mathbb{G}_m(U)/¤mathbb{G}_m(¤underline{S}) ¤otimes_{¤mathbb{Z}} ¤mathbb{Z}_¤ell",
    "misprint_in_print", "high", None,
    "(¤mathbb{G}_m(U)/¤mathbb{G}_m(¤underline{S})) ¤otimes_{¤mathbb{Z}} ¤mathbb{Z}_¤ell",
    "Unbalanced parenthesis in the print. The TeX keeps the printed reading.")

add(481, "'est le composé de u_ℓ avec l'homomorphisme ℤ_ℓ^L → ℤ_ℓ'",
    "u_ℓ with no underline (the u̲_ℓ of (12.8.11) just above is clearly underlined)",
    "est le composé de $u_¤ell$ avec",
    "misprint_in_print", "medium", None,
    "est le composé de $¤underline{u}_¤ell$ avec",
    "Only the pairing u̲_ℓ of (12.8.11) takes values in ℤ_ℓ^L, so the composite is u̲_ℓ followed by ℤ_ℓ^L → ℤ_ℓ; as printed, u_ℓ is said to be the composite of u_ℓ. The TeX keeps the printed reading.")

add(481, "'par tensorisation avec Z_ℓ sur ℤ'",
    "plain typed Z_ℓ (the ℤ after 'sur' and every other ℤ_ℓ on the page are double-struck)",
    "tensorisation avec $Z_¤ell$ sur",
    "misprint_in_print", "medium", None,
    "tensorisation avec $¤mathbb{Z}_¤ell$ sur",
    "The typist left out the double stroke. The TeX keeps the printed reading.")

add(482, "'on a d_λ=1 si et seulement si x est régulier au point x_λ'",
    "x in lower case (x-height, like the following 'est')",
    "si et seulement si $x$ est",
    "misprint_in_print", "high", None,
    "si et seulement si $X$ est",
    "It is the scheme X that is regular at x_λ (next sentence: 'on a supposé X régulier, i.e. les d_λ égaux à 1'). The TeX keeps the printed lower-case x.")

add(482, "'considérons le localisé strict complété S̲^λ de S̲ en le point maximal de D'",
    "D, no index λ",
    "en le point maximal de $D$, et",
    "misprint_in_print", "medium", None,
    "en le point maximal de $D_¤lambda$, et",
    "D = ∪ D_λ has one maximal point for each λ; S̲^λ is the localization at the maximal point of D_λ (cf. a): 'au point maximal s_λ de D_λ'). The TeX keeps the printed reading.")

add(482, "'et X̲^λ = X ×_S S̲^λ. Alors la fibre'",
    "X̲^λ = X×_S S̲^λ: neither the X nor the subscript S is underlined; only the last S carries an underline",
    "X ¤times_{¤underline{S}} ¤underline{S}^¤lambda",
    "misprint_in_print", "high",
    ("X ¤times_{¤underline{S}} ¤underline{S}^¤lambda", "X ¤times_{S} ¤underline{S}^¤lambda"),
    "¤underline{X} ¤times_{¤underline{S}} ¤underline{S}^¤lambda",
    "X̲^λ is the base change of f̲ : X̲ → S̲ (12.8.2) to S̲^λ, so the correct reading is X̲ ×_S̲ S̲^λ. The TeX silently underlines the subscript S (the fix restores the print) and keeps the printed plain X. In a) on the same page, P ×_S̲ D_λ, the print does underline the subscript S.")

add(482, "'Alors la fibre spéciale X_o^λ n'a qu'un seul point singulier'",
    "X_o^λ, the X not underlined",
    "la fibre spéciale $X_o^¤lambda$",
    "misprint_in_print", "medium", None,
    "la fibre spéciale $¤underline{X}_o^¤lambda$",
    "The special fibre of X̲^λ; the next page prints it X̲^λ_o ('en le point y_λ de X̲^λ_o'). The TeX keeps the printed reading.")

add(483, "diagram (12.8.15), label of the arrow M^λ → ℤ",
    "φ_{λ_λ}: a hand-drawn λ in place of the y",
    "¤varphi_{¤lambda_{¤lambda}}",
    "misprint_in_print", "high", None,
    "¤varphi_{y_{¤lambda}}",
    "The form on M^λ is φ_{y_λ}, introduced just above the diagram. The TeX keeps the printed reading.")

add(484, "'Or S̲ est un trait de caractéristique nulle'",
    "S̲ without the superscript λ (the preceding 'sur S̲^λ' has it)",
    "Or $¤underline{S}$ est un trait",
    "misprint_in_print", "medium", None,
    "Or $¤underline{S}^{¤lambda}$ est un trait",
    "S̲ carries the divisors D_λ (ℤ^L ≃ 𝔾_m(U)/𝔾_m(S̲), 12.8.10), so it is not a trait; the trait of characteristic zero over which 12.5 is applied is S̲^λ. The TeX keeps the printed reading.")

add(484, "Remarques 12.9, 'ces cas correspondants respectivement à rang M = 1'",
    "correspondants",
    "ces cas correspondants respectivement",
    "misprint_in_print", "low", None,
    "ces cas correspondant respectivement",
    "Present participle with a complement, normally invariable; a grammatical slip rather than a typing error. The TeX keeps the printed reading.")

add(484, "12.10, 'les accouplements de monodormie'",
    "monodormie",
    "accouplements de monodormie",
    "misprint_in_print", "high", None,
    "accouplements de monodromie",
    "Typing error in the print. The TeX keeps the printed reading.")

# ---- checks ----
ok = True
for d in F:
    with open(os.path.join(BATCH, "page_%d.tex" % d["page"]), encoding="utf-8", newline="") as fh:
        t = fh.read()
    n_tex = t.count(d["tex"])
    if n_tex != 1:
        ok = False
        print("TEX COUNT", d["page"], n_tex, repr(d["tex"]))
    if d["fix"] is not None:
        n_old = t.count(d["fix"]["old"])
        if n_old != 1:
            ok = False
            print("OLD COUNT", d["page"], n_old, repr(d["fix"]["old"]))
        if "%%%%%%%%%%" in d["fix"]["old"] or "%%%%%%%%%%" in d["fix"]["new"]:
            ok = False
            print("MARKER IN FIX", d["page"])
    if any(c in (d["tex"] + (d.get("corrected") or "")) for c in "\t\r\f\v\b"):
        ok = False
        print("CONTROL CHAR", d["page"], repr(d["tex"]))

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

from collections import Counter
c = Counter((d["page"], d["kind"] == "misprint_in_print") for d in F)
for p in range(481, 486):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
print("ALL CHECKS OK" if ok else "CHECKS FAILED")
