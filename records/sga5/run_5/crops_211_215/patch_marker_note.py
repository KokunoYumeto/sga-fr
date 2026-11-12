"""One-off: add the duplicate notice to the p. 211 marker note in make_findings.py."""
import pathlib

p = pathlib.Path(__file__).with_name("make_findings.py")
s = p.read_text(encoding="utf-8")
a = r'''    r"'à $S$,' / 'peut se compléter ...'). Text not moved.")'''
b = (r'''    r"'à $S$,' / 'peut se compléter ...'). Text not moved. The same marker problem, with the same command, is filed "'''
     "\n"
     r'''    r"under page 210 in findings_206_210.json: apply it ONCE (a second run would move the marker back to the "'''
     "\n"
     r'''    r"earlier 'appartient à $S$, peut' of Définition 2.3.1 (c)).")''')
print(s.count(a))
s = s.replace(a, b)
p.write_text(s, encoding="utf-8")
