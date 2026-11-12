import json, pathlib, sys
from collections import Counter
sys.stdout.reconfigure(encoding='utf-8')
B = pathlib.Path(r'C:\Users\user\Documents\sga_scan_check_20261105\run_6\b241_245')
OUT = pathlib.Path(r'C:\Users\user\Documents\sga_scan_check_20261105\run_6\findings_241_245.json')


def fx(old, new):
    return {"old": old, "new": new}


F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    e = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if corrected is not None:
        e["corrected"] = corrected
    e["note"] = note
    F.append(e)


# ---- p. 241
add(241, "Scholie 2.6, 'mettre en oeuvre de nouvelles techniques'",
    "oeuvre: o and e typed as two letters (main scan, crops_241_245/p241_oeuvre.png)",
    "en œuvre (ligature)", "word", "medium",
    fx("en œuvre", "en oeuvre"),
    "The typewriter has no œ; this is the only œ of main.tex (both layers), which keeps the typed 'oeuvre' elsewhere ('mettra probablement en oeuvre', Exposé XIV).")

add(241, "statements of Définition 3.1 (p. 241), Proposition 3.3 (p. 242), Corollaires 3.4 and 3.4.1 (pp. 243-244), Proposition 3.5 (p. 244), Corollaires 3.5.1 and 3.5.2 (p. 245)",
    "each statement underlined word group by word group: Déf. 3.1 'Soient', 'un morphisme de topos annelés', 'un intervalle de Z', 'On dit que', 'est', 'et l'on écrit', 'si', 'considéré comme complexe de', ...; Prop. 3.3 'Les données étant celles de', 'supposons que', 'ait assez de points', 'Les conditions suivantes sont alors équivalentes', (ii) 'pour tout point', 'de', 'on a'; Cor. 3.5.2 'Soit', 'un carré cartésien de schémas', 'où', 'et', 'sont supposés tor-indépendants', 'sur', 'et soit', 'Alors on a'",
    "roman throughout (only the bold labels and \\emph{Preuve.})", "underline", "high", None,
    "Exposé III follows the Exposé II pattern of GLOBAL_ISSUES 82, as reported for pp. 222 and 227 (findings_221_225, findings_226_230): one decision for the exposé, not itemized. On these pages no \\emph on defined terms (the print leaves 'd'amplitude plate' etc. plain inside the underlined statements, the TeX sets everything in roman) and no category L.")

# ---- p. 242
add(242, "Proposition 3.3 (ii), first word", "(ii) pour tout point x de X, on a: small p (main scan)",
    "\\item Pour tout point", "word", "high",
    fx(r"\item Pour tout point", r"\item pour tout point"), "")
add(242, "Proposition 3.3 (iii), first word", "(iii) pour tout objet V de Y: small p (main scan)",
    "\\item Pour tout objet", "word", "high",
    fx(r"\item Pour tout objet", r"\item pour tout objet"), "")
add(242, "Proposition 3.3 (iv), first word", "(iv) même condition que (iii): small m (main scan)",
    "\\item Même condition", "word", "high",
    fx(r"\item Même condition", r"\item même condition"), "")

add(242, "Proposition 3.3 (iii), display H^i((E|f^{-1}(V)) ⊗_V M) = 0, the restriction",
    "E|f^{-1}(V): f^{-1}(V) on the line after the bar (main scan, crops_241_245/p242_Lf.png)",
    "E\\vert_{f^{-1}(V)} (subscript)", "formula", "high",
    fx(r"H^i\left((E\vert_{f^{-1}(V)}", r"H^i\left((E|f^{-1}(V)"),
    "Restriction on the line, as asked (R|U). Independent of the index entry of the same display.")
add(242, "Proposition 3.3 (iii), display H^i((E|f^{-1}(V)) ⊗_V M) = 0, index of the tensor sign",
    "⊗ with L above and V below: index V (main scan, crops_241_245/p242_Lf.png)",
    "\\otimes_{\\mathcal O_V}^{\\mathbf L}", "formula", "high",
    fx(r"_{\mathcal O_V}^{\mathbf L}M\right", r"_V^{\mathbf L}M\right"),
    "The TeX writes out O_V where the print has V. \\mathbf L left as it is (see the L convention entry).")
