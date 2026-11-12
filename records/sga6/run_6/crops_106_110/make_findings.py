"""Write findings_106_110.json for SGA 6 pp. 106-110 and check every fix's old against its page file
(exactly one occurrence in the original page, and still exactly one when the fixes are applied in list order)."""
import json
import pathlib

here = pathlib.Path(__file__).resolve().parent
RUN = here.parent
B = RUN / "b106_110"

F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def fx(old, new):
    return {"old": old, "new": new}


# ---------------------------------------------------------------- p. 106
add(106, "line 2, '(2.10.b)) F'_{≤n} ) (resp. F\"_{≤n}) est n-pseudo-cohérent'",
    "a closing parenthesis after F'_{≤n} that closes nothing: '(2.10.b)) F'_{≤n} ) (resp. F\"_{≤n})' "
    "(both scans; crops_106_110/p106_paren.png)",
    r"(2.10.b)) \(F'_{\leq n}\) (resp.",
    "misprint_in_print", "high",
    fx(r"(2.10.b)) \(F'_{\leq n}\) (resp.", r"(2.10.b)) \(F'_{\leq n}\)) (resp."),
    "Stray parenthesis of the typescript ('(2.10.b))' already closes the reference); the TeX silently drops it.",
    corrected=r"(2.10.b)) \(F'_{\leq n}\) (resp.")

P1A = (r"Soit \((S',\mathcal C',\mathcal C'_0)\) un trio satisfaisant aux mêmes hypothèses (2.0) que "
       r"\((S,\mathcal C,\mathcal C_0)\). Soit \(f:S'\to S\) un morphisme de sites ([G] I 1.4), correspondant à un "
       r"foncteur sous-jacent \(f^{-1}:S\to S'\), et soit")
add(106, "Proposition 2.13, statement, 'Soit (S',C',C'_o) un trio ... correspondant à un foncteur sous-jacent "
         "f^{-1} : S → S', et soit'",
    "underlined by word groups: 'Soit', 'un trio satisfaisant aux mêmes hypothèses', 'que', 'Soit', 'un morphisme "
    "de sites', 'correspondant à un foncteur sous-jacent', 'et soit' (both scans)",
    "no emphasis: the whole statement of Proposition 2.13 is in roman (Proposition 2.12 and Corollaire 2.14 have "
    "\\emph)",
    "underline", "high",
    fx(P1A, r"\emph{" + P1A + "}"),
    "First group of the statement (block \\emph, the volume decision). The formula 'u : D*(C) → D*(C') "
    "(* = +,-,∅)' that follows is not underlined; the next group begins at 'un foncteur cartésien'. Independent of "
    "the display and ∅ entries below.")

P1B = (r"un foncteur cartésien au-dessus de \(f\), i.e. un \(S\)-foncteur cartésien "
       r"\(\Dpx^*(\mathcal C')\times_{S'}S\longleftarrow\Dpx^*(\mathcal C)\). On suppose que \(u\) est exact sur "
       r"chaque fibre et qu'il existe \(a,b\in\mathbb Z\) tels que les conditions suivantes soient vérifiées pour "
       r"tout \(S\in\Ob S\)")
add(106, "Proposition 2.13, statement, 'un foncteur cartésien au-dessus de f, i.e. ... soient vérifiées pour tout "
         "S ∈ ob S :'",
    "underlined by word groups: 'un foncteur cartésien au-dessus de', 'un', 'S-foncteur cartésien', 'On suppose "
    "que', 'est exact', 'sur chaque fibre et qu'il existe', 'tels que les conditions suivantes', 'soient vérifiées "
    "pour tout'; the colon is not (both scans)",
    "no emphasis",
    "underline", "high",
    fx(P1B, r"\emph{" + P1B + "}"),
    "Second group of the opening paragraph; the colon stays outside, as in Proposition 2.7 ('Alors} :').")

DISP = "\\[\n  u:\\Dpx^*(\\mathcal C)\\longrightarrow \\Dpx^*(\\mathcal C')\\qquad (*=+,-,b)\n\\]"
add(106, "Proposition 2.13, 'et soit u : D*(C) → D*(C') (* = +,-,∅) un foncteur cartésien'",
    "the formula stands at the left margin as the start of a text line, which goes on 'un foncteur cartésien "
    "au-dessus de f, i.e.' (both scans): it is part of the sentence, not a display",
    "a display \\[ u:\\Dpx^*(\\mathcal C)\\longrightarrow \\Dpx^*(\\mathcal C')\\qquad (*=+,-,b) \\]",
    "other", "medium",
    fx(DISP, r"\(u:\Dpx^*(\mathcal C)\longrightarrow \Dpx^*(\mathcal C')\) \((*=+,-,b)\)"),
    "The print sets the formula inline; the TeX makes it a display (same kind of fix as pp. 21, 34, 42, 80). "
    "Apply before the ∅ entry below (this old contains (*=+,-,b); JSON order).")

