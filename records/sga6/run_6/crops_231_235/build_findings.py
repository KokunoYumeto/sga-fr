"""Build findings_231_235.json for SGA 6 pp. 231-235 and check that every fix's 'old' occurs exactly once."""
import json
import pathlib

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
PAGES = RUN / "b231_235"
OUT = RUN / "findings_231_235.json"
NL = "<NL>"


def fx(old, new):
    return {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}


L_SCAN = "a plain typed L over the tensor sign (the same typewriter L as in the TeX's plain L of Lpr_1^*, Lg^*)"
L_NOTE = ("The typescript types the L of the derived tensor product with the ordinary typewriter L; the TeX writes "
          "\\mathbf L (bold) here while it keeps the same typed L plain in L\\pr_1^*(E) and Lg^*. Report of the "
          "print's form (no blanket rule for L).")
OB_NOTE = ("Exposé III defines \\Ob as \\operatorname{Ob} (main.tex l. 5335, '% Exposé III additions'), so the TeX "
           "prints 'Ob'; the typescript types lower-case 'ob' here, as on all pages of this batch. Changing that "
           "definition to \\operatorname{ob} would cover the exposé instead of these single edits.")

F = []

# ---------------- page 231 ----------------
F.append(dict(page=231, where="start of page",
              scan="p. 231 begins 'C'est une condition de nature locale ; si X, Y, S sont affines d'anneaux respectifs B, C, A, ...'",
              tex="'C'est une' ends the last line of page_230.tex ('... définis dans (EGA III 6.5). C'est une'), above the folio-231 marker; page_231.tex begins 'condition de nature locale'",
              kind="marker", confidence="high", fix=None,
              note="Page 231 really begins with 'C'est une'. Split the last line of p. 230 before 'C'est une' and put the marker there: python -I move_marker.py 6 231 \"C'est une\" --before (simulated on copies of both layers: the marker then stands between '(EGA III 6.5).' and 'C'est une'; the lines are the same in both layers)."))
F.append(dict(page=231, where="Notation 1.6, 'Soient X et Y deux S-schémas, E ∈ ob D⁻(X), F ∈ ob D⁻(Y).'",
              scan="E ∈ ob D⁻(X), F ∈ ob D⁻(Y) (lower-case ob)",
              tex=r"E\in\Ob D^{-}(X), F\in\Ob D^{-}(Y) (\Ob prints 'Ob' in Exposé III)",
              kind="word", confidence="high",
              fix=fx(r"E\in\Ob D^{-}(X)\), \(F\in\Ob D^{-}(Y)", r"E\in\operatorname{ob} D^{-}(X)\), \(F\in\operatorname{ob} D^{-}(Y)"),
              note=OB_NOTE))
F.append(dict(page=231, where="Lemme 1.7, 'Alors, pour E_i ∈ ob D⁻(X_i)_qcoh (1), il existe ...'",
              scan="E_i ∈ ob D⁻(X_i)_qcoh (lower-case ob)",
              tex=r"E_i\in\Ob D^{-}(X_i)_{\mathrm{qcoh}} ('Ob')",
              kind="word", confidence="high",
              fix=fx(r"E_i\in\Ob D^{-}(X_i)", r"E_i\in\operatorname{ob} D^{-}(X_i)"),
              note="As above (\\Ob prints 'Ob' in Exposé III)."))
F.append(dict(page=231, where="'elle signifie que la flèche canonique B ⊗^L_A C ⟶ B ⊗_A C est un isomorphisme'",
              scan=L_SCAN, tex=r"B\otimes_A^{\mathbf L}C", kind="font", confidence="medium",
              fix=fx(r"B\otimes_A^{\mathbf L}C", r"B\otimes_A^{L}C"), note=L_NOTE))
