import pathlib
BS = "\\"  # one backslash character
p = pathlib.Path(__file__).with_name("build_findings.py")
lines = p.read_text(encoding="utf-8").split("\n")
# heading note (editor lines 176-177 -> indices 175-176)
old_a = '          "(' + BS * 2 + "subsection*{1.2} for the print's '1.2.' on p. 522, " + BS * 2 + "subsection*{1.3} for '1.3.' on p. 523, also 1.1, 2.1-5.3): a \""
old_b = '          "convention for one decision.")))'
assert lines[175] == old_a, repr(lines[175])
assert lines[176] == old_b, repr(lines[176])
lines[175] = ('          "(' + BS * 2 + "subsection*{1.2} for the print's '1.2.' on p. 522, " + BS * 2
              + "subsection*{1.3} for '1.3.' on p. 523, " + BS * 2 + "subsection*{2.1} for '2.1.' on p. 531; \"")
lines[176] = '          "the other headings 1.1 to 5.3 are written the same way): a convention for one decision.")))'
# convention note (editor line 83 -> index 82)
tail = "underline{k}(x)]'.\")))"
assert lines[82].endswith(tail), repr(lines[82])
lines[82] = lines[82][: -len(".\")))")] + ". \""
lines.insert(83, "          \"If adopted, edit 'sur $k(e)$, car ces' only after the folio-526 marker move, whose old string contains it.\")))")
p.write_text("\n".join(lines), encoding="utf-8")
print("ok")
