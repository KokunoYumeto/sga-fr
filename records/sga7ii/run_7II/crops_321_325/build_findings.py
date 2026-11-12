import json, os, sys

BASE = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II"
PAGES = os.path.join(BASE, "b321_325")
OUT = os.path.join(BASE, "findings_321_325.json")

def M(page, where, scan, tex, conf, corrected, note):
    return {"page": page, "where": where, "scan": scan, "tex": tex,
            "kind": "misprint_in_print", "confidence": conf, "fix": None,
            "corrected": corrected, "note": note}

KEEP = "The TeX keeps the printed reading (fix null)."
F = [
 M(321, "first line of the page (end of the statement begun on p. 320)",
   "Lefschetz de sectionsde X (no space between 'sections' and 'de'; the s appears typed into the space)",
   r"\underline{Lefschetz de sectionsde}", "high",
   r"\underline{Lefschetz de sections de}",
   "Missing word space. " + KEEP),
 M(321, "formula (6.4.2.3), left-hand side",
   "χ(Y(d)  =  (closing parenthesis missing)",
   r"\chi(Y(d) \;=\;", "high",
   r"\chi(Y(d)) \;=\;",
   "Unbalanced parenthesis; (6.4.2.4) on p. 322 prints χ(Y(d)). " + KEEP),
 M(322, "6.5, first sentence (line end after 'strict')",
   "hensélien strict / η son point générique, (no comma after 'strict')",
   r"strict $\eta$ son point", "medium",
   r"strict, $\eta$ son point",
   "Missing comma in the enumeration 'S ..., η ..., η̄ ..., et s ...'; the following line is a pasted-in correction in lighter type. " + KEEP),
 M(323, "item label before 'l'élément non trivial σ de Z/2Z'",
   "(6.5.2.2)",
   "(6.5.2.2)", "high",
   "(6.5.1.2)",
   "Wrong formula number: the item belongs to 6.5.1 and follows (6.5.1.1); 6.5.2 begins later on the page and has only (6.5.2.1). " + KEEP),
 M(323, "item (6.5.2.2) [= 6.5.1.2], 'agit sur H^i(...)'",
   "agit sur H^i(X_η̄,Q_ℓ) par la symétrie",
   r"H^i(X_{\overline{\eta}}", "medium",
   r"H^{n-1}(X_{\overline{\eta}}",
   "Wrong index: the symmetry σx = x - (-1)^m(xδ)δ is the action on H^{n-1} (I acts trivially on H^i for i ≠ n-1, p. 322; the bracket after it places (x.δ)δ in H^{n-1}). " + KEEP),
 M(323, "bracket after the symmetry formula, 'H^{2n-2}(X_η̄,Q_ℓ( m) ≃ Q_ℓ(-m)'",
   "H^{2n-2}(X_η̄,Q_ℓ( m) ≃ Q_ℓ(-m) (closing parenthesis of H^{2n-2}(...) missing)",
   r"\mathbb{Q}_\ell(m) \simeq \mathbb{Q}_\ell(-m)$", "high",
   r"\mathbb{Q}_\ell(m)) \simeq \mathbb{Q}_\ell(-m)$",
   "Unbalanced parenthesis. " + KEEP),
 M(323, "6.5.2, 'Il existe un élément δ ∈ H^{n-1}(X_η̄,Q_ℓ(m) ,'",
   "δ ∈ H^{n-1}(X_η̄,Q_ℓ(m) , élément canoniquement (closing parenthesis missing)",
   r"\mathbb{Q}_\ell(m)$ , élément", "high",
   r"\mathbb{Q}_\ell(m))$ , élément",
   "Unbalanced parenthesis. " + KEEP),
 M(323, "6.5.2, 'agit sur χ ∈ H^{n-1}(...)'",
   "agit sur χ ∈ H^{n-1}(X_η̄,Q_ℓ) (Greek chi, same glyph as χ(Y(d)) on p. 321)",
   r"agit sur $\chi \in", "high",
   r"agit sur $x \in",
   "Chi typed for the variable x, which (6.5.2.1) and the following bracket use. " + KEEP),
 M(323, "bracket after (6.5.2.1), 'H^{2n-2}(X_η̄,Q_ℓ(m) ≃ Q_ℓ(-m-1)'",
   "H^{2n-2}(X_η̄,Q_ℓ(m) ≃ Q_ℓ(-m-1) (closing parenthesis of H^{2n-2}(...) missing)",
   r"\mathbb{Q}_\ell(m) \simeq \mathbb{Q}_\ell(-m-1)$", "high",
   r"\mathbb{Q}_\ell(m)) \simeq \mathbb{Q}_\ell(-m-1)$",
   "Unbalanced parenthesis. " + KEEP),
 M(323, "bracket after (6.5.2.1), 'multiplié par δ ∈ H^{n-1}(X_η̄,Q_ℓ(m) donne'",
   "δ ∈ H^{n-1}(X_η̄,Q_ℓ(m)   donne (closing parenthesis missing)",
   r"\mathbb{Q}_\ell(m)$ donne", "high",
   r"\mathbb{Q}_\ell(m))$ donne",
   "Unbalanced parenthesis. " + KEEP),
 M(324, "first paragraph, 'le groupe I_i d'inertie de δ_i en S_i'",
   "le groupe I_i d'inertie de δ_i en S_i (handwritten δ_i after 'de', typed S_i after 'en')",
   r"\underline{d'inertie de} $\delta_{i}$ \underline{en} $S_{i}$", "medium",
   r"\underline{d'inertie de} $S_{i}$ \underline{en} $s_{i}$",
   "δ_i is a cohomology class and has no inertia group; 6.5 says 'le groupe d'inertie de S en s', and S_i is the strict henselization of D at s_i. Corrected reading follows 6.5. " + KEEP),
 M(324, "display giving δ_i and m, 'δ_i ∈ H^{n-1}(X,...'",
   "δ_i ∈ H^{n-1}(X,Q_ℓ(m) (X without the subscript η̄)",
   r"\delta_{i} \in H^{n-1}(X,", "medium",
   r"\delta_{i} \in H^{n-1}(X_{\bar{\eta}},",
   "The vanishing cycles live in the cohomology of the geometric generic fibre (6.5; 6.6.1 has them generate E^{n-1}(X_η̄,Q_ℓ(m)) inside H^{n-1}(X_η̄,Q_ℓ(m))). Independent of the parenthesis finding on the same formula. " + KEEP),
 M(324, "display giving δ_i and m, 'Q_ℓ(m) , m ='",
   "H^{n-1}(X,Q_ℓ(m) , m = (closing parenthesis missing)",
   r"\mathbb{Q}_{\ell}(m) \ , \ m", "high",
   r"\mathbb{Q}_{\ell}(m)) \ , \ m",
   "Unbalanced parenthesis. " + KEEP),
 M(324, "6.6.1, 'E^{n-1}(X_η̄,Q_ℓ(m) ( =dfn'",
   "E^{n-1}(X_η̄,Q_ℓ(m) ( =dfn (closing parenthesis missing)",
   r"E^{n-1}(X_{\bar{\eta}},\mathbb{Q}_{\ell}(m)$", "high",
   r"E^{n-1}(X_{\bar{\eta}},\mathbb{Q}_{\ell}(m))$",
   "Unbalanced parenthesis. " + KEEP),
 M(324, "6.6.1, 'dans H^{n-1}(X_η̄,Q_ℓ(m), cf. 5.4.4)'",
   "H^{n-1}(X_η̄,Q_ℓ(m), cf. 5.4.4) (closing parenthesis of H^{n-1}(...) missing)",
   r"\mathbb{Q}_{\ell}(m)$, cf. 5.4.4)", "high",
   r"\mathbb{Q}_{\ell}(m))$, cf. 5.4.4)",
   "Unbalanced parenthesis. " + KEEP),
 M(325, "formula (6.6.3), left-hand side",
   "H^{n-1}(X_η̄,Q_ℓ(m)^π (closing parenthesis missing; (6.6.4) prints (m))^π)",
   r"\mathbb{Q}_{\ell}(m)^{\pi}", "high",
   r"\mathbb{Q}_{\ell}(m))^{\pi}",
   "Unbalanced parenthesis. " + KEEP),
 M(325, "formula (6.6.4), right-hand side",
   "Im(H^{n-1}(X,Q_ℓ(i)))",
   r"\mathbb{Q}_{\ell}(i)", "high",
   r"\mathbb{Q}_{\ell}(m)",
   "Wrong twist: both sides concern Q_ℓ(m) (left-hand side, (6.6.3) and 6.6.1); i is the index of s_i, δ_i. " + KEEP),
 M(325, "proof of 6.6.2, 'Donc on n'a qu'a appliquer 6.1.2'",
   "on n'a qu'a appliquer (a without grave accent)",
   "qu'a appliquer", "high",
   "qu'à appliquer",
   "Missing accent. " + KEEP),
 M(325, "proof of 6.6.2, 'la conjugaison dans π_1^mod(P^r - X,η̄)'",
   "π_1^mod(P^r - X,η̄) with no check accents on P and X (the diagram and the next paragraph print P̌^r - X̌)",
   r"(\mathbb{P}^{r} - X,\bar{\eta})", "medium",
   r"(\check{\mathbb{P}}^{r} - \check{X},\bar{\eta})",
   "The hand-drawn checks were left off here; the same group appears with both checks in the diagram and in 'par des éléments de π_1^mod(P̌^r - X̌, η̄)'. " + KEEP),
]

# verify: each 'tex' (and any fix 'old') occurs exactly once on its page
ok = True
for f in F:
    path = os.path.join(PAGES, "page_%d.tex" % f["page"])
    with open(path, "r", encoding="utf-8", newline="") as fh:
        s = fh.read()
    for key, val in (("tex", f["tex"]), ("fix.old", f["fix"]["old"] if f["fix"] else None)):
        if val is None:
            continue
        n = s.count(val)
        if n != 1:
            ok = False
            print("NOT UNIQUE", f["page"], key, repr(val), n)
print("all unique" if ok else "PROBLEM")

from collections import Counter
c = Counter((f["page"], f["kind"] == "misprint_in_print") for f in F)
for p in range(321, 326):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])

if ok:
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(F, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("written", OUT, len(F))
