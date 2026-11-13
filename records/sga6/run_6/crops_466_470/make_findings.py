"""Build findings_466_470.json (run_6) and check it: every fix's old string occurs exactly once in its page file
(also after the earlier fixes of the page are applied, in list order), no old/new string touches a marker line; the
main.tex marker edits quoted in the notes occur once in each layer, and after them each page starts and ends where the
print does."""
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_6"
SGA6 = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6"
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
M468 = "%%%%%%%%%%  scan idx 481  |  folio 468  %%%%%%%%%%"
M471 = "%%%%%%%%%%  scan idx 484  |  folio 471  %%%%%%%%%%"
NL = "\\n"  # the two characters backslash-n, for newlines inside quoted main.tex strings in notes

F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 466 ----------------
add(466, "exposé heading and title",
    "EXPOSE VIII in typed capitals with a single underline and no full stop, on its own line; then the title "
    "LE THEOREME DE RIEMANN-ROCH in typed capitals with a double underline (both scans; b466_470/page_466_s1.png, "
    "crops_466_470/wit_466_small.png)",
    r"\section*{Exposé VIII. Le théorème de Riemann--Roch}: number and title run together with a full stop, the title "
    "in small letters, no underline",
    "word", "medium",
    {"old": r"\section*{Exposé VIII. Le théorème de Riemann--Roch}",
     "new": r"\section*{\underline{EXPOSÉ VIII}\\[3pt] \underline{\underline{LE THÉORÈME DE RIEMANN--ROCH}}}"},
    r"Same form as the applied headings of Exposés III and IV (main.tex: \section*{\underline{EXPOSÉ III}\\[3pt] "
    r"\underline{\underline{CONDITIONS DE FINITUDE RELATIVES}}}); É and È keep the TeX's accents (rule for typed "
    "capitals); Riemann--Roch keeps its en dash (handled globally). Independent of the author-line entry.")

add(466, "author line of the heading",
    "'par Pierre BERTHELOT': the name in capitals, the whole line underlined (both scans)",
    "par Pierre Berthelot",
    "word", "medium",
    {"old": "par Pierre Berthelot", "new": r"\underline{par Pierre BERTHELOT}"},
    r"As the applied author lines of Exposés V and VI (\underline{par P. BERTHELOT}, \underline{par Pierre "
    "BERTHELOT}).")

add(466, "Définition 1.1, 'la restriction de f à U se factorise en :' before the diagram",
    "se factorise en : (colon before the diagram, both scans)",
    "se factorise en (no colon)",
    "punctuation", "high",
    {"old": "se factorise en\n\\[", "new": "se factorise en :\n\\["},
    "Colon lost in the transcription.")

add(466, "Définition 1.1, the diagram U → V, U → Y, V → Y",
    "no punctuation after the diagram (both scans; crops_466_470/wit_466_small.png)",
    "& Y, (comma after Y)",
    "punctuation", "high",
    {"old": "& Y,\n\\end{tikzcd}", "new": "& Y\n\\end{tikzcd}"},
    "Comma added at the end of the display by the transcription.")

add(466, "'Quitte à remplacer V par un ouvert, on peut supposer que i est une immersion fermée régulière.'",
    "a new indented paragraph after '(VII 1.4).', which ends the definition (both scans)",
    "run on after 'où $i$ est une immersion régulière (VII 1.4).'",
    "other", "high",
    {"old": "(VII 1.4). Quitte", "new": "(VII 1.4).\n\nQuitte"},
    "Missing paragraph break.")

add(466, "Corollaire 1.3, the diagram X → V' (j), V' → V (p), X → V (i)",
    "a comma after the diagram, to the right of V (both scans; crops_466_470/wit_466_small.png)",
    "no punctuation after the diagram",
    "punctuation", "high",
    {"old": "& V\n\\end{tikzcd}", "new": "& V ,\n\\end{tikzcd}"},
    "Comma lost at the end of the display (the statement continues on p. 467 with 'où i et j sont des "
    "immersions').")