add(106, "Proposition 2.13, '(* = +,-,∅)'",
    "the third value is the typed empty-set sign, an o crossed by a long slash, with no upright stem (both scans; "
    "crops_106_110/p106_b.png, w106_b.png); the typed b of '(* = +, -, b)' on p. 85 has its upright stem "
    "(crops_106_110/p085_b_compare.png); the same sign as K^{-,∅} on p. 100",
    r"(*=+,-,b)",
    "symbol", "high",
    fx(r"(*=+,-,b)", r"(*=+,-,\varnothing)"),
    "\\varnothing is the file's form of this sign (p. 100). After the display entry above, or alone.")

I1 = (r"si \(E\in\Ob\mathcal C_{0,S}\), \(u(E)\) est \(a\)-\(\mathcal C'_0\)-pseudo-cohérent (resp. "
      r"\(\mathcal C'_0\)-pseudo-cohérent)")
add(106, "Proposition 2.13 (i)",
    "underlined: 'si', 'est', '-pseudo-cohérent', 'resp.', '-pseudo-cohérent'; the label (i) is not (both scans)",
    "no emphasis",
    "underline", "high",
    fx(I1, r"\emph{" + I1 + "}"),
    "Apply before the C_{0S} entry below (this old contains \\mathcal C_{0,S}; JSON order).")

add(106, "Proposition 2.13 (i), 'si E ∈ ob C_oS , u(E)'",
    "C̲ with the indices o and S side by side, no comma (both scans; crops_106_110/p106_C0S.png)",
    r"\mathcal C_{0,S}",
    "punctuation", "high",
    fx(r"\Ob\mathcal C_{0,S}", r"\Ob\mathcal C_{0S}"),
    "The TeX adds a comma between the indices (as fixed on pp. 85-100).")

add(106, "Proposition 2.13, end of (i), '(resp. C'_o-pseudo-cohérent)'",
    "no punctuation after the closing parenthesis (both scans; crops_106_110/p106_i_end.png)",
    r"(resp. \(\mathcal C'_0\)-pseudo-cohérent);",
    "punctuation", "high",
    fx(";\n\n(ii)", "\n\n(ii)"),
    "The TeX adds a semicolon at the end of item (i). Independent of the (i) and (ii) underline entries.")

I2 = r"si \(F\in\Ob\Dpx^*(\mathcal C_S)\) est acyclique en degré \(>0\), \(u(F)\) est acyclique en degré \(>b\)."
add(106, "Proposition 2.13 (ii)",
    "underlined: 'si', 'est acyclique en degré', 'est acyclique en', 'degré'; the label (ii) is not (both scans)",
    "no emphasis",
    "underline", "high",
    fx(I2, r"\emph{" + I2 + "}"),
    "")

AL = (r"Alors, si \(F\in\Ob\Dpx^*(\mathcal C_S)\) est \(m\)-pseudo-cohérent rel. à \(\mathcal C_0\) et acyclique en "
      r"degré \(>n\), \(u(F)\in\Ob\Dpx^*(\mathcal C'_{S'})\) (où \(S'=f^{-1}(S)\)) est \(\sup(m+b,n+a)\)-pseudo-cohérent "
      r"(rel. à \(\mathcal C'_0\)) (resp. \((m+b)\)-pseudo-cohérent) et acyclique en degré \(>n+b\).")
add(106, "Proposition 2.13, 'Alors, si F ∈ ob D*(C_S) est m-pseudo-cohérent ... et acyclique en degré > n+b.'",
    "underlined by word groups: 'Alors,', 'si', 'est m-pseudo-cohérent rel.', 'et acyclique', 'en degré', 'où', "
    "'est', 'pseudo-', 'cohérent', 'rel.', 'resp', 'pseudo-cohérent', 'et acyclique en degré' (both scans)",
    "no emphasis",
    "underline", "high",
    fx(AL, r"\emph{" + AL + "}"),
    "")

EP = (r"En particulier, dans le cas respé, si \(F\in\Ob\Dpx^*(\mathcal C_S)\) est pseudo-cohérent (rel. à "
      r"\(\mathcal C_0\)), \(u(F)\) est pseudo-cohérent (rel. à \(\mathcal C'_0\)).")
