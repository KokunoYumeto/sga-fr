"""Score the SGA 4 API comparison (sga4_api_compare.py) against the subagent reference (run_4/findings_FFF_LLL.json).

Reference items: a transcription error is a finding with a fix dict; a misprint of the print has kind
misprint_in_print and fix null. A configuration's finding matches a reference item on the same page when:
- for a transcription error: its fix has the same effect on the page's TeX (both applied, whitespace normalised), or
  the adjudication file (run_4/api_compare/ADJUDICATION.json, written by hand after looking at the candidates) says it
  is the same correction in other LaTeX;
- for a misprint: the adjudication file says so (candidates are proposed by the position of the quoted TeX).
Everything else is an extra, adjudicated against the scan in ADJUDICATION.json (real / false / doubtful).

usage: python -I sga4_api_score.py candidates CONFIG      list reference items with candidate matches, and the extras
       python -I sga4_api_score.py table                  the summary table (from ADJUDICATION.json and RUNS.jsonl)
"""
import difflib
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(__file__).resolve().parent
R = W / "run_4"
OUT = R / "api_compare"
BATCHES = [(41, 45), (51, 55), (101, 105), (361, 365), (386, 390), (401, 405)]
ADJ = OUT / "ADJUDICATION.json"


def norm(s):
    return re.sub(r"\s+", " ", s or "").strip()


def tex_of(page):
    for a, z in BATCHES:
        if a <= page <= z:
            return (R / ("b%03d_%03d" % (a, z)) / ("page_%03d.tex" % page)).read_text(encoding="utf-8")
    return ""


def items(folder):
    """Findings of a folder, with ids p<page>.<n> in page order."""
    out, count = [], {}
    for a, z in BATCHES:
        p = folder / ("findings_%03d_%03d.json" % (a, z))
        fl = json.loads(p.read_text(encoding="utf-8")) if p.exists() else []
        for f in fl:
            try:
                page = int(str(f.get("page")).strip())
            except ValueError:
                page = 0
            count[page] = count.get(page, 0) + 1
            fix = f.get("fix") if isinstance(f.get("fix"), dict) else None
            out.append({"id": "p%d.%d" % (page, count[page]), "page": page, "kind": f.get("kind"), "fix": fix,
                        "f": f, "pos": locate(page, f, fix)})
    return out


def locate(page, f, fix):
    """Character span of the finding on its page's TeX: the fix's old if unique, else the longest match of 'tex'."""
    t = tex_of(page)
    if fix and t.count(fix.get("old", "\0")) == 1:
        i = t.index(fix["old"])
        return (i, i + len(fix["old"]))
    q = f.get("tex") or (fix or {}).get("old") or ""
    if not q:
        return None
    m = difflib.SequenceMatcher(None, t, q, autojunk=False).find_longest_match(0, len(t), 0, len(q))
    return (m.a, m.a + m.size) if m.size >= 6 else None


def effect(page, fix):
    t = tex_of(page)
    if not fix or t.count(fix.get("old", "\0")) != 1:
        return None
    return norm(t.replace(fix["old"], fix.get("new", ""), 1))


def near(p, q, slack=60):
    return p and q and p[0] - slack <= q[1] and q[0] - slack <= p[1]


def short(x, n=150):
    f = x["f"]
    if x["fix"]:
        body = "%r -> %r" % (x["fix"].get("old", "")[:70], x["fix"].get("new", "")[:70])
    else:
        body = "tex %r | corr %r" % ((f.get("tex") or "")[:60], (f.get("corrected") or "")[:60])
    return ("[%s] %s %s" % (x["kind"], body, norm(f.get("note"))[:n]))


def candidates(cfg):
    ref, got = items(R), items(OUT / cfg)
    used = {}
    print("== %s: %d findings (%d with fix)" % (cfg, len(got), sum(1 for g in got if g["fix"])))
    for r in ref:
        same = [g for g in got if g["page"] == r["page"]]
        exact = [g for g in same if r["fix"] and g["fix"] and effect(g["page"], g["fix"]) == effect(r["page"], r["fix"])
                 and effect(r["page"], r["fix"])]
        if exact:
            print("%s EXACT %s" % (r["id"], exact[0]["id"]))
            used[exact[0]["id"]] = r["id"]
            continue
        cand = [g for g in same if near(g["pos"], r["pos"])]
        print("%s %s  %s" % (r["id"], "TEX-ERROR" if r["fix"] else "MISPRINT", short(r, 80)))
        for g in cand:
            print("     cand %s %s" % (g["id"], short(g, 100)))
    print("-- not matched exactly:")
    for g in got:
        if g["id"] not in used:
            print("  %s %s" % (g["id"], short(g, 160)))


