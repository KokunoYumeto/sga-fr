"""Build findings_401_405.json and verify every fix (read-only on the .tex files).
In the raw strings below the character ¶ stands for a line break (LF)."""
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = "C:/Users/user/Documents/sga_scan_check_20261105/run_5"
OUT = RUN + "/findings_401_405.json"
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
L = []


def nl(s):
    return None if s is None else s.replace("¶", "\n")


def F(page, where, scan, tex, kind, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": nl(old), "new": nl(new)}}
    if kind == "misprint_in_print":
        d["corrected"] = nl(corrected)
    d["note"] = note
    L.append(d)


UL_X = "Exposé X has no underline markup in the TeX; \\emph is this file's command for the print's underline (as for the statements of pp. 374-390). Formulas, numbers and the punctuation between the pieces are not underlined in the print."
PLAIN_R = "\\RG = \\R\\Gamma and \\R = \\mathbb{R} in Exposé X, so the TeX prints a double-struck R; the print's R is a plain typewriter R here (one stem, serifs)."
BANG = "The print sets the '!' after the R and before Γ (R_!Γ_V); the TeX's \\RG_{!V} moves it into the index of Γ (ℝΓ_{!V})."
P405 = " Printed at the top of p. 405; in page_404.tex as the files stand (the old stays unique on p. 405 after the folio-405 marker move)."

# ------------------------------------------------------------------ p. 401
F(401, "Corollaire 7.9, statement before (7.10)",
  "underlined: 'sont des complexes de faisceaux satisfaisant', 'aux conditions de', 'et s'ils sont localement isomorphes', 'pour la topo-/logie étale' (not the parentheses), 'comme complexes de', 'modules, on a'; not underlined: 'Si F , F'', '7.1', 'A-', the colon",
  "no underline markup (statement environment, upright text)", "underline", "high",
  r"Si $F$, $F'$ sont des complexes de faisceaux satisfaisant aux conditions de 7.1 et s'ils sont localement isomorphes (pour la topologie étale) comme complexes de $A$-modules, on a:",
  r"Si $F$, $F'$ \emph{sont des complexes de faisceaux satisfaisant aux conditions de} 7.1 \emph{et s'ils sont localement isomorphes} (\emph{pour la topologie étale}) \emph{comme complexes de} $A$-\emph{modules, on a}:",
  UL_X)
F(401, "Corollaire 7.9, 'En particulier, si F est localement constant de valeur M˙ , on a :'",
  "underlined: 'En particulier, si', 'est localement constant de valeur', 'on a'; not: F, M˙ and its comma, the colon",
  "no underline markup", "underline", "high",
  r"En particulier, si $F$ est localement constant de valeur $M^\bullet$, on a:",
  r"\emph{En particulier, si} $F$ \emph{est localement constant de valeur} $M^\bullet$, \emph{on a}:",
  UL_X)
F(401, "Corollaire 7.12, statement lines 1-3 (to 'comme dans')",
  "underlined: 'Soient', 'une courbe algébrique connexe lisse, pro-/pre sur', 'un ouvert non vide de', 'une sous-catégorie de', 'comme dans'; not: C, k, V, C, Δ, D⁺(A) and the commas after them",
  "no underline markup", "underline", "high",
  r"Soient $C$ une courbe algébrique connexe lisse, propre sur $k$, $V$ un ouvert non vide de $C$, $\Delta$ une sous-catégorie de $D^+(A)$ comme dans",
  r"\emph{Soient} $C$ \emph{une courbe algébrique connexe lisse, propre sur} $k$, $V$ \emph{un ouvert non vide de} $C$, $\Delta$ \emph{une sous-catégorie de} $D^+(A)$ \emph{comme dans}",
  UL_X + " Split before '7.1' so that the edit also matches the current layer (which reads 6.1 there).")
F(401, "Corollaire 7.12, statement from ', et F un complexe' to 'Sous ces conditions on a :'",
  "underlined: 'et', 'un complexe de faisceaux de', 'modules', 'sur', 'tel que sa restriction à un sous-ouvert non vide convenable de', 'soit / trivialisée par un revêtement galoisien de', 'Supposons de plus que', 'quelque soit', 'Sous ces conditions on a'; not: F, A-, the second F, V, F_x̄ ∈ Ob(Δ), x ∈ V, the punctuation",
  "no underline markup", "underline", "high",
  r", et $F$ un complexe de faisceaux de $A$-modules sur $V$ tel que sa restriction à un sous-ouvert non vide convenable de $V$ soit trivialisée par un revêtement galoisien de $V$. Supposons de plus que $F_{\bar x}\in\Ob(\Delta)$ quelque soit $x\in V$. Sous ces conditions on a:",
  r", \emph{et} $F$ \emph{un complexe de faisceaux de} $A$-\emph{modules} \emph{sur} $V$ \emph{tel que sa restriction à un sous-ouvert non vide convenable de} $V$ \emph{soit trivialisée par un revêtement galoisien de} $V$. \emph{Supposons de plus que} $F_{\bar x}\in\Ob(\Delta)$ \emph{quelque soit} $x\in V$. \emph{Sous ces conditions on a}:",
  UL_X + " 'modules' and 'sur' are separate groups: the print's second F stands between them (next item). Apply this edit before the next one.")
F(401, "Corollaire 7.12, 'un complexe de faisceaux de A-modules F sur V'",
  "de  A-modules F sur V : a second typed F after 'A-modules' (not underlined)",
  "$A$-modules sur $V$ (no F)", "misprint_in_print", "high",
  r"\emph{modules} \emph{sur}", r"\emph{modules} $F$ \emph{sur}",
  "The complex F is already named at the head of the clause ('et F un complexe ...'); the repeated F is a typing slip, which the TeX silently drops. The old is the text after the underline edit of the previous item (apply that edit first); diplomatic layer only.",
  corrected=r"\emph{modules} \emph{sur}")
F(401, "(*), first member",
  "ℝ!Γ_V(F): a double-struck R, then a hand-drawn '!' hanging below the baseline (dot under the line), then Γ with the index V",
  r"(*)\qquad \RG_{!V}(F) (ℝΓ_{!V}(F))", "formula", "high",
  r"(*)\qquad \RG_{!V}(F)", r"(*)\qquad \R_!\Gamma_V(F)",
  BANG + " The double-struck R agrees with \\R here. The '!' is written as an index of R, as the typed R_!Γ_V of pp. 404-405.")
F(401, "(*), second member",
  "RΓ_V(F) ∈ Ob(Δ): plain R (one stem), unlike the double-struck ℝ of the first member",
  r"\RG_V(F)\in\Ob(\Delta)", "font", "high",
  r"\ \RG_V(F)\in", r"\ \mathrm{R}\Gamma_V(F)\in", PLAIN_R)
F(401, "(**), first member",
  "cℓ_K(Δ)(ℝ!Γ_V(F)): double-struck R, hand-drawn '!' before Γ",
  r"\clK{\Delta}(\RG_{!V}(F))", "formula", "high",
  r"(**)\qquad¶\clK{\Delta}(\RG_{!V}", r"(**)\qquad¶\clK{\Delta}(\R_!\Gamma_V",
  BANG + " As (*).")
F(401, "(**), second member",
  "cℓ_K(Δ)(RΓ_V(F)) . : plain R",
  r"=\clK{\Delta}(\RG_V(F)).", "font", "high",
  r"=\clK{\Delta}(\RG_V(F)).", r"=\clK{\Delta}(\mathrm{R}\Gamma_V(F)).", PLAIN_R)
F(401, "'Posons EP_Δ(V,F) = ...'",
  "'Posons' underlined", "Posons (plain)", "underline", "high",
  r"Posons $", r"\emph{Posons} $", UL_X)
F(401, "'Posons EP_Δ(V,F) = cℓ_K(Δ)(RΓ_V(F)) et'",
  "RΓ_V(F): plain R", r"=\clK{\Delta}(\RG_V(F))$", "font", "high",
  r"=\clK{\Delta}(\RG_V(F))$", r"=\clK{\Delta}(\mathrm{R}\Gamma_V(F))$", PLAIN_R)
F(401, "'... (RΓ_V(F)) et' before the display EP(V) = ...",
  "'et' underlined", "et (plain)", "underline", "high",
  r" et¶\[¶\EP(V)", r" \emph{et}¶\[¶\EP(V)", UL_X)
F(401, "display EP(V) = EP_{D(F_ℓ)coh}(V,F˙_ℓ) = EP(C) - card(Z) ,",
  "(V,F˙_ℓ): F with the raised dot of complexes (as M˙) and the index ℓ",
  r"(V,F_\ell)", "formula", "high",
  r"(V,F_\ell)", r"(V,F_\ell^\bullet)", "The TeX drops the bullet.")
F(401, "'où Z = C - V et où F_ℓ est le faisceau ... On a alors la for-/mule :'",
  "underlined: 'où', 'et où', 'est le faisceau sur', 'défini en dimension / zéro par le faisceau constant associé à', 'On a alors la for-/mule'; not: Z = C - V, F_ℓ, C, F_ℓ = Z/ℓZ ., the colon",
  "no underline markup", "underline", "high",
  r"où $Z=C-V$ et où $F_\ell$ est le faisceau sur $C$ défini en dimension zéro par le faisceau constant associé à $F_\ell=\mathbb Z/\ell\mathbb Z$. On a alors la formule:",
  r"\emph{où} $Z=C-V$ \emph{et où} $F_\ell$ \emph{est le faisceau sur} $C$ \emph{défini en dimension zéro par le faisceau constant associé à} $F_\ell=\mathbb Z/\ell\mathbb Z$. \emph{On a alors la formule}:",
  UL_X)
F(401, "EP throughout pp. 401-405 (convention)",
  "EP is double-struck every time (doubled stems): (7.10) 𝔼ℙ_Δ(C,F) = 𝔼ℙ_Δ(C,F') and 𝔼ℙ(V) = 𝔼ℙ_{D(F_ℓ)coh}(V,F˙_ℓ) = 𝔼ℙ(C) - card(Z) (p. 401), (7.13) (p. 402), 𝔼ℙ_Δ(V,F) = ... = 𝔼ℙ(C)cℓ ... (p. 405)",
  r"\EP = \operatorname{EP} (roman)", "font", "high", None, None,
  "Convention of Exposé X, not itemized (as reported for pp. 390-393): one decision for the exposé, e.g. \\EP as \\mathbb{E}\\mathbb{P} inside Exposé X.")
F(401, "Ob throughout pp. 401-405 (convention)",
  "Ob with a capital O: F_x̄ ∈ Ob(Δ) (p. 401), F_η̄ ∈ Ob(Δ) (p. 402), et appartient donc à Ob(Δ) (p. 403), R_!Γ_V(F) ∈ Ob(Δ) (p. 404), ...",
  r"\Ob, which prints 'ob' (\providecommand{\Ob}{\operatorname{ob}} of s5.tex line 101 wins)", "other", "high", None, None,
  "Not itemized (25 \\Ob in Exposé X): redefine \\Ob as \\operatorname{Ob} for Exposé X, as decided for Exposé VIII (GLOBAL_ISSUES, 12 Nov).")

# ------------------------------------------------------------------ p. 402
F(402, "top of the page: display (7.13)",
  "p. 402 begins with the display (7.13) EP_Δ(V,F) = EP(V) cℓ_K(Δ)(F_η̄) - Σ_{x∈V(k)} ε^Δ_x(F) - Σ_{x∈Z} α^Δ_x(F) ,; p. 401 ends with 'On a alors la for-/mule :' and blank paper",
  "the display (7.13) ('\\[' ... '\\tag{7.13}' '\\]') is the last 8 lines of page_401.tex; the folio-402 marker follows it",
  "marker", "high", None, None,
  "Page 402 really begins at the '\\[' that opens (7.13) (live s5.tex of 16:47: diplomatic line 13627, current 13623; marker at 13635/13631). Exact fix: python -I move_marker.py 5 402 '\\[' --before (simulated in memory on both layers: the marker then stands on its own line between 'On a alors la formule:' and '\\['). Text not moved; (7.13) agrees with the print except the double-struck EP (convention).")
F(402, "Lemme 7.14, statement lines 1-2 (to 'local R')",
  "underlined: 'Soient', 'le corps des fractions d'un anneau de valuation / discrète strictement local'; not: K, R",
  "no underline markup", "underline", "high",
  r"Soient $K$ le corps des fractions d'un anneau de valuation discrète strictement local $R$",
  r"\emph{Soient} $K$ \emph{le corps des fractions d'un anneau de valuation discrète strictement local} $R$",
  UL_X)
F(402, "Lemme 7.14, from 'A un anneau noethérien' to 'et si'",
  "underlined: 'un anneau noethérien qui / est annulé par un entier', 'premier à la caractéristique résiduelle', 'de', 'et', 'un complexe de faisceaux de', 'modules sur', 'trivialisé par / une extension finie de', 'Si', 'est une sous-catégorie triangulée de', 'stable par facteurs directs et si'; not: W = Spec K, A, n, p, R, F, A-, W, K ., Δ, D⁺(A)",
  "no underline markup", "underline", "high",
  r"$A$ un anneau noethérien qui est annulé par un entier $n$ premier à la caractéristique résiduelle $p$ de $R$, et $F$ un complexe de faisceaux de $A$-modules sur $W$ trivialisé par une extension finie de $K$. Si $\Delta$ est une sous-catégorie triangulée de $D^+(A)$ stable par facteurs directs et si",
  r"$A$ \emph{un anneau noethérien qui est annulé par un entier} $n$ \emph{premier à la caractéristique résiduelle} $p$ \emph{de} $R$, \emph{et} $F$ \emph{un complexe de faisceaux de} $A$-\emph{modules sur} $W$ \emph{trivialisé par une extension finie de} $K$. \emph{Si} $\Delta$ \emph{est une sous-catégorie triangulée de} $D^+(A)$ \emph{stable par facteurs directs et si}",
  UL_X)
F(402, "Lemme 7.14, '(η le point généri-/que de S)'",
  "underlined: 'le point généri-/que de'; not: η, S and the parentheses",
  "no underline markup", "underline", "high",
  r"$\eta$ le point générique de", r"$\eta$ \emph{le point générique de}", UL_X)
F(402, "Lemme 7.14, '(η le point générique de S)'",
  "S (clear typed capital S)", "($\\eta$ le point générique de $S$): the printed reading", "misprint_in_print", "medium",
  None, None,
  "S is not introduced in the lemma (R is the strictly local trait, W = Spec K, and η is the point of W); the current layer already reads W. The TeX keeps the printed S.",
  corrected=r"($\eta$ le point générique de $W$)")
F(402, "Lemme 7.14, '(η le point générique de S) alors'",
  "S) alors (no comma)", "$S$), alors", "punctuation", "high",
  r"$S$),", r"$S$)", "The TeX adds a comma. The current layer reads W here: there the same edit is '$W$),' to '$W$)'.")
F(402, "Lemme 7.14, 'alors'",
  "'alors' underlined", "alors (plain)", "underline", "high",
  r"alors $", r"\emph{alors} $", UL_X)
F(402, "Lemme 7.14, 'alors RΓ_W(F) ∈ Ob(Δ)'",
  "RΓ_W(F): plain R", r"\RG_W(F)\in\Ob(\Delta)", "font", "high",
  r"\RG_W(F)\in", r"\mathrm{R}\Gamma_W(F)\in", PLAIN_R)
F(402, "Lemme 7.14, 'et' before cℓ_K(Δ)(RΓ_W(F)) = 0",
  "'et' underlined", "et (plain)", "underline", "high",
  r"\Ob(\Delta)$ et¶\[", r"\Ob(\Delta)$ \emph{et}¶\[", UL_X)
F(402, "Lemme 7.14, cℓ_K(Δ)(RΓ_W(F)) = 0 .",
  "the letter before Γ has one stem with serifs and a bowl, like the plain R before it; its leg is hidden under the overwritten (blotted) hand-drawn Γ, so it looks like a P",
  r"\clK{\Delta}(\RG_W(F))=0.", "font", "medium",
  r"\clK{\Delta}(\RG_W(F))=0.", r"\clK{\Delta}(\mathrm{R}\Gamma_W(F))=0.",
  PLAIN_R + " Not read as a misprint P: the leg may only be covered by the Γ.")
F(402, "proof label 'Démonstration de 7.14.'",
  "'Démonstration de' underlined, '7.14.' not", "Démonstration de 7.14. (plain text)", "underline", "high",
  r"Démonstration de 7.14.", r"\emph{Démonstration de} 7.14.",
  "Plain-text label in the TeX, so the print's underline is lost (as the proof labels of pp. 386 and 390).")
F(402, "'p-sous-groupe de Silov P'",
  "Silov", "Sylow", "misprint_in_print", "high",
  r"Sylow", r"Silov",
  "Misspelt name (Sylow); the TeX silently corrects. Diplomatic layer only.",
  corrected=r"Sylow")
F(402, "'c'est à dire la limite projective'",
  "'c'est' ends the line with no hyphen, 'à dire' begins the next: c'est à dire",
  "c'est-à-dire", "punctuation", "high",
  r"c'est-à-dire la limite", r"c'est à dire la limite",
  "The TeX adds the two hyphens (p. 404 prints 'c'est-à-dire' with them).")
F(402, "'corps résiduel de R . (Si p = 1 , on pose π̄ = π .) On a donc'",
  "a full stop after R, then a parenthesised sentence with a capital S and its full stop inside: de R . (Si p = 1 , on pose π̄ = π .) On a",
  "de $R$ (si $p=1$, on pose $\\bar\\pi=\\pi$). On a", "punctuation", "high",
  r"de $R$ (si $p=1$, on pose $\bar\pi=\pi$).", r"de $R$. (Si $p=1$, on pose $\bar\pi=\pi$.)",
  "The TeX drops the full stop after R, lower-cases Si and moves the final full stop outside the parenthesis.")
F(402, "last display, first member RΓ_W(F)",
  "plain R", r"\RG_W(F)\simeq", "font", "high",
  r"\[¶\RG_W", r"\[¶\mathrm{R}\Gamma_W", PLAIN_R)
F(402, "last display, RΓ^π(M˙)",
  "plain R", r"\R\Gamma^\pi(M^\bullet)", "font", "high",
  r" \R\Gamma^\pi", r" \mathrm{R}\Gamma^\pi", PLAIN_R)
F(402, "last display, RΓ^π̄(...)",
  "plain R", r"\R\Gamma^{\bar\pi}(", "font", "high",
  r" \R\Gamma^{\bar\pi}", r" \mathrm{R}\Gamma^{\bar\pi}", PLAIN_R)
F(402, "last display, RΓ^P(M˙)",
  "plain R", r"(\R\Gamma^P(M^\bullet))", "font", "high",
  r"(\R\Gamma^P(", r"(\mathrm{R}\Gamma^P(", PLAIN_R)

# ------------------------------------------------------------------ p. 403
F(403, "top of the page: '(\"isomorphisme de Hochschild-Serre\")'",
  "p. 403 begins with '(\"isomorphisme de Hochschild-Serre\"). Or P opère ...'; p. 402 ends with the display RΓ_W(F) ≃ ... ≃ RΓ^π̄(RΓ^P(M˙)) and blank paper",
  "'(``' is the last line of page_402.tex; the folio-403 marker stands between '(``' and 'isomorphisme' (the output prints '(`` isomorphisme' with a space after the quotes)",
  "marker", "high", None, None,
  "Page 403 really begins at '(``isomorphisme'. Exact fix, both layers (simulated in memory; the old occurs once in each): replace '\\n(``\\n%%%%%%%%%%  scan idx 414  |  folio 403  %%%%%%%%%%\\nisomorphisme' by '\\n%%%%%%%%%%  scan idx 414  |  folio 403  %%%%%%%%%%\\n(``isomorphisme' (live s5.tex of 16:47: '(``' on diplomatic line 13658, current 13654). Not move_marker.py '(``' --before (it keeps the line break, hence the space, after '(``') nor marker_split_word.py pull (it leaves a blank line, a paragraph break, after the display).")
F(403, "'qui est donc un p-groupe donc d'ordre premier à n'",
  "p-groupe donc (no comma)", "$p$-groupe, donc", "punctuation", "high",
  r"$p$-groupe, donc", r"$p$-groupe donc", "The TeX adds a comma.")
F(403, "'Donc on a RΓ^P(M˙) ≃ Γ^P(M˙)'",
  "'Donc on a' begins a new line at the left margin after the short line '... d'ordre premier à n .' (a paragraph break without indentation)",
  "run on: 'à $n$. Donc on a'", "other", "low",
  r"à $n$. Donc on a", "à $n$.¶¶Donc on a",
  "Paragraph break without indentation (as p. 58 and p. 393); drop it if such breaks are left to a global pass.")
F(403, "display RΓ^P(M˙) ≃ Γ^P(M˙)",
  "plain R", r"\R\Gamma^P(M^\bullet)\simeq", "font", "high",
  r"\R\Gamma^P(M^\bullet)\simeq", r"\mathrm{R}\Gamma^P(M^\bullet)\simeq", PLAIN_R)
F(403, "'D'autre part π̄ = ∏ Z_ℓ'",
  "an indented new paragraph after '... et appartient donc à Ob(Δ) .'",
  "run on: '$\\Ob(\\Delta)$. D'autre part'", "other", "high",
  r"$\Ob(\Delta)$. D'autre part", "$\\Ob(\\Delta)$.¶¶D'autre part", "Paragraph break.")
F(403, "'alors RΓ^π̄(M˙) ∈ Ob(Δ)'",
  "plain R", r"\R\Gamma^{\bar\pi}(M^\bullet)\in", "font", "high",
  r"alors $\R\Gamma^{\bar\pi}", r"alors $\mathrm{R}\Gamma^{\bar\pi}", PLAIN_R)
F(403, "cℓ_K(Δ)(RΓ^π̄(M˙)) = 0 . (before 'Soit pour cela')",
  "plain R", r"\clK{\Delta}(\R\Gamma^{\bar\pi}(M^\bullet))=0.", "font", "high",
  r"\clK{\Delta}(\R\Gamma^{\bar\pi}(M^\bullet))=0.", r"\clK{\Delta}(\mathrm{R}\Gamma^{\bar\pi}(M^\bullet))=0.", PLAIN_R)
F(403, "'Il existe alors un triangle dis-/tingué :'",
  "tingué : (colon before the diagram)", "triangle distingué, then the display", "punctuation", "high",
  "triangle distingué¶", "triangle distingué:¶", "The TeX drops the colon (the file writes the print's ' :' as ':').")
F(403, "triangle (7.15), bottom left vertex",
  "R Γ^π̄(M˙): plain R", r"\R\Gamma^{\bar\pi}(M^\bullet) \arrow[rr]", "font", "high",
  r"\R\Gamma^{\bar\pi}(M^\bullet) \arrow[rr]", r"\mathrm{R}\Gamma^{\bar\pi}(M^\bullet) \arrow[rr]", PLAIN_R)
F(403, "triangle (7.15), after the bottom right vertex",
  "M˙  . : a full stop after the right-hand vertex",
  "no full stop", "punctuation", "high",
  '\\arrow[ul,"1-f"]¶', '\\arrow[ul,"1-f"].¶', "The TeX drops the full stop. The small mark before this M˙ is a speck, not text.")
F(403, "'En effet d'une part il est clair que'",
  "an indented new paragraph after the diagram (7.15)", "runs on after the diagram ('\\]' then 'En effet')", "other", "high",
  "\\]¶En effet", "\\]¶¶En effet", "Paragraph break. Independent of the comma fix next.")
F(403, "'En effet d'une part'",
  "En effet d'une part (no comma)", "En effet, d'une part", "punctuation", "high",
  r", d'une part", r" d'une part", "The TeX adds a comma.")
F(403, "'il est clair que RΓ^π̄ = Ker(1-f)'",
  "plain R", r"$\R\Gamma^{\bar\pi}=\Ker(1-f)$", "font", "high",
  r"$\R\Gamma^{\bar\pi}=\Ker", r"$\mathrm{R}\Gamma^{\bar\pi}=\Ker", PLAIN_R)
F(403, "display H¹(π̄,M) = M˙/(1-f)M˙ ,",
  "a comma at the end of the display", "no comma", "punctuation", "high",
  "(1-f)M^\\bullet¶\\]", "(1-f)M^\\bullet,¶\\]", "The TeX drops the comma.")
F(403, "'(voir pour ce calcul [4] pp. 197) dans un cas sensiblement analogue)'",
  "pp. 197) dans: a closing parenthesis after 197 (the parenthesis opened before 'voir' is closed again after 'analogue')",
  "pp. 197, dans", "misprint_in_print", "high",
  r"197, dans", r"197) dans",
  "Unbalanced parenthesis of the print; the TeX silently writes a comma for it. Diplomatic layer only; independent of the next item.",
  corrected=r"197, dans")
F(403, "'sensiblement analogue) donc il en résulte'",
  "analogue) donc (no comma)", "analogue), donc", "punctuation", "high",
  r"analogue), donc", r"analogue) donc", "The TeX adds a comma.")
F(403, "'en même temps RΓ^π̄(M˙) ∈ Ob(Δ)'",
  "plain R", r"\R\Gamma^{\bar\pi}(M^\bullet)\in", "font", "high",
  r"temps $\R\Gamma^{\bar\pi}", r"temps $\mathrm{R}\Gamma^{\bar\pi}", PLAIN_R)
F(403, "cℓ_K(Δ)(RΓ^π̄(M˙)) = 0 , ce qui prouve 7.14.",
  "plain R", r"\clK{\Delta}(\R\Gamma^{\bar\pi}(M^\bullet))=0,", "font", "high",
  r"\clK{\Delta}(\R\Gamma^{\bar\pi}(M^\bullet))=0,", r"\clK{\Delta}(\mathrm{R}\Gamma^{\bar\pi}(M^\bullet))=0,", PLAIN_R)

# ------------------------------------------------------------------ p. 404
F(404, "proof label 'Démonstration de 7.12.'",
  "'Démonstration de' underlined, '7.12.' not", "Démonstration de 7.12. (plain text)", "underline", "high",
  r"Démonstration de 7.12.", r"\emph{Démonstration de} 7.12.",
  "Plain-text label in the TeX, so the print's underline is lost (as p. 402).")
F(404, "'Le fait que R_!Γ_V(F) ∈ Ob(Δ)'",
  "R_!Γ_V(F): plain R with a typed index '!', then Γ_V", r"\RG_{!V}(F) (ℝΓ_{!V}(F))", "formula", "high",
  r"Le fait que $\RG_{!V}(F)", r"Le fait que $\mathrm{R}_!\Gamma_V(F)",
  BANG + " The R is plain.")
F(404, "display 'R_!Γ_V(F) = RΓ_C(i_!(F)) .', left member",
  "R_!Γ_V(F): plain R, typed index '!'", r"\RG_{!V}(F)=", "formula", "high",
  r"\RG_{!V}(F)=", r"\mathrm{R}_!\Gamma_V(F)=", BANG + " The R is plain.")
F(404, "same display, right member",
  "RΓ_C(i_!(F)) : plain R; after i_! a faint mark (the lower stroke of an opening parenthesis), then F and two clear closing parentheses",
  r"\RG_C(i_!F).", "formula", "medium",
  r"\RG_C(i_!F).", r"\mathrm{R}\Gamma_C(i_!(F)).",
  "The TeX drops the parentheses of i_!(F) (written so everywhere else on these pages) and has ℝ for the plain R. The opening parenthesis is faint in the scan; the two closing ones are clear.")
F(404, "'Pour prouver que RΓ_V(F) ∈ Ob(Δ)'",
  "plain R", r"\RG_V(F)\in", "font", "high",
  r"Pour prouver que $\RG_V(F)", r"Pour prouver que $\mathrm{R}\Gamma_V(F)", PLAIN_R)
F(404, "'on con-/sidère le triangle distingué :'",
  "distingué : (colon before the diagram)", "triangle distingué, then the display", "punctuation", "high",
  "considère le triangle distingué¶", "considère le triangle distingué:¶", "The TeX drops the colon.")
F(404, "first triangle, bottom left vertex",
  "Ri_!(F): plain R", r"\R i_!(F) \arrow[rr]", "font", "high",
  r"\R i_!(F) \arrow[rr]", r"\mathrm{R} i_!(F) \arrow[rr]", "\\R = \\mathbb{R} in Exposé X; the print's R is plain (one stem).")
F(404, "first triangle, bottom right vertex",
  "Ri_*(F) ,: plain R", r"\R i_*(F) \arrow[ul],", "font", "high",
  r"&& \R i_*(F) \arrow[ul],", r"&& \mathrm{R} i_*(F) \arrow[ul],", "\\R = \\mathbb{R} in Exposé X; the print's R is plain (one stem).")
F(404, "'d'où en appliquant RΓ_C le trian-/gle distingué :', after d'où",
  "d'où en appliquant (no comma)", "d'où, en appliquant", "punctuation", "high",
  r"d'où, en", r"d'où en", "The TeX adds a comma.")
F(404, "same sentence, RΓ_C",
  "R Γ_C: plain R", r"$\RG_C$", "font", "high",
  r"appliquant $\RG_C", r"appliquant $\mathrm{R}\Gamma_C", PLAIN_R)
F(404, "same sentence, after RΓ_C and at its end",
  "RΓ_C le triangle distingué : (no comma after RΓ_C; a colon before the diagram)",
  "$\\RG_C$, le triangle distingué, then the display", "punctuation", "high",
  "$, le triangle distingué¶", "$ le triangle distingué:¶", "The TeX adds a comma and drops the colon (one edit, adjacent).")
F(404, "triangle (7.16), top vertex",
  "RΓ_Z(Q˙|Z): plain R", r"\RG_Z(Q^\bullet|Z) \arrow[dl]", "font", "high",
  r"& \RG_Z(Q^\bullet|Z) \arrow[dl]", r"& \mathrm{R}\Gamma_Z(Q^\bullet|Z) \arrow[dl]", PLAIN_R)
F(404, "triangle (7.16), bottom left vertex",
  "R_!Γ_V(F): plain R, typed index '!'", r"\RG_{!V}(F) \arrow[rr]", "formula", "high",
  r"\RG_{!V}(F) \arrow[rr]", r"\mathrm{R}_!\Gamma_V(F) \arrow[rr]",
  BANG + " The R is plain. The bottom right vertex ℝΓ_V(F) is double-struck in the print, as the TeX.")
F(404, "triangle (7.16), end",
  "ℝΓ_V(F) with nothing after it (no full stop)", r"\RG_V(F) \arrow[ul].", "punctuation", "high",
  "\\arrow[ul].¶", "\\arrow[ul]¶", "The TeX adds a full stop at the end of the diagram.")
F(404, "'Comme R!Γ_V(F) ∈ Ob(Δ)'",
  "plain R, then a hand-drawn '!' hanging below the baseline, then Γ_V", r"\RG_{!V}(F)", "formula", "high",
  r"Comme $\RG_{!V}(F)", r"Comme $\mathrm{R}_!\Gamma_V(F)", BANG + " The R is plain.")
F(404, "'il en résulte que RΓ_V(F) ∈ Ob(Δ)'",
  "plain R", r"\RG_V(F)\in", "font", "high",
  r"résulte que $\RG_V(F)", r"résulte que $\mathrm{R}\Gamma_V(F)", PLAIN_R)
F(404, "'si et seulement si RΓ_Z(Q˙| Z) ∈ Ob(Δ)'",
  "plain R", r"\RG_Z(Q^\bullet|Z)\in", "font", "high",
  r"seulement si $\RG_Z", r"seulement si $\mathrm{R}\Gamma_Z", PLAIN_R)
F(404, "'c'est-à-dire (Ri_*(F))_x ∈ Ob(Δ)', the R",
  "plain R", r"(\R i_*(F))", "font", "high",
  r"c'est-à-dire $(\R i_*", r"c'est-à-dire $(\mathrm{R} i_*", "\\R = \\mathbb{R} in Exposé X; the print's R is plain (one stem).")
F(404, "'c'est-à-dire (Ri_*(F))_x ∈ Ob(Δ)', the index",
  "(Ri_*(F))_x: a plain x, no bar (as 'C_x ... au point géométrique x' below)", r"_{\bar x}", "formula", "high",
  r"(F))_{\bar x}\in\Ob(\Delta)$ pour", r"(F))_x\in\Ob(\Delta)$ pour",
  "The TeX adds a bar the print does not have (here x itself is the geometric point).")
F(404, "'pour calculer (Ri_*(F))_x', the R",
  "plain R", r"(\R i_*(F))", "font", "high",
  r"calculer $(\R i_*", r"calculer $(\mathrm{R} i_*", "\\R = \\mathbb{R} in Exposé X; the print's R is plain (one stem).")
F(404, "'pour calculer (Ri_*(F))_x', the index",
  "a plain x, no bar", r"_{\bar x}", "formula", "high",
  r"(F))_{\bar x}$ on", r"(F))_x$ on", "The TeX adds a bar.")
F(404, "'on a Ri_*(F)_x ≃ RΓ_V(u*(F))', the first R",
  "plain R", r"\R i_*(F)_{\bar x}", "font", "high",
  "\\[¶\\R i_*", "\\[¶\\mathrm{R} i_*", "\\R = \\mathbb{R} in Exposé X; the print's R is plain (one stem).")
F(404, "same formula, the index of Ri_*(F)",
  "Ri_*(F)_x: a plain (heavily inked) x, no bar", r"_{\bar x}", "formula", "high",
  r"(F)_{\bar x}", r"(F)_x", "The TeX adds a bar.")
F(404, "same formula, RΓ",
  "plain R", r"\RG_{\bar V}", "font", "high",
  r"\simeq \RG", r"\simeq \mathrm{R}\Gamma", PLAIN_R)
F(404, "same formula, the index of Γ",
  "RΓ_V(u*(F)): the index is a typed V without a bar (the square above has V̄ with its bar)",
  r"\RG_{\bar V}(u^*(F))", "misprint_in_print", "high",
  r"_{\bar V}(u^*", r"_V(u^*",
  "u*(F) lives on V̄ (the cartesian square), so the cohomology is that of V̄; the TeX silently adds the bar. Independent of the R fix before it (adjacent olds). Diplomatic layer only.",
  corrected=r"_{\bar V}(u^*")
F(404, "'donc (Ri_*(F))_x ∈ Ob(Δ)', the R",
  "plain R", r"(\R i_*(F))", "font", "high",
  r"donc $(\R i_*", r"donc $(\mathrm{R} i_*", "\\R = \\mathbb{R} in Exposé X; the print's R is plain (one stem)." + P405)
F(404, "'donc (Ri_*(F))_x ∈ Ob(Δ)', the index",
  "a plain x, no bar", r"_{\bar x}", "formula", "high",
  r"(F))_{\bar x}\in\Ob(\Delta)$ et", r"(F))_x\in\Ob(\Delta)$ et", "The TeX adds a bar." + P405)
F(404, "'et cℓ_K(Δ)(Ri_*(F))_x = 0 .'",
  "cℓ_K(Δ)(Ri_*(F))_x = 0 : the parentheses of the stalk are the only ones after cℓ; plain R; x without a bar",
  r"\clK{\Delta}((\R i_*(F))_{\bar x})=0.", "formula", "high",
  r"\clK{\Delta}((\R i_*(F))_{\bar x})=0.", r"\clK{\Delta}(\mathrm{R} i_*(F))_x=0.",
  "The TeX adds an outer pair of parentheses and the bar, and has ℝ for the plain R (one edit)." + P405)
F(404, "'Il en résulte que cℓ_K(Δ)(RΓ_Z(Q˙|Z) = 0', the R",
  "plain R", r"\RG_Z(Q^\bullet|Z)", "font", "high",
  r"\clK{\Delta}(\RG_Z", r"\clK{\Delta}(\mathrm{R}\Gamma_Z", PLAIN_R + P405)
F(404, "same formula, the parentheses",
  "cℓ_K(Δ)(RΓ_Z(Q˙|Z) = 0 : one closing parenthesis after Z, two opened",
  r"(Q^\bullet|Z))=0", "misprint_in_print", "high",
  r"(Q^\bullet|Z))=0", r"(Q^\bullet|Z)=0",
  "The print does not close the parenthesis of cℓ; the TeX silently adds it. Independent of the R fix (adjacent olds). Diplomatic layer only." + P405,
  corrected=r"(Q^\bullet|Z))=0")

# ------------------------------------------------------------------ p. 405
F(405, "top of the page: 'donc (Ri_*(F))_x ∈ Ob(Δ) et ...'",
  "p. 405 begins with 'donc (Ri_*(F))_x ∈ Ob(Δ) et cℓ_K(Δ)(Ri_*(F))_x = 0 . Il en résulte que / cℓ_K(Δ)(RΓ_Z(Q˙|Z) = 0 et le triangle distingué (7.16) nous donne'; p. 404 ends with '..., en vertu de 7.14,et on a' and blank paper",
  "'donc $(\\R i_*(F))_{\\bar x}\\in\\Ob(\\Delta)$ et', the display cl(...)=0, 'Il en résulte que', the display cl(RΓ_Z(Q|Z))=0 and 'et le' are the end of page_404.tex; the folio-405 marker stands before 'triangle distingué (7.16)'",
  "marker", "high", None, None,
  "Page 405 really begins at 'donc $(' in the line 'en vertu de 7.14, et on a donc ...' (live s5.tex of 16:47: diplomatic line 13725, current 13721; marker at 13734/13730). Exact fix: python -I move_marker.py 5 405 'donc $(' --before (simulated in memory on both layers: the line is split after 'et on a ' and the marker stands on its own line before 'donc $(\\R i_*(F))'; the anchor is unchanged by the fixes of that line). Text not moved; its differences are filed under p. 404.")
F(405, "cℓ_K(Δ)(R!Γ_V(F)) = cℓ_K(Δ)(RΓ_V(F)) ., left member",
  "plain R, then a hand-drawn '!' hanging below the baseline, then Γ_V", r"\RG_{!V}(F))=", "formula", "high",
  r"nous donne¶\[¶\clK{\Delta}(\RG_{!V}", r"nous donne¶\[¶\clK{\Delta}(\mathrm{R}_!\Gamma_V", BANG + " The R is plain.")
F(405, "same display, right member",
  "plain R", r"(\RG_V(F)).", "font", "high",
  r"(\RG_V(F)).¶\]¶Enfin", r"(\mathrm{R}\Gamma_V(F)).¶\]¶Enfin", PLAIN_R)
F(405, "long display, cℓ_K(Δ)(R_!Γ_V(F))",
  "R_!Γ_V(F): plain R, typed index '!'", r"\clK{\Delta}(\RG_{!V}(F))", "formula", "high",
  "\\clK{\\Delta}(\\RG_{!V}(F))¶=", "\\clK{\\Delta}(\\mathrm{R}_!\\Gamma_V(F))¶=", BANG + " The R is plain.")
F(405, "long display, cℓ_K(Δ)(RΓ_C(...)), the R",
  "plain R", r"\clK{\Delta}(\RG_C", "font", "high",
  r"\clK{\Delta}(\RG_C", r"\clK{\Delta}(\mathrm{R}\Gamma_C", PLAIN_R)
F(405, "long display, cℓ_K(Δ)(RΓ_C(i_!(F)=EP(C)...",
  "(RΓ_C(i_!(F)=EP(C): one closing parenthesis, three opened",
  r"\clK{\Delta}(\RG_C(i_!(F)))", "misprint_in_print", "high",
  r"(i_!(F)))", r"(i_!(F)",
  "The print does not close the parentheses of RΓ_C( and cℓ(; the TeX silently adds both. Independent of the R fix (adjacent olds). Diplomatic layer only.",
  corrected=r"(i_!(F)))")
F(405, "'Or on a :'",
  "Or on a : (colon before the display)", "Or on a, then the display", "punctuation", "high",
  "Or on a¶", "Or on a:¶", "The TeX drops the colon.")
F(405, "'Mais pour x ∈ Z on a (i_!(F))_x = 0'",
  "(i_!(F))_x: a plain x, no bar", r"(i_!(F))_{\bar x}", "formula", "high",
  r"$(i_!(F))_{\bar x}=0$", r"$(i_!(F))_x=0$", "The TeX adds a bar.")
F(405, "'pour un tel x / on a :'",
  "on a : (colon before the display)", "on a, then the display", "punctuation", "high",
  "pour un tel $x$ on a¶", "pour un tel $x$ on a:¶", "The TeX drops the colon.")
F(405, "end of the page: 'Références' (folio-406 marker)",
  "p. 405 ends with 'd'où la formule (7.13).' and blank paper; p. 406 begins with 'Références'",
  "'\\section*{Références}', '\\begin{enumerate}' and '\\item[{[1]}] M.' are the last lines of page_405.tex; the folio-406 marker stood between 'M.' and 'Raynaud'",
  "marker", "high", None, None,
  "ALREADY DONE: reported by batch 406-410 and applied in both live layers at 16:47 (the marker now stands just before '\\section*{Références}'). Nothing to do.")

json.dump(L, open(OUT, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
print("wrote", OUT, len(L), "findings")
