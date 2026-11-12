"""Apply the agreed fixes of the SGA 4 API pass (AGREED_FIXES.json, from merge_pass.py) to the working copy, the way
process_sga.py does for SGA 5-7. The working copy is built from the pristine texts (pristine/, made by
snapshot_pristine.py: the corpus copies the models saw), so the script can run again when more answers have come in:
each run applies the whole current AGREED_FIXES.json to the pristine texts and replaces this pass's logs.

- diplomatic layer (sga4/diplomatic): each fix replaces its old text at the position merge_pass.py found for it in
  the pristine text (exactly once in the page's lines); the position is checked again here. Fixes are applied per file
  from the end backwards. The same fix found on two pages (lines shared at a page break) is applied once. Logged in
  FIXLOG_4.jsonl.
- corrected layer (sga4/current: Codex's corrected_history/through_0370 with the 05bis overlay of 28 Sep): each
  diplomatic fix is replayed where its old text occurs exactly once between the \\pageoriginale markers around the same
  page (the markers are counted in both layers; whitespace runs may differ); logged in FIXLOG_4_CURRENT.jsonl,
  otherwise listed in REPLAY_MANUAL_4.json, with status "already there" when the old text is gone and the new text
  stands there (Codex's corrections reached it first: nothing to do), else "by hand".
- misprints of the print that both models report: MISPRINTS_4.json (nothing is applied for them).

Safety: a working-copy file is written only if it still equals its pristine text or the text this script wrote last
time (APPLY_STATE.json); the logs are replaced only if every record in them comes from this pass. Hand edits made
after an application (in-app check, REPLAY_MANUAL by hand) therefore stop a rebuild instead of being lost.

usage: python -I apply_pass.py [--dry]
"""
import datetime
import hashlib
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
W = HERE.parent
WORK = {"diplomatic": W / "sga4" / "diplomatic", "current": W / "sga4" / "current"}
PRISTINE = {"diplomatic": HERE / "pristine" / "diplomatic", "current": HERE / "pristine" / "current"}
MARK = re.compile(r"\\pageoriginaled?(?![A-Za-z])")
TAG = "sga4_api_pass_20261111"
dry = "--dry" in sys.argv


def loose(s):
    """A pattern for s in which any whitespace run matches any other (line breaks differ between the layers)."""
    return r"\s+".join(re.escape(x) for x in s.split())


def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest().upper()


def read_jsonl(p):
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()] if p.exists() else []


# what may be replaced
state_p = HERE / "APPLY_STATE.json"
state = json.loads(state_p.read_text(encoding="utf-8")) if state_p.exists() else {"files": {}}
for name in ("FIXLOG_4.jsonl", "FIXLOG_4_CURRENT.jsonl"):
    foreign = [r for r in read_jsonl(W / name) if not str(r.get("source", "")).startswith(TAG)]
    if foreign:
        raise SystemExit(f"{name} holds {len(foreign)} records not from this pass: not replaced")
if (W / "REPLAY_MANUAL_4_DONE.json").exists():
    raise SystemExit("REPLAY_MANUAL_4_DONE.json exists: hand edits were made on the corrected layer; not rebuilt")

fixes = json.loads((HERE / "AGREED_FIXES.json").read_text(encoding="utf-8"))
# The edition writes the empty set as the character ∅: \emptyset is undefined in its build (macros.tex lets it to
# \varnothing before unicode-math defines that), so an agreed fix that writes \emptyset or \varnothing is applied with ∅.
EMPTY = re.compile(r"\\(?:emptyset|varnothing)(?![A-Za-z])")
for f in fixes:
    if EMPTY.search(f["new"]):
        f["new"] = EMPTY.sub("∅", f["new"])
        f["note"] = "\\emptyset written as ∅, the edition's form (\\emptyset is undefined in its build)"
