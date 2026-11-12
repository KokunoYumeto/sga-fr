import json
B = chr(92)
p = r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\findings_251_255.json"
L = json.load(open(p, encoding="utf-8"))
x = L[4]
assert x["page"] == 252 and x["fix"]["old"].startswith("g_" + B + "alpha^*(F)" + B + "xrightarrow")
a = "g_" + B + "alpha^*(F_" + B + "alpha)"
x["note"] += (" On the current layer, which already reads " + a + " here, the same edit is old '" + a + B + "xrightarrow{" + B
              + "sim}F_" + B + "alpha', new '" + a + B + "simeq F_" + B + "alpha'.")
with open(p, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(L, fh, ensure_ascii=False, indent=2)
    fh.write("\n")
print(x["note"])
