"""Build findings_621_625.json and check that every fix's old string occurs exactly once in its page file.

usage: python -I build_findings.py
"""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
PAGES = RUN / "b621_625"
OUT = RUN / "findings_621_625.json"

M624 = "%%%%%%%%%%  scan idx 637  |  folio 624  %%%%%%%%%%"
M625 = "%%%%%%%%%%  scan idx 638  |  folio 625  %%%%%%%%%%"
M626 = "%%%%%%%%%%  scan idx 639  |  folio 626  %%%%%%%%%%"
IMP = r"\(\Rightarrow\)"
LANG = r"\(\langle c_1(L_1)\cdots c_1(L_s)\cdot Y\rangle\)"


def q(s):
    """Show a string with its line breaks as the two characters \\n, for the notes."""
    return s.replace("\n", "\\n")


F = []

# ---------------------------------------------------------------- page 621
F.append(dict(
    page=621, where="end of the proof of 1.8 (i), 'par récurrence sur s et h^0(F(-1)) ≤ b_0'",
    scan="par récurrence sur s et h^o(F(-1))≤b_o ; (no comma after s; both scans, crops_621_625/m621_sur_s.png)",
    tex=r"par récurrence sur \(s\), et \(h^0(F(-1))\le b_0\);",
    kind="punctuation", confidence="high",
    fix={"old": r"sur \(s\), et", "new": r"sur \(s\) et"},
    note="The TeX adds a comma the print does not have."))
F.append(dict(
    page=621, where="proof of 1.8 (ii), 'G est un (b_1,...,b_{s-1},a_s)-faisceau'",
    scan="(b_i,...,b_{s-1},a_s)-faisceau: the first index is a typed i with its dot and the short stem of i, not the "
         "flagged 1 of (b_1,...,b_r) on the first line of the page (both scans; crops_621_625/m621_b1.png, "
         "m621_b1_line1.png, w621_b1.png)",
    tex=r"\((b_1,\ldots,b_{s-1},a_s)\)-faisceau",
    kind="misprint_in_print", confidence="high",
    fix={"old": r"(b_1,\ldots,b_{s-1}", "new": r"(b_i,\ldots,b_{s-1}"},
    corrected=r"(b_1,\ldots,b_{s-1},a_s)",
    note="Typing error: G is a (b_1,...,b_r)-faisceau (first line of the page), so the sequence starts with b_1. "
         "The TeX silently corrects it."))
F.append(dict(
    page=621, where="Définition 1.9, first line of the cases display",
    scan="P_{-1} = 0 with nothing after it (both scans)",
    tex=r"P_{-1}=0,\\",
    kind="punctuation", confidence="high",
    fix={"old": r"P_{-1}=0,", "new": r"P_{-1}=0"},
    note="The TeX adds a comma at the end of the first line of the display; the second line ends with the printed "
         "full stop."))

# ---------------------------------------------------------------- page 622
F.append(dict(
    page=622, where="proof of 1.11, 'Par 1.7 et l'hypothèse de récurrence on voit que'",
    scan="Par 1.7 et l'hypothèse de récurrence on voit que si n = P_{r-1}(c_1,...,c_r), (no comma after "
         "récurrence; both scans)",
    tex=r"Par 1.7 et l'hypothèse de récurrence, on voit que",
    kind="punctuation", confidence="high",
    fix={"old": "récurrence, on voit", "new": "récurrence on voit"},
    note="The TeX adds a comma the print does not have."))
F.append(dict(
    page=622, where="proof of 1.11, 'par 1.8 (i) car b_i ≥ 0'",
    scan="par 1.8 (i) car b_i ≥ 0. (no comma; both scans)",
    tex=r"par 1.8 (i), car \(b_i\ge0\)",
    kind="punctuation", confidence="high",
    fix={"old": "par 1.8 (i), car", "new": "par 1.8 (i) car"},
    note="The TeX adds a comma the print does not have."))
F.append(dict(
    page=622, where="1.12, 'sur le schéma algébrique X_K et on dit'",
    scan="des faisceaux cohérents F_K sur le schéma algébrique X_K et / on dit qu'un F_K (no comma; both scans)",
    tex=r"sur le schéma algébrique \(X_K\), et on dit",
    kind="punctuation", confidence="high",
    fix={"old": r"\(X_K\), et on dit", "new": r"\(X_K\) et on dit"},
    note="The TeX adds a comma the print does not have."))
