"""One-off patch of build_findings.py (exact substring replacements, each must match once)."""
import pathlib

p = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\crops_381_385\build_findings.py")
s = p.read_text(encoding="utf-8")
R = [
    (r'''    "\\otimes_\\Lambda^{\\mathbb{L}}", "\\otimes_\\Lambda^{\\mathbb{L}}",''',
     r'''    "\\otimes_\\Lambda^{\\mathbf L}", "\\otimes_\\Lambda^{\\mathbb{L}}",'''),
    (r'''Text not moved; the moving words read as the print.")''',
     r'''Text not moved; the moving words read as the print. Live layers (s5.tex as modified 12 Nov "
         "16:17): the marker already stands there (diplomatic line 12952, current 12948); the command then prints "
         "'anchor not found' and changes nothing.")'''),
    (r'''diplomatic s5.tex line 12969, current 12965)''',
     r'''diplomatic s5.tex line 12984, current 12980 in the live files of 16:17)'''),
    (r'''(diplomatic s5.tex line 13042, "''', r'''(diplomatic s5.tex line 13041, "'''),
    (r'''"current 13038)''', r'''"current 13037 in the live files of 16:17)'''),
    (r'''(diplomatic s5.tex line 13073, current 13069)''',
     r'''(diplomatic s5.tex line 13072, current 13068 in the live files of 16:17)'''),
    (r'''(diplomatic s5.tex line 13116, current 13112)''',
     r'''(diplomatic s5.tex line 13116, current 13112 before the move)'''),
    (r'''Run it once (batch 386-390 may report the same move). Text not moved.")''',
     r'''Already done in both live layers (s5.tex as modified 12 Nov 16:17: the marker "
         "stands directly before '\\subsubsection*{4.3.}', diplomatic line 13115, current 13111); the command then "
         "prints 'anchor not found' and changes nothing. Text not moved.")'''),
    (r'''the move's anchor '\\subsubsection*{4.3', so either order works).")''',
     r'''the move's anchor '\\subsubsection*{4.3', so either order works). Already applied in both live "
    "layers (16:17: '\\subsubsection*{4.3.}' under the folio-386 marker).")'''),
    (r'''    c = page_span(cur, p).count(old)''',
     r'''    c = page_span(cur, p).count(old)
    live = DIP.read_text(encoding="utf-8").count(old)'''),
    (r'''    print(f"p{p} n={n} cur={c} {d['kind']:<18} {old[:60]!r}{flag}")''',
     r'''    print(f"p{p} n={n} cur={c} live_dipl_file={live} {d['kind']:<18} {old[:50]!r}{flag}")'''),
    (r'''NL = "\u23ce"''',
     r'''DIP = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5\diplomatic\s5.tex")
NL = "\u23ce"'''),
]
for a, b in R:
    n = s.count(a)
    assert n == 1, (n, a)
    s = s.replace(a, b)
p.write_text(s, encoding="utf-8", newline="")
print("patched", len(R))
