"""Build findings_471_475.json and check that every fix's old string occurs exactly once in its page file."""
import json, pathlib, sys
from collections import Counter
sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b471_475"
OUT = RUN / "findings_471_475.json"

M471 = "%%%%%%%%%%  scan idx 484  |  folio 471  %%%%%%%%%%"
M472 = "%%%%%%%%%%  scan idx 485  |  folio 472  %%%%%%%%%%"
M473 = "%%%%%%%%%%  scan idx 486  |  folio 473  %%%%%%%%%%"
TRI = r"""\[\n\begin{tikzcd}[column sep=large,row sep=large]\nU \arrow[r,"i"] \arrow[dr,"f"'] & V \arrow[d,"g"]\\\n& Y,\n\end{tikzcd}\n\]\n"""
STAMP = "as of the 16:14:32 main.tex; the files are being edited, so use the strings"

F = []

# ---------------- page 471 ----------------
F.append({
    "page": 471,
    "where": "start of page (folio-471 marker)",
    "scan": "p. 470 ends '... quotient d'un anneau régulier par un idéal régulier,'; p. 471 begins 'c'est un anneau d'intersection complète (EGA IV 19.3.2)' (both scans; crops_471_475/w470_bottom.png, wit_471_half.png)",
    "tex": "the last TeX line of p. 470 ends '... par un idéal régulier, c'est un' above the folio-471 marker; page_471.tex begins 'anneau d'intersection complète'",
    "kind": "marker",
    "confidence": "high",
    "fix": None,
    "note": "Page 471 really begins at 'c'est un'. Exact edit in main.tex, both layers (diplomatic lines 12058-12060, current 12064-12066, "
            + STAMP + "; the old string occurs once per layer; simulated in memory: crops_471_475/sim_markers.py): replace "
            + r"'par un idéal régulier, c'est un\n" + M471 + r"\nanneau d'intersection'"
            + " by " + r"'par un idéal régulier,\n" + M471 + r"\nc'est un anneau d'intersection'"
            + " (the sentence runs on; the comment line keeps the space between 'régulier,' and 'c'est'). Same boundary as the last entry of findings_466_470.json (folio-471 marker): apply one of the two.",
})
F.append({
    "page": 471,
    "where": "last line: 'On peut compléter ce diagramme par le carré commutatif :'",
    "scan": "a colon after 'commutatif' (both scans; wit_471_half.png)",
    "tex": "par le carré commutatif (no colon)",
    "kind": "punctuation",
    "confidence": "high",
    "fix": {"old": "par le carré commutatif", "new": "par le carré commutatif :"},
    "note": "Colon dropped before the display (the square at the top of p. 472). Independent of the folio-472 marker edit, whose old string starts at the display's '\\['.",
})
F.append({
    "page": 471,
    "where": "statements of pp. 471-474: Proposition 1.5 (p. 471), 1.6 and 1.7 (p. 472), 1.8 (p. 473), Définition 1.9 and Proposition 1.10 (p. 474)",
    "scan": "underlined word group by word group (both scans): Prop. 1.5 'Soient', 'et', 'deux morphismes localement d'intersection complète', 'Alors', 'est un morphisme localement d'intersection complète'; Prop. 1.6 'Soit', 'un morphisme', 'un changement de base plat', 'Si', 'est d'intersection complète', 'alors le morphisme', 'déduit de', 'l'est aussi', 'La réciproque est vraie si', 'est de plus quasi-compact et surjectif'; Prop. 1.7 'Soit', 'un morphisme d'intersection complète', 'Alors', 'est un morphisme parfait'; Prop. 1.8 'Soient', 'un morphisme d'intersection complète', 'un point de', 'et une factorisation', 'où', 'est un voisinage ouvert de', 'une immersion régulière', 'et', 'un morphisme lisse', 'On note', 'l'idéal de', 'définissant', 'Alors l'entier', 'est indépendant de la factorisation choisie de'; Déf. 1.9 'L'entier', 'de la proposition', 's'appelle', 'de', 'sur', 'ou de', 'au point', with the defined term 'dimension relative virtuelle' left plain; Prop. 1.10 'Soient', 'et', 'deux morphismes d'intersection complète', 'et soit', 'un point de', 'Alors'. Letters, formulas, numbers and punctuation plain; the labels underline only the word",
    "tex": "the statements in roman (no \\underline on pp. 471-475); \\emph{dimension relative virtuelle} on the defined term of Déf. 1.9, which the print leaves plain",
    "kind": "underline",
    "confidence": "high",
    "fix": None,
    "note": "Exposé VIII follows the Exposé II pattern of GLOBAL_ISSUES 82 (pending volume decision), as findings_466_470, findings_476_480 and the later batches report: not itemized. The only other \\emph in the exposé's text (bibliography titles aside) is Déf. 1.1 (\\emph{morphisme d'intersection complète}, p. 466).",
})

