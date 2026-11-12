"""Build findings_266_270.json and check that every fix's 'old' occurs exactly once in its page_NNN.tex
(and, for information, once in that page's span of the current diplomatic s5.tex)."""
import json
import pathlib
import re

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
B = RUN / "b266_270"
OUT = RUN / "findings_266_270.json"


def fx(old, new):
    return {"old": old, "new": new}


F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": confidence, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 266 ----------------
add(266, "top of the page: the display Hom_{Q_l}(F,G) = Q_l (x)_{Z_l} Hom_{Z_l}(F,G) and 'où Hom_{Z_l}(F,G) et Hom_{Q_l}(F,G)'",
    "p. 266 begins with the display 'Hom_{Q_ℓ}(F,G) = Q_ℓ ⊗_{Z_ℓ} Hom_{Z_ℓ}(F,G) ,', then 'où Hom_{Z_ℓ}(F,G) et Hom_{Q_ℓ}(F,G) désignent respectivement les morphismes'; p. 265 ends with '... et si F et G sont deux tels objets,'",
    "the display '\\[ \\Hom_{\\mathbb Q_\\ell}(F,G) =\\mathbb Q_\\ell\\otimes_{\\mathbb Z_\\ell}\\Hom_{\\mathbb Z_\\ell}(F,G), \\]' and the line 'où \\(\\Hom_{\\mathbb Z_\\ell}(F,G)\\) et \\(\\Hom_{\\mathbb Q_\\ell}(F,G)\\)' end page_265.tex, above the folio-266 marker; page_266.tex begins 'désignent respectivement'",
    "marker", "high", None,
    "Page 266 really begins at the display '\\[' that follows 'sont deux tels objets,'. Exact fix: python -I move_marker.py 5 266 '\\[' --before (simulated in memory on both layers: the last '\\[' before the marker is this display, and the marker then stands on its own line between 'sont deux tels objets,' and '\\['). The text that moves matches the print (the display with its final comma, then 'où ... et ...'). Text not moved.")

add(266, "'ce qui montre immédiatement que la catégorie (abélienne) décrite par objets et morphismes ci-dessus'",
    "'la catégorie (abélienne) décrite': the word in parentheses",
    "la catégorie abélienne décrite",
    "punctuation", "high", fx("la catégorie abélienne décrite", "la catégorie (abélienne) décrite"),
    "The TeX drops the parentheses.")

add(266, "'On dit qu'un Q_l-faisceau constructible est constant tordu, s'il est image d'un Z_l-faisceau constant tordu constructible.'",
    "'constant tordu' underlined (the defined term)",
    "est constant tordu s'il est image (no underline markup)",
    "underline", "high", fx("est constant tordu", "est \\emph{constant tordu}"),
    "Exposé VI writes the underline as \\emph, as the logged 'est dit \\emph{constant tordu}' of p. 254. Independent of the next item.")

add(266, "same sentence, 'constant tordu, s'il est image'",
    "a comma after 'tordu'",
    "tordu s'il est image",
    "punctuation", "high", fx(" s'il est image", ", s'il est image"),
    "The TeX drops the comma. Applies before or after the underline item.")

add(266, "'Il résulte de (1.2.4) que si X est connexe, la catégorie des Q_l-faisceaux constants tordus constructibles'",
    "no comma after 'que'",
    "(1.2.4) que, si \\(X\\) est connexe,",
    "punctuation", "high", fx("(1.2.4) que, si", "(1.2.4) que si"),
    "Comma added by the TeX.")

# ---------------- page 267 ----------------
add(267, "1.4.3, 'on définit à partir de la catégorie des Q_l-faisceaux constructibles celle des L-faisceaux constructibles'",
    "no comma after 'on définit' (the line reads 'constructibles,on définit à partir de la catégorie')",
    "on définit, à partir de la catégorie",
    "punctuation", "high", fx("on définit, à partir", "on définit à partir"),
    "Comma added by the TeX; the next item is the second one of the sentence.")

add(267, "same sentence, '... des Q_l-faisceaux constructibles celle des L-faisceaux constructibles'",
    "no comma after 'Q_ℓ-faisceaux constructibles'",
    "faisceaux constructibles, celle des",
    "punctuation", "high", fx("constructibles, celle des", "constructibles celle des"),
    "Comma added by the TeX.")

