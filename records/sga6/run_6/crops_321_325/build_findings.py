"""Build findings_321_325.json and check that every fix's 'old' occurs exactly once in its page_NNN.tex."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b321_325"
OUT = RUN / "findings_321_325.json"
NL = "\n"


def F(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": confidence,
         "fix": None if fix is None else {"old": fix[0], "new": fix[1]}}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    return d


U1 = ("The underlined 1 is the unit element of the ring 1+K[[t]]^+ (= 1+t) and of the rings of series over it, "
      "as distinct from the integer 1 inside (1+t), {1+t}; the TeX drops the underline everywhere on pp. 321-322.")

findings = [
    # ---------------- p. 321 ----------------
    F(321, "a), second display, third member",
      "(1 + {1+t}u)^n with the first 1 underlined (both scans)",
      r"(1+\{1+t\}u)^n", "underline", "high",
      (r"(1+\{1+t\}u)^n", r"(\underline{1}+\{1+t\}u)^n"), U1),
    F(321, "b), 'D'abord, λ_u(1) = λ_u(1+t) = 1 + {1+t}u = 1 + 1.u'",
      "λ_u(1̲) = λ_u(1+t) = 1̲ + {1+t}u = 1̲ + 1̲.u : four underlined 1 (both scans)",
      r"\lambda_u(1)=\lambda_u(1+t)=1+\{1+t\}u=1+1\cdot u", "underline", "high",
      (r"\lambda_u(1)=\lambda_u(1+t)=1+\{1+t\}u=1+1", r"\lambda_u(\underline{1})=\lambda_u(1+t)=\underline{1}+\{1+t\}u=\underline{1}+\underline{1}"),
      U1 + " The 1 inside (1+t) and {1+t} are not underlined. Independent of the \\cdot entry that follows (the two 'old' do not overlap)."),
    F(321, "b), '1 + 1.u'",
      "1̲.u: a typed full stop on the baseline between 1̲ and u (both scans; crops_321_325/c321_1u.png)",
      r"1\cdot u", "symbol", "low",
      (r"\cdot u\)", r".u\)"),
      "\\cdot raises the typed stop to mid-height (as the low entries for (P,.) p. 89, (.,G) p. 117)."),
    F(321, "left diagram, upper right corner",
      "(Ĝ^u∘Ĝ^t) × Ĝ^u∘Ĝ^t) : the second factor has no opening parenthesis (both scans; crops_321_325/c321_diag.png, w332_diag.png)",
      r"(\Ghat^u\circ\Ghat^t)\times(\Ghat^u\circ\Ghat^t)", "misprint_in_print", "high",
      (r"\times(\Ghat^u", r"\times\Ghat^u"),
      "Unbalanced parenthesis in the print; the TeX silently supplies it. The fix restores the printed reading.",
      corrected=r"\times(\Ghat^u"),
    F(321, "left diagram, lower horizontal arrow Ĝ^t → Ĝ^u∘Ĝ^t",
      "λ_u stands above the lower arrow, as λ_u × λ_u above the upper one (both scans)",
      r"\arrow[r,\"\lambda_u\"'] (label set below the arrow)".replace('\\"', '"'), "formula", "medium",
      (r'\arrow[r,"\lambda_u"' + "']", r'\arrow[r,"\lambda_u"]'),
      "Label on the wrong side of the arrow (as reported on pp. 301-303, 307, 314); the labels ∘ (left, right) stand as printed."),
    F(321, "right diagram, lower horizontal arrow Ĝ^u∘Ĝ^t → Ĝ^v∘Ĝ^u∘Ĝ^t",
      "λ_v stands above the lower arrow, as λ_v above the upper one (both scans)",
      r'\arrow[r,"\lambda_v"' + "'] (label set below the arrow)", "formula", "medium",
      (r'\arrow[r,"\lambda_v"' + "']", r'\arrow[r,"\lambda_v"]'),
      "Label on the wrong side of the arrow; λ_u (left) and Ĝ^v(λ_u) (right) stand as printed."),
    # ---------------- p. 322 ----------------
    F(322, "first display, first line 'λ_u(1+Xt)∘λ_u(1+Yt) = (1+{Xt}u)∘(1+{1+Yt}u)'",
      "(1̲+{Xt}u)∘(1̲+{1+Yt}u): both 1 underlined (both scans)",
      r"&=(1+\{Xt\}u)\circ(1+\{1+Yt\}u)", "underline", "high",
      (r"&=(1+\{Xt\}u)\circ(1+\{1+Yt\}u)", r"&=(\underline{1}+\{Xt\}u)\circ(\underline{1}+\{1+Yt\}u)"),
      U1 + " The misprint {Xt} of the same line is a separate entry (fix null)."),
    F(322, "first display, first line, '{Xt}'",
      "(1̲+{Xt}u): the braces enclose Xt only (both scans; crops_321_325/c322_xt.png, w333_xt.png)",
      r"\{Xt\}u", "misprint_in_print", "high", None,
      "λ_u(1+Xt) = 1̲+{1+Xt}u (cf. λ_u(1+t) = 1̲+{1+t}u on p. 321, the second factor {1+Yt} and the next lines {(1+Xt)∘(1+Yt)}, {1+Xt}); the print drops '1+'. The TeX keeps the printed reading.",
      corrected=r"\{1+Xt\}u"),
    F(322, "first display, second line",
      "= 1̲ + {(1+Xt)∘(1+Yt)}u, 1 underlined (both scans)",
      r"&=1+\{(1+Xt)\circ(1+Yt)\}u", "underline", "high",
      (r"&=1+\{(1+Xt)", r"&=\underline{1}+\{(1+Xt)"), U1),
    F(322, "first display, third line",
      "= 1̲ + {1+XYt}u, 1 underlined (both scans)",
      r"&=1+\{1+XYt\}u", "underline", "high",
      (r"&=1+\{1+XYt\}u", r"&=\underline{1}+\{1+XYt\}u"), U1),
    F(322, "display after 'Pour le deuxième :'",
      "λ_v(λ_u(1+Xt)) = 1̲ + { 1̲+{1+Xt}u} v : both 1 underlined (both scans)",
      r"1+\{1+\{1+Xt\}u\}v", "underline", "high",
      (r"1+\{1+\{1+Xt\}u\}v", r"\underline{1}+\{\underline{1}+\{1+Xt\}u\}v"), U1),
    F(322, "2.6 ii), end of the condition",
      "'on a x/n ∈ K' with nothing after K: no full stop (both scans)",
      r"\binom{x}{n}\in K.", "punctuation", "high",
      (r"\in K.", r"\in K"),
      "Added full stop at the end of the condition. Independent of the misprint entry of the same line (the two 'old' do not overlap)."),
    F(322, "2.6 ii), 'on a (x n) ∈ K'",
      "x over n with a fraction bar (x typed underlined, n below) and no parentheses, unlike the binomials (x n) of the next lines (both scans; crops_321_325/c322_ii.png, w333_ii.png)",
      r"\text{on a}\ \binom{x}{n}\in K", "misprint_in_print", "high",
      (r"\text{on a}\ \binom{x}{n}", r"\text{on a}\ \frac{x}{n}"),
      "The condition must be that the binomial coefficients (x n) lie in K (they define λ^n(x) in the next line and 2.6.1; x/n ∈ K is not meant, n = 0 included). The TeX silently corrects; the fix restores the printed fraction.",
      corrected=r"\binom{x}{n}"),
    F(322, "after (2.6.1), 'ceci définit une structure de pré-λ-anneau sur K'",
      "'une structure / de pré-λ-anneau sur K.' (both scans)",
      r"une structure pré-\(\lambda\)-anneau", "missing", "high",
      (r"une structure pré-", r"une structure de pré-"), "The word 'de' is missing."),
    # ---------------- p. 323 ----------------
    F(323, "first paragraph, 'que le pré-λ-anneau Z (2.5.a))'",
      "'le pré- -anneau  Z  (2.5.a))': the λ is not filled in, a blank between the hyphens (both scans; crops_321_325/c323_lam.png, w334_lam.png)",
      r"que le pré-\(\lambda\)-anneau", "misprint_in_print", "high",
      (r"que le pré-\(\lambda\)-anneau", r"que le pré- -anneau"),
      "The handwritten λ (and the double stroke of Z, next entry) were not added on this line; the second λ of the line is missing too. The TeX silently supplies it; the fix restores the printed blank.",
      corrected=r"que le pré-\(\lambda\)-anneau"),
    F(323, "first paragraph, 'Z (2.5.a))'",
      "a plain typed Z, without the hand-drawn double stroke of the Z on pp. 321-323 (both scans)",
      r"\(\mathbb Z\) (2.5.a))", "misprint_in_print", "medium",
      (r"\(\mathbb Z\) (2.5.a))", r"\(Z\) (2.5.a))"),
      "Part of the hand additions not made on this line (the two λ are blank). If the volume treats the typist's plain letters as a font matter (plain Q, SGA 7 II issue 61), take it as a font entry instead.",
      corrected=r"\(\mathbb Z\) (2.5.a))"),
    F(323, "first paragraph, 'est un λ-anneau ; elles sont donc satisfaites'",
      "'est un  -anneau ;': the λ is not filled in (both scans)",
      r"un \(\lambda\)-anneau; elles", "misprint_in_print", "high",
      (r"un \(\lambda\)-anneau; elles", r"un -anneau; elles"),
      "As the first λ of the line. The TeX silently supplies it.",
      corrected=r"un \(\lambda\)-anneau; elles"),
    F(323, "Définition 2.7",
      "statement underlined word group by word group: 'On appelle', 'un anneau vérifiant les con-ditions', 'et', 'muni de la structure de', 'anneau définie par'; 'anneau binômial', 2.6.i), ii), λ- and 2.6.1 plain (both scans)",
      "the statement in roman", "underline", "high", None,
      "Exposé V continues the pattern of GLOBAL_ISSUES 82 (statements in roman where the typescript underlines their word groups), as reported for p. 298: not itemized, for the scripted per-exposé decision. The defined term 'anneau binômial' is plain in print and TeX."),
    F(323, "Exemple 2.8, 'K le faisceau associé au préfaisceau constant'",
      "K̲: a typed K underlined (both scans)",
      r"\(\mathcal K\) le faisceau", "font", "high",
      (r"\(\mathcal K\) le faisceau", r"\(\underline{K}\) le faisceau"),
      "The sheaf is the typed K underlined, not a script K."),
    F(323, "Exemple 2.8, 'alors H^o(X,K) est un anneau binômial'",
      "H^o(X,K̲): K typed and underlined (both scans)",
      r"H^0(X,\mathcal K)", "font", "high",
      (r"H^0(X,\mathcal K)", r"H^0(X,\underline{K})"), "As the previous entry."),
    F(323, "after Exemple 2.8, 'En effet, les conditions 2.6 se conservent'",
      "'En effet, ...' begins a new line at the paragraph indent, after 'un anneau binômial.' (both scans)",
      "run on in the paragraph of the Exemple", "other", "medium",
      ("binômial. En effet, les conditions", "binômial." + NL + NL + "En effet, les conditions"),
      "The typescript indents its new paragraphs (p. 322 'Pour voir', p. 324 'Notons enfin')."),
    F(323, "'En particulier, H^o(X,Z) est un anneau binômial.'",
      "'En particulier, ...' begins a new line at the paragraph indent (both scans)",
      "run on in the same paragraph", "other", "medium",
      ("inductive. En particulier,", "inductive." + NL + NL + "En particulier,"),
      "As the previous entry."),
    F(323, "'En particulier, H^o(X,Z)'",
      "H^o(X,Z̲): the double-struck Z underlined (the constant sheaf; both scans; crops_321_325/c323_z.png, w334_z.png)",
      r"H^0(X,\mathbb Z)", "underline", "high",
      (r"H^0(X,\mathbb Z)", r"H^0(X,\underline{\mathbb Z})"), ""),
    # ---------------- p. 324 ----------------
    F(324, "3.1, 'de nouvelles opérations'",
      "'de nouvelles oérations' (both scans)",
      "de nouvelles oérations", "misprint_in_print", "high", None,
      "Typing error (missing p). The TeX keeps the printed reading.",
      corrected="opérations"),
    F(324, "3.1, 'si E est un fibré vectoriel de rang d'",
      "E̲ underlined (both scans)",
      r"si \(E\) est", "underline", "high",
      (r"si \(E\) est", r"si \(\underline{E}\) est"),
      "The bundle E is underlined throughout pp. 324-325 (six places); the TeX has a plain E."),
    F(324, "3.1, 'la d-ième classe de Chern de E devra être'",
      "E̲ underlined (both scans)",
      r"de \(E\) devra", "underline", "high",
      (r"de \(E\) devra", r"de \(\underline{E}\) devra"), "As the previous entry."),
    F(324, "last words of the TeX page, 'de E\" ;' (printed at the top of p. 325)",
      "p. 325 begins 'de E̲\" ;' with E underlined (both scans)",
      r"de \(E\)~» ;", "underline", "high",
      (r"de \(E\)~» ;", r"de \(\underline{E}\)~» ;"),
      "This text belongs to printed p. 325 (marker entry of p. 325). The edit and the marker move are independent (either order); after the move this 'old' stands under the folio-325 marker."),
    # ---------------- p. 325 ----------------
    F(325, "start of page (folio-325 marker)",
      "p. 325 begins 'de E̲\" ; pour définir la n-ième classe de Chern'; p. 324 ends '... la \"somme alternée des puissances extérieures' (both scans; witness pp. 324-325)",
      "'de \\(E\\)~» ;' ends the last line of page_324.tex (under the folio-324 marker); page_325.tex begins 'pour définir'",
      "marker", "high", None,
      "Page 325 really begins with 'de \\(E\\)~» ;'. python -I move_marker.py 6 325 'de \\(E\\)~' --before (ASCII anchor: the » does not survive the shell; the last occurrence before the marker is the one after 'extérieures'). Simulated in memory on both layers with crops_321_325/sim_markers.py: '... des puissances extérieures ' / the marker / 'de \\(E\\)~» ;' / 'pour définir la ...'."),
    F(325, "first paragraph, 'en ramenant E au rang n'",
      "E̲ underlined (both scans)",
      r"ramenant \(E\) au", "underline", "high",
      (r"ramenant \(E\) au", r"ramenant \(\underline{E}\) au"), "As p. 324."),
    F(325, "first paragraph, 'en considérant (cl(E)-d)+n'",
      "cl(E̲): E underlined (both scans)",
      r"(\cl(E)-d)+n", "underline", "high",
      (r"(\cl(E)-d)+n", r"(\cl(\underline{E})-d)+n"), "As p. 324."),
    F(325, "first paragraph, 'en y faisant x = cl(E)-d :'",
      "cl(E̲): E underlined (both scans)",
      r"x=\cl(E)-d", "underline", "high",
      (r"x=\cl(E)-d", r"x=\cl(\underline{E})-d"), "As p. 324."),
    F(325, "Proposition 3.2",
      "statement underlined word group by word group: 'Soit', 'un', 'anneau' (λ- plain); ii) 'Si on pose', 'et', 'alors', 'donc' (both scans)",
      "the statement in roman", "underline", "high", None,
      "As Définition 2.7 on p. 323: the GLOBAL_ISSUES 82 pattern, not itemized."),
    F(325, "'On voit donc que la connaissance des opérations γ'",
      "a new paragraph at the paragraph indent after the proposition (both scans)",
      "follows \\end{enumerate} without a blank line, so it is set unindented as a continuation", "other", "low",
      (r"\end{enumerate}" + NL + "On voit donc", r"\end{enumerate}" + NL + NL + "On voit donc"),
      "The typescript indents its new paragraphs."),
    F(325, "'Démonstration.'",
      "'Démonstration.' stands alone on its line; 'i) On a' begins the next line at the paragraph indent (both scans)",
      r"\emph{Démonstration.} i) On a", "other", "low",
      (r"\emph{Démonstration.} i) On a", r"\emph{Démonstration.}" + NL + NL + "i) On a"),
      "Not the exempted case (a heading the print runs into the text): here the print breaks after the label."),
    F(325, "proof ii), 'λ_{t/1-t}(x) = Σ λ^n(x). t^n(1-t)^{-n}'",
      "a typed full stop on the baseline after λ^n(x) (both scans)",
      r"\lambda^n(x)\cdot t^n(1-t)^{-n}", "symbol", "low",
      (r"\lambda^n(x)\cdot t^n(1-t)^{-n}", r"\lambda^n(x).t^n(1-t)^{-n}"),
      "As '1.u' on p. 321."),
    F(325, "proof ii), 'On développe'",
      "'On développe' starts at the left margin after the line ii): the paragraph continues (both scans)",
      "a blank line before 'On développe' (new, indented paragraph)", "other", "low",
      (r".\)" + NL + NL + "On développe", r".\)" + NL + "On développe"),
      "New paragraphs are indented in the typescript ('ii)', 'On voit donc'); this line is not."),
    F(325, "proof ii), 'λ_{t/1-t}(x) = Σ [λ^n(x). Σ ...]'",
      "a typed full stop on the baseline after λ^n(x) (both scans)",
      r"\bigl[\lambda^n(x)\cdot\sum", "symbol", "low",
      (r"\bigl[\lambda^n(x)\cdot\sum", r"\bigl[\lambda^n(x).\sum"),
      "As '1.u' on p. 321."),
    F(325, "last display, first sum",
      "Σ with n=0 below and no upper index (both scans; crops_321_325/c325_sums.png, witness p. 325)",
      r"\sum_{n=0}^{p}", "extra", "high",
      (r"\[" + NL + r"  \sum_{n=0}^{p}", r"\[" + NL + r"  \sum_{n=0}"),
      "Added summation index. Independent of the next two entries (the 'old' do not overlap)."),
    F(325, "last display, second sum",
      "Σ with n=0 below and no upper index (both scans)",
      r"=\sum_{n=0}^{p}\lambda^n(x)\lambda^{p-n}(p-1)", "extra", "high",
      (r"=\sum_{n=0}^{p}\lambda^n(x)\lambda", r"=\sum_{n=0}\lambda^n(x)\lambda"),
      "Added summation index."),
    F(325, "last display, 'λ^n(x). (p-1 p-n)'",
      "a typed full stop on the baseline after λ^n(x) (both scans)",
      r"\lambda^n(x)\cdot\binom{p-1}{p-n}", "symbol", "low",
      (r"\lambda^n(x)\cdot\binom{p-1}{p-n}", r"\lambda^n(x).\binom{p-1}{p-n}"),
      "As '1.u' on p. 321."),
    F(325, "end of page (folio-326 marker)",
      "p. 325 ends with the display '... = λ^p(x+p-1) .'; p. 326 begins '3.3. Soient K, K' deux λ-anneaux' (main scan of p. 325; witness of p. 326, crops_321_325/w_337_top.png)",
      "'\\textbf{3.3.}' is the last line of page_325.tex; the folio-326 marker stands between it and 'Soient'",
      "marker", "high", None,
      "Page 326 really begins with '\\textbf{3.3.}' (a heading at the top of a page, not moved by the script). python -I move_marker.py 6 326 '\\textbf{3.3.}' --before (simulated in memory on both layers with crops_321_325/sim_markers.py: '\\]' / blank line / the marker / '\\textbf{3.3.}' / 'Soient ...'). The checker of p. 326 may report the same boundary: apply once."),
]

# fix the tex field of the λ_u label entry (built with a replace above for readability)
findings[4]["tex"] = r'\arrow[r,"\lambda_u"' + "'] (label set below the arrow)"

ok = True
for f in findings:
    fx = f["fix"]
    if fx is None:
        continue
    t = (B / f"page_{f['page']}.tex").read_text(encoding="utf-8")
    n = t.count(fx["old"])
    if n != 1 or "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]:
        ok = False
        print("BAD", f["page"], n, repr(fx["old"]))
print("all olds unique:", ok, "| findings:", len(findings))
counts = {}
for f in findings:
    c = counts.setdefault(f["page"], [0, 0])
    c[1 if f["kind"] == "misprint_in_print" else 0] += 1
print(counts)
if ok:
    OUT.write_text(json.dumps(findings, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("written", OUT)
