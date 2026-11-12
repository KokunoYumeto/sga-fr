"""Build findings_156_160.json from raw strings; the sign ¶ stands for a line break (LF) in old/new."""
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
OUT = r'C:\Users\user\Documents\sga_scan_check_20261105\run_5\findings_156_160.json'
F = []


def add(page, where, scan, tex, kind, conf, old, new, note='', corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, confidence=conf)
    d['fix'] = None if old is None else dict(old=old.replace('¶', '\n'), new=new.replace('¶', '\n'))
    if corrected is not None:
        d['corrected'] = corrected
    d['note'] = note
    F.append(d)


UND = ("Underlined statement, as Lemme 2.2 to Proposition 2.5 (pp. 146-150); \\emph is this file's command for the "
       "print's underline. Numbers, formulas and the punctuation between the underlined groups are not underlined.")

# ---------------- page 156
add(156, "first word of the page", "soient i' ∈ [1,m'] , ... (small s)", r"Soient $i'\in[1,m']$",
    "word", "high", r"Soient $i'", r"soient $i'", "Capital against small letter.")
add(156, "first line, 'l'image de x_{i'} (resp. y'_{j'})'",
    "x_{i'}: no prime on x (nothing above the subscript i'; the prime of y'_{j'} in the same line is typed)",
    r"$x'_{i'}$", "misprint_in_print", "high", r"$x'_{i'}$", r"$x_{i'}$",
    "The points of X' are the x'_{i'} (as the y'_{j'} of Y'); the print drops the prime on x. The TeX silently "
    "corrects it.", corrected=r"x'_{i'}")
add(156, "after the first diagram (squares with A'_{i'}, A_i)",
    "a comma to the right of the first diagram's bottom row (Y ,), a full stop after the second (Y .)",
    r"first tikzcd ends '& Y', then \qquad (no comma)", "punctuation", "high",
    r"A_i \arrow[l] \arrow[r] & Y", r"A_i \arrow[l] \arrow[r] & Y ,",
    "The TeX has only the full stop after the second diagram.")
add(156, "'λ_i = Cλ'^d_{i'} , μ_j = Cμ'^d_{j'} , donc (1) entraîne (2)'",
    "μ_j = Cμ'^d_{j'} , donc (1) entraîne (2) , ce qui achève ... (comma, then small 'donc'; formulas run in the line)",
    r"\mu_j=C{\mu'_{j'}}^d. \] Donc (1) entraîne (2)", "punctuation", "high",
    r"^d.¶\]¶Donc", r"^d,¶\]¶donc",
    "Full stop and capital D added by the TeX (the display against the run-in formula is not reported).")

# ---------------- page 157
add(157, "heading '4. - Fin de la démonstration de 1.2.'",
    "4. - Fin de la démonstration de 1.2. (underlined; ' - ' after '4.', full stop after the underline)",
    r"\subsection*{4. Fin de la démonstration de 1.2}", "punctuation", "high",
    r"\subsection*{4. Fin de la démonstration de 1.2}", r"\subsection*{4. - Fin de la démonstration de 1.2.}",
    "As the headings of nos. 1 and 2 (pp. 140, 146).")
add(157, "Proposition 4.2, label", "Proposition 4.2 - Soient T le localisé strict ...",
    r"\begin{statement}{Proposition 4.2}  (renders 'Proposition 4.2')", "punctuation", "high",
    r"\begin{statement}{Proposition 4.2}", r"\begin{statement}{Proposition 4.2 -}",
    "Exposé III B keeps Exposé III's labels (' -', no added full stop; Exposé III's statement environment is in force "
    "through III B in s5.tex at 20:22).")
