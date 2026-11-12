import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = r"C:\Users\user\Documents\sga_scan_check_20261105"
B = W + r"\run_6\b281_285"
OUT = W + r"\run_6\findings_281_285.json"


def L(*parts):
    return "\n".join(parts)


F = []


def add(page, where, scan, tex, kind, confidence, old=None, new=None, corrected=None, note=""):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": confidence,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 281 ----------------
add(281, "throughout pp. 281-285 (Exposé IV)",
    "K with a raised dot, K˙ (the contravariant group; the lower-dot K. is K_\\bullet): e.g. p. 281 '2.6. Accouplements entre K˙ et K˙', p. 283 '(2.7.1) f* : K˙(_AX) --> K˙(_A'X')', p. 285 '2.9. Comparaison de K˙ et K˙_naïf' (crops: the dot is round and raised, unlike the primes of X', A')",
    "K' (a prime) everywhere: 67 times on pp. 281-285 (7, 15, 13, 20, 12), 150 times in Exposé IV (main.tex lines 6567-7198); \\providecommand{\\Kprime}{K'} is defined but unused",
    "symbol", "high",
    note="Convention of the transcription, reported once and not itemized: replace K' by K^{\\bullet} throughout Exposé IV (the TeX already writes K_\\bullet for the lower dot and Exposé 0 writes K^\\bullet). Every K' on pp. 281-285 is the print's K˙ (no real prime K' on these pages); p. 278 '2. Les foncteurs K. et K˙' likewise.")
add(281, "throughout pp. 281-283 (Exposé IV): every D(...)_parf",
    "parf underlined in every subscript: p. 281 D(_AX)_parf = D^b(_AX)_coh, D(_A'X'_A)_{A'-parf} (twice); p. 282 (2.6.4) three times; p. 283 D(_AX)_parf dans D(_A'X')_parf; also p. 278 (2.1). coh is not underlined",
    "\\parf, which prints plain parf (\\providecommand at line 3387 = \\operatorname{parf}; Exposé IV's \\providecommand{\\parf}{\\mathrm{parf}} has no effect)",
    "underline", "high",
    note="Convention, reported once and not itemized (8 places on pp. 281-283): for Exposé IV redefine \\parf as \\underline{\\mathrm{parf}} (restore after the exposé), or write \\underline{\\parf} at each place.")
add(281, "after (ii), 'Les hypothèses (i) et (ii)'",
    "'Les hypothèses (i) et (ii) sont satisfaites ...' starts an indented new paragraph (indent as '(i)', '(ii)'; the lines around start at the margin)",
    "runs on in the paragraph 'Alors on a, ... est un isomorphisme. Les hypothèses ...'",
    "other", "medium",
    old="isomorphisme. Les hypothèses", new=L("isomorphisme.", "", "Les hypothèses"),
    note="Missing paragraph break.")
add(281, "2.6, between the displays of the tensor product",
    "the display '⊗_A : Mod(_A'X'_A) x Mod(_AX) --> Mod(_A'X')' is followed directly by the display '(E',E) |--> E'⊗_{f^-1(A)} f^-1(E)'; no word between them (OCR likewise)",
    "'envoie' between the two displays",
    "extra", "high",
    old=L(r"\]", "envoie", r"\["), new=L(r"\]", r"\["),
    note="Word added by the transcription.")
add(281, "2.6, display (E',E) |--> E'⊗_{f^-1(A)} f^-1(E)",
    "no punctuation after f^-1(E)",
    "f^{-1}(E),",
    "punctuation", "high",
    old=L("f^{-1}(E),", ""), new=L("f^{-1}(E)", ""),
    note="Comma added at the end of the display.")
add(281, "2.6, after the display (E',E) |--> ...",
    "'induit un foncteur' (no 'et')",
    "et induit un foncteur",
    "extra", "high",
    old=L(r"\]", "et induit un foncteur"), new=L(r"\]", "induit un foncteur"),
    note="Word added by the transcription (with 'envoie' and the comma it turns the two displays into a sentence).")
