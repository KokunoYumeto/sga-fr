# SGA 5, 6, 7 I and 7 II: checking the French transcriptions against the printed pages

Working log of the method, kept for a later write-up (GitHub provenance, a methodology section, a post). It follows
the EGA scan check (`ega_scan_check_20261101/METHODOLOGY.md`); this file records what is specific to SGA. Dates are
2026.

## 1. Material

- **Print:** the Lecture Notes in Mathematics volumes of the Séminaire de géométrie algébrique du Bois-Marie: SGA 5
  (LNM 589, 1977), SGA 6 (LNM 225, 1971), SGA 7 I (LNM 288, 1972), SGA 7 II (LNM 340, 1973): offset reproductions
  of typescripts (typed text, formulas partly typed and partly written by hand, emphasis by underlining). About
  2,150 printed pages.
- **Scans** (survey of every copy on disk, measured resolution, 4 November: `sga_scan_check_prep_20261104/INVENTORY.md`):
  SGA 5 the 300-dpi flatbed scan (the only one), SGA 6 and SGA 7 I the Internet Archive copies (about 360 ppi),
  SGA 7 II the IAS scan (300 dpi). Independent 300-dpi DjVu copies of SGA 6, 7 I and 7 II serve as second witnesses
  for thin strokes (the Internet Archive compression can drop a comma or a prime).
- **Transcriptions:** AI transcriptions made in June–August 2026 (Codex), each in a diplomatic layer and a corrected
  layer. They were copied into this folder for the check; the corpus itself is not changed.

## 2. Decisions taken with the user (5 November)

- SGA 5: the corrected layer existed in two diverged versions (c4, c5); c5 is the base, and what only c4 has is
  brought over after comparison.
- SGA 6: the corrections of 23 August were written into a tree its own note marks as a mixed layer; each is checked
  against the scan before it moves into the corrected layer (`sga6/HOLD_VS_CORR.md`: 119 differences, 80 with a
  correction note).
- Missing front matter (introductions, tables of contents) is transcribed from the scans as part of the check.
- Page markers are added to SGA 5 and SGA 6 ("fine as long as they're not ugly").

## 3. Page markers

SGA 7 I and 7 II already mark every printed page with a comment line
`%%%%%%%%%%  scan idx N  |  folio F  %%%%%%%%%%`. SGA 5 and SGA 6 had none. They were placed by aligning the scan's
own OCR text with the TeX (`insert_markers.py`): accent-free words of four or more letters, in order, aligned with
`difflib`; the marker goes on a line of its own before the first word of the page (a comment line adds nothing to
the output), never inside inline mathematics or a braced argument. A second pass (`refine_markers.py`) moves a
marker before a heading or a display that opens the page. Result: SGA 5 482 of 484 pages, SGA 6 697 of 700. The
checkers report any marker that is off.

## 4. The check

Batches of five printed pages (`queue_sga.py`, 431 batches), one Claude subagent each:
- `prep_sga.py`: the page's TeX (marker to marker) and the scan at its own resolution (360 ppi or 300 dpi), cropped
  to the ink and cut into four overlapping strips;
