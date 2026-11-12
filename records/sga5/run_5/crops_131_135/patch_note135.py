import pathlib

p = pathlib.Path(__file__).parent / "build_findings.py"
s = p.read_text(encoding="utf-8")
a = s.index('    "\'\\\\subsection*{6.14}\' and \'La\' (s5.tex lines 4308-4309) end page_134.tex;')
b = s.index('The moved words agree with the print.")', a) + len('The moved words agree with the print.")')
new = '''    "'\\\\subsection*{6.14}' and 'La' (s5.tex lines 4308-4309 at 20:13) end page_134.tex; the folio-135 marker "
    "(line 4310) follows them, so page_135.tex begins 'formule de Woods Hole'", "marker", "high",
    note="Page 135 really begins at '\\\\subsection*{6.14}', s5.tex line 4308 at 20:13. Exact fix: python -I "
         "move_marker.py 5 135 '\\\\subsection*{6.14}' --before (single quotes; simulated in memory on both layers: "
         "the marker then stands on its own line between '... la condition $(C_1)$.' and '\\\\subsection*{6.14}', "
         "and 'La' joins 'formule de Woods Hole'). The moved words agree with the print.")'''
s = s[:a] + new + s[b:]
s = s.replace("then the three marker moves.", "then the two marker moves.")
p.write_text(s, encoding="utf-8")
print("patched")
