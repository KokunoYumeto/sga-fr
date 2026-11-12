"""Build findings_311_315.json; check that every fix's old occurs exactly once in its page file (dependent misprint
fixes: in the text after the fixes listed before them on that page) and that the fixes apply in order."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
B = RUN / "b311_315"
OUT = RUN / "findings_311_315.json"


def n(s):
    return None if s is None else s.replace("¶", "\n")


F = []


def add(page, where, scan, tex, kind, conf, old, new, note="", corrected=None, after=False):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": n(old), "new": n(new)}}
    if kind == "misprint_in_print":
        d["corrected"] = n(corrected)
    d["note"] = note
    d["_after"] = after
    F.append(d)


R_NOTE = r"Plain typewriter R; \R is \mathbb{R} in this file (as the applied fixes of pp. 283-295)."
DOT_NOTE = r"The print's A with a small raised dot (A•), not the star of u*; A^\bullet as the applied fixes of pp. 290-295."
UL_NOTE = r"Exposé VII statements: the TeX has no underline markup; \emph as the applied statements of pp. 283-295."

# ---------------- page 311 ----------------
add(311, "first sentence, 'une structure de A•(Y)-module'", "A• (raised dot)", r"$A^*(Y)$-module", "symbol", "high",
    r"structure de $A^*(Y)$-module, provenant", r"structure de $A^\bullet(Y)$-module, provenant", DOT_NOTE)
add(311, "'les structures de A•(Y)-module de Q(Y,M) et de A•(Z)-module'", "A• twice", r"$A^*(Y)$, $A^*(Z)$", "symbol",
    "high", r"les structures de $A^*(Y)$-module de $Q(Y,M)$ et de $A^*(Z)$-module",
    r"les structures de $A^\bullet(Y)$-module de $Q(Y,M)$ et de $A^\bullet(Z)$-module")
add(311, "'On en déduit un morphisme de A•(Z)-modules'", "A•", r"$A^*(Z)$-modules", "symbol", "high",
    r"un morphisme de $A^*(Z)$-modules", r"un morphisme de $A^\bullet(Z)$-modules")
add(311, "display A•(Z) ⊗_{A•(Y)} Q(Y,M) → Q(Z,u*M) .", "A• twice", r"A^*(Z)\otimes_{A^*(Y)}", "symbol", "high",
    r"A^*(Z)\otimes_{A^*(Y)}", r"A^\bullet(Z)\otimes_{A^\bullet(Y)}")
add(311, "Proposition 5.5, first two sentences",
    "underlined: 'Soient' | 'un schéma' | 'un' | 'Module localement libre de rang' | 'On note' | 'le' | "
    "'schéma des drapeaux de type' | 'de' (S, E, O_S-, r, f : X → S, S-, (p_1,...,p_m) and the punctuation not); "
    "Module with a capital M; the O of O_S a plain typed O",
    r"Soient $S$ un schéma, $E$ un $\mathcal O_S$-module ... (no underline markup)", "underline", "high",
    r"Soient $S$ un schéma, $E$ un $\mathcal O_S$-module localement libre de rang $r$. On note $f:X\to S$ le $S$-schéma des drapeaux de type $(p_1,\ldots,p_m)$ de $E$.",
    r"\emph{Soient} $S$ \emph{un schéma}, $E$ \emph{un} $\mathcal O_S$-\emph{Module localement libre de rang} $r$. \emph{On note} $f:X\to S$ \emph{le} $S$-\emph{schéma des drapeaux de type} $(p_1,\ldots,p_m)$ \emph{de} $E$.",
    UL_NOTE + " One edit: it also gives the print's capital M (word).")
add(311, "Proposition 5.5, 'Alors, pour tout A_S-Module L , le morphisme canonique'",
    "underlined: 'Alors, pour' / 'tout' | 'Module' | 'le morphisme canonique' (A_S-, L and its comma not); "
    "Module with a capital M", r"Alors, pour tout $A_S$-module $L$, le morphisme canonique", "underline", "high",
    r"Alors, pour tout $A_S$-module $L$, le morphisme canonique",
    r"\emph{Alors, pour tout} $A_S$-\emph{Module} $L$, \emph{le morphisme canonique}",
    "One edit: it also gives the capital M (word).")
add(311, "Proposition 5.5, display α : A•(X) ⊗_{A•(S)} Q(S,L) → Q(X,f*L)", "A• twice", r"\alpha:A^*(X)\otimes_{A^*(S)}",
    "symbol", "high", r"\alpha:A^*(X)\otimes_{A^*(S)}", r"\alpha:A^\bullet(X)\otimes_{A^\bullet(S)}")
add(311, "Proposition 5.5, 'est un isomorphisme.'", "underlined (the full stop not)", "est un isomorphisme.",
    "underline", "high", r"est un isomorphisme.¶\end{statement}", r"\emph{est un isomorphisme}.¶\end{statement}")
add(311, "proof, display A•(D) ⊗_{A•(S)} Q(S,L) → Q(D,h*L)", "A• twice", r"A^*(D)\otimes_{A^*(S)}", "symbol", "high",
    r"A^*(D)\otimes_{A^*(S)}", r"A^\bullet(D)\otimes_{A^\bullet(S)}")
add(311, "proof, display A•(D) ⊗_{A•(X)} Q(X,g*L) → Q(D,g*L)", "A• twice", r"A^*(D)\otimes_{A^*(X)}", "symbol", "high",
    r"A^*(D)\otimes_{A^*(X)}", r"A^\bullet(D)\otimes_{A^\bullet(X)}")
add(311, "proof, 'Par suite id_{A•(D)} ⊗ α ... puisque A•(D) est libre sur A•(X).'", "A• three times",
    r"\mathrm{id}_{A^*(D)}, $A^*(D)$, $A^*(X)$", "symbol", "high",
    r"\mathrm{id}_{A^*(D)}\otimes\alpha$ est un isomorphisme, d'où le résultat puisque $A^*(D)$ est libre sur $A^*(X)$",
    r"\mathrm{id}_{A^\bullet(D)}\otimes\alpha$ est un isomorphisme, d'où le résultat puisque $A^\bullet(D)$ est libre sur $A^\bullet(X)$")
add(311, "display A•(X/T) = ⊕_i R^{2i}(u o f)_*(A_X)", "A•", r"A^*(X/T)", "symbol", "high",
    r"A^*(X/T)=\bigoplus_i", r"A^\bullet(X/T)=\bigoplus_i")
add(311, "display A•(X/T) = ⊕_i R^{2i}(u o f)_*(A_X)", "R^{2i}: plain typewriter R", r"\R^{2i}", "font", "high",
    r"\R^{2i}(u\circ f)_*(A_X)", r"\mathrm{R}^{2i}(u\circ f)_*(A_X)", R_NOTE)
add(311, "'et de même A•(S/T) = ⊕_i R^{2i} u_*(A_S).'", "A•", r"A^*(S/T)", "symbol", "high",
    r"A^*(S/T)=\bigoplus_i", r"A^\bullet(S/T)=\bigoplus_i")
add(311, "'et de même A•(S/T) = ⊕_i R^{2i} u_*(A_S).'", "R^{2i}: plain typewriter R", r"\R^{2i}", "font", "high",
    r"\R^{2i}u_*(A_S)", r"\mathrm{R}^{2i}u_*(A_S)", R_NOTE)
add(311, "'Enfin, pour tout A_S-Module L , on pose'", "Module with a capital M", r"$A_S$-module", "word", "high",
    r"pour tout $A_S$-module $L$, on pose", r"pour tout $A_S$-Module $L$, on pose",
    "The typescript's capital M (sheaf of modules), as the applied 'Module' of pp. 282-295.")
add(311, "display Q(S/T,L) = ⊕_{n,i} R^{2i} u_*(L ⊗ μ_S^{⊗i}) (printed at the top of p. 312)",
    "plain typewriter R", r"\R^n", "font", "high", r"\bigoplus_{n,i}\R", r"\bigoplus_{n,i}\mathrm{R}",
    "Printed on p. 312; filed under p. 311, where the display stands until the marker move of p. 312 (the edit does "
    "not touch the move's anchor). " + R_NOTE)
add(311, "display Q(S/T,L) = ⊕_{n,i} R^{2i} u_*(L ⊗ μ_S^{⊗i}) (printed at the top of p. 312)",
    "the exponent of R is 2i (sum over n,i)", r"\R^n u_*(L\otimes\mu_S^{\otimes i})", "misprint_in_print", "high",
    r"^n u_*(L", r"^{2i} u_*(L",
    "The sum runs over n and i and n occurs nowhere else: R^n is meant, as in Q(X/T,f*L) = ⊕_{n,i} R^n(u o f)_*(...) "
    "just below; the typist repeated the 2i of A•(S/T) = ⊕ R^{2i}u_*(A_S). The TeX silently corrects it. Printed on "
    "p. 312, filed under p. 311 (see the previous item); the old does not overlap the font fix.",
    corrected=r"^n u_*(L")

# ---------------- page 312 ----------------
add(312, "top of the page",
    "p. 312 begins with the display 'Q(S/T,L) = ⊕_{n,i} R^{2i} u_*(L ⊗ μ_S^{⊗i})', then 'et Q(X/T,f*L) = ...'; "
    "p. 311 ends with 'Enfin, pour tout A_S-Module L , on pose'",
    r"page_311.tex ends with the display '\[ Q(S/T,L)=\bigoplus_{n,i}\R^n u_*(L\otimes\mu_S^{\otimes i}) \]'; the folio-312 marker stands before 'et'",
    "marker", "high", None, None,
    r"Page 312 really begins at the '\[' that opens the display 'Q(S/T,L)=...' (the line after 'Enfin, pour tout "
    r"$A_S$-module $L$, on pose'). Exact fix (bash): python -I move_marker.py 5 312 $'\\[\nQ(S/T,L)' --before "
    r"(simulated in memory on both layers: the marker then stands on its own line between '... on pose' and '\['; "
    r"a second run finds no anchor and changes nothing). Text not moved; the two fixes of the moving display are filed "
    r"under p. 311 and do not touch the anchor.")
add(312, "display Q(X/T,f*L) = ⊕_{n,i} R^n(u o f)_*(f*L ⊗ μ_X^{⊗i}).", "plain typewriter R", r"\R^n", "font", "high",
    r"\bigoplus_{n,i}\R^n(u\circ f)_*", r"\bigoplus_{n,i}\mathrm{R}^n(u\circ f)_*", R_NOTE)
add(312, "display H^{2j}(X,μ_X^{⊗j}) → H°(T,R^{2j}(u o f)_*(μ_X^{⊗j})", "plain typewriter R", r"\R^{2j}", "font",
    "high", r"H^0(T,\R^{2j}", r"H^0(T,\mathrm{R}^{2j}", R_NOTE)
add(312, "display H^{2j}(X,μ_X^{⊗j}) → H°(T,R^{2j}(u o f)_*(μ_X^{⊗j})",
    "one closing parenthesis at the end: '(μ_X^{⊗j} )' and nothing after it", r"(\mu_X^{\otimes j}))",
    "misprint_in_print", "high", r"(\mu_X^{\otimes j}))¶\]", r"(\mu_X^{\otimes j})¶\]",
    "The parenthesis opened after H° is never closed; the TeX silently adds it.",
    corrected=r"(\mu_X^{\otimes j}))¶\]")
add(312, "'définit un A_T-morphisme.' before the display c_{ij}", "a typed full stop after 'morphisme'",
    r"définit un $A_T$-morphisme", "misprint_in_print", "medium", r"définit un $A_T$-morphisme",
    r"définit un $A_T$-morphisme.",
    "The sentence goes on in the display 'c_{ij} : A_T → R^{2j}(u o f)_*(μ_X^{⊗j}) .', which has its own stop; the "
    "stop before it is the typist's. The TeX silently drops it.",
    corrected=r"définit un $A_T$-morphisme")
add(312, "display c_{ij} : A_T → R^{2j}(u o f)_*(μ_X^{⊗j}) .", "plain typewriter R", r"\R^{2j}", "font", "high",
    r"A_T\to \R^{2j}", r"A_T\to \mathrm{R}^{2j}", R_NOTE)
add(312, "'permettent de définir un morphisme de A•(S/T)-Algèbres'", "A•; Algèbres with a capital A",
    r"$A^*(S/T)$-algèbres", "word", "high", r"de définir un morphisme de $A^*(S/T)$-algèbres",
    r"de définir un morphisme de $A^\bullet(S/T)$-Algèbres",
    "One edit: the capital A (as the applied 'Algèbre(s)' of p. 287) and the raised dot for the star (symbol).")
add(312, "display θ_1 : A•(S/T)[T_{i,j_i}]_{(i,j_i)} → A•(X/T)", "A• twice", r"A^*(S/T), A^*(X/T)", "symbol", "high",
    r"\theta_1:A^*(S/T)[T_{i,j_i}]_{(i,j_i)}\to A^*", r"\theta_1:A^\bullet(S/T)[T_{i,j_i}]_{(i,j_i)}\to A^\bullet")
add(312, "end of the display θ_1 : ... → A•(X/T)", "no punctuation", r"A^*(X/T).", "punctuation", "high",
    r"(X/T).¶\]¶Notant", r"(X/T)¶\]¶Notant", "The TeX adds a full stop at the end of the display.")
add(312, "'Notant c_i les sections de A•(S/T)'", "A•", r"$A^*(S/T)$", "symbol", "high",
    r"sections de $A^*(S/T)$", r"sections de $A^\bullet(S/T)$")
add(312, "'θ_1 s'annule sur l'Idéal J'", "Idéal with a capital I", "l'idéal", "word", "high",
    r"l'idéal $J$", r"l'Idéal $J$", "The typescript's capital I (sheaf of ideals), as the applied 'Idéal' of pp. 287, 294.")
add(312, "'D'où un morphisme de A•(S/T)-Algèbres'", "A•; Algèbres with a capital A", r"$A^*(S/T)$-algèbres", "word",
    "high", r"D'où un morphisme de $A^*(S/T)$-algèbres", r"D'où un morphisme de $A^\bullet(S/T)$-Algèbres",
    "One edit: also the raised dot for the star (symbol).")
add(312, "display θ : A•(S/T)[T_{i,j_i}]_{(i,j_i)}/J → A•(X/T) .", "A• twice", r"A^*(S/T), A^*(X/T)", "symbol", "high",
    r"\theta:A^*(S/T)[T_{i,j_i}]_{(i,j_i)}/J\to A^*(X/T).",
    r"\theta:A^\bullet(S/T)[T_{i,j_i}]_{(i,j_i)}/J\to A^\bullet(X/T).")
add(312, "Proposition 5.6, 'Avec les notations précédentes :'", "underlined (the colon not); a colon",
    "Avec les notations précédentes:", "underline", "high", r"Avec les notations précédentes:",
    r"\emph{Avec les notations précédentes} :", UL_NOTE)
add(312, "Proposition 5.6 a), 'Le morphisme de A•(S/T)-Algèbres'",
    "underlined: 'Le morphisme de' | 'Algèbres'; A•; Algèbres with a capital A",
    r"\item Le morphisme de $A^*(S/T)$-algèbres", "underline", "high", r"\item Le morphisme de $A^*(S/T)$-algèbres",
    r"\item \emph{Le morphisme de} $A^\bullet(S/T)$-\emph{Algèbres}",
    "One edit: it also gives the capital A (word) and the raised dot (symbol).")
add(312, "Proposition 5.6 a), display θ : A•(S/T)[...]/J → A•(X/T)", "A• twice", r"A^*(S/T), A^*(X/T)", "symbol",
    "high", r"\theta:A^*(S/T)[T_{i,j_i}]_{(i,j_i)}/J\to A^*(X/T)¶\]",
    r"\theta:A^\bullet(S/T)[T_{i,j_i}]_{(i,j_i)}/J\to A^\bullet(X/T)¶\]")
add(312, "Proposition 5.6 a), 'est un isomorphisme.'", "underlined (the full stop not)", "est un isomorphisme.",
    "underline", "high", r"est un isomorphisme.", r"\emph{est un isomorphisme}.")
add(312, "Proposition 5.6 b), 'Pour tout A_S-Module L , le morphisme canonique de A•(X/T)-Modules'",
    "underlined: 'Pour tout' | 'Module' | 'le morphisme canonique de' | 'Modules' (A_S-, L, A•(X/T)- not); "
    "Module(s) with a capital M; A•",
    r"\item Pour tout $A_S$-module $L$, le morphisme canonique de $A^*(X/T)$-modules", "underline", "high",
    r"\item Pour tout $A_S$-module $L$, le morphisme canonique de $A^*(X/T)$-modules",
    r"\item \emph{Pour tout} $A_S$-\emph{Module} $L$, \emph{le morphisme canonique de} $A^\bullet(X/T)$-\emph{Modules}",
    "One edit: it also gives the capital M twice (word) and the raised dot (symbol).")

# ---------------- page 313 ----------------
add(313, "display A•(X/T) ⊗_{A•(S/T)} Q(S/T,L) → Q(X/T,f*L)", "A• twice", r"A^*(X/T)\otimes_{A^*(S/T)}", "symbol",
    "high", r"A^*(X/T)\otimes_{A^*(S/T)}", r"A^\bullet(X/T)\otimes_{A^\bullet(S/T)}")
add(313, "Proposition 5.6 b), 'est un isomorphisme.'", "underlined (the full stop not)", "est un isomorphisme.",
    "underline", "high", r"est un¶isomorphisme.", r"\emph{est un isomorphisme}.")

# ---------------- page 314 ----------------
add(314, "section title 6", "'6. SCHEMAS EN GROUPES': capitals, underlined, no full stop",
    r"\section*{6. Schémas en groupes}", "word", "high", r"\section*{6. Schémas en groupes}",
    r"\section*{6. SCHÉMAS EN GROUPES}",
    "Capitals as printed, as the applied '3. CLASSES DE CHERN' (p. 290); accented capital as the volume's rule.")
add(314, "Proposition 6.1, first sentence",
    "underlined: 'Soient' | 'un schéma' | 'un' | 'schéma en groupes quasi-compact, lisse' / 'et à fibres connexes, et' "
    "| 'un' | 'schéma muni d'une opération à gauche de' (S, G, S-, X and the final G . not)",
    "Soient $S$ un schéma, $G$ un $S$-schéma ... (no underline markup)", "underline", "high",
    r"Soient $S$ un schéma, $G$ un $S$-schéma en groupes quasi-compact, lisse et à fibres connexes, et $X$ un $S$-schéma muni d'une opération à gauche de $G$.",
    r"\emph{Soient} $S$ \emph{un schéma}, $G$ \emph{un} $S$-\emph{schéma en groupes quasi-compact, lisse et à fibres connexes, et} $X$ \emph{un} $S$-\emph{schéma muni d'une opération à gauche de} $G$.",
    UL_NOTE)
add(314, "Proposition 6.1, second sentence",
    "underlined: 'Si' | 'est un' | 'torseur' | 'sous' | 'on note' | 'le' | 'schéma obtenu à' / 'partir de' | "
    "'par torsion au moyen de' | 'et de l'opération de' | 'sur' ('(à droite)', the formulas and S- not)",
    "Si $f:E\\to S$ est un $S$-torseur ... (no underline markup)", "underline", "high",
    r"Si $f:E\to S$ est un $S$-torseur (à droite) sous $G$, on note $X_E$ le $S$-schéma obtenu à partir de $X$ par torsion au moyen de $E$ et de l'opération de $G$ sur $X$.",
    r"\emph{Si} $f:E\to S$ \emph{est un} $S$-\emph{torseur} (à droite) \emph{sous} $G$, \emph{on note} $X_E$ \emph{le} $S$-\emph{schéma obtenu à partir de} $X$ \emph{par torsion au moyen de} $E$ \emph{et de l'opération de} $G$ \emph{sur} $X$.")
add(314, "Proposition 6.1, 'On note p : X → S et q : X_E → S les projections canoniques. Dans ces conditions, pour tout A_S-Module M et tout entier i , le A_S-Module'",
    "underlined: 'On note' | 'et' | 'les projections canoniques. Dans ces conditions, pour tout' | 'Module' | "
    "'et tout entier' | 'le' | 'Module' (formulas, A_S- and i not); Module with a capital M twice",
    "On note $p:X\\to S$ et ... le $A_S$-module (no underline markup)", "underline", "high",
    r"On note $p:X\to S$ et $q:X_E\to S$ les projections canoniques. Dans ces conditions, pour tout $A_S$-module $M$ et tout entier $i$, le $A_S$-module",
    r"\emph{On note} $p:X\to S$ \emph{et} $q:X_E\to S$ \emph{les projections canoniques. Dans ces conditions, pour tout} $A_S$-\emph{Module} $M$ \emph{et tout entier} $i$, \emph{le} $A_S$-\emph{Module}",
    "One edit: it also gives the print's capital M twice (word).")
add(314, "Proposition 6.1, 'R^i q_*(q*M)'", "plain typewriter R", r"$\R^iq_*(q^*M)$", "font", "high",
    r"$\R^iq_*(q^*M)$", r"$\mathrm{R}^iq_*(q^*M)$", R_NOTE)
add(314, "Proposition 6.1, 'est canoniquement isomorphe à'", "underlined (across the line break)",
    "est canoniquement isomorphe à", "underline", "high", r"est canoniquement isomorphe à",
    r"\emph{est canoniquement isomorphe à}")
add(314, "Proposition 6.1, 'à R^i p_*(p*M).'", "plain typewriter R", r"$\R^ip_*(p^*M)$", "font", "high",
    r"$\R^ip_*(p^*M)$.", r"$\mathrm{R}^ip_*(p^*M)$.", R_NOTE)
add(314, "diagram (D_1), label of the bottom arrow E → S", "f above the arrow", r"""\arrow[r,"f"']""", "other", "high",
    r"""X_E \arrow[d,"q"]\\¶E \arrow[r,"f"']""", r"""X_E \arrow[d,"q"]\\¶E \arrow[r,"f"]""",
    "tikz-cd sets a swapped label below a rightward arrow. φ (above), pr_1 (left) and q (right) are right.")
