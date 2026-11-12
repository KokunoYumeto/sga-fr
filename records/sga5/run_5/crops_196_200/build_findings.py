"""Build findings_196_200.json; check that every fix's old occurs exactly once (in list order, per page)."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
B = RUN / "b196_200"
OUT = RUN / "findings_196_200.json"


def N(s):
    return s.replace("¶", "\n")


def fx(old, new):
    return {"old": N(old), "new": N(new)}


F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- page 196
add(196, "top of the page",
    "p. 196 begins '(III 4.7) entraîne que ∫_{X-U} Tr(c_{X-U}) ∈ Λ est la caractéristique ...'",
    "page_196.tex opens with 'Lefschetz (III 4.7) entraîne que'; the line before the folio-196 marker ends '... alors la formule de'",
    "marker", "high", None,
    "Page 196 really begins at '(III 4.7) entraîne que'; 'Lefschetz' is the last word of p. 195. Exact fix: "
    "python -I move_marker.py 5 196 '(III 4.7) entraîne que' (simulated in memory on both editions: "
    "'... alors la formule de' / 'Lefschetz ' / marker / '(III 4.7) entraîne que').")
add(196, "end of 6.14, 'de X-U (à valeurs dans Λ)'",
    "de X-U (à valeurs dans Λ) .", "de $X-U$ à valeurs dans $\\Lambda$.",
    "punctuation", "high",
    fx(r"de $X-U$ à valeurs dans $\Lambda$.", r"de $X-U$ (à valeurs dans $\Lambda$)."),
    "The print's parentheses are dropped.")
add(196, "end of 6.14, 'caractéristique d'Euler-Poincaré'",
    "Euler-Poincaré (typed hyphen)", "Euler--Poincaré",
    "punctuation", "high",
    fx(r"d'Euler--Poincaré", r"d'Euler-Poincaré"),
    "En dash the print does not have.")
add(196, "6.15, number",
    "6.15.", "\\subsection*{6.15}",
    "punctuation", "high",
    fx(r"\subsection*{6.15}", r"\subsection*{6.15.}"),
    "Full stop after the paragraph number, as 6.2.-6.4. of this section.")
add(196, "6.15, first sentence",
    "6.11.1 (avec f , c , d propres) , et U ⟶ X",
    "6.11.1, avec $f$, $c$, $d$ propres, et",
    "punctuation", "high",
    fx(r"6.11.1, avec $f$, $c$, $d$ propres, et", r"6.11.1 (avec $f$, $c$, $d$ propres), et"),
    "Parentheses of the print turned into commas.")
add(196, "6.15, 'de tor-dimension finie, c_1^{-1}(U) ⊂ c_2^{-1}(U)'",
    "quasi-fini et de tor-dimension finie,  c_1^{-1}(U) ⊂ c_2^{-1}(U) , que G agit ...",
    "de tor-dimension finie, que [display c_1^{-1}(U)\\subset c_2^{-1}(U),] que $G$ agit",
    "extra", "high",
    fx(r"de tor-dimension finie, que", r"de tor-dimension finie,"),
    "The print has no 'que' before the inclusion (only before 'G agit').")
add(196, "6.15, 'u = c_{U,X} , et, compte tenu'",
    "u = c_{U,X} , et, compte tenu de 6.14.6, 6.14.7",
    "$u=\\underline c_{U,X}$ et, compte tenu",
    "punctuation", "high",
    fx(r"$u=\underline c_{U,X}$ et,", r"$u=\underline c_{U,X}$, et,"),
    "Comma before 'et' left out.")
add(196, "6.15, last words",
    "on obtient la [blank line] Proposition 6.16 - ...",
    "on obtient:",
    "word", "high",
    fx(r"on obtient:", r"on obtient la"),
    "The print runs on into the statement ('on obtient la Proposition 6.16'); the TeX drops 'la' and adds a colon.")
add(196, "Proposition 6.16, label",
    "Proposition 6.16 -", "\\begin{statement}{Proposition 6.16}",
    "punctuation", "high",
    fx(r"\begin{statement}{Proposition 6.16}", r"\begin{statement}{Proposition 6.16 -}"),
    "As the earlier labels of Exposé III B (Théorème 1.2 -, Proposition 5.10.6 -).")
add(196, "Proposition 6.16, first line",
    "Sous les hypothèses de | on a | pour tout : underlined",
    "Sous les hypothèses de 6.15, on a, pour tout $g\\in G$, (no underline)",
    "underline", "high",
    fx(r"Sous les hypothèses de 6.15, on a, pour tout $g\in G$,¶\begin{equation}¶f_*^{gc}\Tr_{\Lambda}(",
       r"\emph{Sous les hypothèses de} 6.15, \emph{on a}, \emph{pour tout} $g\in G$,¶\begin{equation}¶f_*^{gc}\Tr_{\Lambda}("),
    "Statement underlined word group by word group; \\emph as on the earlier pages of Exposé III B. The old runs into the formula only to be unique (Corollaire 6.17 opens with the same words).")
add(196, "Proposition 6.16, after (6.16.1)",
    "où | est l'inclusion | et | désigne le centralisateur de : underlined",
    "où $j:X-U\\to X$ est l'inclusion, et $Z_g$ désigne le centralisateur de $g$.",
    "underline", "high",
    fx(r"où $j:X-U\to X$ est l'inclusion, et $Z_g$ désigne le centralisateur de $g$.",
       r"\emph{où} $j:X-U\to X$ \emph{est l'inclusion}, \emph{et} $Z_g$ \emph{désigne le centralisateur de} $g$."),
    "")
add(196, "before Corollaire 6.17",
    "on en déduit, d'après 6.13,", "on en déduit, d'après 6.13:",
    "punctuation", "high",
    fx(r"d'après 6.13:", r"d'après 6.13,"),
    "Comma in the print, not a colon.")
add(196, "Corollaire 6.17, label",
    "Corollaire 6.17 -", "\\begin{statement}{Corollaire 6.17}",
    "punctuation", "high",
    fx(r"\begin{statement}{Corollaire 6.17}", r"\begin{statement}{Corollaire 6.17 -}"),
    "")
add(196, "Corollaire 6.17, first line",
    "Sous les hypothèses de | on a | pour tout : underlined",
    "Sous les hypothèses de 6.15, on a, pour tout $g\\in G$, (no underline)",
    "underline", "high",
    fx(r"Sous les hypothèses de 6.15, on a, pour tout $g\in G$,¶\begin{equation}¶f_*^{gc}\Tr_{\mathbb Z",
       r"\emph{Sous les hypothèses de} 6.15, \emph{on a}, \emph{pour tout} $g\in G$,¶\begin{equation}¶f_*^{gc}\Tr_{\mathbb Z"),
    "")
add(196, "Corollaire 6.17, last line",
    "avec les notations de : underlined", "avec les notations de 6.16.",
    "underline", "high",
    fx(r"avec les notations de 6.16.", r"\emph{avec les notations de} 6.16."),
    "")
add(196, "end of the page / top of p. 197",
    "p. 197 opens 'En fait, il n'est pas difficile' flush left: the typescript indents every new paragraph ('Compte tenu', 'Appliquant', 'Par dévissage'), so the paragraph of p. 196 continues",
    "page_196.tex ends 'est l'identité.' followed by a blank line before the folio-197 marker",
    "other", "high",
    fx(r"est l'identité.¶¶", r"est l'identité.¶"),
    "Paragraph break the print does not have (global issue 44); the edit removes the blank line before the marker (the marker line stays).")

# ---------------------------------------------------------------- page 197
add(197, "first paragraph, 'c_1(xg) = c_1(x)φ(g),'",
    "c_1 vérifie c_1(xg) = c_1(x)φ(g), pour tout point x ...",
    "\\[ c_1(xg)=c_1(x)\\varphi(g) \\] pour tout point",
    "punctuation", "high",
    fx(r"c_1(xg)=c_1(x)\varphi(g)¶\]", r"c_1(xg)=c_1(x)\varphi(g),¶\]"),
    "The comma after the formula is left out (display a layout variant).")
add(197, "first paragraph, 'pour tout point x de G'",
    "pour tout point x de G , φ étant ... (G clearly typed)",
    "pour tout point $x$ de $G$",
    "misprint_in_print", "medium", None,
    "c_1 is defined on C (diagram 6.11.1), so x is a point of C (and g runs through G). The TeX keeps the printed reading.",
    corrected=r"pour tout point $x$ de $C$")
add(197, "6.18, number",
    "6.18.", "\\subsection*{6.18}",
    "punctuation", "high",
    fx(r"\subsection*{6.18}", r"\subsection*{6.18.}"),
    "")
add(197, "after (6.18.2)",
    "par l'augmentation naturelle (envoyant tout g ∈ G sur 1).",
    "par l'augmentation naturelle, envoyant tout $g\\in G$ sur $1$.",
    "punctuation", "high",
    fx(r"l'augmentation naturelle, envoyant tout $g\in G$ sur $1$.",
       r"l'augmentation naturelle (envoyant tout $g\in G$ sur $1$)."),
    "Parentheses of the print turned into a comma.")
add(197, "Lemme 6.18.3, label",
    "Lemme 6.18.3 -", "\\begin{statement}{Lemme 6.18.3}",
    "punctuation", "high",
    fx(r"\begin{statement}{Lemme 6.18.3}", r"\begin{statement}{Lemme 6.18.3 -}"),
    "")
add(197, "Lemme 6.18.3, statement",
    "Si | la flèche | est un isomorphisme : underlined",
    "Si $L\\in\\Ob D_{\\mathrm{ctf}}({}_{\\Lambda[G]}X)$, la flèche 6.18.2 est un isomorphisme.",
    "underline", "high",
    fx(r"Si $L\in\Ob D_{\mathrm{ctf}}({}_{\Lambda[G]}X)$, la flèche 6.18.2 est un isomorphisme.",
       r"\emph{Si} $L\in\Ob D_{\mathrm{ctf}}({}_{\Lambda[G]}X)$, \emph{la flèche} 6.18.2 \emph{est un isomorphisme}."),
    "")
add(197, "Proposition 6.19, label",
    "Proposition 6.19 -", "\\begin{statement}{Proposition 6.19}",
    "punctuation", "high",
    fx(r"\begin{statement}{Proposition 6.19}", r"\begin{statement}{Proposition 6.19 -}"),
    "")
add(197, "Proposition 6.19, first line",
    "Dans la situation de | soient : underlined",
    "Dans la situation de 6.11, soient",
    "underline", "high",
    fx(r"Dans la situation de 6.11, soient", r"\emph{Dans la situation de} 6.11, \emph{soient}"),
    "")
add(197, "Proposition 6.19, 'a : M ⟶ f_*L'",
    "v ∈ Hom(d_1^*M,d_2^!M) , a : M ⟶ f_*L une flèche de ...",
    "\\] et $a:M\\to f_*L$",
    "extra", "high",
    fx(r"\]¶et $a:M", r"\]¶$a:M"),
    "The print has no 'et' before a.")
add(197, "Proposition 6.19, 'une flèche de'",
    "une flèche de : underlined", "f_*L$ une flèche de",
    "underline", "high",
    fx(r"f_*L$ une flèche de", r"f_*L$ \emph{une flèche de}"),
    "")
add(197, "Proposition 6.19, '(M étant regardé ... Λ[G] ⟶ Λ ) tels que le carré'",
    "D(_{Λ[G]}Y) (M étant regardé comme objet de D(_{Λ[G]}Y) par l'augmentation Λ[G] ⟶ Λ ) tels que le carré",
    "$D({}_{\\Lambda[G]}Y)$, $M$ étant regardé comme objet de $D({}_{\\Lambda[G]}Y)$ par l'augmentation $\\Lambda[G]\\to\\Lambda$, tels que le carré",
    "punctuation", "high",
    fx(r"Y)$, $M$ étant regardé comme objet de $D({}_{\Lambda[G]}Y)$ par l'augmentation $\Lambda[G]\to\Lambda$, tels que le carré",
       r"Y)$ ($M$ \emph{étant regardé comme objet de} $D({}_{\Lambda[G]}Y)$ \emph{par l'augmentation} $\Lambda[G]\to\Lambda$) \emph{tels que le carré}"),
    "Parentheses of the print turned into commas; the same edit sets the underlines of the three word groups (étant regardé comme objet de, par l'augmentation, tels que le carré), which interleave with the parentheses.")
add(197, "Proposition 6.19, after the square",
    "soit commutatif | On suppose que : underlined",
    "soit commutatif. On suppose que",
    "underline", "high",
    fx(r"soit commutatif. On suppose que", r"\emph{soit commutatif}. \emph{On suppose que}"),
    "")
add(197, "Proposition 6.19, 'On suppose que f_*M ∈ ob D_ctf(_{Λ[G]}Y)'",
    "f_*M ∈ ob D_ctf(_{Λ[G]}Y) (M clearly typed)",
    "$f_*M\\in\\Ob D_{\\mathrm{ctf}}({}_{\\Lambda[G]}Y)$",
    "misprint_in_print", "medium", None,
    "M lives on Y; the object of D(_{Λ[G]}Y) meant is f_*L (L on X, as in a : M ⟶ f_*L and RHom_{Λ[G]}(Λ,f_*L) on the next line; 6.22 states the same hypothesis as f_*f^*M ∈ ob D_ctf(_{Λ[G]}Y) with L = f^*M). The TeX keeps the printed reading.",
    corrected=r"$f_*L\in\Ob D_{\mathrm{ctf}}({}_{\Lambda[G]}Y)$")
add(197, "Proposition 6.19, 'et que a induit un isomorphisme'",
    "et que | induit un isomor-phisme : underlined",
    "et que $a$ induit un isomorphisme",
    "underline", "high",
    fx(r"et que $a$ induit un isomorphisme", r"\emph{et que} $a$ \emph{induit un isomorphisme}"),
    "")
add(197, "Proposition 6.19, last line",
    "Alors on a : underlined", "Alors on a",
    "underline", "high",
    fx(r"Alors on a", r"\emph{Alors on a}"),
    "")

# ---------------------------------------------------------------- page 198
add(198, "6.20, number",
    "6.20.", "\\subsection*{6.20}",
    "punctuation", "high",
    fx(r"\subsection*{6.20}", r"\subsection*{6.20.}"),
    "")
add(198, "6.20, 'Soient L_i ∈ ob D^+(G,X_i)'",
    "L_i ∈ ob D^+(G,X_i) (no left index)",
    "$L_i\\in\\Ob D^+(G,{}_AX_i)$",
    "formula", "high",
    fx(r"D^+(G,{}_AX_i)", r"D^+(G,X_i)"),
    "The left index A is not printed (compare 'de D(G,X)' two lines below).")
add(198, "6.20, 'une flèche (de D(G,X)) notée encore'",
    "définit par adjonction une flèche (de D(G,X)) notée encore",
    "une flèche de $D(G,X)$ notée encore",
    "punctuation", "high",
    fx(r"une flèche de $D(G,X)$ notée", r"une flèche (de $D(G,X)$) notée"),
    "The print's parentheses are dropped.")
add(198, "6.20, 'à tout morphisme (G-equivariant)'",
    "à tout morphisme (G-equivariant) u ∈ Hom(...)",
    "à tout morphisme $G$-équivariant",
    "punctuation", "high",
    fx(r"tout morphisme $G$-équivariant¶", r"tout morphisme ($G$-équivariant)¶"),
    "The print's parentheses are dropped. Apply before the next (misprint) edit, whose old is taken from this edit's result.")
add(198, "6.20, '(G-equivariant)'",
    "G-equivariant without the acute accent (the accents of the line are sharp; 'G-équivariante' on the next line has it)",
    "$G$-équivariant",
    "misprint_in_print", "high",
    fx(r"($G$-équivariant)", r"($G$-equivariant)"),
    "Typing slip (accent left out); the TeX silently corrects it, the edit restores the printed reading (diplomatic layer only). Its old is the text after the preceding punctuation edit: apply the two together, in this order.",
    corrected=r"($G$-équivariant)")
add(198, "6.20, 'une correspondance (G-équivariante)'",
    "une correspondance (G-équivariante)",
    "une correspondance $G$-équivariante",
    "punctuation", "high",
    fx(r"une correspondance $G$-équivariante", r"une correspondance ($G$-équivariante)"),
    "The print's parentheses are dropped.")
add(198, "Proposition 6.21, label",
    "Proposition 6.21 -", "\\begin{statement}{Proposition 6.21}",
    "punctuation", "high",
    fx(r"\begin{statement}{Proposition 6.21}", r"\begin{statement}{Proposition 6.21 -}"),
    "")
add(198, "Proposition 6.21, first sentence",
    "Soient | un | morphisme propre | et un carré com-mutatif équivariant | avec action triviale de | sur | et : underlined (not G-S-, not the letters)",
    "Soient $f:X\\to Y$ un $G$-$S$-morphisme propre, ... et $D$.",
    "underline", "high",
    fx(r"Soient $f:X\to Y$ un $G$-$S$-morphisme propre, et un carré commutatif équivariant 6.11.1, avec action triviale de $G$ sur $Y$ et $D$.",
       r"\emph{Soient} $f:X\to Y$ \emph{un} $G$-$S$-\emph{morphisme propre}, \emph{et un carré commutatif équivariant} 6.11.1, \emph{avec action triviale de} $G$ \emph{sur} $Y$ \emph{et} $D$."),
    "")
add(198, "Proposition 6.21, 'On suppose ... et le carré'",
    "On suppose | propres | quasi-finis et de tor-dimension finie | et le carré : underlined",
    "On suppose $c$, $d$ propres, $c_2$, $d_2$ quasi-finis et de tor-dimension finie, et le carré",
    "underline", "high",
    fx(r"On suppose $c$, $d$ propres, $c_2$, $d_2$ quasi-finis et de tor-dimension finie, et le carré",
       r"\emph{On suppose} $c$, $d$ \emph{propres}, $c_2$, $d_2$ \emph{quasi-finis et de tor-dimension finie}, \emph{et le carré}"),
    "")
add(198, "Proposition 6.21, after the square",
    "cartésien et tor-indépendant | Soient : underlined",
    "cartésien et tor-indépendant (SGA 6 III 1.5). Soient $M",
    "underline", "high",
    fx(r"cartésien et tor-indépendant (SGA 6 III 1.5). Soient $M",
       r"\emph{cartésien et tor-indépendant} (SGA 6 III 1.5). \emph{Soient} $M"),
    "")
add(198, "Proposition 6.21, 'd'où un homomorphisme G-équivariant'",
    "d'où un homomorphisme | équivariant : underlined (not G-)",
    "d'où un homomorphisme $G$-équivariant",
    "underline", "high",
    fx(r"d'où un homomorphisme $G$-équivariant", r"\emph{d'où un homomorphisme} $G$-\emph{équivariant}"),
    "")
add(198, "Proposition 6.21, 'et des correspondances G-équivariantes'",
    "et des correspondances | équivariantes : underlined (not G-)",
    "et des correspondances $G$-équivariantes",
    "underline", "high",
    fx(r"et des correspondances $G$-équivariantes", r"\emph{et des correspondances} $G$-\emph{équivariantes}"),
    "")
add(198, "Proposition 6.21, last sentence of the page",
    "On a alors un carré commutatif de flèches de D(_{Λ[G]}Y) (M étant considéré comme objet de D(_{Λ[G]}Y) par l'action triviale) [diagram on p. 199]",
    "... de flèches de $D({}_{\\Lambda[G]}Y)$, $M$ étant considéré comme objet de $D({}_{\\Lambda[G]}Y)$ par l'action triviale,",
    "punctuation", "high",
    fx(r"On a alors un carré commutatif de flèches de $D({}_{\Lambda[G]}Y)$, $M$ étant considéré comme objet de $D({}_{\Lambda[G]}Y)$ par l'action triviale,",
       r"\emph{On a alors un carré commutatif de flèches de} $D({}_{\Lambda[G]}Y)$ ($M$ \emph{étant considéré comme objet de} $D({}_{\Lambda[G]}Y)$ \emph{par l'action triviale})"),
    "Parentheses of the print turned into commas (no comma after the closing parenthesis); the same edit sets the underlines of the three word groups, which interleave with the parentheses. The print's underline also runs under the closing parenthesis; left outside the \\emph.")
add(198, "diagram of Proposition 6.21 (printed at the top of p. 199), lower row",
    "d_1^*(f_*f^*M) ⟶ d_2^!(f_*f^*M) ,",
    "d_1^*f_*f^*M ... & d_2^!f_*f^*M,",
    "formula", "high",
    fx(r"""d_1^*f_*f^*M \arrow[r,"f_*((h^*v)^!)"'] & d_2^!f_*f^*M,""",
       r"""d_1^*(f_*f^*M) \arrow[r,"f_*((h^*v)^!)"'] & d_2^!(f_*f^*M),"""),
    "The print has the parentheses, as in Hom(d_1^*(f_*f^*M),d_2^!(f_*f^*M)) of the statement. This diagram is printed on p. 199 (see the p. 199 marker finding); the edit does not cross a marker.")

