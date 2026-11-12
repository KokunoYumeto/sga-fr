"""The misprint pass of a corrected French SGA layer with OpenAI GPT-6.1 Sol (effort high, Flex tier), batch by batch:
the EGA misprint prompt of 5 November (ega_scan_check_20261101/MISPRINT_PROMPT.txt) for one-shot answers. Answers in
answer_<batch>.md and decisions_<batch>.json; each decisions file is dry-run with apply_decisions.py.
usage: python -I run.py VOL [CONCURRENCY=3] [--only=BATCH,...]
The API key is read from the user's note at run time by enr_pilot (never printed or stored)."""
import json
import os
import re
import subprocess
import sys
import time

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Users\user\Documents\enriques_api_pilot_20261106")
import enr_pilot as P  # noqa: E402

PROMPT = r"""You correct the printed misprints in the corrected French edition of SGA 7 (Groupes de monodromie en géométrie
algébrique; SGA 7 I = Lecture Notes in Mathematics 288, 1972; SGA 7 II = LNM 340, 1973; offset reproductions of
typescripts, emphasis by underlining). Exposé VI of SGA 7 I is printed in English: there the "French" text is English.

The French SGA 7 has two editions. The diplomatic edition reproduces the printed pages, including their misprints. The
corrected edition is meant to give the correct reading wherever the print has a misprint, but it still holds whatever
the transcription had before the scan check: often the printed (wrong) reading, sometimes another slip. The checkers
recorded every misprint with the printed reading and the correct one.

Your batch is below, between BEGIN BATCH and END BATCH. Per printed page: the corrected edition's text of the page
("----- corrected edition, <file>, page ... -----"), then the misprints recorded there ("[id ...]" with WHERE, PRINT,
CORRECT, TEX BEFORE, NOTE), then the diplomatic edits made on that page for misprints (OLD = the transcription before,
NEW = the printed reading).

For each id decide:
- "apply": the corrected edition does not yet give the correct reading. Give an exact edit of the corrected edition:
  "file" (as named in the block), "old" (an exact substring of that page's text, long enough to occur only once in
  it) and "new" (the same text with the correct reading). Change only the misprint itself.
- "already": the corrected edition already has the correct reading.
- "keep": the recorded "correct" reading is not a certain correction (a deliberate notation or abuse of notation, a
  reading that the mathematics does not settle, a correction that would change the author's argument or wording
  beyond the slip, or a typographic detail of the typescript without effect on the meaning, such as spacing, the
  shape of a dash or of a hand-written symbol, or the extent of an underline). Say why in "note".
- "unclear": you cannot find the place; say why in "note".

Rules:
- Check each correction against the mathematics of the passage yourself: the right letter, index, sign, reference
  number or word must follow from the context (definitions, the statement being proved, the numbering of the cited
  item). A recorded "correct" reading is a proposal, not an authority.
- Corrections of references: the corrected number must point to the statement actually used (check its content in
  the context or by its number in the page's own text); otherwise "keep".
- French spelling and grammar slips of the print (accents, agreement, a missing or doubled letter, a typing error in
  a word): "apply" with the correct French. Leave the typescript's own conventions alone (e.g. capital letters
  without accents, underlining for emphasis).
- Use the edition's own LaTeX conventions as they appear in the page text. Never change the page-marker comment lines
  ("%%%%%%%%%%  scan idx N  |  folio F  %%%%%%%%%%") or \label keys.
- If one edit covers several ids, put it in the first and give the others "already" with note "covered by <id>".
  No two "apply" edits may overlap.

Answer with one fenced block ```json containing one JSON list, one object per id, in the batch's order:
  {"id": "...", "decision": "apply"|"already"|"keep"|"unclear", "file": ..., "old": ..., "new": ..., "note": "..."}
("file", "old", "new" only for "apply"; LF line breaks as \n.) After the block, one line each: the "keep" decisions
that a reader should still know about (a real error of the print you could not settle). Nothing else.
"""


