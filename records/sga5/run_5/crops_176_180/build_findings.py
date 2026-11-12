"""Build findings_176_180.json (SGA 5, pp. 176-180) and check every fix:
- old occurs exactly once in its batch page file (the four 5.10.10 edits: in the live page 176, see LIVE_ONLY);
- applied in order, each old occurs exactly once on its live page (diplomatic; current for non-misprints)."""
import json
import pathlib
import sys

sys.path.insert(0, r"C:\Users\user\Documents\sga_scan_check_20261105")
from sga_config import pages  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
B = RUN / "b176_180"
OUT = RUN / "findings_176_180.json"

LIVE_NOTE = ("Printed on p. 176. This diagram's TeX stood in page_175.tex when this batch was cut; the folio-176 "
             "marker has since been moved before \\begin{equation}\\tag{5.10.10} (marker finding of p. 175), so the "
             "diagram now opens page 176 of s5.tex, where this old occurs once (both layers).")


def F(page, where, scan, tex, kind, conf, old, new, note="", corrected=None, live_only=False):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    d["_live_only"] = live_only
    return d


L = []

# ---------------------------------------------------------------- page 176
L.append(F(176, "diagram (5.10.10), upper left corner",
           "RHom_B(E,B ⊗_K M) ⊗^L_B E : the L stands over ⊗_B only; B ⊗_K M is plain",
           r"\uRHom_B(E,B\lten_KM)\lten_BE", "formula", "high",
           r"B\lten_KM)\lten_BE \arrow", r"B\otimes_KM)\lten_BE \arrow",
           LIVE_NOTE + " As on pp. 174-175, the print writes B ⊗_K M inside RHom without L.", live_only=True))
L.append(F(176, "diagram (5.10.10), upper right corner", "M ⊗_K B_♮ (no L)", r"M\lten_KB_\natural",
           "formula", "high", r"& M\lten_KB_\natural \arrow[d", r"& M\otimes_KB_\natural \arrow[d",
           LIVE_NOTE, live_only=True))
L.append(F(176, "diagram (5.10.10), lower left corner",
           "RHom_A(E,A ⊗_K M) ⊗^L_A E : the L stands over ⊗_A only; A ⊗_K M is plain",
           r"\uRHom_A(E,A\lten_KM)\lten_AE", "formula", "high",
           r"A\lten_KM)\lten_AE \arrow", r"A\otimes_KM)\lten_AE \arrow", LIVE_NOTE, live_only=True))
L.append(F(176, "diagram (5.10.10), lower right corner", "M ⊗_K A_♮ . (no L)", r"M\lten_KA_\natural .",
           "formula", "high", r"& M\lten_KA_\natural .", r"& M\otimes_KA_\natural .", LIVE_NOTE, live_only=True))
L.append(F(176, "paragraph after the diagram, first word",
           "(Les hypothèses supplémentaires sur A et B (vérifiées ...) ... remplacé par A ⊗^L_{A^e} A "
           "(resp. B ⊗^L_{B^e} B) ).  The whole paragraph stands in parentheses.",
           "Les hypothèses supplémentaires ... (resp. $B\\lten_{B^e}B$).", "punctuation", "high",
           "Les hypothèses supplémentaires", "(Les hypothèses supplémentaires",
           "Opening parenthesis left out; apply together with the next edit (its closing parenthesis)."))
L.append(F(176, "same paragraph, end", "(resp. B ⊗^L_{B^e} B) ).", r"(resp. $B\lten_{B^e}B$).", "punctuation",
           "high", r"(resp. $B\lten_{B^e}B$).", r"(resp. $B\lten_{B^e}B$)).",
           "Closes the parenthesis opened before 'Les hypothèses'; apply together with the previous edit."))
L.append(F(176, "first formula after 'On a alors', left-hand side",
           "RHom_B(E,B ⊗_K M) ⊗^L_B E = ... : no L over ⊗_K inside RHom", r"\uRHom_B(E,B\lten_KM)\lten_BE=",
           "formula", "high", r"B\lten_KM)\lten_BE=", r"B\otimes_KM)\lten_BE="))
L.append(F(176, "same formula, right-hand side", "Hom˙_B(E,B ⊗_K M) ⊗_B E with Hom underlined",
           r"\Hom_B^\bullet(E,B\otimes_KM)", "underline", "high", r"\Hom_B^\bullet", r"\uHom_B^\bullet",
           "The complex Hom^•_B is underlined in the print, as the Hom_B of the square (*) below."))
