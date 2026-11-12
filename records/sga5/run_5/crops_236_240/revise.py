"""Revise findings_236_240.json: add the p. 236 end of the 5.1.5 proof (pair with the p. 235 label fix of
findings_231_235.json) and keep a blank line before the two lemma statements where an end of prooftext is removed."""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
BS, NL = chr(92), chr(10)
P = r"C:/Users/user/Documents/sga_scan_check_20261105/run_5/findings_236_240.json"
items = json.load(open(P, encoding="utf-8"))
assert not any("proposition suivante." in (x["fix"] or {}).get("old", "") for x in items)
for x in items:
    f = x["fix"]
    if f and f["old"].startswith(BS + "end{prooftext}" + NL + NL + BS + "begin{statement}{Lemme"):
        f["new"] = NL + f["new"]
new_item = {
    "page": 236, "where": "top of the page: end of the proof of Corollaire 5.1.5 (begun on p. 235)",
    "scan": "'... par l'intermédiaire de la proposition suivante.' then PROPOSITION 5.1.6 (no end mark); the proof opens on p. 235 with underlined 'Preuve :'",
    "tex": BS + "end{prooftext} after 'proposition suivante.'",
    "kind": "extra", "confidence": "high",
    "fix": {"old": "proposition suivante." + NL + BS + "end{prooftext}" + NL, "new": "proposition suivante." + NL},
    "note": "Pair G, across batches: goes with the p. 235 label fix of findings_231_235.json ('" + BS + "begin{prooftext}"
            + BS + "nOn se ramène au cas où' -> '" + BS + "emph{Preuve} : On se ramène au cas où'), whose note names this edit "
            "but lists no p. 236 fix; apply both or neither."}
items.insert(0, new_item)
json.dump(items, open(P, "w", encoding="utf-8", newline=""), ensure_ascii=False, indent=1)
print(len(items), "items written")