add(281, "after (2.6.2), 'Notons D(_A'X'_A)'",
    "'Notons D(_A'X'_A) la catégorie dérivée' starts at the margin after the display (2.6.2), like 'L'application' and 'induit' on this page: the print runs on; the typescript indents its new paragraphs ('Les hypothèses' above)",
    "blank line (new paragraph) before 'Notons'",
    "other", "medium",
    old=L(r"\end{equation}", "", "Notons"), new=L(r"\end{equation}", "Notons"),
    note="Paragraph break the print does not have.")
add(281, "last display, K˙(_A'X'_A)_A' = k(D(_A'X'_A)_{A'-parf}",
    "k(D(_A'X'_A)_{A'-parf}   . : the parenthesis opened by k( is never closed (checked in a crop; the final full stop is there)",
    "k(D({}_{A'} X'_A)_{A'\\text{-}\\parf}). (closing parenthesis supplied)",
    "misprint_in_print", "high",
    old=r"\parf}).", new=r"\parf}.",
    corrected=r"k(D({}_{A'} X'_A)_{A'\text{-}\parf}).",
    note="Missing closing parenthesis in the print; the TeX silently corrected it. The fix restores the printed reading.")

# ---------------- page 282 ----------------
add(282, "display after 'le foncteur dérivé de ⊗_A,'",
    "L over ⊗ typed as a plain typewriter capital L (same weight as the A and D beside it; crop)",
    "\\otimes_A^{\\mathbf L}",
    "font", "high",
    old=r"\otimes_A^{\mathbf L}:D^-", new=r"\otimes_A^{\mathrm L}:D^-",
    note="Plain L as in Exposé III's global rule (\\mathrm L). Exposé IV has 8 more \\mathbf L for the derived tensor (main.tex lines 6893, 6920, 6921, 7013, 7017 (two), 7102, 7147), not checked here.")

# ---------------- page 283 ----------------
add(283, "heading 2.7",
    "'2.7. Loi contravariante et structure d'anneau sur K˙' with no full stop (crop); the heading stands on its own line and 'Nous allons expliciter' starts the next line at the margin",
    "\\textbf{2.7. Loi contravariante et structure d'anneau sur \\(K'\\).}",
    "punctuation", "medium",
    old=r"\).} Nous allons", new=r"\)} Nous allons",
    note="Full stop added inside the bold heading (the run-in layout itself is not reported).")
add(283, "a), after (2.7.2)",
    "qu'on peut encore interpréter comme le produit par cl(A') dans (2.6.2) (resp. (2.6.5))",
    "dans (2.6.2) (resp. (2.6.5)) (printed reading kept)",
    "misprint_in_print", "medium",
    corrected="dans (2.6.5) (resp. (2.6.2))",
    note="The references are swapped: (2.7.1) on K˙ is the product in the derived pairing (2.6.5), (2.7.2) on K˙_naïf the one in the naive pairing (2.6.2) (b) has the right order '(2.6.5) (resp. (2.6.2))'). The corrected layer already has it (RECONCILE_CODEX_6, SGA-SRC-001591); not yet in MISPRINTS_6.json.")
add(283, "end of a), 'Ainsi K˙(_AX) ...'",
    "'est un foncteur contravariant de' underlined (not (X,A))",
    "no underline",
    "underline", "high",
    old="est un foncteur contravariant de", new=r"\emph{est un foncteur contravariant de}",
    note="Exposé IV writes underlining as \\emph.")
add(283, "b), 'l'homomorphisme (2.6.5)'",
    "'l'homomorphisme' underlined",
    "no underline",
    "underline", "high",
    old="tensoriel, l'homomorphisme", new=r"tensoriel, \emph{l'homomorphisme}",
    note="")
add(283, "b), 'munit K˙(X)'",
    "'munit' underlined",
    "no underline",
    "underline", "high",
    old=r"\)) munit", new=r"\)) \emph{munit}",
    note="")
add(283, "b), last line of the page",
    "'d'une structure d'anneau commutatif avec unité' underlined; the page ends after 'unité'",
    "no underline",
    "underline", "high",
    old="d'une structure d'anneau commutatif avec unité", new=r"\emph{d'une structure d'anneau commutatif avec unité}",
    note="")