add(242, "Proposition 3.3 (iii), 'où (E|f^{-1}(V)) ⊗_V M = ...', first restriction",
    "où (E|f^{-1}(V)) ⊗_V M: f^{-1}(V) on the line",
    "où \\((E\\vert_{f^{-1}(V)})", "formula", "high",
    fx(r"où \((E\vert_{f^{-1}(V)}", r"où \((E|f^{-1}(V)"),
    "Restriction on the line.")
add(242, "Proposition 3.3 (iii), 'où (E|f^{-1}(V)) ⊗_V M = ...', index of the first tensor sign",
    "⊗ with L above, index V",
    "\\otimes_{\\mathcal O_V}^{\\mathbf L}M=", "formula", "high",
    fx(r"_{\mathcal O_V}^{\mathbf L}M=", r"_V^{\mathbf L}M="),
    "As the display above.")
add(242, "Proposition 3.3 (iii), '... = (E|f^{-1}(V)) ⊗ Lf*(M) ;', second restriction and second tensor sign",
    "(E|f^{-1}(V)) ⊗ Lf*(M): f^{-1}(V) on the line; the ⊗ has only the L above it, no index (main scan, crops_241_245/p242_Lf.png)",
    "(E\\vert_{f^{-1}(V)})\\otimes_{\\mathcal O_V}^{\\mathbf L}\\mathbf Lf^*(M)", "formula", "high",
    fx(r"(E\vert_{f^{-1}(V)})\otimes_{\mathcal O_V}^{\mathbf L}\mathbf L", r"(E|f^{-1}(V))\otimes^{\mathbf L}\mathbf L"),
    "Two differences in one edit (the restriction, and the index O_V that the TeX adds to the bare ⊗); its text starts after the 'M=' of the previous entry, no overlap.")
add(242, "display before the end of the page, '((E|f^{-1}(V)) ⊗_V P)_x ≃ E_x ⊗_{O_{Y,y}} M ,', the restriction",
    "(E|f^{-1}(V)): f^{-1}(V) on the line",
    "\\bigl((E\\vert_{f^{-1}(V)})", "formula", "high",
    fx(r"\bigl((E\vert_{f^{-1}(V)}", r"\bigl((E|f^{-1}(V)"),
    "Restriction on the line.")
add(242, "display before the end of the page, '((E|f^{-1}(V)) ⊗_V P)_x', index of the tensor sign",
    "⊗ with L above, index V",
    "\\otimes_{\\mathcal O_V}^{\\mathbf L}P", "formula", "high",
    fx(r"_{\mathcal O_V}^{\mathbf L}P", r"_V^{\mathbf L}P"),
    "As in (iii).")
add(242, "derived tensor products and Lf*, Lg* of pp. 242-245 (31 places)",
    "plain typed L (one stem, typewriter face), set above the ⊗; the L of Lf*(M) (p. 242), Lf*(F) (p. 244) and Lg* (p. 245, three times) also plain typed (crops_241_245/p242_Lf.png, p244_Lf.png, p245_Lg.png); no double-struck L or R on these pages",
    "\\mathbf L (bold) at all 31 places", "font", "high", None,
    "Convention of the Exposé III transcription, reported once: main.tex has 146 \\mathbf L and no \\mathrm L in Exposé III, while Exposé I writes this typed L as \\mathrm L (\\overset{\\mathrm L}{\\otimes}). Three examples: p. 242 (*) H^i(E_x\\otimes_{\\mathcal O_{Y,y}}^{\\mathbf L}M)=0; p. 244 \\toramp_h(\\mathbf Lf^*(F)); p. 245 \\mathbf Lg^*:D(f)_{\\mathrm{torf}}\\longrightarrow D(f')_{\\mathrm{torf}}. One decision for the exposé; the edits of this file keep \\mathbf L, so apply them before any scripted change of it.")

# ---- p. 243
add(243, "Preuve of 3.4, display H^i(((E ⊗_Y F)|h^{-1}(Z')) ⊗_{Z'} M) = 0",
    "(E ⊗_Y F)|h^{-1}(Z'): h^{-1}(Z') on the line",
    "\\vert_{h^{-1}(Z')}", "formula", "high",
    fx(r"\vert_{h^{-1}(Z')}", r"|h^{-1}(Z')"), "Restriction on the line.")
