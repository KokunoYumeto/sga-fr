# SGA 7 I and II: six readers, French and English, each in three forms

You are GPT-6 Astra in ChatGPT Pro mode, with a Python and LaTeX environment. Three ZIP files are attached. Each has
`MANIFEST.tsv` at its root (path in the zip, original path, bytes, SHA-256, role); read the manifests first.

## What this is for

SGA 7 (*Groupes de monodromie en géométrie algébrique*), Volume I (Grothendieck, with M. Raynaud and D. S. Rim;
LNM 288, Exposés I, II and VI–IX) and Volume II (P. Deligne and N. Katz; LNM 340, Exposés X–XXII), has been
transcribed into LaTeX, checked page by page against the scans, and translated into English. The checking produced
two French layers (diplomatic and corrected), fix logs, a register of the misprints of the print, and a port of the
corrections into the English. All of that is attached. What is missing is the readers: finished books, one per form
and language, that carry every fix and say exactly what was changed. You build them, by script and diff. The text is
far too long to read whole, so work from the records, and look at the text wherever a decision needs it.

## The six readers

Build one book per form and language, each containing both volumes (Part I = SGA 7 I, Part II = SGA 7 II), each a
single LaTeX file that compiles with a standard TeX Live:

| File | Language | Form |
|---|---|---|
| `SGA7_FR_diplomatique.tex` | French | **Diplomatic**: the text exactly as printed, misprints kept, with the page of the print marked at every page break |
| `SGA7_FR_corrige_apparat.tex` | French | **Corrected, with apparatus**: misprints corrected; every place where it differs from the print is marked, and the apparatus gives the printed reading, the correction and its source |
| `SGA7_FR_texte_de_lecture.tex` | French | **Plain reading text**: the corrected text with no apparatus at all; the printed page numbers in the margin only; a short preface says what was left out |
| `SGA7_EN_diplomatic.tex` | English | **Diplomatic**: the English that follows the print, where a misprint changes the English its printed reading is kept, and the print's page breaks are marked |
| `SGA7_EN_corrected_apparatus.tex` | English | **Corrected, with apparatus**: as for the French |
| `SGA7_EN_reading.tex` | English | **Plain reading text**: as for the French |

**Build all three forms of a language from one annotated master.** Mark every place where the print and the
corrected text differ, for instance with a macro `\var{printed reading}{corrected reading}{source id}`, and generate
the three forms from that master by switching the macro. The forms then cannot drift apart. A misprint that does not
change the English (a French spelling, for example) gets no variant in the English.

Exposé VI of Volume I is printed in English. It stays in English in both readers, and the three forms apply to it as
to the rest.

## Sources of record

