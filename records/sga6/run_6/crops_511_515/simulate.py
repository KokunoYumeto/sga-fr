import json, sys, pathlib, re
sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
B = HERE.parent / "b511_515"
d = json.loads((HERE.parent / "findings_511_515.json").read_text(encoding="utf-8"))
for p in range(511, 516):
    t = (B / f"page_{p}.tex").read_text(encoding="utf-8")
    for f in d:
        if f["page"] == p and f.get("fix"):
            assert t.count(f["fix"]["old"]) == 1, (p, f["fix"]["old"])
            t = t.replace(f["fix"]["old"], f["fix"]["new"])
    (HERE / f"patched_{p}.tex").write_text(t, encoding="utf-8", newline="\n")
    body = t.split("\n", 2)[2]
    # crude balance checks
    dollars = len(re.findall(r"(?<!\\)\$", body))
    opens = body.count("\\[")
    closes = body.count("\\]")
    print(p, "dollars even:", dollars % 2 == 0, "display open/close:", opens, closes)
print(open(HERE / "patched_514.tex", encoding="utf-8").read()[-900:])
print("-----")
print(open(HERE / "patched_515.tex", encoding="utf-8").read()[:1400])
