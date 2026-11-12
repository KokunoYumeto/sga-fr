# SGA 4: first pass of the scan check over the APIs (11 November 2026)

Every printed page of SGA 4 that has TeX, 1,557 pages, checked against the scans by two models. Where both give the
same fix, it is applied to the SGA 4 working copy; everything else is listed for an in-app check (not run here).

The method, as agreed with the user: the API pair of the comparison (`../SGA4_API_COMPARISON_20261110.md`) on every
page, then an in-app check of the pages where the two disagree or flag a doubt (user, 11 Nov about 00:50 UTC: "Your
middle ground's probably smart ... API plus checking disagreement"; user, 11 Nov: "the most efficient way to do the fix
[of] SGA 4 would be over the API first pass ... any disagreements that come from that, or any uncertainties, would be
additionally checked").

## Models and efforts

- **Claude Opus 5.5** (`claude-opus-5-5`), effort **high** (`output_config.effort`), adaptive thinking, **Message
  Batches API**, batch price $2 / $10 per million input / output tokens. Output cap 64,000 tokens per request (the
  comparison's largest Opus answer was 6,105 tokens; an answer cut at the cap would be sent again with 128,000).
- **GPT-6.1 Sol** (`gpt-6.1-sol`), reasoning effort **max**, OpenAI **Responses API, Flex tier**, background mode, Flex
  price $1 / $5 per million. Output cap 128,000 tokens, as in the comparison.

Keys: Anthropic account B (`Untitled 1939.md`, through `claude_tools\run_with_note_key.py`, Message Batches only);
OpenAI through `enriques_api_pilot_20261106\enr_pilot.py` (Flex only). Neither key is printed or stored here.

**Outcome** (final, 11 Nov 2026, 19:00 UTC): all 1,557 pages checked by both models; 898 agreed fixes applied to
`sga4/diplomatic` and 774 of them replayed on `sga4/current`; 443 pages listed for the in-app check
(`PAGES_FOR_APP_CHECK.json`); 930 misprints of the print reported by both models, recorded and not applied; the
edition compiles as before. Cost: Opus $44.66, Sol $47.14. Details under Results; what needs a decision under Needs a
decision.

## Source of record (checked 11 Nov 2026, 10:00-10:40 UTC)

- **What the comparison checked**: `sga4/diplomatic/<NN>/<NN>.tex` of Codex's French SGA corpus,
  `C:\Users\user\Documents\interlanguage_parts\03_projects\language_management\english_germanic\03_working_translations\sga_french_canonical_corpus_20260804_r1\sga4\diplomatic`.
  The six files' SHA-256 in `../run_4/PREP_MANIFEST.json` equal the corpus files today (01 `1955F5FD…`, 04
  `3E47DAA9…`, 05 `6BAF0AF1…`, 08 `3CCEA04A…`, 10 `8895C178…`, 17 `54200E1C…`).
- **What it is**: Fabrice Orgogozo's French LaTeX edition of SGA 4, Tomes 1-3
  ([normalesup.org/~forgogozo/SGA4](https://www.normalesup.org/~forgogozo/SGA4/)), snapshot at git commit `71766d9`
  (archive `SGA4-HEAD-71766d9.tar.gz`, SHA-256 `DA2D939D3BD66B03E7BEFF4353550F7A27982847AE4F798D0872F1DB5D64C7DC`;
  extracted copy in `interlanguage_parts\tmp\pdfs\sga4_orgogozo_71766d9_preflight_20260719T065631`), with Codex's
  source-keeping edits of August-September 2026 (unique bibliography keys, labels, and a few readings brought back to
  the print; 18 of the 20 exposé files differ from the snapshot, 2-146 lines each; newest file 01.tex, 24 Sep). This
  is the text the English SGA 4 was translated from; the credit used here is the one of sga-en's README, ATTRIBUTION.md
  and `sources/native/SGA4/SOURCES.md`: "the French LaTeX edition of SGA 4, Tomes 1–3, distributed by Fabrice Orgogozo
  (normalesup.org/~forgogozo/SGA4; source snapshot at git commit 71766d9)".
- **Repository records**: sga-en (`rights_cc0_20261025\sga-en`, fetched: main `c027e90` = origin/main, clean); latest
  release `v2026-11-10-english-edition` (10 Nov). Its `SOURCE_AUTHORITY.md` refers the exact source identities to the
  release's evidence ZIP; SOURCES.md and the reader's source notice name the snapshot `71766d9`. No French SGA 4
  repository of ours exists.
- **Audit row** (`SOURCE_OF_RECORD_AUDIT_20261110\README.md`, French SGA, "SGA 1, 2, 4, 4½"): corpus
  `sga4\{diplomatic,corrected_history}`, not scan-checked, not touched in November; open point: the V bis overlay of
  28 Sep. Settled here: the overlay `canonical_overlays\sga4t2\c0054_20260928` changes the **corrected** layer only
  (10 line edits of 05bis, `CURRENT.json`: "corrected/current only"; its parent is `through_0370\05bis\05bis.tex`, hash
  checked), so the diplomatic layer the pass checks is unaffected.
- **Corrected layer**: `corrected_history\through_0370` (5 Sep 2026; Codex's corrections SGA4-CORR-0001 to 0370, misprints
  of the print corrected with `\sisi`), with 05bis from the overlay above.
- **Working copy** (made by `make_working_copy.py`; the corpus is only read): `..\sga4\diplomatic` (the corpus
  diplomatic layer) and `..\sga4\current` (the corrected layer); `..\sga4\SOURCE.json` lists every file's size and
  SHA-256 at the copy.

## Scans

As in the comparison (`../run_4/BATCHES.json`), 300 dpi bitonal:
- Tome 1 (LNM 269, Exp. I-IV): `C:\Users\user\Documents\sga4_scans_20261110\rochester_artin-SGA4-1.pdf` (byte-identical
  to `Downloads\artin-SGA4-1.pdf`, the copy the user found next to Tome 2);
- Tome 2 (LNM 270, Exp. V-VIII): `C:\Users\user\Downloads\artin-SGA4-2.pdf`;
- Tome 3 (LNM 305, Exp. IX-XIX): `C:\Users\user\Documents\Papors\OS\Théorie des topos et cohomologie étale des schemas  [SGA 4] ( etc.).pdf`
  (JBIG2 text layer), with Springer's lossless scan of Exposés XVII-XVIII as second witness,
  `C:\Users\user\Downloads\Number4.pdf` (336 pages of the pass have witness strips).

## Pages (`build_pages.py`, `PAGES.json`)

The edition marks the start of each printed page with `\pageoriginale`, a counter set per exposé. The page table puts
every marker on its scan page and cuts the TeX into pages; the scans' own OCR text layer (`ocr/`, made by
`ocr_extract.py`, never shown to the models) does the placing:

- **Scan page of each TeX page**: the Springer folio printed at the foot of each scan page (OCR), with a Viterbi path
  per exposé over offsets between the counter and the scan, scored by how many of the page's first TeX words stand in
  the first three OCR lines. All 1,557 TeX pages land on distinct scan pages; every spot-check page lands where the
  hand cut of 10 Nov put it. The scan pages that no TeX page takes are the exposés' title and summary pages, which the
  edition does not reproduce (V p. 1, Vbis p. 83, VI pp. 163-164, VII p. 341, VIII p. 366, XVI p. 206, XVII
  pp. 250-251), besides each tome's front matter and indexes.
- **Where a page begins**: the marker stands after the page's first word or two, or after a heading or display that
  opens the page, so the block of display and heading lines before a marker can belong to either page. The OCR decides
  where it can (the words of a heading at the top of the new page or at the foot of the old one; whether the old page
  ends with the last running words before a display). Where it cannot, the block goes to both pages, and the marker
  line goes to both when two or more words precede the marker. The page's first comment line names these lines
  ("its lines 1-3 (source lines 4396-4398) ... may end p. 102 instead of opening this page"). 1,046 of the 1,557 pages
  have such a note. On the 30 spot-check pages every hand-cut span lies inside the automatic one.
- `PAGES_DIAG.json`: the 99 pages whose first words the OCR does not show at the top of the scan page (mostly pages
  opening with a formula; their placement rests on the exposé's offset) and the scan pages without TeX.

Two facts about the edition came out of this (see "Needs a decision"): the `\pageoriginale` counter runs one page
behind Springer's numbers in Exposé II and two in Exposé III; and a marker of Exposé Vbis stands inside a
commented-out printed passage.

## Method (`sga4_full_pass.py`)

- **Batches**: the pages of one exposé in groups of up to five, cut at Springer folios 1-5, 6-10, ... (327 batches: 294
  of five pages, 33 of one to four at the ends of exposés). The six batches of the comparison (V 41-45, X 51-55,
  I 101-105, XVII 361-365, VIII 386-390, IV 401-405) were not sent again; their Opus 5.5 high and Sol max answers of
  10 Nov are imported (`import-comparison`). 321 batches were sent to each model.
- **Inputs per page**: its TeX (`batches/<KEY>/page_FFF.tex`: the comment line, then whole lines of
  `sga4/diplomatic`) and its four strips (`strips/t<tome>/pFFF_s1..4.png`, rendered by `prep_strips.py` exactly as
  `prep_sga4.py` did: grey, 300 dpi, cropped to the ink, four overlapping strips), sent as greyscale JPEG quality 90 at
  full resolution; for Exposés XVII-XVIII also the four witness strips. As in the comparison.
- **Prompt**: the comparison's API prompt (`sga4_api_compare.api_prompt`: `CHECKER_PROMPT_SGA.txt` with `NOTE_4.txt`,
  rendered by `render_sga4_prompt.template()`, its tool sentences adapted), with two changes: the batch paragraph names
  the scans and the TeX by file name only (no local paths go to the APIs), and the sentence about the page's first
  comment line describes the overlaps of the automatic cut instead of the hand cut's shared lines. `python -I
  sga4_full_pass.py prompt KEY` prints any batch's prompt; for batch V 41-45 it differs from
  `../run_4/api_compare/prompts/api_prompt_041_045.txt` only in those two places.
- **Money**: one Anthropic batch at a time, each with a worst case (input estimate at 2,000 tokens per image, plus
  requests × output cap) under 45 % of the credit assumed left (start: $90 for account B); request bodies under
  190 MB. OpenAI: the pilot (8 requests) and one group of 50, each sent together and awaited together; then, because
  one slow Flex request held up a whole group for half an hour, a rolling set of at most 40 requests in flight
  (`run-sol-window`), the worst case of those in flight under 45 % of the credit assumed left ($120 assumed), logged
  in chunks of 50. Flex turned many requests away as overloaded (`server_is_overloaded`; no tokens billed); they were
  sent again after a minute, at most three times, and 26 still failed. Five requests stayed `queued` at Flex for two to
  three hours (submitted 10:26-11:23 UTC) while later ones were answered, and kept the first rolling run open until
  they were cancelled at 13:38 UTC (a queued request bills nothing); the run then closed its chunks itself
  (`run_sol_window.log`). The 31 unanswered requests were sent again (`run_sol_window_2.log`, 13:40-14:39 UTC) with up
  to six tries, the wait doubling from one minute to fifteen, and a request still queued after 40 minutes cancelled and
  sent again (`--max-tries 6 --queued-limit 40`): 23 were answered. Flex had failed each of the last eight as
  overloaded six to nine times; they were sent once more at 18:36 UTC (`run_sol_window_3.log`; `--max-tries 20
  --retry-wait 90 --queued-limit 40 --vary-key`, the last giving each try its own `prompt_cache_key`, which is routing
  metadata only), and all eight were answered at the first try within 16 minutes. Whether the key or the hour made the
  difference is not known. Stop if a model passes 1.5 × its expected total (Opus $45, Sol $43). Every
  batch and chunk: `RUNS.jsonl` and a row `sga4-pass-<model>-NN` in
  `C:\Users\user\Documents\compute_cost_ledger\LEDGER.jsonl`.
- **Answers**: `answers/<opus|sol>/<KEY>.json` (findings), `_coordinator.md`, `_raw.txt` (Sol also `_response.json`).

## Merge (`merge_pass.py`) and application (`apply_pass.py`)

For each page, every fix is placed in the page's lines of the TeX the models saw (`pristine/diplomatic`, the corpus
copy kept by `snapshot_pristine.py` with its hashes checked; its `old` exactly once; a whitespace run may differ).
Findings about the TeX without a usable fix count as doubts. Fixes are grouped by the places they change; a group where the two models' fixes give the same TeX
(whitespace normalised) is an agreed fix. One-model groups within 80 characters of a group of the other model are
tried together, so that the same insertion anchored on different words still counts as agreement.

| Category | What | Goes to |
|---|---|---|
| agreed_fix | both models, same effect | applied (`AGREED_FIXES.json`) |
| agreed_fix_held | agreed, but a model marks it low confidence, or calls it a misprint and still gives a fix, or it deletes text in lines the neighbouring page may hold or in the first or last three lines of the page, or it inserts text that the neighbouring page's TeX already has, or more than 300 characters, or it changes lines the edition has commented out, or it changes the editors' apparatus (a `\sisi` correction, a note, a label, a cross-reference or a citation: the editors' record, not removed or retargeted on the models' word) | in-app check |
| conflict | both changed the place differently, or one fixes what the other calls a misprint of the print | in-app check |
| one_model_fix | a fix from one model only | in-app check |
| fix_unplaced | a fix whose `old` is not found once in the page | in-app check |
| doubt | a finding about the TeX (not a misprint, not the cut) without a usable fix | in-app check |
| marker | a model reports that the automatic cut gives a line to the wrong page | `CUT_REPORTS.json`; at the first or last page of a batch also the in-app check (category `cut`), since the neighbour then lies in another batch, whose checker did not have the line; inside a batch the model had both pages |
| agreed_misprint | both report the same misprint of the print (fix null) | `../MISPRINTS_4.json`, nothing applied |
| one_model_misprint | a misprint from one model only | `OPUS_ONLY_MISPRINTS.json`, `SOL_ONLY_MISPRINTS.json`; never applied |

A batch answered by one model only would go to the in-app check page by page (category `one_model_only`, with that
model's findings as leads); in the end both models answered all 327 batches. A cross-reference counts as retargeted
when its macro stays but its label changes (`merge_pass.targets`).

Each one-model misprint carries a `class` (a heuristic of `merge_pass.misprint_class`): **recorded by the editors**
(the TeX quoted already has a `\sisi` there, so the report confirms the editors' correction), **language** (spelling,
grammar, accents, punctuation of the print), or **mathematics** (the printed and the proposed readings differ in a
formula, a symbol, a number or a reference). The mathematics ones are listed apart in
`SOL_ONLY_MISPRINTS_MATHEMATICS.json` and `OPUS_ONLY_MISPRINTS_MATHEMATICS.json`: Sol's list holds the doubtful
"misprints" that correct the author's mathematics or notation (about five per 30 pages in the comparison). Nothing in
these lists is applied or sent to the app check on its own.

`apply_pass.py` builds `sga4/diplomatic` from the pristine texts with the agreed fixes (per file from the end
backwards, positions checked again, a fix found on two pages applied once) and logs them in `../FIXLOG_4.jsonl`; it
replays each on the corrected layer `sga4/current` where its `old` occurs once between the `\pageoriginale` markers
around the same page, whitespace runs free (`../FIXLOG_4_CURRENT.jsonl`; the others in `../REPLAY_MANUAL_4.json`,
"already there" where Codex's corrections had already made the change, else "by hand"), as `process_sga.py` does for
SGA 5-7. Agreed misprints go to `../MISPRINTS_4.json`. Because it starts from the pristine texts, it can run again
after more answers come in; it writes a working-copy file only if the file is still pristine or exactly as it wrote
it last time (`APPLY_STATE.json`), so hand edits made afterwards stop it instead of being lost. `compile_check.py`
compiles every exposé standalone with LuaLaTeX, two runs, before and after (`COMPILE_*.json`; output outside the
working copy).

## Results (final, `SUMMARY.json`)

| | |
|---|---|
| Pages checked | 1,557 (tome 1: 516, tome 2: 406, tome 3: 635) in 327 batches, every page by both models |
| Agreed fixes applied | 898 on 589 pages, to `sga4/diplomatic` (`../FIXLOG_4.jsonl`); by kind: word 361, symbol 168, formula 145, missing 53, formula/symbol 41, extra 29, punctuation 22, number 16, accent 15, other 48. Five write ∅ for the models' `\emptyset` (noted in the log) |
| Corrected layer | 774 replayed on `sga4/current` (`../FIXLOG_4_CURRENT.jsonl`); 68 already there; 56 to replay by hand (`../REPLAY_MANUAL_4.json`) |
| In-app check | 443 pages, 643 items (`PAGES_FOR_APP_CHECK.json`): 347 one-model fixes, 154 conflicts, 84 lines at a cut between batches, 50 held agreed fixes (29 low confidence, 18 the editors' apparatus, 5 a deletion at the page's edge; a fix can have two reasons), 4 doubts, 4 fixes not placed |
| Misprints of the print | 930 reported by both (`../MISPRINTS_4.json`); one model only: Opus 258, Sol 1,343 |
| One-model misprints by class | Opus: mathematics 140, language 99, recorded by the editors 19; Sol: mathematics 754, language 202, recorded by the editors 387. The mathematics ones (`*_ONLY_MISPRINTS_MATHEMATICS.json`) are the doubtful kind; none is applied |
| Page cut | 172 reports (`CUT_REPORTS.json`); the 84 at a batch's first or last page are in the in-app check |
| Compile | both layers, every exposé: exit code, errors and undefined references as before (`COMPILE_after.json`, `COMPILE_current_after.json` against the `_before` files); 914 pages, 912 before (IV and VI one page longer) |
| Spot check | 8 agreed fixes picked at random and checked on the strips by the coordinating Claude Opus 5.5 subagent: all 8 right |
| Cost | Opus $44.66 (14.04 M input, 1.66 M output tokens; $0.029 a page), Sol $47.14 (12.30 M, 6.97 M; $0.031 a page), 1,527 pages sent; with the comparison's six batches $45.49 and $47.94. Ledger rows `sga4-pass-opus-01`…`09`, `sga4-pass-sol-01`, `02`, `04`…`11` (`sol` 3 was abandoned before any request: a KeyError in the runner, nothing billed) |

Applied fixes and pages, by exposé (fixes/pages): I 74/217, II 31/45, III 19/33, IV 98/221, V 118/81, V bis 62/79,
VI 209/176, VII 27/24, VIII 45/46, IX 19/42, X 2/21, XI 2/15, XII 22/53, XIII 9/13, XIV 3/23, XV 9/38, XVI 10/43,
XVII 65/229, XVIII 43/107, XIX 31/51. Pages in the in-app check, by exposé: I 41, II 14, III 7, IV 87, V 32, V bis 40,
VI 58, VII 5, VIII 12, IX 9, X 7, XI 10, XII 17, XIII 6, XIV 1, XV 10, XVI 8, XVII 32, XVIII 35, XIX 12.

`apply_pass.py` reports one fix applied per agreed fix and none refused; the working copy and the logs were rebuilt
from the pristine texts after the last answers came in (19:00 UTC), so they hold exactly the 898 fixes above.

## Needs a decision

1. **The in-app check**: 443 pages (`PAGES_FOR_APP_CHECK.json`). By what brings each page there (a page can have
   several): a one-model fix 271, a conflict 132, a cut between batches 57, a held agreed fix 46, a doubt 4, a fix
   not placed 4. 216 pages are there for one-model fixes alone. The `cut` items name one or two lines at a page break
   between two batches; the doubts are four places a model flagged without a fix.
2. **The page counter of Exposés II and III** (`../GLOBAL_ISSUES_SGA.md` item 90): two `\setcounter` lines, both
   layers.
3. **Printed text the edition comments out** (item 91): V bis p. 138 (« Changement Yves ») and I p. 34.
4. **`\phi` for the printed ∅** (item 92): agreed and applied at I p. 62, IV p. 452, VI p. 224, XII p. 120, XIII
   pp. 132 and 142; one model only or in conflict (in the in-app check) at II p. 243, IV pp. 313, 314, 402, 404, 418,
   422, 423, 456, 461, 474-476, XII p. 112. One pass over the volume, case by case.
5. **Conventions** (item 93): π/Π in I §§ 8-9, \mathsf{e} for the champ's script C in V pp. 65-80, the « IV » of
   Exposé IV's own references, \eqhyperref's parentheses.
6. **The editors' apparatus** (item 95): 18 agreed fixes held: five would remove an editors' `\sisi` where the scans
   already read the correction (IV p. 429, X p. 63, XV p. 194 twice, XVII p. 446), one would change a `\sisi`'s
   record of the print together with its link (IV p. 302), twelve would remove or retarget a cross-reference or a
   citation (II pp. 238, 247; IV pp. 327, 405, 427; V p. 34; XII p. 89; XVII p. 388; XVIII pp. 498, 501, 518, 537).
7. **The corrected layer**: 56 replays by hand (`../REPLAY_MANUAL_4.json`, status "by hand"); 68 fixes the corrected
   layer already had (status "already there", nothing to do).
8. **Credit**: Anthropic account B was assumed to hold $90 at the start; this pass billed $44.66 there, so about $45
   should be left (check the Console). OpenAI: $47.14 for Sol in this pass, 10 % over the $43 expected and under the
   stop line ($64.50), from the $200 balance shared with the Dérivateurs translation.

## Files

- Scripts, in the order they run: `make_working_copy.py`, `ocr_extract.py`, `build_pages.py`, `prep_strips.py`,
  `sga4_full_pass.py` (batches, prompts, runs, comparison import, status), `snapshot_pristine.py`, `merge_pass.py`,
  `apply_pass.py`, `compile_check.py`, `summary.py` (`SUMMARY.json`: the figures below). They reuse
  `../sga4_api_compare.py` (prompt adaptation, JPEG, OpenAI loader), `../render_sga4_prompt.py` (template),
  `../sga_api_batch.py` (answer clause), `../CHECKER_PROMPT_SGA.txt` and `../NOTE_4.txt`.
- Pristine texts: `pristine/{diplomatic,current}/<NN>/<NN>.tex` (the 20 exposé files of both layers as copied from
  the corpus; hashes as in `../sga4/SOURCE.json`).
- Page table: `PAGES.json`, `PAGES_DIAG.json`; batches: `BATCHES.json`, `batches/<KEY>/page_FFF.tex`; strips:
  `strips/t<tome>/` (301 MB); OCR: `ocr/`.
- Runs: `RUNS.jsonl`, `run_*.log`; answers: `answers/opus/`, `answers/sol/`.
- Merge: `MERGED.json` (every item, per page), `AGREED_FIXES.json`, `PAGES_FOR_APP_CHECK.json`,
  `AGREED_MISPRINTS.json`, `OPUS_ONLY_MISPRINTS.json`, `SOL_ONLY_MISPRINTS.json`,
  `OPUS_ONLY_MISPRINTS_MATHEMATICS.json`, `SOL_ONLY_MISPRINTS_MATHEMATICS.json`, `CUT_REPORTS.json`,
  `COORDINATOR_NOTES.md` (what the models said beyond the counts: conventions, edits that belong together).
- Applied: `../FIXLOG_4.jsonl`, `../FIXLOG_4_CURRENT.jsonl`, `../REPLAY_MANUAL_4.json`, `../MISPRINTS_4.json`,
  `APPLY_MANUAL.json`, `APPLY_STATE.json`; compile: `COMPILE_before.json`, `COMPILE_current_before.json`,
  `COMPILE_after.json`, `COMPILE_current_after.json` (the `_partial` files are runs on a provisional application
  before the last answers; the first of them found the undefined `\emptyset`).
- For the in-app check: each entry of `PAGES_FOR_APP_CHECK.json` names the page (tome, Springer page, exposé), its
  batch, its lines in the TeX the models saw (`tex_lines`) and in the fixed working copy (`working_copy_lines`), the
  scan file, path and PDF page (and the witness's for XVII-XVIII), why it is there, and each model's reading (or
  "nothing reported here"). The page's TeX and strips as the models saw them: `batches/<KEY>/page_FFF.tex`,
  `strips/t<tome>/pFFF_s1..4.png` (`_w1..4` for the witness). The fixes applied on the page are in
  `../FIXLOG_4.jsonl`, so the check starts from the current working copy.
