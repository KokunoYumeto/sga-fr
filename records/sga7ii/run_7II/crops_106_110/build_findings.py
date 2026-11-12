import json
import os

RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II"
BATCH = os.path.join(RUN, "b106_110")
OUT = os.path.join(RUN, "findings_106_110.json")

NL = "\n"

findings = [
    {
        "page": 106,
        "where": "first paragraph, first sentence (proof of Lemme 2.1.11)",
        "scan": "Le dévissage utilisé en 2.1.11 nous ramène au cas où F est constant",
        "tex": r"Le dévissage utilisé en 2.1.11 nous ramène",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "2.1.10",
        "note": "Wrong reference number in the print, kept by the TeX. This paragraph proves Lemme 2.1.11 (stated at the foot of p.105); the dévissage reducing to F constant is the one carried out in the proof of Lemme 2.1.10 on p.105 (résolution de F par des faisceaux g'_* G, G constant). The later 'Il suffit donc de prouver 2.1.11' is correct.",
    },
    {
        "page": 106,
        "where": "first paragraph, second sentence",
        "scan": "On peut supposer D réunion de diverseurs lisses (D_i)_{i ∈ I}",
        "tex": r"réunion de diverseurs lisses",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "diviseurs",
        "note": "Typing error 'diverseurs' for 'diviseurs' in the print; the TeX keeps the printed reading.",
    },
    {
        "page": 107,
        "where": "proof of 2.1.13.1, second sentence",
        "scan": "après avoir remplacé L par une des ses composantes",
        "tex": r"par une des ses composantes",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "une de ses composantes",
        "note": "Typing error 'des ses' for 'de ses' in the print; the TeX keeps the printed reading.",
    },
    {
        "page": 107,
        "where": "2.2.1, first trace morphism (on Y_s)",
        "scan": "un morphisme trace Tr_u : u_! u F → F est défini (SGA4 XVII 6.2.3)",
        "tex": r"$\mathrm{Tr}_u : u_! u F \to F$",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": r"\mathrm{Tr}_u : u_! u^* F \to F",
        "note": "The print has no star after the second u here (no blank slot for one; checked on a magnified crop), whereas the analogue two lines below reads u_! u^* F. The TeX keeps the printed reading.",
    },
    {
        "page": 107,
        "where": "diagram of Proposition 2.2.2, after the bottom-right Ψ F",
        "scan": "Ψ F ════ Ψ F   .",
        "tex": r"& \Psi F" + NL + r"\end{tikzcd}",
        "kind": "punctuation",
        "confidence": "high",
        "fix": {
            "old": r"& \Psi F" + NL + r"\end{tikzcd}",
            "new": r"& \Psi F" + NL + r"\end{tikzcd}\quad .",
        },
        "note": "The full stop typed to the right of the diagram is missing (the file's own diagram comment records it).",
    },
    {
        "page": 108,
        "where": "2.2.3, triangle diagram X → Y over S",
        "scan": "S   .  (full stop to the right of S)",
        "tex": r"{} \end{tikzcd}",
        "kind": "punctuation",
        "confidence": "high",
        "fix": {
            "old": r"{} \end{tikzcd}",
            "new": r"{} \end{tikzcd}\quad .",
        },
        "note": "The full stop closing the sentence after the diagram is missing (the file's own diagram comment records it).",
    },
    {
        "page": 108,
        "where": "sentence introducing the deployed diagram",
        "scan": "Le diagramme (2.2.4 ) se déploye en le suivant",
        "tex": r"se déploye en le suivant",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "se déploie",
        "note": "Spelling error 'déploye' for 'déploie' in the print; the TeX keeps the printed reading.",
    },
    {
        "page": 108,
        "where": "deployed diagram with regions (1), (2), (3), after the bottom-right K",
        "scan": "Rg_! g* --Tr_g--> K   .",
        "tex": r"g^* \arrow[r, " + '"' + r"\mathrm{Tr}_g" + '"' + r"] & K" + NL + r"\end{tikzcd}",
        "kind": "punctuation",
        "confidence": "high",
        "fix": {
            "old": r"g^* \arrow[r, " + '"' + r"\mathrm{Tr}_g" + '"' + r"] & K" + NL + r"\end{tikzcd}",
            "new": r"g^* \arrow[r, " + '"' + r"\mathrm{Tr}_g" + '"' + r"] & K" + NL + r"\end{tikzcd}\quad .",
        },
        "note": "The full stop typed to the right of K is missing (the file's own diagram comment records it). The Corollaire 2.2.4 diagram above has no printed punctuation.",
    },
    {
        "page": 109,
        "where": "formula (2.2.5.1), first term",
        "scan": "Tr_g : Rf_Φ RΨg* K(n)[2n] → Rg_!RΨg* K(n)[2n] → Rg_!g* K(n)[2n] → K ,",
        "tex": r"\mathrm{Tr}_g : Rf_\Phi \, R\Psi g^* K(n)[2n]",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": r"Rg_\Phi",
        "note": "Wrong letter in the print, kept by the TeX: Φ is a part of Y_s, Rg_Φ has just been defined, and the composite Tr_g passes from support in Φ to Rg_!; the first term must be Rg_Φ (magnified crop confirms the print's Rf).",
    },
    {
        "page": 109,
        "where": "displayed isomorphism after 'On a alors'",
        "scan": "Rf_{x} ⥲ Rg_{x} ;",
        "tex": r"Rg_{\{x\}} \; ;",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": r"Rg_{\{y\}}",
        "note": "Probable wrong index in the print, kept by the TeX: g lives on Y and y = u(x); the diagram (2.2.5.2) just below writes Rg_{y}. The print may instead intend x identified with y, hence low confidence.",
    },
    {
        "page": 110,
        "where": "Scholie 2.2.6, first reference",
        "scan": "La compatibilité 2.3.5.2 exprime que",
        "tex": r"La compatibilité 2.3.5.2 exprime",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "2.2.5.2",
        "note": "Wrong reference number in the print, kept by the TeX: the compatibility is the diagram (2.2.5.2) of p.109; 2.3 is the finiteness section.",
    },
    {
        "page": 110,
        "where": "Scholie 2.2.6, second reference",
        "scan": "le morphisme trace (2.3.5.1) pour Φ = {x}",
        "tex": r"le morphisme trace (2.3.5.1) pour",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "(2.2.5.1)",
        "note": "Wrong reference number in the print, kept by the TeX: the trace morphism is (2.2.5.1) of p.109.",
    },
]