add(314, "diagram (D_2), label of the bottom arrow E → S", "f above the arrow", r"""\arrow[r,"f"']""", "other", "high",
    r"""X \arrow[d,"p"]\\¶E \arrow[r,"f"']""", r"""X \arrow[d,"p"]\\¶E \arrow[r,"f"]""",
    "tikz-cd sets a swapped label below a rightward arrow. pr_2 (above), pr_1 (left) and p (right) are right.")
add(314, "diagram (D_2), vertex S", "no full stop after S", "& S .", "punctuation", "high", r"& S .", r"& S",
    "The TeX adds a full stop.")
add(314, "display u : f*R^i q_*(q*M) ≃> R^i(pr_1)_*(φ*q*M) .", "both R plain typewriter R", r"\R^i twice", "font",
    "high", r"u:f^*\R^iq_*(q^*M)\xrightarrow{\sim}\R^i(\pr_1)_*(\varphi^*q^*M)",
    r"u:f^*\mathrm{R}^iq_*(q^*M)\xrightarrow{\sim}\mathrm{R}^i(\pr_1)_*(\varphi^*q^*M)", R_NOTE)
add(314, "display v : f*R^i p_*(p*M) ≃> R^i(pr_1)_*((pr_2)*p*M).", "both R plain typewriter R", r"\R^i twice", "font",
    "high", r"v:f^*\R^ip_*(p^*M)\xrightarrow{\sim}\R^i(\pr_1)_*((\pr_2)^*p^*M)",
    r"v:f^*\mathrm{R}^ip_*(p^*M)\xrightarrow{\sim}\mathrm{R}^i(\pr_1)_*((\pr_2)^*p^*M)", R_NOTE)
