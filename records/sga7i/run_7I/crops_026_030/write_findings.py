import json
import pathlib

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I")
BATCH = RUN / "b026_030"
OUT = RUN / "findings_026_030.json"

F = []

F.append(dict(
    page=26,
    where="last paragraph, 'Les conditions (i) et (ii) ne sont autres que les conditions a) et b).'",
    scan="Les conditions (i) et (ii) ne sont autres que les conditions a) et b). Enfin f est lisse aux points de σ ...",
    tex=r"Les conditions (i) et (ii) ne sont autres que les conditions a) et b).",
    kind="misprint_in_print",
    confidence="medium",
    fix=None,
    corrected=r"Les conditions (ii) et (iii) ne sont autres que les conditions c) et b).",
    note="Wrong condition labels. In Proposition 2.1 (p. 25), (i) is the smoothness of f along σ(P^1), which the "
         "next sentence proves ('Enfin f est lisse aux points de σ'); (ii) (integral fibres with only ordinary "
         "singularities) comes from c) together with the integrality of S'_t shown just before; (iii) (smooth "
         "fibres over U) is b); a) (the axis meets S transversally) only serves the blow-up. Same in the DjVu "
         "witness. The TeX keeps the printed reading. The corrected layer reads '(ii) et (iii) ... b) et c)' "
         "(the same pairs as a set). 'corrected' replaces the 'tex' substring.",
))

F.append(dict(
    page=27,
    where="proof of Corollaire 2.2, last sentence",
    scan="... à ces deux conditions et de remplacer / par U ∩ U_1 . (nothing between 'remplacer' and 'par')",
    tex=r"de remplacer par $U \cap U_1$",
    kind="misprint_in_print",
    confidence="high",
    fix=None,
    corrected=r"de remplacer $U$ par $U \cap U_1$",
    note="The object of 'remplacer' is missing at the line break: the open set U of 2.1 is to be replaced by "
         "U ∩ U_1. Same in the DjVu witness. The TeX keeps the printed reading; the corrected layer also still "
         "lacks the U. 'corrected' replaces the 'tex' substring.",
))

F.append(dict(
    page=27,
    where="Théorème 2.3.1, '(condition réalisée si dim X = 2 d'après [1] ou si k = 0 d'après [2])'",
    scan="ou si k = 0 d'après [2]",
    tex=r"\underline{ou si} $k = 0$",
    kind="misprint_in_print",
    confidence="high",
    fix=None,
    corrected=r"\underline{ou si} $\operatorname{char}k = 0$",
    note="k is the field; the condition meant is characteristic zero (p = 0), [2] being Hironaka's resolution of "
         "singularities in characteristic zero. Same in the DjVu witness. The TeX keeps the printed reading; the "
         "corrected layer has $\\operatorname{char}k = 0$. 'corrected' replaces the 'tex' substring.",
))

F.append(dict(
    page=27,
    where="2.3.1, 1), 'on pose X'' = X'×_X S''",
    scan="X'' = X'×_X S'",
    tex=r"$X'' = X'\times_X S'$",
    kind="misprint_in_print",
    confidence="high",
    fix=None,
    corrected=r"$X'' = X'\times_X X'$",
    note="Descent along f : X' → X (SGA 1 IX 5.2, 5.3, cited on p. 28) uses X'' = X' ×_X X'; S', the blown-up "
         "surface of 2.1, has no place here. The S' is clear in the scan and in the DjVu witness. The TeX keeps "
         "the printed reading; the corrected layer has X' ×_X X'. 'corrected' replaces the 'tex' substring.",
))

F.append(dict(
    page=28,
    where="'soit f : ∐ U_i → X le morphisme canonique'",
    scan="coproduct sign typed as two bars standing on an underscore that runs past both bars (∐), the same "
         "glyph as in 'P^1 - U = ∐_{1⩽i⩽n} {t_i}' on p. 30",
    tex=r"$f : \bigsqcup U_i \longrightarrow X$",
    kind="symbol",
    confidence="medium",
    fix={"old": r"\bigsqcup U_i", "new": r"\coprod U_i"},
    note="The base stroke projecting beyond the two bars is the shape of ∐, not ⊔; the TeX writes the identical "
         "printed sign as \\coprod on p. 30 (and in Exposé IX).",
))