# Validate: every non-null fix's "old" occurs exactly once in its page file,
# never spans a marker line, and every "tex" quote is present on its page.
ok = True
for f in findings:
    path = os.path.join(BATCH, "page_%03d.tex" % f["page"])
    with open(path, encoding="utf-8", newline="") as fh:
        text = fh.read()
    if "\r\n" in text:
        print("WARNING CRLF in", path)
    if f["tex"] not in text:
        print("TEX QUOTE NOT FOUND p%d: %r" % (f["page"], f["tex"]))
        ok = False
    fix = f["fix"]
    if fix is not None:
        n = text.count(fix["old"])
        if n != 1:
            print("OLD COUNT %d p%d: %r" % (n, f["page"], fix["old"]))
            ok = False
        if "%%%%%%%%%%" in fix["old"]:
            print("OLD touches marker p%d" % f["page"])
            ok = False
    if f["kind"] == "misprint_in_print" and "corrected" not in f:
        print("MISSING corrected p%d" % f["page"])
        ok = False

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=2)
    fh.write("\n")

counts = {}
for f in findings:
    c = counts.setdefault(f["page"], [0, 0])
    c[1 if f["kind"] == "misprint_in_print" else 0] += 1
print("valid" if ok else "INVALID")
for p in sorted(counts):
    print(p, "normal=%d misprint=%d" % tuple(counts[p]))
print("wrote", OUT)