add(314, "display v^{-1} o u : f*R^i q_*(q*M) ≃> f*R^i p_*(p*M) .", "both R plain typewriter R", r"\R^i twice", "font",
    "high", r"\circ u:f^*\R^iq_*(q^*M)\xrightarrow{\sim} f^*\R^ip_*(p^*M)",
    r"\circ u:f^*\mathrm{R}^iq_*(q^*M)\xrightarrow{\sim} f^*\mathrm{R}^ip_*(p^*M)", R_NOTE)

# ---------------- page 315 ----------------
add(315, "top of the page (and foot of p. 314)",
    "p. 314 ends with 'non vides et connexes, il résulte de'; p. 315 begins 'il résulte de (SGA 4 XII 6.5 (i)) que ...' "
    "(the words repeated)",
    "page_314.tex ends with 'connexes, il'; the folio-315 marker stands before 'résulte de (SGA 4 XII 6.5 (i))'",
    "marker", "high", None, None,
    r"The TeX's single 'il résulte de' is split by the marker after 'il'; 'résulte de' belongs to p. 314, whose last "
    r"line ends with it. Page 315 really begins at '(SGA 4 XII 6.5 (i))' (before the repeated words, next item). "
    r"Exact fix: python -I move_marker.py 5 315 '(SGA 4 XII 6.5' (no --before; simulated in memory on both layers: "
    r"page 314 then ends 'il\nrésulte de ' and the marker stands on its own line before '(SGA 4 XII 6.5 (i)) que'). "
    r"Run it once, before the insertion of the next item. Text not moved.")
