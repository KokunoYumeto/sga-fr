import pathlib
p = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\crops_316_320\build_findings.py")
t = p.read_text(encoding="utf-8")
old = r"""r"then stands on its own line between '... le morphisme canonique, les' and 'faisceaux $\R^it_*(t^*M)$'). "
           r"Text not moved."))"""
new = r"""r"then stands on its own line between '... le morphisme canonique, les' and 'faisceaux $\R^it_*(t^*M)$'). "
           r"Text not moved. Both live layers (s5.tex as modified 12 Nov 15:46) already have the marker there; the "
           r"command leaves it in place."))"""
assert t.count(old) == 1, t.count(old)
t = t.replace(old, new)
old2 = r"""r"'... est sans torsion.' and '\item'). Text not moved."))"""
new2 = r"""r"'... est sans torsion.' and '\item'). Text not moved. The live layers (12 Nov 15:46) still have '\item' "
           r"before the folio-321 marker."))"""
assert t.count(old2) == 1, t.count(old2)
t = t.replace(old2, new2)
p.write_text(t, encoding="utf-8", newline="\n")
print("patched")