# ---------------------------------------------------------------- page 199
add(199, "top of the page",
    "p. 199 begins with the square d_1^*M --v^!--> d_2^!M / d_1^*(f_*f^*M) --f_*((h^*v)^!)--> d_2^!(f_*f^*M) , then 'où les flèches verticales ...'",
    "the square is the last display of page_198.tex; page_199.tex opens with 'où les flèches verticales'",
    "marker", "high", None,
    "Page 199 really begins with the display '\\[ \\begin{tikzcd}[column sep=huge,row sep=large] d_1^*M \\arrow[r,\"v^!\"] ...'. Exact fix: "
    "python -I move_marker.py 5 199 '\\[' --before (the last '\\[' before the marker is the one opening this square; simulated in memory on both editions: "
    "'... par l'action triviale,' / marker / '\\[' / '\\begin{tikzcd}[column sep=huge,row sep=large]').")
add(199, "end of Proposition 6.21",
    "où les flèches verticales sont données par la flèche d'adjonction : one underline",
    "où les flèches verticales sont données par la flèche d'adjonction $M\\to f_*f^*M$.",
    "underline", "high",
    fx(r"où les¶flèches verticales sont données par la flèche d'adjonction",
       r"\emph{où les¶flèches verticales sont données par la flèche d'adjonction}"),
    "")