add(466, "statements of pp. 466-470: Définition 1.1 (p. 466), Proposition 1.2 (p. 466), Corollaire 1.3 (pp. 466-467), "
    "Proposition 1.4 (p. 470)",
    "underlined word group by word group (both scans): Déf. 1.1 'Soit', 'un morphisme de schémas', 'On dit que', "
    "'est', 'un morphisme d'intersection complète si pour tout point', 'de', 'il existe', 'un voisinage ouvert', 'de', "
    "'un', 'schéma lisse', 'tels que la restriction', 'de', 'à', 'se factorise en', 'où', 'est une immersion "
    "régulière'; Prop. 1.2 'Soit', 'un morphisme d'intersection complète', 'Alors toute', 'immersion', 'de', "
    "'dans un', 'schéma lisse est régulière'; Cor. 1.3 'Soit le diagramme commutatif', p. 467 'où', 'et', 'sont des "
    "immersions', 'et', 'un morphisme lisse', 'Alors pour que', 'soit une immersion régulière', 'il faut et il suffit "
    "que', 'soit une immersion régulière'; Prop. 1.4 'Soit', 'un morphisme plat localement de présentation finie', "
    "'Pour que', 'soit un morphisme d'intersection complète au sens', 'de', 'il faut et il suffit qu'il soit un "
    "morphisme d'intersection complète au sens de'; letters, formulas, references and punctuation plain; the labels "
    "underline only the word",
    r"the statements in roman; only the defined term of Déf. 1.1 is emphasized: \emph{morphisme d'intersection "
    "complète}",
    "underline", "high", None,
    "Exposé VIII follows the Exposé II pattern of GLOBAL_ISSUES 82 (pending volume decision), as Exposé VII does "
    "(findings_416_420, findings_431_435): not itemized. The one \\emph covers part of the printed group 'un morphisme "
    "d'intersection complète si pour tout point'; it goes with the volume decision. No category letter on "
    "pp. 466-470.")

# ---------------- page 467 ----------------
add(467, "'Or j' est une immersion régulière, car c'est une section d'un morphisme lisse'",
    "a new indented paragraph after the diagram (both scans)",
    "follows the display without a blank line",
    "other", "high",
    {"old": "\\]\nOr $j'$", "new": "\\]\n\nOr $j'$"},
    "Missing paragraph break.")

add(467, "'Soit i\" la restriction de i' à U, et soit U' un ouvert de V''",
    "a new indented paragraph after 'posons U = j'(X).' (both scans)",
    "run on after 'posons $U=j'(X)$.'",
    "other", "high",
    {"old": "posons $U=j'(X)$. Soit", "new": "posons $U=j'(X)$.\n\nSoit"},
    "Missing paragraph break.")

# ---------------- page 468 ----------------
add(468, "start of page (folio-468 marker)",
    "p. 467 ends 'on peut supposer V affine, i fermée, et que V' = V[T_1,...,T_n]. Posons V = Spec(A),'; p. 468 "
    "begins 'X = Spec(B) ; on a le diagramme commutatif :' (both scans; b466_470/page_467_s4.png, page_468_s1.png; "
    "crops_466_470/wit_467_small.png, wit_468_small.png)",
    "page_467.tex ends 'et que $V'=V[T_1,\\ldots,T_n]$.'; page_468.tex begins 'Posons $V=\\Spec(A)$, "
    "$X=\\Spec(B)$ ;' after the folio-468 marker",
    "marker", "high", None,
    "Page 468 really begins at '$X=\\Spec(B)$ ;'; the words 'Posons $V=\\Spec(A)$,' end p. 467. Exact edit in "
    "main.tex, both layers (diplomatic lines 11988-11990, current 11994-11996): replace 'T_n]$." + NL + M468 + NL
    + "Posons $V=\\Spec(A)$, $X=' by 'T_n]$. Posons $V=\\Spec(A)$," + NL + M468 + NL + "$X=' (old string once "
    "per layer; simulated in memory: page 467 then ends 'Posons $V=\\Spec(A)$,', page 468 begins "
    "'$X=\\Spec(B)$ ; on a le diagramme commutatif :'). The paragraph runs on, so no blank line.")

