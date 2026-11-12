"""Build findings_421_425.json and check that every fix's old occurs exactly once in its page_NNN.tex."""
import json
import pathlib

B = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\b421_425")
OUT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\findings_421_425.json")

MOVE = r'python -I move_marker.py 5 425 "\begin{equation}\tag{4.9.2}" --before'

F = []


def add(page, where, scan, tex, kind, confidence, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": confidence,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 421 ----------------
add(421, "D'autre part ..., 'l'espace vectoriel m^i/m^{i+1}'",
    "numerator m^i typed without the underline (the denominator m^{i+1} is underlined)",
    r"$\fm^i/\fm^{i+1}$", "misprint_in_print", "high",
    r"vectoriel $\fm^i/\fm^{i+1}$", r"vectoriel $m^i/\fm^{i+1}$",
    "The typist left out the underline that marks the maximal ideal; the TeX silently writes \\fm. Clean scan, the "
    "underlines of the neighbouring m are sharp.",
    r"vectoriel $\fm^i/\fm^{i+1}$")
add(421, "same paragraph, 'l'espace vectoriel Hom_k(m/m^2 , m^r/m^{r+1}) s'identifie'",
    "numerator m^r typed without the underline (m, m^2 and m^{r+1} underlined)",
    r"\Hom_k(\fm/\fm^2 \; , \; \fm^r/\fm^{r+1})", "misprint_in_print", "high",
    r"\; \fm^r/\fm^{r+1})$ s'identifie", r"\; m^r/\fm^{r+1})$ s'identifie",
    "Missing underline of the maximal ideal; the TeX silently writes \\fm.",
    r"\; \fm^r/\fm^{r+1})$ s'identifie")
add(421, "'Par l'isomorphisme gamma la structure de G-module de Hom_k(m/m^2 , m^r/m^{r+1}) se transporte'",
    "both denominators m^2 and m^{r+1} typed without the underline (numerators m and m^r underlined)",
    r"\Hom_k(\fm/\fm^2 \; , \; \fm^r/\fm^{r+1})", "misprint_in_print", "high",
    r"\Hom_k(\fm/\fm^2 \; , \; \fm^r/\fm^{r+1})$ se transporte",
    r"\Hom_k(\fm/m^2 \; , \; \fm^r/m^{r+1})$ se transporte",
    "Missing underlines of the maximal ideal; the TeX silently writes \\fm.",
    r"\Hom_k(\fm/\fm^2 \; , \; \fm^r/\fm^{r+1})$ se transporte")
add(421, "'induite par la structure de G-module de m/m^2 :'",
    "denominator m^2 typed without the underline (numerator m underlined)",
    r"$\fm/\fm^2$ :", "misprint_in_print", "high",
    r"-module de $\fm/\fm^2$ :", r"-module de $\fm/m^2$ :",
    "Missing underline of the maximal ideal; the TeX silently writes \\fm.",
    r"-module de $\fm/\fm^2$ :")
add(421, "'l'homomorphisme de \"contraction avec la (r-1)-ème puissance tensorielle ...'",
    "opening quote before 'contraction', no closing quote anywhere: '... puissance tensorielle "
    "(x)_k^{r-1}(m/m^2) :' and then the display",
    r"``contraction ... $\bigotimes_k^{r-1}(\fm/\fm^2)$'' :", "misprint_in_print", "high",
    r"(\fm/\fm^2)$'' :", r"(\fm/\fm^2)$ :",
    "Unclosed quotation in the print; the TeX silently adds the closing quote.",
    r"(\fm/\fm^2)$'' :")
add(421, "line before the item, 'On a donc'",
    "On a donc   (no colon)", "On a donc :", "punctuation", "high",
    "On a donc :", "On a donc",
    "The TeX adds a colon the print does not have.")
add(421, "label of the first condition",
    "1)  (typewriter digit one, flag at the top left; p. 422 has II) with serifed capitals, and cites 'Cond. I')",
    r"\item[I)]", "misprint_in_print", "high",
    r"\item[I)]", r"\item[1)]",
    "The print types the digit 1 for the Roman I; the TeX silently corrects to I).",
    r"\item[I)]")

# ---------------- page 422 ----------------
add(422, "display of the automorphism chi",
    "two lines: 'chi : m/m^2 ---> m/m^2' and below it 'xi ---> eps xi .'; no comma after the first line",
    r"\chi : \fm/\fm^2 \longrightarrow \fm/\fm^2 \quad , \quad \xi \longmapsto \varepsilon\xi \quad .",
    "punctuation", "high",
    r"\fm^2 \quad , \quad", r"\fm^2 \quad \quad",
    "The TeX adds a comma between the map and its formula (the two-line layout itself is not reported). The arrow "
    "is the next finding; the two edits do not overlap.")
add(422, "same display, 'xi ---> eps xi'",
    "plain long arrow, no bar at its tail", r"\xi \longmapsto \varepsilon\xi", "symbol", "high",
    r"\longmapsto", r"\longrightarrow",
    "The TeX writes \\longmapsto for the print's plain arrow.")
add(422, "last sentence, 'étant différent de zero (Cond. I)'",
    "zero  (no accent; 'différent' on the same line has its acute accents)", "zéro", "misprint_in_print", "high",
    "zéro", "zero",
    "Missing accent in the typescript; the TeX silently corrects.",
    "zéro")

# ---------------- page 423 ----------------
add(423, "display 'Card(G_1) = p^t .'", "Card(G_1)", r"\card(G_1)  (prints 'card')", "word", "high",
    r"\card(G_1)", r"\operatorname{Card}(G_1)",
    "\\card is \\operatorname{card} (s5.tex preamble); Exposé XII prints Card, as already applied on pp. 414 and 416.")
add(423, "display 'Card(G) = p^t c .'", "Card(G)", r"\card(G)  (prints 'card')", "word", "high",
    r"\card(G) = p^t c", r"\operatorname{Card}(G) = p^t c",
    "Same as the previous finding.")
add(423, "'Comme d'autre part c^{id_G}(e) = Card(G)'", "Card(G)", r"\card(G)  (prints 'card')", "word", "high",
    r"= \card(G)$", r"= \operatorname{Card}(G)$",
    "Same as the previous finding.")
add(423, "label 'Corollaire 4.8'",
    "Corollaire 4.8   Pour chaque ...  (no full stop after 4.8; 'Proposition 4.9.' below has one)",
    r"\textbf{Corollaire 4.8.}", "misprint_in_print", "medium",
    r"\textbf{Corollaire 4.8.}", r"\textbf{Corollaire 4.8}",
    "The print omits the stop after the label number; the TeX silently adds it. Reading certain; 'medium' only for "
    "calling the missing stop a misprint.",
    r"\textbf{Corollaire 4.8.}")

# ---------------- page 424 ----------------
add(424, "item ii)", "c^phi(g) = Card(G^psi)", r"\card(G^\psi)  (prints 'card')", "word", "high",
    r"\card(G^\psi)$, $G^\psi", r"\operatorname{Card}(G^\psi)$, $G^\psi",
    "Exposé XII prints Card; \\card prints card.")
add(424, "item iii)", "iii)  G^psi opère sur X'^{g^{-1}f'}_x   (no full stop)",
    r"opère sur ${X'_x}^{g^{-1}f'}$.", "punctuation", "high",
    r"opère sur ${X'_x}^{g^{-1}f'}$.", r"opère sur ${X'_x}^{g^{-1}f'}$",
    "The TeX adds a full stop at the end of the item.")
add(424, "item iv)", "... pour chaque h in G^psi   (no full stop)",
    r"pour chaque $h \in G^\psi$.", "punctuation", "high",
    r"pour chaque $h \in G^\psi$.", r"pour chaque $h \in G^\psi$",
    "The TeX adds a full stop at the end of the item.")
add(424, "label of item iv)",
    "i-nu)  (the second letter is the Greek nu of the formulas, not the serifed Latin v of 'voit' on this page)",
    r"\item[iv)]", "misprint_in_print", "high",
    r"\item[iv)]", r"\item[i$\nu$)]",
    "Typewriter symbol element left on: Greek nu typed for the Latin v of the label; the TeX silently corrects. "
    "The reverse of the globally handled 'index nu typed as Latin v'.",
    r"\item[iv)]")
add(424, "label of item v)",
    "nu)  (Greek nu, as in iv)", r"\item[v)]", "misprint_in_print", "high",
    r"\item[v)]", r"\item[$\nu$)]",
    "Same as the previous finding.",
    r"\item[v)]")
add(424, "(4.9.1), index of the first sum",
    "x' in X'^{g^{-1}f'}  (no subscript x under X'; the second sum has X'_x^{g^{-1}f'}/G^psi)",
    r"\sum_{x' \in {X'_x}^{g^{-1}f'}}", "misprint_in_print", "high",
    r"\sum_{x' \in {X'_x}^{g^{-1}f'}} (", r"\sum_{x' \in {X'}^{g^{-1}f'}} (",
    "The sum runs over the fixed points in the fibre X'_x (the sentence before decomposes X'_x^{g^{-1}f'} into "
    "orbits); the print drops the x, the TeX silently restores it. (4.9.2) on p. 425 has the same omission, kept "
    "by the TeX.",
    r"\sum_{x' \in {X'_x}^{g^{-1}f'}} (")
add(424, "(4.9.1), right-hand side", "... / Card(G^psi_{x'})  Card(G^psi) ,",
    r"{\card(G^\psi_{x'})} \card(G^\psi)", "word", "high",
    r"{\card(G^\psi_{x'})} \card(G^\psi)", r"{\operatorname{Card}(G^\psi_{x'})} \operatorname{Card}(G^\psi)",
    "Exposé XII prints Card (twice here).")
add(424, "display after (4.9.1)",
    "(nu_{x'}(g^{-1}f') = nu((g^{-1}f')_{O_{x'}}))  ,  -- the whole equation is in parentheses",
    r"\nu_{x'}(g^{-1}f')=\nu\bigl((g^{-1}f')_{\mathcal{O}_{x'}}\bigr) \quad ,", "missing", "high",
    r"\nu_{x'}(g^{-1}f')=\nu\bigl((g^{-1}f')_{\mathcal{O}_{x'}}\bigr) \quad ,",
    r"(\nu_{x'}(g^{-1}f')=\nu\bigl((g^{-1}f')_{\mathcal{O}_{x'}}\bigr)) \quad ,",
    "The TeX drops the outer parentheses (four opening and four closing in the print). The O here is a hand-drawn "
    "script O, not the underlined typed O (not itemized, see message).")
add(424, "(4.9.2), numerator (printed at the top of p. 425; its TeX stands under the folio-424 marker)",
    "(nu_{x'}(g^{-1}f')-1   -- opening parenthesis, no closing one",
    r"\frac{\nu_{x'}(g^{-1}f')-1}{...}", "misprint_in_print", "high",
    r"\frac{\nu_{x'}(g^{-1}f')-1}", r"\frac{(\nu_{x'}(g^{-1}f')-1}",
    "Unbalanced parenthesis in the print; the TeX silently drops it. Apply before the folio-425 marker move.",
    r"\frac{(\nu_{x'}(g^{-1}f')-1)}")
add(424, "(4.9.2), denominator and end (printed on p. 425)",
    "... / Card(G^psi_{x'})   -- no comma after the display",
    r"{\card(G^\psi_{x'})} \quad ,", "punctuation", "high",
    r"{\card(G^\psi_{x'})} \quad ,", r"{\operatorname{Card}(G^\psi_{x'})}",
    "The TeX adds a comma at the end of the display; the same edit writes Card for \\card (Exposé XII prints Card; "
    "one edit because the two overlap). Apply before the folio-425 marker move.")
add(424, "(4.9.2), index of the sum (printed on p. 425)",
    "x' in X'^{g^{-1}f'}/G^psi  (no subscript x)",
    r"{X'}^{g^{-1}f'}/G^\psi", "misprint_in_print", "medium",
    None, None,
    "The TeX keeps the printed reading; as in (4.9.1) the sum should run over the fibre X'_x (the current layer "
    "already has X'_x).",
    r"{X'_x}^{g^{-1}f'}/G^\psi")
add(425, "top of the page",
    "p. 425 begins with display (4.9.2) 'S_x(f',f,G,phi)(g) = sum ...', then 'et la proposition résulte de la "
    "proposition 4.6.'; p. 424 ends with 'c'est-à-dire :' and blank space",
    "'\\begin{equation}\\tag{4.9.2}' and the body of (4.9.2) stand at the end of page_424.tex; the folio-425 "
    "marker sits inside the equation, before '\\end{equation}'",
    "marker", "high", None, None,
    "Page 425 really begins at '\\begin{equation}\\tag{4.9.2}' (about s5.tex line 14286 in the diplomatic "
    "layer; the file is being edited, the anchor is unique). Exact fix: " + MOVE + " (the anchor occurs once in s5.tex in both layers; simulated in memory on "
    "both: the marker then stands on its own line between 'c'est-à-dire :' and '\\begin{equation}\\tag{4.9.2}'). "
    "Apply the three page-424 edits inside (4.9.2) before the move.")

# ---------------- page 425 ----------------
add(425, "section title 5", "Généralisation d'un formule de type Nielsen-Wecken.",
    "d'un formule", "misprint_in_print", "high", None, None,
    "The TeX keeps the printed reading.", "d'une formule")
add(425, "statement of Proposition 5.1, first sentence",
    "underlined: 'Les hypothèses et les notations étant celles de', 'supposons en plus que', 'est une partie "
    "finie de'; not underlined: '1,2,3,4,', Y', X'",
    "set in roman (statement environment, no emphasis)", "underline", "high",
    r"Les hypothèses et les notations étant celles de 1, 2, 3, 4, supposons en plus que $Y'$ est une partie finie de $X'$.",
    r"\emph{Les hypothèses et les notations étant celles de 1, 2, 3, 4, supposons en plus que $Y'$ est une partie finie de $X'$.}",
    "Exposé XII sets every other statement as \\textbf{label} \\emph{whole statement} (4.5-4.9); Proposition 5.1 "
    "has no emphasis at all. Five edits for the five underlined runs; they do not overlap.")
add(425, "statement of Proposition 5.1, 'Si l ... on a :'",
    "underlined: 'Si', 'est un nombre premier différent de la caractéristique de', 'on a'",
    "roman", "underline", "high",
    r"Si $\ell$ est un nombre premier différent de la caractéristique de $k$, on a :",
    r"\emph{Si $\ell$ est un nombre premier différent de la caractéristique de $k$, on a} :",
    "Part of the underlined statement of Proposition 5.1.")
add(425, "statement of Proposition 5.1, item a)",
    "underlined: 'les valeurs de la fonction', '-centrale'", "roman", "underline", "high",
    r"\item les valeurs de la fonction $\varphi$-centrale",
    r"\item \emph{les valeurs de la fonction $\varphi$-centrale}",
    "Part of the underlined statement of Proposition 5.1.")
add(425, "statement of Proposition 5.1, end of item a)",
    "underlined: 'sont des entiers', 'adiques'", "roman", "underline", "high",
    r"sont des entiers $\ell$-adiques.", r"\emph{sont des entiers $\ell$-adiques.}",
    "Part of the underlined statement of Proposition 5.1.")
add(425, "statement of Proposition 5.1, item b)",
    "underlined: 'la formule suivante est vraie :'", "roman", "underline", "high",
    r"\item la formule suivante est vraie :", r"\item \emph{la formule suivante est vraie :}",
    "Part of the underlined statement of Proposition 5.1.")
add(425, "(5.1.1), left-hand side", "Tr_{Z_l[G],phi}(f' ... H_{U',X'}(l)) with a hand-drawn script H",
    r"H_{U',X'}(\ell)", "font", "high",
    r"f'^\vee_{H_{U',X'}(\ell)}\bigr)", r"f'^\vee_{\mathcal{H}_{U',X'}(\ell)}\bigr)",
    "The print's H is drawn by hand as a script H, not typed; the TeX writes a plain H for it throughout Exposé XII "
    "(p. 410 checked: H_{n,U',X'} is the same hand-drawn script H there). See the message.")
add(425, "Démonstration, 'parce-que NW^{G,phi}_{f'}(x)'",
    "NW^{G,phi}_{f'} (x)  -- subscript f with a prime", r"\mathrm{NW}^{G,\varphi}_{f}(x)", "formula", "high",
    r"\mathrm{NW}^{G,\varphi}_{f}(x)$", r"\mathrm{NW}^{G,\varphi}_{f'}(x)$",
    "The TeX drops the prime. (5.1.1) just above prints NW_f, but no. 3 itself introduces the invariant as "
    "NW_{f'}^{G,phi}(x) (s5.tex, 'On va lui associer ...'), so the prime is not reported as a misprint.")
add(425, "Démonstration, 'Tr_{Z_l[G],phi}(f' ... H_{U',X'}(l))'", "hand-drawn script H, as in (5.1.1)",
    r"H_{U',X'}(\ell)", "font", "high",
    r"(f'^\vee_{H_{U',X'}(\ell)})$ sont", r"(f'^\vee_{\mathcal{H}_{U',X'}(\ell)})$ sont",
    "Same as (5.1.1).")

# ---------------- checks ----------------
ok = True
for d in F:
    if d["fix"] is None:
        continue
    page_text = (B / ("page_%d.tex" % d["page"])).read_text(encoding="utf-8")
    old = d["fix"]["old"]
    c = page_text.count(old)
    if c != 1 or "%%%%%%%%%%" in old or old == d["fix"]["new"]:
        ok = False
        print("PROBLEM", d["page"], c, repr(old))
# overlapping edits on one page
for n in range(421, 426):
    page_text = (B / ("page_%d.tex" % n)).read_text(encoding="utf-8")
    spans = []
    for d in F:
        if d["fix"] and d["page"] == n:
            k = page_text.find(d["fix"]["old"])
            spans.append((k, k + len(d["fix"]["old"]), d["fix"]["old"][:30]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            ok = False
            print("OVERLAP", n, a, b)
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
counts = {}
for d in F:
    k = counts.setdefault(d["page"], [0, 0])
    k[1 if d["kind"] == "misprint_in_print" else 0] += 1
print("ok" if ok else "NOT OK", len(F), counts)
