import json, os, sys

RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I"
BATCH = os.path.join(RUN, "b511_515")
OUT = os.path.join(RUN, "findings_511_515_recheck.json")

F = []

def add(**kw):
    F.append(kw)

# ---- page 511 ----
add(page=511,
    where="«et que cette \"stucture entière\" sur le système des pro-ℓ-groupes»",
    scan="cette \"stucture entière\" sur le",
    tex="``stucture entière''",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected="``structure entière''",
    note="Typing error of the print (r missing). The TeX keeps the printed reading.")
add(page=511,
    where="«Comme l'homomorphisme i (14.1.5) permet de réconstituer la structure d'extension»",
    scan="permet de réconstituer la (acute accent on the first e)",
    tex="permet de réconstituer la",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected="permet de reconstituer la",
    note="Spelling error of the print (reconstituer has no accent); the same spelling recurs on folio 512. The TeX keeps the printed reading.")

# ---- page 512 ----
add(page=512,
    where="first lines: «dans le cas semi-stable de réconstituer les accouplements de monodromie (9.1.2)»",
    scan="réconstituer les accouplements de monodromie (9.1.2)",
    tex="de réconstituer les",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected="de reconstituer les",
    note="Same spelling error as on folio 511. The TeX keeps the printed reading.")
add(page=512,
    where="display after «p_K et p'_K proviennent d'homomorphismes»",
    scan="p : M → B , M' → B' , (the second homomorphism has no name)",
    tex="\\quad , \\quad \\underline{M}' \\longrightarrow B'",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected="\\quad , \\quad p' \\;:\\; \\underline{M}' \\longrightarrow B'",
    note="The name p' of the second homomorphism is omitted; the next line uses the pair (p,p'). The TeX keeps the printed reading.")
add(page=512,
    where="«par image inverse par (p,p') une biextension E de (M,M') par G_mS»",
    scan="(M̲,M'): only the first M carries the underline",
    tex="$(\\underline{M},M')$",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected="$(\\underline{M},\\underline{M}')$",
    note="E is the pull-back by (p,p') of a biextension of (B,B'), hence a biextension of (M̲,M̲'); the constant values M,M' are introduced only in the next sentence. The TeX keeps the printed reading.")
add(page=512,
    where="«Ceci dit, supposant pour simplifier M,M' constants de valeurs M,M'. Pour tout couple»",
    scan="Ceci dit, supposant pour simplifier M̲,M̲' constants de valeurs M,M'. Pour",
    tex="Ceci dit, supposant pour",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected="Ceci dit, supposons pour",
    note="The sentence has no finite verb; supposons is meant (otherwise the full stop after M,M' would have to be a comma). The TeX keeps the printed reading.")

# ---- page 513 ----
add(page=513,
    where="Remarques 14.2.7, «on en déduit une extension A_K^♭»",
    scan="A_K with the handwritten flat sign ♭ as superscript",
    tex="extension $A_K^b$",
    kind="symbol", confidence="high",
    fix={"old": "extension $A_K^b$", "new": "extension $A_K^{\\flat}$"},
    note="The ind-group A_K^♭ of (8.3.3); folio 514 says of this extension «noté également A_K^♭, introduit dans (8.2.3)». The transcription writes the same handwritten sign as \\flat on folios 414 and 417; here it is typed as a Latin b.")
add(page=513,
    where="display (14.2.8)",
    scan="0 → G_K → A_K^♭ → M_K⊗Q/Z → 0 . (handwritten flat sign)",
    tex="A_K^b \\longrightarrow",
    kind="symbol", confidence="high",
    fix={"old": "A_K^b \\longrightarrow", "new": "A_K^{\\flat} \\longrightarrow"},
    note="Same flat sign as in the preceding finding.")

# ---- page 514 ----
add(page=514,
    where="«isomorphe au groupe, noté également A_K^♭ , introduit dans (8.2.3)»",
    scan="noté également A_K^♭ , (handwritten flat sign, triangular bowl)",
    tex="également $A_K^b$",
    kind="symbol", confidence="high",
    fix={"old": "également $A_K^b$", "new": "également $A_K^{\\flat}$"},
    note="«noté également»: the same symbol as the group A_K^♭ of (8.3.3), which the TeX writes \\flat on folio 417.")