add(283, "last line of page_283.tex (printed on p. 284, line 1)",
    "p. 284 line 1: '(1 = cl(O_X)), et l'homomorphisme canonique (2.6.3.2)' with 'et l'homomorphisme canonique' underlined as one group",
    "'\\((1=\\cl(\\mathcal O_X))\\), et l'%' (under the folio-283 marker), no underline",
    "underline", "high",
    old=r"\), et l'%", new=r"\), \emph{et l'}%",
    note="One underline split by the misplaced p. 284 marker: apply together with the p. 284 fix '\\emph{homomorphisme canonique}'. If the p. 284 marker is moved first, this text lies on p. 284.")

# ---------------- page 284 ----------------
add(284, "start of page",
    "p. 284 begins '(1 = cl(O_X)), et l'homomorphisme canonique (2.6.3.2)'; p. 283 ends '... d'une structure d'anneau commutatif avec unité'",
    "'\\((1=\\cl(\\mathcal O_X))\\), et l'%' is at the end of the last line of page_283.tex (under the folio-283 marker); page_284.tex begins 'homomorphisme canonique'",
    "marker", "high",
    note="Page 284 really begins with '\\((1=\\cl(\\mathcal O_X))\\)'. Move the folio-284 marker up, splitting the line after 'avec unité': python -I move_marker.py 6 284 \"\\((1=\\cl(\\mathcal O_X))\\)\" --before (simulated in memory on both layers: '... avec unité' / marker / '\\((1=\\cl(\\mathcal O_X))\\), et l'%' / 'homomorphisme canonique (2.6.3.2)').")
add(284, "line 1, 'et l'homomorphisme canonique'",
    "'et l'homomorphisme canonique' underlined",
    "no underline on 'homomorphisme canonique'",
    "underline", "high",
    old="homomorphisme canonique (2.6.3.2)", new=r"\emph{homomorphisme canonique} (2.6.3.2)",
    note="Second half of the underline split by the marker; apply together with the p. 283 fix '\\emph{et l'}%'.")
add(284, "after the display K˙(X)_naïf --> K˙(X)",
    "'est un homomorphisme d'anneaux unifères' underlined (not the full stop)",
    "no underline",
    "underline", "high",
    old=L(r"\]", "est un homomorphisme d'anneaux unifères"), new=L(r"\]", r"\emph{est un homomorphisme d'anneaux unifères}"),
    note="")
add(284, "'montre que l'homomorphisme'",
    "'l'homomorphisme' underlined",
    "no underline",
    "underline", "high",
    old="montre que l'homomorphisme", new=r"montre que \emph{l'homomorphisme}",
    note="")
add(284, "after the (resp. f* : K˙(Y)_naïf --> K˙(X)_naïf) display",
    "'est un homomorphisme d'anneaux unifères' underlined (not the full stop)",
    "no underline",
    "underline", "high",
    old=") est un homomorphisme d'anneaux unifères", new=r") \emph{est un homomorphisme d'anneaux unifères}",
    note="")
add(284, "2.8, 'munissant ainsi ... (et par suite aussi K˙(X) via l'homomorphisme canonique K˙(X)_naïf --> K˙(X) d'une structure'",
    "the parenthesis opened at '(et par suite aussi' is never closed: 'K˙(X)_naïf --> K˙(X) d'une structure d'algèbre' (crop)",
    "\\(K'(X)_{\\naif}\\to K'(X)\\)) d'une structure d'algèbre (closing parenthesis supplied)",
    "misprint_in_print", "high",
    old=r"\)) d'une structure d'algèbre", new=r"\) d'une structure d'algèbre",
    corrected=r"\(K'(X)_{\naif}\to K'(X)\)) d'une structure d'algèbre",
    note="Missing closing parenthesis in the print; the TeX silently corrected it. The fix restores the printed reading.")
add(284, "2.8, 'par le rang'",
    "'rang' underlined",
    "no underline",
    "underline", "high",
    old="par le rang,", new=r"par le \emph{rang},",
    note="")

# ---------------- page 285 ----------------
add(285, "start of page",
    "p. 284 ends '(où rg désigne le rang) :'; p. 285 begins with the diagram H^o(Y,Z) --i--> K˙(Y)_naïf --> ...",
    "page_285.tex begins 'désigne le rang) :', then the diagram",
    "marker", "high",
    note="The folio-285 marker stands one line too early: 'désigne le rang) :' belongs to p. 284. Move the marker down before the diagram: python -I move_marker.py 6 285 \"\\[\" (no --before; simulated in memory on both layers: '(où \\(\\Rg\\)' / 'désigne le rang) :' / marker / '\\[' / '\\begin{tikzcd}...').")
