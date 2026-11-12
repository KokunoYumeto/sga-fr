import json, io

base = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II"
out = base + r"\findings_376_380_recheck.json"

BS = "\\"

def t(s):
    # write backslashes as '@' in the source to avoid escape problems
    return s.replace("@", BS)

findings = [
 {
  "page": 376,
  "where": "first sentence, before (1.4.7)",
  "scan": "de trouver une H défini sur 𝔽_q, de degré d, ... et tel que",
  "tex": t("de trouver une $H$ défini sur $@mathbb{F}_q$"),
  "kind": "misprint_in_print",
  "confidence": "medium",
  "fix": None,
  "corrected": t("un $H$ défini"),
  "note": "Gender slip in the print: H is masculine in this passage ('défini', 'tel que'; then 'un H', 'Un tel H'). The TeX keeps the printed reading."
 },
 {
  "page": 376,
  "where": "(1.4.8)",
  "scan": "H(α_1,.,α_N) = 0 — comma, a single full stop, comma (the other two ellipses of the line, α_1,...,α_N and α_1=...=α_N, have three dots)",
  "tex": t("H(@alpha_1,@dots,@alpha_N) = 0"),
  "kind": "misprint_in_print",
  "confidence": "high",
  "fix": {"old": t("H(@alpha_1,@dots,@alpha_N) = 0"), "new": t("H(@alpha_1,.,@alpha_N) = 0")},
  "corrected": t("H(@alpha_1,@dots,@alpha_N) = 0"),
  "note": t("The typist typed a one-dot ellipsis in the argument of H. The TeX silently corrects it to @dots; the fix restores the printed reading.")
 },
 {
  "page": 377,
  "where": "2.0, 'sur lesquels opère le groupe de Galois ...'",
  "scan": "le groupe de Galois Gal(/𝔽_q) de 𝔽_q",
  "tex": t("le groupe de Galois $@mathrm{Gal}(/@mathbb{F}_q)$ de $@mathbb{F}_q$"),
  "kind": "misprint_in_print",
  "confidence": "high",
  "fix": None,
  "corrected": t("$@mathrm{Gal}(@overline{@mathbb{F}}_q/@mathbb{F}_q)$"),
  "note": "The print omits 𝔽̄_q before the slash. The TeX keeps the printed reading."
 },
 {
  "page": 377,
  "where": "(2.0.2)",
  "scan": "φ_q ∈ Gal(/𝔽_q) l'automorphisme de Frobenius .",
  "tex": t("@varphi_q @in @mathrm{Gal}(/@mathbb{F}_q)"),
  "kind": "misprint_in_print",
  "confidence": "high",
  "fix": None,
  "corrected": t("@varphi_q @in @mathrm{Gal}(@overline{@mathbb{F}}_q/@mathbb{F}_q)"),
  "note": "Same omission of 𝔽̄_q in the print. The TeX keeps the printed reading."
 },
 {
  "page": 377,
  "where": "sentence before (2.0.3)",
  "scan": "la fonction zêta de X (XXII 3.0.1) est donné par la formule",
  "tex": "est donné par la formule",
  "kind": "misprint_in_print",
  "confidence": "medium",
  "fix": None,
  "corrected": "est donnée par la formule",
  "note": "Agreement slip in the print (the subject is 'la fonction zêta'). The TeX keeps the printed reading."
 },
 {
  "page": 378,
  "where": "Corollaire 2.2, '(notations de XX 2.0.6)'",
  "scan": "(notations de XX 2.0.6) — the underline starts under the 'n' of 'notations'; the opening parenthesis is not underlined",
  "tex": t("@underline{(notations de} XX 2.0.6)"),
  "kind": "underline",
  "confidence": "high",
  "fix": {"old": t("@underline{(notations de}"), "new": t("(@underline{notations de}")},
  "note": t("Move the opening parenthesis out of the underline, as the TeX already does for '(@underline{en tant qu'entiers algébriques})' on p. 377.")
 },
 {
  "page": 378,
  "where": "Démonstration of 2.2, first sentence",
  "scan": "(qui revient à prendre les puissances. M^èmes des valeurs propres envisagées)",
  "tex": t("les puissances. $M$@textsuperscript{èmes} des valeurs"),
  "kind": "misprint_in_print",
  "confidence": "medium",
  "fix": None,
  "corrected": t("les puissances $M$@textsuperscript{èmes} des valeurs"),
  "note": "Stray full stop after 'puissances' in the print. The TeX keeps it."
 },
 {
  "page": 378,
  "where": "'tels que l'homomorphisme de Gal(...)-modules'",
  "scan": "l'homomorphisme de Gal(/𝔽_q)-modules",
  "tex": t("@underline{l'homomorphisme de Gal}$(/@mathbb{F}_q)$-@underline{modules}"),
  "kind": "misprint_in_print",
  "confidence": "high",
  "fix": None,
  "corrected": t("@underline{l'homomorphisme de Gal}$(@overline{@mathbb{F}}_q/@mathbb{F}_q)$-@underline{modules}"),
  "note": "The print omits 𝔽̄_q before the slash, as on p. 377. The TeX keeps the printed reading."
 },
 {
  "page": 378,
  "where": "unnumbered display before 'soit surjectif'",
  "scan": "H^{q-2j}(T̄_i, ℚ_ℓ(-j) —⊕Cl(Z_i)→ N^jH^q(X̄,ℚ_ℓ) — no closing parenthesis after (-j)",
  "tex": t("H^{q-2j}(@overline{T}_i,@ @mathbb{Q}_@ell(-j) @ @stackrel"),
  "kind": "misprint_in_print",
  "confidence": "high",
  "fix": None,
  "corrected": t("H^{q-2j}(@overline{T}_i,@ @mathbb{Q}_@ell(-j)) @ @stackrel"),
  "note": "The print lacks the closing parenthesis of H^{q-2j}(...). The TeX keeps the printed reading."
 },
 {
  "page": 379,
  "where": "line after (3.0.2)",
  "scan": "(on a employé da décomposition primitive, et (3.0.1).)",
  "tex": "employé da décomposition",
  "kind": "misprint_in_print",
  "confidence": "high",
  "fix": None,
  "corrected": "employé la décomposition",
  "note": "Typing error 'da' for 'la' in the print. The TeX keeps it."
 },
 {
  "page": 379,
  "where": "(3.0.4), second row",
  "scan": "0    1 ≤ ≤ n - 1",
  "tex": t("0 & 1 @leq @; @leq n - 1"),
  "kind": "misprint_in_print",
  "confidence": "high",
  "fix": None,
  "corrected": t("0 & 1 @leq i @leq n - 1"),
  "note": "The print omits the index i between the two signs. The TeX keeps the printed reading."
 }
]

ok = True
for f in findings:
    p = f["page"]
    with io.open(base + r"\b376_380\page_%d.tex" % p, encoding="utf-8", newline="") as fh:
        txt = fh.read()
    if f["tex"] not in txt:
        print("TEX NOT FOUND", p, ascii(f["tex"]))
        ok = False
    if f["fix"] is not None:
        old = f["fix"]["old"]
        n = txt.count(old)
        print(p, "fix old count", n, ascii(old))
        if n != 1 or "%%%%%%%%%%" in old:
            ok = False
        # show result of applying the fix
        print("   ->", ascii(txt.replace(old, f["fix"]["new"]).split("\n")[[i for i, l in enumerate(txt.split("\n")) if old in l][0]]))

with io.open(out, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

# re-read and validate
with io.open(out, encoding="utf-8") as fh:
    data = json.load(fh)
print("ok" if ok else "PROBLEM", len(data))
from collections import Counter
c = Counter((d["page"], d["kind"] == "misprint_in_print") for d in data)
for p in range(376, 381):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
