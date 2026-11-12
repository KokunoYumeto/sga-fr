import json

OUT = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II\findings_026_030.json"

F = []

def add(**kw):
    d = {
        "page": kw["page"],
        "where": kw["where"],
        "scan": kw["scan"],
        "tex": kw["tex"],
        "kind": kw["kind"],
        "confidence": kw["confidence"],
        "fix": kw.get("fix"),
    }
    if kw["kind"] == "misprint_in_print":
        d["corrected"] = kw["corrected"]
    d["note"] = kw["note"]
    F.append(d)

# ---------------- page 26 ----------------
add(page=26,
    where="display after 'Enfin, 2.14 (ii) fournit', left-hand side",
    scan="lg_{k(s)} (D∩ Spec (O_S/I(ν)) = ν(s) + ...: three parentheses opened, two closed",
    tex=r"(D \cap \mathrm{Spec}\ (\underline{O}_S/I(\nu)) =",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"(D \cap \mathrm{Spec}\ (\underline{O}_S/I(\nu))) =",
    note="The parenthesis opened after lg_{k(s)} is never closed in the print. The TeX keeps the printed reading.")

add(page=26,
    where="display after 'soit par (2.14.4) appliqué à D'', left-hand side",
    scan="χ(D∩ Spec(O_S/I(ν)) = : three parentheses opened, two closed",
    tex=r"\chi(D \cap \mathrm{Spec}(\underline{O}_S/I(\nu)) &=",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"\chi(D \cap \mathrm{Spec}(\underline{O}_S/I(\nu))) &=",
    note="Same unclosed parenthesis as in (2.14.4) on page 25. The TeX keeps the printed reading.")

add(page=26,
    where="same display, first line, the sum after ν(s) [k(s) : k]",
    scan="+ Σ_{t sur D} ν(t) [k(t) : k]: no prime on D (the second line also reads 't sur D')",
    tex=r"[k(s) : k] + \sum_{t\ \mathrm{sur}\ D}",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"[k(s) : k] + \sum_{t\ \mathrm{sur}\ D'}",
    note="The first line applies (2.14.4) to D' ('soit par (2.14.4) appliqué à D''): lg_{k(s)}(D∩Spec(O_S/I(ν))) = ν(s) + lg_{k(s)}(D'∩T) and χ(D'∩T) = Σ_{t sur D'} ν(t)[k(t):k]. The points of S* other than s that lie on D are those lying on D', so adding the term of s gives the second line, the sum over t sur D. As printed, the same sum stands on both sides and the equality would force ν(s) = 0, whereas ν(s) > 0 in this step of the induction. The TeX keeps the printed reading.")

add(page=26,
    where="same display, end of the second line",
    scan="= Σ_{t sur D} ν(t) [k(t) : k]   .",
    tex=r"&= \sum_{t\ \mathrm{sur}\ D} \nu(t)\ [k(t) : k]",
    kind="punctuation", confidence="high",
    fix={"old": r"&= \sum_{t\ \mathrm{sur}\ D} \nu(t)\ [k(t) : k]",
         "new": r"&= \sum_{t\ \mathrm{sur}\ D} \nu(t)\ [k(t) : k] \quad ."},
    note="The full stop printed after the formula is missing in the TeX.")

add(page=26,
    where="start of the paragraph 'Des bribes de ce qui précèdent ...'",
    scan="(2.15) Des bribes de ce qui précèdent se généralisent en dimension supérieure.",
    tex="Des bribes de ce qui précèdent se généralisent",
    kind="number", confidence="high",
    fix={"old": "Des bribes de ce qui", "new": "(2.15) Des bribes de ce qui"},
    note="The paragraph number (2.15) is missing. The TeX keeps the other paragraph numbers ((2.22) on page 28, (2.25) on page 30), and 2.15 is cited on page 30 ('(2.4 et 2.15)').")

add(page=26,
    where="first sentence of 2.15",
    scan="Des bribes de ce qui précèdent se généralisent",
    tex="ce qui précèdent se généralisent",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected="ce qui précède se généralisent",
    note="Agreement slip: the subject of the verb is 'ce' ('ce qui précède'). The TeX keeps the printed reading.")

add(page=26,
    where="display S* = lim Irr(f^{-1}(s), index under lim",
    scan="s'∈ I: a small s (x-height, lower than the capital I beside it and than the S of S*)",
    tex=r"\varinjlim_{S' \in I}",
    kind="misprint_in_print", confidence="high",
    fix={"old": r"\varinjlim_{S' \in I}", "new": r"\varinjlim_{s' \in I}"},
    corrected=r"\varinjlim_{S' \in I}",
    note="The limit runs over the schemes S' of the set I just defined ('l'ensemble I des schémas f : S' → S'); the typist struck a small s. The TeX silently corrects the misprint.")