add(157, "statement of Proposition 4.2, from 'Soient' to 'l'inclusion.'",
    "underlined: 'Soient' | 'le localisé strict en un point fermé d'un' | 'schéma' + 'lisse de dimension' | "
    "'le point fermé de' | 'des sous-schémas fermés' + 'de dimension' | 'de' | 'l'inclusion'; not underlined: T, "
    "'S-', 2 , t, T , A , B, X, 1, the map i and the punctuation",
    "Soient $T$ le localisé strict ... l'inclusion.  (no underline)", "underline", "high",
    r"Soient $T$ le localisé strict en un point fermé d'un $S$-schéma lisse de dimension $2$, $t$ le point fermé de "
    r"$T$, $A$, $B$, $X$ des sous-schémas fermés de dimension $1$ de $T$, $i:T-(A\cup X)\hookrightarrow T-A$ "
    r"l'inclusion.",
    r"\emph{Soient} $T$ \emph{le localisé strict en un point fermé d'un} $S$-\emph{schéma lisse de dimension} $2$, "
    r"$t$ \emph{le point fermé de} $T$, $A$, $B$, $X$ \emph{des sous-schémas fermés de dimension} $1$ \emph{de} $T$, "
    r"$i:T-(A\cup X)\hookrightarrow T-A$ \emph{l'inclusion}.",
    UND + " Three edits for this statement, and one for 'est nulle'.")
add(157, "statement of Proposition 4.2, from 'On suppose que' to 'Soit d'autre part'",
    "underlined: 'On suppose que' | 'est' + 'régulier' | 'et que' | 'est en position générale par rapport à' | 'et' | "
    "'i.e. que' + 'l'intersection des cônes tangents en' | 'à' | 'et' | 'est réduite à' | 'Soit' + 'd'autre part'; "
    "not underlined: X, A, B, t, B ∪ X, the parentheses and the punctuation",
    "On suppose que $X$ est régulier, ... Soit d'autre part  (no underline)", "underline", "high",
    r"On suppose que $X$ est régulier, et que $A$ est en position générale par rapport à $B$ et $X$ (i.e. que "
    r"l'intersection des cônes tangents en $t$ à $A$ et $B\cup X$ est réduite à $t$). Soit d'autre part",
    r"\emph{On suppose que} $X$ \emph{est régulier}, \emph{et que} $A$ \emph{est en position générale par rapport à} "
    r"$B$ \emph{et} $X$ (\emph{i.e. que l'intersection des cônes tangents en} $t$ \emph{à} $A$ \emph{et} $B\cup X$ "
    r"\emph{est réduite à} $t$). \emph{Soit d'autre part}",
    "As the previous edit.")
add(157, "statement of Proposition 4.2, from 'tel que' to 'Alors la flèche de restriction'",
    "underlined: 'tel que' | 'soit constructible' | 'localement' + 'constant' | 'et que la représentation "
    "correspondante de' | 'se factorise' + 'à travers un' | 'groupe' (not 'ℓ-') | 'Alors la flèche de restriction'; "
    "not underlined: H*(E), π_1(T-(A ∪ X)), 'ℓ-' and the punctuation",
    "tel que $H^*(E)$ soit constructible, ... Alors la flèche de restriction  (no underline)", "underline", "high",
    r"tel que $H^*(E)$ soit constructible, localement constant, et que la représentation correspondante de "
    r"$\pi_1(T-(A\cup X))$ se factorise à travers un $\ell$-groupe. Alors la flèche de restriction",
    r"\emph{tel que} $H^*(E)$ \emph{soit constructible}, \emph{localement constant}, \emph{et que la représentation "
    r"correspondante de} $\pi_1(T-(A\cup X))$ \emph{se factorise à travers un} $\ell$-\emph{groupe}. \emph{Alors la "
    r"flèche de restriction}",
    "As the previous edits.")
add(157, "end of the display of Proposition 4.2, after RΓ(B-t,i_!(E)|B-t)",
    "RΓ(T-A,i_!(E)) ⟶ RΓ(B-t,i_!(E)|B-t)   ,  (comma at the end of the display line), then 'est nulle.'",
    r"\R\Gamma(B-t,i_!(E)|B-t) \]  (no comma)", "punctuation", "high",
    r"i_!(E)|B-t)¶\]", r"i_!(E)|B-t),¶\]", "Comma left out at the end of the display.")
