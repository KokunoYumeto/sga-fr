# SGA 4: six readers, French and English, each in three forms

You are GPT-6 Astra in ChatGPT Pro mode, with a Python and LaTeX environment. Three ZIP files are attached. Each has
`MANIFEST.tsv` at its root (path in the zip, original path, bytes, SHA-256, role); read the manifests first.

## What this is for

SGA 4 (*Théorie des topos et cohomologie étale des schémas*, M. Artin, A. Grothendieck, J.-L. Verdier; LNM 269, 270,
305; 1,557 printed pages in the edition) exists in LaTeX thanks to Fabrice Orgogozo's edition. That edition was
corrected by Codex in July–September 2026 and checked page by page against the scans on 11 November 2026 by two
models, Claude Opus 5.5 and GPT-6.1 Sol. Our English translation is the repository sga-en. What is missing is the
readers: finished books, one per form and language, that carry every agreed fix and say exactly what was changed and
what is still in dispute. You build them by script and diff. Each French version is about a million tokens, so do not
read them whole: work from the records, and look at the text wherever a decision needs it.

## The six readers

Build one book per form and language, each containing all three tomes, each a single LaTeX file that compiles with a
standard TeX Live. Use the system's `amsbook.cls`; it was left out of the upload.

| File | Language | Form |
|---|---|---|
| `SGA4_FR_diplomatique.tex` | French | **Diplomatic**: as printed, misprints kept, the printed text the edition comments out restored (see rule 5), and the page of the print marked at every page break |
| `SGA4_FR_corrige_apparat.tex` | French | **Corrected, with apparatus**: misprints corrected; every place where it differs from the print is marked, and the apparatus gives the printed reading, the correction and its source |
| `SGA4_FR_texte_de_lecture.tex` | French | **Plain reading text**: the corrected text with no apparatus and no editors' notes; the printed page numbers in the margin only; a short preface says what was left out |
| `SGA4_EN_diplomatic.tex` | English | **Diplomatic**: the English that follows the print; where a misprint changes the English its printed reading is kept, and the print's page breaks are marked |
| `SGA4_EN_corrected_apparatus.tex` | English | **Corrected, with apparatus**: as for the French |
| `SGA4_EN_reading.tex` | English | **Plain reading text**: as for the French |

**Build all three forms of a language from one annotated master.** Mark every place where the print and the
corrected text differ, for instance with a macro `\var{printed reading}{corrected reading}{source id}`, and generate
the three forms from that master by switching the macro. The forms then cannot drift apart. A misprint that does not
change the English gets no variant in the English.

## Sources of record

- **French** (ZIP 1):
  - **`fr/D_diplomatic_after_scan_check/` is the diplomatic source of record**: Codex's diplomatic layer plus the 898
    fixes both models agreed on.
  - **`fr/E_corrected_after_scan_check/` is the corrected source of record**: Codex's corrected layer plus 774
    replayed fixes. Codex's corrections SGA4-CORR-0001 to 0370 stand in it as TeX comments.
  - Both are full, buildable trees (`tomes/SGA4.tex`, `tome1-3.tex`).
  - `fr/A_orgogozo_snapshot_71766d9/` (Orgogozo's untouched edition), `fr/B_…` and `fr/C_…` (the corpus before the
    scan check) are the "before" side of the change logs.
- **English** (ZIP 2): `A`, the sga-en tree `sources/native/SGA4` at commit 4a4cbac: 271 `.texfrag` fragments, each the
  translation of lines a..b of Orgogozo's 71766d9, and the main document `source/tomes/SGA4_English_translation_workpass.tex`
  (XeLaTeX). Also in ZIP 2:
  - `C`, the released single-file reader `04_SGA4_EN_COMPLETE_READER.tex` (release of 12 Nov);
  - `D`, the release build tools;
  - `F`, the port of 12 Nov: `PORT_EN4_LOG.jsonl` (all 583 port decisions), `FINAL_4.json` (the status of every
    French fix), `FRENCH_HAND_REPLAYS_4.tsv` and `HANDFIX_EN4.json`.