EPN = (r"\emph{En particulier, dans le cas respé, si \(F\in\Ob\Dpx^*(\mathcal C_S)\) est pseudo-cohérent} (rel. à "
       r"\(\mathcal C_0\)), \emph{\(u(F)\) est pseudo-cohérent (rel. à \(\mathcal C'_0\)).}")
add(106, "Proposition 2.13, 'En particulier, dans le cas respé, ... (rel. à C'_o).'",
    "underlined: 'En particulier,', 'dans le cas respé,', 'si', 'est pseudo-', 'cohérent', 'est pseudo-cohérent', "
    "'rel.', 'à'; the parenthesis '(rel. à C_o),' after the first 'pseudo-cohérent' is not underlined (both "
    "scans)",
    "no emphasis",
    "underline", "high",
    fx(EP, EPN),
    "The word group '(rel. à C_o),' that the typist left out of the underline stays outside the emphasis (as "
    "'(à isomorphisme près)', p. 43); the final '(rel. à C'_o)' is underlined.")

add(106, "Preuve, 'Montrons d'abord que si F ∈ ob D*(C_S) est strictement parfait'",
    "no comma after 'que' (both scans)",
    r"Montrons d'abord que, si",
    "punctuation", "high",
    fx(r"d'abord que, si", r"d'abord que si"),
    "The TeX adds a comma.")

add(106, "pp. 106-110 throughout: the site S̲",
    "S underlined where it names the site, plain where it names the object S: p. 106 'pour tout S ∈ ob S̲', "
    "'f : S̲' → S̲'; p. 108 'Soient S ∈ ob S̲'; p. 109 'On notera S l'objet final de S̲'; p. 110 's : S̲ → M_n' "
    "(both scans)",
    r"plain \(S\): '\(S\in\Ob S\)', '\(f:S'\to S\)', 'On notera \(S\) l'objet final de \(S\)', "
    r"'\(s:S\longrightarrow M_n\)'",
    "underline", "high", None,
    "Convention of the transcription, as reported for pp. 84-100: one decision for the exposé, not a page fix.")

# ---------------------------------------------------------------- p. 107
add(107, "start of page",
    "p. 107 begins 'on a F = F^p[-p] pour un p ≤ n, donc u(F) est (p+a)-C'_o-pseudo-cohérent'; p. 106 ends "
    "'... tels que F^i ≠ 0. Si N = 1,' (both scans)",
    r"'on a \(F=F^p[-p]\)' ends the last line of page_106.tex (under the folio-106 marker); page_107.tex begins "
    r"'pour un \(p\leq n\)'",
    "marker", "high", None,
    "Page 107 really begins with 'on a \\(F=F^p[-p]\\)'. python -I move_marker.py 6 107 'on a \\(F=F^p[-p]\\)' "
    "--before (single quotes; the only occurrence; simulated on both layers: '... Si \\(N=1\\), ', the marker, "
    "'on a \\(F=F^p[-p]\\)', 'pour un \\(p\\leq n\\), ...', which still renders 'Si N = 1, on a F = F^p[-p] pour "
    "un').")

add(107, "first triangle (u(F') → u(F) → u(F\") --+1--> u(F')), end",
    "a comma to the right of the triangle, on the line of u(F) (both scans)",
    "tikzcd without punctuation",
    "punctuation", "high",
    fx("u(F) \\arrow[ul]\n\\end{tikzcd}\n\\]\non déduit", "u(F) \\arrow[ul] & ,\n\\end{tikzcd}\n\\]\non déduit"),
    "Set in a cell of its own, as on pp. 93-99.")

add(107, "second triangle, end",
    "a comma to the right of the triangle, on the line of u(F) (both scans)",
    "tikzcd without punctuation",
    "punctuation", "high",
    fx("u(F) \\arrow[ul]\n\\end{tikzcd}\n\\]\n\\(u(F'')\\)", "u(F) \\arrow[ul] & ,\n\\end{tikzcd}\n\\]\n\\(u(F'')\\)"),
    "As the first triangle.")