add(157, "end of the statement of Proposition 4.2", "'est nulle' underlined, the full stop not",
    "est nulle.  (no underline)", "underline", "high", r"est nulle.", r"\emph{est nulle}.",
    "As the rest of the statement.")
add(157, "Lemme 4.3, label", "Lemme 4.3 - Soient Z un schéma noethérien ...",
    r"\begin{statement}{Lemme 4.3}  (renders 'Lemme 4.3')", "punctuation", "high",
    r"\begin{statement}{Lemme 4.3}", r"\begin{statement}{Lemme 4.3 -}", "As Proposition 4.2.")
add(157, "statement of Lemme 4.3 on p. 157",
    "underlined: 'Soient' | 'un schéma noethérien régulier connexe de dimension' | 'de' + 'caractéristiques "
    "résiduelles premières à' | 'des diviseurs réguliers se cou-' + 'pant transversalement en un point' | "
    "'d'où un diagramme d'inclusions'; not underlined: Z, 2, ℓ , X, Y, z and the commas",
    "Soient $Z$ un schéma noethérien ... d'où un diagramme d'inclusions  (no underline)", "underline", "high",
    r"Soient $Z$ un schéma noethérien régulier connexe de dimension $2$, de caractéristiques résiduelles premières à "
    r"$\ell$, $X$, $Y$ des diviseurs réguliers se coupant transversalement en un point $z$, d'où un diagramme "
    r"d'inclusions",
    r"\emph{Soient} $Z$ \emph{un schéma noethérien régulier connexe de dimension} $2$, \emph{de caractéristiques "
    r"résiduelles premières à} $\ell$, $X$, $Y$ \emph{des diviseurs réguliers se coupant transversalement en un "
    r"point} $z$, \emph{d'où un diagramme d'inclusions}",
    UND + " The last underline starts one character late (under the apostrophe of d'où). 'résiduellespremières': "
    "the typist's added s stands where the space was; the TeX's 'résiduelles premières' is the corrected wording. "
    "The statement continues on p. 158.")

# ---------------- page 158
add(158, "diagram of Lemme 4.3, top row: Z-(X ∪ Y) → Z-Y, label i'",
    "hooked arrow (hook at the source), like the vertical arrows j', j, m', m",
    r"\arrow[r,\"i'\"]  (plain arrow)".replace('\\"', '"'), "symbol", "high",
    r"""\arrow[r,"i'"]""", r"""\arrow[r,hook,"i'"]""",
    "The three horizontal arrows of this diagram are inclusions with a hook in the print (this and the next two "
    "findings).")
add(158, "same diagram, middle row: Z-X → Z, label i", "hooked arrow (hook at the source)",
    r"""\arrow[r,"i"']  (plain arrow)""", "symbol", "high",
    r"""\arrow[r,"i"']""", r"""\arrow[r,hook,"i"']""", "")
add(158, "same diagram, bottom row: Y-z → Y, label i_1", "hooked arrow (hook at the source)",
    r"""\arrow[r,"i_1"']  (plain arrow)""", "symbol", "high",
    r"""\arrow[r,"i_1"']""", r"""\arrow[r,hook,"i_1"']""", "")
add(158, "statement of Lemme 4.3, 'On fait l'hypothèse de pureté :'",
    "'On fait l'hypothèse de pureté' underlined, the colon not", "On fait l'hypothèse de pureté:  (no underline)",
    "underline", "high", "On¶fait l'hypothèse de pureté:", r"\emph{On fait l'hypothèse de pureté}:",
    "Part of the underlined statement of Lemme 4.3 (p. 157).")
add(158, "condition (P), the range of q", "(P)   R^qj_*(ℤ/ℓ) = 0      pour  q > 1   .",
    r"\text{pour }p>2.", "formula", "high", r"p>2", r"q>1",
    "Wrong letter and number in the TeX; the print's q > 1 is the purity used on p. 159 ('pour n > 1 les deux "
    "membres sont nuls ... pour q ≤ 1').")
