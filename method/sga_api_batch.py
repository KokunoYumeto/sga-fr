"""SGA scan check through the Message Batches API (Claude Opus 5.5, effort max): the same checker prompt as the
subagent runs (CHECKER_PROMPT_SGA.txt with the volume's TITLE and NOTE), adapted only where it speaks of tools: the four
strips of each page come attached (JPEG, full resolution), and the answer is returned instead of written to a file.
Writes run_<vol>/findings_FFF_LLL.json (the list process_sga.py reads) and findings_FFF_LLL_coordinator.md (the short
final message). Does not apply anything: run process_sga.py on each findings file afterwards.

usage: python -I run_with_note_key.py sga_api_batch.py --take 7I:4 --take 7II:4 [--budget 28] [--max-out 160000]
       (one batch at a time; refuses to submit if the worst-case cost exceeds the budget)
       python -I run_with_note_key.py sga_api_batch.py --collect BATCH_ID
"""
import base64
import io
import json
import os
import pathlib
import subprocess
import sys
import time
import urllib.request

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(__file__).resolve().parent
Q = W / "QUEUE.json"
LOG = W / "api_batches.jsonl"
TITLE = {"7I": "SGA 7 I, Groupes de monodromie en géométrie algébrique I (LNM 288, 1972)",
         "7II": "SGA 7 II, Groupes de monodromie en géométrie algébrique II (LNM 340, 1973)"}
EXTRA = {  # the per-volume additions of the last subagent prompts (6 Nov 2026), kept verbatim
    "7I": "Also handled globally, do not report: the print's straight typewriter double quotes written ``...'' or "
          "\"...\" in the TeX; blank lines around page markers that break a paragraph the print continues; underlines "
          "that run through an inner comma where the print restarts the underline. Do report a comma or full stop "
          "ending a display that sits on its own line after \\end{...} and its comment, and if you restore punctuation "
          "after a diagram, also correct a STRUCTURE comment that says it is left out. Handled globally, do not report: "
          "a paragraph that the print begins after a display and the TeX runs on (no blank line after \\end{...}); "
          "exposé numerals such as VI_B, and the superscripts ef, et and ab (U^{ef}, U^{et}, A^{ab}), set in math italic where the "
          "print is upright; capital letters that the typescript types without their accent (Evidemment, Ecrivons: "
          "the typewriter has no accented capitals), where the TeX's accented capital stands.",
    "7II": "(The rule on punctuation inside \\underline{...} also covers colons.) Also: the print's small psi is "
           "sometimes written \\Psi in the TeX, and the print's capital Lambda sometimes \\wedge: report each with a "
           "fix. Handled globally, do not report: blank lines around page markers that break a paragraph the print "
           "continues; underlines that run through an inner comma where the print restarts the underline; an "
           "underline that starts with the hyphen after a math letter. If you restore punctuation after a diagram, "
           "also correct a STRUCTURE comment that says it is left out. Handled globally, do not report: a paragraph "
           "that the print begins after a display and the TeX runs on (no blank line after \\end{...}); capital letters "
           "that the typescript types without their accent (Evidemment, Ecrivons: the typewriter has no accented "
           "capitals), where the TeX's accented capital stands.",
}
TITLE.update({"6": "SGA 6, Théorie des intersections et théorème de Riemann-Roch (LNM 225, 1971)",
              "5": "SGA 5, Cohomologie l-adique et fonctions L (LNM 589, 1977)"})
EXTRA.update({"6": "", "5": ""})  # 9 Nov 2026: starting entries for the subagent checks of SGA 6 and 5; refine after the first batches
TOOL_SENTENCE = ("Read each strip once with the Read tool; they are sharp enough for subscripts, primes and accents. "
                 "Make a crop only where one spot is genuinely unreadable; write crops and any helper script into a "
                 "folder crops_<your first page>_<your last page> inside the run folder.")