add(199, "proof of 6.21, diagram with (1)-(5), (A), (B)",
    "upper row d_1^*M --v--> d_2^*M --Tr_{d_2}--> d_2^!M; (2) goes down from d_2^*M to h_*c_2^*L and (3) from d_2^!M to d_2^!f_*L; (A) between (1) and (2), (B) between (2) and (3)",
    "upper row in columns 1, 2, 4: (2) points to h_*c_1^*L and (3) to h_*c_2^!L; (A) and (B) placed accordingly",
    "formula", "high",
    fx(r'''d_1^*M \arrow[r,"v"] \arrow[d,"{(1)}"'] &¶d_2^*M \arrow[rr,"\Tr_{d_2}"] \arrow[d,"{(2)}"'] &&¶d_2^!M \arrow[d,"{(3)}"] & {}\\¶d_1^*f_*L \arrow[r,"{(4)}"'] &¶h_*c_1^*L \arrow[r,"h_*u"'] &¶h_*c_2^*L \arrow[r,"h_*\Tr_{c_2}"'] &¶h_*c_2^!L \arrow[r,"{(5)}"'] &¶d_2^!f_*L,¶\arrow[from=1-1,to=2-2, phantom, "\scriptstyle (A)"]¶\arrow[from=1-2,to=2-4, phantom, "\scriptstyle (B)"]''',
       r'''d_1^*M \arrow[rr,"v"] \arrow[d,"{(1)}"'] &&¶d_2^*M \arrow[rr,"\Tr_{d_2}"] \arrow[d,"{(2)}"'] &&¶d_2^!M \arrow[d,"{(3)}"]\\¶d_1^*f_*L \arrow[r,"{(4)}"'] &¶h_*c_1^*L \arrow[r,"h_*u"'] &¶h_*c_2^*L \arrow[r,"h_*\Tr_{c_2}"'] &¶h_*c_2^!L \arrow[r,"{(5)}"'] &¶d_2^!f_*L,¶\arrow[from=1-1,to=2-3, phantom, "\scriptstyle (A)"]¶\arrow[from=1-3,to=2-5, phantom, "\scriptstyle (B)"]'''),
    "Wrong targets of two vertical arrows: as printed (and as the text says: (2) is d_2^*M ⟶ h_*h^*(d_2^*M) = h_*c_2^*L, (3) comes from M ⟶ f_*L), d_2^*M stands above h_*c_2^*L and d_2^!M above d_2^!f_*L. The edit puts the upper row in columns 1, 3, 5 and re-anchors the phantom labels (A), (B); the lower row is unchanged (its labels below the arrows are the convention reported in the message).")
