"""Merge the two models' findings of the SGA 4 API pass, page by page, into what is applied and what goes to the
in-app check.

For each printed page the findings of Claude Opus 5.5 (opus) and GPT-6.1 Sol (sol) are placed in the page's TeX of
the diplomatic layer as the models saw it (pristine/diplomatic, lines of PAGES.json): a fix by its "old" (exactly once in the page; whitespace
runs may differ), a misprint by its quoted TeX. Fixes are grouped by the places they change (overlapping regions;
then one-model groups within 80 characters of a group of the other model are tried together); a group whose two
sets of fixes give the same TeX (whitespace normalised) is an agreed fix. Categories:

  agreed_fix          both models, same effect, neither marks it low confidence -> applied (AGREED_FIXES.json)
  agreed_fix_held     agreed, but low confidence, a deletion at a page boundary (overlap lines), an insertion whose
                      text the neighbouring pages already hold, an insertion of more than 300 characters, an edit
                      of commented-out lines, or a change to the editors' apparatus (\\sisi, notes, labels,
                      references, citations) -> in-app check
  conflict            both models changed the place, differently (or one fix against the other's misprint)
                      -> in-app check
  one_model_fix       a fix from one model only -> in-app check
  fix_unplaced        a fix whose old cannot be found once in the page -> in-app check
  doubt               a finding about the TeX (not a misprint, not the cut) without a usable fix -> in-app check
  marker              a report that the automatic page cut is wrong (about the cut, not the TeX)
                      -> CUT_REPORTS.json
  agreed_misprint     both report the same misprint of the print (fix null) -> MISPRINTS_4.json, nothing applied
  one_model_misprint  a misprint from one model only -> OPUS_ONLY_MISPRINTS.json / SOL_ONLY_MISPRINTS.json, never
                      applied; each sorted (misprint_class, a heuristic) as language, mathematics or recorded by the
                      editors (\\sisi), and the mathematics ones listed apart in <MODEL>_ONLY_MISPRINTS_MATHEMATICS.json
                      (Sol's holds the doubtful "misprints" that correct the author's mathematics)

Writes MERGED.json (everything, per page), AGREED_FIXES.json, PAGES_FOR_APP_CHECK.json, OPUS_ONLY_MISPRINTS.json,
SOL_ONLY_MISPRINTS.json, AGREED_MISPRINTS.json, CUT_REPORTS.json, COORDINATOR_NOTES.md and prints the counts. Applies nothing (apply_pass.py does).

usage: python -I merge_pass.py
"""
import difflib
import json
import pathlib
import re
import sys
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
W = HERE.parent
DIP = HERE / "pristine" / "diplomatic"  # the TeX the models saw (snapshot_pristine.py), never the fixed copy
ANS = HERE / "answers"
MODELS = ("opus", "sol")
CUT = []  # the models' reports on the page cut (kind "marker")
NAMES = {"opus": "Claude Opus 5.5 (effort high, Message Batches API)",
         "sol": "GPT-6.1 Sol (reasoning effort max, Flex tier)"}


def ws(s):
    return re.sub(r"\s+", " ", s).strip()


def same_text(a, b):
    """Equal up to spacing: whitespace runs, ~ and the thin-space commands (spacing is not checked)."""
    def n(s):
        return ws(re.sub(r"~|\\[,;:! ]", " ", s))
    return n(a) == n(b)


def load_text(fn, _c={}):
    if fn not in _c:
        _c[fn] = (DIP / fn / f"{fn}.tex").read_text(encoding="utf-8")
    return _c[fn]


def line_offsets(text):
    offs = [0]
    for m in re.finditer("\n", text):
        offs.append(m.end())
    return offs


def span_chars(fn, a, z, _c={}):
    if fn not in _c:
        _c[fn] = line_offsets(load_text(fn))
    offs = _c[fn]
    text = load_text(fn)
    s = offs[a - 1]
    e = offs[z] - 1 if z < len(offs) else len(text)
    return s, e


def find_once(text, s, e, old):
    """Positions of old within text[s:e]: exact first, then with any whitespace run matching any other."""
    hits = []
    k = text.find(old, s, e)
    while k >= 0 and k + len(old) <= e:
        hits.append((k, k + len(old)))
        k = text.find(old, k + 1, e)
    if hits:
        return hits
    parts = [re.escape(x) for x in old.split()]
    if not parts:
        return []
    rx = re.compile(r"\s+".join(parts))
    return [(m.start(), m.end()) for m in rx.finditer(text, s, e)]