API_SENTENCE = "They are attached below, in order, at the scan's full resolution; they are sharp enough for subscripts, primes and accents."
OUT_START = "Write JSON to {OUTFILE}: "
API_OUT = ("Answer with one JSON object and nothing else: {\"findings\": [...], \"coordinator\": \"...\"}. \"findings\" is a "
           "list of {\"page\", \"where\", \"scan\", \"tex\", \"kind\" (word|formula|symbol|font|underline|missing|extra|"
           "number|punctuation|accent|misprint_in_print|marker|other), \"confidence\" (high|medium|low), \"fix\", "
           "\"corrected\" (only for misprints), \"note\"}. Only real differences. Before answering, check that every fix's "
           "\"old\" occurs exactly once in its page's TeX (write its line breaks as \\n; the TeX uses LF). \"coordinator\" is "
           "the short final message: one line with the counts per page (normal/misprint); then only what the coordinator "
           "must act on, one line each: marker problems, edits that must be applied together, and conventions of the "
           "transcription that differ from the print throughout (report such a convention once with three examples "
           "instead of every occurrence). Nothing else.")
H = {"x-api-key": os.environ.get("ANTHROPIC_API_KEY", ""), "anthropic-version": "2023-06-01",
     "content-type": "application/json", "anthropic-beta": "output-300k-2026-03-24"}
MAX_OUT = 300000


def api(method, url, body=None):
    data = json.dumps(body).encode("utf-8") if body is not None else None
    with urllib.request.urlopen(urllib.request.Request(url, data=data, headers=H, method=method), timeout=1800) as r:
        return r.read().decode("utf-8")


def system_prompt(vol):
    t = (W / "CHECKER_PROMPT_SGA.txt").read_text(encoding="utf-8")
    note = (W / ("NOTE_%s.txt" % vol)).read_text(encoding="utf-8").strip() + " " + EXTRA[vol]
    assert t.count(TOOL_SENTENCE) == 1 and t.count(OUT_START) == 1 and t.count("Folder: {FOLDER}\n") == 1
    t = t.replace(TOOL_SENTENCE, API_SENTENCE).replace("Folder: {FOLDER}\n", "")
    t = t[:t.index(OUT_START)] + API_OUT + "\n"
    t = t.replace("page_NNN_s1.png ... page_NNN_s4.png: the page", "Four images: the page")
    t = t.replace("- page_NNN.tex: the LaTeX for that page.", "- Its TeX: the LaTeX for that page.")
    t = t.replace("in page_NNN.tex", "in the page's TeX").replace("of page_NNN.tex", "of the page's TeX")
    return t.replace("{TITLE}", TITLE[vol]).replace("{NOTE}", note)


def jpeg_b64(p):
    im = Image.open(p).convert("L")
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=90)
    return base64.b64encode(buf.getvalue()).decode(), im.size


def load_q():
    return json.loads(Q.read_text(encoding="utf-8"))


def save_q(q):
    Q.write_text(json.dumps(q, indent=1), encoding="utf-8")


