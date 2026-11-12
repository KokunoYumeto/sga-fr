import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')

RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I"
BATCH = os.path.join(RUN, "b276_280")
OUT = os.path.join(RUN, "findings_276_280_recheck.json")

F = []

def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "confidence": confidence, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)

# ---------------- page 276 ----------------
add(276,
    "first line of the page: 'deduit de l'homomorphisme canonique f : A -> P est surjectif'",
    "f : A ⟶ P",
    r"$f : A \longrightarrow P$",
    "misprint_in_print", "medium", None,
    "The TeX keeps the printed reading. P is an extension of the abelian scheme A (4.12), so the canonical "
    "homomorphism is the projection P -> A; it induces Pic(A) -> Pic(P) (4.12.2), and both 'L ≃ f*(M)' with M "
    "on A and 'si L = f*(M) est ample, il en est de même de M' further down require f : P -> A.",
    r"$f : P \longrightarrow A$")

add(276,
    "line after the display: 'où M est un Module inversible sur M.'",
    "où M est un Module inversible sur M. (both M underlined)",
    r"inversible sur $\underline{M}$.",
    "misprint_in_print", "high", None,
    "The TeX keeps the printed reading. M is an invertible Module on A: f*(M) is its pull-back to P, and "
    "Proposition 4.13 says 'M est un Module inversible ample sur A'.",
    r"inversible sur $A$.")

add(276,
    "display after 'un isomorphisme'",
    "𝕃* ≃ f*(M) ,  (star after the double-struck L)",
    r"\mathbb{L}^{*} \simeq f^{*}(\underline{M})",
    "misprint_in_print", "low", None,
    "The TeX keeps the printed star. A star after L has no meaning here (in this volume a star on a group "
    "denotes the dual), and the same relation is written 'L = f*(M)' four lines below. Probably a typing slip "
    "anticipating f*; apply the correction only if the coordinator agrees.",
    r"\mathbb{L} \simeq f^{*}(\underline{M})")

# ---------------- page 277 ----------------
add(277,
    "'(qui, en vertu de 4.7, peut d'ailleurs se décrire ... sur (P,P) qui sont symétriques. Il s'impose'",
    "the parenthesis opened before 'qui, en vertu de 4.7' is never closed",
    r"qui sont symétriques. Il s'impose",
    "misprint_in_print", "medium", None,
    "The TeX keeps the unclosed parenthesis; the parenthetical clause ends with this sentence.",
    r"qui sont symétriques). Il s'impose")

# ---------------- page 278 ----------------
add(278,
    "proof of 5.1, first sentence: 'tout torseur E sous G_S est représentable'",
    "sous G_S est représentable",
    r"sous $G_S$ est",
    "misprint_in_print", "medium", None,
    "The TeX keeps G_S. No G is defined here: the sentence concerns torsors under Z_S (the parenthesis "
    "extends the lemma to every separated, locally finitely presented, locally quasi-finite group scheme, "
    "and the next sentence goes on with Z_S).",
    r"sous $Z_S$ est")

# ---------------- page 279 ----------------
add(279,
    "'l'assertion de pleine fidèlité de 5.1'",
    "fidèlité (grave accent on the first e)",
    r"pleine fidèlité",
    "misprint_in_print", "high", None,
    "Spelling slip of the typescript (the word is 'fidélité'); the TeX keeps it.",
    r"pleine fidélité")

add(279,
    "'le fait que H^1(S,Z_S) -> H^1(eta,Z_eta)) est injectif'",
    "H¹(η,Z_η)) with a surplus closing parenthesis",
    r"H^1(\eta,Z_\eta))$ est injectif",
    "misprint_in_print", "high", None,
    "The TeX keeps the surplus parenthesis.",
    r"H^1(\eta,Z_\eta)$ est injectif")

add(279,
    "line after the display H^1(k,Z) = Hom cont(pi,Z)/Z = e: 'puisque E est sans torsion'",
    "puisque E est sans torsion",
    r"puisque $E$ est sans torsion",
    "misprint_in_print", "high", None,
    "The TeX keeps E. The torsion-free group is Z (5.1): Hom cont(pi,Z) is trivial because pi is profinite "
    "and Z is torsion-free; E is the torsor.",
    r"puisque $Z$ est sans torsion")

add(279,
    "Corollaire 5.2: 'le foncteur E -> E_eta de la catégorie des torseurs sur P_eta de groupe Z_{P_eta} dans "
    "la catégorie des torseurs'",
    "catégorie des torseurs sur P_η de groupe Z_{P_η} dans la catégorie des torseurs (p. 280 goes on: "
    "'sur P_η de groupe Z_{P_η}')",
    r"torseurs sur} $P_\eta$ \underline{de groupe} $Z_{P_\eta}$ \underline{dans",
    "misprint_in_print", "high", None,
    "The TeX keeps the printed reading. E -> E_eta goes from the torsors on P under Z_P to the torsors on "
    "P_eta under Z_{P_eta}; the print names the generic-fibre category as both source and target.",
    r"torseurs sur} $P$ \underline{de groupe} $Z_P$ \underline{dans")

# ---------------- page 280 ----------------
add(280,
    "end of the proof of 5.2: 'le point générique p_i de P_i est aussi point générique de P_i .'",
    "aussi point générique de P_i .",
    r"aussi point générique de $P_i$ .",
    "misprint_in_print", "medium", None,
    "The TeX keeps P_i. As printed the clause is tautological; 5.1 is applied to the P_i and to the P_{i eta}, "
    "and the point is that both have the same generic point p_i.",
    r"aussi point générique de $P_{i\eta}$ .")

# ---------------- checks ----------------
ok = True
for d in F:
    p = os.path.join(BATCH, "page_%03d.tex" % d["page"])
    t = open(p, encoding="utf-8", newline="").read()
    assert "\r" not in t
    n = t.count(d["tex"])
    if n != 1:
        ok = False
        print("TEX NOT UNIQUE", d["page"], n, d["tex"])
    if d["fix"] is not None:
        m = t.count(d["fix"]["old"])
        if m != 1:
            ok = False
            print("OLD NOT UNIQUE", d["page"], m, d["fix"]["old"])
    for k, v in d.items():
        if isinstance(v, str) and any(ord(c) < 32 for c in v):
            ok = False
            print("CONTROL CHAR", d["page"], k)
print("checks ok" if ok else "CHECKS FAILED")

with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    json.dump(F, f, ensure_ascii=False, indent=1)
    f.write("\n")

counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0])
    c[1 if d["kind"] == "misprint_in_print" else 0] += 1
for pg in range(276, 281):
    c = counts.get(pg, [0, 0])
    print(pg, "%d/%d" % (c[0], c[1]))
