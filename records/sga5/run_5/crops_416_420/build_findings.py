"""Build findings_416_420.json and check that every fix's old occurs exactly once in its page file."""
import json
import pathlib
from collections import Counter

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
PAGES = RUN / "b416_420"
NL = "\n"


def j(*lines):
    return NL.join(lines)


F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": confidence, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 416 ----------------
add(416,
    "between the displays 'ν(g_R^{-1}f') - 1 = ν(f''_R) - 1' and 'c^φ(g) = c^{φ'}(e) (G_g^φ = G_e^{φ'}) (cf. 4.2)'",
    "nothing between the two displays: no ink at all in the 65 pixel rows between them, across the whole width of the page",
    "a line 'et' between the two displays",
    "extra", "high",
    {"old": j(r"\]", r"et", r"\["), "new": j(r"\]", r"\[")},
    "The TeX adds the word 'et'.")

add(416,
    "display 'c^φ(g) = c^{φ'}(e) (G_g^φ = G_e^{φ'}) (cf. 4.2)'",
    "the display ends with '(cf. 4.2)', no full stop (only dust specks of one or two pixels to its right)",
    r"(\text{cf. 4.2}) \quad .",
    "punctuation", "high",
    {"old": r"(\text{cf. 4.2}) \quad .", "new": r"(\text{cf. 4.2})"},
    "The TeX adds a full stop at the end of the display.")

add(416,
    "display 'G_e^{φ'} = (G_e^{φ'})_e^{id_{G_e^{φ'}}}' after 'et qu'on a :'",
    "no full stop after the display",
    r"(G_e^{\varphi'})_e^{\id_{G_e^{\varphi'}}} \quad .",
    "punctuation", "high",
    {"old": r"_e^{\id_{G_e^{\varphi'}}} \quad .", "new": r"_e^{\id_{G_e^{\varphi'}}}"},
    "The TeX adds a full stop at the end of the display.")

add(416,
    "Lemme 4.7, display 'c = Card(Im(G ⟶ Aut_k(m/m^2)))'",
    "Card, with a capital C",
    r"\card(...), which prints 'card' (s5.tex line 261: \providecommand{\card}{\operatorname{card}})",
    "word", "high",
    {"old": r"c = \card(\im(G", "new": r"c = \operatorname{Card}(\im(G"},
    "Convention of Exposé XII §4 (see the message): the print types 'Card' wherever the TeX has \\card "
    "(p. 414 (4.2), p. 423 three times, and more). If \\card is redefined as \\operatorname{Card} once, this fix "
    "is not needed (applying it as well does no harm).")

add(416,
    "Lemme 4.7, second paragraph: 'Soit'",
    "'Soit' typed plain, not underlined (pixel check: no rule under the word); the sentence 'On a alors la relation "
    "suivante de divisibilité' below it is underlined",
    r"\emph{Soit (the \emph group opens before 'Soit' and closes after the display c \mid (r - 1))",
    "underline", "high",
    {"old": j(r"\emph{Soit", r"\["), "new": j(r"Soit", r"\emph{\[")},
    "\\emph is this exposé's markup for the print's underlined statements. The fix only moves the opening of "
    "the group after 'Soit'; the closing brace '\\]}' stays as it is.")

add(416,
    "display 'c|(r-1)' that ends Lemme 4.7 (printed at the top of p. 417)",
    "c|(r-1) with no full stop",
    r"c \mid (r - 1) \quad .",
    "punctuation", "high",
    {"old": r"c \mid (r - 1) \quad .", "new": r"c \mid (r - 1)"},
    "The TeX adds a full stop at the end of the display. The display belongs to p. 417 (see the marker item "
    "under p. 417); its old is in page_416.tex: apply this fix before the marker is moved, or look for it "
    "under p. 417 afterwards.")

