import json
import pathlib

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I")
BATCH = RUN / "b036_040"
OUT = RUN / "findings_036_040.json"

F = []

# ---------------- page 37 ----------------
F.append(dict(
    page=37,
    where="Proposition 1.5 (1), first line, 'be a π_1-map.'",
    scan="be a  π_1-map. : 'be a' and 'map' are underlined; π_1 and the hyphen are not",
    tex=r"\underline{$\pi_1$-map.}",
    kind="underline",
    confidence="medium",
    fix={"old": r"\underline{$\pi_1$-map.}", "new": r"$\pi_1$-\underline{map.}"},
    note="In both scans the underline starts under the m of 'map'; as elsewhere in the typescript, the symbol is "
         "left out of the underlining.",
))

F.append(dict(
    page=37,
    where="Proof of 1.5 (1), 'the composite map R --h--> R ×_h k[ε] --π_1--> R is the identity'",
    scan="R --h--> R × k[ε] --π_1--> R with h (not k) under the ×; one line up the same fibre product has k under its ×",
    tex=r"R \underset{k}{\times} k[\epsilon] \xrightarrow{\ \pi_1\ } R",
    kind="misprint_in_print",
    confidence="high",
    fix={"old": r"\underset{k}{\times} k[\epsilon] \xrightarrow{\ \pi_1\ }",
         "new": r"\underset{h}{\times} k[\epsilon] \xrightarrow{\ \pi_1\ }"},
    corrected=r"\underset{k}{\times} k[\epsilon] \xrightarrow{\ \pi_1\ }",
    note="The fibre product is over k (h : R → R ×_k k[ε] in the previous sentence). The print has h under the ×, "
         "clear in the scan and in the DjVu witness. The TeX silently corrects it, and so does the corrected layer. "
         "The fix restores the printed h. 'corrected' is the current TeX.",
))

F.append(dict(
    page=37,
    where="Proof of 1.5 (1), 'we get maps a ⇄ f_*a (γ above, α_1 below) such that α_1·γ = 1_a where P(γ) = h'",
    scan="maps  a ⇄ f_*a  (f, not h)",
    tex=r"{\rightleftarrows}} f_* a$",
    kind="misprint_in_print",
    confidence="high",
    fix=None,
    corrected=r"{\rightleftarrows}} h_* a$",
    note="γ lies over P(γ) = h, so its target is h_*a, the object used in the following lines ('h_*a ⟶ (π_2)_*a'', "
         "'u : h_*a ⟶ a''); f is not defined in part (1). Same in the DjVu witness. The TeX keeps the printed "
         "reading, as does the corrected layer. 'corrected' replaces the 'tex' substring.",
))

F.append(dict(
    page=37,
    where="Proposition 1.5 (2), left diamond, right-hand node of the middle row",
    scan="a' (prime, no subscript): the target of α'_1 and the source of α_1",
    tex="a' \\arrow[dl, \"\\alpha_1\"]",
    kind="misprint_in_print",
    confidence="medium",
    fix=None,
    corrected="a'_1 \\arrow[dl, \"\\alpha_1\"]",
    note="The node carries α'_1 : a'' → (node) and α_1 : (node) → a, and the proof builds γ = α'_1·γ' from a' to it "
         "with α_1·γ = α. It is the a'_1 of Definition 1.4 (2) on p. 36 (the versality being proved), and the "
         "matching node of Corollary 1.6 on p. 38 is a_1. Same in the DjVu witness. The TeX keeps the printed "
         "reading, as does the corrected layer. Goes together with the two 'γ : a' ⟶ a' corrections on this page. "
         "'corrected' replaces the 'tex' substring.",
))

F.append(dict(
    page=37,
    where="Proposition 1.5 (2), end of the statement, 'then there exists a map γ: a' ⟶ a such that α = α_1·γ'",
    scan="γ: a' ⟶ a",
    tex=r"$\gamma: a' \longrightarrow a$",
    kind="misprint_in_print",
    confidence="medium",
    fix=None,
    corrected=r"$\gamma: a' \longrightarrow a'_1$",
    note="α_1·γ is defined only if γ lands in the source of α_1, the right-hand node of the diamond (a'_1, see the "
         "diagram finding); with target a it does not compose with α_1. Same in the DjVu witness. The TeX keeps the "
         "printed reading, as does the corrected layer. Goes together with the diamond node and the proof's "
         "'Define γ : a' ⟶ a'. 'corrected' replaces the 'tex' substring.",
))

F.append(dict(
    page=37,
    where="Proof of 1.5 (2), first line, 'The map 1 × f̃ : R' ×_R h' ⟶ R' ×_k k[Ker f]'",
    scan="1 × f̃ : R' ×_R h' ⟶ R' ×_k k[Ker f]",
    tex=r"R' \underset{R}{\times} h' \longrightarrow",
    kind="misprint_in_print",
    confidence="high",
    fix=None,
    corrected=r"R' \underset{R}{\times} R' \longrightarrow",
    note="f̃ is defined on R' ×_R R' (statement of (2)), so 1 × f̃ starts from R' ×_R R'. Same in the DjVu witness. "
         "The TeX keeps the printed reading, as does the corrected layer. 'corrected' replaces the 'tex' substring.",
))