add(285, "after the diagram, '* On verra dans la suite du Séminaire'",
    "'* On verra ...' starts an indented new paragraph (indent as '(i)', '(ii)' below; 'K˙(X)_naïf peut être muni' starts at the margin)",
    "runs on directly after the display: '\\]' then '\\textsuperscript{*}On verra'",
    "other", "medium",
    old=L(r"\]", r"\textsuperscript{*}On verra"), new=L(r"\]", "", r"\textsuperscript{*}On verra"),
    note="Missing paragraph break.")
add(285, "'(V 3.9.1 et VI       ) que'",
    "a blank of about six characters after 'VI' inside the parenthesis: a reference left to be filled in, never typed (crop; OCR likewise)",
    "(V 3.9.1 et VI) que (gap closed)",
    "misprint_in_print", "low",
    old="et VI) que", new=r"et VI\qquad) que",
    corrected="(V 3.9.1 et VI)",
    note="Unfilled reference: the typist left a blank for a number in VI that was never typed in; the TeX closed the gap. The diplomatic fix keeps the blank; the corrected layer keeps '(V 3.9.1 et VI)' (the intended reference in VI is not known).")
add(285, "'Deligne [5] a prouvé récemment'",
    "Deligne [5]",
    "Deligne [5] (printed reading kept)",
    "misprint_in_print", "high",
    corrected="Deligne [1]",
    note="The bibliography of Exposé IV (p. 296, OCR '[1] Deligne, P., papiers secrets'; main.tex: [1] Deligne, [2] Grauert, [3] Grothendieck, [V] Verdier) has no [5]. The corrected layer already reads [1] (RECONCILE_CODEX_6, SGA-SRC-001592); not yet in MISPRINTS_6.json.")
add(285, "'et que l'homomorphisme canonique K˙(X)_naïf --> K˙(X) est un homomorphisme de λ-algèbres'",
    "the map K˙(X)_naïf --> K˙(X) is inline at the start of a text line ('K˙(X)_naïf --> K˙(X) est un homomorphisme de λ-algèbres augmentées, répon-'), at the margin",
    "set as a display \\[ K'(X)_{\\naif}\\longrightarrow K'(X) \\]",
    "other", "high",
    old=L("canonique", r"\[", r" K'(X)_{\naif}\longrightarrow K'(X)", r"\]", "est un homomorphisme de"),
    new=r"canonique \(K'(X)_{\naif}\longrightarrow K'(X)\) est un homomorphisme de",
    note="Inline in the print, display in the TeX (the display of 2.9 below is a real display).")

# ---------------- checks ----------------
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")


def spans(edition):
    t = open(W + "\\sga6\\" + edition + "\\main.tex", encoding="utf-8", newline="").read()
    ms = list(MARK.finditer(t))
    out = {}
    for i, m in enumerate(ms):
        e = ms[i + 1].start() if i + 1 < len(ms) else len(t)
        out[int(m.group(2))] = t[m.start():e]
    return out


live = {"diplomatic": spans("diplomatic"), "current": spans("current")}
ok = True
for x in F:
    fx = x["fix"]
    if not fx:
        continue
    page_text = open(B + "\\page_%03d.tex" % x["page"], encoding="utf-8", newline="").read()
    n = page_text.count(fx["old"])
    nd = live["diplomatic"][x["page"]].count(fx["old"])
    nc = live["current"][x["page"]].count(fx["old"])
    flag = "" if n == 1 and nd == 1 else "  <-- PROBLEM"
    if flag:
        ok = False
    if MARK.search(fx["old"]) or MARK.search(fx["new"]):
        ok = False
        flag += " MARKER"
    print(x["page"], x["kind"], "file:", n, "live dipl:", nd, "live current:", nc, repr(fx["old"][:50]), flag)
counts = {}
for x in F:
    c = counts.setdefault(x["page"], [0, 0])
    c[1 if x["kind"] == "misprint_in_print" else 0] += 1
print("counts", counts, "total", len(F), "all ok" if ok else "PROBLEMS")
with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
print("written", OUT)