add(107, "Corollaire 2.14, end of the opening: 'Alors :' (printed at the top of p. 108)",
    "'Alors' underlined, the colon not (p. 108, first line; both scans)",
    r"\emph{Soit ... est \(\mathcal C_0\)-pseudo-cohérent. Alors :}",
    "underline", "medium",
    fx(r"pseudo-cohérent. Alors :}", "pseudo-cohérent.}\n\\emph{Alors} :"),
    "Closes the statement's group after 'pseudo-cohérent.' and gives 'Alors' a group of its own (prints the same, "
    "the colon now upright as printed), so that the folio-108 marker can stand between the two groups (marker "
    "entry of p. 108). Given here, where the text stands now.")

# ---------------------------------------------------------------- p. 108
add(108, "start of page",
    "p. 108 begins 'Alors :' (Corollaire 2.14), then '(i) C_1 est localement quasi-relevable dans C'; p. 107 ends "
    "'... On suppose que tout objet de C_1 est C_o-pseudo-cohérent.' (both scans)",
    r"'Alors :}' ends the last line of page_107.tex (under the folio-107 marker); page_108.tex begins "
    r"'\emph{(i) \(\mathcal C_1\)'",
    "marker", "high", None,
    "Page 108 really begins with 'Alors :'. After the p. 107 entry that splits the group ('pseudo-cohérent.}' / "
    "'\\emph{Alors} :'): python -I move_marker.py 6 108 '\\emph{Alors} :' --before (simulated on both layers: "
    "'... \\(\\mathcal C_0\\)-pseudo-cohérent.}', the marker, '\\emph{Alors} :', blank line, '\\emph{(i) ...'). "
    "Without that edit: python -I move_marker.py 6 108 'Alors :}' --before (the marker then stands inside the "
    "\\emph group; it compiles).")

add(108, "Corollaire 2.14 (i), label",
    "the label (i) is not underlined; the underline begins at 'est localement' (both scans)",
    r"\emph{(i) \(\mathcal C_1\) est ...}",
    "underline", "medium",
    fx(r"\emph{(i) \(\mathcal C_1\)", r"(i) \emph{\(\mathcal C_1\)"),
    "The TeX sets the item label in italics inside the statement's \\emph; the file's other items keep the label "
    "outside ('a) \\emph{...}', p. 100). Same on p. 109 (Lemme 2.15.1).")

add(108, "Corollaire 2.14 (ii), label",
    "the label (ii) is not underlined; the underline begins at 'Soient' (both scans)",
    r"\emph{(ii) Soient ...}",
    "underline", "medium",
    fx(r"\emph{(ii) Soient", r"(ii) \emph{Soient"),
    "As (i).")

add(108, "Preuve (i), 'avec F ∈ ob C_1S . Comme F est'",
    "C̲ with the indices 1 and S side by side, no comma (both scans; crops_106_110/p108_CS.png)",
    r"\mathcal C_{1,S}",
    "punctuation", "high",
    fx(r"\Ob\mathcal C_{1,S}", r"\Ob\mathcal C_{1S}"),
    "The TeX adds a comma between the indices (as fixed on pp. 85-100).")

add(108, "Preuve (i), 'avec E' ∈ ob C_oS . Utilisant'",
    "C̲ with the indices o and S side by side, no comma (both scans; crops_106_110/p108_C0S.png)",
    r"\mathcal C_{0,S}",
    "punctuation", "high",
    fx(r"\Ob\mathcal C_{0,S}", r"\Ob\mathcal C_{0S}"),
    "As above.")

add(108, "Preuve (ii), '... C'_o et C_o remplacées respectivement par C_o et C_1).'",
    "a closing parenthesis after C_1 with no opening one: '(2.11.a)) ou (2.13) avec S' = S, ..., remplacées "
    "respectivement par C_o et C_1).' (both scans)",
    r"remplacées respectivement par \(\mathcal C_0\) et \(\mathcal C_1\)). (printed reading kept)",
    "misprint_in_print", "medium", None,
    "The parenthesis closes nothing ('(2.13)' is closed); either the stray ')' or a missing '(' before 'avec'. "
    "The TeX keeps the printed reading. Corrected reading given as the smaller change; '(2.13) (avec \\(S'=S\\), "
    "...' would serve as well.",
    corrected=r"remplacées respectivement par \(\mathcal C_0\) et \(\mathcal C_1\).")

# ---------------------------------------------------------------- p. 109
add(109, "Exemple 2.15, 'Un objet de D(S̲) sera dit n-pseudo-cohérent (resp. pseudo-cohérent)'",
    "the defined terms 'n-pseudo-cohérent' and 'pseudo-cohérent' are underlined, '(resp.' is not (both scans)",
    r"sera dit \(n\)-pseudo-cohérent (resp. pseudo-cohérent), in roman",
    "underline", "high",
    fx(r"sera dit \(n\)-pseudo-cohérent (resp. pseudo-cohérent)",
       r"sera dit \emph{\(n\)-pseudo-cohérent} (resp. \emph{pseudo-cohérent})"),
    "")

