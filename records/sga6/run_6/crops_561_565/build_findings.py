"""Build findings_561_565.json and check that every fix's old string occurs exactly once in its page file."""
import json, pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
B = RUN / "b561_565"
OUT = RUN / "findings_561_565.json"

F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- p. 561
add(561,
    "statements of pp. 561-562: end of Corollaire 7.2 (p. 561) and Proposition 7.3 (pp. 561-562)",
    "underlined word group by word group (both scans): Cor. 7.2 'd'autre part', 'on a un homomorphisme', 'Ceci posé', "
    "'le composé', 'est nul'; Prop. 7.3 'Avec les notations de', 'étant supposé noethérien', 'il existe un unique "
    "homomorphisme de groupes', 'dit', 'rendant commutatif le diagramme', and on p. 562 'Lorsqu'on considère les deux "
    "membres de', 'comme des modules sur', 'grâce aux homomorphismes d'anneaux', 'et', 'et aux structures de modules de', "
    "'et', 'sur', 'et', 'respectivement', 'l'homomorphisme', 'est un homomorphisme', 'de', 'modules' (formulas, numbers, "
    "references and punctuation not underlined)",
    "both statements set in roman",
    "underline", "high", None,
    "The appendix follows the Exposé II pattern of GLOBAL_ISSUES 82 (pending volume decision), as findings_521_525 and "
    "findings_526_530 report for Exposé X: not itemized. No \\emph on defined terms the print leaves plain and no "
    "category L on pp. 561-565. The underlined words of the running text (proofs, paragraphs 7.4, 7.7, 7.7.3) are "
    "itemized below with \\emph, the file's command for them in this exposé (folios 559, 566-573).")

add(561,
    "proof of 7.2: 'dont le faisceau conormal N est libre de rang 1'",
    "'libre' underlined (both scans)",
    "est libre de rang",
    "underline", "high",
    {"old": "est libre de rang", "new": "est \\emph{libre} de rang"},
    "Underlined word in running text. Independent of the \\mathbb N entry (the two old strings do not overlap).")

add(561,
    "proof of 7.2: 'dont le faisceau conormal N est libre'",
    "double-struck N: two parallel left stems with a white line between them (witness, pixel check; main scan the same: "
    "crops_561_565/w561_N_zoom.png, m561_N.png)",
    "conormal \\(N\\)",
    "font", "high",
    {"old": "conormal \\(N\\)", "new": "conormal \\(\\mathbb N\\)"},
    "The conormal sheaf is printed with the typescript's double-struck N, here and in λ_{-1}(N) three lines below; the "
    "TeX has a plain N. Apply the two N edits of this page together.")

add(561,
    "'On a donc λ_{-1}(N) = 0'",
    "the same double-struck N, heavily inked: thick doubled left stem, far heavier than the typed letters around it "
    "(both scans; crops_561_565/w561_lambdaN_zoom.png, m561_lambdaN_zoom.png)",
    "\\lambda_{-1}(N)=0",
    "font", "high",
    {"old": "\\lambda_{-1}(N)", "new": "\\lambda_{-1}(\\mathbb N)"},
    "As the previous entry; apply the two together.")

add(561,
    "'Nous supposerons dans toute la suite X noethérien et plat sur S.'",
    "'noethérien' and 'plat sur' underlined, 'et' and 'S.' not (both scans)",
    "noethérien et plat sur",
    "underline", "high",
    {"old": "noethérien et plat sur", "new": "\\emph{noethérien} et \\emph{plat sur}"},
    "Underlined words in running text.")

add(561,
    "diagram (7.3.2), top arrow K.(X) -> K.(X_t)",
    "label j*: long stem descending to the shaft with a leftward hook, as the j* over the first arrow on p. 562; the "
    "i* of the vertical arrow and of p. 562 is short with a foot (witness pixel check; crops_561_565/w561_diagtop.png, "
    "m561_diagtop.png, w562_jstar.png, w562_istar.png)",
    "\\arrow[r,\"i^*\"]",
    "formula", "high",
    {"old": "\\arrow[r,\"i^*\"]", "new": "\\arrow[r,\"j^*\"]"},
    "The restriction to the open X_t is j* (the exact sequence above; 'K˙(X) --j*--> K˙(X_t)' on p. 562). The TeX's "
    "i^* is not the print's reading.")