F.append(dict(page=231, where="Notation 1.6, display E ⊗^L_S F = Lpr_1*(E) ⊗^L Lpr_2*(F)",
              scan="both tensor signs carry a plain typed L, like the L of Lpr_1*, Lpr_2*",
              tex=r"E\otimes_S^{\mathbf L}F = L\pr_1^*(E)\otimes^{\mathbf L}L\pr_2^*(F)", kind="font", confidence="medium",
              fix=fx(r"E\otimes_S^{\mathbf L}F<NL>  =<NL>  L\pr_1^*(E)\otimes^{\mathbf L}L\pr_2^*(F)",
                     r"E\otimes_S^{L}F<NL>  =<NL>  L\pr_1^*(E)\otimes^{L}L\pr_2^*(F)"),
              note="Two \\mathbf L in one display; " + L_NOTE))
F.append(dict(page=231, where="Lemme 1.7, display f_{1*}(E_1) ⊗^L_S f_{2*}(E_2) ⟶~ (f_1 ×_S f_2)_*(E_1 ⊗^L_S E_2)",
              scan="plain typed L over both tensor signs",
              tex=r"\otimes_S^{\mathbf L} (twice)", kind="font", confidence="medium",
              fix=fx(r"f_{1*}(E_1)\otimes_S^{\mathbf L}f_{2*}(E_2)<NL>  \xrightarrow{\sim}<NL>  (f_1\times_Sf_2)_*(E_1\otimes_S^{\mathbf L}E_2)",
                     r"f_{1*}(E_1)\otimes_S^{L}f_{2*}(E_2)<NL>  \xrightarrow{\sim}<NL>  (f_1\times_Sf_2)_*(E_1\otimes_S^{L}E_2)"),
              note="Two \\mathbf L in one display; " + L_NOTE))

# ---------------- page 232 ----------------
F.append(dict(page=232, where="start of page",
              scan="p. 231 ends '... On définit facilement, par adjonction, une flèche canonique' (then the footnote); p. 232 begins with the display f_{1*}(E_1) ⊗^L_S f_{2*}(E_2) ⟶ f_*(E_1 ⊗^L_S E_2) .",
              tex="page_232.tex begins with the line 'canonique' under the folio-232 marker",
              kind="marker", confidence="high", fix=None,
              note="'canonique' is the last word of p. 231: move the folio-232 marker down one line, below 'canonique' and above the display: python -I move_marker.py 6 232 \"\\[\" (simulated on copies of both layers; the lines are the same in both)."))
F.append(dict(page=232, where="first display, f_{1*}(E_1) ⊗^L_S f_{2*}(E_2) ⟶ f_*(E_1 ⊗^L_S E_2)",
              scan="plain typed L over both tensor signs", tex=r"\otimes_S^{\mathbf L} (twice)",
              kind="font", confidence="medium",
              fix=fx(r"f_{1*}(E_1)\otimes_S^{\mathbf L}f_{2*}(E_2)<NL>  \longrightarrow<NL>  f_*(E_1\otimes_S^{\mathbf L}E_2)",
                     r"f_{1*}(E_1)\otimes_S^{L}f_{2*}(E_2)<NL>  \longrightarrow<NL>  f_*(E_1\otimes_S^{L}E_2)"),
              note="Two \\mathbf L in one display; " + L_NOTE))
F.append(dict(page=232, where="display A_1 ⊗^L_{B_1} B ⊗^L_{B_2} A_2 ⟶ A",
              scan="plain typed L over both tensor signs", tex=r"\otimes_{B_1}^{\mathbf L}, \otimes_{B_2}^{\mathbf L}",
              kind="font", confidence="medium",
              fix=fx(r"A_1\otimes_{B_1}^{\mathbf L}B\otimes_{B_2}^{\mathbf L}A_2", r"A_1\otimes_{B_1}^{L}B\otimes_{B_2}^{L}A_2"),
              note="Two \\mathbf L; " + L_NOTE))
F.append(dict(page=232, where="Proposition 1.8, '... et E_i ∈ ob D⁻(X_i)_qcoh un complexe a_i-pseudo-cohérent ...'",
              scan="E_i ∈ ob D⁻(X_i)_qcoh (lower-case ob)", tex=r"E_i\in\Ob D^{-}(X_i)_{\mathrm{qcoh}} ('Ob')",
              kind="word", confidence="high",
              fix=fx(r"E_i\in\Ob D^{-}(X_i)", r"E_i\in\operatorname{ob} D^{-}(X_i)"),
              note="As p. 231 (\\Ob prints 'Ob' in Exposé III)."))
