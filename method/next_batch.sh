#!/usr/bin/env bash
# Prepare the next waiting batch of volume VOL (queue_sga.py next 1 VOL), render its prompt to
# run_VOL/prompt_FFF_LLL.txt and print that path (or nothing if the volume has no waiting batch).
# usage: bash next_batch.sh VOL
cd "$(dirname "$0")" || exit 1
VOL=$1
out=$(PYTHONIOENCODING=utf-8 python -I queue_sga.py next 1 "$VOL" 2>&1 | tail -1)
set -- $out
[ "$1" = "$VOL" ] || { echo "no batch: $out" >&2; exit 1; }
F=$2; L=$3; FF=$(printf %03d "$F"); LL=$(printf %03d "$L")
PYTHONIOENCODING=utf-8 python -I render_sga_prompt.py "$VOL" "$F" "$L" > "run_$VOL/prompt_${FF}_${LL}.txt"
echo "C:\\Users\\user\\Documents\\sga_scan_check_20261105\\run_$VOL\\prompt_${FF}_${LL}.txt"