L.append(F(176, "second formula, left-hand side",
           "RHom_A(E,A ⊗_K M) ⊗^L_A E = ... : no L over ⊗_K inside RHom", r"\uRHom_A(E,A\lten_KM)\lten_AE=",
           "formula", "high", r"A\lten_KM)\lten_AE=", r"A\otimes_KM)\lten_AE="))
L.append(F(176, "same formula, right-hand side", "Hom˙_A(E, A ⊗_K M) ⊗_A E with Hom underlined",
           r"\Hom_A^\bullet(E,A\otimes_KM)", "underline", "high", r"\Hom_A^\bullet", r"\uHom_A^\bullet"))
L.append(F(176, "last lines: 'la flèche horizontale supérieure (resp. inférieure de (*)'",
           "(resp. inférieure de (*) s'identifie : no closing parenthesis after 'inférieure' (the words "
           "'inférieure de' are retyped, darker; nothing between them)",
           "(resp. inférieure) de (*)", "misprint_in_print", "high", "inférieure) de", "inférieure de",
           "The '(resp.' is never closed in the print; the TeX silently supplies the parenthesis. The edit "
           "restores the printed reading (diplomatic layer only).", corrected="inférieure) de"))

# ---------------------------------------------------------------- page 177
L.append(F(177, "top of the page",
           "p. 177 begins 'de Tr_B : B ⟶ B_♮ (resp. ev : Hom_A(B,A) ⊗_A B ⟶ A_♮ ) par la flèche "
           "d'évaluation'; p. 176 ends 'au produit tensoriel (sur K)'",
           "'de $\\Tr_B:B\\to B_\\natural$ (' ends the last line of page_176.tex, before the folio-177 marker; "
           "page_177.tex opens with 'resp. $\\mathrm{ev}:...'", "marker", "high", None, None,
           "Page 177 really begins at 'de $\\Tr_B:B\\to B_\\natural$ (resp.'. The marker also splits '(' from "
           "'resp.' (the line end prints '( resp.'). Exact fix: python -I marker_split_word.py 5 177 pull "
           "'de $\\Tr_B:B\\to B_\\natural$ ('  (simulated in memory on both layers: '... au produit tensoriel "
           "(sur $K$)' / marker / 'de $\\Tr_B:B\\to B_\\natural$ (resp. $\\mathrm{ev}:\\uHom_A(B,A)...'). "
           "Text not moved."))
L.append(F(177, "Corollaire 5.10.11, label", "Corollaire 5.10.11 - Sous les hypothèses de 5.10.9, ...",
           r"\begin{statement}{Corollaire 5.10.11}", "punctuation", "high",
           r"\begin{statement}{Corollaire 5.10.11}", r"\begin{statement}{Corollaire 5.10.11 -}",
           "Run-in label with ' -', as in Exposé III."))
L.append(F(177, "statement of Corollaire 5.10.11, before the diagram",
           "underlined: 'Sous les hypothèses de' | 'pour' | 'on a un carré commutatif de'; not underlined: "
           "'5.10.9,', the formulas, 'D(K)'", "no underline", "underline", "high",
           r"Sous les hypothèses de 5.10.9, pour $E\in\ob D(B)_{\mathrm{parf}}$, $M\in\ob D^b(K)$, on a un carré "
           r"commutatif de $D(K)$",
           r"\emph{Sous les hypothèses de} 5.10.9, \emph{pour} $E\in\ob D(B)_{\mathrm{parf}}$, $M\in\ob D^b(K)$, "
           r"\emph{on a un carré commutatif de} $D(K)$",
           "\\emph is this file's command for the print's underline in statements (as p. 146)."))
L.append(F(177, "diagram (5.10.12), upper right corner", "M ⊗_K B_♮ (no L)", r"M\lten_KB_\natural", "formula",
           "high", r"& M\lten_KB_\natural", r"& M\otimes_KB_\natural"))
L.append(F(177, "diagram (5.10.12), right vertical arrow",
           "plain arrow M ⊗_K B_♮ ⟶ M ⊗_K A_♮, no label (only the horizontal arrows are labelled, Tr_B and Tr_A)",
           r'\arrow[d,"M\lten\Tr_{B/A}"]', "extra", "high",
           r'\arrow[d,"M\lten\Tr_{B/A}"]', r"\arrow[d]",
           "The TeX adds the label 'M ⊗^L Tr_{B/A}', which the print does not have here."))
