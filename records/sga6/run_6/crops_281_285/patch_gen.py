p = r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\crops_281_285\make_findings.py"
s = open(p, encoding="utf-8").read()

old1 = '''    "(V 3.9.1 et VI) que",
    "other", "low",
    old="et VI) que", new=r"et VI\\qquad) que",
    note="Unfilled reference left blank in the typescript; the TeX closes the gap. Keep the blank if the diplomatic layer shows such gaps.")'''
new1 = '''    "(V 3.9.1 et VI) que (gap closed)",
    "misprint_in_print", "low",
    old="et VI) que", new=r"et VI\\qquad) que",
    corrected="(V 3.9.1 et VI)",
    note="Unfilled reference: the typist left a blank for a number in VI that was never typed in; the TeX closed the gap. The diplomatic fix keeps the blank; the corrected layer keeps '(V 3.9.1 et VI)' (the intended reference in VI is not known).")'''
assert s.count(old1) == 1, s.count(old1)
s = s.replace(old1, new1)

old2 = 'Exposé IV has 8 more \\\\mathbf L for the derived tensor (main.tex about lines 6890-7150), not checked here.'
new2 = 'Exposé IV has 8 more \\\\mathbf L for the derived tensor (main.tex lines 6893, 6920, 6921, 7013, 7017 (two), 7102, 7147), not checked here.'
assert s.count(old2) == 1, s.count(old2)
s = s.replace(old2, new2)
open(p, "w", encoding="utf-8", newline="\n").write(s)
print("patched")