add(561,
    "diagram (7.3.2), end",
    "a full stop to the right of the lower row K.(X_s) (both scans)",
    "K_\\bullet(X_s) &\n\\end{tikzcd}",
    "punctuation", "high",
    {"old": "K_\\bullet(X_s) &\n\\end{tikzcd}", "new": "K_\\bullet(X_s) & {.}\n\\end{tikzcd}"},
    "Missing full stop; set in the empty cell as the file sets it for (7.7.2) on p. 564 ('K^\\bullet(X_s) & {.}').")

# ---------------- p. 562
add(562,
    "start of page: 'Lorsqu'on considère les deux membres de (7.3.1) ...' (Proposition 7.3 continued)",
    "flush left at the margin (witness left edge 288 px; margin of the page 285-295 px; the page's new paragraphs "
    "'La dernière assertion', 'Nous allons', 'Pour le voir' are indented to about 400 px): the statement goes on after "
    "the diagram (7.3.2) without a new paragraph (both scans)",
    "the blank lines before and after the local \\providecommand block at the end of page_561.tex end the paragraph, so "
    "'Lorsqu'on' starts a new, indented paragraph",
    "other", "medium",
    {"old": "Lorsqu'on considère les deux membres", "new": "\\noindent Lorsqu'on considère les deux membres"},
    "Extra paragraph break (as findings_571_575, p. 574). Removing the blank lines instead would put the line-end "
    "spaces of the eleven \\providecommand lines into the paragraph (a visible indent) unless the macro block is moved "
    "out of the statement; \\noindent gives the printed layout without touching page 561.")

add(562,
    "K with a raised dot on pp. 562-564 (14 places: 9 on p. 562, 4 on p. 563, 1 on p. 564)",
    "K with a raised filled dot in every place (both scans; crops_561_565/w562_Kdot.png, m562_Kdot.png)",
    "K^\\circ",
    "symbol", "high", None,
    "Convention of the Exposé X TeX up to 7.6, not itemized: one script K^\\circ -> K^{\\bullet} for Exposé X, both "
    "layers, as findings_521_525 (p. 522) proposes. From the heading 7.7 on (p. 564) the TeX itself writes K^\\bullet "
    "for the same printed K˙. Three examples: p. 562 'modules sur \\(K^\\circ(X)\\)' -> 'modules sur "
    "\\(K^{\\bullet}(X)\\)'; p. 563 'est \\(K^\\circ(X)\\)-linéaire' -> 'est \\(K^{\\bullet}(X)\\)-linéaire'; p. 564 "
    "'\\(K^\\circ\\to K_\\bullet\\)' -> '\\(K^{\\bullet}\\to K_\\bullet\\)'. No old string of this file contains "
    "K^\\circ.")

add(562,
    "heading 7.4",
    "'7.4. Compatibilité aux filtrations.' with a full stop after the underlined title (both scans)",
    "\\subsection*{7.4. Compatibilité aux filtrations}",
    "punctuation", "high",
    {"old": "\\subsection*{7.4. Compatibilité aux filtrations}",
     "new": "\\subsection*{7.4. Compatibilité aux filtrations.}"},
    "The other headings of the appendix keep the print's final stop (7.5, 7.7, 7.8 on these pages, 7.9 on p. 566); the "
    "missing underline of the title is accepted.")

add(562,
    "7.4: 'l'homomorphisme de spécialisation est compatible avec ces filtrations, et induit par suite'",
    "underlined from 'l'homomorphisme' to 'filtrations' (hyphenated spécialisa-|tion), the comma not (both scans)",
    "l'homomorphisme de spécialisation est compatible avec ces filtrations",
    "underline", "high",
    {"old": "l'homomorphisme de spécialisation est compatible avec ces filtrations",
     "new": "\\emph{l'homomorphisme de spécialisation est compatible avec ces filtrations}"},
    "Underlined assertion inside the running text of a numbered paragraph, not a labelled statement of the Exposé II "
    "pattern (as findings_566_570, p. 567); the file writes such underlining as \\emph (folio 573).")

