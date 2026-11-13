"""One-off patch of build_findings.py: marker strings shown with single backslashes and \\n for line breaks,
double low line for the doubly underlined P, and the count of the remaining Omegas on p. 481."""
import pathlib
p = pathlib.Path(__file__).resolve().parent / "build_findings.py"
s = p.read_text(encoding="utf-8")
s = s.replace("def T(s):\n    return s.replace(NL, \"\\n\")\n",
              "def T(s):\n    return s.replace(NL, \"\\n\")\n\n\ndef Q(s):\n    return \"'\" + s.replace(\"\\n\", \"\\\\n\") + \"'\"\n", 1)
for name in ("OLD482", "NEW482", "OLD485", "NEW485"):
    s = s.replace("json.dumps(%s, ensure_ascii=False)" % name, "Q(%s)" % name, 1)
s = s.replace("P\u033f", "P\u0333")
s = s.replace("the other ten Omega and", "the other nine Omega (first display, (2.6.2), the diagram) and", 1)
p.write_text(s, encoding="utf-8")
print("patched")
