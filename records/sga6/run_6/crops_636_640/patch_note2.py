import pathlib
p = pathlib.Path(__file__).with_name("build_findings.py")
t = p.read_text(encoding="utf-8")
old = '+ json.dumps(M_OLD, ensure_ascii=False) + " by " + json.dumps(M_NEW, ensure_ascii=False)'
new = '+ "\\"" + M_OLD.replace("\\n", "\\\\n") + "\\" by \\"" + M_NEW.replace("\\n", "\\\\n") + "\\""'
assert t.count(old) == 1, t.count(old)
t = t.replace(old, new)
p.write_text(t, encoding="utf-8", newline="\n")
print("ok")
