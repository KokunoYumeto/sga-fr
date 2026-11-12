# Builds findings_406_410_recheck.json and checks every fix against the page files.
import json, os, sys

RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II"
PAGES = os.path.join(RUN, "b406_410")
OUT = os.path.join(RUN, "findings_406_410_recheck.json")

def F(page, where, scan, tex, kind, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d

findings = [
# ---------------- 406
F(406, "Proposition 2.0, heading",
  "Proposition 2.0. (only the word Proposition underlined)",
  r"\underline{Proposition 2.0.}", "underline", "high",
  r"\underline{Proposition 2.0.}", r"\underline{Proposition} 2.0.",
  "The number is not underlined."),
F(406, "Proposition 2.0, statement",
  "Soit / un schéma propre sur un corps / séparablement clos, et désignons par underlined; X̄ and k not underlined",
  r"one \underline over the whole statement, including $\bar X$ and $k$", "underline", "high",
  r"""\underline{Soit $\bar X$ un schéma propre sur
un corps $k$ séparablement clos, et désignons par}""",
  r"""\underline{Soit} $\bar X$ \underline{un schéma propre sur
un corps} $k$ \underline{séparablement clos, et désignons par}""",
  "The underline breaks at each math letter."),
F(406, "after (2.0.1), 'l'application p-linéaire induite par'",
  "l'application and linéaire induite par underlined; p- not underlined",
  r"\underline{l'application $p$-linéaire induite par}", "underline", "high",
  r"\underline{l'application $p$-linéaire induite par}",
  r"\underline{l'application} $p$-\underline{linéaire induite par}",
  ""),
F(406, "statement after the display of H^·_et, second line",
  "ℤ/pℤ. not underlined; the underline resumes at Alors",
  r"constant $\mathbb Z/p\mathbb Z$. Alors ... :} inside one \underline", "underline", "high",
  r"constant $\mathbb Z/p\mathbb Z$. Alors on a des isomorphismes canoniques :}",
  r"constant} $\mathbb Z/p\mathbb Z$. \underline{Alors on a des isomorphismes canoniques :}",
  "The colon stays inside the underline (global rule)."),
F(406, "last paragraph, 'de dimension finie X̄ étant propre'",
  "de dimension finie X̄ étant propre (no comma)",
  r"\underline{de dimension finie}" + "\n" + r"$\bar X$ étant propre", "misprint_in_print", "medium",
  None, None,
  "The comma before the participial clause is missing in the print. The TeX keeps the printed reading.",
  corrected=r"\underline{de dimension finie}, $\bar X$ étant propre"),
# ---------------- 407
F(407, "Corollaire 2.1, heading",
  "Corollaire 2.1. (only the word Corollaire underlined)",
  r"\underline{Corollaire 2.1.}", "underline", "high",
  r"\underline{Corollaire 2.1.}", r"\underline{Corollaire} 2.1.",
  "The number is not underlined."),
F(407, "Corollaire 2.1, statement",
  "Pour / propre sur un corps séparablement clos underlined; X̄ and k, not underlined",
  r"\underline{Pour $\bar X$ ... clos $k$,}", "underline", "high",
  r"""\underline{Pour $\bar X$ propre sur un corps
séparablement clos $k$,}""",
  r"""\underline{Pour} $\bar X$ \underline{propre sur un corps
séparablement clos} $k$,""",
  ""),
F(407, "Proposition 2.2.4, heading",
  "Proposition 2.2.4. (only the word Proposition underlined)",
  r"\underline{Proposition 2.2.4.}", "underline", "high",
  r"\underline{Proposition 2.2.4.}", r"\underline{Proposition} 2.2.4.",
  "The number is not underlined."),
F(407, "Proposition 2.2.4, statement",
  "Désignons par / l'élément de / Frobenius / et soit / On a une identité de polynômes caractéristiques underlined; φ_q ∈ Gal(k/𝔽_q), the quotation marks, φ_q(λ) = λ^q and i ∈ ℤ . not underlined",
  "one \\underline over the whole statement, including the formulas and the quotation marks", "underline", "high",
  r"""\underline{Désignons par
$\varphi_q\in\Gal(k/\mathbb F_q)$ l'élément de ``Frobenius'',
$\varphi_q(\lambda)=\lambda^q$ et soit $i\in\mathbb Z$. On a une identité de
polynômes caractéristiques}""",
  r"""\underline{Désignons par}
$\varphi_q\in\Gal(k/\mathbb F_q)$ \underline{l'élément de} ``\underline{Frobenius}'',
$\varphi_q(\lambda)=\lambda^q$ \underline{et soit} $i\in\mathbb Z$. \underline{On a une identité de
polynômes caractéristiques}""",
  "The underline of Frobenius stops before each quotation mark."),
F(407, "after (2.2.4.1), 'où le premier membre ...'",
  "φ_q^{-1}, π_1(Sp(𝔽_q)) and H^i(X̄,ℤ/pℤ). not underlined; dans and agissant sur le module galoisien underlined",
  "one \\underline over the whole sentence, including the formulas", "underline", "high",
  r"""\underline{où le premier membre est le polynôme caractéristique de l'élément
$\varphi_q^{-1}$ dans $\pi_1(\operatorname{Sp}(\mathbb F_q))$ agissant sur le
module galoisien $H^i(\bar X,\mathbb Z/p\mathbb Z)$.}""",
  r"""\underline{où le premier membre est le polynôme caractéristique de l'élément}
$\varphi_q^{-1}$ \underline{dans} $\pi_1(\operatorname{Sp}(\mathbb F_q))$ \underline{agissant sur le
module galoisien} $H^i(\bar X,\mathbb Z/p\mathbb Z)$.""",
  ""),
# ---------------- 408
F(408, "Proposition 2.2.5, heading",
  "Proposition 2.2.5. (only the word Proposition underlined)",
  r"\underline{Proposition 2.2.5.}", "underline", "high",
  r"\underline{Proposition 2.2.5.}", r"\underline{Proposition} 2.2.5.",
  "The number is not underlined."),
F(408, "Proposition 2.2.5, first sentence",
  "Soit / propre sur / Il y a un isomorphisme canonique underlined; X and Spec(𝔽_q) . not underlined",
  r"\underline{Soit $X$ propre sur $\Spec(\mathbb F_q)$. Il y a ...}", "underline", "high",
  r"""\underline{Soit $X$ propre sur
$\Spec(\mathbb F_q)$. Il y a un isomorphisme canonique}""",
  r"""\underline{Soit} $X$ \underline{propre sur}
$\Spec(\mathbb F_q)$. \underline{Il y a un isomorphisme canonique}""",
  ""),
F(408, "Proposition 2.2.5, 'qui transforme ... du premier membre en l'automorphisme'",
  "qui transforme l'automorphisme / du premier membre en l'automorphisme underlined; 𝔉_q⊗_{𝔽_q}k not underlined",
  "one \\underline from 'qui transforme' to 'Frobenius.', including all formulas", "underline", "high",
  r"""\underline{qui transforme l'automorphisme
$\mathfrak F_q\otimes_{\mathbb F_q}k$ du premier membre en l'automorphisme
$\varphi_q^{-1}""",
  r"""\underline{qui transforme l'automorphisme}
$\mathfrak F_q\otimes_{\mathbb F_q}k$ \underline{du premier membre en l'automorphisme}
$\varphi_q^{-1}""",
  "Apply together with the next edit (the two halves of one underline; the misprinted subscript between them stays untouched, so both edits fit both layers)."),
F(408, "Proposition 2.2.5, 'du second (qu'on peut ... de Frobenius.'",
  "du second / qu'on peut aussi interpréter comme l'endomorphisme / où / est le / endomorphisme de Frobenius. underlined; the parenthesis, fr_q^{X*}⊗_{𝔽_p}k, , fr_q^X : X̄ → X̄ and k- not underlined",
  "same \\underline as the previous finding", "underline", "high",
  r"""k$ du second (qu'on peut aussi interpréter
comme l'endomorphisme $\mathrm{fr}_q^{X*}\otimes_{\mathbb F_p}k$, où
$\mathrm{fr}_q^X:\bar X\longrightarrow\bar X$ est le $k$-endomorphisme de
Frobenius.}""",
  r"""k$ \underline{du second} (\underline{qu'on peut aussi interpréter
comme l'endomorphisme} $\mathrm{fr}_q^{X*}\otimes_{\mathbb F_p}k$, \underline{où}
$\mathrm{fr}_q^X:\bar X\longrightarrow\bar X$ \underline{est le} $k$-\underline{endomorphisme de
Frobenius.}""",
  "Apply together with the previous edit."),
F(408, "Proposition 2.2.5, 'l'automorphisme φ_q^{-1}⊗ k du second'",
  "φ_q^{-1} ⊗_{𝔽_q} k",
  r"\varphi_q^{-1}\otimes_{\mathbb F_q}k", "misprint_in_print", "medium",
  None, None,
  "The second member of (2.2.6) is H^i_et(X̄,ℤ/pℤ)⊗_{𝔽_p}k, an 𝔽_p-tensor product. The TeX keeps the printed reading.",
  corrected=r"\varphi_q^{-1}\otimes_{\mathbb F_p}k"),
F(408, "before (2.2.10), '(cf. 1.0.5))'",
  "(cf. 1.0.5)) with two closing parentheses",
  "(cf. 1.0.5))", "misprint_in_print", "high",
  None, None,
  "One closing parenthesis too many in the print. The TeX keeps the printed reading.",
  corrected="(cf. 1.0.5)"),
# ---------------- 409
F(409, "after (2.2.12), 'dont les pointes fixes'",
  "pointes",
  "pointes", "misprint_in_print", "high",
  None, None,
  "Points fixes is meant. The TeX keeps the printed reading.",
  corrected="les points fixes"),
F(409, "'s'écrivent aussi ...', third operator",
  "𝔉_k ⊗ φ_k",
  r"\mathfrak F_k\otimes\varphi_k", "misprint_in_print", "medium",
  None, None,
  "With 𝔉_q = 𝔉_q⊗id_k and φ_q = id⊗φ_q, (2.2.13) gives the third operator as 𝔉_q⊗φ_q. The TeX keeps the printed reading.",
  corrected=r"\mathfrak F_q\otimes\varphi_q"),
F(409, "(2.2.14), left-hand side, exponent",
  "1-𝔉_q without bar",
  r"1-\overline{\mathfrak F}_q", "misprint_in_print", "high",
  r"""^{1-\overline{\mathfrak F}_q}
\simeq""",
  r"""^{1-\mathfrak F_q}
\simeq""",
  "The print has no bar on either exponent of (2.2.14) (nothing above the 𝔉, even at high contrast), unlike the barred 1-𝔉̄_q, 1-𝔉̄_p a few lines higher. The argument needs the fixed points of 𝔉̄_q and 𝔉̄_p (2.2.10, 2.0.1), so the bar is missing in the print. The TeX silently corrects; the corrected layer keeps the bar.",
  corrected=r"^{1-\overline{\mathfrak F}_q}"),
F(409, "(2.2.14), right-hand side, exponent",
  "1-𝔉_p without bar",
  r"1-\overline{\mathfrak F}_p", "misprint_in_print", "high",
  r"""^{1-\overline{\mathfrak F}_p}
\otimes_{\mathbb F_p}\mathbb F_q,""",
  r"""^{1-\mathfrak F_p}
\otimes_{\mathbb F_p}\mathbb F_q,""",
  "Same missing bar as the left-hand side. This edit reverses the bar added by the earlier fix of findings_406_410.json (low confidence there); the scan shows no stroke above the exponent. The corrected layer keeps the bar.",
  corrected=r"^{1-\overline{\mathfrak F}_p}"),
F(409, "'l'automorphisme φ_q de H^i(X̄,O_X̄)^{1-𝔉_q} devient, via 2.2.14'",
  "1-𝔉_q without bar",
  r"1-\overline{\mathfrak F}_q", "misprint_in_print", "high",
  r"^{1-\overline{\mathfrak F}_q}$ devient",
  r"^{1-\mathfrak F_q}$ devient",
  "Same missing bar as in (2.2.14), the line above; the next line's 1-𝔉̄_p does have its bar. The TeX silently corrects.",
  corrected=r"^{1-\overline{\mathfrak F}_q}"),
# ---------------- 410
F(410, "acknowledgement, end",
  "de (3.1.1),",
  "de (3.1.1),", "misprint_in_print", "medium",
  None, None,
  "The sentence ends with a comma in the print. The TeX keeps the printed reading.",
  corrected="de (3.1.1)."),
F(410, "Théorème 3.1, heading",
  "Théorème 3.1. (only the word Théorème underlined)",
  r"\underline{Théorème 3.1.}", "underline", "high",
  r"\underline{Théorème 3.1.}", r"\underline{Théorème} 3.1.",
  "The number is not underlined."),
F(410, "Théorème 3.1, statement",
  "Soit / un schéma propre sur / Alors underlined; X and 𝔽_q. not underlined",
  r"\underline{Soit $X$ un schéma propre sur $\mathbb F_q$. Alors}", "underline", "high",
  r"""\underline{Soit $X$ un schéma propre sur
$\mathbb F_q$. Alors}

\begin{equation}\tag{3.1.1}""",
  r"""\underline{Soit} $X$ \underline{un schéma propre sur}
$\mathbb F_q$. \underline{Alors}

\begin{equation}\tag{3.1.1}""",
  ""),
F(410, "(3.1.1), (3.1.2), (3.2.1): 'mod p'",
  "mod p (no parentheses)",
  r"\pmod p, which prints (mod p)", "formula", "high",
  None, None,
  r"Convention of the transcription for Exposé XXII (global issue 66: \pmod to \mod in the diplomatic layer); the three cases of this page: (3.1.1), (3.1.2), (3.2.1). Not changed page by page."),
F(410, "line after (3.1.1)",
  "ou, / ce qui est équivalent par underlined; (2.2.4). not underlined",
  r"\underline{ou, ce qui est équivalent par (2.2.4).}", "underline", "high",
  r"\underline{ou, ce qui est équivalent par (2.2.4).}",
  r"\underline{ou, ce qui est équivalent par} (2.2.4).",
  "The reference is not underlined. The printed full stop is a misprint (next finding); on the corrected layer the old text has the comma: \\underline{ou, ce qui est équivalent par (2.2.4),}."),
F(410, "line after (3.1.1), end",
  "(2.2.4). with a full stop before the continuing formula (3.1.2)",
  "(2.2.4).", "misprint_in_print", "medium",
  None, None,
  "The incise 'ce qui est équivalent par (2.2.4)' is closed by a full stop although the sentence continues with (3.1.2). The TeX keeps the printed reading.",
  corrected="(2.2.4),"),
F(410, "Corollaire 3.2, heading",
  "Corollaire 3.2. (only the word Corollaire underlined)",
  r"\underline{Corollaire 3.2.}", "underline", "high",
  r"\underline{Corollaire 3.2.}", r"\underline{Corollaire} 3.2.",
  "The number is not underlined."),
F(410, "Corollaire 3.2, statement",
  "Soit / un schéma propre sur underlined; X and 𝔽_q. not underlined; 'Alors' (underlined) begins a new indented line after 𝔽_q.",
  r"\underline{Soit $X$ un schéma propre sur $\mathbb F_q$. Alors} in one paragraph", "underline", "high",
  r"""\underline{Soit $X$ un schéma propre sur
$\mathbb F_q$. Alors}

\begin{equation}\tag{3.2.1}""",
  r"""\underline{Soit} $X$ \underline{un schéma propre sur}
$\mathbb F_q$.

\underline{Alors}

\begin{equation}\tag{3.2.1}""",
  "The print ends the line after 𝔽_q. and sets the underlined Alors as a new indented paragraph (unlike Théorème 3.1, where Alors runs on); the fix also makes that paragraph break."),
F(410, "(3.2.1)",
  "trace(𝔉_q|H^i(X,O_X) ≡ ... (the parenthesis after trace is never closed)",
  r"\left(\mathfrak F_q\mid H^i(X,\mathcal O_X)\right.", "misprint_in_print", "high",
  None, None,
  "One closing parenthesis is missing in the print. The TeX keeps the printed reading (\\right.).",
  corrected=r"\left(\mathfrak F_q\mid H^i(X,\mathcal O_X)\right)"),
F(410, "last line",
  "ou, / ce qui est équivalent par underlined; (2.2.4) not underlined",
  r"\underline{ou, ce qui est équivalent par (2.2.4)}", "underline", "high",
  r"\underline{ou, ce qui est équivalent par (2.2.4)}",
  r"\underline{ou, ce qui est équivalent par} (2.2.4)",
  "The reference is not underlined."),
]

# ---- checks
texts = {}
for p in (406, 407, 408, 409, 410):
    with open(os.path.join(PAGES, f"page_{p}.tex"), encoding="utf-8", newline="") as fh:
        texts[p] = fh.read()

ok = True
applied = dict(texts)
spans = {p: [] for p in texts}
for i, f in enumerate(findings):
    p = f["page"]
    if f["fix"] is None:
        continue
    old, new = f["fix"]["old"], f["fix"]["new"]
    n = texts[p].count(old)
    if n != 1:
        ok = False
        print(f"#{i} page {p}: old occurs {n} times: {old!r}")
    if "%%%%%%%%%%" in old:
        ok = False
        print(f"#{i} crosses a marker")
    s = texts[p].find(old)
    spans[p].append((s, s + len(old), i))
    if old == new:
        ok = False
        print(f"#{i} old == new")

# overlaps
for p, lst in spans.items():
    lst.sort()
    for a, b in zip(lst, lst[1:]):
        if a[1] > b[0]:
            ok = False
            print(f"page {p}: fixes #{a[2]} and #{b[2]} overlap")

# apply all fixes (in a copy) and check brace balance of \underline groups
for p in texts:
    t = texts[p]
    for f in findings:
        if f["page"] == p and f["fix"] is not None:
            assert t.count(f["fix"]["old"]) == 1, (p, f["fix"]["old"])
            t = t.replace(f["fix"]["old"], f["fix"]["new"])
    depth = 0
    for ch in t:
        if ch == "{": depth += 1
        elif ch == "}": depth -= 1
        if depth < 0: break
    if depth != 0:
        ok = False
        print(f"page {p}: unbalanced braces after applying fixes ({depth})")
    applied[p] = t
    # the original brace balance for reference
    d0 = texts[p].count("{") - texts[p].count("}")
    print(p, "brace balance before/after:", d0, t.count("{") - t.count("}"))

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

# counts
from collections import Counter
c = Counter((f["page"], f["kind"] == "misprint_in_print") for f in findings)
print("; ".join(f"{p}: {c[(p, False)]}/{c[(p, True)]}" for p in (406, 407, 408, 409, 410)))
print("OK" if ok else "PROBLEMS")
if "--show" in sys.argv:
    for p in applied:
        print("=" * 20, p)
        print(applied[p])