# ---------------- page 472 ----------------
F.append({
    "page": 472,
    "where": "start of page (folio-472 marker)",
    "scan": "p. 471 ends 'On peut compléter ce diagramme par le carré commutatif :'; p. 472 begins with that square V[T_1,...,T_n] → Z[T'_1,...,T'_m,T_1,...,T_n] over V → Z[T'_1,...,T'_m] (both scans; wit_471_half.png, wit_472_half.png)",
    "tex": "the folio-472 marker stands inside the square's option list: page_471.tex ends '\\[ \\begin{tikzcd}[column sep=large,row sep=' and page_472.tex begins 'large]'",
    "kind": "marker",
    "confidence": "high",
    "fix": None,
    "note": "Page 472 really begins at the square's '\\['. Exact edit in main.tex, both layers (diplomatic lines 12075-12078, current 12081-12084, "
            + STAMP + "; old string once per layer; simulated: crops_471_475/sim_markers.py): replace "
            + r"'\[\n\begin{tikzcd}[column sep=large,row sep=\n" + M472 + r"\nlarge]\n'"
            + " by " + "'" + M472 + r"\n\[\n\begin{tikzcd}[column sep=large,row sep=large]\n'"
            + ". This also takes the marker out of the tikzcd option. Independent of the colon fix on p. 471.",
})
F.append({
    "page": 472,
    "where": "the square at the top of the page: label j of the lower arrow V → Z[T'_1,...,T'_m]",
    "scan": "j stands above the lower arrow, as j' above the upper one (both scans; wit_472_half.png)",
    "tex": "\\arrow[r,\"j\"'] (label below the arrow)",
    "kind": "formula",
    "confidence": "medium",
    "fix": {"old": "\\arrow[r,\"j\"']", "new": "\\arrow[r,\"j\"]"},
    "note": "Label side only, the same kind of fix as findings_476_480 (pp. 476, 477).",
})
F.append({
    "page": 472,
    "where": "Proposition 1.6: 'alors le morphisme f' : Xx_YY' → Y' déduit de f l'est aussi'",
    "scan": "the formula stands in the running line between 'le morphisme' and 'déduit de f' (both scans; wit_472_half.png)",
    "tex": "a display \\[ f':X\\times_Y Y'\\to Y' \\]",
    "kind": "other",
    "confidence": "medium",
    "fix": {"old": "alors le morphisme\n\\[\nf':X\\times_Y Y'\\to Y'\n\\]\ndéduit de $f$",
            "new": "alors le morphisme $f':X\\times_Y Y'\\to Y'$ déduit de $f$"},
    "note": "The TeX makes an inline formula a display (same kind of fix as pp. 426, 458, 460). No common text with the misprint entry 'un morphisme $g$' below.",
})
F.append({
    "page": 472,
    "where": "proof of 1.6: 'Pour la réciproque on conclut d'abord de EGA IV 2.7.1 (iv)'",
    "scan": "no comma after 'réciproque' at the line end (both scans; crops_471_475/c472_reciproque.png, w472_reciproque.png)",
    "tex": "Pour la réciproque, on conclut",
    "kind": "punctuation",
    "confidence": "high",
    "fix": {"old": "Pour la réciproque, on conclut", "new": "Pour la réciproque on conclut"},
    "note": "Comma added by the TeX.",
})
F.append({
    "page": 472,
    "where": "end of the proof of 1.5: 'j'∘i est une immersion régulière de U dans un schéma lisse sur W, d'où le résultat'",
    "scan": "'sur W' (both scans; wit_472_half.png)",
    "tex": "lisse sur $W$ (printed reading kept)",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "lisse sur $Z$",
    "note": "The scheme is Z[T'_1,...,T'_m,T_1,...,T_n], smooth over Z (g : Y → Z in Proposition 1.5); no W occurs in 1.5 or its proof. The current layer also reads W: the corrected edition needs Z.",
})
F.append({
    "page": 472,
    "where": "Proposition 1.6: 'Soit f : X → Y un morphisme g : Y' → Y un changement de base plat.'",
    "scan": "nothing between 'un morphisme' and 'g : Y' → Y' (both scans; wit_472_half.png)",
    "tex": "un morphisme $g:Y'\\to Y$ (printed reading kept)",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": "un morphisme et $g:Y'\\to Y$",
    "note": "A word (or comma) dropped by the typist between the two items. The current layer reads 'un morphisme et $g:Y'\\to Y$'.",
})
F.append({
    "page": 472,
    "where": "proof of 1.6: 'au cas ou f est une immersion fermée'",
    "scan": "'ou' without the grave accent (both scans; wit_472_half.png)",
    "tex": "au cas ou $f$ (printed reading kept)",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "au cas où $f$",
    "note": "The relative 'où' typed without its accent. The current layer reads 'au cas où'.",
})

