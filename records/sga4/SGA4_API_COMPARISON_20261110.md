# SGA 4: checking the LaTeX against the scans over the API, compared with the in-app subagents (10 November 2026)

## Result

The reference is the in-app subagent check of 30 printed pages: 26 transcription errors (TE) and 33 misprints of the
print (MP). Among the API runs' extras, three are real and the subagents missed them: one TE and two MP. Recall is
counted against the reference.

| Configuration | TE recall (of 26) | MP recall (of 33) | Extras: real / false / doubtful | `\phi` convention | $ per page, as billed | All of SGA 4 (1,609 pp.) | Wall time |
|---|---|---|---|---|---|---|---|
| Subagents: Claude Opus 5.5, effort max, with tools (reference) | 26 | 33 | (reference) | yes | $0.388 (API-equivalent, list price) | $625 | 10.7 min (six in parallel) |
| Claude Fable 5.2, effort medium, Message Batches | 23 | 25 | 4: 2 / 2 / 0 | no | $0.062 | $100 | 2.8 min |
| Claude Opus 5.5, effort high, Message Batches | 23 | 20 | 2: 1 / 1 / 0 | no | $0.028 | $44 | 2.5 min |
| GPT-6.1 Sol, high, Flex | 23 (+1 place found) | 22 (+1 place found) | 9: 3 / 1 / 5 | yes, both | $0.015 | $23 | 5.4 min |
| GPT-6.1 Sol, max, Flex | 25 | 22 (+1 place found) | 9: 3 / 1 / 5 | yes, both | $0.027 | $43 | 11.1 min |

- At list price the API runs cost twice the billed figure: $0.124, $0.055, $0.029 and $0.053 per page.
- In every run, each fix's `old` occurs exactly once on its page, so each fix applies as written.
- "Place found" means the right spot with the wrong treatment: a misprint written into the TeX as a fix, or a TeX error
  reported as a misprint.
- `\phi` column: whether the run caught Exposé IV's `\phi` for the empty set on pp. 402 and 404.

Combined routes (union of the findings), against the full set of 27 TE and 35 MP (the reference plus the three real
extras):

| Route | TE (of 27) | MP (of 35) | $ per page | All of SGA 4 |
|---|---|---|---|---|
| Subagents (reference) | 26 | 33 | $0.388 (list) | $625 |
| Claude Fable 5.2 medium | 23 | 27 | $0.062 | $100 |
| Claude Opus 5.5 high | 24 | 20 | $0.028 | $44 |
| GPT-6.1 Sol high | 24 | 24 | $0.015 | $23 |
| GPT-6.1 Sol max | 26 | 24 | $0.027 | $43 |
| Opus 5.5 high + Sol high | 26 | 27 | $0.042 | $68 |
| **Opus 5.5 high + Sol max** | **27** | **28** | **$0.054** | **$87** |
| Fable 5.2 medium + Sol high | 26 | 29 | $0.077 | $123 |
| Fable 5.2 medium + Sol max | 27 | 29 | $0.089 | $143 |
| All four | 27 | 29 | $0.131 | $211 |

## Recommendation

- **Best fixes per dollar: GPT-6.1 Sol.** At max it found 25 of the 26 reference errors, plus the error the subagents
  missed, for $0.027 per page. At high it found 23 for $0.015. Claude Opus 5.5 high found as many errors as Claude
  Fable 5.2 medium (23) for less than half the price.
- **A cheap pass plus a cheap second opinion beats one expensive pass.** Claude Opus 5.5 high plus GPT-6.1 Sol max
  found all 27 transcription errors (the subagents 26) and 28 of 35 misprints, for $0.054 per page as billed. That is
  about $87 for all of SGA 4 and minutes per batch. The subagent path costs $0.388 per page API-equivalent, seven times
  the pair at billed price and 3.6 times at list price. The single most expensive API pass, Fable 5.2 medium, found fewer
  errors (23) at a higher price ($0.062).