L.append(F(177, "diagram (5.10.12), lower right corner", "M ⊗_K A_♮ , (no L)", r"M\lten_KA_\natural,",
           "formula", "high", r"M\lten_KA_\natural,", r"M\otimes_KA_\natural,"))
L.append(F(177, "statement of Corollaire 5.10.11, after the diagram",
           "'où la flèche verticale de gauche est la restriction des scalaires' underlined (the full stop is not)",
           "no underline", "underline", "high",
           "où la flèche verticale de gauche est la restriction des scalaires.",
           r"\emph{où la flèche verticale de gauche est la restriction des scalaires}."))
L.append(F(177, "title 5.11", "5.11. Application aux groupes finis : propriétés de divisibilité.  (underlined, "
           "full stop)", r"\subsubsection*{5.11. Application aux groupes finis: propriétés de divisibilité}",
           "punctuation", "high", "propriétés de divisibilité}", "propriétés de divisibilité.}",
           "Full stop at the end of the underlined title."))
L.append(F(177, "Proposition 5.11.1, label", "Proposition 5.11.1 - (cf. SGA 4^{1/2} Rapport 4.5). ...",
           r"\begin{statement}{Proposition 5.11.1}", "punctuation", "high",
           r"\begin{statement}{Proposition 5.11.1}", r"\begin{statement}{Proposition 5.11.1 -}"))
L.append(F(177, "Proposition 5.11.1, reference at the start",
           "(cf. SGA 4^{1/2} Rapport 4.5).  (in parentheses, small 'cf.', no comma; the whole parenthesis is "
           "underlined, the full stop after it is not)",
           r"Cf. SGA $4^{1/2}$, Rapport 4.5.", "punctuation", "high",
           r"Cf. SGA $4^{1/2}$, Rapport 4.5.", r"\emph{(cf. SGA $4^{1/2}$ Rapport 4.5)}.",
           "Parentheses, small c and no comma as printed; the new text also carries the parenthesis's underline "
           "(part of the statement's underline, next two findings)."))
L.append(F(177, "statement of Proposition 5.11.1, 'Soient ... Pour'",
           "underlined: 'Soient', 'Pour'; the formulas are not", "no underline", "underline", "high",
           r"Soient $E\in\ob D(B)_{\mathrm{parf}}$, $M\in\ob D^b(K)$. Pour $u",
           r"\emph{Soient} $E\in\ob D(B)_{\mathrm{parf}}$, $M\in\ob D^b(K)$. \emph{Pour} $u"))
L.append(F(177, "statement of Proposition 5.11.1, 'u ∈ Hom_B(E,M ⊗^L_K E) , on a, dans'",
           "Hom_B is NOT underlined here (Hom in D(B)); 'on a' and 'dans' are underlined",
           r"$u\in\uHom_B(E,M\lten_KE)$, on a, dans", "underline", "high",
           r"\in\uHom_B(E,M\lten_KE)$, on a, dans", r"\in\Hom_B(E,M\lten_KE)$, \emph{on a}, \emph{dans}",
           "Plain (global) Hom, as on p. 181 (5.13.3); the edit also underlines 'on a' and 'dans' as the print."))
L.append(F(177, "formula of Proposition 5.11.1 and its footnote",
           "Tr_K(u) = |G| Tr_B(u)(e) ^(*) .  : no equation tag; the raised (*) after Tr_B(u)(e) is the call "
           "of the footnote '(*) Si X est un ensemble, on note |X| le cardinal de X .'",
           r"\begin{equation}\tag{*} \Tr_K(u)=|G|\footnote{...}\,\Tr_B(u)(e). \end{equation}", "other", "high",
           "\\begin{equation}\\tag{*}\n\\Tr_K(u)=|G|\\footnote{Si $X$ est un ensemble, on note $|X|$ le cardinal "
           "de $X$.}\\,\\Tr_B(u)(e).\n\\end{equation}",
           "\\[\n\\Tr_K(u)=|G|\\,\\Tr_B(u)(e)\\footnote{Si $X$ est un ensemble, on note $|X|$ le cardinal de "
           "$X$.}.\n\\]",
           "The TeX tags the formula (*) and puts the footnote call after |G|; the print has one (*), the "
           "footnote call, after Tr_B(u)(e), and no tag (the (*) cited on p. 178 is the tagged display there)."))
