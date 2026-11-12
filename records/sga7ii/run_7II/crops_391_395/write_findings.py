import json, sys, pathlib
sys.stdout.reconfigure(encoding="utf-8")
BS = chr(92)
RUN = pathlib.Path("C:/Users/user/Documents/sga_scan_check_20261105/run_7II")
OUT = RUN / "findings_391_395_recheck.json"


def b(s):
    """the character ¤ stands for a backslash"""
    if s is None:
        return None
    return s.replace("¤", BS)


F = []
F.append({
 "page": 391,
 "where": "Théorème 5.4, last line: 'de H^i_c(X,G)^∨.'",
 "scan": "de H^i_c(X,G)^∨. : 'de' underlined; the H (printed heavy, apparently struck twice) has no underline",
 "tex": b("¤underline{de} $¤underline{H}_c^i(X,G)^¤vee$."),
 "kind": "misprint_in_print",
 "confidence": "high",
 "fix": {"old": b("$¤underline{H}_c^i(X,G)^¤vee$."), "new": b("$H_c^i(X,G)^¤vee$.")},
 "corrected": b("¤underline{H}_c^i(X,G)^¤vee"),
 "note": "The typist left out the underline that marks the cohomology H (the first H^i_c(X,G)^∨ of the same sentence has it; the plain H of this proof is the sheaf H of 0 → j_!G → j_*G → H → 0). The TeX silently supplies it; the fix restores the printed plain H. The heavier stroke of the H is not reproduced. Same slip on p. 393 (Thm 5.5.2); p. 386 (Thm 5.2.2) has a printed plain H too, which both layers already keep plain."
})
F.append({
 "page": 392,
 "where": "5.5, second paragraph: 'avec # k(x) = q_x'",
 "scan": "avec # k(x) = q_x (the typed number sign #, horizontal bars)",
 "tex": b("avec $¤sharp¤, k(x) = q_x$"),
 "kind": "symbol",
 "confidence": "medium",
 "fix": {"old": b("¤sharp¤, k(x)"), "new": b("¤#¤, k(x)")},
 "note": b("The print has the number sign #, not the music sharp ♯ that ¤sharp gives. The 7 II TeX writes ¤# for this sign elsewhere (pp. 35, 78, 202, 410, 411).")
})
F.append({
 "page": 392,
 "where": "proof of Lemme 5.5.1, last line: 'la fraction rationnelle σ Z(X,G,t)'",
 "scan": "σ ℤ(X,G,t): the Z is the typescript's double-struck Z (thick doubled diagonal, as in ℤ[(1/r)_{r∈T}] on p. 384), not the plain Z of Z(X,G,t) on pp. 386 and 393",
 "tex": b("$¤sigma Z(X,¤underline{G},t)$"),
 "kind": "misprint_in_print",
 "confidence": "medium",
 "fix": {"old": b("$¤sigma Z(X,"), "new": b("$¤sigma ¤mathbb{Z}(X,")},
 "corrected": b("¤sigma Z(X,¤underline{G},t)"),
 "note": "Wrong glyph of the typist for the zeta function Z; the TeX silently types the plain Z, the fix restores the printed glyph. Goes with the held volume decision on reproducing the typist's glyphs (plain Q for double-struck Q, the 'Gal' G)."
})
F.append({
 "page": 393,
 "where": "Théorème 5.5.2, second line: 'et G un E-faisceau'",
 "scan": "et G un : 'et' and 'un' underlined, G without underline",
 "tex": b("¤underline{et} $¤underline{G}$ ¤underline{un}"),
 "kind": "underline",
 "confidence": "high",
 "fix": {"old": b("¤underline{et} $¤underline{G}$ ¤underline{un}"), "new": b("¤underline{et} $G$ ¤underline{un}")},
 "note": "The underline stops after 'et' and starts again at 'un'. The print often writes the E-sheaf G without underline (p. 391 j_*G, H^i_c(X,G); p. 393 Tr(F,x*G)) and both layers follow it there, so this is not classed as a misprint."
})
F.append({
 "page": 393,
 "where": "Théorème 5.5.2, second line: 'tel que log|G| ≤ λ'",
 "scan": "log|G| ≤ λ : G without underline",
 "tex": b("$¤log|¤underline{G}| ¤leqslant ¤lambda$"),
 "kind": "underline",
 "confidence": "high",
 "fix": {"old": b("$¤log|¤underline{G}|"), "new": b("$¤log|G|")},
 "note": "As 'et G un' in the same line: the print does not underline G in this statement."
})
F.append({
 "page": 393,
 "where": "Théorème 5.5.2: 'de Frobenius agissant sur H^i_c(X,G) vérifient'",
 "scan": "H^i_c(X,G) : G underlined, H not underlined (the underline of 'agissant sur' stops before H)",
 "tex": b("$¤underline{H}^i_c(X,¤underline{G})$"),
 "kind": "misprint_in_print",
 "confidence": "high",
 "fix": {"old": b("$¤underline{H}^i_c(X"), "new": b("$H^i_c(X")},
 "corrected": b("¤underline{H}^i_c(X,¤underline{G})"),
 "note": "Same slip as p. 391 (Thm 5.4, last H): the underline that marks the cohomology H is left out (Lemme 5.5.1 and Cor. 5.5.3 have it). The TeX silently supplies it; the fix restores the printed plain H."
})
F.append({
 "page": 393,
 "where": "display after 'trivialement une majoration': '# X(F_{q^k}) ≤ A.q^k .'",
 "scan": "handwritten # (two horizontal bars across two upright strokes)",
 "tex": b("¤sharp ¤; X(¤mathbb{F}_{q^k})"),
 "kind": "symbol",
 "confidence": "medium",
 "fix": {"old": b("¤sharp ¤; X("), "new": b("¤# ¤; X(")},
 "note": b("As on p. 392: the print's sign is #, the TeX's ¤sharp gives ♯; elsewhere the 7 II TeX writes ¤#.")
})
F.append({
 "page": 394,
 "where": "first paragraph (proof of 5.5.2): 'comme dans la démonstration de 5.5.2.'",
 "scan": "On procède alors par récurrence sur n, comme dans la démonstration de 5.5.2.",
 "tex": "comme dans la démonstration de 5.5.2.",
 "kind": "misprint_in_print",
 "confidence": "medium",
 "fix": None,
 "corrected": "5.2.2",
 "note": "The paragraph is the proof of 5.5.2 itself; the induction on n by fibration in curves that it invokes is the proof of 5.2.2 (p. 386 'Procédons maintenant par récurrence sur n = dim(X)'; 5.5 calls it 'la méthode précédente de fibration en courbes'). Wrong reference number; the TeX keeps the printed reading."
})
F.append({
 "page": 394,
 "where": "proof of Cor. 5.5.3 (iv): 'montre qu'il suffit de prouver 5.2.2 pour U'",
 "scan": "montre qu'il suffit de prouver 5.2.2 pour U.",
 "tex": "montre qu'il suffit de prouver 5.2.2 pour $U$.",
 "kind": "misprint_in_print",
 "confidence": "low",
 "fix": None,
 "corrected": "(iv)",
 "note": "The induction proves (iv) of 5.5.3: integrality (5.2.2) is already known for every X, and the exact sequence H^i_c(U) → H^i_c(X) → H^i_c(Z) reduces the bound (iv) from X to U and Z. The intended reference is probably '(iv)' (or '5.5.3'); author slip, low confidence in the exact reading. The TeX keeps the printed reading."
})
F.append({
 "page": 395,
 "where": "last display: '(resp. |α| ≤ q^{i-2+1} = q^{i-1} ≤ q^{i-1/2} .'",
 "scan": "the parenthesis opened by '(resp.' is never closed",
 "tex": b("(¤mathrm{resp.} ¤; |¤alpha| ¤leq q^{i-2+1} ¤quad = q^{i-1} ¤leq q^{i-¤frac{1}{2}} ¤qquad ."),
 "kind": "misprint_in_print",
 "confidence": "medium",
 "fix": None,
 "corrected": b("(¤mathrm{resp.} ¤; |¤alpha| ¤leq q^{i-2+1} ¤quad = q^{i-1} ¤leq q^{i-¤frac{1}{2}}) ¤qquad ."),
 "note": "Unbalanced parenthesis of the print; the TeX keeps the printed reading."
})

ok = True
for x in F:
    p = RUN / "b391_395" / ("page_%d.tex" % x["page"])
    s = p.read_text(encoding="utf-8")
    if "¤" in json.dumps(x, ensure_ascii=False):
        print("PLACEHOLDER LEFT", x["page"]); ok = False
    if x["tex"] not in s:
        print("TEX NOT FOUND", x["page"], x["tex"]); ok = False
    fx = x["fix"]
    if fx is None:
        continue
    n = s.count(fx["old"])
    if n != 1 or "%%%%%%%%%%" in fx["old"]:
        print("BAD", x["page"], n, fx["old"]); ok = False
    else:
        print("ok", x["page"], fx["old"], "->", fx["new"])
print("ALL OK" if ok else "PROBLEMS")
if ok:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("written", OUT, len(F))
