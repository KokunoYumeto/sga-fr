import sys
sys.stdout.reconfigure(encoding="utf-8")
B = r"C:/Users/user/Documents/sga_scan_check_20261105/run_5/b016_020"
for p in range(16, 21):
    t = open(f"{B}/page_{p:03d}.tex", encoding="utf-8").read()
    for pat in (r"\xrightarrow{\sim}", r"\uH"):
        k = 0
        n = 0
        while True:
            i = t.find(pat, k)
            if i < 0:
                break
            n += 1
            print(p, pat[:5], n, repr(t[max(0, i - 40):i + len(pat) + 30]))
            k = i + 1