add(page=26,
    where="same display, Irr(f^{-1}(s)",
    scan="Irr(f^{-1}(s): two parentheses opened, one closed",
    tex=r"\mathrm{Irr}(f^{-1}(s)",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"\mathrm{Irr}(f^{-1}(s))",
    note="Unclosed parenthesis in the print. The TeX keeps the printed reading.")

# ---------------- page 27 ----------------
add(page=27,
    where="(2.18), degree in the sum",
    scan="μ_t(E) = Σ_{t' proche de t} μ_{t'}(E) [k(t') : k]   .",
    tex=r"\mu_{t'}(E) \, [k(t') : k]",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"\mu_{t'}(E) \, [k(t') : k(t)]",
    note="(2.18) is obtained 'comme en 2.11', whose part (i) reads μ_t(D) = Σ_{t' proche de t} μ_{t'}(D)[k(t'):k(t)] (page 19); μ_t is the Samuel multiplicity (2.7, 2.8) and does not involve k. With [k(t'):k] the formula fails as soon as k(t) ≠ k: for E regular at s with [k(s):k] = 2, μ_s(E) = 1, while the only point proche de s on E is the point t' of E'∩s*, rational over k(s), giving 1·[k(t'):k] = 2. The TeX keeps the printed reading.")

add(page=27,
    where="2.19, second paragraph, 'on désigne par S_i la surface correspondantes'",
    scan="la surface correspondantes",
    tex="la surface correspondantes",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected="la surface correspondante",
    note="Agreement slip (singular noun). The TeX keeps the printed reading.")

# ---------------- page 29 ----------------
add(page=29,
    where="Exemple 2.23, '... en chaque point t ∈ S*, et un invariant birationnel de S'",
    scan="et un invariant (no s; one space between 'et' and 'un')",
    tex="et un invariant birationnel de $S$",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected="est un invariant birationnel de $S$",
    note="Typing slip for 'est': the sheaf affected with these multiplicities is a birational invariant. The TeX keeps the printed reading.")

add(page=29,
    where="Exemple 2.24, 'la \"courbe généralisée\" de coïncidences'",
    scan="coîncidences: the mark over the i is a single peak (circumflex), not the two dots of a diaeresis",
    tex="coïncidences",
    kind="misprint_in_print", confidence="medium",
    fix={"old": "coïncidences", "new": "coîncidences"},
    corrected="coïncidences",
    note="Accent slip of the typescript (î for ï). The TeX silently corrects it.")

add(page=29,
    where="last sentence, 'Cette \"courbe généralisée\" à un support'",
    scan="à un support (grave accent)",
    tex="à un support",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected="a un support",
    note="The verb avoir is meant. The TeX keeps the printed reading.")

add(page=29,
    where="last sentence, '... contenu dans le fermé de S_2 où f n'est pas étale'",
    scan="le fermé de S_2",
    tex="dans le fermé de $S_2$",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected="dans le fermé de $S_1$",
    note="𝔡*(f) = Ω²_{S_1/k}* - f*Ω²_{S_2/k}* is a generalized curve on S_1 (𝔡(f) is a divisor on S_1), so its support is a subset of S_1: the closed set of S_1 where f is not étale (at a point t where f is étale the terms t* and f*(f(t)*) cancel, since blowing up commutes with étale maps). A closed set of S_2 cannot contain it. The TeX keeps the printed reading.")

# ---------------- page 30 ----------------
add(page=30,
    where="2.25, first sentence, 'l'espace affine à n dimension sur k'",
    scan="à n dimension sur k (one space between 'dimension' and 'sur')",
    tex="à $n$ dimension sur",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected="à $n$ dimensions sur",
    note="Missing plural s. The TeX keeps the printed reading.")

add(page=30,
    where="table, header row",
    scan="Dessin   équation   δ   diagramme (avec multiplicités): plain typescript, small é and small d, no underline",
    tex=r"\textit{Dessin} & \textit{Équation} & $\delta$ & \textit{Diagramme (avec multiplicités)}",
    kind="word", confidence="high",
    fix={"old": r"\textit{Dessin} & \textit{Équation} & $\delta$ & \textit{Diagramme (avec multiplicités)}",
         "new": r"Dessin & équation & $\delta$ & diagramme (avec multiplicités)"},
    note="The TeX capitalizes 'Équation' and 'Diagramme', which the print writes with small letters, and sets the headings in italics, which the print does not have.")

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write("\n")
print(len(F), "findings written")
