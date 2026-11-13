import pathlib

p = pathlib.Path(__file__).parent / "make_findings.py"
s = p.read_text(encoding="utf-8")

reps = [
    ('''    r"\\end{aligned} \\tag{3.4}",
    "other", "medium",''',
     '''    r"\\end{aligned} \\tag{3.4}",
    "other", "high",'''),
    ('''    r"\\tag turns the reference into an equation number (3.4), which clashes with Proposition 3.4. Does not "
    r"overlap the comma fix just above.")''',
     '''    r"\\tag turns the reference into an equation number (3.4), which clashes with Proposition 3.4; the "
    r"typescript's equation numbers stand at the left margin ((3.7.1), (4.3.1), (4.3.2)). Does not overlap the "
    r"comma fix just above.")'''),
    ('OUT.write_text(json.dumps(items, ensure_ascii=False, indent=1), encoding="utf-8")',
     'OUT.write_bytes(json.dumps(items, ensure_ascii=False, indent=1).encode("utf-8"))'),
    ('''    (pathlib.Path(__file__).parent / ("applied_%d.tex" % p)).write_text(t, encoding="utf-8")''',
     '''    (pathlib.Path(__file__).parent / ("applied_%d.tex" % p)).write_bytes(t.encode("utf-8"))'''),
]
for a, b in reps:
    n = s.count(a)
    assert n == 1, (n, a[:60])
    s = s.replace(a, b)
p.write_bytes(s.encode("utf-8"))
print("patched", len(reps))