add(315, "first line, 'il résulte de (SGA 4 XII 6.5 (i))'",
    "'il résulte de' printed twice: at the foot of p. 314 and again at the top of p. 315",
    "the TeX has the words once ('il' / 'résulte de' across the marker)", "misprint_in_print", "high",
    r"(SGA 4 XII 6.5 (i)) que", r"il résulte de (SGA 4 XII 6.5 (i)) que",
    "The typist repeated the last words of p. 314 at the top of p. 315; the TeX silently keeps one copy. Apply after "
    "the marker move of the previous item (applied before it, the move would leave both copies on p. 314). The old "
    "occurs once before and after the move.",
    corrected=r"(SGA 4 XII 6.5 (i)) que")
add(315, "Proposition 6.2, attribution '(Mme RAYNAUD ([5]).'", "RAYNAUD in capitals", "Mme Raynaud", "word", "high",
    r"Mme Raynaud", r"Mme RAYNAUD", "As the applied capitals of 'GYSIN' (p. 285) and 'J. P. JOUANOLOU' (p. 282).")
add(315, "Proposition 6.2, attribution '(Mme RAYNAUD ([5]).'",
    "[5] in parentheses, the full stop after the parentheses", "[5].)", "punctuation", "high", r"[5].)", r"([5])).",
    "The TeX drops the parentheses round [5] and puts the full stop inside. The new text has the closing parenthesis "
    "the print leaves out; the next item restores the printed reading.")
