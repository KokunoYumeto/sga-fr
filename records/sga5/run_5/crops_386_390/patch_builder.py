import pathlib
p = pathlib.Path(__file__).parent / "build_findings.py"
s = p.read_text(encoding="utf-8")
a = '''        print(ed, "marker", folio, "at line", ln, "; anchor at line", t.count("\\n", 0, k) + 1)
'''
b = '''        print(ed, "marker", folio, "at line", ln, "; anchor at line", t.count("\\n", 0, k) + 1)
        LINES.setdefault(folio, {})[ed] = t.count("\\n", 0, k) + 1
'''
assert s.count(a) == 1, ("a", s.count(a))
s = s.replace(a, b)
a2 = '''for ed, path in S5.items():
    t = path.read_text(encoding="utf-8")
'''
b2 = '''LINES = {}
for ed, path in S5.items():
    t = path.read_text(encoding="utf-8")
'''
assert s.count(a2) == 1, ("a2", s.count(a2))
s = s.replace(a2, b2)
a3 = '''OUT.write_text(json.dumps(F'''
b3 = '''for r in F:
    for folio, d in LINES.items():
        ph = "<<L%d>>" % folio
        if ph in r["note"]:
            r["note"] = r["note"].replace(ph, "diplomatic s5.tex line %d, current %d" % (d["diplomatic"], d["current"]))
    assert "<<L" not in r["note"], r["note"][:80]
OUT.write_text(json.dumps(F'''
assert s.count(a3) == 1, ("a3", s.count(a3))
s = s.replace(a3, b3)
p.write_text(s, encoding="utf-8")
print("ok")
