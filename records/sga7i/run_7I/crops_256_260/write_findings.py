import json, sys
base = sys.argv[1]
findings = [
 {"page": 257, "where": "b), last line: \"et L = M/T le quotient, qui est isomorphisme à Z^r\"",
  "scan": "qui est isomorphisme à ℤ^r .",
  "tex": "qui est isomorphisme à",
  "kind": "misprint_in_print", "confidence": "high", "fix": None,
  "corrected": "qui est isomorphe à",
  "note": "Typing error of the print: 'isomorphisme' for the adjective 'isomorphe'. The TeX keeps the printed reading."},
 {"page": 258, "where": "first paragraph, second exact sequence (after \"donne une suite exacte\")",
  "scan": "0 → D(L) → D(M) → D(L) → 0 (SGA 3 IX 3.1)",
  "tex": "D(M) \longrightarrow D(L)",
  "kind": "misprint_in_print", "confidence": "high", "fix": None,
  "corrected": "D(M) \longrightarrow D(T)",
  "note": "The print repeats D(L) as the third term. Dualizing 0 → T → M → L → 0 gives 0 → D(L) → D(M) → D(T) → 0, and the next sentence treats D(L) and D(T). The TeX keeps the printed reading."},
 {"page": 260, "where": "\"Notons qu'il suffit de trouver une section f de P sur P telle que f(0) = 0\"",
  "scan": "une section f de P sur P telle que f(0) = 0,",
  "tex": "une section $f$ de $P$ sur $P$",
  "kind": "misprint_in_print", "confidence": "medium", "fix": None,
  "corrected": "une section $f$ de $E$ sur $P$",
  "note": "f must be a section of the extension E over P: f(x+y)-f(x)-f(y) is then a morphism P x_S P → Z_S (cf. Lemme 3.4.2, sections of the torsor E). The TeX keeps the printed 'de P sur P'."},
 {"page": 260, "where": "\"... qui est nul sur la section nulle de P x_S P , donc est nulle puisque ...\"",
  "scan": "donc est nulle puisque PX_SP est à fibres connexes",
  "tex": "donc est nulle puisque",
  "kind": "misprint_in_print", "confidence": "low", "fix": None,
  "corrected": "donc est nul puisque",
  "note": "Agreement slip of the print: the subject is 'le premier membre' / 'un morphisme' (masculine), as in 'qui est nul' just before. The TeX keeps the printed 'nulle'."},
]
for f in findings:
    p = f"{base}/b256_260/page_{f['page']}.tex"
    t = open(p, encoding='utf-8', newline='').read()
    n = t.count(f['tex'])
    print(f['page'], repr(f['tex']), 'count', n)
    if f['fix'] is not None:
        print('  fix old count', t.count(f['fix']['old']))
out = f"{base}/findings_256_260_recheck.json"
with open(out, 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
    fh.write('\n')
print('written', out)
