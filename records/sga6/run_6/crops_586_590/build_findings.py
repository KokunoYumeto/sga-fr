"""Build findings_586_590.json (notes write the main.tex line breaks as a literal backslash-n, as in earlier batches)."""
import json, pathlib, sys
from collections import Counter
sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b586_590"
NL = "\\" + "n"          # literal backslash-n inside notes
M588 = "%%%%%%%%%%  scan idx 601  |  folio 588  %%%%%%%%%%"
M590 = "%%%%%%%%%%  scan idx 603  |  folio 590  %%%%%%%%%%"
M591 = "%%%%%%%%%%  scan idx 604  |  folio 591  %%%%%%%%%%"
BS = "\\"
F = [
 {"page": 588,
  "where": "start of page (folio-588 marker)",
  "scan": "p. 588 begins \"qu'il résulte de 7.16.2 que Gr.^num(X_t̄) est isomorphe à un quotient d'un\"; "
          "p. 587 ends \"... dans les sections précédentes. Signalons seulement\" (both scans: b586_590/page_587_s4.png, "
          "page_588_s1.png; crops_586_590/wit_587_half.png, wit_588_half.png)",
  "tex": "\"qu'il\" is the last word of page_587.tex (\"Signalons seulement qu'il\", under the folio-587 marker); "
         "page_588.tex begins \"résulte de 7.16.2\"",
  "kind": "marker", "confidence": "high", "fix": None,
  "note": "Page 588 really begins with \"qu'il\". Exact edit in main.tex, both layers (diplomatic about line 15144, "
          "current about 15148 at 16:32 on 13 Nov; the file is being edited, use the string, which occurs once per "
          "layer): replace \"Signalons seulement qu'il" + NL + M588 + NL + "résulte de 7.16.2\" by \"Signalons seulement"
          + NL + M588 + NL + "qu'il résulte de 7.16.2\" (simulated in memory on both layers: "
          "crops_586_590/sim_markers.py). marker_split_word.py pull \"qu'il\" would join it to \"résulte\" without a "
          "space, so use the string edit."},
 {"page": 588,
  "where": "7.17.4, \"en représentant K' comme limite inductive des anneaux affines\"",
  "scan": "en représentant K' comme limite inductive (a capital K with its prime, against the small k of "
          "\"si k' est une extension pure\" two lines above; the same in the witness: crops_586_590/m588_Kprime.png, "
          "m588_kprime_si.png, wit_588_half.png)",
  "tex": "en représentant " + BS + "(k'" + BS + ") comme limite inductive",
  "kind": "misprint_in_print", "confidence": "high",
  "fix": {"old": "en représentant " + BS + "(k'" + BS + ") comme",
          "new": "en représentant " + BS + "(K'" + BS + ") comme"},
  "corrected": BS + "(k'" + BS + ")",
  "note": "Typing error of the print: the object written as an inductive limit of affine rings is the pure "
          "extension k' of the sentence. The diplomatic TeX silently corrects it to k'; the fix restores the printed "
          "K'. The current layer already has " + BS + "(k'" + BS + ")."},
 {"page": 588,
  "where": "paragraph after (7.17.4.1), first words",
  "scan": "Un autre façon de définir un homomorphisme (7.17.4.1) consiste à se (both scans)",
  "tex": "Un autre façon de définir un homomorphisme (7.17.4.1)",
  "kind": "misprint_in_print", "confidence": "high",
  "fix": None,
  "corrected": "Une autre façon",
  "note": "Agreement error of the print (façon is feminine). The diplomatic TeX keeps the printed reading; the "
          "current layer already reads \"Une autre façon\"."},
 {"page": 590,
  "where": "start of page (folio-590 marker)",
  "scan": "p. 590 begins \"cas où la base est un trait. Il s'ensuit que les propriétés sur l'homomor-\"; p. 589 ends "
          "\"s'est ramené pour la construction d'un homomorphisme de spécialisation au\" (both scans: "
          "b586_590/page_589_s4.png, page_590_s1.png; crops_586_590/wit_589_half.png, wit_590_half.png)",
  "tex": "\"cas où la\" ends page_589.tex (\"... de spécialisation au cas où la\", under the folio-589 marker); "
         "page_590.tex begins \"base est un trait.\"",
  "kind": "marker", "confidence": "high", "fix": None,
  "note": "Page 590 really begins with \"cas où la\". Exact edit in main.tex, both layers (diplomatic about line "
          "15172, current about 15176 at 16:32 on 13 Nov; the string occurs once per layer): replace "
          "\"de spécialisation au cas où la" + NL + M590 + NL + "base est un trait.\" by \"de spécialisation au" + NL
          + M590 + NL + "cas où la base est un trait.\" (simulated in memory on both layers: "
          "crops_586_590/sim_markers.py)."},
 {"page": 590,
  "where": "end of page (folio-591 marker)",
  "scan": "p. 590 ends \"Soit K une extension de k, nous cherchons des cri-\"; p. 591 begins \"tères pour que "
          "F(k) --> F(K) soit injectif (resp. surjectif).\" (b586_590/page_590_s4.png, b591_595/page_591_s1.png, "
          "crops_586_590/m591_top.png, wit_590_half.png)",
  "tex": "page_590.tex ends with the whole word \"nous cherchons des critères\" above the folio-591 marker; "
         "page_591.tex begins \"pour que\"",
  "kind": "marker", "confidence": "high", "fix": None,
  "note": "Page 591 really begins with \"tères\", the second half of \"cri-tères\" divided at the page break. This "
          "is the same boundary as the start of page 591 (batch 591-595): apply once. Exact edit in main.tex, both "
          "layers (the string occurs once per layer): replace \"nous cherchons des critères" + NL + M591 + NL
          + "pour que\" by \"nous cherchons des cri%" + NL + M591 + NL + "tères pour que\" (the % keeps "
          "\"critères\" one word, as \"cet ex%\" at folio 18; simulated in memory on both layers: "
          "crops_586_590/sim_markers.py)."},
]
for x in F:
    for k in ("scan", "tex", "note", "where"):
        assert "\n" not in x[k], (x["page"], k)
    if x["fix"]:
        t = (B / f"page_{x['page']}.tex").read_text(encoding="utf-8")
        old = x["fix"]["old"]
        n = t.count(old)
        print(x["page"], "old count", n, repr(old), "->", repr(x["fix"]["new"]))
        assert n == 1 and "%%%%%%%%%%" not in old
out = RUN / "findings_586_590.json"
out.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
L = json.loads(out.read_text(encoding="utf-8"))
print("written", out, len(L))
c = Counter((x["page"], "misprint" if x["kind"] == "misprint_in_print" else "normal") for x in L)
print(sorted(c.items()))