add(158, "statement of Lemme 4.3, from 'Soit d'autre part' to 'Alors :'",
    "underlined: 'Soit d'autre part' | 'à cohomologie constructible localement' + 'constante' | 'telle que la "
    "représentation correspondante de' | 'se facto-' + 'rise à travers un' | 'groupe' (not 'ℓ-') | 'Alors'; not "
    "underlined: L ∈ ob D^b(Z-(X ∪ Y),Λ), π_1(Z-(X ∪ Y)), 'ℓ-', the commas and the colon",
    "Soit d'autre part $L\\in\\Ob D^b(...)$, ... Alors:  (no underline)", "underline", "high",
    r"Soit d'autre part $L\in\Ob D^b(Z-(X\cup Y),\Lambda)$, à cohomologie constructible localement constante, telle "
    r"que la représentation correspondante de $\pi_1(Z-(X\cup Y))$ se factorise à travers un $\ell$-groupe. Alors:",
    r"\emph{Soit d'autre part} $L\in\Ob D^b(Z-(X\cup Y),\Lambda)$, \emph{à cohomologie constructible localement "
    r"constante}, \emph{telle que la représentation correspondante de} $\pi_1(Z-(X\cup Y))$ \emph{se factorise à "
    r"travers un} $\ell$-\emph{groupe}. \emph{Alors}:",
    UND)
add(158, "Lemme 4.3 a), first line", "a) On a un isomorphisme canonique  (underlined after 'a)')",
    r"\item On a un isomorphisme canonique  (no underline)", "underline", "high",
    r"\item On a un isomorphisme canonique", r"\item \emph{On a un isomorphisme canonique}", "")
add(158, "Lemme 4.3 a), display, left side",
    "i_{1!}m'*Rj'_*L ⟶~ m*Rj_*(i'_!L) : on the left R j'_* L (the prime typed over the subscript star), no i'_!",
    r"i_{1!}m'^*\R j_*i'_!L", "formula", "high", r"i_{1!}m'^*\R j_*i'_!L", r"i_{1!}m'^*\R j'_*L",
    "The print's j'_* is the prime over the subscript star (as Rj'_*(i'^*i'_!L) = Rj'_*L at the foot of the page); "
    "the TeX reads it as j_*i'_!, which does not compose with m' (m': Y-z → Z-X, j': Z-(X ∪ Y) → Z-X). The same "
    "misreading: end of a) below and four times on p. 159.")
add(158, "end of a), 'et le complexe m'*Rj'_*L est à cohomologie ...'", "'et le complexe' underlined",
    "et le complexe  (no underline)", "underline", "high", r"et le complexe", r"\emph{et le complexe}",
    "Separate from the formula edit that follows.")
add(158, "end of a), the complex", "m'*Rj'_*L  (R j'_* L, no i'_!)", r"$m'^*\R j_*i'_!L$", "formula", "high",
    r"$m'^*\R j_*i'_!L$", r"$m'^*\R j'_*L$", "As the display of a).")
add(158, "end of a), 'est à cohomologie constructible, localement constante.'",
    "underlined: 'est à cohomologie constructible' | 'localement constante'; the comma and the full stop not",
    "no underline", "underline", "high",
    r"est à cohomologie constructible, localement constante.",
    r"\emph{est à cohomologie constructible}, \emph{localement constante}.", "")
add(158, "Lemme 4.3 b)",
    "underlined: 'Supposons' | 'connexe' | 'et soit' | 'un point géométrique de' | 'loca-' + 'lisé en un point "
    "fermé' | 'Alors la flèche de restriction'; not underlined: Y, s̄, Y, s ≠ z and the punctuation",
    "Supposons $Y$ connexe, ... Alors la flèche de restriction  (no underline)", "underline", "high",
    r"Supposons $Y$ connexe, et soit $\bar s$ un point géométrique de $Y$ localisé en un point fermé $s\ne z$. Alors "
    r"la flèche de restriction",
    r"\emph{Supposons} $Y$ \emph{connexe}, \emph{et soit} $\bar s$ \emph{un point géométrique de} $Y$ \emph{localisé "
    r"en un point fermé} $s\ne z$. \emph{Alors la flèche de restriction}", "")
