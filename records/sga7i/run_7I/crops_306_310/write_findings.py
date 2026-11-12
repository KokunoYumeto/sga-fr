import json, sys, os
run = sys.argv[1]
out = os.path.join(run, "findings_306_310_recheck.json")
F = []
F.append({
 "page": 307,
 "where": r"display (7.3.4.1)",
 "scan": r"d(q^*_η(E_*)) : Φ ⟶ (Q/Z)_k — E carries a subscript asterisk",
 "tex": r"d(q^*_\eta(E_*))",
 "kind": "misprint_in_print",
 "confidence": "high",
 "fix": None,
 "corrected": r"d(q^*_\eta(E_\eta))",
 "note": r"The print types E with a subscript asterisk where E_η is meant (cf. the display just above, q^*_η(E_η)); the TeX keeps the printed reading."
})
F.append({
 "page": 307,
 "where": r"7.3.4.3, 'lorsque S est strictement_local, en vertu du lemme de Hensel'",
 "scan": r"strictement_local — a short dash on the baseline (typed underscore) between the two words",
 "tex": r"strictement\_local",
 "kind": "misprint_in_print",
 "confidence": "medium",
 "fix": None,
 "corrected": r"strictement local",
 "note": r"Typing slip in the print: a baseline dash stands where the space belongs (the page's hyphens, e.g. k-schéma, sit at mid-height). The TeX keeps the printed mark as \_."
})
F.append({
 "page": 308,
 "where": r"first paragraph, 'si et seulement si pour tout section q de Q'",
 "scan": r"pour tout section q de Q",
 "tex": r"pour tout section $q$ de $Q$",
 "kind": "misprint_in_print",
 "confidence": "high",
 "fix": None,
 "corrected": r"pour toute section",
 "note": r"Agreement slip in the print (section is feminine); the TeX keeps the printed reading."
})
F.append({
 "page": 308,
 "where": r"display (7.3.5.1)",
 "scan": r"long(V'/m V) — m underlined, the last V has no prime",
 "tex": r"\mathrm{long}(V'/\underline{m}\,V)",
 "kind": "misprint_in_print",
 "confidence": "high",
 "fix": None,
 "corrected": r"\mathrm{long}(V'/\underline{m}\,V')",
 "note": r"The ramification index e(V'/V) is the length of V'/mV' (cf. 7.3.5.3, where e(S'/S) = 1 means m' = m V'); the print drops the prime on the last V and the TeX keeps the printed reading."
})
F.append({
 "page": 309,
 "where": r"paragraph after (7.3.5.2), last line: 'à l'aise du changement de base η' ⟶ η'",
 "scan": r"à l'aise du changement de base",
 "tex": r"à l'aise du changement de base",
 "kind": "misprint_in_print",
 "confidence": "high",
 "fix": None,
 "corrected": r"à l'aide du changement de base",
 "note": r"Typing error in the print (aise for aide); the TeX keeps the printed reading."
})
F.append({
 "page": 309,
 "where": r"7.3.5.3, first line: 'e(S'/S) = 1 , i.e. où'",
 "scan": r"= 1 , i.e. — before the comma only a faint raised speck (about 30 px against 70 px for a typed full stop, sitting above the baseline); no full stop is typed",
 "tex": r"$e(S'/S) = 1$ ., i.e. où",
 "kind": "extra",
 "confidence": "medium",
 "fix": {"old": r"= 1$ .,", "new": r"= 1$ ,"},
 "note": r"The TeX turns a speck into a full stop. The mark is smaller, lighter and higher than the full stops of 'i.e.' on the same line; a similar speck sits beside the second full stop of 'i.e.'. If it is the remnant of an erased full stop, the typist's correction still gives '1 ,'."
})
with open(out, "w", encoding="utf-8", newline="\n") as f:
    json.dump(F, f, ensure_ascii=False, indent=1)
    f.write("\n")
# verify fixes
bad = 0
for x in F:
    if x["fix"] is None: continue
    p = os.path.join(run, "b306_310", "page_%03d.tex" % x["page"])
    t = open(p, encoding="utf-8").read()
    n = t.count(x["fix"]["old"])
    print(x["page"], repr(x["fix"]["old"]), "count =", n)
    if n != 1: bad += 1
# check tex quotes for misprints exist in the tex
for x in F:
    p = os.path.join(run, "b306_310", "page_%03d.tex" % x["page"])
    t = open(p, encoding="utf-8").read()
    print(x["page"], x["kind"], "tex-snippet found:", x["tex"] in t)
print("bad fixes:", bad)
json.load(open(out, encoding="utf-8"))
print("json ok", out)
