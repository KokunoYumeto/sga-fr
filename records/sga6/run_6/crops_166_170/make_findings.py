"""Write findings_166_170.json (SGA 6, pp. 166-170) and check that every fix's old occurs exactly once on its page.
In the strings below the sign ¶ stands for a line break (LF)."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
OUT = RUN / "findings_166_170.json"
NL = "¶"


def fx(old, new):
    return {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}


def em(old):
    """Wrap the whole old text in \\emph{...}."""
    return fx(old, r"\emph{" + old + "}")


F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected.replace(NL, "\n")
    d["note"] = note
    F.append(d)


BLOCK = ("Missing underline of the statement: the TeX sets Exposé II's statements in roman (see the message). "
         "One \\emph over the inner formulas and punctuation (the volume's block decision), as the statements fixed "
         "on pp. 93-100 and 136-144.")

# ---------------------------------------------------------------- p. 166
add(166, "Lemme 2.1.3 a) (ii), after the display: 'est un isomorphisme, et pour tout n >= 1 et tout x ... qui efface x.'",
    "underlined by word groups: 'est un isomorphisme', 'et pour tout', 'et tout', 'il existe un épimorphisme', 'de', "
    "'qui efface'; n >= 1, x ∈ Ext^n_B(φ(L),φ(M)), L' -> L, A and the final 'x.' not (both scans)",
    "no emphasis (roman)", "underline", "high",
    em(r"est un¶isomorphisme, et pour tout $n\ge1$ et tout $x\in\Ext^n_{\mathcal B}(\varphi(L),\varphi(M))$ il existe "
       r"un épimorphisme $L'\to L$ de $\mathcal A$ qui efface"),
    BLOCK + " The lemma begins on p. 165; the final x and full stop stay in roman.")
add(166, "Lemme 2.1.3 b), 'Les conditions suivantes sont équivalentes :'",
    "'Les conditions suivantes sont équivalentes' underlined, the colon not (both scans)",
    "no emphasis", "underline", "high",
    fx(r"Les conditions suivantes sont équivalentes :", r"\emph{Les conditions suivantes sont équivalentes} :"),
    "Part of the statement of Lemme 2.1.3.")
add(166, "Lemme 2.1.3 b) (i), 'pour tous L, M ∈ ob A et tout n ∈ Z, la flèche canonique'",
    "'pour tous', 'et tout', 'la flèche canonique' underlined; the formulas and the comma not (both scans)",
    "no emphasis", "underline", "high",
    em(r"pour tous $L,M\in\Ob\mathcal A$ et tout $n\in\mathbb Z$, la flèche canonique"),
    BLOCK)
add(166, "Lemme 2.1.3 b) (i), after the display: 'est un isomorphisme ;'",
    "'est un isomorphisme' underlined, the semicolon not (both scans)",
    "no emphasis", "underline", "high",
    fx(r"est un isomorphisme ;", r"\emph{est un isomorphisme} ;"),
    "Part of the statement.")
add(166, "Lemme 2.1.3 b) (ii), 'le foncteur canonique (induit par φ)'",
    "'le foncteur canonique' and 'induit par' underlined; the parentheses and φ not (both scans)",
    "no emphasis", "underline", "high",
    fx(r"le foncteur canonique (induit par $\varphi$)", r"\emph{le foncteur canonique} (\emph{induit par} $\varphi$)"),
    "Two groups, so that the emphasis does not open inside the parenthesis and close outside it.")
add(166, "Lemme 2.1.3 b) (ii), after the display: 'est pleinement fidèle ... de φ pour tout i.'",
    "underlined by word groups: 'est pleinement fidèle et a pour image essentielle la sous-catégorie', 'pleine de', "
    "'formée des complexes', 'tels que', 'soit dans l'image essentielle de', 'pour tout'; D^b(B), F, H^i(F), φ and "
    "the final 'i.' not (H not underlined) (both scans)",
    "no emphasis", "underline", "high",
    em(r"est pleinement fidèle et a pour image essentielle la sous-catégorie pleine de $\mathrm D^b(\mathcal B)$ formée "
       r"des complexes $F$ tels que $H^i(F)$ soit dans l'image essentielle de $\varphi$ pour tout"),
    BLOCK + " End of the statement.")
add(166, "proof of 2.1.3 a), the Yoneda sequence 0 -> M -> E_{n-1} -> ... -> E_o -> L -> 0 ;",
    "three typed full stops on the line between the arrows (both scans; crops_166_170/p166_ldots.png)",
    r"E_{n-1}\longrightarrow\cdots\longrightarrow E_0", "symbol", "medium",
    fx(r"E_{n-1}\longrightarrow\cdots\longrightarrow E_0", r"E_{n-1}\longrightarrow\ldots\longrightarrow E_0"),
    r"\cdots sets the dots at mid-height (same kind of fix as pp. 79, 80, 86, 95, 102, 127, 137).")
add(166, "proof of 2.1.3, display 'Ext^n_A(.,M) = F^n'",
    "the empty argument is the typewriter's full stop (both scans; crops_166_170/p166_dots.png)",
    r"\Ext^n_{\mathcal A}(\cdot,M)", "symbol", "low",
    fx(r"(\cdot,M)", r"(.,M)"),
    r"As (P,.) p. 89, (E,.) and (.,I) p. 136, Add(C,.) p. 141 (applied). Same decision as the next entry: both or neither.")
add(166, "same display, 'Ext^n_B(φ(.),φ(M)) = G^n'",
    "φ(.): the typewriter's full stop (both scans; crops_166_170/p166_dots.png)",
    r"\varphi(\cdot)", "symbol", "low",
    fx(r"\varphi(\cdot)", r"\varphi(.)"),
    "As the previous entry: both or neither.")
add(166, "Lemme 2.1.3 and Remarques 2.1.3.1 (pp. 166-167): the abelian categories A and B",
    "plain typed capitals A, B, neither underlined nor double-struck: 'Hom_A(L,M) -> Hom_B(φ(L),φ(M))', 'de A qui "
    "efface x', 'L, M ∈ ob A', 'D^b(A) -> D^b(B)'; p. 167 'si A et B ont assez d'injectifs', 'ob D^-(A)', "
    "'ob D^+(A)' (both scans). The fibred categories of p. 168 are underlined: C̲, C̲_o",
    r"\mathcal A (9 times on p. 166, 3 on p. 167) and \mathcal B (6 and 1); \mathcal C, \mathcal C_0 on p. 168",
    "font", "high", None,
    "Convention, not a page fix: decide with the pending category-letter decision (as the plain C of §§6.1-6.4, "
    "findings_141_145.json).")

# ---------------------------------------------------------------- p. 167
add(167, "start of page",
    "p. 167 begins '0 -> L_1 -> L_o -> L -> 0. D'après ce qu'on a vu plus haut'; p. 166 ends '... la limite "
    "inductive étant prise suivant l'ensemble des suites exactes' (both scans)",
    r"the last line of page_166.tex ends 'des suites exactes $0\to L_1\to L_0\to L\to0$. D'%'; the folio-167 marker "
    "stands after it, before 'après'",
    "marker", "high", None,
    r"Page 167 really begins with '$0\to L_1\to L_0\to L\to0$. D''. Move the folio-167 marker up: "
    r"python -I move_marker.py 6 167 '$0\to L_1\to L_0\to L\to0$' --before (single quotes; simulated on both layers, "
    r"crops_166_170/sim_markers.py: '... l'ensemble des suites exactes ' / marker / '$0\to L_1\to L_0\to L\to0$. "
    r"D'%' / 'après ce qu'on a vu plus haut ...', which still renders 'D'après').")
add(167, "Remarques 2.1.3.1 (iii), display, first member 'R Hom(L,M)'",
    "R with a double underline, the double-struck R of the derived functor; Hom plain (both scans)",
    r"\mathrm R\!\operatorname{Hom}(L,M)", "font", "high",
    fx(r"\mathrm R\!\operatorname{Hom}(L,M)", r"\mathbb R\!\operatorname{Hom}(L,M)"),
    r"Double-struck R written plain (as \mathrm R\Hom -> \mathbb R\Hom on p. 134).")
add(167, "same display, second member 'R Hom(φ(L),φ(M))'",
    "the same double-underlined R (both scans)",
    r"\mathrm R\!\operatorname{Hom}(\varphi(L),\varphi(M))", "font", "high",
    fx(r"\mathrm R\!\operatorname{Hom}(\varphi(L)", r"\mathbb R\!\operatorname{Hom}(\varphi(L)"),
    "As the previous entry.")
add(167, "Proposition 2.2.2, 'Soit S un schéma noethérien. Le foncteur canonique'",
    "'Soit', 'un schéma noethérien', 'Le foncteur canonique' underlined; S and the full stop not (both scans)",
    "no emphasis", "underline", "high",
    em(r"Soit $S$ un schéma noethérien. Le foncteur"),
    BLOCK + " The last word, 'canonique', stands under the folio-168 marker: its \\emph is given on p. 168.")

# ---------------------------------------------------------------- p. 168
add(168, "start of page",
    "p. 168 begins with the display D^-(Coh(S)) -> D(Qcoh(S)); 'canonique' (underlined) is the last word of p. 167, "
    "'Le foncteur canonique' (both scans)",
    "page_168.tex begins 'canonique' (under the folio-168 marker), then the display",
    "marker", "high", None,
    r"Page 168 really begins with the display. Move the folio-168 marker down past 'canonique': "
    r"python -I move_marker.py 6 168 '\[' (no --before: the first \[ after the marker; simulated on both layers with "
    r"the next entry applied: '... Le foncteur' / '\emph{canonique}' / marker / '\[' / display; without that entry "
    r"the same with plain 'canonique').")
add(168, "Proposition 2.2.2, 'canonique' (end of the first statement line, printed on p. 167)",
    "underlined (both scans)",
    "canonique (roman)", "underline", "high",
    fx(r"canonique¶\[¶\mathrm D^{-}", r"\emph{canonique}¶\[¶\mathrm D^{-}"),
    "Continues the p. 167 entry; belongs to p. 167 (marker entry above).")
add(168, "Proposition 2.2.2, after the display: 'est pleinement fidèle et a pour image essentielle'",
    "'est pleinement fidèle et a pour image essentielle' underlined; D^-(Qcoh(S)_coh. not (both scans)",
    "no emphasis", "underline", "high",
    fx(r"est pleinement fidèle et a pour image essentielle $\mathrm D^{-}",
       r"\emph{est pleinement fidèle et a pour image essentielle} $\mathrm D^{-}"),
    "End of the statement. Apply before the misprint entry that follows (no overlap).")
add(168, "Proposition 2.2.2, 'image essentielle D^-(Qcoh(S))_coh'",
    "D^-(Qcoh(S)_coh . : only one closing parenthesis, the one opened after D^- is never closed (both scans; "
    "crops_166_170/p168_dqcoh.png)",
    r"\mathrm D^{-}(\Qcoh(S))_{\coh} (silently corrected)", "misprint_in_print", "high",
    fx(r"(\Qcoh(S))_{\coh}$.", r"(\Qcoh(S)_{\coh}$."),
    "Notation 2.2.1 defines D^-(Qcoh(S))_coh; the typist dropped a parenthesis.",
    corrected=r"(\Qcoh(S))_{\coh}$.")
add(168, "proof of 2.2.2, 'le fait que tous O_S-Module quasi-cohérent est limite inductive'",
    "tous O̲_S-Module quasi-cohérent est (both scans)",
    r"tous $\mathcal O_S$-Module (printed reading kept)", "misprint_in_print", "high", None,
    "Agreement slip (singular Module, est). The TeX keeps the printed reading; the corrected layer already reads "
    "'tout'.",
    corrected=r"tout $\mathcal O_S$-Module")
add(168, "Corollaire 2.2.2.1, 'Soit S un schéma noethérien (resp. ...). Le foncteur canonique'",
    "underlined: 'Soit', 'un schéma noethérien', 'resp', 'noethérien et de dimension finie', 'Le foncteur canonique'; "
    "S, the parentheses and the full stops not (both scans)",
    "no emphasis", "underline", "high",
    em(r"Soit $S$ un schéma noethérien (resp. noethérien et de dimension finie). Le foncteur canonique"),
    BLOCK)
add(168, "Corollaire 2.2.2.1, after the displays: 'est pleinement fidèle et a pour image essentielle'",
    "'est pleinement fidèle et a pour image essentielle' underlined; D^b(S)_coh (resp. D^-(S)_coh) (I 2.15). not "
    "(both scans)",
    "no emphasis", "underline", "high",
    fx(r"est pleinement fidèle et a pour image essentielle $\mathrm D^b",
       r"\emph{est pleinement fidèle et a pour image essentielle} $\mathrm D^b"),
    "End of the statement.")
add(168, "Proposition 2.2.3, statement before the items: 'Soit S un schéma ... Les conditions suivantes sont équivalentes :'",
    "underlined by word groups from 'Soit' to 'Les conditions suivantes sont équivalentes' ('un schéma quasi-compact "
    "et quasi-séparé', 'et soit', 'une famille de faisceaux inversibles sur', 'Pour tout', '-Module', 'et tout "
    "couple', 'on note', 'le sous-', '-Module de', 'engendré par les sections de', 'au-dessus de'); S, the "
    "formulas, the full stops and the colon not; O̲_S with their own underlines (both scans)",
    "no emphasis (the reference '(cf. EGA II 4.5.2 et 4.5.5).' is rightly roman)", "underline", "high",
    em(r"Soit $S$ un schéma quasi-compact et quasi-séparé, et soit $(L_i)_{i\in I}$ une famille de faisceaux "
       r"inversibles sur $S$. Pour tout $\mathcal O_S$-Module $F$, et tout couple $(i,n)\in I\times\mathbb Z$, on note "
       r"$F_{(i,n)}$ le sous-$\mathcal O_S$-Module de $F\otimes L_i^{\otimes n}$ engendré par les sections de "
       r"$F\otimes L_i^{\otimes n}$ au-dessus de $S$. Les conditions suivantes sont équivalentes"),
    BLOCK + " The items (i)-(iii') follow on p. 169.")

# ---------------------------------------------------------------- p. 169
add(169, "Proposition 2.2.3 (i)",
    "'Les ouverts', 'pour', 'et', 'forment une base de la topologie de' underlined; S_f, the formulas and 'S.' not "
    "(both scans)",
    "no emphasis", "underline", "high",
    em(r"Les¶ouverts $S_f$, pour $f\in\Gamma(S,L_i^{\otimes n})$, $i\in I$ et $n\in\mathbb N$, forment une base de la "
       r"topologie de"),
    BLOCK)
add(169, "Proposition 2.2.3 (i')",
    "'Ceux des', 'qui sont affines recouvrent' underlined; S_f and 'S.' not (both scans)",
    "no emphasis", "underline", "high",
    em(r"Ceux des $S_f$ qui sont affines recouvrent"),
    BLOCK)
add(169, "Proposition 2.2.3 (ii)",
    "underlined: 'Pour tout', '-Module', 'quasi-cohérent et de type fini', 'il existe une famille', 'd'entiers', 'et un "
    "épimorphisme'; F, the families, '>= 0 (resp. > 0),' not (both scans)",
    "no emphasis", "underline", "high",
    em(r"Pour tout $\mathcal O_S$-Module $F$ quasi-cohérent et de type fini, il existe une famille $(r_i)_{i\in I}$ "
       r"(resp. $(n_i)_{i\in I}$) d'entiers $\ge0$ (resp. $>0$), et un épimorphisme"),
    BLOCK)
add(169, "Proposition 2.2.3 (iii), 'Pour tout F ∈ ob Qcoh(S), on a'",
    "'Pour tout' and 'on a' underlined (both scans)",
    "no emphasis", "underline", "high",
    em(r"Pour tout $F\in\Ob\Qcoh(S)$, on a"),
    BLOCK)
add(169, "Proposition 2.2.3 (iii), after the display: '(somme (non directe) de sous-faisceaux de F).'",
    "'somme', 'non directe', 'de sous-faisceaux de' underlined; the parentheses, F and the full stop not (both scans)",
    "no emphasis", "underline", "high",
    fx(r"(somme (non directe) de sous-faisceaux de", r"(\emph{somme (non directe) de sous-faisceaux de}"),
    BLOCK)
add(169, "Proposition 2.2.3 (iii')",
    "'Même condition que', 'mais', 'étant un Idéal quasi-cohérent de' underlined; '(iii),', F and O̲_S not (both scans)",
    "no emphasis", "underline", "high",
    em(r"Même condition que (iii), mais $F$ étant un Idéal quasi-cohérent de"),
    BLOCK + " Apply before the misprint entry that follows (no overlap).")
add(169, "Proposition 2.2.3 (iii'), end: '... quasi-cohérent de O_S'",
    "no full stop after O̲_S, which ends the line and the item (both scans; crops_166_170/p169_iiiprime.png, "
    "w169_os.png)",
    r"$\mathcal O_S$. (silently corrected)", "misprint_in_print", "medium",
    fx(r"$\mathcal O_S$.", r"$\mathcal O_S$"),
    "The other items end with a full stop; the typist left it out here. The TeX supplies it.",
    corrected=r"$\mathcal O_S$.")
add(169, "Lemme 2.2.3.1 statement",
    "underlined: 'Soient', 'un schéma', 'un', '-Module inversible', 'L'immersion canonique', 'est affine'; X, L, "
    "'f ∈ Γ(X,L).', 'i : X_f -> X' and the final full stop not (both scans)",
    "no emphasis", "underline", "high",
    em(r"Soient $X$ un schéma, $L$ un $\mathcal O_X$-Module inversible $f\in\Gamma(X,L)$. L'immersion canonique "
       r"$i:X_f\to X$ est affine"),
    BLOCK)
add(169, "Lemme 2.2.3.1, 'L un O_X-Module inversible f ∈ Γ(X,L)'",
    "no comma between 'inversible' and 'f ∈ Γ(X,L)' (both scans)",
    r"inversible $f\in\Gamma(X,L)$ (printed reading kept)", "misprint_in_print", "low", None,
    "The third item of the 'Soient' list runs on without a comma; the corrected layer has none either: decide whether "
    "the corrected edition adds it.",
    corrected=r"inversible, $f\in\Gamma(X,L)$")

# ---------------------------------------------------------------- p. 170
add(170, "start of page",
    "p. 170 begins 'F | S_{f_ij} est engendré par un nombre fini de sections'; p. 169 ends '... égaux à un entier "
    "m_i. Le faisceau' (both scans)",
    r"page_169.tex ends '... Le faisceau $F\,|\,S_{f_{ij}}$ est' (under the folio-169 marker); page_170.tex begins "
    "'engendré par'",
    "marker", "high", None,
    r"Page 170 really begins with '$F\,|\,S_{f_{ij}}$ est'. Move the folio-170 marker up: python -I move_marker.py 6 "
    r"170 '$F\,|\,S_{f_{ij}}$ est' --before (single quotes; simulated on both layers, crops_166_170/sim_markers.py: "
    r"'... un entier $m_i$. Le faisceau ' / marker / '$F\,|\,S_{f_{ij}}$ est' / 'engendré par ...').")
add(170, "(ii) => (iii), '(EGA I 9.4.9 et IV 1.7.7), on peut se borner'",
    "a comma right after the parenthesis (witness: a clean comma; main scan: a comma with a faint speck above it, far "
    "smaller than a semicolon's dot; crops_166_170/w170_semicolon.png, p170_semicolon_zoom.png)",
    "IV 1.7.7) ; on peut", "punctuation", "medium",
    fx(r"IV 1.7.7) ; on peut", r"IV 1.7.7), on peut"),
    "The typist sets a semicolon with a space before it (p. 169 '(loc. cit.) ;', ') ; posons'); here the mark follows "
    "the parenthesis directly, and the 'Comme ...' clause takes a comma. The corrected layer has the same ' ;'.")
add(170, "display Im(u_i) = ..., end of the second line",
    "no punctuation after '= Im(u_i ⊗ Id(L_i^{⊗n_i})) ⊗ L_i^{⊗-n_i}' (both scans; crops_166_170/p170_im.png)",
    r"\otimes L_i^{\otimes-n_i}.", "punctuation", "high",
    fx(r"\bigr)\otimes L_i^{\otimes-n_i}.", r"\bigr)\otimes L_i^{\otimes-n_i}"),
    "The TeX adds a full stop at the end of the display.")

# ---------------------------------------------------------------- write and check
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
bad = 0
for d in F:
    if not d["fix"]:
        continue
    t = (RUN / "b166_170" / f"page_{d['page']}.tex").read_text(encoding="utf-8")
    body = t.split("\n", 2)[2]  # after '% from main.tex' and the marker line
    n = t.count(d["fix"]["old"])
    if n != 1 or body.count(d["fix"]["old"]) != 1 or "%%%%%%%%%%" in d["fix"]["old"] or "%%%%%%%%%%" in d["fix"]["new"]:
        bad += 1
        print("NOT UNIQUE / BAD:", d["page"], n, repr(d["fix"]["old"][:80]))
counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0])
    c[1 if d["kind"] == "misprint_in_print" else 0] += 1
print("written", OUT, len(F), "findings;", "bad:", bad)
print(" ".join(f"p{p} {a}/{b}" for p, (a, b) in sorted(counts.items())))
