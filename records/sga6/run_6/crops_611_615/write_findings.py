"""Write findings_611_615.json and check that every fix's old string occurs exactly once on its page."""
import json
import pathlib

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
PAGES = RUN / "b611_615"
OUT = RUN / "findings_611_615.json"
C = "crops_611_615/"

F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": confidence, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- p. 611
add(611,
    "statements of Lemme 4.2 (p. 611), Lemme 4.3 with its items 1)-5) (p. 612), Lemme 4.4 with 'pour' in its "
    "display (p. 613), Lemmes 4.5 and 4.6 (p. 614)",
    "underlined word group by word group (both scans), e.g. Lemme 4.2: 'Sous les conditions de', 'est un morphisme "
    "de descente pour', 'la catégorie des faisceaux localement libres', 'c'est-à-dire pour tout couple', 'de "
    "faisceaux localement libres sur', 'le diagramme', 'est exact'; the letters, formulas and most punctuation not "
    "underlined",
    "all five statements in roman (only the bold labels, accepted as typesetting)",
    "underline", "high", None,
    "Convention of the Exposé XII TeX, the same pattern as Exposé II (GLOBAL_ISSUES 82): pending volume decision, "
    "not itemized.")
add(611,
    "'En effet, si N = Hom_{O_Y}(L,M), on doit montrer que la suite'",
    "Hom underlined (both scans): the sheaf Hom; the three Hom of the display in Lemme 4.2 (global Hom) are plain, "
    "as in the TeX",
    r"N=\Hom_{\mathcal O_Y}(L,M) with plain Hom (\Hom is \operatorname{Hom})",
    "underline", "high",
    {"old": r"N=\Hom_{\mathcal O_Y}", "new": r"N=\underline{\Hom}_{\mathcal O_Y}"},
    r"The file writes the underlined Hom as \underline{\Hom} elsewhere.")
add(611,
    "display after 'on doit montrer que la suite'",
    "'Γ Y,N) → Γ(X,f^*N) ⇉ Γ(X×_Y X,g^*N)': no opening parenthesis after the first Γ (both scans; "
    + C + "c611_gamma.png)",
    r"\Gamma\ Y,N)\longrightarrow\Gamma(X,f^*N)",
    "misprint_in_print", "high", None,
    "The TeX keeps the printed reading; the current layer has \\Gamma(Y,N).",
    corrected=r"\Gamma(Y,N)")
add(611,
    "'et la catégoire Deff(S) des données de descente effectives'",
    "catégoire (both scans; " + C + "b611_3.png)",
    r"la catégoire \(\mathrm{Deff}(S)\)",
    "misprint_in_print", "high", None,
    "The TeX keeps the printed reading; the current layer has 'catégorie'.",
    corrected="catégorie")
add(611,
    "'Mais c'est précisément l'ensemble Z(S) de S-points de l'image réciproque'",
    "'l'ensemble Z(S) de S-points' (both scans; " + C + "c611_des.png)",
    r"l'ensemble \(Z(S)\) des \(S\)-points",
    "misprint_in_print", "high",
    {"old": r"des \(S\)-points", "new": r"de \(S\)-points"},
    "The print drops the s of 'des'; the TeX silently corrects it, the fix restores the printed reading.",
    corrected=r"des \(S\)-points")

# ---------------- p. 612
ISOM_NOTE = (r"\Isom is \operatorname{Isom} (defined before Exposé XII; also used on pp. 602-603). The print "
             r"underlines Isom in all three places of p. 612; if pp. 602-603 underline it too, one redefinition "
             r"(\underline{\operatorname{Isom}}) replaces the three edits.")
add(612,
    "'Par définition Rec est égal au foncteur Isom(p_1*L, p_2*L) où les p_i'",
    "Isom underlined (both scans; " + C + "b612_1.png)",
    r"\(\Isom(p_1^*L,p_2^*L)\), plain Isom",
    "underline", "high",
    {"old": r"foncteur \(\Isom(", "new": r"foncteur \(\underline{\Isom}("},
    ISOM_NOTE)
add(612,
    "display 'i : Deff ↪ Isom(p_1*L, p_2*L)'",
    "Isom underlined (both scans)",
    r"i:\mathrm{Deff}\hookrightarrow \Isom(p_1^*L,p_2^*L), plain Isom",
    "underline", "high",
    {"old": r"\hookrightarrow \Isom(", "new": r"\hookrightarrow \underline{\Isom}("},
    "See the first Isom entry of this page.")
add(612,
    "'Remarquons en passant que si l'on y tient on peut restreindre Isom(p_1*L, p_2*L)'",
    "Isom underlined (both scans)",
    r"restreindre \(\Isom(p_1^*L,p_2^*L)\), plain Isom",
    "underline", "high",
    {"old": r"restreindre \(\Isom(", "new": r"restreindre \(\underline{\Isom}("},
    "See the first Isom entry of this page.")
add(612,
    "Lemme 4.3, item 3): '(ou le dernier isomorphisme est g_*(φ))'",
    "'ou' without the grave accent (both scans; " + C + "c612_ou2.png); the typist types 'où' elsewhere on the "
    "page ('où les p_i')",
    "(ou le dernier isomorphisme est",
    "misprint_in_print", "high", None,
    "The TeX keeps the printed reading (the current layer also has 'ou').",
    corrected="(où le dernier")

