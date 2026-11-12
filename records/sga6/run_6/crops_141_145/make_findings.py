"""Build findings_141_145.json, check every fix's old occurs exactly once in its page file and that the fixes apply
in JSON order; simulate the p. 143/144 edits with the folio-144 marker move in memory. Writes only the JSON."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b141_145"
OUT = RUN / "findings_141_145.json"
NL = "\n"

OLD_A = (r"Soient \(S\) une catégorie, \(\mathcal C\) une \(S\)-catégorie additive (resp. triangulée) (1.1.1), "
         r"\(F\) un préfaisceau abélien sur \(S\). On dit qu'une famille de fonctions "
         r"\(f_X:\Ob(\mathcal C_X)\longrightarrow F(X)\) indexée par \(X\in\Ob S\) est une \(S\)-fonction additive "
         r"de \(\mathcal C\) dans \(F\) si les conditions suivantes sont réalisées")
OLD_B = r"pour tout \(X\in\Ob\mathcal C_X\), \(f_X\) est une fonction additive"
OLD_C = r"pour toute flèche \(u:X\to Y\) de \(S\), le diagramme suivant est commutatif"
OLD_D = r"Les \(S\)-fonctions additives de \(\mathcal C\) dans \(F\) forment un groupe abélien, noté"
OLD_E = (r"Soient \(S\) un site, \(\mathcal C\) une \(S\)-catégorie abélienne plate, \(\mathcal C_0\) une "
         r"sous-\(S\)-catégorie additive strictement pleine de \(\mathcal C\) satisfaisant aux hypothèses (4.0). "
         r"Alors le morphisme de préfaisceaux")
BODY_F = (r"induit par l'inclusion de \(\mathcal C_0\) dans \(\Parf(\mathcal C,\mathcal C_0)\), définit un "
          r"isomorphisme sur les faisceaux associés. En d'autres termes, pour tout faisceau abélien \(F\) sur \(S\),")
OLD_F = BODY_F + r" l'%"
NEW_F = r"\emph{" + BODY_F + "}" + NL + r"\emph{l'}%"


def em(s):
    return r"\emph{" + s + "}"


F = []


def add(**kw):
    F.append(kw)


# ---------------------------------------------------------------- p. 141
add(page=141, where="start of page",
    scan="p. 141 begins '6.2. Soient C une catégorie triangulée'; p. 140 ends '... forment un groupe abélien, noté "
         "Add(C,F).' (both scans)",
    tex=r"\textbf{6.2.} is the last line of page_140.tex (under the folio-140 marker); page_141.tex begins 'Soient'",
    kind="marker", confidence="high", fix=None,
    note="Page 141 really begins with the heading 6.2. Move the folio-141 marker above it: python -I move_marker.py 6 "
         r"""141 "\textbf{6.2.}" --before (simulated on both layers: '... noté \(\Add(\mathcal C,F)\).', blank line, """
         r"the marker, '\textbf{6.2.}', 'Soient ...').")
add(page=141, where="(6.4.1)",
    scan="f(L) = Σ(-1)^i f(L^i): a bare hand-drawn sum sign, nothing under it (both scans; "
         "crops_141_145/p141_sum.png, w141_sum.png)",
    tex=r"f(L)=\sum_i (-1)^i f(L^i)", kind="formula", confidence="high",
    fix={"old": r"\sum_i (-1)^i", "new": r"\sum (-1)^i"},
    note="The TeX adds the summation index.")
add(page=141, where="6.3, 'Le foncteur Add(C,.) est représentable'",
    scan="Add(C,.): the empty argument is the typewriter's full stop, low on the line like the stops of '6.3.' "
         "(both scans; crops_141_145/p141_addcdot.png)",
    tex=r"\Add(\mathcal C,\cdot)", kind="symbol", confidence="low",
    fix={"old": r"\Add(\mathcal C,\cdot)", "new": r"\Add(\mathcal C,.)"},
    note=r"Low: perhaps a typewriter substitute for the centred dot; p. 89 kept \Hom(P,\cdot) for the typed "
         "'(P,.)'. One decision for both.")
add(page=141, where="§§6.2-6.4 throughout (also Définition 6.1 on p. 140 and the first line of p. 142)",
    scan="the category letter is a plain typed C, neither underlined nor double-struck: 'Soient C une catégorie "
         "triangulée', 'Add(C,F) ⊂ Add(C^ad,F)', 'cl_C : ob(C) → k(C)', 'u, u' : C → D', Lemme 6.4 'Soit C une "
         "catégorie additive' (C left out of the statement's underline). From Définition 6.5 (p. 142) the "
         "S-categories are underlined C̲ (both scans)",
    tex=r"\mathcal C (and \mathcal D) throughout", kind="font", confidence="high", fix=None,
    note=r"Convention, not a page fix: the print sets plain C for the ordinary additive or triangulated categories "
         r"of §§6.1-6.4 and underlined C̲ for the S-categories from 6.5 on; the TeX writes \mathcal C for both (36 "
         r"times on p. 141, footnote included, \mathcal D once, and twice in the first line of p. 142). Decide with the pending category-letter decision.")

# ---------------------------------------------------------------- p. 142
add(page=142, where="Définition 6.5, first paragraph",
    scan="underlined by word groups from 'Soient' to 'si les conditions suivantes sont réalisées' (S̲, C̲, C̲_X "
         "with their own underlines; '(1.1.1),', F, 'f_X : ob(C_X) → F(X)' and 'X ∈ ob' outside); ' :' not "
         "underlined (both scans)",
    tex=r"no emphasis: the definition is in roman (Lemme 6.4 on p. 141 has \emph)",
    kind="underline", confidence="high", fix={"old": OLD_A, "new": em(OLD_A)},
    note="Missing underline of the statement (block emphasis, as Lemme 6.4). Items (i), (ii) and the closing "
         "sentence follow as separate entries.")
add(page=142, where="Définition 6.5 (i)",
    scan="'pour tout' and 'est une fonction additive' underlined; '(6.1) ;' not (both scans)",
    tex="no emphasis", kind="underline", confidence="high", fix={"old": OLD_B, "new": em(OLD_B)},
    note="Part of the definition (see the first entry); the reference stays in roman. For the printed 'X ∈ ob C_X' "
         "see the misprint entry (fix null, no conflict).")
add(page=142, where="Définition 6.5 (ii)",
    scan="'pour toute flèche', 'de S̲,', 'le diagramme suivant est commutatif' underlined (both scans)",
    tex="no emphasis", kind="underline", confidence="high", fix={"old": OLD_C, "new": em(OLD_C)},
    note="Part of the definition.")
add(page=142, where="Définition 6.5, closing sentence 'Les S-fonctions additives de C dans F forment un groupe "
                    "abélien, noté Add_S(C,F).'",
    scan="underlined by word groups from 'Les' to 'noté'; 'Add_S(C,F).' not (only S̲ and C̲ carry their own "
         "underlines) (both scans)",
    tex="no emphasis", kind="underline", confidence="high", fix={"old": OLD_D, "new": em(OLD_D)},
    note="End of the definition (as the closing sentence of Définition 6.1, p. 140).")
add(page=142, where="Définition 6.5 (i), 'pour tout X ∈ ob C_X'",
    scan="pour tout X ∈ ob C̲_X , f_X est une fonction additive (6.1) ; (both scans)",
    tex=r"pour tout \(X\in\Ob\mathcal C_X\) (printed reading kept)",
    kind="misprint_in_print", confidence="high", fix=None, corrected=r"pour tout \(X\in\Ob S\)",
    note="The family f_X is indexed by X ∈ ob S̲ and X is the base of the fibre C_X, so 'X ∈ ob C_X' cannot be meant. "
         "The TeX keeps the printed reading.")
add(page=142, where="Définition 6.5 (ii), the square: bottom arrow f_X : ob C_X → F(X)",
    scan="a plain line without arrowhead under the label f_X; the top arrow f_Y has its head (both scans; "
         "crops_141_145/p142_diag.png, w142_small.png)",
    tex=r'\arrow[r,"f_X"] (with a head)',
    kind="misprint_in_print", confidence="medium",
    fix={"old": r'\arrow[r,"f_X"]', "new": r'\arrow[r,"f_X",dash]'}, corrected=r'\arrow[r,"f_X"]',
    note="The head was not drawn; the TeX silently supplies it. dash is tikz-cd's key for a line without tips.")
add(page=142, where="pp. 142-145 throughout: the base S̲",
    scan="S underlined where it names the base category, site or topos: p. 142 'Soient S̲ une catégorie', "
         "'X ∈ ob S̲', 'u ∈ Fl(S̲)'; p. 143 'Soient S̲ un site', 'préfaisceau abélien sur S̲'; p. 144 'faisceau "
         "abélien sur S̲'; p. 145 '(S̲,A) un topos annelé', 'u : (S̲',A') → (S̲,A)'; also the index of Add_S̲ and "
         "Cart_S̲ (both scans)",
    tex=r"plain \(S\): 'Soient \(S\) une catégorie', '\(X\in\Ob S\)', '\((S,A)\) un topos annelé', \Add_S",
    kind="underline", confidence="high", fix=None,
    note="Convention of the transcription, as reported for pp. 84-100: one decision for the exposé, not a page fix.")
add(page=142, where=r"pp. 142-144: all 12 uses of \Cart",
    scan="Cart̲_S: the name Cart carries its own underline (apart from the S̲ under it) in text and displays: "
         "p. 142 'Cart̲_S(C^is,F̲) (resp. Cart̲_S(Tr(C)^is,F̲) (1.1.2))'; p. 143 the display of 6.6 a), the two "
         "in the text and (6.6.1); p. 144 the four of the diagram. Add and Tr are not underlined (both scans)",
    tex=r"\Cart_S(...), \Cart defined as \operatorname{Cart} (main.tex line 2851; again 3407): no underline",
    kind="underline", confidence="high", fix=None,
    note=r"Convention of the transcription: \Cart is used only on pp. 142-144, 12 times, all underlined in the "
         r"print. One edit covers them: line 2851 \providecommand{\Cart}{\operatorname{Cart}} -> "
         r"\providecommand{\Cart}{\underline{\operatorname{Cart}}} (the \providecommand of line 3407 then does "
         r"nothing); or \underline{\Cart}_S at each use.")

# ---------------------------------------------------------------- p. 143
RHO_NOTE = (r"The same letter four times on this page (display, \rho(f)(T), \rho(f)=0, the arrow of (6.6.1)): apply "
            r"the four edits together. \phi as for the closed phi of pp. 3 and 12.")
add(page=143, where="6.6 a), display 'φ : Cart_S(C^is,F) → Cart_S(Tr(C)^is,F) ,' (\\rho in the TeX)",
    scan="the map's letter is a hand-drawn closed phi: a small loop crossed by one slanted stroke that rises well "
         "above the loop (ascender height) and ends below it; a rho has no stroke above its bowl (both scans; "
         "crops_141_145/p143_rho_big.png, w143_rho.png, p143_661_arrow.png)",
    tex=r"\rho:\Cart_S", kind="symbol", confidence="medium",
    fix={"old": r"\rho:\Cart_S", "new": r"\phi:\Cart_S"}, note=RHO_NOTE)
add(page=143, where="6.6 a), 'défini par φ(f)(T) = f(L) - f(L') - f(L\")'",
    scan="the same closed phi (both scans)", tex=r"\rho(f)(T)", kind="symbol", confidence="medium",
    fix={"old": r"\rho(f)(T)", "new": r"\phi(f)(T)"}, note=RHO_NOTE)
add(page=143, where="6.6 a), 'additif signifie que φ(f) = 0'",
    scan="the same closed phi (both scans)", tex=r"\rho(f)=0", kind="symbol", confidence="medium",
    fix={"old": r"\rho(f)=0", "new": r"\phi(f)=0"}, note=RHO_NOTE)
add(page=143, where="(6.6.1), label of the third arrow",
    scan="the same closed phi over the arrow (both scans)", tex=r"\xrightarrow{\rho}", kind="symbol",
    confidence="medium", fix={"old": r"\xrightarrow{\rho}", "new": r"\xrightarrow{\phi}"}, note=RHO_NOTE)
add(page=143, where="6.6 a), 'pour f ∈ Cart_S(C^is,F) et T = ...'",
    scan="Cart̲_S(C̲^is,F) et: this F has no underline (both scans; crops_141_145/w143_pourF.png), while the same "
         "expression a line below ('Dire que f ∈ Cart̲_S(C̲^is,F̲)'), the display above and (6.6.1) have F̲",
    tex=r"\(f\in\Cart_S(\mathcal C^{\is},\underline F)\) et (silently corrected)",
    kind="misprint_in_print", confidence="high",
    fix={"old": r"\underline F)\) et", "new": r"F)\) et"}, corrected=r"\underline F)\) et",
    note="The typist left out the underline of the fibred category F̲ once.")
add(page=143, where="Proposition 6.7, statement before the display",
    scan="underlined by word groups from 'Soient' to 'Alors le morphisme de préfaisceaux' (S̲, C̲, C̲_o with their "
         "own underlines; '(4.0).' not underlined) (both scans)",
    tex="no emphasis: the statement is in roman", kind="underline", confidence="high",
    fix={"old": OLD_E, "new": em(OLD_E)},
    note="Missing underline of the statement, as Définition 6.5 (p. 142). It goes on after the display (next entry) "
         "and on p. 144.")
add(page=143, where="Proposition 6.7 after the display, 'induit par l'inclusion ... pour tout faisceau abélien F sur S,'",
    scan="underlined by word groups ('induit par l'inclusion de', 'dans Parf', 'définit un isomorphisme sur les', "
         "'faisceaux associés.', 'En d'autres termes,', 'pour tout faisceau abélien', 'sur'); p. 143 ends 'sur S̲,' "
         "and the next words 'l'homomorphisme de restriction' (underlined) open p. 144 (both scans)",
    tex=r"no emphasis; the line ends 'sur \(S\), l'%', whose l' is printed on p. 144",
    kind="underline", confidence="high", fix={"old": OLD_F, "new": NEW_F},
    note=r"Closes the group at the end of p. 143 and gives the l' of p. 144 an \emph of its own on its own line, so "
         r"that the folio-144 marker can stand between them (marker entry of p. 144: apply this edit first). With "
         r"the p. 144 entries the output reads '... sur S, l'homomorphisme de restriction', emphasised throughout.")

# ---------------------------------------------------------------- p. 144
add(page=144, where="start of page",
    scan="p. 144 begins 'l'homomorphisme de restriction'; p. 143 ends '... pour tout faisceau abélien F sur S̲,' "
         "(both scans)",
    tex="'l'%' ends the last line of page_143.tex (under the folio-143 marker); page_144.tex begins "
        "'homomorphisme de restriction'",
    kind="marker", confidence="high", fix=None,
    note=r"Page 144 really begins with l'. After the p. 143 underline edit (which sets '\emph{l'}%' on a line of its "
         r"""own): python -I move_marker.py 6 144 "\emph{l'}%" --before. Without that edit: python -I """
         r"""move_marker.py 6 144 "l'%" --before. Both simulated on both layers: the marker goes between 'sur """
         r"\(S\),' and the l' line, whose % joins l' to 'homomorphisme' across the marker.")