add(562,
    "proof of 7.4: 'Or soit Y d'adhérence schématique de Y_t dans X'",
    "d'adhérence (both scans; crops_561_565/w562_adherence.png)",
    "Or soit \\(Y\\) d'adhérence schématique",
    "misprint_in_print", "high", None,
    "Typing error d' for l': Y is the schematic closure of Y_t in X. The TeX keeps the printed reading.",
    corrected="Or soit \\(Y\\) l'adhérence schématique")

# ---------------- p. 563
add(563,
    "after the diagram (7.5.2): 'Pour prouver (7.5.1), on est encore ramené au cas où ...'",
    "flush left at the margin (witness left edge 194 px; margin 190-198 px; indented paragraphs of this typescript "
    "start near 305-310 px, e.g. p. 565 'Notons aussi', 'Supposant toujours'): no new paragraph (both scans)",
    "\\end{equation}\n\nPour prouver",
    "other", "medium",
    {"old": "\\end{equation}\n\nPour prouver", "new": "\\end{equation}\nPour prouver"},
    "Extra paragraph break.")

add(563,
    "diagram (7.6.2), bottom arrow K.(X_t) -> K.(X_s)",
    "σ. above the arrow (both scans)",
    "\\arrow[rr,\"\\sigma_\\bullet\"']",
    "formula", "medium",
    {"old": "\\arrow[rr,\"\\sigma_\\bullet\"']", "new": "\\arrow[rr,\"\\sigma_\\bullet\"]"},
    "Label on the wrong side of the arrow (as findings_041_045, findings_301_305); j* (upper left) and i* (upper right) "
    "stand as printed.")

# ---------------- p. 564
add(564,
    "diagram (7.7.2), top arrow K˙(X) -> K˙(X_t)",
    "label j*: long stem with a leftward hook reaching the shaft (witness pixel check, crops_561_565/w564_jstar.png); "
    "the next sentence names both maps of the diagram: 'Comme dans ce dernier i* et j* sont des homomorphismes "
    "d'anneaux (IV 2.7 b) avec j* surjectif'",
    "\\arrow[r,\"i^*\"]",
    "formula", "high",
    {"old": "\\arrow[r,\"i^*\"]", "new": "\\arrow[r,\"j^*\"]"},
    "As (7.3.2) on p. 561.")

add(564,
    "after the diagram (7.7.2): 'Comme dans ce dernier i* et j* sont des homomorphismes d'anneaux'",
    "flush left at the margin (witness left edge 284 px; margin 284-293 px): no new paragraph (both scans)",
    "\\end{equation}\n\nComme dans ce dernier",
    "other", "medium",
    {"old": "\\end{equation}\n\nComme dans ce dernier", "new": "\\end{equation}\nComme dans ce dernier"},
    "Extra paragraph break.")

add(564,
    "'il s'ensuit que l'homomorphisme de spécialisation (7.7.1) est un homomorphisme d'anneaux.'",
    "'l'homomorphisme de spécialisation' and 'est un homomorphisme d'anneaux' underlined; '(7.7.1)' and the full stop "
    "not (both scans)",
    "l'homomorphisme de spécialisation (7.7.1) est un homomorphisme d'anneaux",
    "underline", "high",
    {"old": "l'homomorphisme de spécialisation (7.7.1) est un homomorphisme d'anneaux",
     "new": "\\emph{l'homomorphisme de spécialisation} (7.7.1) \\emph{est un homomorphisme d'anneaux}"},
    "Underlined conclusion in the running text of 7.7 (as 7.4 on p. 562).")

add(564,
    "'Pour la même raison, si X est séparé, l'homomorphisme (7.7.1) est même un homomorphisme de λ-anneaux.'",
    "underlined: 'si', 'est séparé', 'l'homomorphisme' (hyphenated l'homo-|morphisme), 'est même un homomorphisme de', "
    "'anneaux' (λ- not; crops_561_565/w564_lambda_anneaux.png); X, the comma, (7.7.1) and the full stop not (both scans)",
    "si \\(X\\) est séparé, l'homomorphisme (7.7.1) est même un homomorphisme de \\(\\lambda\\)-anneaux",
    "underline", "high",
    {"old": "si \\(X\\) est séparé, l'homomorphisme (7.7.1) est même un homomorphisme de \\(\\lambda\\)-anneaux",
     "new": "\\emph{si} \\(X\\) \\emph{est séparé}, \\emph{l'homomorphisme} (7.7.1) \\emph{est même un homomorphisme "
            "de} \\(\\lambda\\)-\\emph{anneaux}"},
    "Independent of the previous entry.")