add(199, "Corollaire 6.22, label",
    "Corollaire 6.22 -", "\\begin{statement}{Corollaire 6.22}",
    "punctuation", "high",
    fx(r"\begin{statement}{Corollaire 6.22}", r"\begin{statement}{Corollaire 6.22 -}"),
    "")
add(199, "Corollaire 6.22, first line",
    "Sous les hypothèses de | on suppose que : underlined",
    "Sous les hypothèses de 6.21, on suppose que",
    "underline", "high",
    fx(r"Sous les hypothèses de 6.21, on suppose que", r"\emph{Sous les hypothèses de} 6.21, \emph{on suppose que}"),
    "")
add(199, "Corollaire 6.22, 'et que la flèche d'adjonction'",
    "et que la flèche d'adjonction : underlined", "et que la flèche d'adjonction",
    "underline", "high",
    fx(r"et que la flèche d'adjonction", r"\emph{et que la flèche d'adjonction}"),
    "")
add(199, "Corollaire 6.22, 'induit un isomorphisme'",
    "induit un isomorphisme : underlined", "induit un isomorphisme",
    "underline", "high",
    fx(r"induit un isomorphisme", r"\emph{induit un isomorphisme}"),
    "")
add(199, "Corollaire 6.22, 'Alors on a'",
    "Alors on a : underlined", "Alors on a",
    "underline", "high",
    fx(r"Alors on a", r"\emph{Alors on a}"),
    "")
