import json, sys, pathlib
from collections import defaultdict, Counter
sys.stdout.reconfigure(encoding='utf-8')
RUN = pathlib.Path(r'C:\Users\user\Documents\sga_scan_check_20261105\run_5')
B = RUN / 'b346_350'
OUT = RUN / 'findings_346_350.json'
NL = '\n'


def F(page, where, scan, tex, kind, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == 'misprint_in_print':
        d["corrected"] = corrected
    d["note"] = note
    return d


L = []
# ---------------- page 346 ----------------
L.append(F(346, "Lemme 9.8.7, the statement",
  "underlined: 'L'application' | 'est injective' (v_* and the full stop not underlined)",
  "L'application $v_*$ est injective. (no underline markup)",
  "underline", "high",
  r"L'application $v_*$ est injective.",
  r"\emph{L'application} $v_*$ \emph{est injective}.",
  r"Exposé VII statements are underlined word group by word group; \emph is the file's command for the underline, as the statements itemized on pp. 283-295 and 343."))
L.append(F(346, "statement labels of pp. 346-347 (convention, reported once)",
  "'LEMME 9.8.7.' (p. 346: capitals, full stop, no dash); 'THEOREME 9.9.-' (p. 347: capitals, '.-'); neither underlined",
  r"\begin{statement}{Lemme 9.8.7}, \begin{statement}{Théorème 9.9}: bold mixed case, the environment adds a full stop, no dash",
  "word", "high", None, None,
  "The label convention of Exposé VII (global issue 89 (a); reported once on p. 337), not itemized. For the closing pass: 'LEMME 9.8.7.' is printed without the dash that the other labels of the exposé carry."))
L.append(F(346, "first diagram, bottom row X' -> Z'",
  "X' --v--> Z' with no full stop after Z'",
  "&Z'.",
  "punctuation", "high",
  "&Z'.", "&Z'",
  "The TeX adds a full stop at the end of the diagram. Independent of the next item."))
L.append(F(346, "first diagram, label of the bottom arrow X' -> Z'",
  "v above the arrow (as v'' above the top arrow)",
  r"""\arrow[r,"v"'] (label below)""",
  "other", "medium",
  r"""X'\arrow[r,"v"']""", r"""X'\arrow[r,"v"]""",
  "Label position as in the print (as the label fixes of pp. 277-278, 296, 300, 310, 314-315, 343)."))
L.append(F(346, "(9.8.8)",
  "(f'_1)* o v_* = v''_* o (f')* with no comma at the end",
  "(f')^*,",
  "punctuation", "high",
  "(f')^*,", "(f')^*",
  "The TeX adds a comma at the end of the display."))
L.append(F(346, "cartesian diagram, label of the middle vertical arrow H x P^1 -> Y x P^1",
  "g x id at the right of the arrow (g at the left of the first arrow, f x id at the right of the third)",
  r"""\arrow[d,"{g\times\operatorname{id}}"'] (label at the left)""",
  "other", "medium",
  r""""{g\times\operatorname{id}}"'""", r""""{g\times\operatorname{id}}\"""".replace('\\"', '"'),
  "Label position as in the print; g (left) and f x id (right) are already on the printed sides in the TeX."))
# ---------------- page 347 ----------------
L.append(F(347, "first paragraph, 'il revient au même de montrer que v_* est injective'",
  "est injective lorsque de plus Y est de codimension 1",
  "est injectif lorsque",
  "word", "high",
  "est injectif lorsque", "est injective lorsque",
  "The TeX changes the ending of the adjective."))
L.append(F(347, "end of the first paragraph",
  "u_* un monomorphisme direct (u admet une rétraction).",
  "un monomorphisme direct, $u$ admettant une rétraction.",
  "word", "high",
  "direct, $u$ admettant une rétraction.", "direct ($u$ admet une rétraction).",
  "The TeX rewrites the printed parenthesis as a participle clause."))
L.append(F(347, "'Énonçons maintenant le théorème correspondant à (8.5) b).'",
  "(8.5) b)",
  "(8.5 b)",
  "punctuation", "high",
  "(8.5 b)", "(8.5) b)",
  "The print closes the parenthesis after 8.5 and writes b) after it."))
L.append(F(347, "Théorème 9.9, first line",
  "underlined: 'Pour tout entier' | 'la suite'",
  r"Pour tout entier $p\ge0$, la suite (no underline markup)",
  "underline", "high",
  r"Pour tout entier $p\ge0$, la suite", r"\emph{Pour tout entier} $p\ge0$, \emph{la suite}",
  "As the underlined statements of the exposé ('dans laquelle λ et μ désignent les flèches' is not underlined in the print)."))
L.append(F(347, "Théorème 9.9, the arrow λ",
  "λ : x ↦ [g*(x)c_{d-1}(F̌), -i_*(x)]: square brackets",
  r"\bigl(g^*(x)c_{d-1}(\check F),-i_*(x)\bigr)",
  "formula", "high",
  r"\bigl(g^*(x)c_{d-1}(\check F),-i_*(x)\bigr)", r"[g^*(x)c_{d-1}(\check F),-i_*(x)]",
  "The TeX has parentheses for the print's brackets. Independent of the next item."))
L.append(F(347, "Théorème 9.9, end of the λ line",
  "no comma after the bracket (the print sets λ and μ on two lines, neither with punctuation)",
  r"\bigr),\n\qquad",
  "punctuation", "high",
  "," + NL + r"\qquad" + NL + r"\mu:", NL + r"\qquad" + NL + r"\mu:",
  "The TeX adds a comma inside the display."))
L.append(F(347, "Théorème 9.9, after the display of λ and μ",
  "underlined: 'est exacte. De plus, l'application' | 'a pour inverse à gauche'",
  r"est exacte. De plus, l'application $\lambda$ a pour inverse à gauche (no underline markup)",
  "underline", "high",
  r"est exacte. De plus, l'application $\lambda$ a pour inverse à gauche",
  r"\emph{est exacte. De plus, l'application} $\lambda$ \emph{a pour inverse à gauche}",
  "Independent of the next item (the colon goes after the end of this line)."))
L.append(F(347, "Théorème 9.9, before the display of λ'",
  "'a pour inverse à gauche :' (colon, not underlined)",
  "à gauche (no colon)",
  "punctuation", "high",
  NL + r"\[" + NL + r"\lambda':", " :" + NL + r"\[" + NL + r"\lambda':",
  "The TeX drops the colon."))
L.append(F(347, "(9.9.1)",
  "(z ∈ C•(X)): C with a raised dot",
  r"(z\in C^*(X))",
  "symbol", "high",
  r"(z\in C^*(X))", r"(z\in C^{\bullet}(X))",
  "A round raised dot (the typewriter's full stop raised), not the six-pointed asterisk of f* on the same line; as C• on pp. 341-343."))
L.append(F(347, "after (9.9.1), 'et du fait, évident, que f_*(1) = 1'",
  "du fait, évident, que (two commas)",
  "du fait évident que",
  "punctuation", "high",
  "du fait évident que", "du fait, évident, que",
  "The TeX drops the two commas."))
L.append(F(347, "after (9.9.1), 'Soit donc t ∈ C•(X')'",
  "C with a raised dot, as in (9.9.1) two lines above; no p",
  r"t\in C^p(X')",
  "symbol", "high",
  r"t\in C^p(X')", r"t\in C^{\bullet}(X')",
  "The TeX has the degree p for the print's raised dot."))
L.append(F(347, "last line, 'U' = X' ∸ Y' sur U = X ∸ Y'",
  "two minus signs with a crisp dot centred above (∸)",
  "$U'=X'-Y'$ sur $U=X-Y$",
  "symbol", "high",
  "$U'=X'-Y'$ sur $U=X-Y$", r"$U'=X'\mathbin{\dot{-}}Y'$ sur $U=X\mathbin{\dot{-}}Y$",
  "The typescript's set-difference sign of Exposé VII, as the fixes of pp. 285, 301, 318, 327, 330, 342."))
# ---------------- page 348 ----------------
L.append(F(348, "first display, 'avec a ∈ C•(Y')'",
  "C with a raised dot",
  r"a\in C^*(Y')",
  "symbol", "high",
  r"a\in C^*(Y')", r"a\in C^{\bullet}(Y')",
  "As (9.9.1) on p. 347 and pp. 341-343."))
L.append(F(348, "before (9.9.3), 'd'où compte tenu de (9.9.1),'",
  "no comma after d'où",
  "d'où, compte tenu de (9.9.1),",
  "punctuation", "high",
  "d'où, compte tenu", "d'où compte tenu",
  "The TeX adds a comma."))
# ---------------- page 349 ----------------
L.append(F(349, "top of the page / folio-349 marker",
  "p. 349 begins 'de z résulte des deux relations j_*(z) = 0 et g_*(z) = 0 .'; p. 348 ends '... Montrons maintenant comment la nullité'",
  "'de $z$' ends the last line of page_348.tex ('... comment la nullité de $z$', s5.tex diplomatic line 11925, current 11921); page_349.tex begins at 'résulte des deux relations'",
  "marker", "high", None, None,
  "Page 349 really begins at 'de $z$'. Exact fix: python -I move_marker.py 5 349 'de $z$' --before (simulated in memory on both layers: '... comment la nullité ' / marker / 'de $z$' / 'résulte des deux relations ...'; the marker is a comment line, so the sentence stays whole). Not marker_split_word.py pull: it would join 'de $z$résulte' without a space. Text not moved; no other finding touches these lines."))
L.append(F(349, "'d'où g*(a_o)ξ+...+g*(a_{d-1})ξ^{d-1} = 0 ; donc tous les a_i sont nuls'",
  "last term g*(a_{d-1})ξ^{d-1}",
  r"g^*(a_{d-1})\xi^{d-1}=0;",
  "misprint_in_print", "medium", None, None,
  "zξ = Σ g*(a_i)ξ^{i+1} and a_{d-1} = 0 has just been shown, so the sum ends with g*(a_{d-2})ξ^{d-1} (all powers below d, whence a_i = 0 by the uniqueness of the representation); the printed index d-1 does not fit the exponent d-1 (the first term g*(a_o)ξ has index 0 and exponent 1). The TeX keeps the printed reading.",
  corrected=r"g^*(a_{d-2})\xi^{d-1}"))
L.append(F(349, "heading 9.10",
  "9.10. (with a full stop), run into 'Avec les notations de (9.9)'",
  r"\subsection*{9.10}",
  "punctuation", "high",
  r"\subsection*{9.10}", r"\subsection*{9.10.}",
  "As the heading '9.5.' of p. 342."))
L.append(F(349, "'Par suite μ enduit un isomorphisme'",
  "enduit",
  r"$\mu$ induit",
  "misprint_in_print", "high",
  r"$\mu$ induit", r"$\mu$ enduit",
  "Typing error of the print (e for i); the TeX silently corrects it.",
  corrected="induit"))
L.append(F(349, "relations before 'montrent que'",
  "g_*(ξ^i) = 0 pour i < d-1 ; g_*(ξ^{d-1}) = 1: a semicolon between the two relations",
  r"i<d-1,\qquad",
  "punctuation", "high",
  r"i<d-1,\qquad", r"i<d-1;\qquad",
  "The TeX has a comma for the print's semicolon. Independent of the next item."))
L.append(F(349, "same display, end",
  "no punctuation after '= 1'",
  r"g_*(\xi^{d-1})=1,",
  "punctuation", "high",
  r"(\xi^{d-1})=1,", r"(\xi^{d-1})=1",
  "The TeX adds a comma at the end of the display."))
# ---------------- page 350 ----------------
L.append(F(350, "'Ainsi que me l'a signalé MURRE'",
  "MURRE in capitals",
  "signalé Murre",
  "word", "high",
  "signalé Murre", "signalé MURRE",
  "Capitals as printed (as MUMFORD, p. 303)."))
L.append(F(350, "same sentence, the reference to Samuel",
  "par SAMUEL (Relations d'équivalence, Proceedings of the International Congress, Edinburgh 1958 ) . : capitals; the reference in parentheses; no 'dans'; the title not underlined",
  r"par Samuel, dans \emph{Relations d'équivalence}, Proceedings of the International Congress, Edinburgh 1958.",
  "word", "high",
  r"par Samuel, dans \emph{Relations d'équivalence}, Proceedings of the International Congress, Edinburgh 1958.",
  "par SAMUEL (Relations d'équivalence, Proceedings of the International Congress, Edinburgh 1958).",
  r"One edit: the capitals, the word 'dans' that the print does not have, the print's parentheses for the TeX's commas, and the title typed plain (\emph is the file's underline)."))
L.append(F(350, "heading of the bibliography",
  "BIBLIOGRAPHIE: capitals (centred, underlined, no full stop)",
  r"\subsection*{Bibliographie}",
  "word", "high",
  r"\subsection*{Bibliographie}", r"\subsection*{BIBLIOGRAPHIE}",
  r"Capitals as printed, as the BIBLIOGRAPHIE fixes of pp. 54, 72 and 136; the underline is the accepted \subsection* setting."))


def author(label, old, new, scan):
    return F(350, "bibliography " + label + ", author", scan, old, "word", "high", old, new,
             "Capitals as printed; the print sets the author and the title in two columns, with no comma between them (as 'VERDIER, J-L.' on p. 72). One edit.")


def tend(label, old, new, scan):
    return F(350, "bibliography " + label + ", end of the title", scan, old, "punctuation", "high", old, new,
             "The print ends the title with a full stop (outside the underline); the TeX has a comma.")


L.append(author("[1]", r"\item Grothendieck, \emph{", r"\item GROTHENDIECK \emph{", "GROTHENDIECK, then the title in the right-hand column"))
L.append(tend("[1]", "Chern}, Bull.", "Chern}. Bull.", "La théorie des classes de Chern. (full stop)"))
L.append(F(350, "bibliography [1], volume number", "86 underlined", r"\textbf{86}", "underline", "high",
  r"\textbf{86}", r"\emph{86}",
  r"The print underlines the volume number (\emph is the file's command for the underline); the TeX sets it bold."))
L.append(F(350, "bibliography [1], pages", "pp. 137-154 (typewriter hyphen)", "137--154", "punctuation", "high",
  "137--154", "137-154", "En dash added by the transcription (as p. 137)."))
L.append(author("[2]", r"\item Hodge, \emph{", r"\item HODGE \emph{", "HODGE, then the title in the right-hand column"))
L.append(tend("[2]", "integrals}, Cambridge", "integrals}. Cambridge", "The theory and applications of harmonic integrals. (full stop)"))
L.append(author("[3]", r"\item Hirzebruch, \emph{", r"\item HIRZEBRUCH \emph{", "HIRZEBRUCH, then the title in the right-hand column"))
L.append(tend("[3]", "Geometry}, Springer", "Geometry}. Springer", "Topological Methods in Algebraic Geometry. (full stop)"))
L.append(author("[4]", r"\item Lefschetz, \emph{", r"\item LEFSCHETZ \emph{", "LEFSCHETZ, then the title in the right-hand column"))
L.append(tend("[4]", "Geometry}, Princeton", "Geometry}. Princeton", "Algebraic Geometry. (full stop)"))
L.append(F(350, "bibliography [4], publisher and year", "Princeton University Press 1953. (no comma before the year)",
  "Princeton University Press, 1953.", "punctuation", "high",
  "Press, 1953.", "Press 1953.", "The TeX adds a comma ([2] prints 'Cambridge University Press, 1952.' with one)."))
L.append(author("[5]", r"\item Mme Raynaud, \emph{", r"\item Mme RAYNAUD \emph{", "Mme RAYNAUD ('Mme' in small letters), then the title in the right-hand column"))
L.append(tend("[5]", "universels}, Inventiones", "universels}. Inventiones", "Modules projectifs universels. (full stop)"))
L.append(author("[TF]", r"Godement, \emph{", r"GODEMENT \emph{", "GODEMENT, then the title in the right-hand column"))
L.append(tend("[CH]", "applications}, Séminaire", "applications}. Séminaire", "Anneaux de Chow et applications. Séminaire (full stop)"))
L.append(tend("[6]", "dégénérescence}, Pub.", "dégénérescence}. Pub.", "Théorème de Lefschetz et critères de dégénérescence. (full stop)"))
L.append(F(350, "end of the page / folio-351 marker",
  "p. 350 ends with the bibliography ('[6] ... Pub. I.H.E.S. n° 35.'); p. 351 begins with the heading 'EXPOSE VIII' (b351_355/page_351_s1.png)",
  r"'\newpage', '\section*{Exposé VIII}' and '\begin{center}' stand before the folio-351 marker (s5.tex diplomatic lines 11995-11998, current 11991-11994); the marker sits inside the center block of the title",
  "marker", "high", None, None,
  r"Page 351 really begins at '\section*{Exposé VIII}' (diplomatic line 11996, current 11992). Exact fix: python -I move_marker.py 5 351 '\section*{Exposé VIII}' --before (simulated in memory on both layers: the marker then stands between '\newpage' and '\section*{Exposé VIII}', and the heading and the whole center block are on p. 351). Text not moved. Batch 351-355 may report the same move: run it once."))

# ---- checks ----
bad = 0
pages = {p: (B / f"page_{p}.tex").read_text(encoding='utf-8') for p in range(346, 351)}
for d in L:
    fx = d['fix']
    if fx is None:
        continue
    t = pages[d['page']]
    n = t.count(fx['old'])
    if n != 1 or '%%%%%%%%%%' in fx['old'] or fx['old'] == fx['new']:
        bad += 1
        print('BAD', d['page'], n, repr(fx['old']))
spans = defaultdict(list)
for d in L:
    fx = d['fix']
    if fx is None:
        continue
    t = pages[d['page']]
    i = t.find(fx['old'])
    spans[d['page']].append((i, i + len(fx['old']), fx['old'][:30]))
for p, s in spans.items():
    s.sort()
    for a, b in zip(s, s[1:]):
        if a[1] > b[0]:
            bad += 1
            print('OVERLAP', p, a, b)
for p in sorted(spans):
    t = pages[p]
    for d in L:
        if d['page'] != p or d['fix'] is None:
            continue
        if t.count(d['fix']['old']) != 1:
            bad += 1
            print('SEQ', p, repr(d['fix']['old']))
        t = t.replace(d['fix']['old'], d['fix']['new'], 1)
    if p in (346, 347, 349, 350):
        pass
c = Counter((d['page'], d['kind'] == 'misprint_in_print') for d in L)
for p in range(346, 351):
    print(p, 'normal', c[(p, False)], 'misprint', c[(p, True)])
print('total', len(L), 'bad', bad)
if bad == 0 and '--write' in sys.argv:
    OUT.write_text(json.dumps(L, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('written', OUT)