add(page=144, where="Proposition 6.7, end of the statement: 'l'homomorphisme de restriction'",
    scan="underlined (both scans)", tex="no emphasis", kind="underline", confidence="high",
    fix={"old": "homomorphisme de restriction", "new": em("homomorphisme de restriction")},
    note=r"Continues the p. 143 entries (the l' gets its own \emph there).")
add(page=144, where="Proposition 6.7, 'est un isomorphisme.' after the display",
    scan="'est un isomorphisme' underlined, the full stop not (both scans)", tex="no emphasis", kind="underline",
    confidence="high",
    fix={"old": "est un isomorphisme." + NL + NL + r"\emph{Preuve.}",
         "new": em("est un isomorphisme") + "." + NL + NL + r"\emph{Preuve.}"},
    note="End of the statement.")
add(page=144, where="label 'Remarque 6.7.1. (cf.4.10.1).'",
    scan="a full stop after the number 6.7.1 (both scans; crops_141_145/p144_rem.png)",
    tex=r"\textbf{Remarque 6.7.1} (cf. 4.10.1).", kind="punctuation", confidence="high",
    fix={"old": r"\textbf{Remarque 6.7.1}", "new": r"\textbf{Remarque 6.7.1.}"},
    note="The TeX drops the label's full stop.")