F.append(dict(
    page=37,
    where="Proof of 1.5 (2), 'We note that k[Ker f] ≃ k[ε]'",
    scan="k[Ker f] ≃ k[ε]: a tilde over a single bar, the same sign as 'Ker f ≃ k' in Definition 1.4 (p. 36)",
    tex=r"k[\mathrm{Ker}\ f] \cong k[\epsilon]",
    kind="symbol",
    confidence="high",
    fix={"old": r"\mathrm{Ker}\ f] \cong k[\epsilon]", "new": r"\mathrm{Ker}\ f] \simeq k[\epsilon]"},
    note="One bar under the tilde in both scans; the TeX gives the same printed sign as \\simeq on p. 36.",
))

F.append(dict(
    page=37,
    where="Proof of 1.5 (2), 'a' ⟶ (f̃)_*a'' = (π_2)_*[(1 f̃)_*a'']'",
    scan="[(1 f̃)_*a''] : nothing between 1 and f̃",
    tex=r"[(1\ \tilde{f})_* a'']",
    kind="misprint_in_print",
    confidence="high",
    fix=None,
    corrected=r"[(1 \times \tilde{f})_* a'']",
    note="The map is 1 × f̃, introduced two lines up (π_2·(1×f̃) = f̃). Same in the DjVu witness. The TeX keeps the "
         "printed reading, as does the corrected layer. 'corrected' replaces the 'tex' substring.",
))

F.append(dict(
    page=37,
    where="Proof of 1.5 (2), 'Define γ : a' ⟶ a by γ = α'_1·γ''",
    scan="Define  γ : a' ⟶ a  by  γ = α'_1·γ'",
    tex=r"$\gamma : a' \longrightarrow a$ by",
    kind="misprint_in_print",
    confidence="medium",
    fix=None,
    corrected=r"$\gamma : a' \longrightarrow a'_1$ by",
    note="γ' : a' → a'' and α'_1 : a'' → a'_1, so γ = α'_1·γ' maps a' to a'_1 (and then α_1·γ = α). Same in the "
         "DjVu witness. The TeX keeps the printed reading, as does the corrected layer. Goes together with the "
         "diamond node and the statement's 'γ: a' ⟶ a'. 'corrected' replaces the 'tex' substring.",
))

# ---------------- page 38 ----------------
F.append(dict(
    page=38,
    where="Corollary 1.6, 'Then there exists a map a' --ρ-- a_1 such that α = α_1ρ'",
    scan="a' —ρ— a_1 : a plain rule with ρ on it and no arrowhead",
    tex=r"$a' \xrightarrow{\ \rho\ } a_1$",
    kind="misprint_in_print",
    confidence="medium",
    fix={"old": r"a' \xrightarrow{\ \rho\ } a_1",
         "new": r"a' \overset{\ \rho\ }{\relbar\joinrel\relbar\joinrel\relbar} a_1"},
    corrected=r"a' \xrightarrow{\ \rho\ } a_1",
    note="The head was never drawn: the rule ends cleanly in the IA scan and in the DjVu witness (not a broken "
         "stroke); the same ρ has its head in the diagram at the top of p. 40. The TeX silently supplies the head. "
         "The fix restores the printed headless rule (\\relbar and \\joinrel are the kernel's pieces of "
         "\\longrightarrow); 'corrected' is the current TeX.",
))

F.append(dict(
    page=38,
    where="Definition 1.7, 'where m_Λ M are the maximal ideals of Λ , R respectively'",
    scan="m̲_Λ : the underline is under the m only (the maximal-ideal notation, like m̲_i on p. 40); the subscript Λ is outside it",
    tex=r"\underline{$m_{\Lambda}$}",
    kind="underline",
    confidence="low",
    fix={"old": r"\underline{$m_{\Lambda}$} $M$", "new": r"$\underline{m}_{\Lambda}$ $M$"},
    note="Same form as \\underline{C}_{\\Lambda} and \\underline{m}_i elsewhere in the TeX. Apply before the "
         "missing-comma misprint below, whose 'tex' is the text after this fix.",
))

F.append(dict(
    page=38,
    where="Definition 1.7, 'where m_Λ M are the maximal ideals of Λ , R respectively'",
    scan="where  m̲_Λ  (line end) / M  are the maximal ideals of  Λ , R  respectively : no comma between m̲_Λ and M",
    tex=r"$\underline{m}_{\Lambda}$ $M$",
    kind="misprint_in_print",
    confidence="low",
    fix=None,
    corrected=r"$\underline{m}_{\Lambda}$ , $M$",
    note="The two ideals are listed in parallel with 'of Λ , R respectively'. Same in the DjVu witness. The TeX "
         "keeps the printed reading. 'tex' is the text after the underline fix above (before it: "
         "'\\underline{$m_{\\Lambda}$} $M$'); 'corrected' replaces it.",
))