add(468, "letters of sheaves on pp. 468 and 470",
    "underlined in the print (both scans): p. 468 the K, J, I of 0 → i*(K/K²) → J/J² → I/I² → 0, of 'I, J et K "
    "désignant', of 'i*(K/K²) est facteur direct de J/J²', of i'*(K), of 'le faisceau conormal de j' est "
    "i*(K/K²)', of J/J² → i*(K/K²) and of the composite i*(K/K²) → J/J² → i*(K/K²); p. 470 the E of 'de type fini "
    "E' and 'u : E → O_V', the K of K.(u_y) = K.(u)_y, of K.(u) and of K.(u)_y. Plain in the print: the J of 'la "
    "décomposition de J en somme directe' (p. 468) and all other letters (X, Y, U, V, W, A, B, u, v, w, s, t_i, "
    "T_i, ...)",
    "all plain",
    "underline", "high", None,
    "Convention of the transcription, as in Exposé VII (findings_431_435): not itemized. Three examples in the form "
    "to use if the diplomatic layer reproduces the underline: p. 468 '$I$, $J$ et $K$ désignant' -> "
    "'$\\underline{I}$, $\\underline{J}$ et $\\underline{K}$ désignant'; p. 470 'de type fini $E$, et' -> "
    "'de type fini $\\underline{E}$, et'; p. 470 'donc plat, $K_\\bullet(u)$ est' -> 'donc plat, "
    "$\\underline{K}_\\bullet(u)$ est'. The underlined O (written \\mathcal O on these pages) falls under the pending "
    "volume decision; the sheaf Tor and the k of k(y) (p. 470) are separate entries.")

# ---------------- page 469 ----------------
add(469, "'un voisinage ouvert W' de j(x) au dessus de W'",
    "'au' ends the line with no hyphen, 'dessus de W,' begins the next (both scans; crops_466_470/p469_au.png, "
    "w469_au.png); p. 467 types 'au-dessus de X' within a line",
    "au-dessus de $W$",
    "misprint_in_print", "low",
    {"old": "au-dessus de $W$", "new": "au dessus de $W$"},
    "The typist dropped the compound's hyphen at the line break, so the print reads 'au dessus'; the TeX silently "
    "corrects it. Low confidence: a hyphen at a line end is close to the hyphenation the check ignores; drop the "
    "entry if the volume treats it so.",
    corrected="au-dessus de $W$")

add(469, "iv), the diagram W' → W[T_1,...,T_n] (q), W' → W (p), W[T_1,...,T_n] → W (p_o)",
    "a comma after the diagram, to the right of its bottom row (both scans; crops_466_470/wit_469_small.png)",
    "no punctuation after the diagram",
    "punctuation", "high",
    {"old": "W &\n\\end{tikzcd}", "new": "W & ,\n\\end{tikzcd}"},
    "Comma lost at the end of the display (the sentence continues 'où p_o est le morphisme structural').")

add(469, "'Appliquant les résultats ii) et iii), on en déduit que q∘i est régulière, puis que i est régulière.'",
    "q∘i (both scans; crops_466_470/p469_qi.png, w469_qi2.png)",
    "$q\\circ i$ est régulière (printed reading kept)",
    "misprint_in_print", "high", None,
    "q : W' → W[T_1,...,T_n] and j : X → V' = W', so only q∘j is defined (i lands in V = W); the sentence before "
    "says that q∘j is an immersion, ii) (q étale) makes it regular, and iii) (W[T_1,...,T_n] a vector bundle over W) "
    "then gives i regular. The diplomatic TeX keeps the printed reading; the current layer also reads q∘i: the "
    "corrected edition needs q∘j.",
    corrected="$q\\circ j$ est régulière")

