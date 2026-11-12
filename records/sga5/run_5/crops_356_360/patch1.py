import pathlib

p = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\crops_356_360\build_findings.py")
s = p.read_text(encoding="utf-8")
old1 = r'''r"Guillemets for the print's straight quotes (the accepted forms are ``...'' and \"...\"). Exposé VIII has "'''
new1 = r'''r"Guillemets for the print's straight quotes (the accepted forms are ``...'' and plain double quotes). Exposé VIII has "'''
old2 = "Unlike the two-stroke ≃ of pp. 359 (four times)"
new2 = "Unlike the two-stroke ≃ of p. 359 (four times)"
print(s.count(old1), s.count(old2))
s = s.replace(old1, new1).replace(old2, new2)
p.write_text(s, encoding="utf-8")
