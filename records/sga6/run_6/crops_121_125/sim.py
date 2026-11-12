"""Simulate (in memory; main.tex is only read) the fixes of findings_121_125 (as built by make_findings.py, file
applied/ not used) and the four marker moves of pp. 121, 122, 124, 125 on both layers of SGA 6 main.tex, in both
orders (fixes first / markers first), with the logic of move_marker.py. Print the text around the moved markers and
write the diplomatic region pp. 120-125 (fixes, then markers) into a small test document test_121_125.tex.
usage: python -I sim.py"""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
W = HERE.parents[1]
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
FINDINGS = json.loads((HERE.parent / "findings_121_125.json").read_text(encoding="utf-8")) \
    if (HERE.parent / "findings_121_125.json").exists() else None
# p. 121 (anchor 'si \(F\) est') was already moved in main.tex from findings_116_120.json (19:51); not repeated
MOVES = [(122, r"\(F'\to F\)"), (124, "est"), (125, "Soit")]


def span(t, folio):
    ms = list(MARK.finditer(t))
    for i, m in enumerate(ms):
        if int(m.group(2)) == folio:
            return m.start(), (ms[i + 1].start() if i + 1 < len(ms) else len(t))
    raise SystemExit(f"no folio {folio}")


def fix_on_page(t, folio, old, new, log):
    s, e = span(t, folio)
    seg = t[s:e]
    n = seg.count(old)
    if n != 1:
        log.append(f"  fix on {folio} occurs {n} times: {old[:50]!r}")
        return t
    return t[:s] + seg.replace(old, new) + t[e:]


def move(t, folio, anchor):
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start())
    if k < 0:
        print("  anchor not found", repr(anchor))
        return t
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        return t2[:ls] + line + "\n" + t2[ls:]
    return t2[:k] + "\n" + line + "\n" + t2[k:]


def fixes(findings):
    return [(f["page"], f["fix"]["old"], f["fix"]["new"]) for f in findings if f["fix"]]


def run(t, findings, order):
    log = []
    if order == "fixes-first":
        for p, o, n in fixes(findings):
            t = fix_on_page(t, p, o, n, log)
        for f, a in MOVES:
            t = move(t, f, a)
    else:
        for f, a in MOVES:
            t = move(t, f, a)
        for p, o, n in fixes(findings):
            t = fix_on_page(t, p, o, n, log)
    return t, log


if FINDINGS is None:
    raise SystemExit("write findings_121_125.json first (make_findings.py --write)")
for edition in ("diplomatic", "current"):
    t0 = (W / "sga6" / edition / "main.tex").read_text(encoding="utf-8")
    for order in ("fixes-first", "markers-first"):
        t, log = run(t0, FINDINGS, order)
        print(f"== {edition}, {order}: {len(log)} fixes not applied")
        for x in log:
            print(x)
        if order == "fixes-first":
            for f in (121, 122, 124, 125):
                s, _ = span(t, f)
                print(f"-- folio {f}:")
                print(t[s - 110:s + 120])
            if edition == "diplomatic":
                s, _ = span(t, 120)
                _, e = span(t, 125)
                pre = t[:t.index("\\begin{document}")]
                lines = t0.split("\n")
                macros = "\n".join(lines[1835:1858]) + "\n" + "\n".join(lines[2316:2333])
                doc = pre + "\\begin{document}\n" + macros + "\n" + t[s:e] + "\n\\end{document}\n"
                (HERE / "test_121_125.tex").write_text(doc, encoding="utf-8", newline="\n")
                print("test document written")