# ---------------- p. 565
add(565,
    "end of display (7.7.3) 'H^0(X_t,ℤ) -> H^0(X_s,ℤ)'",
    "a comma (clear in the witness, crops_561_565/w565_773end.png; the main scan shows a dark blot at that place); the "
    "sentence goes on 'qui mérite encore le nom de ...'",
    "H^0(X_s,\\mathbb Z).",
    "punctuation", "high",
    {"old": "H^0(X_s,\\mathbb Z).\n\\end{equation}", "new": "H^0(X_s,\\mathbb Z),\n\\end{equation}"},
    "Full stop for the printed comma.")

add(565,
    "'de sorte que l'homomorphisme H^0(X,ℤ) -> H^0(X_t,Z) induit par l'inclusion X_t -> X est bijectif'",
    "the Z of H^0(X_t,Z) is a plain typed Z (its 0 a small raised circle), the Z of H^0(X,ℤ) before it double-struck "
    "(both scans; crops_561_565/w565_H0Z.png, m565_H0Z.png)",
    "\\to H^0(X_t,\\mathbb Z)\\)",
    "font", "low",
    {"old": "\\to H^0(X_t,\\mathbb Z)\\)", "new": "\\to H^0(X_t,Z)\\)"},
    "The typist's plain Z where the TeX has \\mathbb Z; low, as the plain Q (volume decision with SGA 7 II issue 61). "
    "The other seven Z of the page are double-struck.")

add(565,
    "'est compatible avec les structures d'algèbres augmentées sur H^0(X_t,ℤ)'",
    "'algèbres augmentées' underlined, d' not (both scans)",
    "d'algèbres augmentées",
    "underline", "high",
    {"old": "d'algèbres augmentées", "new": "d'\\emph{algèbres augmentées}"},
    "Underlined words in running text.")

add(565,
    "'les structures d'algèbres augmentées sur H^0(X_t,ℤ) resp. H^0(X_s,ℤ) des deux membres définie dans (IV 2.8 )'",
    "définie (both scans)",
    "des deux membres définie dans (IV 2.8)",
    "misprint_in_print", "medium", None,
    "Agreement slip: the participle goes with 'les structures'. The TeX keeps the printed reading.",
    corrected="des deux membres définies dans (IV 2.8)")

# ---------------- checks
ok = True
for d in F:
    page_tex = (B / f"page_{d['page']}.tex").read_text(encoding="utf-8")
    fx = d["fix"]
    if fx is not None:
        n = page_tex.count(fx["old"])
        if n != 1:
            ok = False
            print("NOT UNIQUE", d["page"], n, repr(fx["old"]))
        if "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]:
            ok = False
            print("MARKER IN FIX", d["page"])
    if d["kind"] == "misprint_in_print":
        if page_tex.count(d["tex"]) != 1:
            ok = False
            print("MISPRINT TEX NOT UNIQUE", d["page"], repr(d["tex"]))
# overlapping fixes on the same page
for p in sorted({d["page"] for d in F}):
    t = (B / f"page_{p}.tex").read_text(encoding="utf-8")
    spans = []
    for d in F:
        if d["page"] == p and d["fix"] is not None:
            i = t.find(d["fix"]["old"])
            spans.append((i, i + len(d["fix"]["old"]), d["where"][:40]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            ok = False
            print("OVERLAP", p, a, b)
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
cnt = {}
for d in F:
    k = "m" if d["kind"] == "misprint_in_print" else "n"
    cnt.setdefault(d["page"], {"n": 0, "m": 0})[k] += 1
print("written", OUT, len(F), "entries; checks", "OK" if ok else "FAILED")
for p in sorted(cnt):
    print(p, cnt[p])