SUB = (r"\(\Dpx(\mathcal C)_{n-\mathcal C_0-\coh}\) (resp. \(\Dpx(\mathcal C)_{\mathcal C_0-\coh}\)) (2.6) sera "
       r"notée \(\Dpx({}_A S)_{n-\coh}\)")
SUBN = (r"\(\Dpx(\mathcal C)_{n\text{-}\mathcal C_0\text{-}\coh}\) (resp. \(\Dpx(\mathcal C)_{\mathcal C_0\text{-}\coh}\)) "
        r"(2.6) sera notée \(\Dpx({}_A S)_{n\text{-}\coh}\)")
add(109, "Exemple 2.15, 'D(C)_{n-C_o-coh} (resp. D(C)_{C_o-coh}) (2.6) sera notée D(_A S̲)_{n-coh}'",
    "the hyphens of the compound indices n-C_o-coh, C_o-coh, n-coh (the typed hyphen of 'n-pseudo-cohérent')",
    r"math-mode '-' in the subscripts: _{n-\mathcal C_0-\coh}, _{\mathcal C_0-\coh}, _{n-\coh}",
    "symbol", "medium",
    fx(SUB, SUBN),
    "In math mode the hyphens print as minus signs with operator spacing (n − C_0 − coh); the file writes the same "
    "notation with \\text{-} on p. 100 ('\\Dpx(\\mathcal C)_{\\mathcal C_0\\text{-}n\\text{-coh}}'). These are the "
    "only three '-\\coh' of main.tex.")

add(109, "Lemme 2.15.1 (i), label",
    "the label (i) is not underlined (both scans)",
    r"\emph{(i) \(S\) « a assez de points » ...}",
    "underline", "medium",
    fx(r"\emph{(i) \(S\) «", r"(i) \emph{\(S\) «"),
    "As Corollaire 2.14 (i), p. 108.")

add(109, "Lemme 2.15.1 (i), 'les A_s-modules (à gauche) projectifs de type fini'",
    "'(à gauche)' is not underlined, while '-modules' before it and 'projectifs de type fini sont libres' after "
    "it are (both scans)",
    r"inside the \emph of (i)",
    "underline", "medium",
    fx(r"\(A_s\)-modules (à gauche) projectifs", r"\(A_s\)-modules} (à gauche) \emph{projectifs"),
    "A parenthetical word group the typist left out of the underline (as '(à isomorphisme près)', p. 43); in the "
    "conclusion of the lemma ('d'un A-module (à gauche) libre') the same words are underlined. Independent of the "
    "label entry.")

add(109, "Lemme 2.15.1 (ii), label",
    "the label (ii) is not underlined (both scans)",
    r"\emph{(ii) \((S,A)\) est un topos ...}",
    "underline", "medium",
    fx(r"\emph{(ii) \((S,A)\)", r"(ii) \emph{\((S,A)\)"),
    "As (i).")

# ---------------------------------------------------------------- p. 110
add(110, "display at the top of the page, 'Hom̲(E,F)_s → Hom(E_s,F_s)'",
    "the first Hom is underlined (Hom̲, the sheaf Hom), the second is not (both scans)",
    r"\Hom(E,F)_s\longrightarrow\Hom(E_s,F_s)",
    "underline", "high",
    fx(r"\Hom(E,F)_s", r"\underline{\Hom}(E,F)_s"),
    "\\underline{\\Hom} is the file's form (7 times).")

add(110, "'et si E_s ≃ F_s en un point s de S̲'",
    "≃: a tilde over a single stroke, no arrowhead (both scans; crops_106_110/p110_qis1.png)",
    r"\(E_s\qis F_s\) (\qis = \xrightarrow{\sim}, an arrow)",
    "symbol", "high",
    fx(r"\(E_s\qis F_s\)", r"\(E_s\simeq F_s\)"),
    "")

add(110, "'tel que E|U ≃ F|U'",
    "≃ without arrowhead, as above (both scans; crops_106_110/p110_qis2.png)",
    r"\(E|U\qis F|U\)",
    "symbol", "high",
    fx(r"\(E|U\qis F|U\)", r"\(E|U\simeq F|U\)"),
    "")