add(315, "Proposition 6.2, attribution '(Mme RAYNAUD ([5]).'",
    "two opening parentheses, one closing: '(Mme RAYNAUD ([5]).'", "(Mme Raynaud [5].)", "misprint_in_print", "medium",
    r"([5])).", r"([5]).",
    "The parenthesis opened before 'Mme' is never closed. Its old is taken from the text after the punctuation fix "
    "listed above (apply that first). Corrected reading: one more closing parenthesis.",
    corrected=r"([5])).", after=True)
add(315, "Proposition 6.2, first sentences up to 'le A_S-Module'",
    "underlined: 'Soient' | 'un schéma et' | 'un' | 'schéma en' / 'groupes réductifs' | 'Pour tout' | "
    "'Module localement constant constructible' | 'et pour tout entier' | 'le' | 'Module' (S, p : G → S, S-, "
    "(SGA 3 XIX)., A_S-, M, i not); Module with a capital M twice",
    "Soient $S$ un schéma et ... le $A_S$-module (no underline markup)", "underline", "high",
    r"Soient $S$ un schéma et $p:G\to S$ un $S$-schéma en groupes réductifs (SGA 3 XIX). Pour tout $A_S$-module localement constant constructible $M$ et pour tout entier $i$, le $A_S$-module",
    r"\emph{Soient} $S$ \emph{un schéma et} $p:G\to S$ \emph{un} $S$-\emph{schéma en groupes réductifs} (SGA 3 XIX). \emph{Pour tout} $A_S$-\emph{Module localement constant constructible} $M$ \emph{et pour tout entier} $i$, \emph{le} $A_S$-\emph{Module}",
    UL_NOTE + " One edit: it also gives the print's capital M twice (word).")
