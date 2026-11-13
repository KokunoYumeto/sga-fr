"""Rewrite the folio-429 marker note so that the quoted main.tex strings hold no apostrophe."""
import json

P = r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\findings_426_430.json"
BS = chr(92)
NL = BS + "n"  # the two characters backslash-n, as the notes write a line break
MARK = "%%%%%%%%%%  scan idx 442  |  folio 429  %%%%%%%%%%"
d = json.load(open(P, encoding="utf-8"))
n = 0
for x in d:
    if x["page"] == 429 and x["kind"] == "marker":
        old_q = "replace 'c'est donc le" + NL + MARK + NL + "composé de deux' by 'c'est donc" + NL + MARK + NL + "le composé de deux'"
        new_q = "replace 'donc le" + NL + MARK + NL + "composé de deux' by 'donc" + NL + MARK + NL + "le composé de deux'"
        assert x["note"].count(old_q) == 1, x["note"]
        x["note"] = x["note"].replace(old_q, new_q)
        n += 1
assert n == 1
with open(P, "w", encoding="utf-8", newline="\n") as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("rewritten", n)