def overlap_zones(p):
    """Character ranges of the page's overlap lines (shared lines, display/heading blocks given to both pages)."""
    out = []
    for o in p["overlaps"]:
        x, y = o["lines"]
        x, y = max(x, p["lines"][0]), min(y, p["lines"][1])
        if x <= y:
            out.append(span_chars(p["file"], x, y))
    return out


def norm_fix(f):
    fx = f.get("fix")
    if not isinstance(fx, dict):
        return None
    old = (fx.get("old") or "").replace("\r\n", "\n")
    new = (fx.get("new") or "").replace("\r\n", "\n")
    if not old or old == new:
        return None
    return old, new


def is_low(f):
    return str(f.get("confidence", "")).lower() == "low"


def apply_set(text, s, e, edits):
    """The span text with a set of (start, end, new) edits applied (non-overlapping; else None)."""
    edits = sorted(edits)
    for (a1, b1, _), (a2, b2, _) in zip(edits, edits[1:]):
        if a2 < b1:
            return None
    out, cur = [], s
    for a, b, new in edits:
        out.append(text[cur:a])
        out.append(new)
        cur = b
    out.append(text[cur:e])
    return "".join(out)


APPARATUS = {"sisi", "nde", "ndt", "nda", "label", "ref", "eqref", "eqhyperref", "hyperref", "hyperrefext",
             "eqhyperrefext", "neweqhyperrefext", "refnoexpose", "refvb", "cite", "pageoriginale", "setcounter",
             "footnote", "index"}


def apparatus(s):
    """The editors' apparatus macros in s, counted (corrections, notes, labels, references, citations, markers)."""
    return Counter(m for m in re.findall(r"\\([A-Za-z]+)", s) if m in APPARATUS)


def cites(s):
    return re.findall(r"\\cite(\[[^\]]*\])?\{([^}]*)\}", s)


REFS = re.compile(r"\\(hyperref|hyperrefext|eqhyperref|eqhyperrefext|neweqhyperrefext|refnoexpose|refvb|eqref|ref|"
                  r"label)(?![A-Za-z])((?:\[[^\]]*\])*)(\{[^}]*\})?")
BRACED = {"ref", "eqref", "label", "refnoexpose", "refvb"}


def targets(s):
    """The targets of the cross-references and labels in s: the macro, its bracketed arguments, and its braced
    argument where that is the label (a fix that keeps the reference but changes where it points retargets it)."""
    return [(m.group(1), m.group(2)) + ((m.group(3),) if m.group(1) in BRACED else ()) for m in REFS.finditer(s)]


def misprint_key(f):
    return ws(" ".join(str(f.get(k) or "") for k in ("tex", "scan", "corrected")))


def same_misprint(f, g, text, s, e):
    """Two misprint reports name the same place: their quoted TeX overlaps on the page, or their readings agree."""
    pf, pg = [], []
    for x, acc in ((f, pf), (g, pg)):
        q = str(x.get("tex") or "").strip()
        if len(q) >= 3:
            acc += find_once(text, s, e, q)
    for a1, b1 in pf:
        for a2, b2 in pg:
            if a1 < b2 + 5 and a2 < b1 + 5:
                return True
    return difflib.SequenceMatcher(None, misprint_key(f), misprint_key(g)).ratio() >= 0.7


