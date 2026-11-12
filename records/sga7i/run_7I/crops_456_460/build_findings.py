import json
import sys

out_path = sys.argv[1]
page_dir = sys.argv[2]

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
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)

# ---------------- page 456
add(456,
    "paragraph after (11.6.2): 'comme Φ_o(ℓ), est fini'",
    "comme Φ_o(ℓ), est fini, et M_ℓ et M̌'_ℓ ont même rang",
    "comme $\\Phi_o(\\ell)$, est fini",
    "misprint_in_print", "medium", None,
    "Stray comma between subject and verb in the print. The TeX keeps the printed reading.",
    corrected="comme $\\Phi_o(\\ell)$ est fini")

add(456,
    "unnumbered display after 'd'indice fini dans M̌'_ℓ :'",
    "Φ(ℓ) = V/M_ℓ , Φ'(ℓ) = V/M̌'_ℓ ,",
    "\\Phi(\\ell) = V/M_{\\ell} \\quad , \\quad \\Phi'(\\ell) = V/\\check{M}'_{\\ell}",
    "misprint_in_print", "low", None,
    "The display justifies (11.6.3) coker ũ_ℓ ≃ ker(ũ_ℓ⊗D_ℓ): with V = M_ℓ⊗Q_ℓ one has M_ℓ⊗D_ℓ = V/M_ℓ and "
    "M̌'_ℓ⊗D_ℓ = V/M̌'_ℓ, and the kernel of V/M_ℓ → V/M̌'_ℓ is M̌'_ℓ/M_ℓ = Φ(ℓ). As printed, the finite group Φ(ℓ) "
    "is equated with the divisible group V/M_ℓ, and Φ'(ℓ) plays no role here. Author's slip; the corrected "
    "left-hand sides are reconstructed from the argument. The TeX keeps the printed reading.",
    corrected="M_{\\ell}\\otimes D_{\\ell} = V/M_{\\ell} \\quad , \\quad \\check{M}'_{\\ell}\\otimes D_{\\ell} = V/\\check{M}'_{\\ell}")

# ---------------- page 457
add(457,
    "first line",
    "définir l'isomorphisme canonique (11.6,2).  (comma for the second dot)",
    "canonique (11.6,2).",
    "misprint_in_print", "high", None,
    "Wrong separator in the formula number. The TeX keeps the printed reading.",
    corrected="canonique (11.6.2).")

add(457,
    "'Ecrivant M_ℓ⊗D_ℓ (resp. M̌_ℓ⊗D_ℓ)'",
    "(resp. M̌_ℓ⊗D_ℓ): M with check, no prime",
    "(resp. $\\check{M}_\\ell \\otimes D_\\ell$)",
    "misprint_in_print", "medium", None,
    "Must be M̌'_ℓ⊗D_ℓ, the target of ũ_ℓ⊗D_ℓ in (11.6.2), whose finite levels are the M̌'_n named in the same "
    "sentence. The TeX keeps the printed reading.",
    corrected="(resp. $\\check{M}'_\\ell \\otimes D_\\ell$)")

add(457,
    "'il revient au même de définir (11.6.2), où des isomorphismes canoniques'",
    "(11.6.2), où des isomorphismes canoniques  (grave accent printed)",
    "(11.6.2), où des isomorphismes",
    "misprint_in_print", "medium", None,
    "'où' is printed for 'ou' (or): defining (11.6.2) amounts to defining the compatible isomorphisms (11.6.4). "
    "The TeX keeps the printed reading.",
    corrected="(11.6.2), ou des isomorphismes")

add(457,
    "line after (11.6.4)",
    "comptatibles avec les morphismes de transition évidents",
    "comptatibles",
    "misprint_in_print", "high", None,
    "Typing error. The TeX keeps the printed reading.",
    corrected="compatibles")

# ---------------- page 458
add(458,
    "proof of Lemme 11.6.8: 'et comme _nΨ donc ce noyau est séparé'",
    "et comme _nΨ donc ce noyau est séparé, et sa fibre générique ...",
    "et comme ${}_n\\Psi$ donc ce noyau est séparé",
    "misprint_in_print", "medium", None,
    "Words are missing after _nΨ: the kernel is separated because _nΨ is separated (stated after (11.6.6) on p. 457). "
    "The corrected reading inserts only the missing words and keeps the printed 'donc'; its exact wording is "
    "conjectural. The TeX keeps the printed reading.",
    corrected="et comme ${}_n\\Psi$ est séparé, donc ce noyau est séparé")

# ---------------- page 460
add(460,
    "paragraph after (11.6.14): 'fibre générique de (11.7.5)'",
    "fibre générique de (11.7.5), où on pose",
    "fibre générique de (11.7.5)",
    "misprint_in_print", "high", None,
    "Exposé IX has no (11.7.5): 11.7 is the following 'Remarques' paragraph (p. 461), which speaks of "
    "'l'extension panachée (11.6.5)' and of X_nη = (_nA_K). X_nη is the generic fibre of the filtration (11.6.5) "
    "of _nA, with F_n = (_nA^o)^f. The same stale number recurs on p. 461 ('La construction faite dans 11.7'). "
    "The TeX keeps the printed reading.",
    corrected="fibre générique de (11.6.5)")

add(460,
    "(11.6.15), first term",
    "E_n = D(F_n) ,  (no prime on F), followed by 0 → R_n → E_n → M_n → 0 with R_n ≀ D(R'_n)",
    "E_n = D(F_n) \\; ,",
    "misprint_in_print", "medium", None,
    "D(F_n) is an extension of M'_n by D(R_n) = R'_n. The sequence printed beside it (sub-object R_n ≃ D(R'_n), "
    "quotient M_n) requires E_n = D(F'_n), as in (9.6.1): E = D(F') = D(T_ℓ(A'^o)^f). The TeX and its STRUCTURE "
    "comment keep the printed reading.",
    corrected="E_n = D(F'_n) \\; ,")

add(460,
    "'où Ē_n est le sous-groupe extension de K_n par R_n qu'on devine'",
    "extension de K_n par R_n  (no prime on K)",
    "extension de $K_n$ par $R_n$",
    "misprint_in_print", "medium", None,
    "Ē_n is the inverse image in E_n of the variable subgroup K'_n; p. 461 then specialises 'en y prenant "
    "K'_n = K_n'. The index should carry the prime. The TeX keeps the printed reading.",
    corrected="extension de $K'_n$ par $R_n$")

# ---------------- checks
ok = True
for d in F:
    path = f"{page_dir}/page_{d['page']}.tex"
    with open(path, encoding="utf-8", newline="") as fh:
        text = fh.read()
    n_tex = text.count(d["tex"])
    if n_tex != 1:
        ok = False
        print("TEX COUNT", d["page"], n_tex, repr(d["tex"]))
    if d["fix"] is not None:
        n_old = text.count(d["fix"]["old"])
        if n_old != 1:
            ok = False
            print("OLD COUNT", d["page"], n_old, repr(d["fix"]["old"]))

with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0])
    c[1 if d["kind"] == "misprint_in_print" else 0] += 1
print("all substrings unique:", ok)
print(counts)