L.append(F(177, "'en notant que Tr_{B/K} : B_♮ ⟶ K est donné par'", "est donné par", "est donnée par", "word",
           "high", "est donnée par", "est donné par", "The print has the masculine 'donné'."))
L.append(F(177, "display (5.11.2)", "Tr_{B/K}(g) = { |G| si g = e / 0 si g ≠ e } .  ('si' before each "
           "condition, no commas)", "|G|,& g=e,\\\\\n0,& g\\ne e.", "word", "high",
           "|G|,& g=e,\\\\\n0,& g\\ne e.", "|G| & \\text{si } g=e\\\\\n0 & \\text{si } g\\ne e.",
           "The TeX replaces the print's 'si' by commas (as on p. 146)."))
L.append(F(177, "Proposition 5.11.3, label", "Proposition 5.11.3 - Sous les hypothèses de 5.11.1, ...",
           r"\begin{statement}{Proposition 5.11.3}", "punctuation", "high",
           r"\begin{statement}{Proposition 5.11.3}", r"\begin{statement}{Proposition 5.11.3 -}"))
L.append(F(177, "statement of Proposition 5.11.3, first clause",
           "underlined: 'Sous les hypothèses de' | 'soit' | 'notons' | 'le centralisateur de' | 'dans'; numbers "
           "and formulas not", "no underline", "underline", "high",
           r"Sous les hypothèses de 5.11.1, soit $g\in G$, notons $Z_g$ le centralisateur de $g$ dans $G$,",
           r"\emph{Sous les hypothèses de} 5.11.1, \emph{soit} $g\in G$, \emph{notons} $Z_g$ \emph{le centralisateur "
           r"de} $g$ \emph{dans} $G$,"))
L.append(F(177, "statement of Proposition 5.11.3, 'G , posons A = K[Z_g] . Soit'",
           "'dans G , posons A = K[Z_g] .' : no 'et' ('posons' and 'Soit' underlined)",
           r"$G$, et posons $A=K[Z_g]$. Soit", "extra", "high",
           r"et posons $A=K[Z_g]$. Soit $u", r"\emph{posons} $A=K[Z_g]$. \emph{Soit} $u",
           "The TeX adds 'et'; the edit also underlines 'posons' and 'Soit' as the print."))
L.append(F(177, "statement of Proposition 5.11.3, 'u ∈ Hom_B(E,M ⊗^L_K E) , notons'",
           "Hom_B NOT underlined (Hom in D(B)); 'notons' underlined", r"$u\in\uHom_B(E,M\lten_KE)$, notons",
           "underline", "high", r"\in\uHom_B(E,M\lten_KE)$, notons", r"\in\Hom_B(E,M\lten_KE)$, \emph{notons}",
           "Plain Hom (as in 5.11.1); the edit also underlines 'notons'."))
L.append(F(177, "statement of Proposition 5.11.3, 'gu ∈ Hom_A(E,M ⊗^L_K E) le composé de l'image de u dans'",
           "Hom_A NOT underlined; 'le composé de l'image de' and 'dans' underlined",
           r"$gu\in\uHom_A(E,M\lten_KE)$ le composé de l'image de $u$ dans", "underline", "high",
           r"\in\uHom_A(E,M\lten_KE)$ le composé de l'image de $u$ dans",
           r"\in\Hom_A(E,M\lten_KE)$ \emph{le composé de l'image de} $u$ \emph{dans}",
           "Plain Hom; the edit also carries the statement's underline."))
L.append(F(177, "statement of Proposition 5.11.3, 'Hom_A(E,M ⊗^L_K E) avec la multiplication ... Alors on a, dans'",
           "Hom_A NOT underlined; 'avec la multiplication à gauche par' and 'Alors on a, dans' underlined",
           r"$\uHom_A(E,M\lten_KE)$ avec la multiplication à gauche par $g$. Alors on a, dans", "underline", "high",
           r"$\uHom_A(E,M\lten_KE)$ avec la multiplication à gauche par $g$. Alors on a, dans",
           r"$\Hom_A(E,M\lten_KE)$ \emph{avec la multiplication à gauche par} $g$. \emph{Alors on a, dans}",
           "Plain Hom; the edit also carries the statement's underline."))