def merge():
    pages = json.loads((HERE / "PAGES.json").read_text(encoding="utf-8"))
    batches = json.loads((HERE / "BATCHES.json").read_text(encoding="utf-8"))
    pidx = {(p["tome"], p["folio"]): p for p in pages}
    nbr = {}
    for p in pages:
        nbr.setdefault((p["tome"], p["file"]), []).append(p)
    merged, agreed, app, agreed_mis, only_mis = [], [], [], [], {"opus": [], "sol": []}
    missing = defaultdict(list)
    for b in batches:
        ans = {}
        for m in MODELS:
            pth = ANS / m / f"{b['key']}.json"
            if pth.exists():
                ans[m] = json.loads(pth.read_text(encoding="utf-8"))
            else:
                missing[m].append(b["key"])
        if not ans:
            continue
        # a batch answered by one model only is merged from that model's findings alone (all of them one-model
        # items); outputs() sends each of its pages whole to the in-app check
        for folio in b["folios"]:
            p = pidx[(b["tome"], folio)]
            fn = p["file"]
            text = load_text(fn)
            s, e = span_chars(fn, *p["lines"])
            zones = overlap_zones(p)
            a0, z0 = p["lines"]
            edges = [span_chars(fn, a0, min(z0, a0 + 2)), span_chars(fn, max(a0, z0 - 2), z0)]
            fixes, mis, markers, unplaced = [], [], [], []
            for m in MODELS:
                for f in ans.get(m, []):
                    try:
                        if int(f.get("page", -1)) != folio:
                            continue
                    except (TypeError, ValueError):
                        continue
                    kind = str(f.get("kind", ""))
                    nf = norm_fix(f)
                    if kind == "marker":
                        markers.append({"model": m, "finding": f})
                        continue
                    if nf is None:
                        if kind == "misprint_in_print":
                            mis.append({"model": m, "finding": f})
                        else:  # a finding about the TeX without a usable fix: a doubt, for the in-app check
                            unplaced.append({"model": m, "finding": f, "doubt": True,
                                             "why": "a model flags this place without giving a fix"})
                        continue
                    hits = find_once(text, s, e, nf[0])
                    if len(hits) != 1:
                        unplaced.append({"model": m, "finding": f, "why": f"old found {len(hits)} times in the page"})
                        continue
                    a, z = hits[0]
                    fixes.append({"model": m, "finding": f, "start": a, "end": z, "old": text[a:z], "new": nf[1]})
            # groups of fixes by overlapping regions
            n = len(fixes)
            parent = list(range(n))

            def root(i):
                while parent[i] != i:
                    parent[i] = parent[parent[i]]
                    i = parent[i]
                return i

            def join(i, j):
                parent[root(i)] = root(j)

            for i in range(n):
                for j in range(i + 1, n):
                    fi, fj = fixes[i], fixes[j]
                    if fi["start"] < fj["end"] and fj["start"] < fi["end"] or (
                            fi["start"] == fi["end"] == fj["start"] == fj["end"]):
                        join(i, j)

            def groups():
                g = defaultdict(list)
                for i in range(n):
                    g[root(i)].append(i)
                return list(g.values())

            def same_effect(ids):
                by = {m: [(fixes[i]["start"], fixes[i]["end"], fixes[i]["new"]) for i in ids
                          if fixes[i]["model"] == m] for m in MODELS}
                if not by["opus"] or not by["sol"]:
                    return None
                ro, rs = apply_set(text, s, e, by["opus"]), apply_set(text, s, e, by["sol"])
                if ro is None or rs is None:
                    return False
                return same_text(ro, rs)

            # one-model groups near a group of the other model: try them together
            for _ in range(2):
                gs = groups()
                for g1 in gs:
                    ms1 = {fixes[i]["model"] for i in g1}
                    if len(ms1) != 1:
                        continue
                    for g2 in gs:
                        if g2 is g1 or root(g2[0]) == root(g1[0]):
                            continue
                        ms2 = {fixes[i]["model"] for i in g2}
                        if ms1 & ms2 and len(ms2) == 1:
                            continue
                        lo1, hi1 = min(fixes[i]["start"] for i in g1), max(fixes[i]["end"] for i in g1)
                        lo2, hi2 = min(fixes[i]["start"] for i in g2), max(fixes[i]["end"] for i in g2)
                        if lo1 - 80 <= hi2 and lo2 - 80 <= hi1 and same_effect(g1 + g2):
                            join(g1[0], g2[0])
            items = []
            for g in groups():
                ms = {fixes[i]["model"] for i in g}
                lo, hi = min(fixes[i]["start"] for i in g), max(fixes[i]["end"] for i in g)
                rec = {"region": [lo, hi], "fixes": [{k: fixes[i][k] for k in ("model", "old", "new", "start", "end")}
                                                     | {"kind": fixes[i]["finding"].get("kind"),
                                                        "confidence": fixes[i]["finding"].get("confidence"),
                                                        "where": fixes[i]["finding"].get("where"),
                                                        "scan": fixes[i]["finding"].get("scan"),
                                                        "tex": fixes[i]["finding"].get("tex"),
                                                        "note": fixes[i]["finding"].get("note")} for i in g]}
                if len(ms) == 2:
                    eff = same_effect(g)
                    if eff:
                        why = []
                        if any(is_low(fixes[i]["finding"]) for i in g):
                            why.append("a model marks it low confidence")
                        if any(str(fixes[i]["finding"].get("kind")) == "misprint_in_print" for i in g):
                            why.append("a model calls it a misprint of the print and still gives a fix (for SGA 4 a "
                                       "misprint gets no fix, whether the TeX keeps it or corrects it)")
                        opus_edits = [(fixes[i]["start"], fixes[i]["end"], fixes[i]["new"]) for i in g
                                      if fixes[i]["model"] == "opus"]
                        removed = sum(z - a for a, z, _ in opus_edits) - sum(len(x) for _, _, x in opus_edits)
                        in_zone = any(a < ze and zs < z for a, z, _ in opus_edits for zs, ze in zones)
                        if in_zone and removed >= 10:
                            why.append("a deletion in lines the neighbouring page may hold")
                        elif removed >= 10 and any(a < ze and zs < z for a, z, _ in opus_edits for zs, ze in edges):
                            why.append("a deletion in the first or last three lines of the page (the page cut may "
                                       "be off)")
                        added = sum(len(x) for _, _, x in opus_edits) - sum(z - a for a, z, _ in opus_edits)
                        if added > 300:
                            why.append("an insertion of more than 300 characters")
                        if any(re.search(r"(^|\n)\s*%", text[a:z]) or re.search(r"(^|\n)\s*%", x)
                               for a, z, x in opus_edits):
                            why.append("it changes lines the edition has commented out (uncommenting may affect "
                                       "the build; decide with the edition's intent)")
                        elif added > 40 and re.search(r"(^|\n)[ \t]*%[^\n]*\n[ \t]*%[^\n]*\n[ \t]*%", text[s:e]):
                            why.append("an insertion on a page where the edition has commented out printed lines "
                                       "(the insertion may duplicate them)")
                        olds = " ".join(text[a:z] for a, z, _ in opus_edits)
                        news = " ".join(x for _, _, x in opus_edits)
                        ao, an = apparatus(olds), apparatus(news)
                        what = ["\\" + m for m in sorted(set(ao) | set(an)) if ao[m] != an[m]]
                        if cites(olds) != cites(news) and "\\cite" not in what:
                            what.append("the target of a \\cite")
                        if targets(olds) != targets(news):
                            what.append("the target of a cross-reference")
                        if what:
                            why.append("it changes the editors' apparatus (" + ", ".join(what) +
                                       "): a \\sisi correction, note, label, cross-reference or citation is the "
                                       "editors' record and is not removed or retargeted on the models' word")
                        if added > 40:
                            ins = ws(" ".join(x for _, _, x in opus_edits))
                            for q in nbr[(p["tome"], fn)]:
                                if abs(q["folio"] - folio) == 1:
                                    qs, qe = span_chars(fn, *q["lines"])
                                    if ins[:60] and ins[:60] in ws(text[qs:qe]):
                                        why.append(f"the inserted text stands on p. {q['folio']} in the TeX")
                        rec["category"] = "agreed_fix_held" if why else "agreed_fix"
                        if why:
                            rec["why"] = why
                        else:
                            rec["apply"] = [{"start": a, "end": z, "old": text[a:z], "new": x} for a, z, x in
                                            sorted(opus_edits)]
                    else:
                        rec["category"] = "conflict"
                else:
                    rec["category"] = "one_model_fix"
                items.append(rec)
            # misprints: agreed between the models, against a fix of the other model, or one model only
            used = set()
            for i, x in enumerate(mis):
                if i in used:
                    continue
                partner = None
                for j in range(i + 1, len(mis)):
                    if j not in used and mis[j]["model"] != x["model"] and \
                            same_misprint(x["finding"], mis[j]["finding"], text, s, e):
                        partner = j
                        break
                if partner is not None:
                    used |= {i, partner}
                    items.append({"category": "agreed_misprint", "misprints": [x, mis[partner]]})
                    continue
                used.add(i)
                # a misprint of one model where the other model gave a fix: a conflict over the place
                q = str(x["finding"].get("tex") or "").strip()
                pos = find_once(text, s, e, q) if len(q) >= 3 else []
                hit = None
                for it in items:
                    if it.get("fixes") and pos and any(a < it["region"][1] + 5 and it["region"][0] < b + 5
                                                       for a, b in pos) and \
                            {fx["model"] for fx in it["fixes"]} == {[m for m in MODELS if m != x["model"]][0]}:
                        hit = it
                        break
                if hit is not None:
                    hit.setdefault("misprints", []).append(x)
                    if hit["category"] in ("one_model_fix",):
                        hit["category"] = "conflict"
                        hit["why"] = ["one model fixes the TeX, the other calls it a misprint of the print"]
                    continue
                items.append({"category": "one_model_misprint", "misprints": [x]})
            for u in unplaced:
                items.append({"category": "doubt" if u.get("doubt") else "fix_unplaced", "finding": u["finding"],
                              "model": u["model"], "why": u["why"]})
            for mk in markers:
                items.append({"category": "marker", "finding": mk["finding"], "model": mk["model"]})
            merged.append({"tome": p["tome"], "page": folio, "expose": p["expose"], "file": fn, "batch": b["key"],
                           "pdf_page": p["pdf_page"], "answered_by": sorted(ans), "items": items})
    return merged, missing


