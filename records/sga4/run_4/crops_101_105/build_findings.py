import json
import os

RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_4"
PAGES = os.path.join(RUN, "b101_105")
OUT = os.path.join(RUN, "findings_101_105.json")

findings = [
    {
        "page": 101,
        "where": "Proof of 8.8.2, first sentence: 'et tout objet phi de ...'",
        "scan": "et tout objet \u03c6 de Hom(C,J) [Hom underlined], l'application canonique",
        "tex": "et tout objet $\\varphi$ de $\\Hhom(C,J)$, l'application",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "$\\Hhom(J,C)$",
        "note": "The print has Hom(C,J), a slip for Hom(J,C): phi, like the phi_i, is a functor J -> C (Hom(phi,phi_i) is formed in Hom(J,C)). The TeX keeps the printed reading."
    },
    {
        "page": 101,
        "where": "Proof of 8.8.2, after (8.8.2.1): 'la limite inductive prise dans ...'",
        "scan": "la limite inductive prise dans Hom(J,Ind(C)) [Hom NOT underlined]",
        "tex": "prise dans $\\Hom(J,\\Ind(C))$",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "$\\Hhom(J,\\Ind(C))$",
        "note": "The print omits the underline under Hom here, although the limit is taken in the functor category, written with underlined Hom in 8.8.1 and in 8.8.4 b) (TeX \\Hhom(J,\\Ind(C)) there). The TeX keeps the print's plain Hom."
    },
    {
        "page": 101,
        "where": "Prop. 8.8.3 a), end: 'de source dans Hom(J,C)) est filtrante'",
        "scan": "de but \u03c6 et de source dans Hom(J,C)) est filtrante. [Hom underlined, separately from the words; (J,C) not underlined]",
        "tex": "et de source dans\n$\\Hom(J,C)$) est filtrante.",
        "kind": "symbol",
        "confidence": "high",
        "fix": {"old": "$\\Hom(J,C)$) est filtrante", "new": "$\\Hhom(J,C)$) est filtrante"},
        "note": "The print underlines this Hom (the functor category, as in the two other Hom of the same sentence, which the TeX gives as \\Hhom); the TeX has the plain \\Hom."
    },
    {
        "page": 102,
        "where": "Prop. 8.8.3 b), line after (8.8.3.1)",
        "scan": "est cofinal, i.e. satisfaisant aux conditions F 1), F 2) de 8.1.3.",
        "tex": "est cofinal. \\ie satisfaisant aux conditions",
        "kind": "punctuation",
        "confidence": "high",
        "fix": {"old": "est cofinal. \\ie", "new": "est cofinal, \\ie"},
        "note": "The print has a comma after 'cofinal'; the TeX's full stop cuts the sentence and leaves 'i.e. satisfaisant ...' as a fragment."
    },
    {
        "page": 102,
        "where": "Proof of 8.8.3, after the display lim_I psi_i(j) -> phi(j)",
        "scan": "d\u00e9duit du foncteur (8.8.3.1). Comme de dernier est cofinal,",
        "tex": "d\u00e9duit du foncteur (8.8.3.1). Comme %%\nce dernier est cofinal,",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "ce dernier",
        "note": "Typing error 'de dernier' in the print; the TeX silently corrects it to 'ce dernier'."
    },
    {
        "page": 103,
        "where": "Lemme 8.8.3.4, line after the display f_j : I -> I_j",
        "scan": "une petite famille de foncteur cofinaux de I",
        "tex": "une petite famille de foncteur cofinaux de $I$",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "foncteurs cofinaux",
        "note": "Missing plural s in the print ('foncteur cofinaux'); the TeX keeps the printed reading."
    },
    {
        "page": 104,
        "where": "First line after the display psi : I -> E_{/phi}",
        "scan": "d\u00e9duit du ind-objet \u03c6 de E index\u00e9 par I,",
        "tex": "d\u00e9duit\\pageoriginale de ind-objet $\\varphi$ de $E$",
        "kind": "word",
        "confidence": "high",
        "fix": {"old": "de ind-objet", "new": "du ind-objet"},
        "note": "The print reads 'du ind-objet'; the TeX has 'de ind-objet'."
    },
    {
        "page": 104,
        "where": "Heading of 8.8.4",
        "scan": "Remarques 8.8.4. a) Dans le cas o\u00f9 ...",
        "tex": "\\begin{enonce*}[remark]{Remarque 8.8.4}",
        "kind": "word",
        "confidence": "high",
        "fix": {"old": "{Remarque 8.8.4}", "new": "{Remarques 8.8.4}"},
        "note": "The print's heading is plural (two remarks a) and b)); the TeX has the singular. The edition keeps the plural elsewhere (Remarques 8.9.4)."
    },
    {
        "page": 105,
        "where": "Lemme 8.8.5.1, line 2",
        "scan": "J' et J\" deux sous-cat\u00e9gories pleine telles que",
        "tex": "deux sous-cat\u00e9gories\npleine telles que",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "pleines",
        "note": "Missing agreement s in the print ('sous-cat\u00e9gories pleine'); the TeX keeps the printed reading."
    },
    {
        "page": 105,
        "where": "Lemme 8.8.5.1, lines 2-3: 'pour tout j' in Ob J' et ...'",
        "scan": "pour tout j'\u2208 Ob J' et J\" \u2208 Ob J\", on ait Hom(j\",j') = \u2205 [capital J\" before \u2208]",
        "tex": "$j'\\in \\Ob J'$ et $J''\\in \\Ob J''$, on ait\n$\\Hom(j'',j')=\u2205$",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "$j''\\in \\Ob J''$",
        "note": "The print has a capital J\" for the object j\" (the object used in Hom(j\",j') and parallel to j' in Ob J'); the TeX keeps the printed capital."
    },
]

ok = True
for f in findings:
    if f["fix"] is None:
        continue
    path = os.path.join(PAGES, "page_%03d.tex" % f["page"])
    with open(path, encoding="utf-8", newline="") as fh:
        lines = fh.read().split("\n")
    body = "\n".join(lines[1:])  # skip the comment line
    full = "\n".join(lines)
    old = f["fix"]["old"]
    n_body = body.count(old)
    n_full = full.count(old)
    print(f["page"], repr(old), "body:", n_body, "full:", n_full)
    if n_body != 1 or n_full != 1:
        ok = False

# also check that quoted TeX snippets (tex field) occur, for sanity
for f in findings:
    path = os.path.join(PAGES, "page_%03d.tex" % f["page"])
    with open(path, encoding="utf-8", newline="") as fh:
        full = fh.read()
    t = f["tex"]
    print("tex-check", f["page"], full.count(t), repr(t[:40]))

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=2)
    fh.write("\n")
print("written", OUT, "ok" if ok else "UNIQUENESS PROBLEM")
