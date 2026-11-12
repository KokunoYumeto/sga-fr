"""Prepare in-app re-check batches for pages first checked over the API (user, 9 Nov: the API route found about half
the errors). For each batch FIRST-LAST of VOL: prepare the pages (prep_sga.py) into run_VOL/bFFF_LLL, render the
subagent prompt, and point its output at run_VOL/findings_FFF_LLL_recheck.json so the API findings stay. Prints the
prompt paths. Then launch one subagent per prompt; afterwards process_sga.py VOL run_VOL/findings_FFF_LLL_recheck.json.
usage: python -I prep_recheck.py VOL FIRST LAST [FIRST LAST ...]"""
import pathlib
import subprocess
import sys

W = pathlib.Path(__file__).resolve().parent
vol, nums = sys.argv[1], [int(x) for x in sys.argv[2:]]
for a, b in zip(nums[::2], nums[1::2]):
    folder = W / f"run_{vol}" / f"b{a:03d}_{b:03d}"
    subprocess.run([sys.executable, "-I", str(W / "prep_sga.py"), vol, str(a), str(b), str(folder)], check=True,
                   capture_output=True)
    r = subprocess.run([sys.executable, "-I", str(W / "render_sga_prompt.py"), vol, str(a), str(b)], check=True,
                       capture_output=True, text=True, encoding="utf-8")
    old = f"findings_{a:03d}_{b:03d}.json"
    assert old in r.stdout
    p = W / f"run_{vol}" / f"prompt_{a:03d}_{b:03d}_recheck.txt"
    p.write_text(r.stdout.replace(old, f"findings_{a:03d}_{b:03d}_recheck.json"), encoding="utf-8")
    print(p)
