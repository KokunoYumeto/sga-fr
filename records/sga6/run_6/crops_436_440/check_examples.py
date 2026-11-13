"""Check that the convention examples quoted in the notes occur once in their page files."""
import pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")
B = pathlib.Path(__file__).resolve().parent.parent / "b436_440"
EX = [
    (436, r"soient \(x,y\in K^\circ(Y)\)"),
    (440, r"i_*:K^\circ(Y)\to K^\circ(X);"),
    (440, r"g_*:K^\circ(Y')\to K^\circ(Y)."),
    (436, r"de type fini \(M\). L'élément"),
    (437, r"On note \(J\) l'idéal"),
    (437, r"on le notera \(L\)."),
    (437, r"un idéal de \(\cO_X\)"),
    (437, r"\(j:Y'\to X\)"),
    (438, r"\(E=(A)^n\)"),
    (440, r"additifs (IV"),
]
for p, s in EX:
    t = (B / f"page_{p}.tex").read_text(encoding="utf-8")
    print(p, t.count(s), s)