add(page=514,
    where="«noté également A_K^♭ , introduit dans (8.2.3), compte tenu de l'isomorphisme 11.11»",
    scan="introduit dans (8.2.3), compte",
    tex="introduit dans (8.2.3)",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected="introduit dans (8.3.3)",
    note="Wrong reference number: A_K^♭ is defined in (8.3.3) (folio 417); paragraph 8.2 (folio 416) has no numbered formulas. Folio 464 likewise cites (8.2.4) for (8.3.4). The TeX keeps the printed reading.")
add(page=514,
    where="display (14.3.2)",
    scan="Hom(M,G_K(K)) → ∏_ℓ Hom(M,H^1(K,T_ℓ(G_K)) : three opening, two closing parentheses in the right-hand term",
    tex="\\mathrm{Hom}(M, H^1(K, T_\\ell(G_K))",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected="\\mathrm{Hom}(M, H^1(K, T_\\ell(G_K)))",
    note="One closing parenthesis is missing in the print. The TeX keeps the printed reading.")

# ---- page 515 ----
add(page=515,
    where="«Ceci détermine donc déjà i modulo un élément Hom(M,g), où g est le sous-groupe»",
    scan="modulo un élément Hom(M,g), où",
    tex="un élément $\\mathrm{Hom}(M,g)$",
    kind="misprint_in_print", confidence="low", fix=None,
    corrected="un élément de $\\mathrm{Hom}(M,g)$",
    note="The word de appears to be missing. The TeX keeps the printed reading.")
add(page=515,
    where="proof of 14.3.4: «admet une suite de composition dans les quotients successifs sont de l'un des types suivants»",
    scan="suite de composition dans les quotients successifs sont",
    tex="composition dans les quotients",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected="composition dont les quotients",
    note="dans typed for dont. The TeX keeps the printed reading.")
add(page=515,
    where="proof of 14.3.4: «On est donc réduit aussitôt au cas où G_K lui-même est de l'un des types précédents»",
    scan="au cas où 𝔾_K lui-même (the double-struck G of 𝔾_mK, 𝔾_aK two lines above)",
    tex="au cas où $\\mathbb{G}_K$ lui-même",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected="au cas où $G_K$ lui-même",
    note="The group G_K of the lemma is meant, not the double-struck G. The TeX keeps the printed glyph.")

# ---- validation ----
ok = True
texts = {}
for p in sorted({f["page"] for f in F}):
    with open(os.path.join(BATCH, "page_%03d.tex" % p), encoding="utf-8", newline="") as fh:
        texts[p] = fh.read()
for f in F:
    t = texts[f["page"]]
    if f["tex"] not in t:
        print("TEX NOT FOUND", f["page"], repr(f["tex"])); ok = False
    if f["fix"] is not None:
        n = t.count(f["fix"]["old"])
        if n != 1:
            print("OLD COUNT", n, f["page"], repr(f["fix"]["old"])); ok = False
        if "%%%%%%%%%%" in f["fix"]["old"]:
            print("MARKER IN OLD", f["page"]); ok = False
    if f["kind"] == "misprint_in_print":
        if "corrected" not in f:
            print("NO CORRECTED", f["page"]); ok = False
    else:
        if "corrected" in f:
            print("CORRECTED ON NON-MISPRINT", f["page"]); ok = False
# overlapping fixes on the same page
for p in texts:
    spans = []
    for f in F:
        if f["page"] == p and f["fix"] is not None:
            i = texts[p].find(f["fix"]["old"])
            spans.append((i, i + len(f["fix"]["old"])))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            print("OVERLAP", p, a, b); ok = False

order = ["page", "where", "scan", "tex", "kind", "confidence", "fix", "corrected", "note"]
out = [{k: f[k] for k in order if k in f} for f in F]
if ok:
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("written", OUT, len(out))
    from collections import Counter
    c = Counter((f["page"], f["kind"] == "misprint_in_print") for f in out)
    for p in sorted(texts):
        print(p, "%d/%d" % (c[(p, False)], c[(p, True)]))
else:
    print("NOT WRITTEN")
    sys.exit(1)