add(158, "b), after (4.3.1)", "'est nulle' underlined, the full stop not", "est nulle.  (no underline)",
    "underline", "high", r"est nulle.¶\item", r"\emph{est nulle}.¶\item", "")
add(158, "Lemme 4.3 c)",
    "underlined: 'Sous les hypothèses de' | 'soit' | 'un sous-schéma fermé de dimension' | 'de' | 'tel que' | "
    "'notons' | 'le localisé strict de' | 'en' | 'Alors' + 'la flèche de restriction'; not underlined: b), C, 1, Z, "
    "Y ∩ C = s, C̃, s̄ and the punctuation",
    "Sous les hypothèses de b), ... Alors la flèche de restriction  (no underline)", "underline", "high",
    r"Sous les hypothèses de b), soit $C$ un sous-schéma fermé de dimension $1$ de $Z$ tel que $Y\cap C=s$, notons "
    r"$\widetilde C$ le localisé strict de $C$ en $\bar s$. Alors la flèche de restriction",
    r"\emph{Sous les hypothèses de} b), \emph{soit} $C$ \emph{un sous-schéma fermé de dimension} $1$ \emph{de} $Z$ "
    r"\emph{tel que} $Y\cap C=s$, \emph{notons} $\widetilde C$ \emph{le localisé strict de} $C$ \emph{en} $\bar s$. "
    r"\emph{Alors la flèche de restriction}", "")
add(158, "c), after (4.3.2)", "'est nulle' underlined, the full stop not", "est nulle.  (no underline)",
    "underline", "high", r"est nulle.¶\end{enumerate}", r"\emph{est nulle}.¶\end{enumerate}", "")
add(158, "last line, 'L'isomorphisme (trivial)'", "L'isomorphisme (trivial)  i*Rj_*i'_!L ⟶~ ...",
    "L'isomorphisme trivial", "punctuation", "high", r"L'isomorphisme trivial", r"L'isomorphisme (trivial)",
    "Parentheses left out.")

# ---------------- page 159
add(159, "first line, left side of the isomorphism",
    "isomorphisme  m'*Rj'_*L ⟶~ i_1^*m*Rj_*i'_!L : on the left R j'_* L (prime over the subscript star), no i'_!",
    r"m'^*\R j_*i'_!L\xrightarrow{\sim}", "formula", "high",
    r"m'^*\R j_*i'_!L\xrightarrow{\sim}", r"m'^*\R j'_*L\xrightarrow{\sim}",
    "As Lemme 4.3 a) on p. 158; the right side i_1^*m^*Rj_*i'_!L is right.")
add(159, "second display, left side", "i_{1!}m'*Rj'_*L ⟶ m*Rj_*(i'_!L)   ,", r"i_{1!}m'^*\R j_*i'_!L",
    "formula", "high", r"i_{1!}m'^*\R j_*i'_!L", r"i_{1!}m'^*\R j'_*L", "As the first line.")
add(159, "display after 'au-dessus de z ,'", "Rj_*(i'_!L)_z̄ = 0   .  (no outer parentheses)",
    r"(\R j_*(i'_!L))_{\bar z}=0.", "formula", "high",
    r"(\R j_*(i'_!L))_{\bar z}=0.", r"\R j_*(i'_!L)_{\bar z}=0.",
    "Outer parentheses added by the TeX (the print has them in (4.3.1) and on p. 160, not here).")
add(159, "'au cas où L est un ℤ/ℓ^ν Module localement constant'", "ℤ/ℓ^ν  Module  (capital M, no hyphen)",
    r"$\mathbb Z/\ell^\nu$-module", "word", "high",
    r"$\mathbb Z/\ell^\nu$-module", r"$\mathbb Z/\ell^\nu$ Module", "")
add(159, "'qui est simple sous-l'action d'un ℓ-groupe'", "sous-l'action  (a hyphen typed for the space)",
    "sous l'action", "misprint_in_print", "high", r"sous l'action", r"sous-l'action",
    "Typing slip of the print; the TeX silently corrects it.", corrected=r"sous l'action")
