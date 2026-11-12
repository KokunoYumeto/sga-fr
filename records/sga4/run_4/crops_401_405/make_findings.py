import json
import pathlib

L = chr(10)
BASE = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_4")
PAGES = BASE / "b401_405"
OUT = BASE / "findings_401_405.json"

conv_phi = (r"The print has the empty-set sign; \phi prints the Greek letter phi (macros.tex does not redefine \phi; "
            r"it lets \emptyset be \varnothing). Exposé IV writes \phi for the empty set throughout "
            r"(convention, reported once in the coordinator message).")

findings = [
    {
        "page": 401,
        "where": "Exercice 6.9 c), end of line 1 / start of line 2 of c)",
        "scan": "que pour toute partie I' de I de foncteur phi_{I'} sur C proreprésenté ...",
        "tex": r"que pour toute partie $I'$ de $I$" + L + r"le foncteur $\varphi_{I'}$ sur $C$",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "le foncteur",
        "note": "Typing error of the print: 'de foncteur' for 'le foncteur'. The TeX silently corrects it to 'le foncteur'.",
    },
    {
        "page": 401,
        "where": "Exercice 6.9 d), line 2",
        "scan": "Fib(C) ≊ Fib(C) (both sides identical, Fib underlined; no trace of a tilde over either C)",
        "tex": r"$\Ffib(C)\approxeq \Ffib(C)$",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": r"\Ffib(C)\approxeq \Ffib(C^{\sim})",
        "note": (r"The print states the tautology 'Fib(C) ≊ Fib(C)'; presumably one side is the category of fibre functors "
                 r"on the topos, Fib(C^~), cf. the equivalence \Ffib(C^{\sim})\xrightarrow{\approx}\Ffib(C) of 6.3 "
                 r"(04.tex line 3532); which side carries the tilde cannot be read from the page. The TeX keeps the printed reading."),
    },
    {
        "page": 401,
        "where": "Exercice 6.10, line 3",
        "scan": "Fais(C,D) la catégorie des faisceaux sur C à valeurs dans F (II 6.1)).",
        "tex": r"$\Fais(C,D)$ la catégorie des" + L + r"faisceaux sur $C$ à valeurs dans $F$",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": r"à valeurs dans $D$",
        "note": ("The print reads 'à valeurs dans F'; Fais(C,D) is the category of sheaves on C with values in D "
                 "(F only appears afterwards, as a sheaf, in (6.10.1)). The TeX keeps the printed 'F'."),
    },
    {
        "page": 401,
        "where": "Exercice 6.10, line 3, reference to II 6.1",
        "scan": "(II 6.1)). Définir",
        "tex": r"(\hyperrefext[II][II.def6.1]{6.1}). Définir",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": r"(\hyperrefext[II][II.def6.1]{6.1}).",
        "note": "The print closes the parenthesis twice, with no matching opening parenthesis; the TeX silently drops the extra ')'.",
    },
    {
        "page": 402,
        "where": "formula (7.1.4), index of lim",
        "scan": "F_Z = lim-> over U∩Z≠∅ F(U) , (handwritten empty-set sign)",
        "tex": r"F_Z=\varinjlim_{U\cap Z\neq \phi} F(U){\quoi},",
        "kind": "symbol",
        "confidence": "medium",
        "fix": {"old": r"U\cap Z\neq \phi}", "new": r"U\cap Z\neq \emptyset}"},
        "note": conv_phi,
    },
    {
        "page": 404,
        "where": "7.1.7, line 1",
        "scan": "On vient de voir comment on peut réconstituer un espace sobre X",
        "tex": r"On vient de voir comment on peut reconstituer un espace sobre $X$",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "reconstituer",
        "note": "Spelling error of the typescript ('réconstituer', with an accent); the TeX silently corrects it to 'reconstituer'.",
    },
    {
        "page": 404,
        "where": "7.1.7, sentence 'D'après ce qui a été dit dans 2.1'",
        "scan": "D'après ce qui a été dit dans 2.1, on réconstitue également la topologie de X",
        "tex": r"on reconstitue également la topologie",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "reconstitue",
        "note": "Same spelling error of the typescript ('réconstitue'); the TeX silently corrects it to 'reconstitue'.",
    },
    {
        "page": 404,
        "where": "7.1.7, definition of Pt(U)",
        "scan": "l'ensemble des x ∈ X tels que U_x ≠ ∅ (typed empty-set sign)",
        "tex": r"l'ensemble des $x\in X$ tels que $U_x\neq\phi$",
        "kind": "symbol",
        "confidence": "medium",
        "fix": {"old": r"U_x\neq\phi", "new": r"U_x\neq\emptyset"},
        "note": conv_phi,
    },
    {
        "page": 405,
        "where": "Exercice 7.1.10 b), the Bourbaki reference",
        "scan": "(Bourbaki, Top. Gen. Chap. III § 4)",
        "tex": r"(Bourbaki," + L + r"Top. Gen. Chap. \hyperrefext[III][III.sec4]{4})",
        "kind": "symbol",
        "confidence": "high",
        "fix": {"old": r"Chap. \hyperrefext[III][III.sec4]{4})", "new": r"Chap. III \S 4)"},
        "note": (r"\hyperrefext[III][III.sec4]{4} prints 'III 4' (macros.tex: \hyperref[#2]{#1 #3}), so the TeX loses the § sign "
                 r"and makes the reference a link to SGA 4 Exposé III § 4, whereas the print cites Bourbaki, Topologie générale, "
                 r"Chap. III § 4. The fix restores the § and drops the wrong link (04.tex writes § as \S, line 1040 '\S 12')."),
    },
]

# checks: every fix's old occurs exactly once in its page file (never in the comment line); no control characters
ok = True
for f in findings:
    for key in ("where", "scan", "tex", "note", "corrected"):
        v = f.get(key)
        if isinstance(v, str) and any(ord(c) < 32 and c != L for c in v):
            print("control character in", f["page"], key)
            ok = False
    if f["fix"] is None:
        continue
    text = (PAGES / f"page_{f['page']}.tex").read_text(encoding="utf-8")
    body = text.split(L, 1)[1]
    n_all = text.count(f["fix"]["old"])
    n_body = body.count(f["fix"]["old"])
    print(f["page"], repr(f["fix"]["old"]), "occurrences:", n_all, "outside comment line:", n_body)
    if n_all != 1 or n_body != 1:
        ok = False
    if any(ord(c) < 32 and c != L for c in f["fix"]["old"] + f["fix"]["new"]):
        print("control character in fix", f["page"])
        ok = False

with open(OUT, "w", encoding="utf-8", newline=L) as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
    fh.write(L)

back = json.loads(OUT.read_text(encoding="utf-8"))
print("written", len(back), "findings; checks ok:", ok)
from collections import Counter
c = Counter((x["page"], x["kind"] == "misprint_in_print") for x in back)
for p in (401, 402, 403, 404, 405):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