# ---------------------------------------------------------------- page 178
L.append(F(178, "diagram (5.11.4), lower left corner",
           "RHom_A(E,M ⊗_K E) : no L over this ⊗_K (clean scan), while the upper row has RHom_B(E,M ⊗^L_K E) and "
           "5.10.12 and 5.11.3 have RHom_A(E,M ⊗^L_K E) / Hom_A(E,M ⊗^L_K E)",
           r"\uRHom_A(E,M\otimes_KE)  (keeps the printed reading)", "misprint_in_print", "medium", None, None,
           "Typing omission of the L, classed as on p. 175 for (5.10.7) (the same term carries ⊗^L elsewhere); "
           "the same omission recurs twice in the next diagram. With E perfect the plain ⊗ is not wrong, so "
           "this may also be read as the author's notation. The TeX keeps the printed reading; the corrected "
           "layer already has \\lten here.", corrected=r"\uRHom_A(E,M\lten_KE)"))
L.append(F(178, "large diagram (bord), top middle", "M ⊗_K B_♮ (no L)", r"M\lten_KB_\natural", "formula",
           "high", "M\\lten_KB_\\natural \\arrow[r,\"{x\\mapsto x(g^{-1})}\"] \\arrow[d",
           "M\\otimes_KB_\\natural \\arrow[r,\"{x\\mapsto x(g^{-1})}\"] \\arrow[d",
           "As in (5.11.4) just above, where the TeX already has M\\otimes_KB_\\natural."))
L.append(F(178, "large diagram, middle row, left", "RHom_A(E,M ⊗_K E) : no L over ⊗_K (clean scan)",
           r"\uRHom_A(E,M\lten_KE)", "misprint_in_print", "medium",
           "M\\lten_KE) \\arrow[r,\"\\Tr_A\"'] \\arrow[d", "M\\otimes_KE) \\arrow[r,\"\\Tr_A\"'] \\arrow[d",
           "Same omission of the L as in (5.11.4); the TeX silently supplies it. The edit restores the printed "
           "reading (diplomatic layer only).", corrected=r"\uRHom_A(E,M\lten_KE)"))
L.append(F(178, "large diagram, middle row, middle", "M ⊗_K A_♮ (no L)", r"M\lten_KA_\natural", "formula", "high",
           r"M\lten_KA_\natural \arrow[d", r"M\otimes_KA_\natural \arrow[d"))
L.append(F(178, "large diagram, middle row, right column",
           "no object: the double line runs from the top M to the bottom M across the middle row; (3) stands "
           "in the region between the middle column and that line",
           "an M in the middle row, right column, with \\arrow[d,equal] from the top M to it and nothing from it "
           "to the bottom M", "extra", "high",
           "description] &\nM \\\\", "description] &\n\\\\",
           "Apply together with the next edit (the equality then joins the top and bottom M)."))
L.append(F(178, "large diagram, right column, double line", "one double line from the top M to the bottom M",
           r"M \arrow[d,equal]  (top M to the middle-row M)", "other", "high",
           "description] &\nM \\arrow[d,equal] \\\\", "description] &\nM \\arrow[dd,equal] \\\\",
           "Apply together with the previous edit."))
L.append(F(178, "large diagram, bottom row, left", "RHom_A(E,M ⊗_K E) : no L over ⊗_K (clean scan)",
           r"\uRHom_A(E,M\lten_KE)", "misprint_in_print", "medium",
           "M\\lten_KE) \\arrow[r,\"\\Tr_A\"'] &", "M\\otimes_KE) \\arrow[r,\"\\Tr_A\"'] &",
           "As in the middle row; the TeX silently supplies the L. The edit restores the printed reading "
           "(diplomatic layer only).", corrected=r"\uRHom_A(E,M\lten_KE)"))
L.append(F(178, "large diagram, bottom row, middle", "M ⊗_K A_♮ (no L)", r"M\lten_KA_\natural", "formula", "high",
           "M\\lten_KA_\\natural \\arrow[r,\"{x\\mapsto x(e)}\"'] &\nM,\n\\end{tikzcd}\n\\]",
           "M\\otimes_KA_\\natural \\arrow[r,\"{x\\mapsto x(e)}\"'] &\nM,\n\\end{tikzcd}\n\\]",
           "The old reaches to the closing \\] because the corrected layer's (5.11.4) has the same line."))
L.append(F(178, "'Le carré (1) commute en vertu du 5.10.11'", "en vertu du 5.10.11", "en vertu de 5.10.11", "word",
           "high", "vertu de 5.10.11", "vertu du 5.10.11"))
