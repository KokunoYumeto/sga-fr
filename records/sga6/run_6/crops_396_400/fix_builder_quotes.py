"""Turn the two raw strings that contain escaped double quotes into triple-quoted raw strings (edits build_findings.py only)."""
import pathlib

p = pathlib.Path(__file__).resolve().parent / "build_findings.py"
lines = p.read_text(encoding="utf-8").split("\n")
BS = chr(92)
QQ = chr(34)
done = 0
for i, l in enumerate(lines):
    if (BS + QQ + "h" + BS + QQ) in l or (BS + QQ + "g" + BS + QQ) in l:
        s = l.lstrip()
        assert s.startswith("r" + QQ), s[:20]
        assert l.rstrip().endswith(QQ + ")"), l[-20:]
        indent = l[: len(l) - len(s)]
        body = s[2:]
        body = body[: body.rstrip().rfind(QQ + ")")]
        body = body.replace(BS + QQ, QQ)
        lines[i] = indent + "r" + QQ * 3 + body + QQ * 3 + ")"
        done += 1
print("lines changed:", done)
p.write_text("\n".join(lines), encoding="utf-8", newline="\n")
