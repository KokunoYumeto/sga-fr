import json
import pathlib

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I")
PAGES = RUN / "b381_385"
OUT = RUN / "findings_381_385.json"

findings = [
    {
        "page": 383,
        "where": "Démonstration de 5.9, sentence after the display 0 -> F''(n) -> F(n) -> F'(n) -> 0",
        "scan": "avec F'(n) connexe et F''(n)_o purement infinitésimal",
        "tex": "avec $F'(n)$ connexe et $F''(n)_o$ purement infinitésimal",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "$F'(n)$ étale",
        "note": "Slip in the print; the TeX keeps the printed reading. F' is the ind-étale quotient "
                "(stated two lines earlier), so F'(n) is finite étale and in general not connected; "
                "Lemma 5.9.2 is then applied with G'' = F'(n), which must be lisse. Intended reading: "
                "'F'(n) étale'. (A dropped prime, 'F''(n) connexe', would also be true but leaves the "
                "lemma's smoothness hypothesis unstated.)",
    },
    {
        "page": 385,
        "where": "Corollaire 5.10, first line of the statement",
        "scan": "un schéma abélien sur le corps des fonctions K  (underline stops after 'fonctions'; K not underlined)",
        "tex": "\\underline{un schéma abélien sur le corps des fonctions $K$}",
        "kind": "underline",
        "confidence": "high",
        "fix": {
            "old": "\\underline{un schéma abélien sur le corps des fonctions $K$}",
            "new": "\\underline{un schéma abélien sur le corps des fonctions} $K$",
        },
        "note": "The print leaves the variable K outside the underline (as in Théorème 5.8 on p. 382, which the TeX gives correctly).",
    },
    {
        "page": 385,
        "where": "proof of 5.10, 'Traitons maintenant le cas général ... strictement local.'",
        "scan": "Soir K' une extension galoisienne finie",
        "tex": "Soir $K'$",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "Soit $K'$",
        "note": "Typing error of the print (Soir for Soit); the TeX keeps the printed reading.",
    },
]

# Check every fix's "old" occurs exactly once in its page file.
ok = True
for f in findings:
    if f["fix"] is None:
        continue
    text = (PAGES / f"page_{f['page']:03d}.tex").read_text(encoding="utf-8")
    n = text.count(f["fix"]["old"])
    print(f["page"], repr(f["fix"]["old"]), "occurrences:", n)
    if n != 1:
        ok = False
    # also confirm the fix does not touch a marker line
    assert "%%%%%%%%%%" not in f["fix"]["old"]

# Confirm quoted tex snippets exist on the page.
for f in findings:
    text = (PAGES / f"page_{f['page']:03d}.tex").read_text(encoding="utf-8")
    print(f["page"], "tex snippet present:", f["tex"] in text)

OUT.write_text(json.dumps(findings, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
json.loads(OUT.read_text(encoding="utf-8"))
print("written", OUT, "all olds unique:", ok)
