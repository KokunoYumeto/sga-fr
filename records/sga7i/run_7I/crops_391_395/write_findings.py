import json, os

BS = chr(92)


def L(s):
    # the paragraph sign stands for a backslash, so that no backslash passes through tool parameters
    return s.replace("§", BS)


base = os.path.join("C:" + BS, "Users", "user", "Documents", "sga_scan_check_20261105", "run_7I")
batch = os.path.join(base, "b391_395")
out = os.path.join(base, "findings_391_395.json")

F = []
F.append({
    "page": 391,
    "where": "proof of 5.14, '(puisque l'hypothèse (iii) est conservée en remplaçant K par une extension séparable finie K', i.e. I par un sous-groupe ouvert I' (   ). Lorsque ...'",
    "scan": "(puisque l'hypothèse (iii) est conservée ... un sous-groupe ouvert I' (      ). Lorsque",
    "tex": L("$I'$ (§quad§quad ). Lorsque"),
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": L("$I'$ (§quad§quad )). Lorsque"),
    "note": "The parenthesis opened at '(puisque' is never closed: the only ')' closes the empty reference '(   )'. The TeX keeps the printed reading.",
})
F.append({
    "page": 391,
    "where": "Corollaire 5.15, '(U_{ℓQ_ℓ})^f dfn= (U_ℓ^f)_{Q_ℓ}'",
    "scan": "'dfn' over two long bars that form the equals sign; no third line",
    "tex": L("§stackrel{§underline{§mathrm{dfn}}}{=}"),
    "kind": "underline",
    "confidence": "low",
    "fix": {"old": L("§stackrel{§underline{§mathrm{dfn}}}{=}"), "new": L("§stackrel{§mathrm{dfn}}{=}")},
    "note": L("Both bars are as long as 'dfn' and wider apart than the bars of a typed '=' (cf. 'U_ℓ = U_ℓ^f' in the next paragraph): they are the equals sign, typed as a double underscore. The §underline adds a third line. Elsewhere the file writes §stackrel{§mathrm{dfn}}{=}."),
})
F.append({
    "page": 392,
    "where": "6.1, 'mais au lieu de relever le tore maximal de T_o de A_o tout entier'",
    "scan": "le tore maximal de T_o de A_o tout entier",
    "tex": "le tore maximal de $T_o$ de $A_o$",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": "le tore maximal $T_o$ de $A_o$",
    "note": "T_o is itself the maximal torus of A_o (lifted as a whole in 5.1; the sentence goes on 'à relever le sous-groupe _{p^ν}T_o'); the first 'de' is a typing slip. The TeX keeps the printed reading.",
})
F.append({
    "page": 394,
    "where": "6.2, 'Dans le cas semi-stable, où on a A_o-bar = A_o^o, la question se résoud par l'affirmative'",
    "scan": "la question se résoud par l'affirmative",
    "tex": "la question se résout par l'affirmative",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": {"old": "se résout", "new": "se résoud"},
    "corrected": "se résout",
    "note": "The typescript spells 'résoud'; the TeX silently corrects it to 'résout'. The fix restores the printed reading.",
})
F.append({
    "page": 395,
    "where": "6.2.2, 'et A_K = ∏_{K'/K} A'_{K'}/K' est simple sur K''",
    "scan": "est simple sur K'. Or prenons",
    "tex": "est simple sur $K'$. Or prenons",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "est simple sur $K$. Or prenons",
    "note": "A_K is an abelian variety over K, and the next sentences treat 'A_K simple sur K' ('dire que A_K est simple sur K signifie ...', 'la condition que A_K soit simple sur K'); over K' it is isogenous to a product of two elliptic curves. The TeX keeps the printed reading.",
})
F.append({
    "page": 395,
    "where": "6.2.2, 'qui sera donc nécessairement une isogénie, i.e, la condition que A_K soit simple sur K'",
    "scan": "une isogénie, i.e, la condition",
    "tex": "une isogénie, i.e, la condition",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": "une isogénie, i.e. la condition",
    "note": "The second full stop of 'i.e.' is typed as a comma. The TeX keeps the printed reading.",
})

ok = True
for f in F:
    path = os.path.join(batch, "page_%03d.tex" % f["page"])
    with open(path, encoding="utf-8", newline="") as fh:
        txt = fh.read()
    if "\r" in txt:
        print("CR found in", path)
    if f["fix"] is not None:
        n = txt.count(f["fix"]["old"])
        print(f["page"], "fix old count:", n, f["fix"]["old"])
        if n != 1:
            ok = False
    n2 = txt.count(f["tex"])
    print(f["page"], "tex count:", n2, f["tex"])
    if n2 < 1:
        ok = False
    for k, v in f.items():
        if isinstance(v, str) and any(ord(c) < 32 for c in v):
            print("control char in", k, repr(v))
            ok = False
print("ALL OK" if ok else "PROBLEM")
with open(out, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write("\n")
print("wrote", out, len(F))