add(267, "numbered paragraph 1.4.4",
    "'1.4.4.' (with a full stop)",
    "\\subsubsection*{1.4.4}",
    "punctuation", "high", fx("\\subsubsection*{1.4.4}", "\\subsubsection*{1.4.4.}"),
    "As the logged '1.1.4.' of p. 253.")

add(267, "'supposons que F soit localement libre, i.e. que pour tout entier n, F_n soit un ...'",
    "no comma after 'i.e. que'",
    "i.e. que, pour tout entier \\(n\\),",
    "punctuation", "high", fx("i.e. que, pour", "i.e. que pour"),
    "Comma added by the TeX.")

add(267, "'(A/l^{n+1}A)_X-Module localement libre'",
    "'Module' with a capital M",
    "\\((A/\\ell^{\\,n+1}A)_X\\)-module",
    "word", "high", fx("A)_X\\)-module", "A)_X\\)-Module"),
    "The typescript's capital M (sheaf of modules), as the logged 'Module' of p. 159.")

# ---------------- page 268 ----------------
add(268, "numbered paragraph 1.4.5",
    "'1.4.5.' (with a full stop)",
    "\\subsubsection*{1.4.5}",
    "punctuation", "high", fx("\\subsubsection*{1.4.5}", "\\subsubsection*{1.4.5.}"),
    "As the logged '1.1.4.' of p. 253.")

add(268, "numbered paragraph 1.4.6 (printed at the top of p. 269)",
    "'1.4.6.' (with a full stop), the first line of p. 269",
    "\\subsubsection*{1.4.6}, the last line of page_268.tex",
    "punctuation", "high", fx("\\subsubsection*{1.4.6}", "\\subsubsection*{1.4.6.}"),
    "Filed under p. 268 because the line stands in page_268.tex until the marker move of p. 269: apply it before that move if edits are matched within page spans. The move's anchor '\\subsubsection*{1.4.6' matches with or without this full stop (simulated).")

# ---------------- page 269 ----------------
add(269, "top of the page: numbered paragraph 1.4.6",
    "p. 269 begins with '1.4.6. Soit F un Z_ℓ-faisceau constructible localement libre (1.3.3) .'; p. 268 ends with '... la représentation diagonale de π_1(X) sur V⊗W .'",
    "'\\subsubsection*{1.4.6}' is the last line of page_268.tex, above the folio-269 marker; page_269.tex begins 'Soit \\(F\\) un'",
    "marker", "high", None,
    "Page 269 really begins at '\\subsubsection*{1.4.6}'. Exact fix: python -I move_marker.py 5 269 '\\subsubsection*{1.4.6' --before (simulated in memory on both layers, before and after the full-stop fix of 1.4.6 filed under p. 268: the marker then stands between the blank line after 'sur \\(V\\otimes W\\).' and the heading). Text not moved.")

add(269, "1.4.6, 'et du foncteur G -> Hom(F,G) (1.3.2)'",
    "a plain long arrow 'G ——> ℋom(F,G)', without the bar of a maps-to arrow (p. 268's 'G |——> F ⊗ G' has its bar)",
    "\\(G\\mapsto\\cHom(F,G)\\)",
    "symbol", "high", fx("G\\mapsto\\cHom(F,G)", "G\\longrightarrow\\cHom(F,G)"),
    "As the logged '(u,v)\\longrightarrow vu' of p. 115.")

add(269, "'il résulte, de l'interprétation des restrictions de F aux composantes connexes Y de X comme pi_1(Y)-modules continus, que F s'écrit'",
    "a comma after 'résulte'",
    "il résulte de l'interprétation",
    "punctuation", "high", fx("il résulte de l'interprétation", "il résulte, de l'interprétation"),
    "The TeX drops the comma.")

# ---------------- page 270 ----------------
add(270, "numbered paragraph 1.4.7",
    "'1.4.7.' (with a full stop)",
    "\\subsubsection*{1.4.7}",
    "punctuation", "high", fx("\\subsubsection*{1.4.7}", "\\subsubsection*{1.4.7.}"),
    "As the logged '1.1.4.' of p. 253.")

add(270, "1.4.7, 'Ceci permet, de même qu'en (1.4.6), de définir à partir du produit tensoriel de (1.4.4) un produit tensoriel'",
    "'de même qu'en (1.4.6)'",
    "de même qu'en (1.4.6), (the printed number)",
    "misprint_in_print", "low", None,
    "Probable wrong reference: the tensor product of Q_ℓ-faisceaux, obtained from that of (1.4.4) by passing to the quotient by torsion, is 1.4.5; 1.4.6 does the same for Hom, and the paragraph then cites (1.4.6) twice, correctly, for the Hom part. The TeX keeps the printed reading. Optional: leave the printed number if the reference is read as pointing to the general method.",
    corrected="(1.4.5)")