add(159, "'... le faisceau constant ℤ/ℓ . Soient Z̃ le localisé strict'",
    "one paragraph: 'Soient' follows in the same line", r"$\mathbb Z/\ell$.  (blank line)  Soient",
    "other", "high", r"$\mathbb Z/\ell$.¶¶Soient", r"$\mathbb Z/\ell$. Soient", "Paragraph break added by the TeX.")
add(159, "display after 'l'inclusion. On a', left side", "Rj_*(i'_!(ℤ/ℓ))_z̄  (no outer parentheses)",
    r"(\R j_*(i'_!(\mathbb Z/\ell)))_{\bar z}", "formula", "high",
    r"(\R j_*(i'_!(\mathbb Z/\ell)))_{\bar z}", r"\R j_*(i'_!(\mathbb Z/\ell))_{\bar z}",
    "Outer parentheses added by the TeX, as in the display above.")
add(159, "same display, right side", "= RΓ(Z̃-Ỹ,i'_!(ℤ/ℓ)   ,  (one closing parenthesis after ℓ: RΓ( is not closed)",
    r"\R\Gamma(\widetilde Z-\widetilde Y,i'_!(\mathbb Z/\ell)),", "misprint_in_print", "high",
    r"i'_!(\mathbb Z/\ell)),", r"i'_!(\mathbb Z/\ell),",
    "The TeX silently adds the closing parenthesis.", corrected=r"i'_!(\mathbb Z/\ell)),")
add(159, "'L'hypothèse (P) entraîne, par dévissage, R^qj'_*L = 0'", "R^qj'_*L = 0  (prime over the subscript star, no i'_!)",
    r"$\R^qj_*i'_!L=0$", "formula", "high", r"\R^qj_*i'_!L=0", r"\R^qj'_*L=0", "As the first line.")
add(159, "same sentence, 'pour p > 2' (edit 1 of 2)", "pour  p > 2",
    "$q>2$: neither the print (p > 2) nor the correct reading (q > 1)", "number", "high",
    r"$q>2$", r"$q>1$",
    "Edit 1 of 2, apply before the misprint edit that follows: it gives the corrected edition the correct q > 1 "
    "(condition (P) on p. 158, and 'pour q ≤ 1' in the next sentence); the misprint edit then restores the print's "
    "p > 2 in the diplomatic edition.")
add(159, "same sentence, 'pour p > 2' (edit 2 of 2)", "pour  p > 2", "$q>2$ (after edit 1: $q>1$)",
    "misprint_in_print", "high", r"$q>1$", r"$p>2$",
    "Wrong letter and number in the print: the vanishing needed is for q > 1 (the next sentence treats q ≤ 1). The "
    "TeX corrected the letter only. The 'old' is the text after edit 1: apply the two in order.",
    corrected=r"$q>1$")
add(159, "'la locale constance de m'*R^qj'_*L pour q ≤ 1'", "m'*R^qj'_*L", r"$m'^*\R^qj_*i'_!L$", "formula",
    "high", r"$m'^*\R^qj_*i'_!L$", r"$m'^*\R^qj'_*L$", "As the first line.")
add(159, "'on a alors m'*j'_*L = (L_o)_{Y-z}'", "m'*j'_*L = (L_o)_{Y-z}", r"m'^*j_*i'_!L=(L_0)_{Y-z}", "formula",
    "high", r"m'^*j_*i'_!L=(L_0)", r"m'^*j'_*L=(L_0)", "As the first line.")
add(159, "between the two formulas of 'on a alors'", "(L_o)_{Y-z} , et m'*R^1j'_*L = ...",
    r"(L_0)_{Y-z}, \qquad m'^*\R^1j_*i'_!L  (no 'et')", "missing", "high",
    r"_{Y-z},¶\qquad", r"_{Y-z},¶\quad\text{et}\quad", "The word 'et' is left out.")
add(159, "'m'*R^1j'_*L = (L_o)_{Y-z}(-1) par Abhyankar'", "m'*R^1j'_*L", r"m'^*\R^1j_*i'_!L", "formula", "high",
    r"m'^*\R^1j_*i'_!L", r"m'^*\R^1j'_*L", "As the first line.")