L.append(F(178, "display (*)", "Tr_A(x ⟼ gxh)(e) = { 1 si g^{-1} est conjugué à h / 0 sinon } .  ('si', no "
           "commas)", "1,& g^{-1}\\text{ est conjugué à }h,\\\\\n0,& \\text{sinon}.", "word", "high",
           "1,& g^{-1}\\text{ est conjugué à }h,\\\\\n0,& \\text{sinon}.",
           "1 & \\text{si } g^{-1}\\text{ est conjugué à }h\\\\\n0 & \\text{sinon}.",
           "The TeX leaves out 'si' and adds the commas."))

# ---------------------------------------------------------------- page 179
L.append(F(179, "top of the page",
           "p. 179 begins with the display Tr_Z(x ⟼ gxh) = { |Z_g| si ... / 0 sinon } .; p. 178 ends 'on est "
           "donc ramené à montrer que'",
           "the opening of that display ('\\[', '\\Tr_{\\mathbb Z}(x\\mapsto gxh)=', '\\begin{cases}') ends "
           "page_178.tex; the folio-179 marker stands inside the cases environment", "marker", "high", None, None,
           "Page 179 really begins at the '\\[' that opens Tr_{\\mathbb Z}(x\\mapsto gxh)=... Exact fix: python -I "
           "move_marker.py 5 179 '\\[' --before  (the last '\\[' before the marker is the one that opens this "
           "display; simulated in memory on both layers: '...on est donc ramené à montrer que' / marker / '\\[' "
           "/ '\\Tr_{\\mathbb Z}(x\\mapsto gxh)='). Text not moved."))
L.append(F(179, "display Tr_Z(x ⟼ gxh) = {...}", "{ |Z_g| si g^{-1} est conjugué à h / 0 sinon } .  ('si', no "
           "commas)", "|Z_g|,& g^{-1}\n\\text{ est conjugué à }h,\\\\\n0,& \\text{sinon}.", "word", "high",
           "|Z_g|,& g^{-1}\n\\text{ est conjugué à }h,\\\\\n0,& \\text{sinon}.",
           "|Z_g| & \\text{si } g^{-1}\n\\text{ est conjugué à }h\\\\\n0 & \\text{sinon}.",
           "As in (*) on p. 178."))
L.append(F(179, "Corollaire 5.11.5, label", "Corollaire 5.11.5 - Sous les hypothèses de 5.11.3 , on a",
           r"\begin{statement}{Corollaire 5.11.5}", "punctuation", "high",
           r"\begin{statement}{Corollaire 5.11.5}", r"\begin{statement}{Corollaire 5.11.5 -}"))
L.append(F(179, "statement of Corollaire 5.11.5", "underlined: 'Sous les hypothèses de' | 'on a'", "no underline",
           "underline", "high", "Sous les hypothèses de 5.11.3, on a",
           r"\emph{Sous les hypothèses de} 5.11.3, \emph{on a}"))
L.append(F(179, "formula of Corollaire 5.11.5", "Tr_K(gu) = |Z_g|Tr_B(u)(g^{-1}) = |Z_g|Tr_A(gu)(e) .  (no "
           "equation number)", r"\begin{equation}\tag{5.11.5} ... \end{equation}", "extra", "high",
           "\\begin{equation}\\tag{5.11.5}\n\\Tr_K(gu)=|Z_g|\\,\\Tr_B(u)(g^{-1})=|Z_g|\\,\\Tr_A(gu)(e).\n"
           "\\end{equation}",
           "\\[\n\\Tr_K(gu)=|Z_g|\\,\\Tr_B(u)(g^{-1})=|Z_g|\\,\\Tr_A(gu)(e).\n\\]",
           "The tag (5.11.5) is not printed (5.11.5 is the corollary's own number)."))
L.append(F(179, "title 5.12", "5.12. Traces et produits tensoriels externes.  (underlined, full stop)",
           r"\subsubsection*{5.12. Traces et produits tensoriels externes}", "punctuation", "high",
           "produits tensoriels externes}", "produits tensoriels externes.}",
           "Full stop at the end of the underlined title."))
