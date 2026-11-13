import pathlib
p = pathlib.Path(__file__).with_name("build_findings.py")
t = p.read_text(encoding="utf-8")
old = "^\\\\tau in 4.3 and 4.7)"
new = "^\\\\tau further on in the section)"
assert t.count(old) == 1, t.count(old)
t = t.replace(old, new)
p.write_text(t, encoding="utf-8", newline="\n")
print("ok")