def reading(f):
    return {k: f.get(k) for k in ("kind", "confidence", "where", "scan", "tex", "fix", "corrected", "note")
            if f.get(k) is not None}


MATH_CH = re.compile(r"[0-9\\^_{}=+<>|/\[\]]")


def in_math(s, i):
    return len(re.findall(r"(?<!\\)\$", s[:i])) % 2 == 1


def misprint_class(f):
    """What a misprint report is about (a heuristic, for sorting the lists): "recorded by the editors" when the TeX
    quoted already has a \\sisi there; "mathematics" when the printed and the proposed readings differ in a formula, a
    symbol, a number or a reference (the doubtful kind: a correction of the author's mathematics or notation);
    otherwise "language" (spelling, grammar, accents, punctuation of the print)."""
    if "\\sisi" in str(f.get("tex") or ""):
        return "recorded by the editors"
    a, b = str(f.get("scan") or f.get("tex") or ""), str(f.get("corrected") or "")
    if not b:
        return "mathematics" if MATH_CH.search(a) or "$" in a else "language"
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op == "equal":
            continue
        near = a[max(0, i1 - 3):i2 + 3] + b[max(0, j1 - 3):j2 + 3]  # the change and three characters around it
        if MATH_CH.search(near) or in_math(a, i1) or in_math(b, j1) or "$" in near:
            return "mathematics"
        if re.fullmatch(r"[A-Za-z]", (a[i1:i2] or b[j1:j2]).strip()) and not re.search(r"[a-zà-ÿ]", a[max(0, i1 - 1):i1] + a[i2:i2 + 1]):
            return "mathematics"  # a lone letter changed: a variable
    return "language"


