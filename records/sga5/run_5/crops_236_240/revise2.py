"""Drop the p. 236 '\\end{prooftext}' item: the coordinator removed that line when applying findings_231_235.json."""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
P = r"C:/Users/user/Documents/sga_scan_check_20261105/run_5/findings_236_240.json"
items = json.load(open(P, encoding="utf-8"))
keep = [x for x in items if not (x["fix"] and x["fix"]["old"].startswith("proposition suivante."))]
print(len(items), "->", len(keep))
json.dump(keep, open(P, "w", encoding="utf-8", newline=""), ensure_ascii=False, indent=1)
