import json, io
# "@@" stands for one backslash (avoids escape decoding in tool parameters)
BS = chr(92)
base = "C:/Users/user/Documents/sga_scan_check_20261105/run_7I"

def b(s):
    return None if s is None else s.replace("@@", BS)

F = []
F.append({
 "page": 386,
 "where": "end of the proof of 5.10, 'Or il est clair que X opère trivialement sur la fibre spéciale de X×_S S''",
 "scan": "Or il est clair que X opère trivialement",
 "tex": "Or il est clair que $X$ opère trivialement",
 "kind": "misprint_in_print",
 "confidence": "high",
 "fix": None,
 "corrected": "Or il est clair que $G$ opère trivialement",
 "note": "The typescript types X (the Barsotti-Tate group) where the acting group G is meant: G acts on X×_S S' by transport of structure, and the sentence continues 'donc il opère trivialement sur T_ℓ(A*o_o)'. The TeX keeps the printed reading."
})
F.append({
 "page": 386,
 "where": "Définition 5.12, 'un pro-ℓ-groupe de Barsotti-Tate sur le point générique'",
 "scan": "underline under 'un pro' and under '-groupe de Barsotti-Tate sur le point générique'; the hand-written ℓ is not underlined",
 "tex": "@@underline{un pro-$@@ell$-groupe de Barsotti-Tate sur le point générique}",
 "kind": "underline",
 "confidence": "medium",
 "fix": {"old": "@@underline{un pro-$@@ell$-groupe de Barsotti-Tate sur le point générique}",
         "new": "@@underline{un pro}-$@@ell$@@underline{-groupe de Barsotti-Tate sur le point générique}"},
 "note": "The typed underline stops after 'pro' and restarts after the ℓ. The replacement starts the second underline at the hyphen, in the file's $R$@@underline{-algebra} manner."
})
F.append({
 "page": 386,
 "where": "Définition 5.12, 'de X par des sous-groupes de Barsotti-Tate stricts (*)'",
 "scan": "'de' underlined, 'X' not underlined, 'par des sous-groupes de Barsotti-Tate stricts' underlined",
 "tex": "@@underline{de $X$ par des sous-groupes de Barsotti-Tate stricts}",
 "kind": "underline",
 "confidence": "high",
 "fix": {"old": "@@underline{de $X$ par des sous-groupes de Barsotti-Tate stricts}",
         "new": "@@underline{de} $X$ @@underline{par des sous-groupes de Barsotti-Tate stricts}"},
 "note": "The print breaks the underline at X, as at every other math letter of the definition."
})
F.append({
 "page": 387,
 "where": "end of Définition 5.12, '(resp. bonne réduction virtuelle, resp. bonne réduction virtuelle d'échelon n) sur le normalisé S' dans K''",
 "scan": "underline under 'bonne réduction virtuelle d'échelon' only; 'n)' not underlined",
 "tex": "@@underline{bonne réduction virtuelle d'échelon $n$)}",
 "kind": "underline",
 "confidence": "high",
 "fix": {"old": "@@underline{bonne réduction virtuelle d'échelon $n$)}",
         "new": "@@underline{bonne réduction virtuelle d'échelon} $n$)"},
 "note": "The TeX extends the underline over 'n)'; the print ends it after 'd'échelon'."
})
F.append({
 "page": 389,
 "where": "proof of 5.13 b), 'un sous-groupe ouvert π' de π = Gal(K̄/K̄)'",
 "scan": "π = Gal(K̄/K̄) (bar over both K)",
 "tex": "@@mathrm{Gal}(@@overline{K}/@@overline{K})",
 "kind": "misprint_in_print",
 "confidence": "high",
 "fix": None,
 "corrected": "@@mathrm{Gal}(@@overline{K}/K)",
 "note": "The print bars both K; π is Gal(K̄/K), as printed in the proof of 5.14 on p. 390. The TeX keeps the printed reading."
})
F.append({
 "page": 389,
 "where": "end of the proof of 5.13 c), 'et cela achève la démonstration'",
 "scan": "achève la démonstration (no full stop)",
 "tex": "et cela achève la démonstration",
 "kind": "misprint_in_print",
 "confidence": "high",
 "fix": None,
 "corrected": "et cela achève la démonstration.",
 "note": "The full stop that ends the proof is not typed; the next paragraph is Remarque 5.13.1. The TeX keeps the printed reading."
})
F.append({
 "page": 390,
 "where": "Proposition 5.14, 'Soient S un trait de corps de fonctions K'",
 "scan": "'Soient' underlined, 'S' not underlined, 'un trait de corps de fonctions' underlined",
 "tex": "@@underline{Soient $S$ un trait de corps de fonctions}",
 "kind": "underline",
 "confidence": "high",
 "fix": {"old": "@@underline{Soient $S$ un trait de corps de fonctions}",
         "new": "@@underline{Soient} $S$ @@underline{un trait de corps de fonctions}"},
 "note": "The TeX underlines S; the print does not."
})
F.append({
 "page": 390,
 "where": "Proposition 5.14 b), 'son image dans le groupe Z_ℓ des automorphismes de ∧^{2n} U_ℓ est d'indice fini'",
 "scan": "le groupe ℤ_ℓ des automorphismes (no star)",
 "tex": "$@@mathbb{Z}_@@ell$ @@underline{des automorphismes de}",
 "kind": "misprint_in_print",
 "confidence": "medium",
 "fix": None,
 "corrected": "$@@mathbb{Z}^*_@@ell$ @@underline{des automorphismes de}",
 "note": "The automorphism group of the rank-one module ∧^{2n}U_ℓ is ℤ_ℓ^*, as the proof on the same page prints it ('ℤ^*_ℓ ≃ Aut(∧^{2n} U_ℓ)'). No trace of a star shows on the scan here. The TeX keeps the printed reading."
})

for f in F:
    for k in ("tex", "corrected", "note"):
        if k in f:
            f[k] = b(f[k])
    if f["fix"]:
        f["fix"] = {"old": b(f["fix"]["old"]), "new": b(f["fix"]["new"])}
    assert "@@" not in json.dumps(f, ensure_ascii=False)

ok = True
for f in F:
    path = base + "/b386_390/page_%03d.tex" % f["page"]
    txt = io.open(path, encoding="utf-8", newline="").read()
    assert "\r" not in txt
    checks = []
    if f["fix"]:
        checks.append(("fix.old", f["fix"]["old"]))
        assert "%%%%%%%%%%" not in f["fix"]["old"]
    if f["kind"] == "misprint_in_print":
        checks.append(("tex", f["tex"]))
    for key, s in checks:
        n = txt.count(s)
        print(f["page"], key, n, s)
        if n != 1:
            ok = False

out = base + "/findings_386_390.json"
with io.open(out, "w", encoding="utf-8", newline="") as fh:
    fh.write(json.dumps(F, ensure_ascii=False, indent=1) + chr(10))
print("written", out, "items", len(F), "all unique:", ok)
