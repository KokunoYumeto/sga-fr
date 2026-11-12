import json, os, sys

RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I"
PAGES = os.path.join(RUN, "b291_295")
OUT = os.path.join(RUN, "findings_291_295_recheck.json")

C = "'corrected' replaces the 'tex' substring."

findings = [
    {
        "page": 291,
        "where": "6.3, first sentence: 'de sorte que toute extension G de Z_{S,T} par G = G_mS sera bien représentable (6.2.4)'",
        "scan": "toute extension G de ℤ_{S,T}: the G carries a typed underline, no bar",
        "tex": r"toute extension $\underline{G}$ de",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": r"toute extension $\overline{G}$ de",
        "note": "The TeX keeps the printed underline. The extension of Z_{S,T} by G is G-bar throughout §6: 6.2.4, cited in this sentence, says 'G-bar est représentable', and 'Donc G-bar est décrit' follows four lines below. The typescript put the bar stroke under the G instead of over it. " + C,
    },
    {
        "page": 291,
        "where": "display (6.3.2)",
        "scan": "(O_S(-D),s_D|U): the index of s is D, without a minus sign",
        "tex": r"(\underline{O}_S(-D),s_D|U)",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": r"(\underline{O}_S(-D),s_{-D}|U)",
        "note": "The TeX keeps the printed s_D. The sentence that follows describes the second member as the restriction to U of the canonical rational section s_{-D} of O_S(-D); s_D would be the canonical section of O_S(D). " + C,
    },
    {
        "page": 291,
        "where": "6.3, 'donc une extension G de Z_{S,T} par G_m , que nous appelerons le modèle de Néron-Raynaud de G_m'",
        "scan": "donc une extension G de ℤ_{S,T} par G_m: plain G, no bar",
        "tex": r"donc une extension $G$ de",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": r"donc une extension $\overline{G}$ de",
        "note": "The TeX keeps the unbarred G. In 6.3 G stands for G_mS (first sentence); the extension defined here is the Néron-Raynaud model, 'cette extension G-bar' at the top of p. 292 and G-bar in 6.3.3 to 6.6. " + C,
    },
    {
        "page": 291,
        "where": "6.3, 'que nous appelerons le modèle de Néron-Raynaud de G_m'",
        "scan": "appelerons",
        "tex": "appelerons",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "appellerons",
        "note": "Spelling slip of the typescript (appeler doubles the l before a mute e); the TeX keeps the printed reading. " + C,
    },
    {
        "page": 292,
        "where": "6.3.3, 'tel que la restriction de div f à V est égal à celle de nD'",
        "scan": "est égal à celle de nD",
        "tex": "est égal à celle de",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "est égale à celle de",
        "note": "Agreement slip: the subject is 'la restriction' (feminine), compared with 'celle de nD'. The TeX keeps the printed reading. " + C,
    },
    {
        "page": 293,
        "where": "Théorème 6.5, last sentence: '(plus généralement, si ces anneaux locaux sont factoriels)'",
        "scan": "si ces anneaux locaux sont factoriels",
        "tex": r"\underline{si ces anneaux locaux sont factoriels}",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": r"\underline{si ses anneaux locaux sont factoriels}",
        "note": "Homophone slip: the local rings of S, possessive 'ses'. The TeX keeps the printed 'ces'. " + C,
    },
    {
        "page": 294,
        "where": "second paragraph of the proof of 6.5: 'essentiellement surjectif lorsque les anneaux locaux de X sont factoriels'",
        "scan": "les anneaux locaux de X sont factoriels",
        "tex": r"de $X$ sont factoriels",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": r"de $S$ sont factoriels",
        "note": "Wrong letter: no X occurs in §6; the hypothesis of 6.5 is on the local rings of S, and the paragraph ends 'de l'hypothèse faite sur S'. The TeX keeps the printed X. " + C,
    },
    {
        "page": 295,
        "where": "Corollaire 6.6, 'purement 1-codimensionnel'",
        "scan": "1-codimensionnel: the underline begins under the c; the 1 and the hyphen are not underlined",
        "tex": r"1\underline{-codimensionnel}",
        "kind": "underline",
        "confidence": "medium",
        "fix": {"old": r"1\underline{-codimensionnel}", "new": r"1-\underline{codimensionnel}"},
        "note": "Same pattern as the globally handled $R$\\underline{-algebra}, but after a text numeral rather than a math letter, so that handling may not catch it.",
    },
    {
        "page": 295,
        "where": "6.5.1, first words",
        "scan": "Plaçons nous maintenant (no hyphen)",
        "tex": "Plaçons nous",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": "Plaçons-nous",
        "note": "Orthographic slip: the imperative with its pronoun takes a hyphen. The TeX keeps the printed reading. " + C,
    },
]

ok = True
for f in findings:
    path = os.path.join(PAGES, "page_%03d.tex" % f["page"])
    with open(path, "r", encoding="utf-8", newline="") as fh:
        text = fh.read()
    n_tex = text.count(f["tex"])
    msg = "p%d tex count=%d" % (f["page"], n_tex)
    if n_tex < 1:
        ok = False
        msg += "  <-- TEX NOT FOUND"
    if f["fix"] is not None:
        n_old = text.count(f["fix"]["old"])
        msg += " | fix old count=%d" % n_old
        if n_old != 1:
            ok = False
            msg += "  <-- OLD NOT UNIQUE"
        marker_lines = [ln for ln in text.split("\n") if ln.startswith("%%%%%%%%%%")]
        for ln in marker_lines:
            if f["fix"]["old"] in ln:
                ok = False
                msg += "  <-- OLD TOUCHES MARKER"
    if f["kind"] == "misprint_in_print" and "corrected" not in f:
        ok = False
        msg += "  <-- NO CORRECTED"
    print(msg)

if not ok:
    print("CHECK FAILED; not writing")
    sys.exit(1)

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

# re-read to validate
with open(OUT, "r", encoding="utf-8") as fh:
    data = json.load(fh)
print("written", OUT, len(data), "findings")