add(315, "Proposition 6.2, 'le A_S-Module R^i p_*(p*M)'", "plain typewriter R", r"$\R^ip_*(p^*M)$", "font", "high",
    r"$\R^ip_*(p^*M)$", r"$\mathrm{R}^ip_*(p^*M)$", R_NOTE)
add(315, "Proposition 6.2, 'est localement constant et constructible. De plus, pour tout morphisme'",
    "underlined (one run across the line break)", "no underline markup", "underline", "high",
    r"est localement constant et constructible. De plus, pour tout morphisme",
    r"\emph{est localement constant et constructible. De plus, pour tout morphisme}")
add(315, "Proposition 6.2, 'définissant un diagramme cartésien'", "underlined", "no underline markup", "underline",
    "high", r"définissant un diagramme cartésien", r"\emph{définissant un diagramme cartésien}")
add(315, "Proposition 6.2, diagram, label of the bottom arrow S' → S", "u above the arrow", r"""\arrow[r,"u"']""",
    "other", "high", r"""S' \arrow[r,"u"']""", r"""S' \arrow[r,"u"]""",
    "tikz-cd sets a swapped label below a rightward arrow. u' (above), p' (left) and p (right) are right.")
add(315, "Proposition 6.2, diagram, vertex S", "no comma after S", "& S,", "punctuation", "high", r"& S,", r"& S",
    "The TeX adds a comma.")