add(416,
    "display 'ν(g_R^{-1}f') - 1 = ν(f''_R) - 1' after 'en observant aisément qu'on a :'",
    "ν(g_R^{-1}f') - 1: f' without the index R (checked at 2x; the R under g and under f'' are crisp)",
    r"\nu(g_R^{-1}f') - 1 = \nu(f''_R) - 1 (the printed reading)",
    "misprint_in_print", "high",
    None,
    "The TeX keeps the printed reading; the corrected layer (current/s5.tex) already reads f'_R. The same "
    "quantity is ν(g_R^{-1}f'_R) in the statement of 4.6 and at the top of this page.",
    corrected=r"\nu(g_R^{-1}f'_R) - 1 = \nu(f''_R) - 1")

# ---------------- page 417 ----------------
add(417,
    "top of the page: the display 'c|(r-1)' that ends Lemme 4.7",
    "p. 417 begins with the display 'c|(r-1)', then 'Démonstration. Il est clair que l'entier r satisfait aux "
    "conditions suivantes :'; p. 416 ends with 'On a alors la relation suivante de divisibilité :' and blank paper",
    "the display '\\[ c \\mid (r - 1) \\quad . \\]}' (diplomatic s5.tex lines 14040-14042) stands at the end of "
    "page_416.tex, before the folio-417 marker (line 14047)",
    "marker", "high",
    None,
    "Page 417 really begins at the display '\\[' + 'c \\mid (r - 1)' (diplomatic line 14040). Exact fix: "
    "python -I move_marker.py 5 417 '\\[' --before (simulated in memory on both layers: the marker lands on "
    "its own line between 'On a alors la relation suivante de divisibilité :' and that '\\[', inside the \\emph "
    "group, where a comment line does no harm).")

add(417,
    "a) and b): 'f'_r : A/m^r ⟶ A/m^r' and 'f'_{r+1} : A/m^{r+1} ⟶ A/m^{r+1}'",
    "the ring is typed A (four times)",
    r"A/\fm^r, A/\fm^{r+1} (the printed reading)",
    "misprint_in_print", "low",
    None,
    "The TeX keeps the printed reading. The ring of Proposition 4.6 and Lemme 4.7 is R, also in this proof "
    "(x ∈ R on this page, α ∈ R on p. 418, x_o ∈ R on p. 419); A appears only here and in 'le corps K des "
    "fractions de A' on p. 420: a slip of notation. For the corrected edition, all five or none.",
    corrected=r"f'_r : R/\fm^r \longrightarrow R/\fm^r ; f'_{r+1} : R/\fm^{r+1} \longrightarrow R/\fm^{r+1}")

# ---------------- page 418 ----------------
add(418,
    "second line of the display after 'groupes abéliens :': 'x ⟶ (f'_R(x)-x)mod m^{r+1}'",
    "a plain long arrow, no bar at its tail (checked at 2x), the same arrow as in 'm ⟶ m^r/m^{r+1}' above it",
    r"x \longmapsto (f'_R(x) - x) \bmod \fm^{r+1}",
    "symbol", "high",
    {"old": r"x \longmapsto", "new": r"x \longrightarrow"},
    "The TeX writes \\longmapsto for the print's plain arrow.")

# ---------------- page 419 ----------------
add(419,
    "'Mais on a :' before the display f'_R(αx) - αf'_R(x) = (f'_R(α) - α)f'_R(x) ,",
    "Mais on a :",
    "Mais on a (no colon)",
    "punctuation", "high",
    {"old": j(r"Mais on a", r"\["), "new": j(r"Mais on a :", r"\[")},
    "The TeX drops the colon.")

add(419,
    "display after 'parce que': 'f'_R(α) - α ∈ m^r (Condition a))'",
    "(Condition a)) with a capital C",
    r"\hbox{(condition a))}",
    "word", "high",
    {"old": r"\hbox{(condition", "new": r"\hbox{(Condition"},
    "Capital against small.")

add(419,
    "same display, after '(Condition a))'",
    "no comma after '(Condition a))'; the print sets 'f'_R(x) ∈ m (x ∈ m) .' on its own line below",
    r"\hbox{(condition a))}, \qquad f'_R(x)\in\fm ... (a comma joins the two printed lines on one line)",
    "punctuation", "high",
    {"old": j(r"a))},", ""), "new": j(r"a))}", "")},
    "The TeX adds a comma; setting the two lines on one is layout and is not reported.")