# ---------------- page 160
add(160, "'... lemme d'Abhyankar. On a donc démontré a).'",
    "one paragraph: the line before is full and 'On a donc' starts at the margin, not indented like the paragraphs "
    "of the page ('Prouvons 4.2')", "d'Abhyankar.  (blank line)  On a donc", "other", "medium",
    r"d'Abhyankar.¶¶On a donc", r"d'Abhyankar. On a donc", "Paragraph break added by the TeX.")
add(160, "end of 'a : η̄ ⟶ Y(z̄) , b : η̄ ⟶ Y(s̄)'", "no punctuation after Y(s̄); the next line begins '(où'",
    r"b:\bar\eta\to Y(\bar s),", "punctuation", "high", r"Y(\bar s),¶\]", r"Y(\bar s)¶\]",
    "Comma added at the end of the display.")
add(160, "'(où Y(z̄) (resp. Y(s̄) est le localisé strict ...'", "(où  Y(z̄)  ...: the clause opens with a parenthesis",
    r"où $Y(\bar z)$", "punctuation", "high", r"où $Y(\bar z)$", r"(où $Y(\bar z)$",
    "Apply with the two edits on the same clause below (a misprint and the closing parenthesis).")
add(160, "same clause, '(resp. Y(s̄) est'", "(resp. Y(s̄)  est: the parenthesis of 'resp.' is not closed",
    r"(resp. $Y(\bar s)$) est", "misprint_in_print", "high", r"$Y(\bar s)$) est", r"$Y(\bar s)$ est",
    "The TeX silently closes it.", corrected=r"$Y(\bar s)$) est")
add(160, "same clause, end '(resp. s̄)). Posons'", "(resp. s̄)). Posons  (two closing parentheses)",
    r"(resp. $\bar s$). Posons", "punctuation", "high", r"(resp. $\bar s$). Posons", r"(resp. $\bar s$)). Posons",
    "Closes the parenthesis that opens at '(où' (edit above).")
add(160, "end of the last diagram, after RΓ(Z̃-Ỹ,(i'_!L)|Z̃-Ỹ)", "a comma to the right of the bottom row",
    r"... |\widetilde Z-\widetilde Y) \arrow[u]  (no comma)", "punctuation", "high",
    r"|\widetilde Z-\widetilde Y) \arrow[u]", r"|\widetilde Z-\widetilde Y) , \arrow[u]",
    "Comma after the diagram left out.")
add(160, "after the last diagram, 'la nullité de 4.3.2 découle donc de b)'",
    "la nullité  (small l; the sentence runs on after the diagram's comma)", "La nullité", "word", "high",
    r"La nullité de 4.3.2", r"la nullité de 4.3.2", "Capital against small letter.")
add(160, "end of the page: the last four printed lines, 'maximal de T , D = f^{-1}(z) (≃ P^1_s) ...' to "
         "'... signifient que A' est disjoint de'",
    "p. 160 ends '... les hypothèses de position générale sur A, B , X signifient que A' est disjoint de'",
    "page_160.tex ends at 'Prouvons 4.2. Soient $f:T'\\to T$ l'éclatement de l'idéal'; the rest of p. 160 stands "
    "after the folio 161 marker", "marker", "high", None, None,
    "Page 161 really begins at '$B'\\cup X'$. Notons $E'$ l'image inverse' (s5.tex line 5075 at 20:22, mid-line, in "
    "both layers). Exact fix: python -I move_marker.py 5 161 \"\\$B'\\\\cup X'\\$. Notons\" (bash double quotes; the "
    "anchor is $B'\\cup X'$. Notons; simulated in memory on both layers: the marker then stands on its own line "
    "after 'signifient que $A'$ est disjoint de' and before '$B'\\cup X'$. Notons'). The moved text was compared "
    "with the scan of p. 160: no difference.")

json.dump(F, open(OUT, 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
print(len(F), 'findings written')