add(469, "'Montrons maintenant 1.2.' and 'La propriété étant locale sur Z'",
    "two indented paragraphs: 'Montrons maintenant 1.2.' stands alone on its line (both scans)",
    "one paragraph 'Montrons maintenant 1.2. La propriété ...'",
    "other", "high",
    {"old": "Montrons maintenant 1.2. La", "new": "Montrons maintenant 1.2.\n\nLa"},
    "Missing paragraph break.")

add(469, "'On en déduit une immersion fermée i\" : U → Z x_Y V, et le diagramme commutatif :'",
    "a new indented paragraph after the diagram (both scans)",
    "follows the display without a blank line",
    "other", "high",
    {"old": "\\]\nOn en déduit", "new": "\\]\n\nOn en déduit"},
    "Missing paragraph break.")

# ---------------- page 470 ----------------
add(470, "proof of Proposition 1.4, the factorisation U → V (i), U → Y (f), V → Y (g)",
    "no punctuation after the diagram (both scans; crops_466_470/wit_470_small.png)",
    "& Y, (comma after Y)",
    "punctuation", "high",
    {"old": "& Y,\n\\end{tikzcd}", "new": "& Y\n\\end{tikzcd}"},
    "Comma added at the end of the display by the transcription.")

add(470, "'Par suite, les groupes d'homologie de K.(u)_y sont les'",
    "comma after 'Par suite' (both scans; crops_466_470/p470_parsuite.png, w470_tor.png)",
    "Par suite les groupes",
    "punctuation", "high",
    {"old": "Par suite les groupes", "new": "Par suite, les groupes"},
    "Comma lost in the transcription.")

add(470, "'sont les Tor_i^{O_Y}(O_U,k(y))'",
    "Tor underlined: the sheaf Tor (both scans; crops_466_470/p470_tor.png, w470_tor2.png)",
    "\\Tor_i^{\\mathcal O_Y} plain",
    "underline", "high",
    {"old": "$\\Tor_i^{\\mathcal O_Y}", "new": "$\\underline{\\Tor}_i^{\\mathcal O_Y}"},
    "\\underline{\\Tor} is the file's form (39 times in main.tex; findings_431_435). The typescript types the "
    "superscript O_Y as a raised O followed by Y on the line; the TeX's ^{\\mathcal O_Y} stands. Independent of the "
    "k(y) entry on the same line.")

add(470, "'(O_U,k(y)), où k(y) est le corps résiduel de O_{Y,y}'",
    "the k of both k(y) underlined (both scans; crops_466_470/p470_tor.png, w470_tor2.png)",
    "k(y) plain, twice",
    "underline", "high",
    {"old": ",k(y))$, où $k(y)$", "new": ",\\underline{k}(y))$, où $\\underline{k}(y)$"},
    "The residue field's k is underlined (the typescript's mark for EGA's bold k). main.tex writes k(x), k(y) plain "
    "everywhere (about 45 places); on pp. 466-470 only these two. Independent of the Tor entry.")

add(470, "'Comme l'anneau local de U_y en y est quotient d'un anneau régulier par un idéal régulier,'",
    "en y (both scans; crops_466_470/p470_eny.png, wit_470_small.png)",
    "de $U_y$ en $y$ (printed reading kept)",
    "misprint_in_print", "high", None,
    "The local ring is taken at the point x of U_y (the sentence before: 'l'anneau local de V_y en x'; p. 471: "
    "'f est d'intersection complète en x'). The diplomatic TeX keeps the printed reading; the current layer already "
    "reads 'en $x$'.",
    corrected="de $U_y$ en $x$")