L.append(F(179, "diagram (5.12.3), upper left corner (printed on p. 180)",
           "(RHom_{A_1}(E_1,F_1) ⊗^L_{A_1} G_1) ⊗^L_K (RHom_{A_2}(E_2,F_2) ⊗^L_{A_2} G_2  ⟶(1) : the parenthesis "
           "opened before RHom_{A_2} is not closed (clean scan, nothing after G_2)",
           r"(\uRHom_{A_2}(E_2,F_2)\lten_{A_2}G_2)", "misprint_in_print", "high",
           r"F_2)\lten_{A_2}G_2)", r"F_2)\lten_{A_2}G_2",
           "Unbalanced parenthesis in the print; the TeX silently closes it. Printed on p. 180, filed under p. 179 "
           "because the text stands before the folio-180 marker (marker finding of p. 180): apply before moving "
           "the marker. The edit restores the printed reading (diplomatic layer only).",
           corrected=r"(\uRHom_{A_2}(E_2,F_2)\lten_{A_2}G_2)"))

# ---------------------------------------------------------------- page 180
L.append(F(180, "top of the page",
           "p. 180 begins with the diagram (5.12.3); p. 179 ends 'on a un carré commutatif'",
           "\\begin{equation}\\tag{5.12.3} and the upper left cell of the diagram end page_179.tex; the folio-180 "
           "marker stands inside the tikzcd, in the first gathered cell", "marker", "high", None, None,
           "Page 180 really begins at '\\begin{equation}\\tag{5.12.3}'. Exact fix, after the p. 179 edit of that "
           "cell: python -I move_marker.py 5 180 '\\begin{equation}\\tag{5.12.3}' --before  (simulated in memory "
           "on both layers: '...on a un carré commutatif' / marker / '\\begin{equation}\\tag{5.12.3}'). Text not "
           "moved."))
L.append(F(180, "'pour u_i ∈ Hom_{A_i}(E_i,F_i ⊗^L_{A_i} E_i) , on a'", "Hom_{A_i} not underlined",
           r"$u_i\in\uHom_{A_i}(E_i,F_i\lten_{A_i}E_i)$", "underline", "high", r"$u_i\in\uHom_{A_i}",
           r"$u_i\in\Hom_{A_i}", "Plain (global) Hom, as for u in 5.11.1 and 5.11.3."))
L.append(F(180, "title 5.13", "5.13. Traces d'endomorphismes semi-linéaires.  (underlined, full stop)",
           r"\subsubsection*{5.13. Traces d'endomorphismes semi-linéaires}", "punctuation", "high",
           "endomorphismes semi-linéaires}", "endomorphismes semi-linéaires.}",
           "Full stop at the end of the underlined title."))
L.append(F(180, "'x ∈ E , i.e. si u est un homomorphisme A-linéaire'", "i.e. si u", "c'est-à-dire si $u$", "word",
           "high", "c'est-à-dire si $u$", "i.e. si $u$", "Abbreviation written out by the TeX."))


# ---------------------------------------------------------------- checks
def live_pages(edition):
    P = pages("5", edition)
    return {p: "".join(f.read_text(encoding="utf-8")[s:e] for f, s, e in P[p]) for p in range(175, 182)}


ok = True
for x in L:
    fx = x["fix"]
    if not fx:
        continue
    snap = (B / f"page_{x['page']}.tex").read_text(encoding="utf-8")
    n = snap.count(fx["old"])
    want = 0 if x["_live_only"] else 1
    if n != want:
        ok = False
        print("SNAPSHOT COUNT", x["page"], n, repr(fx["old"][:60]))
    if "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]:
        ok = False
        print("MARKER IN FIX", repr(fx["old"][:60]))
    for ch in fx["old"] + fx["new"]:
        if ord(ch) < 32 and ch != "\n":
            ok = False
            print("CONTROL CHAR", repr(fx["old"][:60]))
for edition in ("diplomatic", "current"):
    T = live_pages(edition)
    for x in L:
        fx = x["fix"]
        if not fx:
            continue
        if edition == "current" and x["kind"] == "misprint_in_print":
            continue
        t = T[x["page"]]
        n = t.count(fx["old"])
        if n != 1:
            ok = False
            print("LIVE", edition, x["page"], n, repr(fx["old"][:70]))
            continue
        T[x["page"]] = t.replace(fx["old"], fx["new"], 1)
print("all checks passed" if ok else "CHECKS FAILED")

for x in L:
    del x["_live_only"]
OUT.write_text(json.dumps(L, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
from collections import Counter  # noqa: E402
c = Counter((x["page"], x["kind"] == "misprint_in_print") for x in L)
for p in range(176, 181):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
print("total", len(L))