add(199, "(6.22.1)",
    "Tr_{Λ[G]}(f_*(f^*v)^!)(g^{-1})",
    "\\Tr_{\\Lambda[G]}(f_*((f^*v)^!))(g^{-1})",
    "formula", "high",
    fx(r"(f_*((f^*v)^!))(g^{-1})", r"(f_*(f^*v)^!)(g^{-1})"),
    "One pair of parentheses fewer in the print (also four times on p. 200). f^*v as printed (h^*v in 6.21), kept.")
add(199, "Proposition 6.23, label",
    "Proposition 6.23 -", "\\begin{statement}{Proposition 6.23}",
    "punctuation", "high",
    fx(r"\begin{statement}{Proposition 6.23}", r"\begin{statement}{Proposition 6.23 -}"),
    "")
add(199, "Proposition 6.23, first line",
    "Sous les hypothèses de | on suppose donné de plus une immer-sion ouverte : underlined",
    "Sous les hypothèses de 6.21, on suppose donné de plus une immersion ouverte",
    "underline", "high",
    fx(r"Sous les hypothèses de 6.21, on suppose donné de plus une immersion ouverte",
       r"\emph{Sous les hypothèses de} 6.21, \emph{on suppose donné de plus une immersion ouverte}"),
    "")
add(199, "Proposition 6.23, 'telle que (fc_1)^{-1}(V) soit connexe, que'",
    "telle que | soit connexe, que : underlined (the second through the comma)",
    "telle que $(fc_1)^{-1}(V)$ soit connexe, que",
    "underline", "high",
    fx(r"telle que $(fc_1)^{-1}(V)$ soit connexe, que", r"\emph{telle que} $(fc_1)^{-1}(V)$ \emph{soit connexe, que}"),
    "")