add(470, "end of page (folio-471 marker)",
    "p. 470 ends '... quotient d'un anneau régulier par un idéal régulier,'; p. 471 begins 'c'est un anneau "
    "d'intersection complète (EGA IV 19.3.2)' (both scans; crops_466_470/main_471_top.png, wit_471_top.png)",
    "page_470.tex ends 'par un idéal régulier, c'est un' above the folio-471 marker; the folio-471 text begins "
    "'anneau d'intersection complète'",
    "marker", "high", None,
    "Page 471 really begins at the words c'est un (the last two words of page_470.tex). Exact edit in main.tex, "
    "both layers (diplomatic lines 12047-12049, current 12053-12055), two replacements applied together (the quoted "
    "strings avoid the apostrophe): replace 'est un" + NL + M471 + NL + "anneau' by 'est un anneau'; then replace "
    "'anneau régulier par un idéal régulier, c' by 'anneau régulier par un idéal régulier," + NL + M471 + NL + "c' "
    "(each old string once per layer; simulated in memory: page 470 then ends 'par un idéal régulier,', page 471 "
    "begins with the words c'est un anneau). Or: python -I move_marker.py 6 471 \"c'est un\" --before. The sentence "
    "runs on, so no blank line. The checker of p. 471 may report the same boundary: apply once.")

json.dump(F, open(RUN + r"\findings_466_470.json", "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)

# ---------------- checks ----------------
ok = True
KINDS = {"word", "formula", "symbol", "font", "underline", "missing", "extra", "number", "punctuation", "accent",
         "misprint_in_print", "marker", "other"}
d = json.load(open(RUN + r"\findings_466_470.json", encoding="utf-8"))
pages = {n: open(RUN + rf"\b466_470\page_{n}.tex", encoding="utf-8", newline="").read() for n in range(466, 471)}
counts = {}
for i, x in enumerate(d):
    if x["kind"] not in KINDS or x["confidence"] not in ("high", "medium", "low"):
        print("bad kind/confidence", i); ok = False
    if (x["kind"] == "misprint_in_print") != ("corrected" in x):
        print("corrected key mismatch", i); ok = False
    c = counts.setdefault(x["page"], [0, 0])
    c[1 if x["kind"] == "misprint_in_print" else 0] += 1
    f = x["fix"]
    if f is None:
        continue
    k = pages[x["page"]].count(f["old"])
    if k != 1:
        print("entry", i, "page", x["page"], "old occurs", k, "times:", repr(f["old"])); ok = False
    if MARK.search(f["old"]) or MARK.search(f["new"]) or "%%%%" in f["old"] or "%%%%" in f["new"]:
        print("entry", i, "touches a marker line"); ok = False
work = dict(pages)
for i, x in enumerate(d):
    f = x["fix"]
    if f is None:
        continue
    t = work[x["page"]]
    if t.count(f["old"]) != 1:
        print("after earlier fixes, entry", i, "old occurs", t.count(f["old"])); ok = False
        continue
    work[x["page"]] = t.replace(f["old"], f["new"])
print("page fixes:", "OK" if ok else "PROBLEMS")
print("counts (normal/misprint):", {p: f"{a}/{b}" for p, (a, b) in sorted(counts.items())})


def unq(s):
    return s.replace("\\n", "\n")


for layer in ("diplomatic", "current"):
    t = open(SGA6 + "\\" + layer + r"\main.tex", encoding="utf-8", newline="").read()
    for x in d:
        if x["kind"] != "marker":
            continue
        for o, nw in re.findall(r"replace '(.*?)' by '(.*?)'", x["note"]):
            o, nw = unq(o), unq(nw)
            k = t.count(o)
            print(layer, "marker edit of page", x["page"], "old occurs", k)
            if k != 1:
                ok = False
                continue
            t = t.replace(o, nw)
    ms = list(MARK.finditer(t))
    for j, m in enumerate(ms):
        fo = int(m.group(2))
        if 466 <= fo <= 471:
            body = t[m.end():ms[j + 1].start()] if j + 1 < len(ms) else t[m.end():]
            body = body.strip("\n")
            print("  ", layer, fo, "starts", repr(body[:48]), "| ends", repr(body[-48:]))
print("ALL OK" if ok else "PROBLEMS FOUND")