F.append(dict(page=232, where="Proposition 1.8, 'Alors E_1 ⊗^L_S E_2 est a-pseudo-cohérent rel. à f'",
              scan=L_SCAN, tex=r"E_1\otimes_S^{\mathbf L}E_2", kind="font", confidence="medium",
              fix=fx(r"Alors \(E_1\otimes_S^{\mathbf L}E_2\)", r"Alors \(E_1\otimes_S^{L}E_2\)"), note=L_NOTE))
F.append(dict(page=232, where="Preuve of 1.8, 'on doit montrer que f'_*(E_1 ⊗^L_S E_2) est a-pseudo-cohérent'",
              scan=L_SCAN, tex=r"f'_*(E_1\otimes_S^{\mathbf L}E_2)", kind="font", confidence="medium",
              fix=fx(r"f'_*(E_1\otimes_S^{\mathbf L}E_2)", r"f'_*(E_1\otimes_S^{L}E_2)"), note=L_NOTE))
F.append(dict(page=232, where="Preuve of 1.8, 'donc (I 2.16) f_{1*}(E_1) ⊗^L_S f_{2*}(E_2) est a-pseudo-cohérent'",
              scan=L_SCAN, tex=r"f_{1*}(E_1)\otimes_S^{\mathbf L}f_{2*}(E_2)", kind="font", confidence="medium",
              fix=fx(r"(I 2.16) \(f_{1*}(E_1)\otimes_S^{\mathbf L}f_{2*}(E_2)\)", r"(I 2.16) \(f_{1*}(E_1)\otimes_S^{L}f_{2*}(E_2)\)"),
              note=L_NOTE))

# ---------------- page 233 ----------------
F.append(dict(page=233, where="start of page",
              scan="p. 232 ends 'degré > b. On conclut grâce à (1.7).'; p. 233 begins 'Corollaire 1.9. Sous les hypothèses de (1.8), le foncteur'",
              tex="page_233.tex begins with the line 'grâce à (1.7).' under the folio-233 marker",
              kind="marker", confidence="high", fix=None,
              note="'grâce à (1.7).' ends p. 232: move the folio-233 marker down below it (and the blank line), above Corollaire 1.9: python -I move_marker.py 6 233 \"\\textbf{Corollaire 1.9.}\" (simulated on copies of both layers; the lines are the same in both)."))
F.append(dict(page=233, where="Corollaire 1.9, '⊗^L_S : D⁻(X_1) x D⁻(X_2) ⟶ D⁻(X) induit un foncteur'",
              scan=L_SCAN, tex=r"\otimes_S^{\mathbf L}:D^{-}(X_1)\times D^{-}(X_2)", kind="font", confidence="medium",
              fix=fx(r"\otimes_S^{\mathbf L}:D^{-}(X_1)", r"\otimes_S^{L}:D^{-}(X_1)"), note=L_NOTE))
F.append(dict(page=233, where="Corollaire 1.9, display ⊗^L_S : D⁻(f_1)_coh x D⁻(f_2)_coh ⟶ D⁻(f)_coh (cf. (1.2)) .",
              scan=L_SCAN, tex=r"\otimes_S^{\mathbf L}:D^{-}(f_1)_{\mathrm{coh}}", kind="font", confidence="medium",
              fix=fx(r"\otimes_S^{\mathbf L}:D^{-}(f_1)", r"\otimes_S^{L}:D^{-}(f_1)"), note=L_NOTE))
F.append(dict(page=233, where="Corollaire 1.10 b), 'soient n ∈ Z ∪ {-∞} et E ∈ ob D⁻(X) un complexe à cohomologie quasi-cohérente'",
              scan="E ∈ ob D⁻(X) (lower-case ob)", tex=r"E\in\Ob D^{-}(X) ('Ob')",
              kind="word", confidence="high",
              fix=fx(r"E\in\Ob D^{-}(X)", r"E\in\operatorname{ob} D^{-}(X)"),
              note="As p. 231 (\\Ob prints 'Ob' in Exposé III)."))

