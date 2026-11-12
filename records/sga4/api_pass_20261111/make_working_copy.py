"""Make the SGA 4 working copy of the scan check (sga_scan_check_20261105/sga4), as for SGA 5-7 (5 Nov):

- sga4/diplomatic: Codex's maintained French SGA 4 (corpus sga4/diplomatic) = Fabrice Orgogozo's LaTeX edition of
  SGA 4, Tomes 1-3 (snapshot at git commit 71766d9), with Codex's source-keeping edits of July-September 2026. This is
  the text the comparison of 10 Nov checked and the text the API pass checks and fixes.
- sga4/current: the corrected layer = corpus sga4/corrected_history/through_0370 (5 Sep), with 05bis/05bis.tex taken
  from the canon keeper's overlay sga4t2/c0054_20260928 (28 Sep; its parent is through_0370's 05bis, checked here).
  Transcription fixes are replayed there as process_sga.py does for SGA 5-7.

The corpus is only read. Writes sga4/SOURCE.json (paths, bytes, SHA-256 of every copied file). Refuses to overwrite an
existing working copy.

usage: python -I make_working_copy.py
"""
import hashlib
import json
import pathlib
import shutil
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
CORPUS = pathlib.Path(r"C:\Users\user\Documents\interlanguage_parts\03_projects\language_management\english_germanic"
                      r"\03_working_translations\sga_french_canonical_corpus_20260804_r1\sga4")
DIP = CORPUS / "diplomatic"
CUR = CORPUS / "corrected_history" / "through_0370"
OVERLAY = pathlib.Path(r"C:\Users\user\Documents\interlanguage_parts\00_governance\work"
                       r"\canon_keeper_successor_01a047ab_20260830\canonical_overlays\sga4t2")
OV_FILE = OVERLAY / "c0054_20260928" / "fr" / "current" / "05bis" / "05bis.tex"
OUT = W / "sga4"


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest().upper()


def tree(root):
    return {p.relative_to(root).as_posix(): {"bytes": p.stat().st_size, "sha256": sha(p)}
            for p in sorted(root.rglob("*")) if p.is_file()}


if OUT.exists():
    raise SystemExit("working copy exists: %s" % OUT)
binding = json.loads((OVERLAY / "CURRENT.json").read_text(encoding="utf-8"))
parent = binding["french"]["parent"]
assert parent["sha256"] == sha(CUR / "05bis" / "05bis.tex"), "overlay parent is not through_0370's 05bis"
assert binding["french"]["component"]["sha256"] == sha(OV_FILE), "overlay component hash differs"
shutil.copytree(DIP, OUT / "diplomatic")
shutil.copytree(CUR, OUT / "current")
shutil.copyfile(OV_FILE, OUT / "current" / "05bis" / "05bis.tex")
src = {"made": "2026-11-11", "by": "make_working_copy.py (Claude Opus 5.5)",
       "edition": "Fabrice Orgogozo's LaTeX edition of SGA 4, Tomes 1-3 (normalesup.org/~forgogozo/SGA4), snapshot at "
                  "git commit 71766d9 (archive SGA4-HEAD-71766d9.tar.gz, SHA-256 DA2D939D...C7DC), as maintained in "
                  "Codex's French SGA corpus (source-keeping edits of July-September 2026)",
       "diplomatic_from": str(DIP), "current_from": str(CUR), "current_05bis_from": str(OV_FILE),
       "diplomatic": tree(OUT / "diplomatic"), "current": tree(OUT / "current")}
(OUT / "SOURCE.json").write_text(json.dumps(src, ensure_ascii=False, indent=1), encoding="utf-8")
print("diplomatic files", len(src["diplomatic"]), "current files", len(src["current"]))