by_file, seen, dup = {}, set(), 0
for f in fixes:
    k = (f["file"], f["start"], f["end"], f["new"])
    if k in seen:
        dup += 1
        continue
    seen.add(k)
    by_file.setdefault(f["file"], []).append(f)

log, log_cur, manual, writes = [], [], [], []
line_shift = {}  # per file: (pristine line where a fix ends, lines it adds) for the app-check entries' line numbers
for fn, fl in sorted(by_file.items()):
    text = (PRISTINE["diplomatic"] / fn / f"{fn}.tex").read_text(encoding="utf-8")
    fl.sort(key=lambda f: f["start"])
    keep, last_end = [], -1
    for f in fl:
        if text[f["start"]:f["end"]] != f["old"]:
            manual.append(dict(f, why="the old text is not at its position in the pristine text"))
            continue
        if f["start"] < last_end:
            manual.append(dict(f, why="overlaps another agreed fix"))
            continue
        keep.append(f)
        last_end = f["end"]
    marks_dip = [m.start() for m in MARK.finditer(text)]
    new_text = text
    for f in reversed(keep):
        new_text = new_text[:f["start"]] + f["new"] + new_text[f["end"]:]
    line_shift[fn] = [(text.count("\n", 0, f["end"]) + 1, f["new"].count("\n") - f["old"].count("\n")) for f in keep]
    for f in keep:
        log.append({"vol": "4", "tome": f["tome"], "file": f"{fn}/{fn}.tex", "page": f["page"], "old": f["old"],
                    "new": f["new"], "kind": "/".join(f["kinds"]),
                    "source": f"{TAG} {f['batch']} (Claude Opus 5.5 high and GPT-6.1 Sol max agree)",
                    **({"note": f["note"]} if f.get("note") else {})})
    writes.append(("diplomatic", fn, new_text))
    # replay on the corrected layer
    ctext = (PRISTINE["current"] / fn / f"{fn}.tex").read_text(encoding="utf-8")
    marks_cur = [m.start() for m in MARK.finditer(ctext)]
    same_count = len(marks_cur) == len(marks_dip)
    edits = []
    for f in keep:
        if not same_count:
            manual.append(dict(f, layer="current", status="by hand",
                               why=f"marker count differs ({len(marks_dip)} diplomatic, {len(marks_cur)} current)"))
            continue
        k = sum(1 for m in marks_dip if m <= f["start"])  # markers up to the fix: the fix lies after marker k-1
        lo = marks_cur[k - 2] if k >= 2 else 0
        hi = marks_cur[k + 1] if k + 1 < len(marks_cur) else len(ctext)
        hits = [(m.start(), m.end()) for m in re.finditer(re.escape(f["old"]), ctext[lo:hi])] or \
            [(m.start(), m.end()) for m in re.finditer(loose(f["old"]), ctext[lo:hi])]
        if len(hits) != 1:
            if not hits and len(f["new"].strip()) >= 6 and re.search(loose(f["new"]), ctext[lo:hi]):
                manual.append(dict(f, layer="current", status="already there",
                                   why="the corrected layer already reads the fixed text here (old not found, new "
                                       "found): nothing to do"))
                continue
            manual.append(dict(f, layer="current", status="by hand",
                               why=f"old occurs {len(hits)} times around the page in the corrected layer"))
            continue
        a, b = lo + hits[0][0], lo + hits[0][1]
        edits.append((a, b, f))
    edits.sort()
    ok_edits, last = [], -1
    for a, b, f in edits:
        if a < last:
            manual.append(dict(f, layer="current", status="by hand", why="overlaps another replayed fix"))
            continue
        ok_edits.append((a, b, f))
        last = b
    for a, b, f in reversed(ok_edits):
        ctext = ctext[:a] + f["new"] + ctext[b:]
    for a, b, f in ok_edits:
        log_cur.append({"vol": "4", "tome": f["tome"], "file": f"{fn}/{fn}.tex", "page": f["page"], "old": f["old"],
                        "new": f["new"], "kind": "/".join(f["kinds"]),
                        "source": f"{TAG} {f['batch']} (replayed from the diplomatic fix)"})
    writes.append(("current", fn, ctext))