add(243, "Preuve of 3.4, second display, first member ((E ⊗_Y F)|X') ⊗_{Z'} M",
    "(E ⊗_Y F)|X': X' on the line",
    "(E\\otimes_Y^{\\mathbf L}F)\\vert_{X'}", "formula", "high",
    fx(r"F)\vert_{X'}", r"F)|X'"), "Restriction on the line.")
add(243, "Preuve of 3.4, second display, '(E|X') ⊗_{Y'}'",
    "(E|X'): X' on the line",
    "(E\\vert_{X'})", "formula", "high",
    fx(r"(E\vert_{X'})", r"(E|X')"), "Restriction on the line.")
add(243, "Preuve of 3.4, second display, '((F|Y') ⊗_{Z'} M)'",
    "(F|Y'): Y' on the line",
    "(F\\vert_{Y'})", "formula", "high",
    fx(r"(F\vert_{Y'})", r"(F|Y')"), "Restriction on the line.")

# ---- p. 244
add(244, "Corollaire 3.4.1 b), first line, 'si f est de tor-dimension ≤ m'",
    "tor-dimension, one word (main scan, crops_241_245/p244_tordim.png)",
    "tor- (line end) dimension: the line end sets a space, 'tor- dimension'", "other", "high",
    fx("tor-\ndimension", "tor-dimension"),
    "Both layers have the line break (diplomatic main.tex lines 5888-5889). The only other such break in main.tex is in the index table ('de tor-' / 'dimension finie & I & 5.2', near line 17188), outside these pages.")

# ---- p. 245
add(245, "start of page (folio-245 marker)",
    "p. 245 begins 'catégorie dérivée D(B) des B-modules'; p. 244 ends '... est canoniquement isomorphe, dans la' (main scan; OCR of p. 245 begins 'catégorie dérivée')",
    "'catégorie' is the last word of page_244.tex ('... dans la catégorie'); page_245.tex begins 'dérivée \\(D(B)\\)'",
    "marker", "high", None,
    "Page 245 really begins with 'catégorie'. Move the folio-245 marker before it: python -I move_marker.py 6 245 \"catégorie\" --before (simulated in memory on both layers of the live main.tex with crops_241_245/sim_marker.py: '... isomorphe, dans la ' / the marker / 'catégorie' / 'dérivée \\(D(B)\\) des \\(B\\)-modules, ...'). Apply once: a second run would take an earlier 'catégorie'.")
add(245, "end of page_245.tex, macro block '% Additions for Exposé III, pages 253--280' (live main.tex line 5948)",
    "the print types 'ob' (E ∈ ob D(X)) on pp. 241-245 (6 places, main scan) and, by the OCR, on every page 246-280 (e.g. p. 246 'E ∈ ob D(X)', p. 260 'ob Mod(X)', p. 274 'ob C', p. 280 'ob D'); the OCR keeps capital 'Ob' where p. 222 has it, so its case is reliable",
    "\\renewcommand{\\Ob}{\\operatorname{Ob}}", "word", "high",
    fx(r"\renewcommand{\Ob}{\operatorname{Ob}}", r"\renewcommand{\Ob}{\operatorname{ob}}"),
    "The live main.tex already prints 'ob' for pp. 222-245 (line 5323 changed to \\operatorname{ob}, so the six \\Ob of pp. 241-245, still 'Ob' in the page snapshots, need no edit), but this second \\renewcommand, after the last display of p. 245, switches \\Ob back to 'Ob' for pp. 246-280. Page 245's own text is not affected. Per-page \\ob edits of later batches stay harmless after this change. The same line recurs in main.tex for later exposés (lines 6540, 7189, 13288, 17025): apply this edit inside the folio-245 span only.")

# ---- check and write
bad = 0
for e in F:
    if e["fix"] is None:
        continue
    t = (B / f"page_{e['page']}.tex").read_text(encoding="utf-8")
    n = t.count(e["fix"]["old"])
    if n != 1:
        bad += 1
        print("NOT UNIQUE", e["page"], n, repr(e["fix"]["old"]))
    if "%%%%%%%%%%" in e["fix"]["old"]:
        bad += 1
        print("MARKER IN OLD", e["page"])
print("entries", len(F), "bad", bad)
print(Counter(e["page"] for e in F))
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