add(199, "Proposition 6.23, 'et que f' (printed on p. 200)",
    "et que : underlined", "et que $f$",
    "underline", "high",
    fx(r"et que $f$", r"\emph{et que} $f$"),
    "Printed on p. 200, line 1 (see the p. 200 marker finding).")

# ---------------------------------------------------------------- page 200
add(200, "top of the page",
    "p. 200 begins 'd_1^{-1}(V) ⊂ d_2^{-1}(V) ., et que f induise un revêtement'; p. 199 ends 'soit connexe, que'",
    "'$d_1^{-1}(V)\\subset d_2^{-1}(V)$, et que $f$' ends page_199.tex; page_200.tex opens with 'induise un revêtement'",
    "marker", "high", None,
    "Page 200 really begins at '$d_1^{-1}(V)\\subset d_2^{-1}(V)$'. Exact fix: python -I move_marker.py 5 200 '$d_1^{-1}(V)\\subset d_2^{-1}(V)$' --before "
    "(simulated in memory on both editions: '... soit connexe, que ' / marker / '$d_1^{-1}(V)\\subset d_2^{-1}(V)$, et que $f$' / 'induise un revêtement ...'). "
    "The faint dot before the comma after d_2^{-1}(V) is much smaller than a typed full stop: taken as a speck, not reported.")