add(315, "Proposition 6.2, 'le morphisme de changement de base'", "underlined", "no underline markup", "underline",
    "high", r"le morphisme de changement de base", r"\emph{le morphisme de changement de base}")
add(315, "Proposition 6.2, display u*R^i p_*(p*M) → R^i p'_*(p o u')*(M)", "both R plain typewriter R", r"\R^i twice",
    "font", "high", r"u^*\R^ip_*(p^*M)\to \R^ip'_*", r"u^*\mathrm{R}^ip_*(p^*M)\to \mathrm{R}^ip'_*", R_NOTE)
add(315, "Proposition 6.2, 'est un isomorphisme.'", "underlined (the full stop not)", "est un isomorphisme.",
    "underline", "high", r"est un isomorphisme.¶\end{statement}", r"\emph{est un isomorphisme}.¶\end{statement}")
add(315, "proof, 'les foncteurs R^i r_*'", "plain typewriter R", r"$\R^ir_*$", "font", "high",
    r"$\R^ir_*$", r"$\mathrm{R}^ir_*$", R_NOTE)
add(315, "proof, 'Par ailleurs, par (SGA 4 XXII 5.5.1)'", "(SGA 4 XXII 5.5.1)", "(SGA 4 XXII 5.5.1)",
    "misprint_in_print", "high", None, None,
    "Wrong reference: SGA 4 has no Exposé XXII; the structure of the Borel subgroup B is SGA 3 XXII 5.5.1, as the "
    "neighbouring references (SGA 3 XXII 5.1.1, 5.8.5). The TeX keeps the printed reading; the current layer already "
    "reads 'SGA 3 XXII 5.5.1'.",
    corrected=r"(SGA 3 XXII 5.5.1)")
