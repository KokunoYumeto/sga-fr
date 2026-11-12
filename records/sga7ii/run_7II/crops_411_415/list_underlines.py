import sys

sys.stdout.reconfigure(encoding="utf-8")
base = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II\b411_415"
key = chr(92) + "underline{"
for p in (411, 412, 413, 414, 415):
    t = open(base + f"\\page_{p}.tex", encoding="utf-8").read()
    k = t.find(key)
    while k >= 0:
        i = k + len(key)
        depth = 1
        while depth:
            c = t[i]
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
            i += 1
        print(p, repr(t[k:i]))
        k = t.find(key, i)
