import pathlib

p = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\crops_626_630\make_findings.py")
s = p.read_text(encoding="utf-8")
R = [
    ("le', \"\n        r\"main.tex line 15926).\",", "le').\","),
    ("Donc par (i) \"\n        \"déjà', main.tex line 16025).\",", "Donc par (i) \"\n        \"déjà').\","),
    (", main.tex lines 16054-16058) stands below the ", ") stands below the "),
    ("(the string occurs once there, line 16057)", "(the string occurs once there)"),
    ("provided for this exposé at main.tex line 15697; same fix as the p. 164 finding)",
     "provided in the Exposé XIII local macros of main.tex; same fix as the p. 164 finding)"),
]
for a, b in R:
    n = s.count(a)
    print(n, repr(a[:50]))
    if n == 1:
        s = s.replace(a, b)
p.write_text(s, encoding="utf-8")
print("line refs left:", s.count("main.tex line"))