- `CHECKER_PROMPT_SGA.txt`: as for EGA, adapted to typescripts (underlining for emphasis, hand-written symbols, the
  typist's corrections count as the print, physical defects are not misprints); conventions that hold for a whole
  volume are reported once with examples and decided once (`GLOBAL_ISSUES_SGA.md`);
- `process_sga.py`: applies each fix when its `old` is unique on the page, logs it (`FIXLOG_<vol>.jsonl`), replays
  transcription fixes on the corrected layer (`FIXLOG_<vol>_CURRENT.jsonl`), and records misprints of the print
  (`MISPRINTS_<vol>.json`).

**The per-batch note is revised in a loop.** Each checker reports conventions that hold beyond its pages; they go into
`GLOBAL_ISSUES_SGA.md`, and the next batches' prompts name them as known: either "handled globally, do not report"
(double-struck Z, Q, F, C, A typed as bold in the TeX; the typescript's letter o for an index zero) or "report each
case with a fix" (punctuation after diagrams left out; commas added in intersection numbers). So the findings stay
about the page in front of the checker, and a whole-volume decision is taken once.

**Pilot (SGA 7 I and 7 II, pp. 1–5 each):** 210–280 thousand subagent tokens per batch (about 50 thousand per page).
SGA 7 I's transcription had silently corrected many misprints of the print; the diplomatic layer now keeps them, and
the misprint list gives the corrected layer its readings.

## 5. The API path (8 November 2026)

From 8 Nov the batches also run through the Message Batches API (`sga_api_batch.py`, Claude Opus 5.5, effort max,
adaptive thinking), on the remaining API credit of account F, so that the plan's usage is kept for the work that
needs tools. The prompt is the subagent prompt with only its tool sentences changed: the four strips of each page
come attached (greyscale JPEG, quality 90, full resolution) and the answer comes back as one JSON object (findings and
the short coordinator message) instead of a file; the note is the same (`NOTE_<vol>.txt` plus the per-volume
additions kept in `sga_api_batch.py`, which `render_sga_prompt.py` also uses for the subagent prompts). The findings
go through `process_sga.py` like any other batch.

First batch (msgbatch_01JEX1HtrWtrsLbDZ4w1DhgJ: 7 I pp. 251-270, 7 II pp. 266-285): 8 requests, 343 thousand input
and 376 thousand output tokens (30-82 thousand per request, thinking included), about $4.44 at the batch price, against
a worst-case estimate of $24.62 with a 300-thousand output cap. The yield matches the subagent batches before it
(normal/misprint findings per five pages: 7 I 1/0, 2/4, 2/6, 3/6 against 2/3 to 6/11; 7 II 1/13, 6/10, 4/14, 1/10
against 0/4 to 6/18). All 22 fixes applied (one low-confidence formula, 7 I p. 256 nQ = 0 against {}_nQ = 0,
checked on the scan: the n stands on the line, and the proof uses multiplication by n). From the second batch the
output cap is 160 thousand (`--max-out`), so that more requests fit the worst case within the remaining credit.

Cost, 8 Nov 2026 (rows in C:\Users\user\Documents\compute_cost_ledger\LEDGER.jsonl): API batches $0.09-0.11 billed per printed page (batch price), 34 requests so far; subagent checks $2.90-7.26 per five pages at list price (mean $4.57), about 4-5 times the API path at list price, mostly from re-reading the growing context (4-21 million cache-read tokens per run). The prompts are CHECKER_PROMPT_SGA.txt with NOTE_<vol>.txt and the per-volume additions in sga_api_batch.py; each subagent batch keeps its rendered prompt as run_<vol>/b<first>_<last>/CHECKER_PROMPT.txt.

**Correction, 9 November 2026.** Over 32 API batches of SGA 7 I (pp. 251-270 and 401-530) the API checker found 2.25
transcription errors and 0.41 misprints of the print per five pages, against 4.88 and 0.79 for the 57 subagent
batches of pp. 1-400: about half. The first batch's comparison above was too small to show it. The API checker sees
only fixed strips of the main scan (no zoom, no crop, no second witness), which matters on these typescript scans.
The API route is therefore not used for the scan check; the pages it checked (7 I pp. 251-270 and 401-530, 7 II
pp. 266-285 and 396-430) are to be checked again by subagents.

## 6. SGA 4: API first pass (11 November 2026)

SGA 4 is a clean print (Springer LNM 269, 270, 305); its French TeX is Fabrice Orgogozo's LaTeX edition (snapshot
`71766d9`) as kept in Codex's corpus. In the comparison of 10 November (`SGA4_API_COMPARISON_20261110.md`) Claude
Opus 5.5 at effort high and GPT-6.1 Sol at effort max together found every transcription error the subagents had found
on 30 pages, at $0.054 a page. On 11 November the user chose to check all of SGA 4 that way first ("the most
efficient way to do the fix [of] SGA 4 would be over the API first pass ... any disagreements that come from that, or
any uncertainties, would be additionally checked", in the app). Every page with TeX (1,557) went to both models; the
fixes both give identically are applied (`FIXLOG_4.jsonl`, replayed on the corrected layer in
`FIXLOG_4_CURRENT.jsonl`), except where a safety hold applies; everything else is listed page by page in
`sga4_api_pass_20261111/PAGES_FOR_APP_CHECK.json` for the in-app check. Method, holds and figures:
`sga4_api_pass_20261111/README.md`; volume-wide points: items 90-95 of `GLOBAL_ISSUES_SGA.md`.

## Model provenance, 10-11 November 2026

- Scan checks and in-app re-checks (SGA 5, 6, 7 I, 7 II batches of 10 Nov): Claude Opus 5.5 subagents (session default effort); fixes applied by process_sga.py, run by Claude Opus 5.5.
- Cross-volume error-pattern review (FABLE_PILOT_PATTERNS_20261110.md): Claude Fable 5.2, subagent, high effort.
- Combined misprint round (misprint_pass, batches 7I_301, 7II_401-403): GPT-6.1 Sol (OpenAI API, effort high, Flex tier); decisions applied by apply_decisions.py.
- REPLAY_MANUAL hand edits (REPLAY_MANUAL_<vol>_DONE.json): Claude Opus 5.5 subagent, medium effort.
- Reconciliation with Codex's earlier SGA 5/6 corrections (RECONCILE_CODEX_5/6.json): Claude Opus 5.5 subagent, high effort. Codex's corrections themselves: OpenAI Codex sessions (August-September).
- SGA 4 API first pass (sga4_api_pass_20261111, 11 Nov): the page checks by Claude Opus 5.5 (`claude-opus-5-5`, Message Batches API, effort high, adaptive thinking) and GPT-6.1 Sol (`gpt-6.1-sol`, OpenAI Responses API, reasoning effort max, Flex tier); page table, batches, merge, application (apply_pass.py) and compile checks run by a Claude Opus 5.5 subagent.