F.append(dict(
    page=29,
    where="first display, 'codim(X - ⋃_{1⩽i⩽n} {x_i}, X) ⩾ 2'",
    scan="codim(X- ⋃_{1⩽i⩽n} {x_i},X) ⩾ 2 ,",
    tex=r"\mathrm{codim}(X- \bigcup_{1\leqslant i\leqslant n} \{x_i\},X)",
    kind="misprint_in_print",
    confidence="medium",
    fix=None,
    corrected=r"\mathrm{codim}(\bigcup_{1\leqslant i\leqslant n} \{x_i\},X)",
    note="The extension of étale covers across the points x_i needs the removed set ⋃{x_i} to have codimension "
         "⩾ 2 in X; the dense open X - ⋃{x_i} (on which the next sentence restricts the cover) has codimension 0. "
         "The TeX keeps the printed reading; the corrected layer has codim(⋃{x_i}, X). 'corrected' replaces the "
         "'tex' substring.",
))

F.append(dict(
    page=29,
    where="proof of condition a), 'X'_Z = X'×_{P^1} Z vérifie la condition (S_2) aux points fermés de X''",
    scan="vérifie la condition (S_2) aux points fermés de X' et est régulier en tout autre point",
    tex=r"aux points fermés de $X'$ et est régulier",
    kind="misprint_in_print",
    confidence="low",
    fix=None,
    corrected=r"aux points fermés de $X'_Z$ et est régulier",
    note="(S_2) and regularity are asserted of the points of X'_Z (Serre's criterion then gives 'donc est "
         "normal'). Low because 'points fermés de X'' can be read as the points of X'_Z over closed points of X', "
         "which are exactly the closed points of X'_Z (X'_Z → X' is integral). Same in the DjVu witness. The TeX keeps the printed reading; "
         "the corrected layer has X'_Z. 'corrected' replaces the 'tex' substring.",
))

F.append(dict(
    page=30,
    where="first display, condition c)",
    scan="prof ét_T(S) ⩾ 2 ,",
    tex=r"\text{prof ét}_T(S)",
    kind="misprint_in_print",
    confidence="medium",
    fix=None,
    corrected=r"\text{prof ét}_T(P^1)",
    note="The sentence is about the base of h: 'Comme P^1 est normal et T = P^1 - U de codimension 1, on a ...'. "
         "S is the base's letter in SGA 1 XIII 4, but in this exposé S is the surface, which does not contain T. Same in the DjVu witness. "
         "The TeX keeps the printed reading; the corrected layer has P^1. 'corrected' replaces the 'tex' substring.",
))

F.append(dict(
    page=30,
    where="display after 'D'après loc. cit. (4.7.4), on a un isomorphisme'",
    scan="Π_1^{(p)}(X',a) ≃ Π_1^{(p)}(X'_η̄,a) . (no index K)",
    tex=r"\simeq \Pi_1^{(p)}(X'_{\bar{\eta}},a) \qquad .",
    kind="misprint_in_print",
    confidence="high",
    fix=None,
    corrected=r"\simeq \Pi_1^{(p)}(X'_{\bar{\eta}},a)_K \qquad .",
    note="The isomorphism is with the group of coinvariants defined just before: the page ends by deducing from the "
         "finite presentation of Π_1^{(p)}(X'_η̄,a)_K that of 'Π_1^{(p)}(X) qui lui est isomorphe'. No trace of a "
         "K in the scan or the DjVu witness. The TeX keeps the printed reading; the corrected layer has the index "
         "K. 'corrected' replaces the 'tex' substring.",
))

# checks: every fix's old occurs exactly once on its page; every 'tex' occurs on its page
ok = True
for e in F:
    t = (BATCH / f"page_{e['page']:03d}.tex").read_text(encoding="utf-8")
    if e["fix"] is not None:
        n = t.count(e["fix"]["old"])
        print(e["page"], "fix old count", n, repr(e["fix"]["old"]))
        ok &= (n == 1)
    m = t.count(e["tex"])
    print(e["page"], "tex count", m, repr(e["tex"][:60]))
    ok &= (m >= 1)
    if e["kind"] != "misprint_in_print":
        e.pop("corrected", None)
print("ALL OK" if ok else "PROBLEM")

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", OUT, len(F))
