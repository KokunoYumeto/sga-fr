"""Print repr() of selected snippets of the page TeX files (to get exact whitespace)."""
import sys

folder = sys.argv[1]
probes = {
    236: ["annulé par", "incl.", "(pq)^{*}\"]", "\\end{tikzcd}}", "diagram.\n"],
    237: ["Biext}^1(P,Q;G)\n"],
    238: ["\\varphi^n_{P,Q}", "(P,Q;G)$", "accouplements"],
    240: ["T_\\ell(G) \\arrow"],
}
for page, keys in probes.items():
    with open(f"{folder}/page_{page}.tex", encoding="utf-8", newline="") as f:
        t = f.read()
    print(page, "CRLF" if "\r\n" in t else "LF", "ends with:", repr(t[-30:]))
    for k in keys:
        i = t.find(k)
        print("  ", repr(k), "count", t.count(k), "->", repr(t[max(0, i - 40): i + len(k) + 40]))
