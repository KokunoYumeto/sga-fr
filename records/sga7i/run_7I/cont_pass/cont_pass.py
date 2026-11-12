"""CONT pass on SGA 7 I, Exposé IX (8 Nov 2026): remove the transcriber's continuation tags CONT>> and <<CONT (and the
one variant \\mathrm{CONT{>}{>}}) from expose_IX_body.tex, join the words that a page break splits, log every edit.

Rules (from the coordinator's brief):
1. Remove every tag with the space that separates it from the text; in formulas also the spacing command next to
   the tag (\\quad \\text{CONT>>}, \\qquad CONT>>, <<CONT\\quad); punctuation stays.
2a. Word split, only blank lines and the marker line between the fragments: the first fragment ends with %, the blank
   lines on both sides of the marker line go, the marker line stays on its own line.
2b. Word split with footnote paragraphs between: the whole word goes at the end of the first page's text, the next
   page's text begins with what follows the fragment (leading space stripped). Punctuation attached to the second
   fragment (no space between them) moves back with it.
3. Split between words: the tags are removed, nothing else.

Every tag is one edit and one log line {"vol", "file", "page", "old", "new", "kind": "marker", "source"}; old and new
carry enough context to be unique in the file and never contain a marker line.

usage: python -I cont_pass.py LAYER [--apply]     LAYER = diplomatic | current
Without --apply the result goes to cont_pass/preview_<layer>.tex and the log lines to cont_pass/preview_<layer>.jsonl;
with --apply the edition file is rewritten (LF, UTF-8) and the lines are appended to the layer's FIXLOG.
A detailed record of every edit (tag, rule, pairing) goes to cont_pass/edits_<layer>.json in both modes.
"""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
LAYERS = {"diplomatic": (W / "sga7i" / "diplomatic" / "expose_IX_body.tex", W / "FIXLOG_7I.jsonl"),
          "current": (W / "sga7i" / "current" / "expose_IX_body.tex", W / "FIXLOG_7I_CURRENT.jsonl")}
SOURCE = "CONT pass 8 Nov 2026"
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
TAG = re.compile(r"\\text\{ ?CONT>>\}|\\mathrm\{CONT\{>\}\{>\}\}|CONT>>|<<CONT")
DISPLAY = re.compile(r"\\(begin|end)\{(equation\*?|align\*?|gather\*?|multline\*?)\}")
# Words that a page break splits (decided from the French): folio of the first fragment -> fragments, rule
SPLITS = {315: ("singula", "rités", "2b"), 406: ("isomor", "phisme", "2a"), 460: ("l'ex", "tension", "2a"),
          502: ("épimor", "phisme", "2a")}

layer = sys.argv[1]
apply = "--apply" in sys.argv
path, fixlog = LAYERS[layer]
t = path.read_bytes().decode("utf-8")
assert "\r" not in t
marks = [(m.start(), m.end(), int(m.group(2))) for m in MARK.finditer(t)]


def folio_at(pos):
    f = None
    for s, _, fo in marks:
        if s > pos:
            break
        f = fo
    return f


def in_display(pos):
    last = None
    for m in DISPLAY.finditer(t, 0, pos):
        last = m.group(1)
    return last == "begin"


def marks_between(a, b):
    return [m for m in marks if a <= m[0] and m[1] <= b]


tags = [(m.start(), m.end(), "end" if "CONT>" in m.group(0) or "CONT{" in m.group(0) else "start", m.group(0))
        for m in TAG.finditer(t)]
# pairing: an end tag whose next tag is a start tag with exactly one marker line and nothing but blank lines and
# footnote paragraphs between them
partner = {}
for i, (s, e, k, _) in enumerate(tags):
    if k == "end" and i + 1 < len(tags) and tags[i + 1][2] == "start":
        s2 = tags[i + 1][0]
        if len(marks_between(e, s2)) == 1:
            partner[i], partner[i + 1] = i + 1, i