# files written last time that get no fix now go back to their pristine text
written = {f"{layer}/{fn}/{fn}.tex" for layer, fn, _ in writes}
for rel in state["files"]:
    if rel not in written:
        layer, fn = rel.split("/")[0], rel.split("/")[1]
        writes.append((layer, fn, (PRISTINE[layer] / fn / f"{fn}.tex").read_text(encoding="utf-8")))
# every working-copy file to write must still be pristine or as written last time
for layer, fn, _ in writes:
    rel = f"{layer}/{fn}/{fn}.tex"
    now = (WORK[layer] / fn / f"{fn}.tex").read_text(encoding="utf-8")
    pristine = (PRISTINE[layer] / fn / f"{fn}.tex").read_text(encoding="utf-8")
    if now != pristine and sha(now) != state["files"].get(rel):
        raise SystemExit(f"{rel} was changed since the last application (not pristine, not as written by this "
                         f"script): nothing written")

mis = json.loads((HERE / "AGREED_MISPRINTS.json").read_text(encoding="utf-8"))
if not dry:
    new_state = {"applied": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                 "agreed_fixes": len(fixes), "files": {}}
    for layer, fn, t in writes:
        (WORK[layer] / fn / f"{fn}.tex").write_text(t, encoding="utf-8", newline="")
        new_state["files"][f"{layer}/{fn}/{fn}.tex"] = sha(t)
    with open(W / "FIXLOG_4.jsonl", "w", encoding="utf-8") as fh:
        for r in log:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    with open(W / "FIXLOG_4_CURRENT.jsonl", "w", encoding="utf-8") as fh:
        for r in log_cur:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    (W / "REPLAY_MANUAL_4.json").write_text(json.dumps([m for m in manual if m.get("layer") == "current"],
                                                       ensure_ascii=False, indent=1), encoding="utf-8")
    (HERE / "APPLY_MANUAL.json").write_text(json.dumps([m for m in manual if m.get("layer") != "current"],
                                                       ensure_ascii=False, indent=1), encoding="utf-8")
    mp = W / "MISPRINTS_4.json"
    prev = [x for x in (json.loads(mp.read_text(encoding="utf-8")) if mp.exists() else [])
            if not str(x.get("source", "")).startswith(TAG)]
    mp.write_text(json.dumps(prev + mis, ensure_ascii=False, indent=1), encoding="utf-8")
    state_p.write_text(json.dumps(new_state, ensure_ascii=False, indent=1), encoding="utf-8")
    # the in-app check starts from the fixed working copy: give each page its lines there too
    app_p = HERE / "PAGES_FOR_APP_CHECK.json"
    app = json.loads(app_p.read_text(encoding="utf-8"))
    for e in app:
        sh = line_shift.get(e["file"], [])
        e["working_copy_lines"] = [ln + sum(d for end, d in sh if end < ln) for ln in e["tex_lines"]]
    app_p.write_text(json.dumps(app, ensure_ascii=False, indent=1), encoding="utf-8")
if dry:
    for m in manual:
        if m.get("status") != "already there":
            print("  by hand:", m.get("layer", "diplomatic"), m["file"], m["page"], m["why"], "|", repr(m["old"])[:70])
print(f"agreed fixes {len(fixes)} (duplicates across pages {dup}); applied to the diplomatic layer {len(log)}; "
      f"not applied {sum(1 for m in manual if m.get('layer') != 'current')}; replayed on the corrected layer "
      f"{len(log_cur)}; already there in the corrected layer "
      f"{sum(1 for m in manual if m.get('status') == 'already there')}; corrected layer by hand "
      f"{sum(1 for m in manual if m.get('layer') == 'current' and m.get('status') != 'already there')}; "
      f"misprints recorded {len(mis)}" + (" (dry run)" if dry else ""))