# ---------------- p. 613
add(613,
    "'donc la donnée de descente sur L restreindre au-dessus de V=f^{-1}(V)'",
    "restreindre (both scans; " + C + "b613_1.png)",
    r"sur \(L\) restreindre au-dessus",
    "misprint_in_print", "high", None,
    "The TeX keeps the printed reading; the current layer has 'restreinte'.",
    corrected="restreinte")
add(613,
    "Lemme 4.4, '(précisément, S_n(T) = {∅} si R^i(f_T)_*(F_T) est plat pour tout i≥n'",
    "R^i: the superscript is a dotted i, like the i of the underlined 'si' just before it and unlike the 1 of "
    "f^{-1}(V) on the same page (witness clear: " + C + "c613_R1c.png, c613_fm1.png; the main scan blurs the dot, "
    + C + "m613_R.png)",
    r"R^1(f_T)_*(F_T)",
    "formula", "high",
    {"old": r"R^1(f_T)_*(F_T)", "new": r"R^i(f_T)_*(F_T)"},
    "Transcription error, not a misprint; the current layer already has R^i.")

# ---------------- p. 614
add(614,
    "start of the page (folio-614 marker)",
    "p. 613 ends '... L'assertion est donc vraie pour n > r ;' (both scans); p. 614 begins 'en procédant par "
    "récurrence décroissante, supposons qu'elle est connue pour n+1.'",
    r"page_613.tex ends 'L'assertion est donc vraie' above the folio-614 marker; page_614.tex begins "
    r"'pour \(n>r\)~; en procédant'",
    "marker", "high", None,
    r"The marker stands too early: page 614 really begins at 'en procédant'. Edit in main.tex, both layers: the "
    r"line above the marker should end '... L'assertion est donc vraie pour \(n>r\)~;' and the line below it begin "
    r"'en procédant par récurrence décroissante, ...'.")
add(614,
    "'on peut supposer que R^n f_*(F) est S-plat pour i ≥ n+1'",
    "R^n (both scans; " + C + "c614_Rn.png)",
    r"\(R^nf_*(F)\) est \(S\)-plat pour \(i\ge n+1\)",
    "misprint_in_print", "high", None,
    "The quantifier 'pour i ≥ n+1' requires R^i; the TeX keeps the printed R^n (the current layer has R^i). "
    "The next sentence's R^n f_*(F) ('commute à tout changement de base') is right.",
    corrected=r"R^if_*(F)")
add(614,
    "'(voir : J.P. Murre, Representation of unramified functors, Séminaire Bourbaki ; Mai 1965, p.294-11, th.2)'",
    "the title is typed plain, not underlined (both scans; " + C + "c614_murre.png)",
    r"\emph{Representation of unramified functors}",
    "underline", "high",
    {"old": r"\emph{Representation of unramified functors}", "new": "Representation of unramified functors"},
    "Emphasis added by the transcription.")
add(614,
    "Lemme 4.6, 'u : F → G un homomorphisme de O_Y-Modules de présentation finie'",
    "O_Y (both scans; " + C + "c614_OY.png)",
    r"\(\mathcal O_Y\)-Modules",
    "misprint_in_print", "medium", None,
    "F and G live on X (λ : X → S; the lemma has no Y), so O_X is meant; the TeX keeps the printed O_Y (the "
    "current layer has O_X).",
    corrected=r"\(\mathcal O_X\)-Modules")

# ---------------- p. 615
add(615,
    "start of the page (folio-615 marker)",
    "p. 614 ends '... Représentons d'abord le foncteur qui rend u un épimorphisme,'; p. 615 begins 'i.e. qui rend "
    "Coker u nul.' (both scans)",
    r"page_614.tex ends '... un épimorphisme, i.e. qui' above the folio-615 marker; page_615.tex begins "
    r"'rend \(\operatorname{Coker}u\) nul.'",
    "marker", "high", None,
    r"Page 615 really begins at 'i.e. qui'. Edit in main.tex, both layers: the line above the marker should end "
    r"'... qui rend \(u\) un épimorphisme,' and the line below it begin 'i.e. qui rend \(\operatorname{Coker}u\) "
    r"nul. ...'.")
add(615,
    "'Comme la formation de Coker u commute au diagramme de base, on voit qu'il est représenté'",
    "'commute au diagram-me de base' (hyphenated across the line end; both scans; " + C + "c615_top.png)",
    "commute au changement de base, on voit",
    "misprint_in_print", "high",
    {"old": "au changement de base, on voit", "new": "au diagramme de base, on voit"},
    "The TeX silently corrects the print; the fix restores the printed 'diagramme'. The second 'commute au "
    "changement de base' of the page is printed so.",
    corrected="au changement de base, on voit")

# ---------------- checks
bad = 0
for d in F:
    fx = d["fix"]
    if fx is None:
        continue
    t = (PAGES / f"page_{d['page']}.tex").read_text(encoding="utf-8")
    n = t.count(fx["old"])
    if n != 1:
        bad += 1
        print("NOT UNIQUE", d["page"], n, fx["old"])
    if "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]:
        bad += 1
        print("MARKER IN FIX", d["page"], fx["old"])
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
json.loads(OUT.read_text(encoding="utf-8"))
counts = {}
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else "normal"
    counts.setdefault(d["page"], {"normal": 0, "misprint": 0})[k] += 1
print("entries", len(F), "bad", bad)
for p in sorted(counts):
    print(p, counts[p])