add(page=144, where="end of the proof, 'Il en est donc de même de a, cqfd.'",
    scan="on a new line at the left margin after the short line '... sont des isomorphismes.' (both scans), like "
         "'Considérons le diagramme' above, which the TeX sets as a new paragraph",
    tex=r"'... sont des isomorphismes. Il en est donc de même de \(a\), cqfd.' in one paragraph",
    kind="other", confidence="medium",
    fix={"old": "isomorphismes. Il en est donc", "new": "isomorphismes." + NL + NL + "Il en est donc"},
    note="Missing paragraph break.")

# ---------------------------------------------------------------- p. 145
add(page=145, where="start of page",
    scan="p. 145 begins '6.8. Soient (S,A) un topos annelé'; p. 144 ends with Remarque 6.7.1 '... (* = - ou b).' "
         "(both scans)",
    tex=r"\textbf{6.8.} is the last line of page_144.tex (under the folio-144 marker); page_145.tex begins 'Soient'",
    kind="marker", confidence="high", fix=None,
    note=r"Page 145 really begins with the heading 6.8. Move the folio-145 marker above it: python -I "
         r"""move_marker.py 6 145 "\textbf{6.8.}" --before (simulated on both layers).""")
add(page=145, where="end of page",
    scan="p. 145 ends with the display k(C_1) → k(C_o) → k(D^-(S)_parf) → k(Parf(S)); p. 146 begins '(les deux "
         "de gauche étant des homomorphismes' (witness DjVu p. 157, OCR of p. 146)",
    tex="page_145.tex ends with the line '(les', which belongs to p. 146",
    kind="marker", confidence="high", fix=None,
    note=r"""Move the folio-146 marker above '(les': python -I move_marker.py 6 146 "(les" --before (simulated on """
         r"both layers: '\]', the marker, '(les', 'deux de gauche ...').")