# ---------------- page 234 ----------------
F.append(dict(page=234, where="Proposition 1.11, triangle X → Y → Z: label of the arrow X → Z",
              scan="the arrow X → Z is labelled f (both scans), the same letter as the arrow X → Y; a) and b) then speak of 'rel. à h'",
              tex=r'''X \arrow[r,"f"] \arrow[dr,"f"'] (printed reading kept)''',
              kind="misprint_in_print", confidence="high", fix=None,
              corrected=r'''\arrow[dr,"h"']''',
              note="The composite X → Z is h (a): 'm-pseudo-cohérent rel. à h'; b): 'rel. à h'; Preuve de a): h_*). The print labels it f; the TeX keeps the printed reading."))
F.append(dict(page=234, where="Proposition 1.11, 'soient E ∈ ob D(X), F ∈ ob D(Y), et [a,b], [c,d] des intervalles de Z'",
              scan="E ∈ ob D(X), F ∈ ob D(Y) (lower-case ob)", tex=r"E\in\Ob D(X), F\in\Ob D(Y) ('Ob')",
              kind="word", confidence="high",
              fix=fx(r"\(E\in\Ob D(X)\), \(F\in\Ob D(Y)\)", r"\(E\in\operatorname{ob} D(X)\), \(F\in\operatorname{ob} D(Y)\)"),
              note="As p. 231 (\\Ob prints 'Ob' in Exposé III)."))
F.append(dict(page=234, where="Proposition 1.11 a), 'alors E ⊗^L_Y F (cf. (1.6)) est m-pseudo-cohérent rel. à h'",
              scan=L_SCAN, tex=r"E\otimes_Y^{\mathbf L}F", kind="font", confidence="medium",
              fix=fx(r"E\otimes_Y^{\mathbf L}F", r"E\otimes_Y^{L}F"), note=L_NOTE))

# ---------------- page 235 ----------------
F.append(dict(page=235, where="'Preuve de a). D'après (1.1 (iii)), ...'",
              scan="'Preuve de' underlined; 'a).' not underlined (both scans)", tex=r"\emph{Preuve de a).}",
              kind="underline", confidence="high",
              fix=fx(r"\emph{Preuve de a).}", r"\emph{Preuve de} a)."),
              note="The item letter is outside the underline in the print; not the global case of a full stop after an underlined word."))
F.append(dict(page=235, where="'Preuve de b). On doit prouver l'assertion suivante : ...'",
              scan="'Preuve de' underlined; 'b).' not underlined (both scans)", tex=r"\emph{Preuve de b).}",
              kind="underline", confidence="high",
              fix=fx(r"\emph{Preuve de b).}", r"\emph{Preuve de} b)."),
              note="As for a)."))
F.append(dict(page=235, where="Preuve de a), 'alors h_*(E ⊗^L_Y F) est m-pseudo-cohérent'",
              scan=L_SCAN, tex=r"h_*(E\otimes_Y^{\mathbf L}F)", kind="font", confidence="medium",
              fix=fx(r"h_*(E\otimes_Y^{\mathbf L}F)", r"h_*(E\otimes_Y^{L}F)"), note=L_NOTE))
F.append(dict(page=235, where="Preuve de a), display f_*(E) ⊗^L F ⟶~ f_*(E ⊗^L_Y F)",
              scan="plain typed L over both tensor signs", tex=r"\otimes^{\mathbf L}, \otimes_Y^{\mathbf L}",
              kind="font", confidence="medium",
              fix=fx(r"f_*(E)\otimes^{\mathbf L}F\xrightarrow{\sim} f_*(E\otimes_Y^{\mathbf L}F)",
                     r"f_*(E)\otimes^{L}F\xrightarrow{\sim} f_*(E\otimes_Y^{L}F)"),
              note="Two \\mathbf L in one display; " + L_NOTE))
F.append(dict(page=235, where="Preuve de a), 'Comme le foncteur g_*(. ⊗^L F) transforme ...'",
              scan=L_SCAN, tex=r"g_*(.\otimes^{\mathbf L}F)", kind="font", confidence="medium",
              fix=fx(r"g_*(.\otimes^{\mathbf L}F)", r"g_*(.\otimes^{L}F)"), note=L_NOTE))
