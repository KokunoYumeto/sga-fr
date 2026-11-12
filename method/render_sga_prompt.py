"""Render the subagent checker prompt for one batch (the same prompt as the subagent runs of 5-6 Nov 2026: the template
CHECKER_PROMPT_SGA.txt with the volume's TITLE, and NOTE_<vol>.txt followed by the per-volume additions EXTRA kept in
sga_api_batch.py, so the API and the subagent runs share one note).

usage: python -I render_sga_prompt.py VOL FIRST LAST > prompt.txt
       (prepare the batch first: python -I queue_sga.py next 1 VOL)
"""
import importlib.util
import pathlib
import sys

W = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("sga_api_batch", W / "sga_api_batch.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

vol, a, z = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
folder = W / ("run_" + vol) / ("b%03d_%03d" % (a, z))
out = W / ("run_" + vol) / ("findings_%03d_%03d.json" % (a, z))
assert folder.is_dir(), "batch not prepared: %s" % folder
missing = [n for n in range(a, z + 1) if not (folder / ("page_%03d.tex" % n)).exists()]
t = (W / "CHECKER_PROMPT_SGA.txt").read_text(encoding="utf-8")
note = (W / ("NOTE_%s.txt" % vol)).read_text(encoding="utf-8").strip() + " " + m.EXTRA[vol]
t = (t.replace("{TITLE}", m.TITLE[vol]).replace("{NOTE}", note).replace("{FOLDER}", str(folder))
     .replace("{PAGES}", ", ".join(map(str, range(a, z + 1)))).replace("{OUTFILE}", str(out)))
if missing:
    t += "\n(No TeX was prepared for page(s) %s: say so in the final message.)\n" % ", ".join(map(str, missing))
sys.stdout.write(t)