- **Misprints are where the subagents stay ahead.** No API route reaches their 33 of 35; the best reach 29. Six
  misprints escaped all four API runs:
  - the ± for + (p. 41);
  - a comma for a semicolon (p. 43);
  - a stray parenthesis (p. 44);
  - a stray full stop (p. 388);
  - "ambiguité" (p. 390);
  - the tautology Fib(C) ≊ Fib(C) (p. 401).

  Five of these are marks a crop resolves. For correcting SGA 4's LaTeX, run Opus 5.5 high plus Sol max over the API. Keep
  the subagents where the misprint record matters.
- **Review cost of Sol.** Each Sol run adds about five doubtful "misprints" per 30 pages. These are corrections of the
  author's mathematics or notation, all with fix null, so they never touch the TeX but have to be read and dropped. Each
  Sol run also read the plain H of p. 42 as underlined and proposed writing the sheaf ℋ into the TeX.

## What the API results suggest for a subagent of the same model

The six subagent runs (Claude Opus 5.5, effort max, 180 turns) used:
- 279,888 output tokens: $5.60;
- 12.86 million cache-read tokens: $2.57;
- 0.70 million cache-write tokens: $3.48.

That is $11.65 in all, $0.388 per page. The cache part ($6.05) is the re-reading of the growing context of strips and
crops at every turn: it depends on the number of turns and images, not on the effort. The output part depends on model
and effort. The projection below assumes the same turns and images and prices the cache part at each model's prices.
The output part lies between that model's API output on these pages (lower bound) and the reference's 279,888 tokens
(upper bound). Fable 5.2's cache writes cost $10 per million against Opus 5.5's $5.

Expected recall with zoom (estimates):
- The API runs miss fine marks and look-ups. Opus 5.5 high over the API missed 3 TE and 13 MP that the same model found
  as a subagent at max.
- Of those 13 MP, nine are small marks a crop resolves: four missing closing parentheses, the stray commas, the stray
  full stop, the missing diaeresis, the ±, the stray parenthesis.
- Two of the 3 TE are the `\phi` pair, which a subagent settles by looking up macros.tex, as the reference did.
- Fable 5.2 medium misses the same kinds of marks, while having the best misprint recall over the API (27 of 35).

| Subagent of | Expected TE (of 27) | Expected MP (of 35) | $ per page (API-equivalent, list) | All of SGA 4 |
|---|---|---|---|---|
| Claude Opus 5.5, max (measured: the reference) | 26 | 33 | $0.39 | $625 |
| Claude Opus 5.5, high | 25-26 | 30-33 | $0.22-0.39 | $350-625 |
| Claude Fable 5.2, medium | 25-27 | 31-34 | $0.37-0.69 | $600-1,110 |

Cheapest route to the reference's recall:
- **Transcription errors** (what the LaTeX fix needs): Claude Opus 5.5 high plus GPT-6.1 Sol max over the API, $0.054
  per page, about $87 for SGA 4. Sol max alone ($0.027, $43) matches the subagents' count of 26, as a slightly different
  set: it misses one comma and finds the double prime.
- **Misprints as well:** no API route measured reaches it. The cheapest route expected to is an Opus 5.5 subagent:
  measured at max, $0.39 per page API-equivalent, paid in plan usage on the subscription. At high, the estimate is
  $0.22-0.39 per page; it was not measured. A Fable 5.2 subagent would cost more than Opus at max for about the same
  recall.

On the SGA 7 typescripts (9 Nov), Opus 5.5 at max over the API found about half of the subagents' errors. On these
clean SGA 4 pages, Opus 5.5 at high found 88% of their transcription errors and 61% of their misprints. The gap is now
in the fine marks.

## 1. What was compared