add(419,
    "display 'u(f'_R)(g(x mod m^2)) = ... = gu(f'_R)(x mod m^2)'",
    "the second line ends with 'gu(f'_R)(x mod m^2)', no full stop (pixel check: no ink to the right of it)",
    r"=gu(f'_R)(x\bmod\fm^2).",
    "punctuation", "high",
    {"old": r"=gu(f'_R)(x\bmod\fm^2).", "new": r"=gu(f'_R)(x\bmod\fm^2)"},
    "The TeX adds a full stop at the end of the display.")

# ---------------- page 420 ----------------
add(420,
    "after the last display '... = 0', end of the page",
    "the page ends with the display '= 1/x( ... ) = 0' and blank paper; p. 421 begins with 'Si l'on munit "
    "l'espace vectoriel sur k :'",
    r"et donc $f'_R(x_0) - x_0 \in \fm^{r+1}$ , ce qui est absurde.",
    "extra", "high",
    {"old": j(r"\]", r"et donc $f'_R(x_0) - x_0 \in \fm^{r+1}$ , ce qui est absurde."), "new": r"\]"},
    "A sentence the print does not have, neither at the foot of p. 420 nor at the head of p. 421: the TeX adds "
    "the conclusion of the argument.")

add(420,
    "last display, first line, second term: '- f'_R(x)/x · x'/f_R(x')' (after '= f'_R(x/x')/(x/x')')",
    "the denominator is f_R(x') without the prime (checked at 4x; every other prime of the display is crisp)",
    r"\frac{x'}{f'_R(x')} (the prime supplied)",
    "misprint_in_print", "high",
    {"old": j(r"\frac{x'}{f'_R(x')}", r"= \frac{x'\,f'_R"), "new": j(r"\frac{x'}{f_R(x')}", r"= \frac{x'\,f'_R")},
    "The TeX silently corrects; the fix restores the printed reading (diplomatic layer only). The same factor "
    "is x'/f'_R(x') in the first and third terms of the line.",
    corrected=r"\frac{x'}{f'_R(x')}")

add(420,
    "last display, second line, numerator: 'x'f'_R(x')f'_R(x/x') - x'f_R(x)'",
    "x'f_R(x) without the prime (checked at 3x)",
    r"- x'\,f'_R(x)} (the prime supplied)",
    "misprint_in_print", "high",
    {"old": r"- x'\,f'_R(x)}", "new": r"- x'\,f_R(x)}"},
    "The TeX silently corrects; the fix restores the printed reading (diplomatic layer only). The value 0 "
    "needs f'_R(x')f'_R(x/x') = f'_R(x).",
    corrected=r"- x'\,f'_R(x)}")

add(420,
    "'On aura donc, dans le corps K des fractions de A :'",
    "fractions de A",
    r"des fractions de $A$ (the printed reading)",
    "misprint_in_print", "low",
    None,
    "The TeX keeps the printed reading. Same slip as in a) and b) on p. 417: the ring is R. For the corrected "
    "edition, all five or none.",
    corrected=r"des fractions de $R$")

# ---------------- checks ----------------
ok = True
texts = {n: (PAGES / f"page_{n}.tex").read_text(encoding="utf-8") for n in range(416, 421)}
for d in F:
    fx = d["fix"]
    if fx is None:
        continue
    t = texts[d["page"]]
    c = t.count(fx["old"])
    if c != 1 or "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]:
        ok = False
        print("BAD", d["page"], repr(fx["old"]), c)
for n in range(416, 421):
    spans = []
    for d in F:
        if d["page"] == n and d["fix"]:
            i = texts[n].find(d["fix"]["old"])
            spans.append((i, i + len(d["fix"]["old"]), d["where"][:40]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            ok = False
            print("OVERLAP", n, a, b)
out = RUN / "findings_416_420.json"
out.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
cnt = Counter((d["page"], d["kind"] == "misprint_in_print") for d in F)
for n in range(416, 421):
    print(n, cnt[(n, False)], "/", cnt[(n, True)])
print("all olds unique and non-overlapping:", ok, "| findings:", len(F))
