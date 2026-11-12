"""List every CONT>> / <<CONT tag of expose_IX_body.tex with its folio and context (read-only).

usage: python -I analyze_cont.py FILE [--full]
"""
import re
import sys

MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
TAG = re.compile(r"CONT>>|<<CONT")

sys.stdout.reconfigure(encoding="utf-8")
path = sys.argv[1]
full = "--full" in sys.argv
t = open(path, encoding="utf-8", newline="").read()
marks = [(m.start(), int(m.group(2))) for m in MARK.finditer(t)]


def folio_at(pos):
    f = None
    for s, fo in marks:
        if s <= pos:
            f = fo
        else:
            break
    return f


tags = [(m.start(), m.group(0)) for m in TAG.finditer(t)]
print("tags:", len(tags), "markers:", len(marks))
# pairing: sequence
i = 0
pairs = []
unp = []
while i < len(tags):
    p, k = tags[i]
    if k == "CONT>>":
        if i + 1 < len(tags) and tags[i + 1][1] == "<<CONT":
            pairs.append((tags[i], tags[i + 1]))
            i += 2
            continue
        unp.append(tags[i])
        i += 1
    else:
        unp.append(tags[i])
        i += 1
print("pairs:", len(pairs), "unpaired:", len(unp))
for p, k in unp:
    print("UNPAIRED", k, "folio", folio_at(p), "line", t.count("\n", 0, p) + 1)
    print("   ", repr(t[max(0, p - 300):p + 300]))
if full:
    for n, ((a, _), (b, _)) in enumerate(pairs):
        mid = t[a + 6:b]
        nm = len(MARK.findall(mid))
        has_fn = bool(re.search(r"^\s*\(\*+\)", mid, re.M))
        print(f"--- pair {n + 1}: folio {folio_at(a)} -> {folio_at(b)} lines {t.count(chr(10), 0, a) + 1}-"
              f"{t.count(chr(10), 0, b) + 1} markers_between={nm} footnote_between={has_fn} midlen={len(mid)}")
        print("  BEFORE:", repr(t[max(0, a - 120):a + 6]))
        if len(mid) < 400:
            print("  MID   :", repr(mid))
        else:
            print("  MID   :", repr(mid[:200]), "...", repr(mid[-200:]))
        print("  AFTER :", repr(t[b:b + 120]))
