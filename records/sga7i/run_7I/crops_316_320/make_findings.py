"""Write findings_316_320_recheck.json (SGA 7 I, folios 316-320) and check every fix 'old' and every 'tex'."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
BS = chr(92)
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I")
B = RUN / "b316_320"
OUT = RUN / "findings_316_320_recheck.json"

F = [
    {"page": 316,
     "where": "0.3, 'dont nous avons déjà eû à faire usage dans l'étude de l'action de monodromie'",
     "scan": "déjà eû à faire usage (circumflex on the u; crops_316_320/p316_eu.png)",
     "tex": "déjà eû à faire",
     "kind": "misprint_in_print", "confidence": "high", "fix": None,
     "corrected": "déjà eu à faire",
     "note": "Spelling error of the print: the past participle of avoir is 'eu'. The TeX keeps the printed reading; "
             "'corrected' replaces the 'tex' substring."},
    {"page": 316,
     "where": "0.3, '(ces termes étant synonymes, parait-il, lorsqu'il est question de variétés abéliennes'",
     "scan": "parait-il (plain i, no circumflex; crops_316_320/p316_parait.png)",
     "tex": "synonymes, parait-il,",
     "kind": "misprint_in_print", "confidence": "medium", "fix": None,
     "corrected": "synonymes, paraît-il,",
     "note": "Missing circumflex; the typewriter has the î (p. 317 types 'apparaît'). The TeX keeps the printed "
             "reading; 'corrected' replaces the 'tex' substring."},
    {"page": 316,
     "where": "footnote (**), 'via la théorie rigide-analytique, n'utilisant pas le théorème de réduction semi-stable'",
     "scan": "n'utilisant pas: the space cell between the two words holds only a faint speck about 3 px across at "
             "the baseline; the typewriter's full stop is a dark dot about 8 px across (e.g. 'semi-stable.' at the "
             "end of the same footnote) (crops_316_320/p316_dot_6x.png against p316_period_4x.png)",
     "tex": "n'utilisant.pas",
     "kind": "extra", "confidence": "medium",
     "fix": {"old": "n'utilisant.pas", "new": "n'utilisant pas"},
     "note": "The speck is a physical defect of the scan, not a typed full stop, so the diplomatic TeX should not "
             "carry it. MISPRINTS_7I.json holds a record of this spot from findings_316_320.json (print "
             "'n'utilisant.pas', correct 'n'utilisant pas', TeX keeps it); once this fix is applied that record "
             "is wrong and should go. The corrected layer already reads 'n'utilisant pas'."},
    {"page": 317,
     "where": "'sous la réserve toutesfois, parfois, de disposer du théorème fondamental de TATE'",
     "scan": "toutesfois (one word, no space before the f; f and i struck twice; crops_316_320/p317_toutesfois.png)",
     "tex": "réserve toutesfois, parfois",
     "kind": "misprint_in_print", "confidence": "medium", "fix": None,
     "corrected": "réserve toutefois, parfois",
     "note": "Archaic or erroneous spelling of 'toutefois'. The TeX keeps the printed reading; 'corrected' replaces "
             "the 'tex' substring (the corrected layer already reads 'toutefois')."},
    {"page": 317,
     "where": "'il est clair dès maintenant que l'étude des pro-p-groupes de Barsotti-Tate définis par voie "
              "géométrique ... doit être considéré comme faisant partie de la théorie de la \"monodromie locale\"'",
     "scan": "doit être considéré comme",
     "tex": "doit être considéré comme",
     "kind": "misprint_in_print", "confidence": "low", "fix": None,
     "corrected": "doit être considérée comme",
     "note": "Agreement slip: the subject of 'doit être considéré' is 'l'étude' (feminine). Low: possibly the "
             "author's own wording. The TeX keeps the printed reading; the corrected layer also still reads "
             "'considéré'. 'corrected' replaces the 'tex' substring."},
    {"page": 319,
     "where": "heading of §1, 'et la biextension cancnique W^o de (A^o,A'^o)'",
     "scan": "cancnique (crops_316_320/p319_cancnique.png)",
     "tex": BS + "underline{et la biextension cancnique}",
     "kind": "misprint_in_print", "confidence": "high", "fix": None,
     "corrected": BS + "underline{et la biextension canonique}",
     "note": "Typing error; the same heading prints 'l'accouplement canonique' correctly. The TeX keeps the printed "
             "reading; 'corrected' replaces the 'tex' substring (the corrected layer already reads 'canonique')."},
    {"page": 319,
     "where": "1.0, 'pour lequel nous utilisons nos notations habituelles s, η, k, X etc. de I 1'",
     "scan": "s, η, k, X etc. (a clear typed capital X; crops_316_320/p319_Xetc.png)",
     "tex": "$k$, $X$ etc.",
     "kind": "misprint_in_print", "confidence": "low", "fix": None,
     "corrected": "$k$, $K$ etc.",
     "note": "The list names the usual notations attached to the trait S (closed point s, generic point η, residue "
             "field k); the next sentence uses K, the field of fractions, without introducing it ('un schéma "
             "abélien A_K sur K'), and X is not a notation of the trait. Probably K misread as X. Low: no second "
             "witness; the corrected layer also reads X. The TeX keeps the printed reading; 'corrected' replaces the "
             "'tex' substring."},
]

ok = True
for x in F:
    t = (B / f"page_{x['page']:03d}.tex").read_bytes().decode("utf-8")
    assert "\r" not in t
    for label, s in (("tex", x["tex"]), ("old", (x["fix"] or {}).get("old"))):
        if s is None:
            continue
        n = t.count(s)
        print(x["page"], label, repr(s), n)
        ok &= n == 1
assert ok, "a substring is not unique"
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
print("written", OUT, len(F))