F.append(dict(
    page=622, where="1.12, 'sur X_T = X×_S T où T est de type fini'",
    scan="F sur X_T = Xx_S T où T est de type fini sur S, (no comma before où; both scans)",
    tex=r"\(X_T=X\times_S T\), où \(T\) est de type fini",
    kind="punctuation", confidence="high",
    fix={"old": r"X\times_S T\), où", "new": r"X\times_S T\) où"},
    note="The TeX adds a comma the print does not have."))
F.append(dict(
    page=622, where="1.12, 'des faisceaux F_{k(t)} avec t ∈ T'",
    scan="faisceaux F_{k(t)} avec t ∈ T ; (no comma; both scans)",
    tex=r"\(F_{k(t)}\), avec \(t\in T\);",
    kind="punctuation", confidence="high",
    fix={"old": r"\(F_{k(t)}\), avec", "new": r"\(F_{k(t)}\) avec"},
    note="The TeX adds a comma the print does not have."))
F.append(dict(
    page=622, where="last sentence, 'représentée par un F_K avec K algébriquement clos'",
    scan="représentée par un F_K avec K algébriquement clos, qui est un (b)-faisceau. (no comma after F_K; both "
         "scans)",
    tex=r"représentée par un \(F_K\), avec \(K\) algébriquement clos,",
    kind="punctuation", confidence="high",
    fix={"old": r"\(F_K\), avec", "new": r"\(F_K\) avec"},
    note="The TeX adds a comma the print does not have (the comma after 'clos' is printed)."))

# ---------------------------------------------------------------- page 624
old624 = "Alors, le\n" + M624 + "\nnombre des polynômes"
new624 = "Alors,\n" + M624 + "\nle nombre des polynômes"
F.append(dict(
    page=624, where="start of page (folio-624 marker)",
    scan="p. 624 begins 'le nombre des polynômes χ(F(n)) est au plus égal au nombre de composantes'; p. 623 ends "
         "'... on peut supposer F plat sur T. Alors,' (both scans: b621_625/page_623_s4.png, page_624_s1.png; "
         "crops_621_625/w_634_3.png, w_635_1.png)",
    tex=r"'le' ends the last line of page_623.tex ('... plat sur \(T\). Alors, le'), above the folio-624 marker; "
        "page_624.tex begins 'nombre des polynômes'",
    kind="marker", confidence="high", fix=None,
    note="The folio-624 marker stands one word late: page 624 really begins at 'le nombre des polynômes'. Exact edit "
         "in main.tex, both layers (the string occurs once in each; simulated in memory on both layers, "
         "crops_621_625/sim_markers.py): replace '" + q(old624) + "' by '" + q(new624) + "'. Equivalent: "
         "python -I move_marker.py 6 624 le --before (leaves 'le' on a line of its own)."))
F.append(dict(
    page=624, where="first paragraph, 'F_t est localement libre de rang p'",
    scan="F_t est localement libre derang p, (no word space between 'de' and 'rang': less than one typewriter cell; "
         "both scans, crops_621_625/m624_derang.png, w_635_1.png)",
    tex=r"\(F_t\) est localement libre de rang \(p\),",
    kind="misprint_in_print", confidence="low",
    fix={"old": "libre de rang", "new": "libre derang"},
    corrected="libre de rang",
    note="Typing slip: the word space after 'de' is missing; the TeX silently restores it. Low: drop it if a missing "
         "word space counts as spacing."))
F.append(dict(
    page=624, where="'L'implication (iii) ⟹ (iv) résulte de 1.3 (iii) en prenant M = max(χ(F_K(m)))'",
    scan="M = max(χ(F_K(m)) et E = O_X(-m)^{⊕M}. : three opening parentheses, only two closing ones after m (both "
         "scans; crops_621_625/m624_max.png, w_635_2.png)",
    tex=r"\(M=\max(\chi(F_K(m)))\)",
    kind="misprint_in_print", confidence="high",
    fix={"old": r"\max(\chi(F_K(m)))\)", "new": r"\max(\chi(F_K(m))\)"},
    corrected=r"\max(\chi(F_K(m)))",
    note="The print drops the closing parenthesis of max(...); the TeX silently adds it."))