edits = []  # (span start, span end, replacement, record)
for i, (s, e, k, tok) in enumerate(tags):
    folio = folio_at(s)
    disp = in_display(s)
    rec = dict(n=i, tag=tok, side=k, folio=folio, in_formula=disp, paired=i in partner,
               partner_folio=folio_at(tags[partner[i]][0]) if i in partner else None, rule="1+3")
    if k == "end":
        a = s
        while True:  # the space (and in formulas the spacing command) that separates the tag from the text
            while a > 0 and t[a - 1] in " \t":
                a -= 1
            m = re.search(r"\\q?quad$", t[max(0, a - 7):a])
            if disp and m:
                a -= len(m.group(0))
                continue
            break
        if t[a - 1] == "\n":  # tag alone on its line: remove the line
            assert t[a - 2] != "\n"
            a -= 1
        span = (a, e)
        repl = ""
        sp = SPLITS.get(folio)
        if sp and i in partner:
            first, second, rule = sp
            assert t[:a].endswith(first), (folio, t[a - 20:a])
            j = partner[i]
            s2, e2 = tags[j][0], tags[j][1]
            assert t[e2:].startswith(" " + second), (folio, t[e2:e2 + 20])
            rec["rule"] = rule
            rec["word"] = first + second
            if rule == "2a":
                mk = marks_between(e, s2)[0]
                assert t[e:mk[0]].strip("\n") == "" and t[mk[1]:s2].strip("\n") == ""
                span, repl = (a, mk[0]), "%\n"
            else:  # 2b: the whole word on the first page, with the punctuation attached to its second fragment
                tail = re.match(re.escape(" " + second) + r"[,.;:)]*", t[e2:]).group(0)[1:]
                repl = tail
                rec["moved_back"] = tail
        edits.append((span[0], span[1], repl, rec))
    else:
        b = e
        while b < len(t) and t[b] in " \t":
            b += 1
        m = re.match(r"\\q?quad(?![A-Za-z]) *", t[b:])
        if disp and m:
            b += len(m.group(0))
        span, repl = (s, b), ""
        j = partner.get(i)
        sp = SPLITS.get(folio_at(tags[j][0])) if j is not None else None
        if sp:
            first, second, rule = sp
            rec["rule"] = rule
            rec["word"] = first + second
            if rule == "2a":
                mk = marks_between(tags[j][1], s)[0]
                assert t[mk[1]] == "\n"
                span = (mk[1] + 1, b)  # the blank line(s) after the marker line and the tag with its space
                assert t[span[0]:s].strip("\n") == ""
            else:
                tail = re.match(re.escape(second) + r"[,.;:)]*", t[b:]).group(0)
                b2 = b + len(tail)
                while b2 < len(t) and t[b2] in " \t":
                    b2 += 1
                span = (s, b2)
        edits.append((span[0], span[1], repl, rec))

# old/new with unique context; no edit may overlap another or touch a marker line
edits.sort()
lines, out = [], []
prev_end = 0
for k, (a, b, repl, rec) in enumerate(edits):
    assert a >= prev_end, ("overlap", rec)
    nxt = edits[k + 1][0] if k + 1 < len(edits) else len(t)
    if rec["side"] == "end":
        c = a - 12
        while True:
            while c > 0 and (not t[c - 1].isspace() or t[c - 2] == "\\"):  # a control space is not a boundary
                c -= 1
            old = t[c:b]
            if t.count(old) == 1:
                break
            c -= 8
        assert c >= prev_end and "\n\n" not in t[c:a], ("context", rec)
        old, new = t[c:b], t[c:a] + repl
        win = (c, b)
    else:
        d = b + 12
        while True:
            while d < len(t) and (not t[d].isspace() or t[d - 1] == "\\"):
                d += 1
            old = t[a:d]
            if t.count(old) == 1:
                break
            d += 8
        assert d <= nxt and "\n\n" not in t[b:d], ("context", rec)
        old, new = t[a:d], repl + t[b:d]
        win = (a, d)
    assert not MARK.search(old) and not MARK.search(new)
    prev_end = win[1]
    rec.update(old=old, new=new, removed=t[a:b], replacement=repl)
    out.append(rec)
    assert folio_at(a) == rec["folio"]
    lines.append(dict(vol="7I", file="expose_IX_body.tex", page=rec["folio"], old=old, new=new, kind="marker",
                      source=SOURCE))
res = t
for a, b, repl, rec in sorted(edits, reverse=True):
    res = res[:a] + repl + res[b:]
assert not re.search(r"CONT>>|<<CONT|CONT\{>\}\{>\}", res)
assert [m.group(0) for m in MARK.finditer(res)] == [m.group(0) for m in MARK.finditer(t)]
(HERE / f"edits_{layer}.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
if apply:
    path.write_bytes(res.encode("utf-8"))
    with open(fixlog, "a", encoding="utf-8") as fh:
        for x in lines:
            fh.write(json.dumps(x, ensure_ascii=False) + "\n")
else:
    (HERE / f"preview_{layer}.tex").write_bytes(res.encode("utf-8"))
    with open(HERE / f"preview_{layer}.jsonl", "w", encoding="utf-8") as fh:
        for x in lines:
            fh.write(json.dumps(x, ensure_ascii=False) + "\n")
n_end = sum(1 for r in out if r["side"] == "end")
print(f"{layer}: {len(out)} tags removed ({n_end} end, {len(out) - n_end} start), "
      f"2a {sum(1 for r in out if r['rule'] == '2a' and r['side'] == 'end')}, "
      f"2b {sum(1 for r in out if r['rule'] == '2b' and r['side'] == 'end')}, "
      f"unpaired {sum(1 for r in out if not r['paired'])}" + ("" if apply else " (preview)"))