def outputs(merged, missing):
    pages = json.loads((HERE / "PAGES.json").read_text(encoding="utf-8"))
    pidx = {(p["tome"], p["folio"]): p for p in pages}
    bfol = {b["key"]: b["folios"] for b in json.loads((HERE / "BATCHES.json").read_text(encoding="utf-8"))}
    agreed, app, agreed_mis = [], [], []
    only = {"opus": [], "sol": []}
    cats = Counter()
    for pg in merged:
        p = pidx[(pg["tome"], pg["page"])]
        reasons, entries = [], []
        absent = [m for m in MODELS if m not in pg.get("answered_by", MODELS)]
        if absent:  # one model only checked this page: the whole page goes to the in-app check
            reasons.append("one_model_only")
            entries.append({"category": "one_model_only",
                            "why": "only " + NAMES[pg["answered_by"][0]] + " checked this page: " + NAMES[absent[0]] +
                                   " gave no answer for batch " + pg["batch"] + " (the Flex tier turned the request "
                                   "away or did not run it); check the whole page against the scan, with the findings "
                                   "below as leads",
                            "readings": {m: ("listed below" if m in pg["answered_by"] else "no answer for this batch")
                                         for m in MODELS}})
        for it in pg["items"]:
            c = it["category"]
            cats[c] += 1
            if c == "agreed_fix":
                for ap in it["apply"]:
                    agreed.append({"tome": pg["tome"], "page": pg["page"], "file": pg["file"], "batch": pg["batch"],
                                   **ap, "kinds": sorted({str(fx.get("kind")) for fx in it["fixes"]}),
                                   "where": next((fx.get("where") for fx in it["fixes"] if fx.get("where")), None),
                                   "readings": {m: [reading_fx(fx) for fx in it["fixes"] if fx["model"] == m]
                                                for m in MODELS}})
            elif c == "agreed_misprint":
                f0 = it["misprints"][0]["finding"]
                agreed_mis.append({"vol": "4", "tome": pg["tome"], "page": pg["page"], "expose": pg["expose"],
                                   "where": f0.get("where"), "print": f0.get("scan"), "correct": f0.get("corrected"),
                                   "tex_did": f0.get("tex"), "note": f0.get("note"),
                                   "readings": {x["model"]: reading(x["finding"]) for x in it["misprints"]},
                                   "source": f"sga4_api_pass_20261111 {pg['batch']} (both models)"})
            elif c == "one_model_misprint":
                x = it["misprints"][0]
                only[x["model"]].append({"tome": pg["tome"], "page": pg["page"], "expose": pg["expose"],
                                         "batch": pg["batch"], "class": misprint_class(x["finding"]),
                                         **({"other_model": "no answer for this batch"} if absent else {}),
                                         **reading(x["finding"])})
                if absent:  # the page goes to the in-app check whole: its misprint reports go with it
                    reasons.append(c)
                    entries.append({"category": c, "why": "a misprint of the print reported by the one model that "
                                    "checked this page", "readings": {m: ([reading(x["finding"])] if m == x["model"]
                                                                          else "no answer for this batch")
                                                                      for m in MODELS}})
            elif c == "marker":  # about the automatic page cut: listed apart (CUT_REPORTS.json). Inside a batch the
                # model had both pages' TeX and scans; at a batch's first or last page the neighbour may lie in another
                # batch, whose checker did not have the lines: those go to the in-app check
                CUT.append({"tome": pg["tome"], "page": pg["page"], "expose": pg["expose"], "batch": pg["batch"],
                            "model": it["model"], **reading(it["finding"])})
                if pg["page"] not in (bfol[pg["batch"]][0], bfol[pg["batch"]][-1]):
                    continue
                reasons.append("cut")
                e = {"category": "cut", "why": "a model reports that the automatic cut gives lines of this page to "
                     "its neighbour, or the neighbour's lines to this page: check the lines it names against the "
                     "scan of the page that prints them (that page's checker did not have their TeX)",
                     "readings": {m: ([reading(it["finding"])] if m == it["model"] else
                                      "no answer for this batch" if m in absent else "nothing reported here")
                                  for m in MODELS}}
                entries.append(e)
            else:
                why = {"agreed_fix_held": "both models give the same fix, held: " + "; ".join(it.get("why", [])),
                       "conflict": "the two models differ at this place" + (
                           ": " + "; ".join(it["why"]) if it.get("why") else ""),
                       "one_model_fix": "a fix from one model only",
                       "fix_unplaced": "a fix whose old text is not found once on the page",
                       "doubt": "a model flags this place without giving a fix",
                       "marker": "a model reports that the page's TeX is cut at the wrong place"}[c]
                reasons.append(c)
                e = {"category": c, "why": why}
                if it.get("fixes"):
                    e["readings"] = {m: [reading_fx(fx) for fx in it["fixes"] if fx["model"] == m] for m in MODELS}
                    e["tex_now"] = None
                if it.get("misprints"):
                    for x in it["misprints"]:
                        e.setdefault("readings", {}).setdefault(x["model"], []).append(reading(x["finding"]))
                if it.get("finding"):
                    e["readings"] = {it["model"]: [reading(it["finding"])]}
                for m in MODELS:
                    e.setdefault("readings", {}).setdefault(m, [])
                    if not e["readings"][m]:
                        e["readings"][m] = "no answer for this batch" if m in absent else "nothing reported here"
                if absent:
                    e["why"] += " (the other model gave no answer for this batch)"
                e.pop("tex_now", None)
                entries.append(e)
        if entries:
            app.append({"tome": pg["tome"], "page": pg["page"], "expose": pg["expose"], "file": pg["file"],
                        "tex_lines": p["lines"], "scan": p["scan"], "scan_path": p.get("scan_path"),
                        "pdf_page": p["pdf_page"],
                        "strips": f"sga4_api_pass_20261111/strips/t{pg['tome']}/p{pg['page']:03d}_s1..4.png",
                        **({"witness": p["witness"], "witness_path": p.get("witness_path"),
                            "witness_pdf_page": p["witness_pdf_page"]}
                           if p.get("witness_pdf_page") else {}),
                        "batch": pg["batch"], "why": sorted(set(reasons)), "items": entries})
    return agreed, app, agreed_mis, only, cats