def table():
    adj = json.loads(ADJ.read_text(encoding="utf-8"))
    ref = items(R)
    n_err = sum(1 for r in ref if r["fix"])
    n_mis = len(ref) - n_err
    runs = {}
    for line in (OUT / "RUNS.jsonl").read_text(encoding="utf-8").splitlines():
        x = json.loads(line)
        if x["event"] == "done":
            runs[x["run"]] = x
    rows = []
    for cfg, a in adj["configs"].items():
        got = items(OUT / cfg)
        exact = {}
        for r in ref:
            for g in got:
                if g["page"] == r["page"] and r["fix"] and g["fix"] and effect(g["page"], g["fix"]) == effect(
                        r["page"], r["fix"]) and effect(r["page"], r["fix"]):
                    exact[r["id"]] = g["id"]
                    break
        match = dict(exact)
        match.update(a.get("match", {}))           # reference id -> finding id (same correction)
        partial = a.get("partial", {})              # reference id -> finding id (spot found, wrong treatment)
        err_ok = sum(1 for r in ref if r["fix"] and r["id"] in match)
        mis_ok = sum(1 for r in ref if not r["fix"] and r["id"] in match)
        matched_ids = set(match.values()) | set(partial.values()) | set(a.get("duplicate", []))
        extras = [g["id"] for g in got if g["id"] not in matched_ids]
        verdict = a.get("extras", {})
        rows.append({"config": cfg, "findings": len(got), "err": err_ok, "n_err": n_err, "mis": mis_ok, "n_mis": n_mis,
                     "partial": len(partial), "extras": len(extras), "unadjudicated": [e for e in extras if e not in verdict],
                     "real": sum(1 for e in extras if verdict.get(e, "").startswith("real")),
                     "false": sum(1 for e in extras if verdict.get(e, "").startswith("false")),
                     "doubtful": sum(1 for e in extras if verdict.get(e, "").startswith("doubtful")),
                     "phi": a.get("phi"), "run": runs.get(cfg)})
    print(json.dumps(rows, indent=1, default=str)[:20000])


def matched(cfg, a, ref):
    """Reference ids found by a configuration (exact-effect fixes plus the hand matches)."""
    got = items(OUT / cfg)
    out = set(a.get("match", {}))
    for r in ref:
        if r["fix"] and any(g["page"] == r["page"] and g["fix"] and effect(r["page"], r["fix"])
                            and effect(g["page"], g["fix"]) == effect(r["page"], r["fix"]) for g in got):
            out.add(r["id"])
    return out


def detail():
    """Per-batch counts, real extras and unions of configurations (for the report)."""
    adj = json.loads(ADJ.read_text(encoding="utf-8"))
    ref = items(R)
    runs = {}
    for line in (OUT / "RUNS.jsonl").read_text(encoding="utf-8").splitlines():
        x = json.loads(line)
        if x["event"] == "done":
            runs[x["run"]] = x
    found, real = {}, {}
    for cfg, a in adj["configs"].items():
        found[cfg] = matched(cfg, a, ref)
        real[cfg] = {k for k, v in a["extras"].items() if v.startswith("real")}
        print("==", cfg)
        for (lo, hi), rq in zip(BATCHES, sorted(runs[cfg]["requests"], key=lambda q: q["batch"])):
            rr = [r for r in ref if lo <= r["page"] <= hi]
            te = [r for r in rr if r["fix"]]
            mp = [r for r in rr if not r["fix"]]
            print("  %03d-%03d  TE %d/%d  MP %d/%d  findings %s  out %s  fix-old-not-unique %s" % (
                lo, hi, sum(r["id"] in found[cfg] for r in te), len(te), sum(r["id"] in found[cfg] for r in mp),
                len(mp), rq.get("findings"), rq.get("output_tokens"), rq.get("fix_old_not_unique")))
        print("  missed TE:", sorted(r["id"] for r in ref if r["fix"] and r["id"] not in found[cfg]))
        print("  missed MP:", sorted(r["id"] for r in ref if not r["fix"] and r["id"] not in found[cfg]))
    # the real extras, keyed by the place (page and what), from real_extras_union
    places = {"TE:p44-E''": {"opus55-high", "sol61-high", "sol61-max"},
              "MP:p44-par": {"fable52-medium", "sol61-high", "sol61-max"},
              "MP:p404-algebriquements": {"fable52-medium", "sol61-high", "sol61-max"}}
    n_te = sum(1 for r in ref if r["fix"]) + 1
    n_mp = sum(1 for r in ref if not r["fix"]) + 2
    print("== against reference + real extras (TE %d, MP %d); subagent: TE %d, MP %d" % (n_te, n_mp, n_te - 1, n_mp - 2))
    import itertools
    cfgs = list(adj["configs"])
    for k in range(1, len(cfgs) + 1):
        for combo in itertools.combinations(cfgs, k):
            f = set().union(*(found[c] for c in combo))
            te = sum(1 for r in ref if r["fix"] and r["id"] in f) + sum(
                1 for p, s in places.items() if p.startswith("TE") and s & set(combo))
            mp = sum(1 for r in ref if not r["fix"] and r["id"] in f) + sum(
                1 for p, s in places.items() if p.startswith("MP") and s & set(combo))
            usd = sum(runs[c]["billed_usd"] for c in combo)
            print("  %-45s TE %2d/%d  MP %2d/%d  $%.2f  $/page %.4f  SGA4 $%.0f" % (
                "+".join(combo), te, n_te, mp, n_mp, usd, usd / 30, usd / 30 * 1609))


if __name__ == "__main__":
    if sys.argv[1] == "detail":
        detail()
    elif sys.argv[1] == "candidates":
        candidates(sys.argv[2])
    elif sys.argv[1] == "reference":
        for r in items(R):
            print(r["id"], "TEX-ERROR" if r["fix"] else "MISPRINT", short(r, 60))
    else:
        table()
