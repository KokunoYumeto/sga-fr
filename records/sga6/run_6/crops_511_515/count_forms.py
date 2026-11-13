import re, sys, pathlib
sys.stdout.reconfigure(encoding="utf-8")
B = pathlib.Path(__file__).resolve().parent.parent / "b511_515"
BS = chr(92)
for p in range(511, 516):
    t = (B / f"page_{p}.tex").read_text(encoding="utf-8")
    body = t.split("\n", 2)[2]
    kc = body.count("K^" + BS + "circ")
    sym = len(re.findall(r"(?<![A-Za-z\\_^{])S\((?!\))", body))
    sub = body.count("_{0,")
    und = body.count(BS + "underline")
    mbbD = len(re.findall(r"(?<![A-Za-z\\])D\(", body))
    print(p, "K^circ:", kc, "S(:", sym, "_{0,:", sub, "underline:", und, "D(:", mbbD)
    for m in re.finditer(r"(?<![A-Za-z\\_^{])S\((?!\))", body):
        print("   S( at", repr(body[max(0, m.start()-25):m.end()+10]))