def submit(name, effort="high"):
    vol = name.split("_")[1]
    text = open(os.path.join(HERE, f"batches_{vol}", name + ".txt"), encoding="utf-8").read()
    body = {"model": "gpt-6.1-sol", "input": PROMPT + "\nBEGIN BATCH\n" + text + "\nEND BATCH\n",
            "reasoning": {"effort": effort}, "max_output_tokens": 128000, "background": True, "service_tier": "flex"}
    code, r = P.call("POST", P.API, body)
    return code, r.get("id"), r.get("error")


def finish(vol, name, r):
    text = "".join(c.get("text", "") for o in r.get("output", []) if o.get("type") == "message"
                   for c in o.get("content", []))
    open(os.path.join(HERE, f"answer_{name}.md"), "w", encoding="utf-8").write(text)
    m = re.search(r"```json\s*\n(.*?)```", text, re.S)
    ok = False
    if m:
        try:
            lst = json.loads(m.group(1))
            json.dump(lst, open(os.path.join(HERE, f"decisions_{name}.json"), "w", encoding="utf-8"), ensure_ascii=False,
                      indent=1)
            ok = True
        except ValueError as e:
            print(name, "JSON error", e, flush=True)
    u = r.get("usage") or {}
    usd = (u.get("input_tokens", 0) * 2 + u.get("output_tokens", 0) * 10) / 1e6 / 2
    dry = ""
    if ok:
        res = subprocess.run([sys.executable, "-I", "-B", os.path.join(HERE, "apply_decisions.py"), vol,
                              os.path.join(HERE, f"decisions_{name}.json"), "--dry"], capture_output=True, text=True,
                             encoding="utf-8")
        dry = (res.stdout.strip().splitlines() or [res.stderr.strip()[-300:]])[-1]
    return ok, round(usd, 4), dry, u


def run(vol, conc, only=None):
    sp = os.path.join(HERE, f"state_{vol}.json")
    st = json.load(open(sp, encoding="utf-8")) if os.path.exists(sp) else {}
    index = json.load(open(os.path.join(HERE, f"batches_{vol}", "BATCHES.json"), encoding="utf-8"))
    todo = [b["batch"] for b in index if not os.path.exists(os.path.join(HERE, f"decisions_{b['batch']}.json"))
            and (only is None or b["batch"] in only)]
    flying = {n: v["id"] for n, v in st.items() if v.get("status") == "submitted" and n in todo}
    queue = [n for n in todo if n not in flying]
    while queue or flying:
        while queue and len(flying) < conc:
            n = queue.pop(0)
            code, rid, err = submit(n)
            if code >= 300 or not rid:
                print(n, "submit failed", code, json.dumps(err)[:200], flush=True)
                time.sleep(30)
                queue.append(n)
                continue
            flying[n] = rid
            st[n] = {"status": "submitted", "id": rid, "t": time.time(), "tries": st.get(n, {}).get("tries", 0) + 1}
            json.dump(st, open(sp, "w", encoding="utf-8"), indent=1)
        time.sleep(45)
        for n, rid in list(flying.items()):
            code, r = P.call("GET", f"{P.API}/{rid}")
            s = r.get("status")
            if s in ("queued", "in_progress"):
                continue
            del flying[n]
            if s == "completed":
                ok, usd, dry, u = finish(vol, n, r)
                st[n].update(status="done" if ok else "bad_answer", usd=usd, dry=dry,
                             tokens=[u.get("input_tokens"), u.get("output_tokens")],
                             minutes=round((time.time() - st[n]["t"]) / 60, 1))
                print(n, st[n]["status"], f"${usd}", st[n]["minutes"], "min |", dry, flush=True)
            else:
                st[n].update(status=s)
                print(n, s, json.dumps(r.get("error"))[:200], flush=True)
                if st[n]["tries"] < 3:
                    queue.append(n)
            json.dump(st, open(sp, "w", encoding="utf-8"), indent=1)
    print(vol, "done; cost so far", f"${sum(v.get('usd') or 0 for v in st.values()):.2f}", flush=True)


if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    o = dict(x[2:].split("=", 1) for x in sys.argv[1:] if x.startswith("--") and "=" in x)
    run(a[0], int(a[1]) if len(a) > 1 else 3, o["only"].split(",") if "only" in o else None)