def reading_fx(fx):
    return {k: fx.get(k) for k in ("kind", "confidence", "where", "scan", "tex", "note") if fx.get(k) is not None} | {
        "fix": {"old": fx["old"], "new": fx["new"]}}


def coordinator_notes():
    """What the models told the coordinator beyond the counts (conventions, edits to apply together, cut problems)."""
    batches = json.loads((HERE / "BATCHES.json").read_text(encoding="utf-8"))
    out = ["# What the two models told the coordinator, beyond the page counts", "",
           "One line per batch and model; the count line of each message is left out. Not applied; read for "
           "conventions of the edition and for edits that belong together.", ""]
    for b in batches:
        for m in MODELS:
            p = ANS / m / f"{b['key']}_coordinator.md"
            if not p.exists():
                continue
            t = p.read_text(encoding="utf-8").strip()
            lines = [x.strip() for x in t.splitlines() if x.strip()]
            if lines:
                counts = list(re.finditer(r"\d+\s*/\s*\d+", lines[0]))
                if len(counts) >= 2 or (len(counts) == 1 and len(lines[0]) < 40):
                    first = lines[0][counts[-1].end():].strip(" .;,)")
                    lines = ([first] if first else []) + lines[1:]
            lines = [x for x in lines if not re.fullmatch(r"\(?\s*normal\s*/\s*misprints?\s*\)?\.?", x, flags=re.I)]
            rest = " ".join(lines).strip()
            if not rest or re.fullmatch(r"(no marker problems.*|none\.?|nothing else\.?)", rest, flags=re.I):
                continue
            out.append(f"- **{b['key']}**, {m}: {rest}")
    (HERE / "COORDINATOR_NOTES.md").write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    coordinator_notes()
    merged, missing = merge()
    agreed, app, agreed_mis, only, cats = outputs(merged, missing)
    (HERE / "MERGED.json").write_text(json.dumps(merged, ensure_ascii=False, indent=1), encoding="utf-8")
    (HERE / "AGREED_FIXES.json").write_text(json.dumps(agreed, ensure_ascii=False, indent=1), encoding="utf-8")
    (HERE / "PAGES_FOR_APP_CHECK.json").write_text(json.dumps(app, ensure_ascii=False, indent=1), encoding="utf-8")
    (HERE / "AGREED_MISPRINTS.json").write_text(json.dumps(agreed_mis, ensure_ascii=False, indent=1), encoding="utf-8")
    (HERE / "OPUS_ONLY_MISPRINTS.json").write_text(json.dumps(only["opus"], ensure_ascii=False, indent=1),
                                                   encoding="utf-8")
    (HERE / "SOL_ONLY_MISPRINTS.json").write_text(json.dumps(only["sol"], ensure_ascii=False, indent=1),
                                                  encoding="utf-8")
    for m in MODELS:  # the doubtful kind, listed apart: one model's corrections of formulas, symbols, numbers, references
        (HERE / f"{m.upper()}_ONLY_MISPRINTS_MATHEMATICS.json").write_text(json.dumps(
            [x for x in only[m] if x["class"] == "mathematics"], ensure_ascii=False, indent=1), encoding="utf-8")
    (HERE / "CUT_REPORTS.json").write_text(json.dumps(CUT, ensure_ascii=False, indent=1), encoding="utf-8")
    print("pages merged", len(merged), "| batches without both answers:", {m: len(v) for m, v in missing.items()})
    print("one-model misprints by class:", {m: dict(Counter(x["class"] for x in only[m])) for m in MODELS})
    print("categories", dict(cats))
    print("agreed fixes to apply", len(agreed), "| pages for the in-app check", len(app),
          "| agreed misprints", len(agreed_mis), "| one-model misprints: opus", len(only["opus"]), "sol",
          len(only["sol"]))