comma_old = "par (i) " + IMP + " (iv),"
comma_new = "par (i) " + IMP + " (iv)"
F.append(dict(
    page=624, where="end of page_624.tex, 'En effet, par (i) ⟹ (iv), prenons' (these words are printed at the top "
                    "of p. 625)",
    scan="p. 625, line 1: 'par (i) ⟹ (iv) prenons une surjection L = ...' (no comma after (iv); both scans, "
         "b621_625/page_625_s1.png, crops_621_625/w_636_1.png)",
    tex=r"En effet, par (i) \(\Rightarrow\) (iv),",
    kind="punctuation", confidence="high",
    fix={"old": comma_old, "new": comma_new},
    note="The TeX adds a comma the print does not have. The words belong to p. 625 (marker finding of page 625): "
         "apply this fix before moving the folio-625 marker; after the move its old string is in page 625's span."))

# ---------------------------------------------------------------- page 625
old625 = "En effet, " + comma_new + "\n" + M625 + "\nprenons une surjection"
new625 = "En effet,\n" + M625 + "\n" + comma_new + " prenons une surjection"
F.append(dict(
    page=625, where="start of page (folio-625 marker)",
    scan="p. 625 begins 'par (i) ⟹ (iv) prenons une surjection L = O_{X_T}(-m)^{⊕M} → E. Quitte'; p. 624 ends "
         "'... de la forme O_X(-m)^{⊕M}. En effet,' (both scans: b621_625/page_624_s4.png, page_625_s1.png; "
         "crops_621_625/w_635_3.png, w_636_1.png)",
    tex=r"'par (i) \(\Rightarrow\) (iv),' ends the last line of page_624.tex ('... En effet, par (i) "
        r"\(\Rightarrow\) (iv),'), above the folio-625 marker; page_625.tex begins 'prenons une surjection'",
    kind="marker", confidence="high", fix=None,
    note="The folio-625 marker stands four words late: page 625 really begins at 'par (i) ⟹ (iv) prenons'. Apply "
         "the comma fix of page 624 first; then, in main.tex, both layers (once in each after that fix; simulated in "
         "memory, crops_621_625/sim_markers.py): replace '" + q(old625) + "' by '" + q(new625) + "'. In a layer that "
         "keeps the comma, the same edit with '(iv),' in both strings. Equivalent: python -I move_marker.py 6 625 "
         "'par (i)' --before (leaves 'par (i) ... (iv)' on a line of its own)."))
F.append(dict(
    page=625, where="'soit γ la composition L'_K → E'_K → E_K'",
    scan="soit γ la composition / L'_K → E'_K → E_K ; alors γ provient d'un homomorphisme δ : L_{1,K} → L_K, (both "
         "scans; crops_621_625/m625_comp.png)",
    tex=r"\(L'_K\to E'_K\to E_K\)",
    kind="misprint_in_print", confidence="medium",
    fix=None,
    corrected=r"L_{1,K}\to E'_K\to E_K",
    note="No L' is defined: the surjection onto E' is L_1 → E', and γ lifts to δ : L_{1,K} → L_K, so the composition "
         "starts at L_{1,K}. The TeX keeps the printed L'_K."))
F.append(dict(
    page=625, where="'et (δ, u_K∘α) : L_{1,K} ⊕ L_{2,K} → L_K'",
    scan="(δ,u_K∘α): a small composition circle between u_K and α (both scans; crops_621_625/m625_circ.png, "
         "m625_delta.png, w_636_2.png)",
    tex=r"$(\delta,u_K\alpha):L_{1,K}\oplus L_{2,K}\longrightarrow L_K$",
    kind="symbol", confidence="high",
    fix={"old": r"u_K\alpha", "new": r"u_K\circ\alpha"},
    note="The TeX drops the printed composition sign."))
HOM_NOTE = ("The print types Hom and underlines it (sheaf Hom; the subscript O_{X_T} is not underlined); the TeX writes "
            r"a script H. The volume writes the print's underlined Hom \underline{\Hom} (108 places in main.tex); "
            r"these three \mathcal H\!om on p. 625 are the only ones in the file.")
F.append(dict(
    page=625, where="'on peut supposer en plus que X_T (donc Hom_{O_{X_T}}(E',E))'",
    scan="(donc Hom_{O_{X_T}}(E',E)) with Hom underlined (both scans; crops_621_625/m625_hom.png)",
    tex=r"(donc \(\mathcal H\!om_{\mathcal O_{X_T}}(E',E)\))",
    kind="underline", confidence="high",
    fix={"old": r"(donc \(\mathcal H\!om", "new": r"(donc \(\underline{\Hom}"},
    note=HOM_NOTE))