def submit(takes, budget):
    q = load_q()
    picked = []
    for spec in takes:
        vol, n = spec.split(":")
        picked += [b for b in q if b["vol"] == vol and b["state"] == "waiting"][:int(n)]
    reqs, est_in = [], 0
    for b in picked:
        vol, a, z = b["vol"], b["first"], b["last"]
        folder = W / ("run_" + vol) / ("b%03d_%03d" % (a, z))
        r = subprocess.run([sys.executable, "-I", str(W / "prep_sga.py"), vol, str(a), str(z), str(folder)],
                           capture_output=True, text=True)
        content, tokens = [], 0
        pages = list(range(a, z + 1))
        content.append({"type": "text", "text": "Your pages: %s." % ", ".join(map(str, pages))})
        for n in pages:
            tex = folder / ("page_%03d.tex" % n)
            if not tex.exists():
                content.append({"type": "text", "text": "Page %d: no TeX was prepared for this page (%s)." % (n, r.stdout.strip()[-200:])})
                continue
            t = tex.read_text(encoding="utf-8")
            tokens += len(t) // 3
            content.append({"type": "text", "text": "Page %d. Its TeX:\n```latex\n%s\n```\nIts scan, four strips, top to bottom:" % (n, t)})
            for s in range(1, 5):
                png = folder / ("page_%03d_s%d.png" % (n, s))
                if png.exists():
                    data, size = jpeg_b64(png)
                    tokens += 1600
                    content.append({"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": data}})
        content.append({"type": "text", "text": "Check these pages."})
        est_in += tokens + 2500
        reqs.append({"custom_id": "%s-%03d-%03d" % (vol, a, z), "params": {
            "model": "claude-opus-5-5", "max_tokens": MAX_OUT, "thinking": {"type": "adaptive"},
            "output_config": {"effort": "max"}, "system": system_prompt(vol).replace("{PAGES}", ", ".join(map(str, pages))),
            "messages": [{"role": "user", "content": content}]}})
    worst = est_in * 2e-6 + len(reqs) * MAX_OUT * 1e-5
    print("requests %d, estimated input %d tokens, worst case $%.2f (budget $%.2f)" % (len(reqs), est_in, worst, budget), flush=True)
    if worst > budget:
        raise SystemExit("worst case over budget: take fewer batches")
    body = {"requests": reqs}
    print("payload %.1f MB" % (len(json.dumps(body)) / 1e6), flush=True)
    bt = json.loads(api("POST", "https://api.anthropic.com/v1/messages/batches", body))
    ids = [(b["vol"], b["first"], b["last"]) for b in picked]
    q = load_q()
    for b in q:
        if (b["vol"], b["first"], b["last"]) in ids:
            b["state"] = "started"
    save_q(q)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps({"batch": bt["id"], "created": bt.get("created_at"), "batches": ids,
                            "estimated_input_tokens": est_in, "worst_case_usd": round(worst, 2)}) + "\n")
    print("batch", bt["id"], flush=True)
    return bt["id"]


def collect(bid):
    while True:
        s = json.loads(api("GET", "https://api.anthropic.com/v1/messages/batches/" + bid))
        print(time.strftime("%H:%M:%S"), s["processing_status"], json.dumps(s["request_counts"]), flush=True)
        if s["processing_status"] == "ended":
            break
        time.sleep(300)
    tin = tout = 0
    for line in api("GET", s["results_url"]).splitlines():
        if not line.strip():
            continue
        x = json.loads(line)
        vol, a, z = x["custom_id"].split("-")
        out = W / ("run_" + vol) / ("findings_%s_%s.json" % (a, z))
        if x["result"]["type"] != "succeeded":
            print(x["custom_id"], x["result"]["type"], json.dumps(x["result"])[:300], flush=True)
            continue
        m = x["result"]["message"]
        u = m.get("usage") or {}
        tin += u.get("input_tokens", 0)
        tout += u.get("output_tokens", 0)
        text = "".join(c.get("text", "") for c in m["content"] if c.get("type") == "text")
        (out.with_name(out.stem + "_raw.txt")).write_text(text, encoding="utf-8")
        try:
            d = json.loads(text[text.index("{"):text.rindex("}") + 1])
            out.write_text(json.dumps(d.get("findings", []), ensure_ascii=False, indent=1), encoding="utf-8")
            out.with_name(out.stem + "_coordinator.md").write_text(str(d.get("coordinator", "")) + "\n", encoding="utf-8")
            print(x["custom_id"], m.get("stop_reason"), "findings", len(d.get("findings", [])), "out tokens", u.get("output_tokens"), flush=True)
        except Exception as e:  # noqa: BLE001
            print(x["custom_id"], "could not parse the answer:", e, flush=True)
    print("tokens in %d, out %d, about $%.2f at batch price" % (tin, tout, tin * 2e-6 + tout * 1e-5), flush=True)


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--collect" in args:
        collect(args[args.index("--collect") + 1])
    else:
        takes = [args[i + 1] for i, a in enumerate(args) if a == "--take"]
        budget = float(args[args.index("--budget") + 1]) if "--budget" in args else 28.0
        if "--max-out" in args:  # a lower cap fits more requests into the worst case (observed: 30-82 thousand)
            MAX_OUT = int(args[args.index("--max-out") + 1])
        collect(submit(takes, budget))
