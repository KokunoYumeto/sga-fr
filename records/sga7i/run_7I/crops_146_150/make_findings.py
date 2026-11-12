import json
import sys

FOLDER = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\b146_150"
OUT = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\findings_146_150.json"

F = []

F.append({
    "page": 146,
    "where": "1.3.3, last line of the page: 'qui satisfait \u00e0 la condition g.e_E = e_E.g (g \u2208 G(S). On \u00e9tend de m\u00eame la terminologie des'",
    "scan": "(g \u2208 G(S). : a single closing parenthesis, directly followed by the full stop (checked in a crop)",
    "tex": r"($g \in G(S)$.",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": r"($g \in G(S)$).",
    "note": "The parenthesis opened before g is never closed. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
})

F.append({
    "page": 148,
    "where": "1.3.4.3, third line: 'au foncteur constant de valeur la bitorseur birigidifi\u00e9 trivial sur P\u00d7P'",
    "scan": "la bitorseur",
    "tex": "de valeur la bitorseur",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "de valeur le bitorseur",
    "note": "Gender slip: 'bitorseur' is masculine ('le bitorseur trivial' in 1.3.3 and 1.3.4; 'birigidifi\u00e9 trivial' in the same phrase). The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
})

F.append({
    "page": 148,
    "where": "Proposition 1.3.5, first line: 'Soient P et Q deux Groupes de T .'",
    "scan": "Q (checked in a crop)",
    "tex": r"\underline{et} $Q$ \underline{deux Groupes de}",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": r"\underline{et} $G$ \underline{deux Groupes de}",
    "note": "Letter slip: the statement and its proof (pp. 149-150) concern P and G only (morphisms P\u00d7P -> G, extensions of P by G, bitorsors under (G_P,G_P)); Q does not occur in them, and 1.3.4 introduces 'deux Groupes P et G'. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
})

F.append({
    "page": 148,
    "where": "Proposition 1.3.5 a), fourth line: 'sur un bitorseur E sous (G_P,G_P), biridifi\u00e9 relativement \u00e0 e_P i.e. muni d'une section centrale e_E de E_1 = e*_P(E)'",
    "scan": "biridifi\u00e9 (checked in a crop)",
    "tex": r"\underline{biridifi\u00e9 relativement \u00e0}",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": r"\underline{rigidifi\u00e9 relativement \u00e0}",
    "note": "'biridifi\u00e9' is not a word. What follows 'i.e.' (a central section of E_1 = e_P^*(E)) is the rigidification of a bitorsor defined in 1.3.3, and b) says 'toute rigidification de E relativement \u00e0 e_P' and 'consid\u00e9r\u00e9 comme bitorseur rigidifi\u00e9 relativement \u00e0 e_P'; birigidifications belong to P\u00d7P. Medium: the typist may have aimed at 'birigidifi\u00e9', but the sense requires 'rigidifi\u00e9'. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
})

F.append({
    "page": 148,
    "where": "Proposition 1.3.5 b), second line: 'Soit E un torseur sous G_P .'",
    "scan": "un torseur sous G_P",
    "tex": r"\underline{un torseur sous} $G_P$",
    "kind": "misprint_in_print",
    "confidence": "low",
    "fix": None,
    "corrected": r"\underline{un bitorseur sous} $(G_P,G_P)$",
    "note": "The same statement speaks of E's 'structure de bitorseur', of central sections of E_1 and of 'E, consid\u00e9r\u00e9 comme bitorseur rigidifi\u00e9'; a) has 'un bitorseur E sous (G_P,G_P)', and the proof on p. 149 again says 'sa structure de bitorseur'. Low: possibly the author's own shorthand. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
})

F.append({
    "page": 149,
    "where": "Proof of 1.3.5 a), sixth and seventh lines: 'car les deux membres sont respectivement \u00e9gaux \u00e0 j(f(xy)) et \u00e0 j(f(x)f(y)), qui sont \u00e9gaux puisque j est multiplicatif'",
    "scan": "j(f(xy)) et \u00e0 j(f(x)f(y)) (checked in a crop)",
    "tex": r"\u00e9gaux \u00e0 $j(f(xy))$ et \u00e0 $j(f(x)f(y))$",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": r"\u00e9gaux \u00e0 $j(xy)$ et \u00e0 $j(x)j(y)$",
    "note": "j : E -> P is the structural morphism of E and does not apply to f(xy), an element of E'. Since j'f = j (f is a morphism of torsors over P) and j' is multiplicative, the two members j'f(xy) and j'(f(x)f(y)) equal j(xy) and j(x)j(y), which are equal because j is multiplicative; as printed, the sentence restates the claim. Possibly the author's own slip. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
})

F.append({
    "page": 150,
    "where": "Proof of 1.3.5 b), first paragraph: 'n'est pas n\u00e9cessairement compatible avec cette birigidification ; ces restrictions \u00e0 P\u00d7e_P et \u00e0 e_P\u00d7P s'expriment'",
    "scan": "ces restrictions (checked in a crop)",
    "tex": "ces restrictions \u00e0",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": "ses restrictions \u00e0",
    "note": "Homophone slip: the restrictions are those of the trivialization phi just named ('ses restrictions'). The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
})

F.append({
    "page": 150,
    "where": "Proof of 1.3.5 b), before the last two displays: 'sont des isomorphismes de bitorseurs sous (G_{P\u00d7P\u00d7P} , G_{P\u00d7P\u00d7P}), donc diff\u00e9rent par un morphisme central'",
    "scan": "diff\u00e9rent, with an acute accent (checked in a crop)",
    "tex": "donc diff\u00e9rent par",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": "donc diff\u00e8rent par",
    "note": "Accent slip: the verb (subject 'les deux compos\u00e9s') is 'diff\u00e8rent'; the print has the adjective's spelling. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
})

# Decode literal backslash-u-XXXX sequences left inside raw strings (LaTeX commands such as underline are untouched,
# since 'nder' is not a hex number).
import re
BS = chr(92)
PAT = re.compile(re.escape(BS) + "u([0-9a-fA-F]{4})")
def dec(v):
    if isinstance(v, str):
        return PAT.sub(lambda m: chr(int(m.group(1), 16)), v)
    if isinstance(v, dict):
        return {k: dec(w) for k, w in v.items()}
    return v
F = [dec(x) for x in F]
for x in F:
    for k in ("tex", "corrected"):
        if k in x and (BS + "u0") in x[k]:
            print("UNDECODED", x["page"], k)

# Validation: 'tex' and fix 'old' must occur exactly once on their page; no marker line touched.
ok = True
for x in F:
    path = FOLDER + "\\page_%03d.tex" % x["page"]
    with open(path, encoding="utf-8", newline="") as fh:
        text = fh.read()
    n_tex = text.count(x["tex"])
    if n_tex != 1:
        ok = False
        print("TEX COUNT", x["page"], n_tex, repr(x["tex"]))
    if x["fix"] is not None:
        old = x["fix"]["old"]
        n_old = text.count(old)
        if n_old != 1 or "%%%%%%%%%%" in old:
            ok = False
            print("OLD COUNT", x["page"], n_old, repr(old))
    # for misprints, applying corrected must change only the tex substring
    if x["kind"] == "misprint_in_print" and "corrected" not in x:
        ok = False
        print("NO CORRECTED", x["page"])

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

# reload check
with open(OUT, encoding="utf-8") as fh:
    back = json.load(fh)
print("written", len(back), "findings; validation", "OK" if ok else "FAILED")
from collections import Counter
c = Counter((x["page"], x["kind"] == "misprint_in_print") for x in back)
for p in (146, 147, 148, 149, 150):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