# ---------------- page 473 ----------------
F.append({
    "page": 473,
    "where": "start of page (folio-473 marker)",
    "scan": "p. 472 ends 'supposer qu'il existe un ouvert U contenant x, et une factorisation :' (the rest of the page blank); p. 473 begins with the triangle U --i--> V, f : U → Y, g : V → Y and a comma, then 'où i est une immersion régulière' (both scans; wit_472_half.png, wit_473_half.png)",
    "tex": "page_472.tex ends with that triangle (\\[ ... & Y, ... \\]) above the folio-473 marker",
    "kind": "marker",
    "confidence": "high",
    "fix": None,
    "note": "Page 473 really begins at the triangle's '\\[' after 'et une factorisation :'. Exact edit in main.tex, both layers (diplomatic lines 12094-12102, current 12100-12108, "
            + STAMP + "; old string once per layer; simulated: crops_471_475/sim_markers.py): move the marker line up six lines, i.e. replace "
            + r"'et une factorisation :\n" + TRI + M473 + r"\n'"
            + " by " + r"'et une factorisation :\n" + M473 + r"\n" + TRI + "'"
            + ". The triangle matches the print of p. 473 (comma included).",
})
F.append({
    "page": 473,
    "where": "diagram at the foot of the page: X --j--> V', p : V' → V, X --i--> V",
    "scan": "no punctuation after V (both scans; crops_471_475/w473_botdiag.png); p. 474 begins 'où p est un morphisme lisse'",
    "tex": "& V, (comma at the end of the diagram)",
    "kind": "punctuation",
    "confidence": "high",
    "fix": {"old": "& V,\n\\end{tikzcd}", "new": "& V\n\\end{tikzcd}"},
    "note": "Comma added at the end of the display. No common text with the label entry below (the two edits do not overlap).",
})
F.append({
    "page": 473,
    "where": "same diagram: label i of X → V",
    "scan": "i stands above the arrow X → V, inside the triangle under the diagonal j (both scans; crops_471_475/w473_botdiag.png)",
    "tex": "\\arrow[r,\"i\"'] (label below the arrow)",
    "kind": "formula",
    "confidence": "medium",
    "fix": {"old": "X \\arrow[ur,\"j\"] \\arrow[r,\"i\"']", "new": "X \\arrow[ur,\"j\"] \\arrow[r,\"i\"]"},
    "note": "Label side only, the same triangle and fix as findings_476_480 (pp. 476, 477).",
})
F.append({
    "page": 473,
    "where": "letters of sheaves on pp. 473-475",
    "scan": "underlined in the print (both scans; crops_471_475/w473_dx.png, w473_onote.png): the J of 'On note J l'idéal de O_V', both J of (J/J^2)_x and the Ω of Ω^1_{V/Y} in the d_x display (p. 473); every Ω^1 (the three of the first line, the three of (1.8.1), Ω^1_{V'/V} and Ω^1_{X'/X} twice in the text, Ω^1_{V'/V} in (1.8.2)) and both N of (1.8.2) (p. 474); every J, Ω^1 and L^{X/Y} of 2.1 (p. 475). Plain in the print: X, Y, U, V, V', X', d, f, g, i, j, p",
    "tex": "all plain (no \\underline on pp. 471-475)",
    "kind": "underline",
    "confidence": "high",
    "fix": None,
    "note": "Convention of the Exposé VIII transcription, as in Exposé VII (findings_441_445, findings_461_465) and as findings_466_470 and findings_476_480 report it: not itemized. The underlined O of O_V, O_X (pp. 473, 475), written \\mathcal O, falls under the pending structure-sheaf decision. Examples, in the form to use if the diplomatic layer reproduces the underline: p. 473 'On note $J$ l'idéal' -> 'On note $\\underline{J}$ l'idéal'; p. 474 'supposer $\\Omega^1_{V/Y}$' -> 'supposer $\\underline{\\Omega}^1_{V/Y}$' and '\\operatorname{rang}(N_{V/X})+' -> '\\operatorname{rang}(\\underline{N}_{V/X})+'; p. 475 'chaines $L^{X/Y}_\\bullet$' -> 'chaines $\\underline{L}^{X/Y}_\\bullet$'.",
})

