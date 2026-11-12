import json, pathlib, sys
run = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I")
pages = run / "b326_330"
F = [
 {"page": "328",
  "where": "first line, before (2.1.8)",
  "scan": "de sorte que la suite exacte (2.1.5) s'écrit alors",
  "tex": "de sorte que la suite exacte (2.1.5) s'écrit alors",
  "kind": "misprint_in_print", "confidence": "high", "fix": None,
  "corrected": "(2.1.6)",
  "note": "Wrong reference number in the print: 2.1.5 is a paragraph (definition of rang unipotent nul), not an exact sequence. The sequence that (2.1.7) turns into (2.1.8) is (2.1.6); p. 329 (2.1.14) also says 'correspondant à (2.1.6) ou (2.1.8)'. The TeX keeps the printed reading."},
 {"page": "328",
  "where": "2.1.12, sentence after 'rang abélien de A_o .'",
  "scan": "Il sont encore reliés par les relations (2.1.10)",
  "tex": "Il sont encore reliés par les relations (2.1.10)",
  "kind": "misprint_in_print", "confidence": "high", "fix": None,
  "corrected": "Ils sont",
  "note": "Typing error in the print (subject 'Les entiers n, mu, lambda, alpha', plural): the s of 'Ils' is missing. The TeX keeps the printed reading."},
 {"page": "329",
  "where": "first paragraph (end of 2.1.13), last line",
  "scan": "(ou \"hauteur\") des groupes-de Barsotti-Tate envisagés.",
  "tex": "des groupes-de Barsotti-Tate envisagés.",
  "kind": "misprint_in_print", "confidence": "medium", "fix": None,
  "corrected": "groupes de",
  "note": "The typescript has a hyphen in place of the space between 'groupes' and 'de' (typing error; elsewhere 'groupes de Barsotti-Tate'). The TeX keeps the printed reading."},
 {"page": "329",
  "where": "Lemme 2.2.1 (iv), end",
  "scan": "est de rang unipotent nul (cf. 1.5.5).",
  "tex": chr(92) + "underline{est de rang unipotent nul} (cf. 1.5.5).",
  "kind": "misprint_in_print", "confidence": "medium", "fix": None,
  "corrected": "(cf. 2.1.5)",
  "note": "Wrong reference number in the print: Exposé IX has no 1.5.5 (Proposition 1.5 has no subparagraphs); 'rang unipotent nul' is explained in 2.1.5, which 2.1.13 (p. 328) and 3.2 (i) cite for the same notion. The TeX keeps the printed reading."},
]
ok = True
for f in F:
    t = (pages / f"page_{f['page']}.tex").read_text(encoding="utf-8")
    n = t.count(f["tex"])
    if n < 1:
        ok = False; print("TEX NOT FOUND", f["page"], f["tex"])
    if f["fix"] is not None:
        c = t.count(f["fix"]["old"])
        if c != 1:
            ok = False; print("OLD COUNT", c, f["page"], f["fix"]["old"])
out = run / "findings_326_330_recheck.json"
out.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
json.loads(out.read_text(encoding="utf-8"))
print("ok" if ok else "PROBLEM", out)
