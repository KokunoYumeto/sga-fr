"""Check findings_331_335.json: every fix's old occurs exactly once in its page file; no marker lines touched;
misprints carry 'corrected'; the literal marker replacements of the notes match once in both layers of main.tex.
Reads only; writes nothing."""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
SGA6 = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
KINDS = {"word", "formula", "symbol", "font", "underline", "missing", "extra", "number", "punctuation", "accent",
         "misprint_in_print", "marker", "other"}

items = json.loads((RUN / "findings_331_335.json").read_text(encoding="utf-8"))
ok = True
for n, x in enumerate(items):
    page = int(x["page"])
    folder = "b331_335" if 331 <= page <= 335 else "b326_330"
    tex = (RUN / folder / f"page_{page:03d}.tex").read_text(encoding="utf-8")
    assert x["kind"] in KINDS, x["kind"]
    assert x["confidence"] in {"high", "medium", "low"}
    for key in ("where", "scan", "tex", "note"):
        s = x.get(key) or ""
        if re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", s):
            print("CONTROL CHAR in", n, key); ok = False
    if x["kind"] == "misprint_in_print" and not x.get("corrected"):
        print("misprint without corrected:", n); ok = False
    if x["kind"] != "misprint_in_print" and "corrected" in x:
        print("corrected on a non-misprint:", n); ok = False
    fix = x.get("fix")
    if fix is None:
        print(f"[{n}] p.{page} {x['kind']}: fix null")
        continue
    old, new = fix["old"], fix["new"]
    c = tex.count(old)
    marker = bool(MARK.search(old) or MARK.search(new))
    ctl = bool(re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", old + new))
    print(f"[{n}] p.{page} {x['kind']}: count={c} marker={marker} ctl={ctl}")
    print("    old:", repr(old))
    print("    new:", repr(new))
    if c != 1 or marker or ctl:
        ok = False

# literal marker replacements quoted in the notes (old -> new), checked on both layers
lit = [
    ("\\textbf{3.10.}\n%%%%%%%%%%  scan idx 344  |  folio 331  %%%%%%%%%%\nSoit",
     "%%%%%%%%%%  scan idx 344  |  folio 331  %%%%%%%%%%\n\\textbf{3.10.}\nSoit"),
    ("qui se trouve ainsi muni d'une\n%%%%%%%%%%  scan idx 347  |  folio 334  %%%%%%%%%%\nstructure de",
     "qui se trouve ainsi muni\n%%%%%%%%%%  scan idx 347  |  folio 334  %%%%%%%%%%\nd'une structure de"),
    ("et définit \\(f'\\),\n%%%%%%%%%%  scan idx 348  |  folio 335  %%%%%%%%%%\névidemment unique.",
     "et définit\n%%%%%%%%%%  scan idx 348  |  folio 335  %%%%%%%%%%\n\\(f'\\), évidemment unique."),
    ("sur \\(A\\)~; on\n%%%%%%%%%%  scan idx 349  |  folio 336  %%%%%%%%%%\ndéfinit un",
     "sur \\(A\\)~;\n%%%%%%%%%%  scan idx 349  |  folio 336  %%%%%%%%%%\non définit un"),
]
notes = " ".join(x.get("note", "") for x in items)
for ed in ("diplomatic", "current"):
    t = (SGA6 / ed / "main.tex").read_text(encoding="utf-8")
    for old, new in lit:
        c = t.count(old)
        in_note = old.replace("\n", "\\n") in notes and new.replace("\n", "\\n") in notes
        print(ed, "literal", repr(old[:30]), "count", c, "quoted in a note:", in_note)
        if c != 1 or not in_note:
            ok = False
print("ALL OK" if ok else "PROBLEMS")