# ---------------- page 474 ----------------
F.append({
    "page": 474,
    "where": "diagram after 'Du diagramme commutatif (où tous les morphismes sont lisses) :'",
    "scan": "no punctuation after Y; 'on déduit :' follows (both scans; crops_471_475/w474_diagwide.png)",
    "tex": "& Y,",
    "kind": "punctuation",
    "confidence": "high",
    "fix": {"old": "& Y,", "new": "& Y"},
    "note": "Comma added at the end of the display. No common text with the misprint entry on the arrow p (fix null).",
})
F.append({
    "page": 474,
    "where": "same diagram: the arrow p",
    "scan": "V --p--> V', the arrow drawn from V to V' (both scans; crops_471_475/c474_diag.png, w474_diag.png)",
    "tex": "V \\arrow[r,\"p\"] \\arrow[dr] & V' \\arrow[d] (printed reading kept)",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "V' \\arrow[r,\"p\"] \\arrow[dr] & V \\arrow[d]",
    "note": "p : V' → V is the smooth morphism of the diagram at the foot of p. 473 ('où p est un morphisme lisse'), and (1.8.1) is the rank formula for V' → V → Y; the print draws p from V to V'. The current layer already reads V' \\arrow[r,\"p\"] \\arrow[dr] & V \\arrow[d].",
})
F.append({
    "page": 474,
    "where": "after (1.8.1): 'Soit X' = V'x_VX ; alors le rang de ...'",
    "scan": "'Soit X'' begins a new, indented paragraph (both scans; wit_474_half.png)",
    "tex": "\\end{equation} followed directly by 'Soit $X'=V'\\times_V X$' (the paragraph runs on)",
    "kind": "other",
    "confidence": "high",
    "fix": {"old": "\\end{equation}\nSoit $X'", "new": "\\end{equation}\n\nSoit $X'"},
    "note": "Missing paragraph break.",
})
F.append({
    "page": 474,
    "where": "after (1.8.2): 'En comparant (1.8.1) et (1.8.2), on en déduit la proposition.'",
    "scan": "begins a new, indented paragraph (both scans; wit_474_half.png)",
    "tex": "\\end{equation} followed directly by 'En comparant'",
    "kind": "other",
    "confidence": "high",
    "fix": {"old": "\\end{equation}\nEn comparant", "new": "\\end{equation}\n\nEn comparant"},
    "note": "Missing paragraph break.",
})
F.append({
    "page": 474,
    "where": "'Si f est une immersion régulière de codimension n, sà dimension relative virtuelle est -n.'",
    "scan": "'sà', a grave accent on the a (both scans; crops_471_475/c474_sa.png, w474_sa.png), the same accent as in 'à valeurs' two lines above",
    "tex": "sa dimension (silently corrected)",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": {"old": "codimension $n$, sa dimension", "new": "codimension $n$, sà dimension"},
    "corrected": "codimension $n$, sa dimension",
    "note": "Typist's à for the possessive 'sa' (as 'sa dimension relative virtuelle est n' in the sentence before). Medium only because a speck on the original typescript cannot be ruled out; the mark is the same in both independent scans. The current layer reads 'sa' (the corrected edition keeps it).",
})
F.append({
    "page": 474,
    "where": "display of Proposition 1.10: 'dim.rel.virt._x(g∘f) = dim.rel.virt._x(f) + dim.rel.virt._{f(x)}(g)'",
    "scan": "no punctuation after (g) (both scans; crops_471_475/c474_dimend.png, w474_dimend.png); p. 475 begins 'Cela résulte immédiatement'",
    "tex": "\\operatorname{dim.rel.virt.}_{f(x)}(g).",
    "kind": "punctuation",
    "confidence": "high",
    "fix": {"old": "\\operatorname{dim.rel.virt.}_{f(x)}(g).", "new": "\\operatorname{dim.rel.virt.}_{f(x)}(g)"},
    "note": "Full stop added at the end of the display.",
})