- **French:** in ZIP 1, `fr/sga7i/{diplomatic,current}/` and `fr/sga7ii/{diplomatic,current}/`. `diplomatic` is the
  layer as printed; `current` is the corrected layer. Each page begins with a marker
  `%%%%%%%%%%  scan idx N  |  folio F  %%%%%%%%%%`. Volume I has folios 1–528 (I 1–24, II 25–31, VI 32–132, VII 133–217,
  VIII 218–312, IX 313–528; the publisher's catalogue is pp. 525–528). Volume II has folios 1–438 (X 1–38 … XXII 401–438).
  `fr/sga7ii/corrections.md` holds the corrected-layer records and `source_defects.md` the defects of the source.
- **The French before the scan check:** ZIP 3 (August 2026). It is the "before" side of the change logs only.
- **English:** ZIP 2, `en/sources/native/SGA7I/` (master and 188 components) and `en/sources/native/SGA7II/` (master
  and 183 components), the sga-en repository at commit 4a4cbac, release `v2026-11-12-english-edition`. The released
  single-file readers are in `en/release_v2026-11-12/`, and the repository records in `en/repo/`. The English has no
  page markers. Align it with the French by exposé, section and paragraph numbers, as the port did (`port/segment.py`),
  and add the folio of the print at each section start and wherever the alignment allows.
- **Fixes and their status** (ZIP 1 `fixes/`):
  - `FIXLOG_7I.jsonl` (719, diplomatic) and `FIXLOG_7I_CURRENT.jsonl` (1,036, corrected) are all applied.
  - `FIXLOG_7II.jsonl` (773) and `FIXLOG_7II_CURRENT.jsonl` (906) are all applied.
  - `MISPRINTS_7I.json` (1,147) and `MISPRINTS_7II.json` (1,132) are the registers of the misprints of the print, with
    the decision taken on each (applied in the corrected layer, already right, or kept as printed).
  - The replay records `REPLAY_MANUAL_7I/7II` and their `_DONE` files.
  - The port of the corrections into the English is in ZIP 2 `port/` (`PORT_EN7I_LOG.jsonl`, `PORT_EN7II_LOG.jsonl`,
    the decisions files, `METHODOLOGY.md`).
- **Conventions** (ZIP 1 `conventions/`): `GLOBAL_ISSUES_SGA.md` (the decisions taken once for the edition; items
  1–79 concern SGA 7), `NOTE_7I.txt`, `NOTE_7II.txt` and `CHECKER_PROMPT_SGA.txt`. The Codex corpus's `policy.md` files
  define the two layers.

## Rules

1. **Keep the author's notation and language** in every form. Correct a misprint only where it is a misprint of the
   print, recorded in the registers, or decided by you below with a reason. Never standardize notation silently. You
   may write one consistent macro set, but it must not change what prints.
2. **The English terms and notation** are those of the released English. No SGA glossary exists yet, so write one:
   `GLOSSARY_SGA7_FR_EN.tsv` (French term or notation, English rendering, count, first place). List every French term
   rendered in more than one way in `GLOSSARY_INCONSISTENCIES.md`. Make the English consistent only where the
   variation is plainly a slip, and record each change in the English change log.
3. **Decide the open items**, each with a reason, in `OPEN_ITEMS_DECIDED.tsv` (item, page, the readings, your
   decision, the reason, the form or forms affected). You have no scans: where only the scan could decide, keep the
   printed reading, put both readings in the apparatus, and mark the item "needs the scan". The open items are:
   - the 7 I MANUAL item of pp. 331–335 (`MANUAL_7I_findings_331_335.json`, kind `extra`, "old occurs 0 times");
   - misprints 7I:356 (p. 179; its old text occurs twice on the page) and 7II:627 and 7II:1018 (p. 353, "unclear");
   - the English "unclear" port items en7I C82, C713 and C874, and en7II C8, C17, C138, C475 and C508;
   - in Exposé XV Cor. 1.3.2 (i), the English underlines "$S$-" where the French does not;
   - the items of `GLOBAL_ISSUES_SGA.md` marked low confidence or "to review before the corrected edition" that
     concern SGA 7.
4. **Front matter.** The SGA 7 II layers start at Exposé X, and Volume I has no separate table of contents. Build the
   tables of contents from the text, and list the printed front matter that is not transcribed as missing in the
   README. Do not invent it.
5. **Credit and rights.** Each reader's front matter carries:
   - the authors and the volume's bibliographic data;
   - the credits and provenance exactly as the records give them (`en/repo/README.md`, `ATTRIBUTION`,
     `SOURCE_AUTHORITY.md`, `INHERITED_ENGLISH_PROVENANCE_AND_ADVERSE_USE.md`, the Codex corpus README). Keep every
     human contribution they name;
   - the wording "AI-transcribed", "AI-translated" and "AI-produced corrections", never "AI-assisted";
   - this rights statement, in the reader's language: "The rights in the original work belong to its author or the
     author's representatives or heirs. Where we hold rights, in the AI-produced transcription, translation,
     corrections and typesetting, they are dedicated to the public domain under CC0 1.0. This edition is published for
     educational, non-profit purposes, and we claim no rights we do not hold. If you hold rights in this work and
     object to its publication here, please open a GitHub issue and we will take it down."

   Credit this build to GPT-6 Astra (OpenAI, ChatGPT Pro mode).
6. **Privacy.** Some records contain local file paths with a personal name. Never copy a local path into a reader
   or a log; refer to files by their path inside the ZIP. Copy no e-mail address.

## What to deliver

Deliver one ZIP per language and one for the records, named `SGA7_READERS_FR.zip`, `SGA7_READERS_EN.zip` and
`SGA7_READERS_RECORDS.zip`:

- the six reader `.tex` files and the annotated masters, with their PDFs if they compile (leave a PDF out only if
  the ZIP would exceed about 100 MB, and say so);
- `CHANGES_FR.tsv`: every difference between the corrected French reader and the August 2026 baseline (ZIP 3) and
  between it and the current layer. Columns: page, place, before, after, source (fix id, misprint id, or your
  decision id);
- `CHANGES_EN.tsv`: every difference between the corrected English reader and the released English;
- `APPARATUS_COUNTS.md`: per exposé and form, the number of apparatus entries by kind;
- `GLOSSARY_SGA7_FR_EN.tsv`, `GLOSSARY_INCONSISTENCIES.md` and `OPEN_ITEMS_DECIDED.tsv`;
- `README.md`: what each file is, how each form was made, the counts, what is missing and why, and the compile
  status of each reader with its LaTeX errors and warnings;
- your build scripts, with their outputs.

## When it is done

**Each item is done when:**
- **A reader** compiles without errors; it carries every applied fix (check this by script against the fix logs and
  report the counts); and its page markers agree with the folios of the French layers.
- **The apparatus** has one entry for each difference between the diplomatic and the corrected forms, and none for
  anything else.
- **Each open item** has a decision and a reason.

**Not acceptable:**
- a reader that drops, summarizes or paraphrases any part of the text;
- a fix applied in one form and missing from another;
- an apparatus entry without a source;
- a silent change of notation;
- a decision without a reason;
- local paths or e-mail addresses in any output.

**The task is finished** when all six readers, the change logs, the glossary, the decisions and the README are in
the three ZIPs.

## Working method

- Start from the manifests, then the fix logs and the misprint registers. Build the annotated masters by script,
  generate the forms, compile, and check the counts.
- After each finished reader, save a checkpoint ZIP of everything so far to the user's Library, or wherever files
  survive the loss of the execution environment, named `SGA7_READERS_checkpoint_<n>.zip`. Save the final ZIPs there
  too.
- This task is long by design. Work through it completely; do not stop at an outline, a sample or a plan, and do not
  ask whether to continue. Ignore any clock. Write the files from the start and extend them as you go, so that an
  interruption loses little.

## If the execution environment fails

If the workspace disconnects or an attached ZIP cannot be opened, wait and retry for at least ten minutes. If it does
not come back, write the work out in the chat as text:
- the decisions table, the glossary, the README and the change logs so far, each in full in its own code block
  headed by its file name;
- your build scripts in full, so that the readers can be rebuilt from the attached sources;
- which readers were finished and where their checkpoints are.

An answer that only reports the failure or asks for the files again is not acceptable.
