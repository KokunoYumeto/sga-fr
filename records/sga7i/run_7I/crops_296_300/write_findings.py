import json, io
BS = chr(92)
def b(s):
    return s.replace('@', BS)

base = "C:/Users/user/Documents/sga_scan_check_20261105/run_7I/"
F = []
def add(**k):
    for key in ("tex", "corrected"):
        if key in k and k[key] is not None:
            k[key] = b(k[key])
    if k.get("fix"):
        k["fix"] = {"old": b(k["fix"]["old"]), "new": b(k["fix"]["new"])}
    F.append(k)

add(page=297,
    where="6.9 a), first sentence: the open immersion",
    scan="Soit j:V ↪ S un ouvert schématiquement dense (the open is U everywhere else: j_*G_mU in the next sentence, U = S-Y in b) and in the Corollaire)",
    tex="$j:V @hookrightarrow S$",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected="$j:U @hookrightarrow S$",
    note="Printed V for U; the TeX keeps the printed reading.")

add(page=297,
    where="6.9 a), unnumbered display after 'Soit D le faisceau étale quotient'",
    scan="0 → G_mS → j_* G_mS → D → 0 .",
    tex="j_{*} @, @underline{G}_{mS}",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected="j_{*} @, @underline{G}_{mU}",
    note="The middle term is the sheaf j_*G_mU of the preceding sentence; the print has the subscript mS. The TeX keeps the printed reading.")

add(page=299,
    where="heading of section 7",
    scan="the heading underline stops after 'par'; G_m carries only its own notation underline, with a gap between the two",
    tex="@underline{Prolongements canoniques d'extensions et de biextensions par $@underline{G}_m$}",
    kind="underline", confidence="medium",
    fix={"old": "biextensions par $@underline{G}_m$}", "new": "biextensions par} $@underline{G}_m$"},
    note="The TeX runs the heading underline over the formula; the print underlines only the words.")

add(page=299,
    where="7.0, third sentence",
    scan="s sont point fermé",
    tex="$s$ sont point fermé",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected="$s$ son point fermé",
    note="'sont' for 'son'; the TeX keeps the printed reading.")

add(page=300,
    where="7.1 b), line 'soit un groupe de torsion (par exemple P ou Q de'",
    scan="'soit un groupe de torsion' underlined; the underline breaks, the opening parenthesis is not underlined, and a new underline starts at 'par exemple'",
    tex="@underline{soit un groupe de torsion (par exemple}",
    kind="underline", confidence="medium",
    fix={"old": "@underline{soit un groupe de torsion (par exemple}", "new": "@underline{soit un groupe de torsion} (@underline{par exemple}"},
    note="The TeX underline runs through the space and the opening parenthesis.")

add(page=300,
    where="7.1 b), 'alors le foncteur E ⟼ E_η dans la catégorie des biextensions de (P,Q)'",
    scan="dans la catégorie des biextensions de (P,Q) par G_mS dans la catégorie des biextensions de (P_η,Q_η)",
    tex="@underline{dans la catégorie des biextensions de} $(P,Q)$",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected="@underline{de la catégorie des biextensions de} $(P,Q)$",
    note="First 'dans' for 'de' (the functor goes de ... dans ..., as in 7.1 a)); the TeX keeps the printed reading.")

add(page=300,
    where="7.1 b), sentence after (7.1.2)",
    scan="pour que E soit isomorphe à la fibre générique d'une biextension E de (P,Q)",
    tex="pour que} $E$ @underline{soit",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected="pour que} $E_@eta$ @underline{soit",
    note="The given biextension is E_η (cf. 7.1 a): 'pour que l'extension E_η soit isomorphe'); the print drops the index η. The TeX keeps the printed reading.")

add(page=300,
    where="Démonstration a), second sentence",
    scan="le foncteur \"restriction à η\" défini sur la catégorie des biextensions par Ḡ",
    tex="défini sur la catégorie des biextensions par $@overline{G}$",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected="défini sur la catégorie des extensions par $@overline{G}$",
    note="Part a) concerns extensions of P (the cited 6.6 is the statement for extensions; biextensions are 6.7, used for b) on the next page). The TeX keeps the printed reading.")

ok = True
for f in F:
    p = f["page"]
    src = io.open(base + "b296_300/page_%d.tex" % p, encoding="utf-8", newline="").read()
    n = src.count(f["tex"])
    if n != 1:
        print("TEX count", n, p, repr(f["tex"])); ok = False
    if f["fix"]:
        n = src.count(f["fix"]["old"])
        if n != 1:
            print("OLD count", n, p, repr(f["fix"]["old"])); ok = False
        if "%%%%%%%%%%" in f["fix"]["old"]:
            print("marker in old", p); ok = False
        new_src = src.replace(f["fix"]["old"], f["fix"]["new"])
        print("applied", p, new_src.count(f["fix"]["new"]))
    if f["kind"] == "misprint_in_print":
        assert "corrected" in f
    else:
        assert "corrected" not in f
print("all unique:", ok)
out = base + "findings_296_300_recheck.json"
io.open(out, "w", encoding="utf-8", newline="\n").write(json.dumps(F, ensure_ascii=False, indent=1) + "\n")
print("wrote", out, len(F))