add(200, "Proposition 6.23, 'induise un revêtement principal galoisien de groupe'",
    "induise un revêtement principal galoisien de groupe : underlined",
    "induise un revêtement principal galoisien de groupe $G$,",
    "underline", "high",
    fx(r"induise un revêtement principal galoisien de groupe $G$,",
       r"\emph{induise un revêtement principal galoisien de groupe} $G$,"),
    "")
add(200, "Proposition 6.23, the map f_V",
    "G , U = f^{-1}(V) --f_V--> V . (f_V written over the arrow)",
    "f_V:U=f^{-1}(V)\\to V.",
    "formula", "high",
    fx(r"f_V:U=f^{-1}(V)\to V.", r"U=f^{-1}(V)\xrightarrow{f_V}V."),
    "The print has no 'f_V :' before U; f_V labels the arrow.")
add(200, "Proposition 6.23, 'On suppose en outre que ... et qu'on a un isomorphisme'",
    "On suppose en outre que | est de la forme | où | et qu'on a un isomorphisme : underlined",
    "On suppose en outre que $M$ est de la forme $M=i_!E$, où $E\\in\\Ob D(V)$, et qu'on a un isomorphisme",
    "underline", "high",
    fx(r"On suppose en outre que $M$ est de la forme $M=i_!E$, où $E\in\Ob D(V)$, et qu'on a un isomorphisme",
       r"\emph{On suppose en outre que} $M$ \emph{est de la forme} $M=i_!E$, \emph{où} $E\in\Ob D(V)$, \emph{et qu'on a un isomorphisme}"),
    "")
add(200, "Proposition 6.23, α : f_V^*E ⟶ Λ_X ⊗_Λ E_o",
    "Λ_X ⊗_Λ E_o: plain tensor sign, no L above it",
    "\\Lambda_X\\lten_{\\Lambda}E_0",
    "symbol", "high",
    fx(r"\Lambda_X\lten_{\Lambda}E_0", r"\Lambda_X\otimes_{\Lambda}E_0"),
    "\\lten sets the stacked L, which the print does not have here (as Λ_{U,X} ⊗ E_o below).")
add(200, "Proposition 6.23, 'avec E_o ∈ ob D(Λ[G]) , parfait sur Λ . On se donne'",
    "avec | parfait sur | On se donne : underlined",
    "avec $E_0\\in\\Ob D(\\Lambda[G])$, parfait sur $\\Lambda$. On se donne",
    "underline", "high",
    fx(r"avec $E_0\in\Ob D(\Lambda[G])$, parfait sur $\Lambda$. On se donne",
       r"\emph{avec} $E_0\in\Ob D(\Lambda[G])$, \emph{parfait sur} $\Lambda$. \emph{On se donne}"),
    "")
add(200, "Proposition 6.23, 'comme en 6.21, et l'on note'",
    "comme / en | et l'on note : underlined",
    "comme en 6.21, et l'on note",
    "underline", "high",
    fx(r"comme en 6.21, et l'on note", r"\emph{comme en} 6.21, \emph{et l'on note}"),
    "")
add(200, "Proposition 6.23, 'l'homomorphisme défini, grâce à α , par'",
    "l'homomorphisme défini | grâce à | par : underlined",
    "l'homomorphisme défini, grâce à $\\alpha$, par $f^*v",
    "underline", "high",
    fx(r"l'homomorphisme défini, grâce à $\alpha$, par $f^*v",
       r"\emph{l'homomorphisme défini}, \emph{grâce à} $\alpha$, \emph{par} $f^*v"),
    "")
add(200, "Proposition 6.23, 'Alors, si c_{U,X} désigne la correspondance définie en 6.14.3'",
    "Alors, si | désigne la correspondance définie en : underlined",
    "Alors, si $\\underline c_{U,X}$ désigne la correspondance définie en 6.14.3,",
    "underline", "high",
    fx(r"Alors, si $\underline c_{U,X}$ désigne la correspondance définie en 6.14.3,",
       r"\emph{Alors, si} $\underline c_{U,X}$ \emph{désigne la correspondance définie en} 6.14.3,"),
    "The print underlines 'Alors, si' through the comma.")
add(200, "Proposition 6.23, 'on a (avec la notation 6.20.2)'",
    "on / a (avec la notation 6.20.2)  — 'on a' and 'avec la notation' underlined, no comma",
    "on a, avec la notation 6.20.2,",
    "punctuation", "high",
    fx(r"on a, avec la notation 6.20.2,", r"\emph{on a} (\emph{avec la notation} 6.20.2)"),
    "Parentheses of the print turned into commas; the same edit sets the underlines ('on a', 'avec la notation'). The underline runs on under the opening parenthesis; left outside the \\emph.")
add(200, "after (6.23.1), '(Noter que ... α ).'",
    "(Noter que, grâce au caractère central de Tr_Λ , le second membre ne dépend pas du choix de α ).",
    "Noter que, grâce au caractère central de $\\Tr_{\\Lambda}$, le second membre ne dépend pas du choix de $\\alpha$.",
    "punctuation", "high",
    fx(r"Noter que, grâce au caractère central de $\Tr_{\Lambda}$, le second membre ne dépend pas du choix de $\alpha$.",
       r"(Noter que, grâce au caractère central de $\Tr_{\Lambda}$, le second membre ne dépend pas du choix de $\alpha$)."),
    "The print's parentheses around the remark are dropped.")