add(270, "same sentence, 'de définir à partir du produit tensoriel de (1.4.4) un produit tensoriel :'",
    "no comma after 'de définir'",
    "de définir, à partir",
    "punctuation", "high", fx("de définir, à partir", "de définir à partir"),
    "Comma added by the TeX; the next item is the second one of the sentence.")

add(270, "same sentence, '... de (1.4.4) un produit tensoriel :'",
    "no comma after '(1.4.4)'",
    "de (1.4.4), un produit tensoriel:",
    "punctuation", "high", fx("(1.4.4), un produit", "(1.4.4) un produit"),
    "Comma added by the TeX.")

add(270, "'Comme l'anneau A est de Dedekind, l'argument utilisé en (1.4.6) ...'",
    "new paragraph (indented) after the display 'L-fc(X) x L-fc(X) ——> L-fc(X) .'",
    "'\\]' then 'Comme l'anneau' on the next line, no blank line",
    "other", "high", fx("\\]\nComme l'anneau", "\\]\n\nComme l'anneau"),
    "Paragraph break dropped by the TeX.")

add(270, "display 'Hom: (L-fct(X))° x L-fc(X) ——> L-fc(X)'",
    "no punctuation after the display; the next line is 'vérifiant les propriétés d'exactitude habituelles.'",
    "\\longrightarrow L\\text{-}\\fc(X),",
    "punctuation", "high", fx("L\\text{-}\\fc(X),\n\\]", "L\\text{-}\\fc(X)\n\\]"),
    "Comma added by the TeX at the end of the display (the corresponding display of 1.4.6 on p. 269 has its printed comma).")

add(270, "underlined title 1.5.",
    "'1.5. (AR, Z_ℓ)-faisceaux constructibles.' ends with a full stop",
    "\\subsubsection*{1.5. \\((AR,\\mathbb Z_\\ell)\\)-faisceaux constructibles}",
    "punctuation", "high", fx("-faisceaux constructibles}", "-faisceaux constructibles.}"),
    "Underlined title: the full stop dropped.")

add(270, "Définition 1.5.1, 'Un objet F de Hom(N°, Ab(X)) est appelé ...'",
    "Hom underlined (the functor category)",
    "\\(\\Hom(\\mathbb N^\\circ,\\Ab(X))\\)",
    "underline", "high", fx("\\Hom(\\mathbb N^\\circ", "\\uHom(\\mathbb N^\\circ"),
    "As the logged \\uHom(\\mathbb N^\\circ,\\Ab(X)) of p. 252.")

add(270, "Définition 1.5.1, 'est appelé un (AR- Z_l)-faisceau constructible'",
    "'(AR- Z_ℓ)': a hyphen after AR, where the title above and p. 271 have '(AR, Z_ℓ)' with a comma",
    "\\((AR,\\mathbb Z_\\ell)\\)-faisceau constructible",
    "misprint_in_print", "high", fx("un \\((AR,", "un \\((AR\\text{-}"),
    "Typing slip, a hyphen for the comma; the TeX silently corrects it. The fix restores the printed hyphen (\\text{-}, as in \\mathbb Z_\\ell\\text{-}\\fc(X)). Does not overlap the \\uHom item.",
    corrected="(AR,\\mathbb Z_\\ell)")

# ---------------- checks ----------------
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
s5 = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5\diplomatic\s5.tex").read_text(encoding="utf-8")
ms = list(MARK.finditer(s5))
span = {}
for i, m in enumerate(ms):
    span[int(m.group(2))] = s5[m.start():(ms[i + 1].start() if i + 1 < len(ms) else len(s5))]

ok = True
for d in F:
    if d["fix"] is None:
        continue
    t = (B / f"page_{d['page']:03d}.tex").read_text(encoding="utf-8")
    old = d["fix"]["old"]
    n = t.count(old)
    n5 = span.get(d["page"], "").count(old)
    if n != 1 or "%%%%%%%%%%" in old:
        ok = False
    print(d["page"], d["kind"], "page file:", n, "| s5 span now:", n5, "|", repr(old)[:60])
counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0])
    c[1 if d["kind"] == "misprint_in_print" else 0] += 1
print("counts", counts, "total", len(F), "ok" if ok else "NOT OK")
if ok:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
    print("written", OUT)
