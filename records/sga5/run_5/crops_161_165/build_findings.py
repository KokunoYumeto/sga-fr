"""Build findings_161_165.json; check that every fix's old occurs exactly once in its page_NNN.tex."""
import io
import json
import pathlib
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
B = W / "run_5" / "b161_165"
OUT = W / "run_5" / "findings_161_165.json"
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
NL = "\n"


def F(page, where, scan, tex, kind, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


L = []

# ---------------- page 161
L.append(F(161, "top of the page",
           "p. 161 begins 'B' ∪ X' . Notons E' l'image inverse de E sur T'-(A' ∪ D ∪ X') et'; p. 160 ends "
           "'... hypothèses de position générale sur A, B , X signifient que A' est disjoint de'",
           r"page_161.tex begins 'maximal de $T$, $D=f^{-1}(z)(\simeq\mathbb P^1_s)$ le diviseur exceptionnel' "
           r"and goes on to 'signifient que $A'$ est disjoint de' (s5.tex lines 5074-5075): the end of 'Prouvons 4.2', "
           r"printed at the foot of p. 160; the folio-161 marker (line 5073) follows 'l'éclatement de l'idéal'",
           "marker", "high", None, None,
           r"Page 161 really begins at '$B'\cup X'$. Notons' in s5.tex line 5075 (after 'signifient que $A'$ est "
           r"disjoint de '). Exact fix: python -I move_marker.py 5 161 " + '"' + r"\$B'\cup X'\$. Notons" + '"'
           + r" (bash, double quotes with \$; the anchor occurs once after the marker; simulated in memory on both "
           r"layers: the marker then splits line 5075 after 'est disjoint de ' and stands on its own line before "
           r"'$B'\cup X'$. Notons'). The moved text agrees with the print of p. 160 (page_160_s4.png, P^1_s included)."))

L.append(F(161, "display (*), target of the restriction arrow",
           "RΓ(B' ∪ D),i'_!(E')|B'-(B' ∪ D))  - a closing parenthesis after the first 'B' ∪ D', so the "
           "parentheses do not balance; both unions are printed ∪ (the ∩ of 'B'_j ∩ D' below is distinct)",
           r"\R\Gamma(B'\cup D,i'_!(E')|B'-(B'\cup D))",
           "misprint_in_print", "high",
           r"\R\Gamma(B'\cup D,i'_!(E')|B'-(B'\cup D))",
           r"\R\Gamma(B'\cup D),i'_!(E')|B'-(B'\cup D))",
           r"The printed target is garbled: an unbalanced ')' after 'B' ∪ D', and ∪ for ∩ (B'-(B'∪D) is empty). "
           r"The TeX silently drops the ')' and keeps the two ∪; the edit restores only the ')'. Intended reading "
           r"(medium confidence): the restriction to B'-(B'∩D), the disjoint union of the B'_j-b_j of the second "
           r"display, since B'_j ∩ D = {b_j}.",
           corrected=r"\R\Gamma(B'-(B'\cap D),i'_!(E')|B'-(B'\cap D))"))

# ---------------- page 162
L.append(F(162, "heading of Part II",
           "II. Correspondances équivariantes.  (underlined; full stop after the underline)",
           r"\section*{II. Correspondances équivariantes}",
           "punctuation", "high",
           r"\section*{II. Correspondances équivariantes}",
           r"\section*{II. Correspondances équivariantes.}",
           "Full stop of the underlined title dropped."))

L.append(F(162, "heading of §5",
           "5. - Traces non commutatives.  (underlined)",
           r"\subsection*{5. Traces non commutatives}",
           "punctuation", "high",
           r"\subsection*{5. Traces non commutatives}",
           r"\subsection*{5. - Traces non commutatives.}",
           "The print's ' -' after the number and the final full stop are dropped (as the §2 heading, p. 146)."))

L.append(F(162, "heading 5.0",
           "5.0. - Introduction.  (underlined)",
           r"\subsubsection*{5.0. Introduction}",
           "punctuation", "high",
           r"\subsubsection*{5.0. Introduction}",
           r"\subsubsection*{5.0. - Introduction.}",
           "The print's ' -' and the final full stop are dropped."))

L.append(F(162, "5.0, 'On dispose alors d'un homomorphisme trace (de nature locale)'",
           "trace underlined",
           "homomorphisme trace, (no emphasis)",
           "underline", "high",
           "homomorphisme trace",
           r"homomorphisme \emph{trace}",
           r"Exposé III B writes the print's underlining as \emph. Independent of the next edit."))

L.append(F(162, "5.0, same sentence",
           "trace (de nature locale)  - in parentheses, no commas, then the display (5.0.1)",
           "trace, de nature locale,",
           "punctuation", "high",
           ", de nature locale,",
           " (de nature locale)",
           "Parentheses of the print replaced by commas."))

L.append(F(162, "'défini par composition de la \"flèche d'évaluation\"'",
           "\"flèche d'évaluation\" between straight double quotes",
           "de la flèche d'évaluation (no quotes)",
           "punctuation", "high",
           "de la flèche d'évaluation",
           "de la ``flèche d'évaluation''",
           "Quotes dropped; ``...'' is the file's form for the print's straight quotes."))

L.append(F(162, "'avec l'inverse de l'isomorphisme canonique \"produit tensoriel\"'",
           "\"produit tensoriel\" between straight double quotes",
           "canonique produit tensoriel (no quotes)",
           "punctuation", "high",
           "canonique produit tensoriel",
           "canonique ``produit tensoriel''",
           "Quotes dropped."))

L.append(F(162, "'Par dérivation, 5.0.4, 5.0.5 donnent'",
           "5.0.4, 5.0.5 donnent",
           "5.0.4 et 5.0.5 donnent",
           "word", "high",
           "5.0.4 et 5.0.5 donnent",
           "5.0.4, 5.0.5 donnent",
           "The TeX writes 'et' for the print's comma."))

L.append(F(162, "'des flèches de D(K) :' before (5.0.6)",
           "colon after D(K)",
           r"des flèches de $D(K)$ (no colon)",
           "punctuation", "high",
           r"des flèches de $D(K)$",
           r"des flèches de $D(K)$:",
           "Colon dropped."))

L.append(F(162, "(5.0.7), first argument",
           "RHom_K(E;K)  - semicolon",
           r"\uRHom_K(E;K)",
           "misprint_in_print", "high",
           None, None,
           "Semicolon typed for the comma (RHom_K(E,K) in 5.0.6); the TeX keeps the printed reading.",
           corrected=r"\uRHom_K(E,K)"))

# ---------------- page 163
L.append(F(163, "'5.0.7 est un isomorphisme (comme on le vérifie ... où E = K) , et,'",
           "isomorphisme (comme on le vérifie facilement par réduction au cas où E = K) , et,",
           r"isomorphisme, comme on le vérifie facilement par réduction au cas où $E=K$, et,",
           "punctuation", "high",
           r"isomorphisme, comme on le vérifie facilement par réduction au cas où $E=K$, et",
           r"isomorphisme (comme on le vérifie facilement par réduction au cas où $E=K$), et",
           "Parenthesis of the print replaced by commas; one edit, both parentheses."))

L.append(F(163, "'on obtient un homomorphisme trace, de nature globale,'",
           "globale underlined (the comma after it is not)",
           "de nature globale, (no emphasis)",
           "underline", "high",
           "de nature globale,",
           r"de nature \emph{globale},",
           "On this page 'trace' is not underlined."))

L.append(F(163, "'(pour plus de détails, voir (SGA 6 I 7, 8)).'",
           "voir (SGA 6 I 7, 8)).",
           "voir SGA 6 I 7, 8).",
           "punctuation", "high",
           "voir SGA 6 I 7, 8).",
           "voir (SGA 6 I 7, 8)).",
           "Inner parentheses dropped."))

L.append(F(163, "'Nous nous proposons ici d'examiner dans qeulle mesure'",
           "qeulle",
           "dans quelle mesure",
           "misprint_in_print", "high",
           "dans quelle mesure",
           "dans qeulle mesure",
           "Typing error (u and e transposed); the TeX silently corrects it.",
           corrected="dans quelle mesure"))

L.append(F(163, "'la notion de trace \"non commutative\" introduite par Stallings'",
           "\"non commutative\" between straight double quotes",
           "trace non commutative introduite (no quotes)",
           "punctuation", "high",
           "trace non commutative introduite",
           "trace ``non commutative'' introduite",
           "Quotes dropped."))

L.append(F(163, "'développée par Grothendieck dans l'exposé XI de ce séminaire (comme on l'a dit ...'",
           "one sentence: '... de ce séminaire (comme on l'a dit dans l'introduction, cet exposé, rédigé par "
           "I. Bucur, a malheureusement été perdu ; le lecteur pourra ... les points essentiels). Si le remplacement'",
           "de ce séminaire. Comme on l'a dit ... les points essentiels. Si le (the parenthesis made a sentence)",
           "punctuation", "high",
           "de ce séminaire. Comme on l'a dit",
           "de ce séminaire (comme on l'a dit",
           "Opens the parenthesis; apply together with the edit 'les points essentiels). Si le', which closes it."))

L.append(F(163, "'se reporter à l'exposé de Deligne (SGA 4^{1/2} Rapport)'",
           "(SGA 4^{1/2} Rapport)  - no comma",
           r"(SGA $4^{1/2}$, Rapport)",
           "punctuation", "high",
           r"(SGA $4^{1/2}$, Rapport)",
           r"(SGA $4^{1/2}$ Rapport)",
           "Comma added by the TeX."))

L.append(F(163, "'où sont indiqués les points essentiels). Si le remplacement'",
           "essentiels). Si",
           "essentiels. Si",
           "punctuation", "high",
           "les points essentiels. Si le",
           "les points essentiels). Si le",
           "Closes the parenthesis opened at 'séminaire (comme'; apply both edits together."))

L.append(F(163, "'Si le remplacement de K par A dans 5.0.3 de présente pas de difficulté'",
           "de présente",
           "ne présente",
           "misprint_in_print", "high",
           "5.0.3 ne présente",
           "5.0.3 de présente",
           "Typing error 'de' for 'ne'; the TeX silently corrects it.",
           corrected="5.0.3 ne présente"))

L.append(F(163, "unnumbered display 'Hom_A(E,A) ⊗_K E → A , f ⊗ x ↦ f(x)'",
           "no punctuation after f(x); the sentence goes on 'ne se factorise pas'",
           r"f\otimes x\longmapsto f(x),",
           "punctuation", "high",
           r"\longmapsto f(x)," + NL + r"\]",
           r"\longmapsto f(x)" + NL + r"\]",
           "Comma added at the end of the display."))

# ---------------- page 164
L.append(F(164, "top of the page",
           "p. 164 begins with the display '(5.0.11) Tr_A : Hom_A(E,E) ⟶ A_♮ ,'; p. 163 ends '... en composant "
           "l'inverse de 5.0.10 avec 5.0.9, un homomorphisme trace'",
           r"'\begin{equation}\tag{5.0.11}' and '\Tr_A:\uHom_A(E,E)\longrightarrow A_\natural,' end page_163.tex "
           r"(s5.tex lines 5147-5148); the folio-164 marker (line 5149) sits inside the equation environment, "
           r"before '\end{equation}'",
           "marker", "high", None, None,
           r"Page 164 really begins at '\begin{equation}\tag{5.0.11}' (s5.tex line 5147). Exact fix: python -I "
           r"move_marker.py 5 164 '\begin{equation}\tag{5.0.11}' --before (single quotes; simulated in memory on "
           r"both layers: the marker then stands on its own line between '... un homomorphisme trace' and "
           r"'\begin{equation}\tag{5.0.11}'). The moved display agrees with the print."))

L.append(F(164, "'au n° 6, de termes locaux de Lefschetz-Verdier'",
           "au n° 6",
           "au numéro 6",
           "word", "high",
           "au numéro 6",
           r"au n\textsuperscript{o}~6",
           r"Abbreviation written out; n\textsuperscript{o}~ is the file's own form ('Au n\textsuperscript{o}~1', "
           r"Exposé III)."))

L.append(F(164, "'Lefschetz-Verdier'",
           "hyphen",
           "Lefschetz--Verdier (en dash)",
           "punctuation", "high",
           "Lefschetz--Verdier",
           "Lefschetz-Verdier",
           "En dash added by the TeX."))

L.append(F(164, "'de termes locaux de Lefschetz-Verdier \"non commutatifs\".'",
           "\"non commutatifs\" between straight double quotes",
           "« non commutatifs »",
           "punctuation", "high",
           "« non commutatifs »",
           "``non commutatifs''",
           "Guillemets are another sign; the accepted forms for the print's straight quotes are ``...'' and "
           "\"...\" (as batch 106-110)."))

L.append(F(164, "heading 5.1",
           "5.1.- Notations.  (underlined; no space between '5.1.' and '-')",
           r"\subsubsection*{5.1. Notations}",
           "punctuation", "high",
           r"\subsubsection*{5.1. Notations}",
           r"\subsubsection*{5.1.- Notations.}",
           "The print's '-' and the final full stop are dropped."))

L.append(F(164, "'Si E est un bimodule rappelons ([1] IX 4) que'",
           "no comma after 'bimodule'",
           "est un bimodule, rappelons",
           "punctuation", "high",
           "est un bimodule, rappelons",
           "est un bimodule rappelons",
           "Comma added by the TeX."))

L.append(F(164, "'par le sous K-module engendré localement par les sections locales de la forme ax - xa'",
           "sous K-module  - no hyphen after 'sous' (p. 163 prints sous-K-module)",
           r"sous-$K$-module",
           "misprint_in_print", "high",
           r"par le sous-$K$-module",
           r"par le sous $K$-module",
           "Hyphen omitted by the typist; the TeX silently supplies it.",
           corrected=r"par le sous-$K$-module"))

L.append(F(164, "'on utilisera la notation de Cartan-Eilenberg'",
           "hyphen",
           "Cartan--Eilenberg (en dash)",
           "punctuation", "high",
           "Cartan--Eilenberg",
           "Cartan-Eilenberg",
           "En dash added by the TeX."))

L.append(F(164, "end of the text of the page: '(resp. des A-B-bimodules, à gauche sur A , à droite sur B .'",
           "no closing parenthesis before the full stop",
           r"à droite sur $B$).",
           "misprint_in_print", "high",
           r"à droite sur $B$).",
           r"à droite sur $B$.",
           "The parenthesis opened at '(resp. des' is not closed in the print; the TeX silently closes it.",
           corrected=r"à droite sur $B$)."))

# ---------------- page 165
L.append(F(165, "top of the page",
           "p. 165 begins with the paragraph number: '5.2   Soient A , B des K-algèbres.'; p. 164 ends '... à "
           "droite sur B .' and the footnote",
           r"'\subsubsection*{5.2}' (s5.tex line 5163) ends page_164.tex; the folio-165 marker (line 5165) follows "
           r"it, so page_165.tex begins 'Soient $A$, $B$'",
           "marker", "high", None, None,
           r"Page 165 really begins at '\subsubsection*{5.2}' (s5.tex line 5163). Exact fix: python -I "
           r"move_marker.py 5 165 '\subsubsection*{5.2}' --before (single quotes; simulated in memory on both "
           r"layers: the marker then stands on its own line after the blank line that follows '... à droite sur "
           r"$B$).' and before '\subsubsection*{5.2}')."))

L.append(F(165, "'G borné inférieurement et à composantes injectives, on a alors'",
           "comma after 'injectives'",
           "injectives; on a alors",
           "punctuation", "high",
           "composantes injectives; on a alors",
           "composantes injectives, on a alors",
           "Semicolon for the print's comma."))

L.append(F(165, "'on a alors RHom_B(F ⊗^L_A E,G) = Hom•_B(F ⊗_A E,G) , RHom_B(F,G) = Hom•_B(F,G)'",
           "both Hom• underlined, as every Hom• of 5.2",
           r"\Hom_B^\bullet(F\otimes_AE,G), \Hom_B^\bullet(F,G) (not underlined)",
           "underline", "high",
           r"=\Hom_B^\bullet(F\otimes_AE,G)$, $\uRHom_B(F,G)=\Hom_B^\bullet(F,G)$",
           r"=\uHom_B^\bullet(F\otimes_AE,G)$, $\uRHom_B(F,G)=\uHom_B^\bullet(F,G)$",
           r"The print underlines all 11 Hom• of 5.2 (this edit and three more); the TeX writes \Hom^\bullet "
           r"without underline, against its own \uHom_K^\bullet on p. 162."))

L.append(F(165, "'et RHom_A(E,Hom•_B(F,G)) = Hom•_A(E,Hom•_B(F,G))'",
           "the three Hom• underlined",
           r"\Hom_B^\bullet, \Hom_A^\bullet (not underlined)",
           "underline", "high",
           r"$\uRHom_A(E,\Hom_B^\bullet(F,G))=\Hom_A^\bullet(E,\Hom_B^\bullet(F,G))$",
           r"$\uRHom_A(E,\uHom_B^\bullet(F,G))=\uHom_A^\bullet(E,\uHom_B^\bullet(F,G))$",
           "Underlined Hom• of the print."))

L.append(F(165, "'= Hom•_A(E,Hom•_B(F,G)) car, si E est acyclique'",
           "no comma before 'car'",
           r"(F,G))$, car, si",
           "punctuation", "high",
           ", car, si",
           " car, si",
           "Comma added by the TeX."))

L.append(F(165, "'donc Hom•_A(E,Hom•_B(F,G)) ≃ Hom•_B(F ⊗_A E,G) est acyclique'",
           "the three Hom• underlined",
           r"\Hom_A^\bullet, \Hom_B^\bullet (not underlined)",
           "underline", "high",
           r"donc $\Hom_A^\bullet(E,\Hom_B^\bullet(F,G))\simeq\Hom_B^\bullet(F\otimes_AE,G)$",
           r"donc $\uHom_A^\bullet(E,\uHom_B^\bullet(F,G))\simeq\uHom_B^\bullet(F\otimes_AE,G)$",
           "Underlined Hom• of the print."))

L.append(F(165, "'est acyclique ; pour E et G comme ci-dessus'",
           "semicolon and small p",
           "est acyclique. Pour",
           "punctuation", "high",
           "est acyclique. Pour",
           "est acyclique; pour",
           "Full stop and capital for the print's semicolon."))

L.append(F(165, "isomorphism 'Hom•_A(E,Hom•_B(F,G)) ⟶~ Hom•_B(F ⊗_A E,G) défini par 5.2.1'",
           "the three Hom• underlined",
           r"\Hom_A^\bullet, \Hom_B^\bullet (not underlined)",
           "underline", "high",
           r"\Hom_A^\bullet(E,\Hom_B^\bullet(F,G))\xrightarrow{\sim}\Hom_B^\bullet(F\otimes_AE,G)",
           r"\uHom_A^\bullet(E,\uHom_B^\bullet(F,G))\xrightarrow{\sim}\uHom_B^\bullet(F\otimes_AE,G)",
           "Underlined Hom• of the print (run into the text there; the display is a layout variant)."))

L.append(F(165, "(5.2.3)",
           "Hom_A(E,RHom_B(F,G)) ⟶~ Hom_B(F ⊗^L_A E,G) .  - the two outer Hom are not underlined (only the "
           "Hom of RHom is)",
           r"\uHom_A(E,\uRHom_B(F,G))\xrightarrow{\sim}\uHom_B(F\lten_AE,G).",
           "underline", "high",
           r"\uHom_A(E,\uRHom_B(F,G))\xrightarrow{\sim}\uHom_B(F\lten_AE,G).",
           r"\Hom_A(E,\uRHom_B(F,G))\xrightarrow{\sim}\Hom_B(F\lten_AE,G).",
           "The plain Hom of the derived categories D(A), D(B); the TeX underlines them."))

L.append(F(165, "paragraph number 5.3",
           "5.3.  (full stop; 5.2 is printed without one)",
           r"\subsubsection*{5.3}",
           "punctuation", "high",
           r"\subsubsection*{5.3}",
           r"\subsubsection*{5.3.}",
           "Full stop dropped."))

L.append(F(165, "(5.3.2), second arrow",
           "f ⊗ x ⟶ f(x)  - a plain arrow, no bar",
           r"f\otimes x\longmapsto f(x)",
           "symbol", "high",
           r"f\otimes x\longmapsto f(x)",
           r"f\otimes x\longrightarrow f(x)",
           r"\longmapsto for the print's plain arrow (the other maps-to arrows of pp. 162-165 have the bar)."))

# ---------------- checks
pages = {p: (B / f"page_{p}.tex").read_text(encoding="utf-8") for p in range(161, 166)}
cur = (W / "sga5" / "current" / "s5.tex").read_text(encoding="utf-8")
cms = list(MARK.finditer(cur))
cspan = {}
for i, m in enumerate(cms):
    f = int(m.group(2))
    if 161 <= f <= 165:
        cspan[f] = cur[m.start():cms[i + 1].start()]
ok = True
for d in L:
    fx = d["fix"]
    if fx is None:
        continue
    t = pages[d["page"]]
    n = t.count(fx["old"])
    nc = cspan[d["page"]].count(fx["old"])
    bad = n != 1 or MARK.search(fx["old"]) or fx["old"] == fx["new"]
    if bad:
        ok = False
    print(d["page"], "OK " if not bad else "BAD", n, "current:", nc, "|", fx["old"][:70].replace(NL, "\\n"))
# non-overlap of olds on each page
for p in range(161, 166):
    spans = []
    for d in L:
        if d["page"] == p and d["fix"]:
            k = pages[p].find(d["fix"]["old"])
            spans.append((k, k + len(d["fix"]["old"]), d["fix"]["old"][:30]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            ok = False
            print("OVERLAP", p, a, b)
cnt = {}
for d in L:
    c = cnt.setdefault(d["page"], [0, 0])
    c[1 if d["kind"] == "misprint_in_print" else 0] += 1
print("counts", cnt, "total", len(L))
if ok:
    OUT.write_text(json.dumps(L, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("written", OUT)
else:
    print("NOT written")