add(200, "proof, 'Par la formule de projection f_*f^*Λ_Y ⊗ M ⟶ f_*f^*M'",
    "f_*f^*Λ_Y ⊗ M: plain tensor sign, no L above it",
    "f_*f^*\\Lambda_Y\\lten M",
    "symbol", "high",
    fx(r"f_*f^*\Lambda_Y\lten M", r"f_*f^*\Lambda_Y\otimes M"),
    "")
add(200, "proof, 'et f_*(f^*v)^! au produit tensoriel externe'",
    "f_*(f^*v)^!", "$f_*((f^*v)^!)$",
    "formula", "high",
    fx(r"et $f_*((f^*v)^!)$ au produit", r"et $f_*(f^*v)^!$ au produit"),
    "One pair of parentheses fewer in the print.")
add(200, "proof, 'la correspondance (Z_g-équivariante)'",
    "la correspondance (Z_g-équivariante) gf_*(f^*v)^!",
    "la correspondance $Z_g$-équivariante",
    "punctuation", "high",
    fx(r"la correspondance $Z_g$-équivariante", r"la correspondance ($Z_g$-équivariante)"),
    "The print's parentheses are dropped.")
add(200, "proof, 'gf_*(f^*v)^! s'identifie donc à'",
    "gf_*(f^*v)^!", "$gf_*((f^*v)^!)$",
    "formula", "high",
    fx(r"$gf_*((f^*v)^!)$ s'identifie", r"$gf_*(f^*v)^!$ s'identifie"),
    "")
add(200, "proof, display after 'Comme, d'après 6.10.4, on a' (left side)",
    "Tr_{Λ[G]}(f_*(f^*v)^!)(g^{-1})",
    "\\Tr_{\\Lambda[G]}(f_*((f^*v)^!))(g^{-1})",
    "formula", "high",
    fx(r"\Tr_{\Lambda[G]}(f_*((f^*v)^!))(g^{-1})", r"\Tr_{\Lambda[G]}(f_*(f^*v)^!)(g^{-1})"),
    "")
add(200, "proof, display after 'Comme, d'après 6.10.4, on a' (right side)",
    "Tr_{Λ[Z_g]}(gf_*(f^*v)^!)(e)",
    "\\Tr_{\\Lambda[Z_g]}(gf_*((f^*v)^!))(e)",
    "formula", "high",
    fx(r"\Tr_{\Lambda[Z_g]}(gf_*((f^*v)^!))(e)", r"\Tr_{\Lambda[Z_g]}(gf_*(f^*v)^!)(e)"),
    "")
add(200, "proof, 'ou, ce qui revient au même, d'après 6.10.4,'",
    "ou, ce qui revient au même, d'après 6.10.4,",
    "ou, ce qui revient au même d'après 6.10.4,",
    "punctuation", "high",
    fx(r"revient au même d'après", r"revient au même, d'après"),
    "Comma left out.")
add(200, "last line, 'le lemme suivant :'",
    "on voit qu'il suffit d'établir le lemme suivant :",
    "le lemme suivant.",
    "punctuation", "high",
    fx(r"le lemme suivant.", r"le lemme suivant:"),
    "Colon in the print, not a full stop.")

# ---------------------------------------------------------------- checks
ok = True
for page in sorted({f["page"] for f in F}):
    orig = (B / f"page_{page}.tex").read_text(encoding="utf-8")
    assert "¶" not in orig
    cur = orig
    spans = []
    for f in F:
        if f["page"] != page:
            continue
        if f["kind"] == "misprint_in_print" and f["fix"] is None:
            n = orig.count(f["tex"])
            print(page, "misprint tex count", n, repr(f["tex"][:50]))
            ok &= n == 1
        fix = f["fix"]
        if not fix:
            continue
        old, new = fix["old"], fix["new"]
        n_orig = orig.count(old)
        n_cur = cur.count(old)
        if n_cur != 1:
            ok = False
        print(page, f["kind"], "orig", n_orig, "cur", n_cur, repr(old[:60]))
        for ln in orig.splitlines():
            if "%%%%%%%%%%" in ln and ln in old:
                print("   !!! old crosses a marker line"); ok = False
        if n_orig == 1:
            s = orig.find(old)
            spans.append((s, s + len(old), old[:40]))
        cur = cur.replace(old, new, 1)
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            print("   !!! overlap", a[2], "|", b[2]); ok = False
print("ALL OK" if ok else "PROBLEMS")
counts = {}
for f in F:
    c = counts.setdefault(f["page"], [0, 0])
    c[1 if f["kind"] == "misprint_in_print" else 0] += 1
print(counts, len(F))
if ok and "--write" in sys.argv:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("written", OUT)