- **Fixes, disputes, method, conventions** (ZIP 3):
  - `fixes/`: `FIXLOG_4.jsonl`, `FIXLOG_4_CURRENT.jsonl`, `REPLAY_MANUAL_4.json` and `MISPRINTS_4.json`.
  - `api_pass_20261111/`: the scan check's records, including `PAGES_FOR_APP_CHECK.json`, `AGREED_FIXES`, the
    one-model misprint lists `OPUS_ONLY_MISPRINTS*.json` and `SOL_ONLY_MISPRINTS*.json`, `CUT_REPORTS.json`,
    `COORDINATOR_NOTES.md`, the page index `PAGES.json`, and each model's findings per batch.
  - `method/`: `GLOBAL_ISSUES_SGA.md` (items 90–95 concern SGA 4) and `NOTE_4.txt`.
  - `conventions/` and `codex_history/`.

## Decisions already taken (apply them; do not reopen them)

1. **Notation.** Keep the author's notation everywhere.
   - The diplomatic form is exactly as printed, with plain P, raised dots and labels in capitals, as GLOBAL_ISSUES
     item 89 and the NOTE files describe.
   - The corrected form corrects misprints only, with the notation as printed.
   - The English uses the notation of the French print and the terms of the released sga-en.
   - You may write one consistent macro set, but it must not change what prints.
   - No SGA glossary of ours exists. Write `GLOSSARY_SGA4_FR_EN.tsv` (French term or notation, English rendering,
     count, first place) from the existing English, and list every French term rendered in more than one way in
     `GLOSSARY_INCONSISTENCIES.md`.
   - Make the English consistent only where the variation is plainly a slip, and record each change.
2. **The 443 disputed pages** (643 items in `PAGES_FOR_APP_CHECK.json`: one-model fixes, conflicts, cuts between
   batches, held fixes, doubts, fixes not placed). You have no scans, so do not decide them. Build every form with the
   agreed text. Mark each disputed place in the apparatus of the corrected forms with both readings and the item id,
   and list them all in `DISPUTED_PLACES.tsv` (page, place, reading 1 with its model, reading 2 with its model, kind).
   A separate check against the scans will decide them.
3. **The 56 by-hand replays** (`REPLAY_MANUAL_4.json`, status "by hand"; also `FRENCH_HAND_REPLAYS_4.tsv`) are not yet
   in the corrected French: each is a fix whose old text no longer matches. Place each one in the corrected French by
   finding where it belongs, and list what you did with each in `HAND_REPLAYS_PLACED.tsv`. H39 is already settled in the
   English. Hand replays on disputed pages stay in `DISPUTED_PLACES.tsv`.
4. **Orgogozo's records (`\sisi`) and the editorial notes (N.D.E.)** are human editorial work.
   - Keep them in the diplomatic and corrected forms, marked as his, distinct from our apparatus.
   - Leave them out of the plain reading text, and say so in its preface.
   - Of the 18 held fixes that touch his apparatus (GLOBAL_ISSUES item 95), apply none to his notes. List them.
5. **Edition-level points** (GLOBAL_ISSUES items 90–91):
   - the printed text that the edition comments out (V bis p. 138, « Changement Yves »; I p. 34) appears in the
     diplomatic form;
   - the page counters of Exposés II and III follow the print.
   - Decide items 92–94 (`\phi` for ∅ at the places left; π/Π in I §§ 8–9; `\mathsf{e}` in V pp. 65–80; « IV » in the
     references of Exposé IV; the parentheses of `\eqhyperref`) by the rule "as printed in the diplomatic form,
     corrected only if it is a misprint". Record each decision.
6. **Misprints.**
   - The 930 misprints both models agree on (`MISPRINTS_4.json`) are corrected in the corrected and plain forms and
     kept in the diplomatic form, each with its apparatus entry.
   - The 1,601 misprints found by one model only (Opus 258, Sol 1,343; mathematics, language, already recorded by the
     editors): judge each one yourself. Either accept it, with a one-line reason, and treat it like the 930; or reject
     it, with a reason; or leave it in an appendix "Possible misprints, not verified", if the text alone cannot settle
     it.
   - Record every judgement in `ONE_MODEL_MISPRINTS_JUDGED.tsv` (id, model, page, reading, your verdict, reason).
7. **Not transcribed:** the exposés' summary pages (V p. 1, V bis p. 83, VI pp. 163–164, VII p. 341, VIII p. 366,
   XVI p. 206, XVII pp. 250–251) and each tome's front matter and indexes. Do not invent them. Build the tables of
   contents from the text, and list the missing pages in the README.