add(315, "proof, 'de fibrés vectoriels épointés et par suite'", "no comma after 'épointés'", "épointés, et par",
    "punctuation", "high", r"épointés, et par", r"épointés et par", "The TeX adds a comma.")
add(315, "end of the page / folio-316 marker",
    "p. 315 ends with '... que, notant t : B → S le morphisme canonique, les'; p. 316 begins 'faisceaux R^i t_*(t*M), "
    "avec M un A_S-Module ...'",
    "page_315.tex ends with 'épointés, et par'; 'suite il résulte immédiatement de (1.1) et (1.2) que, notant "
    "$t:B\\to S$ le morphisme canonique, les' stands under the folio-316 marker",
    "marker", "high", None, None,
    r"Page 316 really begins at 'faisceaux $\R^it_*(t^*M)$' (the same line, after '... le morphisme canonique, les'). "
    r"Exact fix: python -I move_marker.py 5 316 'faisceaux' (no --before; simulated in memory on both layers: the "
    r"marker then stands on its own line between '... le morphisme canonique, les' and 'faisceaux $\R^it_*'; the "
    r"anchor survives a font fix of that \R, and a second run, e.g. from batch 316-320, changes nothing). Text not "
    r"moved; the moving text ('suite il résulte immédiatement de (1.1) et (1.2) que, notant $t:B\to S$ le morphisme "
    r"canonique, les') reads as the print.")

# ---------------- checks ----------------
pages = {p: (B / f"page_{p}.tex").read_text(encoding="utf-8") for p in range(311, 316)}
for t in pages.values():
    assert "\r" not in t
ok = True
state = dict(pages)
for i, d in enumerate(F):
    fx = d["fix"]
    for k in ("where", "scan", "tex", "note"):
        if any(ord(c) < 32 and c not in "\n" for c in d[k]):
            print("CONTROL CHAR in", i, k); ok = False
    if fx is None:
        continue
    for k in ("old", "new"):
        if any(ord(c) < 32 and c != "\n" for c in fx[k]):
            print("CONTROL CHAR in fix", i, k); ok = False
    orig = pages[d["page"]]
    c0 = orig.count(fx["old"])
    c1 = state[d["page"]].count(fx["old"])
    if "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]:
        print("MARKER in fix", i); ok = False
    if d["_after"]:
        if c1 != 1:
            print("DEPENDENT old not unique at its turn", i, d["page"], repr(fx["old"]), c1); ok = False
    elif c0 != 1 or c1 != 1:
        print("old not unique", i, d["page"], repr(fx["old"]), "orig", c0, "at its turn", c1); ok = False
    state[d["page"]] = state[d["page"]].replace(fx["old"], fx["new"], 1)
for d in F:
    del d["_after"]
print("checks", "OK" if ok else "FAILED", len(F), "findings")
from collections import Counter
cnt = Counter((d["page"], d["kind"] == "misprint_in_print") for d in F)
for p in range(311, 316):
    print(p, "normal", cnt[(p, False)], "misprint", cnt[(p, True)])
if ok:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    print("written", OUT)
    (RUN / "crops_311_315" / "after_fixes_preview.txt").write_text(
        "\n\n".join(f"===== {p}\n{state[p]}" for p in range(311, 316)), encoding="utf-8", newline="\n")