- **Pages.** The six batches of the SGA 4 spot check (run_4), five printed pages each, 30 pages: Exposé V pp. 41-45
  (Tome 2), X pp. 51-55 (Tome 3), I pp. 101-105 (Tome 1), XVII pp. 361-365 (Tome 3, with the second witness scan),
  VIII pp. 386-390 (Tome 2), IV pp. 401-405 (Tome 1). The TeX is Fabrice Orgogozo's LaTeX edition of SGA 4 in the
  corpus copy (hashes in `run_4/PREP_MANIFEST.json`). The scans are 300 dpi, each page cut into four strips of
  1,450-1,720 × 700-750 pixels.
- **Reference.** Six Claude Opus 5.5 subagents in the app (sga-checker, session default effort, 10 Nov), each with the
  Read tool, crops of the strips and look-ups in the corpus (source file, macros.tex): 26 transcription errors with a fix
  and 33 misprints of the print (`run_4/findings_*.json`). Two of the 26 fixes are the one convention of the pages:
  Exposé IV writes `\phi` for the empty set (pp. 402 and 404).
- **API runs.** The same inputs (each page's TeX and its four strips; for Exposé XVII also the four witness strips)
  and the same checker prompt, one request per batch, six requests per configuration, run one after the other:
  1. Claude Fable 5.2 (`claude-fable-5-2`), effort medium, Message Batches API;
  2. Claude Opus 5.5 (`claude-opus-5-5`), effort high, Message Batches API;
  3. GPT-6.1 Sol (OpenAI API), reasoning effort high, Flex tier;
  4. GPT-6.1 Sol, reasoning effort max, Flex tier. The API lists the accepted values as none, minimal, low, medium,
     high, xhigh and max, so max is the highest.

  Output cap 128,000 tokens per request. Strips sent as greyscale JPEG (quality 90) at full resolution, as
  `sga_api_batch.py` sends them; Claude takes them without downscaling (high-resolution limit 2,576 pixels), and GPT-6.1
  Sol gets them with detail "high". Anthropic key: account B (the $200 key, `Untitled 1939.md`), passed by
  `run_with_note_key.py` with KEY_NOTE. The wrapper's default note is account F, which had about $2 left on 9 Nov, too
  little for a $16 worst case. OpenAI key: the loader of the misprint pass (`enr_pilot.key()`). Budget: $30 in all; before
  each run, the cost of the earlier runs plus the new run's worst case (counted input + 6 × 128,000 output tokens) was
  checked against it.

## 2. The prompt for the API

The API prompt is the subagent prompt `run_4/prompt_FFF_LLL.txt` (identical to what `render_sga4_prompt.py` renders),
changed only where it speaks of tools, in the way `sga_api_batch.py` changes it for SGA 7:
`sga4_api_compare.py prompts` writes the six prompts to `run_4/api_compare/prompts/` and checks that each tool passage
occurs exactly once and that no tool wording is left. The changes:
- the Folder line is dropped; "page_NNN_s1.png ... page_NNN_s4.png" becomes "Four images", and the Read-tool and crop
  sentences become `sga_api_batch.py`'s "They are attached below, in order, at the scan's full resolution; they are sharp
  enough for subscripts, primes and accents." The template's newer sentence on reading a page's TeX and strips in one
  message with five Read calls becomes "Work page by page: take a page's TeX and its four strips together before you
  compare.";
- "page_NNN.tex" becomes "Its TeX" or "the page's TeX". The TeX comes in the message, page by page, as in
  `sga_api_batch.py`: "Page N. Its TeX: ```latex ...``` Its scan, four strips, top to bottom:" and the four images;
- XVII: the witness strips follow the main strips, and "read the witness strip before deciding; do not read the witness
  strips otherwise" becomes "look at the witness strip before deciding; otherwise go by the main strips";
- what a subagent could look up is marked as not attached: the source file ("labels, \bibitem entries and the
  neighbouring pages cannot be looked up") and macros.tex;
- the output: `sga_api_batch.py`'s answer clause (one JSON object, findings and the coordinator message) replaces "Write
  JSON to ...". "Do not edit any .tex file" goes with it.

Side finding: `sga_api_batch.py` itself can no longer render its SGA 5-7 API prompt. Its TOOL_SENTENCE assertion fails on
the current `CHECKER_PROMPT_SGA.txt`, because the template has since gained the "Work page by page ..." sentence inside
that passage.

## 3. How the answers were scored

- **Transcription errors (26).** A configuration's finding matches when its fix has the same effect on the page's TeX
  (both edits applied, whitespace normalised), or makes the same correction in other LaTeX (checked by hand,
  `run_4/api_compare/ADJUDICATION.json`). A finding at the right place with a different correction, or one that reports
  the place as a misprint without a fix, counts as "place found" but not as recalled.
- **Misprints of the print (33).** A finding matches when it reports the same misprint at the same place (by hand,
  candidates proposed by the position of the quoted TeX). A misprint reported as a transcription error with a fix that
  would write the misprint into the TeX counts as "place found" only.
- **Extras.** Every finding that matches no reference item, checked against the scan strips: *real* (an error that the
  subagent missed), *false* (no such difference, a difference the prompt excludes, or a wrong reading), *doubtful*.
  At most 15 extras per configuration were checked, in a random sample where there were more.
- **Cost.** Billed price of each run: batch price on Anthropic (Fable 5.2 $4/$20, Opus 5.5 $2/$10 per million input/
  output tokens) and Flex price on OpenAI (GPT-6.1 Sol $1/$5), from the usage of each answer. The subagent path's cost is
  its API-equivalent cost at list price, from the six transcripts (`api_equivalent_cost.py`; `claude_tokens.py` does not
  exist). Extrapolation: SGA 4 Tomes 1-3, 541 + 423 + 645 = 1,609 printed pages.

## 4. Per-batch detail

TE / MP found, against the reference's count on each batch:

| Batch | Reference | Fable 5.2 medium | Opus 5.5 high | Sol high | Sol max |
|---|---|---|---|---|---|
| V, pp. 41-45 | 13 / 11 | 12 / 8 | 12 / 4 | 12 / 6 | 13 / 7 |
| X, pp. 51-55 | 0 / 0 | 0 / 0 (1 false extra) | 0 / 0 | 0 / 0 (1 doubtful) | 0 / 0 (1 doubtful) |
| I, pp. 101-105 | 4 / 6 | 4 / 6 | 4 / 5 | 2 / 5 | 3 / 5 |
| XVII, pp. 361-365 | 2 / 5 | 2 / 3 | 2 / 4 | 2 / 5 | 2 / 5 |
| VIII, pp. 386-390 | 4 / 5 | 4 / 3 | 4 / 2 | 4 / 3 | 4 / 3 |
| IV, pp. 401-405 | 3 / 6 | 1 / 5 | 1 / 5 | 3 / 3 | 3 / 2 |

Missed reference items (ids `p<page>.<n>` in reference order, `sga4_api_score.py reference`):
- Fable 5.2 medium: TE p42.2 (the arrows with a tilde in Prop. 6.7) and the `\phi` pair p402.1, p404.3. MP p41.2,
  p43.7, p44.4, p362.2, p363.1, p388.3, p390.3, p401.2.
- Opus 5.5 high: TE as Fable. MP p41.2, p42.4, p43.5, p43.6, p43.7, p44.4, p44.5, p101.2, p362.1, p387.1, p388.3, p390.3,
  p401.2.
- Sol high: TE p42.2 and p102.1 (the comma after "cofinal"). It found p104.1's "du ind-objet" but reported it as a
  misprint (fix null). MP p41.2, p43.7, p44.4, p44.5, p101.2, p388.3, p390.3, p401.2, p404.1, p404.2. It reported p42.3 as
  a fix (place found).
- Sol max: TE p102.1. MP p41.2, p43.7, p44.4, p101.2, p388.3, p390.3, p401.2, p401.4, p404.1, p404.2. It reported p42.3 as
  a fix (place found).

## 5. Extras

All extras were adjudicated: no configuration had more than 15, so no sampling was needed. Verdicts are in
`ADJUDICATION.json`.
- **Real, missed by the subagents (3):**
  1. p. 44, (6.9.2): the TeX's ``` ``E^{p,q}_2 ``` prints two opening quotes in math mode, where the print has a double
     prime (strip 1). A transcription error, found by Opus 5.5 high, Sol high and Sol max.
  2. p. 44: "suite exacte analogue par les groupes Ext" for "pour" (strip 4; the proof below has "pour"). A misprint of
     the print; the TeX keeps "par". Found by Fable 5.2, Sol high and Sol max.
  3. p. 404: "algébriquements clos" (strip 1). A misprint; the TeX silently corrects it. Found by Fable 5.2, Sol high and
     Sol max.
- **False (5):**
  - Fable p. 52: parentheses around a formula reference (style).
  - Fable and Opus p. 104: "(F 1)" against "F 1)", the typography of labels.
  - Sol high p. 44: "exacre" (the print reads "exacte").
  - Sol max p. 401: `\sheaf{\mathcal{U}}`, which prints the same script U (macros.tex: `\def\sheaf#1{\protect\mathcal{#1}}`).
- **Doubtful (Sol, all fix null):**
  - p. 42: "acyclique pour H^0_Z(X;M)";
  - p. 55: F_x for (F_i)_x;
  - p. 389: f_* for (f_i)_*;
  - p. 390: the topos X_ét without its tilde;
  - p. 401: I' for P(I');
  - Sol max also p. 403, "𝒰-petite".

  Each changes the author's notation or statement; none is a misprint that the page itself settles.

## 6. Cost and tokens

| Run | Input tokens | Output tokens (thinking included) | Billed | List price | Worst case checked / spent before |
|---|---|---|---|---|---|
| Claude Fable 5.2 medium | 260,186 | 41,058 | $1.86 | $3.72 | $16.40 / $0.00 |
| Claude Opus 5.5 high | 260,186 | 30,573 | $0.83 | $1.65 | $8.20 / $1.86 |
| GPT-6.1 Sol high | 227,554 | 41,799 | $0.44 | $0.87 | $4.23 / $2.69 |
| GPT-6.1 Sol max | 227,554 | 114,681 | $0.80 | $1.60 | $4.23 / $3.12 |
| Subagents (6 runs, effort max) | 380 + 12,855,520 cache read + 696,602 cache write | 279,888 | (plan) | $11.65 | |

- The API runs cost $3.93 in all, against the $30 budget. The input token counts are counted (Anthropic count_tokens) or
  reported (OpenAI).
- Anthropic batch ids: msgbatch_01M66zWTQC5mG7jRdh2EDzp4 (Fable 5.2) and msgbatch_01BwVZ75LzXqxUTtTV2oeNhw (Opus 5.5).
  The OpenAI response ids are in `run_4/api_compare/<config>/findings_*_response.json`. Every OpenAI request ran at the
  Flex tier; "max" was accepted there.
- OpenAI reports nearly all input as cache-write tokens; the figures price them at the Flex input rate, as the earlier
  Sol runs did.
- Extrapolation: per-page cost × 1,609 pages. Output scales with the number of findings, so dense exposés cost somewhat
  more.

## Files

- `sga4_api_compare.py`: prompt adaptation, submission, collection and logging; `sga4_api_score.py`: matching and
  table.
- `run_4/api_compare/<config>/findings_FFF_LLL.json` (the findings list), `_coordinator.md`, `_raw.txt`;
  `run_4/api_compare/RUNS.jsonl` (each run: tokens, dollars, worst case, budget check); `run_4/api_compare/ADJUDICATION.json`
  (matches by hand and verdicts on the extras); `run_4/api_compare/prompts/` (the six API prompts).
- Ledger rows `sga4-apicmp-*` and `sga4-sub-run4` in `C:\Users\user\Documents\compute_cost_ledger\LEDGER.jsonl`.
- Nothing was applied to any TeX, corpus or SGA 5/6 file.