F.append(dict(
    page=625, where="'et tous les R^q(f_T)_*Hom_{O_{X_T}}(E',E)'",
    scan="R^q(f_T)_*Hom_{O_{X_T}}(E',E) with Hom underlined (both scans; crops_621_625/m625_hom.png)",
    tex=r"\(R^q(f_T)_*\mathcal H\!om_{\mathcal O_{X_T}}(E',E)\)",
    kind="underline", confidence="high",
    fix={"old": r"R^q(f_T)_*\mathcal H\!om", "new": r"R^q(f_T)_*\underline{\Hom}"},
    note=HOM_NOTE))
F.append(dict(
    page=625, where="'afin que la formation de G=(f_T)_*Hom_{O_{X_T}}(E',E) commute'",
    scan="G=(f_T)_*Hom_{O_{X_T}}(E',E) with Hom underlined (both scans; b621_625/page_625_s3.png, w_636_2.png)",
    tex=r"\(G=(f_T)_*\mathcal H\!om_{\mathcal O_{X_T}}(E',E)\)",
    kind="underline", confidence="high",
    fix={"old": r"G=(f_T)_*\mathcal H\!om", "new": r"G=(f_T)_*\underline{\Hom}"},
    note=HOM_NOTE))
F.append(dict(
    page=625, where="'Soit R = V(G^*), alors X_R porte canoniquement'",
    scan="R = 𝕍(G^*): a double-struck V with a doubled left stroke (both scans; crops_621_625/m625_V.png, "
         "w_636_2.png)",
    tex=r"Soit $R=V(G^*)$, alors",
    kind="font", confidence="high",
    fix={"old": r"$R=V(G^*)$", "new": r"$R=\mathbb V(G^*)$"},
    note=r"The print's double-struck V (the vector-bundle functor of EGA) is a plain V in the TeX; the file writes "
         r"\mathbb V elsewhere (29 places)."))
old626 = "désigne par " + LANG + " le\n" + M626 + "\nnombre d'intersection"
new626 = "désigne par\n" + M626 + "\n" + LANG + " le nombre d'intersection"
F.append(dict(
    page=625, where="end of page (folio-626 marker)",
    scan="p. 625 ends '... de dimension ≤ s. Rappelons qu'on désigne par'; p. 626 begins '< c_1(L_1)...c_1(L_s).Y > "
         "le nombre d'intersection, qui peut être calculé' (main scan b621_625/page_625_s4.png; witness DjVu p. 637, "
         "crops_621_625/w626_top.png)",
    tex=r"page_625.tex ends 'Rappelons qu'on désigne par \(\langle c_1(L_1)\cdots c_1(L_s)\cdot Y\rangle\) le' "
        "above the folio-626 marker; the text under the folio-626 marker begins 'nombre d'intersection'",
    kind="marker", confidence="high", fix=None,
    note="The folio-626 marker stands one formula and one word late: page 626 really begins at '⟨c_1(L_1)...⟩ le "
         "nombre d'intersection'. Same boundary as the start of page 626 (batch 626-630): apply once. Exact edit in "
         "main.tex, both layers (once in each; simulated in memory, crops_621_625/sim_markers.py): replace '"
         + q(old626) + "' by '" + q(new626) + "'. Equivalent: python -I move_marker.py 6 626 "
         r"'\(\langle c_1(L_1)' --before. The moved formula reads as in the witness apart from the typewriter's "
         r"< >, ... and . for \langle \rangle, \cdots, \cdot; its check belongs to page 626."))

# ---------------------------------------------------------------- checks
bad = 0
for f in F:
    fx = f.get("fix")
    if not fx:
        continue
    t = (PAGES / f"page_{f['page']}.tex").read_text(encoding="utf-8")
    n = t.count(fx["old"])
    if n != 1 or "%%%%%%%%%%" in fx["old"] or fx["old"] == fx["new"]:
        bad += 1
        print("BAD", f["page"], repr(fx["old"]), n)
for f in F:
    if f["kind"] == "misprint_in_print" and "corrected" not in f:
        bad += 1
        print("misprint without corrected", f["page"], f["where"])
    if f["kind"] != "misprint_in_print" and "corrected" in f:
        bad += 1
        print("corrected on a non-misprint", f["page"], f["where"])
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
counts = {}
for f in F:
    c = counts.setdefault(f["page"], [0, 0])
    c[1 if f["kind"] == "misprint_in_print" else 0] += 1
print("written", OUT, len(F), "findings; bad:", bad)
print({p: f"{a}/{b}" for p, (a, b) in sorted(counts.items())})
