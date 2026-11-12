import json
import pathlib

B = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\b426_430")
OUT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\findings_426_430.json")


def F(page, where, scan, tex, kind, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


L = []

# ---------------- page 426 ----------------
L.append(F(426, "(5.2), first line, left side: the subscript of f' in Tr_{Z_l[G],phi}(...)(g)",
           "f'_{ℋ^∨_{U',X'}(ℓ)}: the dual sign stands at the upper right of the hand-drawn ℋ, after it (U',X' below it), not on f'",
           r"f'^\vee_{H_{U',X'}(\ell)}", "formula", "high",
           r"(f'^\vee_{H_{U',X'}(\ell)})(g)", r"(f'_{H^\vee_{U',X'}(\ell)})(g)",
           "Same placement on the right side of this line and in (5.9), (5.11) on p. 427. The fix keeps the file's plain H (script ℋ: convention item below)."))
L.append(F(426, "(5.2), first line, right side",
           "Tr_{Z_ℓ}(g^{-1}_{X'}f')_{ℋ^∨_{U',X'}(ℓ)}: the dual sign after ℋ, nothing on the closing parenthesis",
           r"(g_{X'}^{-1}f')^\vee_{H_{U',X'}(\ell)}", "formula", "high",
           r"f')^\vee_{H_{U',X'}(\ell)}", r"f')_{H^\vee_{U',X'}(\ell)}",
           "The first line of (5.2) has the dual ℋ^∨ on both sides."))
L.append(F(426, "(5.2), second line",
           "= Tr_{Z_ℓ}(g^{-1}_{X'}f')_{ℋ_{U',X'}(ℓ)} . : no dual sign (clean paper at the upper right of ℋ)",
           r"(g_{X'}^{-1}f')_{H^\vee_{U',X'}(\ell)}", "formula", "high",
           r"f')_{H^\vee_{U',X'}(\ell)} \quad .", r"f')_{H_{U',X'}(\ell)} \quad .",
           "The print passes from the trace on ℋ^∨ (first line) to the trace on ℋ (second line), and (5.3), (5.6) continue with ℋ; the TeX moves the dual sign onto this line and keeps it in (5.3), (5.6)."))
L.append(F(426, "(5.3), left side",
           "Tr_{Z_ℓ}(g^{-1}_{X'}f')_{ℋ_{U',X'}(ℓ)}: no dual sign",
           r"H^\vee_{U',X'}(\ell)", "formula", "high",
           r"_{H^\vee_{U',X'}(\ell)} = \Tr", r"_{H_{U',X'}(\ell)} = \Tr",
           "The exact sequence of (1.3) concerns ℋ_{U',X'}(ℓ) itself."))
L.append(F(426, "(5.6), left side",
           "Tr_{Z_ℓ}(g^{-1}_{X'}f')_{ℋ_{U',X'}(ℓ)}: no dual sign",
           r"H^\vee_{U',X'}(\ell)", "formula", "high",
           r"_{H^\vee_{U',X'}(\ell)} = \sum", r"_{H_{U',X'}(\ell)} = \sum",
           ""))
L.append(F(426, "(5.6), second line, index of the inner sum",
           "x'∈X'^{g^{-1}_{X'}f'}: no subscript x under X' (clean paper; the first line prints X'_x)",
           r"{X'_x}^{g_{X'}^{-1}f'}", "misprint_in_print", "high",
           r"{X'_x}^{g_{X'}^{-1}f'}} (1", r"{X'}^{g_{X'}^{-1}f'}} (1",
           "The inner sum runs over the fixed points in the fibre X'_x of the outer index x ∈ Y^f, as in (5.4) and the first line. The TeX silently corrects; the fix restores the printed reading (diplomatic layer only). Same omission in (5.9), p. 427.",
           corrected=r"{X'_x}^{g_{X'}^{-1}f'}"))
L.append(F(426, "the module ℋ_{U',X'}(ℓ) in (5.2) (both lines), (5.3), (5.6); p. 427 (5.9), (5.11)",
           "a hand-drawn script ℋ (a loop at the foot of the left stem, the bar run out to the left), not a typed H",
           "plain H", "font", "medium", None, None,
           "Convention of the transcription for this module, not itemized (the TeX writes the same plain H on p. 425 (5.1.1) and as H_{n,U',X'} on pp. 408-411, 432-433; print not checked there). If it is set as \\mathcal{H}, apply the dual-sign fixes of pp. 426-427 first: their old strings contain the plain H."))

# ---------------- page 427 ----------------
L.append(F(427, "first sentence, 'l'ensemble X'^{g^{-1}_{X'}f'} est non vide'",
           "X'^{g^{-1}_{X'}f'}: no subscript x under X' (clean paper below it)",
           r"{X'_x}^{g_{X'}^{-1}f'}", "misprint_in_print", "high",
           r"l'ensemble ${X'_x}^", r"l'ensemble ${X'}^",
           "The set depends on the given x ∈ U^f (fixed points in the fibre X'_x, as in (5.7)); the TeX silently corrects. Diplomatic layer only.",
           corrected=r"{X'_x}^{g_{X'}^{-1}f'}"))
L.append(F(427, "first sentence, 'si et seulement si NW^{G,φ}_{f'}(x) = 1'",
           "NW^{G,φ}_{f'}(x): subscript f' with a clear prime",
           r"\mathrm{NW}_{f}^{G,\varphi}(x)", "formula", "high",
           r"\mathrm{NW}_{f}^{G", r"\mathrm{NW}_{f'}^{G",
           "The exposé introduces the invariant as NW_{f'}^{G,φ}(x) (s5.tex line 13927, p. 413) before naming it NW_f^{G,φ}(x); (5.9) and (5.11) print NW_f. Reported as the print's reading, not as a misprint."))
L.append(F(427, "(5.7)",
           "Card X'_x^{g^{-1}_{X'}f'} = c^φ(g) , x ∈ U . : 'Card' with a capital C",
           r"\card (\providecommand{\card}{\operatorname{card}}, s5.tex line 261: prints 'card')", "word", "high",
           r"\card {X'_x}", r"\operatorname{Card} {X'_x}",
           "p. 423 also prints Card(G_1) and Card(G) (twice) where the TeX has \\card: see the message (a redefinition of \\card would cover all)."))
L.append(F(427, "(5.9), left side",
           "Tr_{Z_ℓ[G],φ}(f'_{ℋ^∨_{U',X'}(ℓ)})(g): the dual sign after ℋ, not on f'",
           r"f'^\vee_{H_{U',X'}(\ell)}", "formula", "high",
           r"f'^\vee_{H_{U',X'}(\ell)})(g)", r"f'_{H^\vee_{U',X'}(\ell)})(g)",
           "As (5.2) on p. 426."))
L.append(F(427, "(5.9), second line, index of the inner sum",
           "x'∈X'^{g^{-1}_{X'}f'}: no subscript x under X' (clean paper)",
           r"{X'_x}^{g_{X'}^{-1}f'}", "misprint_in_print", "high",
           r"{X'_x}^{g_{X'}^{-1}f'}} \frac", r"{X'}^{g_{X'}^{-1}f'}} \frac",
           "As (5.6) on p. 426; the TeX silently corrects. Diplomatic layer only.",
           corrected=r"{X'_x}^{g_{X'}^{-1}f'}"))
L.append(F(427, "(5.9), numerator (1-ν_{x'}(g^{-1}_{x'}f'))",
           "the subscript of g is a small x' (15 px high, like the x' of ν; the capital X' of g_{X'} in the sum index is 21 px)",
           r"g_{X'}^{-1}f'", "misprint_in_print", "high",
           r"(g_{X'}^{-1}f'))}{c", r"(g_{x'}^{-1}f'))}{c",
           "g_{X'} is the action of g on X', as everywhere on these pages; the TeX silently corrects. Diplomatic layer only.",
           corrected=r"g_{X'}^{-1}f'"))
L.append(F(427, "heading 5.10",
           "5.10. Cas particuliers. (underlined title, full stop after it)",
           r"\subsection*{5.10. Cas particuliers}", "punctuation", "high",
           r"\subsection*{5.10. Cas particuliers}", r"\subsection*{5.10. Cas particuliers.}",
           ""))
L.append(F(427, "(5.11), left side",
           "Tr_{Z_ℓ[G],φ}(f'_{ℋ^∨_{U',X'}(ℓ)}): the dual sign after ℋ, not on f'",
           r"f'^\vee_{H_{U',X'}(\ell)}", "formula", "high",
           r"f'^\vee_{H_{U',X'}(\ell)}) =", r"f'_{H^\vee_{U',X'}(\ell)}) =",
           "As (5.2) on p. 426."))
L.append(F(427, "b), 'ν_{x'}(g^{-1}_X f') = 1'",
           "g^{-1}_X: capital X without prime (clean paper between X and f')",
           r"g_{X'}^{-1}f'", "misprint_in_print", "high",
           r"(g_{X'}^{-1}f') = 1$", r"(g_{X}^{-1}f') = 1$",
           "(5.8) prints g^{-1}_{X'}; the TeX silently corrects. Diplomatic layer only.",
           corrected=r"g_{X'}^{-1}f'"))
L.append(F(427, "b), '∀x'∈Y'^{...}'",
           "the typed quantifier ∀, no words",
           r"pour tout $x'\in", "symbol", "high",
           r"pour tout $x'\in", r"$\forall x'\in",
           "Abbreviation written out by the TeX."))
L.append(F(427, "b), exponent of Y' in '∀x'∈Y'^{g^{-1}_Y f'_Y}'",
           "g^{-1}_Y f'_Y: both subscripts Y without prime (clean paper after each Y)",
           r"{Y'}^{g_{Y'}^{-1}f'_{Y'}}", "misprint_in_print", "high",
           r"{Y'}^{g_{Y'}^{-1}f'_{Y'}}", r"{Y'}^{g_{Y}^{-1}f'_{Y}}",
           "(5.5) on p. 426 prints g^{-1}_{Y'}f'_{Y'}; the TeX silently corrects both. Diplomatic layer only.",
           corrected=r"{Y'}^{g_{Y'}^{-1}f'_{Y'}}"))
L.append(F(427, "b), 'et ∀g ∈ G .'",
           "et ∀g ∈ G . (typed quantifier)",
           r"et tout $g\in G$", "symbol", "high",
           r"et tout $g\in G$", r"et $\forall g\in G$",
           "Abbreviation written out by the TeX."))
L.append(F(427, "last line, 'ν_x(f) = 1 pour tout y ∈ Y'",
           "ν_x(f) = 1: argument f",
           r"\nu_y(x)=1", "formula", "high",
           r"(x)=1$ pour", r"(f)=1$ pour",
           "The TeX's \\nu_y(x) is neither the print (ν_x(f)) nor the corrected reading (ν_y(f)). This fix restores the argument f in both layers; the next item restores the printed subscript x (no overlap between the two). In the same sentence, the full stop after 'formule 5.11' is only a faint 2x2 grey speck at the stop's position: the TeX's '5.11.' is left as it is."))
L.append(F(427, "last line, subscript of ν in 'ν_x(f) = 1 pour tout y ∈ Y'",
           "ν_x: subscript x, against the bound y of 'pour tout y ∈ Y'",
           r"\nu_y", "misprint_in_print", "high",
           r", $\nu_y", r", $\nu_x",
           "The TeX silently corrects the subscript (the source comment on this line already names ν_x(f) as the diplomatic reading). Diplomatic layer only.",
           corrected=r"\nu_y(f)=1"))

# ---------------- page 428 ----------------
L.append(F(428, "heading 6",
           "6. Application à une formule de Lefschetz. (underlined title, full stop after it)",
           r"\section*{6. Application à une formule de Lefschetz}", "punctuation", "high",
           r"\section*{6. Application à une formule de Lefschetz}", r"\section*{6. Application à une formule de Lefschetz.}",
           ""))
L.append(F(428, "number 6.1",
           "6.1. Nous garderons ... (number with its full stop, run into the text)",
           r"\subsection*{6.1}", "punctuation", "high",
           r"\subsection*{6.1}", r"\subsection*{6.1.}",
           "As reported for \\subsection*{3.6.5} (p. 97)."))
L.append(F(428, "'et par conséquence un endomorphisme de complexes'",
           "par conséquence (clear, 2x crop)",
           "par conséquent", "word", "high",
           r"et par conséquent un endomorphisme", r"et par conséquence un endomorphisme",
           "The print has 'par conséquence' here and on p. 429 ('et par conséquence M est un'), 'par conséquent' elsewhere; an older form of the locution, reported as a word difference, not as a misprint."))
L.append(F(428, "display after 'endomorphisme de complexes de A-modules :', left member",
           "ℝΓ_x(u,f): the subscript of Γ is a small x (the three others on the line are capital X)",
           r"\R\Gamma_X(u, f)", "misprint_in_print", "high",
           r"\R\Gamma_X(u, f) :", r"\R\Gamma_x(u, f) :",
           "The TeX silently corrects. Diplomatic layer only.",
           corrected=r"\R\Gamma_X(u, f)"))
L.append(F(428, "same display, target of the arrow",
           "⟶(ℝΓ_X(F) . : an opening parenthesis before ℝ, never closed",
           r"\longrightarrow \R\Gamma_X(F)", "misprint_in_print", "high",
           r"\longrightarrow \R\Gamma_X(F) \quad .", r"\longrightarrow (\R\Gamma_X(F) \quad .",
           "Stray parenthesis; the TeX silently drops it. Diplomatic layer only.",
           corrected=r"\longrightarrow \R\Gamma_X(F)"))

# ---------------- page 429 ----------------
L.append(F(429, "heading 6.2",
           "6.2.Définition des termes locaux. (underlined title, full stop after it)",
           r"\subsection*{6.2. Définition des termes locaux}", "punctuation", "high",
           r"\subsection*{6.2. Définition des termes locaux}", r"\subsection*{6.2. Définition des termes locaux.}",
           ""))
L.append(F(429, "'la restruction du faisceau F' = p*(F)'",
           "restruction (clear, 3x crop)",
           "restriction", "misprint_in_print", "high",
           r"la restriction du", r"la restruction du",
           "Typing error; the TeX silently corrects. Diplomatic layer only.",
           corrected="restriction"))
L.append(F(429, "display 'F'|_{U'} ≈ M_{U'} .'",
           "≈: two wavy strokes, no straight stroke",
           r"\simeq (≃)", "symbol", "medium",
           r"F'|_{U'} \simeq", r"F'|_{U'} \approx",
           "Same sign in the display after 'on a :' (next item but one)."))
L.append(F(429, "'un point géométrique sur η (resp η' ) on a :'",
           "(resp η' ): no full stop after resp (clean paper; the three other resp. of the sentence have it)",
           r"(resp. $\eta'$)", "misprint_in_print", "high",
           r"(resp. $\eta'$) on a", r"(resp $\eta'$) on a",
           "The TeX silently supplies the abbreviation's full stop. Diplomatic layer only.",
           corrected=r"(resp. $\eta'$)"))
L.append(F(429, "display after 'on a :', first line",
           "p(η') = η  (on a line of its own, no comma after it)",
           r"p(\eta')=\eta,", "punctuation", "high",
           r"p(\eta')=\eta,", r"p(\eta')=\eta",
           "The print sets the two relations on two lines without punctuation between them; the TeX adds the comma."))
L.append(F(429, "display after 'on a :', second line",
           "F_η̄ ≈ F'_η̄' . : two wavy strokes",
           r"\simeq (≃)", "symbol", "medium",
           r"F_{\bar\eta} \simeq", r"F_{\bar\eta} \approx",
           ""))
L.append(F(429, "'est isomorphe à M et par conséquence M est un A-module parfait'",
           "par conséquence (clear, 3x crop)",
           "par conséquent", "word", "high",
           r"et par conséquent $M$", r"et par conséquence $M$",
           "As p. 428. After the first M there is only a faint 2x2 grey speck where a full stop could stand (the typed full stops of the page are solid 3x4 dots): too faint to read, not reported."))

# ---------------- page 430 ----------------
L.append(F(430, "'Le dual M̌ de M par rapport à A'",
           "the dual sign set above M (an accent, as \\check M); on the same page u^∨_M has it as a superscript",
           r"M^\vee", "symbol", "medium",
           r"dual $M^\vee$", r"dual $\check{M}$",
           "Four places on this page (this and the next three items); the file already uses \\check for such signs (\\check{Sw}). u_M^\\vee stays."))
L.append(F(430, "display 'u^∨_M : M̌ ⟶ M̌ ,'",
           "both M with the dual sign above them",
           r"M^\vee (twice)", "symbol", "medium",
           r"u_M^\vee:M^\vee\longrightarrow M^\vee ,", r"u_M^\vee:\check{M}\longrightarrow \check{M} ,",
           ""))
L.append(F(430, "display 'u^∨_M(gx) = φ(g)u^∨_M(x)  ∀ g ∈ G, ∀ x ∈ M̌ .'",
           "x ∈ M̌: the dual sign above M",
           r"M^\vee", "symbol", "medium",
           r"x\in M^\vee .", r"x\in \check{M} .",
           ""))
L.append(F(430, "'En plus M̌ est un A-module parfait'",
           "M̌: the dual sign above M",
           r"M^\vee", "symbol", "medium",
           r"plus $M^\vee$", r"plus $\check{M}$",
           ""))
L.append(F(430, "'(On identifie les points fermés de X avec les points de X(x)) :'",
           "X(x)): a small x in the parentheses (clear)",
           r"$X(x)$", "misprint_in_print", "medium",
           None, None,
           "X is proper over the field k (6.1): its closed points are the points of X(k). The TeX keeps the printed reading.",
           corrected=r"$X(k)$"))

# ---------------- checks ----------------
texts = {p: (B / f"page_{p}.tex").read_text(encoding="utf-8") for p in range(426, 431)}
ok = True
for i, d in enumerate(L):
    fx = d["fix"]
    if fx is None:
        continue
    n = texts[d["page"]].count(fx["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE", i, d["page"], n, repr(fx["old"]))
    if "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]:
        ok = False
        print("MARKER IN FIX", i)
# sequential application, all fixes (diplomatic) and non-misprint fixes only
for label, keep in (("all", lambda d: True), ("non-misprint", lambda d: d["kind"] != "misprint_in_print")):
    cur = dict(texts)
    for i, d in enumerate(L):
        fx = d["fix"]
        if fx is None or not keep(d):
            continue
        n = cur[d["page"]].count(fx["old"])
        if n != 1:
            ok = False
            print("SEQ", label, "fails at", i, d["page"], n, repr(fx["old"]))
        cur[d["page"]] = cur[d["page"]].replace(fx["old"], fx["new"], 1)
    if label == "all":
        final = cur
# misprint fixes must change only the misprinted characters: report the diff size
import difflib
for i, d in enumerate(L):
    if d["kind"] == "misprint_in_print" and d["fix"]:
        o, n_ = d["fix"]["old"], d["fix"]["new"]
        sm = difflib.SequenceMatcher(None, o, n_)
        ops = [(t, o[a:b], n_[c:e]) for t, a, b, c, e in sm.get_opcodes() if t != "equal"]
        print("misprint", d["page"], ops)
OUT.write_text(json.dumps(L, ensure_ascii=False, indent=1), encoding="utf-8")
from collections import Counter
cnt = Counter((d["page"], d["kind"] == "misprint_in_print") for d in L)
for p in range(426, 431):
    print(p, "normal", cnt[(p, False)], "misprint", cnt[(p, True)])
print("OK" if ok else "PROBLEMS", len(L))
for p in (426, 427, 429, 430):
    pass