# ---------------- page 475 ----------------
F.append({
    "page": 475,
    "where": "first line: 'Cela résulte immédiatement de 1.9 et de la démonstration de 1.5.'",
    "scan": "begins a new, indented paragraph after the display of Proposition 1.10 (both scans; wit_475_half.png)",
    "tex": "follows the display's '\\]' and the folio-475 marker line without a blank line (run on, unindented)",
    "kind": "other",
    "confidence": "high",
    "fix": {"old": "Cela résulte immédiatement", "new": "\nCela résulte immédiatement"},
    "note": "Missing paragraph break; the blank line goes after the marker line, which the edit does not touch.",
})
F.append({
    "page": 475,
    "where": "2.1: 'On définit alors un complexe de chaines L.^{X/Y} en posant :'",
    "scan": "'chaines' without the circumflex (both scans; wit_475_half.png)",
    "tex": "complexe de chaines (printed reading kept)",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": "complexe de chaînes",
    "note": "The spelling of 1971 is 'chaînes' (as findings_476_480 records 'entrainera' on p. 477). The current layer also reads 'chaines'; main.tex also writes 'chaines' on folios 11-12 (Exposé 0).",
})
F.append({
    "page": 475,
    "where": "last line of 2.1: 'et en prenant comme homomorphisme L_1^{X/Y} → L_o^{X/Y} l'homomorphisme (1.5.1).'",
    "scan": "'(1.5.1)' (both scans; crops_471_475/w475_151.png)",
    "tex": "l'homomorphisme (1.5.1). (printed reading kept)",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "l'homomorphisme (2.1.1).",
    "note": "The homomorphism J/J^2 → i^*(Ω^1_{V/Y}) defined just above is (2.1.1); Exposé VIII has no (1.5.1). The current layer already reads (2.1.1).",
})

# ---------------- checks and output ----------------
ok = True
for f in F:
    assert set(f) <= {"page", "where", "scan", "tex", "kind", "confidence", "fix", "corrected", "note"}
    if f["kind"] != "misprint_in_print":
        assert "corrected" not in f
    else:
        assert "corrected" in f
    fx = f["fix"]
    if fx is None:
        continue
    t = (B / f"page_{f['page']}.tex").read_text(encoding="utf-8")
    n = t.count(fx["old"])
    marker_cross = "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]
    print(f["page"], n, "MARKER!" if marker_cross else "", repr(fx["old"])[:70])
    if n != 1 or marker_cross:
        ok = False
# overlapping fixes on one page?
for p in range(471, 476):
    t = (B / f"page_{p}.tex").read_text(encoding="utf-8")
    spans = sorted((t.find(f["fix"]["old"]), t.find(f["fix"]["old"]) + len(f["fix"]["old"])) for f in F if f["page"] == p and f["fix"])
    for (a1, b1), (a2, b2) in zip(spans, spans[1:]):
        if a2 < b1:
            print("OVERLAP on page", p, (a1, b1), (a2, b2)); ok = False
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
c = Counter((f["page"], f["kind"] == "misprint_in_print") for f in F)
print(" ".join(f"{p} {c[(p, False)]}/{c[(p, True)]}" for p in range(471, 476)), "total", len(F))
print("ALL OLD UNIQUE, NO OVERLAP" if ok else "PROBLEM")