8. **The English corrected form** carries every French fix that changes the English. The port has applied 157 fixes
   to the English; 293 French fixes wait for the disputed pages and stay out, listed. Fix the one point the port noted
   but left unchanged: V 8.2.6 (C293, p. 78), where the English reads "to $\Ss/U$" and the corrected French reads
   "dans $\Ss/V$". Check it and record the decision.

## Credit, rights, privacy

- Each reader's front matter carries:
  - the authors and the bibliographic data of the three tomes;
  - **credit to Fabrice Orgogozo for the LaTeX edition on which every layer rests** (commit 71766d9), and to every
    other contributor named in the records (`en/repo_records/` README, ATTRIBUTION, SOURCE_AUTHORITY;
    `codex_history/`);
  - the wording "AI-transcribed", "AI-translated" and "AI-produced corrections", never "AI-assisted";
  - this rights statement, in the reader's language: "The rights in the original work belong to its author or the
    author's representatives or heirs. Where we hold rights, in the AI-produced transcription, translation,
    corrections and typesetting, they are dedicated to the public domain under CC0 1.0. This edition is published for
    educational, non-profit purposes, and we claim no rights we do not hold. If you hold rights in this work and
    object to its publication here, please open a GitHub issue and we will take it down."
- Credit this build to GPT-6 Astra (OpenAI, ChatGPT Pro mode).
- Some records contain local file paths with a personal name. Never copy a local path into a reader or a log; refer
  to files by their path inside the ZIP. Copy no e-mail address.

## What to deliver

Deliver three ZIPs: `SGA4_READERS_FR.zip`, `SGA4_READERS_EN.zip` and `SGA4_READERS_RECORDS.zip`. Together they hold:

- the six reader `.tex` files and the two annotated masters, with their PDFs if they compile (leave a PDF out only
  if a ZIP would exceed about 100 MB, and say so);
- `CHANGES_FR.tsv`: every difference between the corrected French reader and Orgogozo's 71766d9, and between it and
  the corrected source of record `E`. Columns: page, place, before, after, source (fix id, misprint id, SGA4-CORR id,
  or your decision id);
- `CHANGES_EN.tsv`: every difference between the corrected English reader and the released English;
- `DISPUTED_PLACES.tsv`, `HAND_REPLAYS_PLACED.tsv` and `ONE_MODEL_MISPRINTS_JUDGED.tsv`;
- the glossary files, and `DECISIONS.tsv` for items 92–94, the 18 held apparatus fixes and C293;
- `APPARATUS_COUNTS.md`: per exposé and form, the number of apparatus entries by kind;
- `README.md`: what each file is, how each form was made, all the counts, what is missing and why, and the compile
  status of each reader with its errors and warnings;
- your build scripts, with their outputs.

## When it is done

**Each item is done when:**
- **A reader** compiles without errors and carries every agreed fix (check this by script against the fix logs and
  report the counts). Its page markers agree with `PAGES.json`.
- **The apparatus** has one entry for each difference between the diplomatic and the corrected forms, and none for
  anything else.
- **The disputed places, hand replays and one-model misprints** each have a row.

**Not acceptable:**
- a reader that drops, summarizes or paraphrases any part of the text;
- a fix applied in one form and missing from another;
- a disputed place decided without the scan;
- an apparatus entry without a source;
- Orgogozo's notes altered or presented as ours;
- a silent change of notation;
- local paths or e-mail addresses in any output.

**The task is finished** when all six readers and every file listed above are in the three ZIPs.

## Working method

- Start from the manifests, then the fix logs, the misprint lists and the disputed-pages file. Build the annotated
  masters by script, generate the forms, compile, and check the counts.
- After each finished reader, save a checkpoint ZIP of everything so far to the user's Library, or wherever files
  survive the loss of the execution environment, named `SGA4_READERS_checkpoint_<n>.zip`. Save the final ZIPs there
  too.
- This task is long by design. Work through it completely; do not stop at an outline, a sample or a plan, and do not
  ask whether to continue. Ignore any clock. Write the files from the start and extend them as you go, so that an
  interruption loses little.

## If the execution environment fails

If the workspace disconnects or an attached ZIP cannot be opened, wait and retry for at least ten minutes. If it does
not come back, write the work out in the chat as text:
- the tables and the README so far, each in full in its own code block headed by its file name;
- your build scripts in full, so that the readers can be rebuilt from the attached sources;
- which readers were finished and where their checkpoints are.

An answer that only reports the failure or asks for the files again is not acceptable.