F.append(dict(page=235, where="Preuve de b), 'quitte à se localiser, un triangle distingué [diagram] , où E'^i est localement libre ...'",
              scan="a triangle diagram: E' ⟶ E on the bottom line, E'' above, arrows E → E'' (up-left) and E'' → E' (down-left), a comma after it; no E'[1] (both scans)",
              tex=r"E'\longrightarrow E\longrightarrow E''\longrightarrow E'[1] (linear, with E'[1], no comma)",
              kind="formula", confidence="high",
              fix=fx(r"E'\longrightarrow E\longrightarrow E''\longrightarrow E'[1]",
                     r"\begin{tikzcd}<NL>& E'' \arrow[dl] & \\<NL>E' \arrow[rr] & & E \arrow[ul],<NL>\end{tikzcd}"),
              note="Same arrows, but the print draws the triangle and has no E'[1]; it ends with a comma. A small hook '(' stands at the tail of the arrow E'' → E' (both scans; perhaps the degree-one mark), not rendered in the fix. The TeX of Exposé III writes the print's triangles in this linear form elsewhere too (p. 230, Prop. 1.4)."))
F.append(dict(page=235, where="Preuve de b), 'supposons f_*(E) a-pseudo-cohérent et acyclique en degré > b, et g_*(O_Y) (a+1-b)-pseudo-cohérent, alors f_*(E) est a-pseudo-cohérent'",
              scan="supposons f_*(E) a-pseudo-cohérent (both scans)",
              tex=r"supposons \(f_*(E)\) \(a\)-pseudo-cohérent (printed reading kept)",
              kind="misprint_in_print", confidence="medium", fix=None,
              corrected=r"supposons \(h_*(E)\) \(a\)-pseudo-cohérent",
              note="The hypothesis of 1.11 b) is that E is a-pseudo-cohérent rel. à h (f, g, h closed immersions after the reduction), i.e. h_*(E) a-pseudo-cohérent; with f_*(E) the assertion assumes its own conclusion. After 'on peut supposer X = Y et f = Id_X' (so h = g) the proof uses 'Comme g_*(E) est a-pseudo-cohérent'. The TeX keeps the printed reading."))
F.append(dict(page=235, where="Preuve de a), '(cas particulier de l'isomorphisme (*) de la preuve de (1.8))'",
              scan="de la preuve de (1.8)) (both scans)",
              tex="de la preuve de (1.8)) (printed reading kept)",
              kind="misprint_in_print", confidence="low", fix=None,
              corrected="(1.7)",
              note="The isomorphism f_*(E) ⊗^L F ≅ f_*(E ⊗^L_Y F) is the case S = Y, f_2 = id_Y of Lemme 1.7, whose proof (pp. 231-232) defines the arrow; the proof of (1.8) only cites (1.7), and no '(*)' stands in either proof (both scans). A stale cross-reference of the typescript; the intended reading is uncertain, hence low confidence."))

# ---------------- checks ----------------
ok = True
for f in F:
    if f["fix"] is None:
        assert f["kind"] in ("marker", "misprint_in_print"), f
        continue
    t = (PAGES / f"page_{f['page']:03d}.tex").read_text(encoding="utf-8")
    old = f["fix"]["old"]
    n = t.count(old)
    if n != 1 or "%%%%%%%%%%" in old or "\r" in old:
        ok = False
        print("BAD", f["page"], n, repr(old[:80]))
    for s in (old, f["fix"]["new"]):
        if any(ord(c) < 32 and c != "\n" for c in s):
            ok = False
            print("CONTROL CHAR", f["page"], repr(s[:80]))
order = ["page", "where", "scan", "tex", "kind", "confidence", "fix", "corrected", "note"]
out = [{k: f[k] for k in order if k in f} for f in F]
for f in out:
    if f["kind"] != "misprint_in_print":
        f.pop("corrected", None)
counts = {}
for f in out:
    c = counts.setdefault(f["page"], [0, 0])
    c[1 if f["kind"] == "misprint_in_print" else 0] += 1
print("counts", counts, "total", len(out), "ok", ok)
if ok:
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    print("written", OUT)
