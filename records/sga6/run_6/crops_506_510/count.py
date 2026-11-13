import sys
base = r"C:/Users/user/Documents/sga_scan_check_20261105/run_6/b506_510"
pats = [r"K^\circ", r"K_\bullet", r"\mathcal O", r"\underline", r"\emph", r"\Lambda", r"\mathbb"]
for p in range(506, 511):
    t = open(f"{base}/page_{p}.tex", encoding="utf-8").read()
    print(p, {q: t.count(q) for q in pats})