# ---------------- page 39 ----------------
F.append(dict(
    page=39,
    where="Proposition 1.8 (ii), 'p(a') ⟶ p(a) is surjective; and the kernel is annihilated by the maximal ideal of p(a)'",
    scan="p(a') ⟶ p(a) ... p(a): lower-case p three times",
    tex=r"(ii)  $p(a')$ $\longrightarrow$ $p(a)$  \underline{is surjective; and the kernel is annihilated by the maximal ideal of}  $p(a)$",
    kind="misprint_in_print",
    confidence="medium",
    fix=None,
    corrected=r"(ii)  $P(a')$ $\longrightarrow$ $P(a)$  \underline{is surjective; and the kernel is annihilated by the maximal ideal of}  $P(a)$",
    note="The structure functor is the capital P everywhere else (Corollary 1.6; 'Set R = P(a)' in this proof). "
         "Same in the DjVu witness. The TeX keeps the printed reading, as does the corrected layer. 'corrected' "
         "replaces the 'tex' substring.",
))

F.append(dict(
    page=39,
    where="proof of 1.8, 'by the definiton of the ideal J''",
    scan="by the definiton of the ideal  J'",
    tex="the definiton of the ideal",
    kind="misprint_in_print",
    confidence="high",
    fix=None,
    corrected="the definition of the ideal",
    note="Typing error. The TeX keeps the printed reading, as does the corrected layer. 'corrected' replaces the "
         "'tex' substring.",
))

F.append(dict(
    page=39,
    where="proof of 1.8, 'Therefore in either cases we obtain a commutative diagram'",
    scan="Therefore in either cases we obtain a commutative diagram",
    tex="in either cases we obtain",
    kind="misprint_in_print",
    confidence="low",
    fix=None,
    corrected="in either case we obtain",
    note="'either' takes the singular. The TeX keeps the printed reading. Low: a slip of the English, not of the "
         "mathematics. 'corrected' replaces the 'tex' substring.",
))

F.append(dict(
    page=39,
    where="proof of 1.8, triangle S/J' --f-- R_1 over R",
    scan="S/J' —f— R_1 : a plain rule with f above it and no arrowhead (the two diagonals π', π_1 have heads)",
    tex="S/J' \\arrow[rr, \"f\"]",
    kind="misprint_in_print",
    confidence="medium",
    fix={"old": "S/J' \\arrow[rr, \"f\"]", "new": "S/J' \\arrow[rr, \"f\", no head]"},
    corrected="S/J' \\arrow[rr, \"f\"]",
    note="f : S/J' → R_1 is the map just constructed ('h_1 induces f : S/J' → R_1'). The rule ends plainly in the IA "
         "scan and in the DjVu witness. The TeX silently supplies the head. The fix restores the printed headless "
         "rule ('no head' is the tikz-cd key); 'corrected' is the current TeX.",
))

# ---------------- checks ----------------
texts = {}
for n in (36, 37, 38, 39, 40):
    texts[n] = (BATCH / f"page_{n:03d}.tex").read_text(encoding="utf-8")

ok = True
post = dict(texts)  # page text after applying the fixes in list order
for f in F:
    t = texts[f["page"]]
    if f["fix"] is not None:
        old = f["fix"]["old"]
        c = t.count(old)
        if c != 1:
            ok = False
            print("FIX OLD COUNT", c, f["page"], repr(old))
        if "%%%%%%%%%%" in old:
            ok = False
            print("MARKER IN OLD", f["page"])
        post[f["page"]] = post[f["page"]].replace(old, f["fix"]["new"], 1)
for f in F:
    if f["kind"] == "misprint_in_print":
        if f["fix"] is None:
            c = post[f["page"]].count(f["tex"])
            if c != 1:
                ok = False
                print("MISPRINT TEX COUNT (post-fix)", c, f["page"], repr(f["tex"]))
        else:
            # silent correction: 'corrected' must equal the text the fix replaces
            if f["corrected"] not in texts[f["page"]]:
                ok = False
                print("CORRECTED NOT IN CURRENT TEX", f["page"], repr(f["corrected"]))
    else:
        if "corrected" in f:
            ok = False
            print("CORRECTED ON NON-MISPRINT", f["page"])
        c = texts[f["page"]].count(f["tex"])
        if c < 1:
            ok = False
            print("TEX NOT FOUND", f["page"], repr(f["tex"]))

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
print("written", OUT, len(F), "findings; checks", "OK" if ok else "FAILED")
for n in (36, 37, 38, 39, 40):
    norm = sum(1 for f in F if f["page"] == n and f["kind"] != "misprint_in_print")
    mis = sum(1 for f in F if f["page"] == n and f["kind"] == "misprint_in_print")
    print(n, f"{norm}/{mis}")