add(110, "'Supposons (ii), Soit n ∈ ℕ'",
    "a comma after '(ii)' (tailed, both scans; crops_106_110/p110_ii.png), then capital S",
    r"Supposons (ii). Soit",
    "misprint_in_print", "high",
    fx(r"Supposons (ii). Soit", r"Supposons (ii), Soit"),
    "The capital S shows that a full stop was meant (cf. 'Supposons (i). On remarque', p. 109); the TeX silently "
    "corrects it.",
    corrected=r"Supposons (ii). Soit")

add(110, "'le foncteur End̲_𝔻(𝔻^n)'",
    "End underlined (End̲), the index 𝔻 not (both scans; crops_106_110/p110_End.png)",
    r"\End_{\mathbb D}(\mathbb D^n)",
    "underline", "high",
    fx(r"\End_{\mathbb D}", r"\underline{\End}_{\mathbb D}"),
    "The internal End, written like Hom̲ at the top of the page.")

add(110, "'muni de l'endomorphisme U_n de (O_{M_n})^n'",
    "capital U_n (both scans), while the same endomorphism is u_n three times below: 's^*(u_n) = p', "
    "'p = s'^* i^*(u_n)', 'l'image de i^*(u_n)'",
    r"l'endomorphisme \(U_n\) (printed reading kept)",
    "misprint_in_print", "low", None,
    "The universal endomorphism is named u_n everywhere else. The TeX keeps the printed reading.",
    corrected=r"l'endomorphisme \(u_n\)")

add(110, "'le sous-schéma fermé i : P_n → M_n'",
    "a plain arrow, no hook (both scans; crops_106_110/p110_soit.png)",
    r"\(i:P_n\hookrightarrow M_n\)",
    "symbol", "high",
    fx(r"\(i:P_n\hookrightarrow M_n\)", r"\(i:P_n\to M_n\)"),
    "")

add(110, "'correspondant aux projecteurs en S̲ --s'--> P_n --i--> M_n.'",
    "'... aux projecteurs en S̲ --s'--> P_n --i--> M_n. On a donc' ('se factorise ... en S → P_n → M_n'): one S, "
    "no comma and no 'soit' (both scans; crops_106_110/p110_soit.png)",
    r"aux projecteurs en \(S\), soit \(S\xrightarrow{s'}P_n\xrightarrow{i}M_n\).",
    "extra", "high",
    fx(r"aux projecteurs en \(S\), soit \(S\xrightarrow{s'}", r"aux projecteurs en \(S\xrightarrow{s'}"),
    "The TeX adds ', soit' and a second S.")

C216 = (r"Soit \(f:(S',A')\to(S,A)\) un morphisme de topos annelés (défini par un foncteur \(f^{-1}:S\to S'\) et un "
        r"morphisme de faisceaux d'anneaux \(f^{-1}(A)\to A'\)). Notons \(\Dpx({}_{A'}S'_A)\) la catégorie dérivée "
        r"de celle des \(A'\)-\(A\)-biModules (à gauche sur \(A'\), à droite sur \(A\)), et")
add(110, "Corollaire 2.16, statement before the display",
    "underlined by word groups: 'Soit', 'un morphisme de topos annelés', 'défini par un foncteur', 'et un morphisme "
    "de faisceaux d'anneaux', 'Notons', 'la catégorie dérivée de celle des', 'biModules', 'à gauche sur', 'à droite "
    "sur', 'et' (both scans)",
    "no emphasis: the statement is in roman",
    "underline", "high",
    fx(C216, r"\emph{" + C216 + "}"),
    "The display ⊗^L_A : ... is not underlined; the statement goes on on p. 111.")

# ---------------------------------------------------------------- checks
pages = {p: (B / f"page_{p:03d}.tex").read_text(encoding="utf-8") for p in range(106, 111)}
cur = dict(pages)
for x in F:
    f = x["fix"]
    if not f:
        continue
    p = x["page"]
    n0 = pages[p].count(f["old"])
    n1 = cur[p].count(f["old"])
    assert n0 == 1, (p, "original", n0, f["old"][:60])
    assert n1 == 1, (p, "in order", n1, f["old"][:60])
    assert "%%%%%%%%%%" not in f["old"]
    cur[p] = cur[p].replace(f["old"], f["new"])
for p in cur:
    (here / f"applied_{p}.tex").write_text(cur[p], encoding="utf-8", newline="")
out = RUN / "findings_106_110.json"
out.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
from collections import Counter
c = Counter((x["page"], x["kind"] == "misprint_in_print") for x in F)
for p in range(106, 111):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
print("wrote", out, len(F))