add(page=145, where="6.8, 'induites par le foncteur Lu* (cf. (4.19.1))'",
    scan="double-struck L (an L with a doubled stem): 𝕃u* (both scans; crops_141_145/p145_Lu.png)",
    tex=r"\(\mathrm L u^*\)", kind="font", confidence="high",
    fix={"old": r"\mathrm L u^*", "new": r"\mathbb L u^*"},
    note=r"The L over the tensor sign in the next sentence is a plain typed L (\overset{\mathrm L}{\otimes} is right).")
add(page=145, where="6.8, the square of k(C_o) and k(D^-(_A S)_parf), bottom-right entry",
    scan="no punctuation after k(D^-(_{A'}S')_parf) (both scans)",
    tex=r"k(\Dpx^-({}_{A'} S')_{\mathrm{parf}}),", kind="punctuation", confidence="high",
    fix={"old": r"S')_{\mathrm{parf}}),", "new": r"S')_{\mathrm{parf}})"},
    note="The TeX adds a comma at the end of the diagram.")

# ---------------------------------------------------------------- checks
ok = True
pages = {p: (B / f"page_{p}.tex").read_text(encoding="utf-8") for p in range(141, 146)}
work = dict(pages)
for i, f in enumerate(F):
    fx = f.get("fix")
    if not fx:
        continue
    p, old, new = f["page"], fx["old"], fx["new"]
    n = pages[p].count(old)
    if n != 1:
        ok = False
        print("NOT UNIQUE in original", i, p, n, repr(old[:60]))
    if "%%%%%%%%%%  scan idx" in old:
        ok = False
        print("crosses marker", i)
    n2 = work[p].count(old)
    if n2 != 1:
        ok = False
        print("NOT UNIQUE at application", i, p, n2, repr(old[:60]))
    else:
        work[p] = work[p].replace(old, new)
for p in pages:  # brace balance per page after all fixes
    t = work[p].replace(r"\{", "").replace(r"\}", "")
    print(p, "braces", t.count("{") - t.count("}"),
          "orig", pages[p].replace(r"\{", "").replace(r"\}", "").count("{")
          - pages[p].replace(r"\{", "").replace(r"\}", "").count("}"))
print("all olds unique and applicable:", ok)
cnt = {}
for f in F:
    k = "m" if f["kind"] == "misprint_in_print" else "n"
    cnt.setdefault(f["page"], {"n": 0, "m": 0})[k] += 1
print(cnt)
# simulate p. 143 F edit + marker move with the new anchor (end of p. 143 / start of p. 144)
seam = work[143].rstrip("\n").split("\n")[-2:] + ["<marker 144>"] + work[144].split("\n")[2:5]
print("\n".join(seam))
if ok:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("written", OUT, len(F))
