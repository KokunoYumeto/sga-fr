import io, json, pathlib, collections
run = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I")
data = json.load(io.open(run / "findings_281_285_recheck.json", encoding="utf-8"))
counts = collections.defaultdict(lambda: [0, 0])
ok = True
for i, f in enumerate(data):
    p = f["page"]
    t = io.open(run / "b281_285" / f"page_{p}.tex", encoding="utf-8").read()
    for key in ("page", "where", "scan", "tex", "kind", "confidence", "fix", "note"):
        if key not in f:
            print(i, "missing key", key); ok = False
    if f["kind"] == "misprint_in_print":
        counts[p][1] += 1
        if "corrected" not in f:
            print(i, "misprint without corrected"); ok = False
    else:
        counts[p][0] += 1
    fx = f["fix"]
    if fx is not None:
        n = t.count(fx["old"])
        if n != 1:
            print(i, "fix old occurs", n, "times"); ok = False
    n = t.count(f["tex"])
    if n != 1:
        print(i, "tex occurs", n, "times:", repr(f["tex"])); ok = False
    if f["kind"] == "misprint_in_print":
        a, b = f["tex"], f["corrected"]
        # common prefix/suffix -> changed span
        k = 0
        while k < min(len(a), len(b)) and a[k] == b[k]:
            k += 1
        m = 0
        while m < min(len(a), len(b)) - k and a[-1 - m] == b[-1 - m]:
            m += 1
        print(p, "change:", repr(a[k:len(a) - m]), "->", repr(b[k:len(b) - m]))
print({p: f"{c[0]}/{c[1]}" for p, c in sorted(counts.items())})
print("OK" if ok else "PROBLEMS")
