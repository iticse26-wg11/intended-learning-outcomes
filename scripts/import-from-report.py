#!/usr/bin/env -S uv run --quiet --with pyyaml python3
"""Sync ILO statements and justifications in ilos.yaml from the WG11 report.

Source: ../report/sections/50-design-ilos.tex, the four "Intended Learning Outcomes" tables
(columns ID / Description / Justification for Inclusion). The report is the source of truth:
edit it there and re-run this script. Only `statement` and `justification` are rewritten;
`area`, `subarea`, `topic`, `status`, ordering and the comments in ilos.yaml are repo-owned.

Usage:  scripts/import-from-report.py [--report PATH]   # rewrite ilos.yaml (then run build-pages.py)
        scripts/import-from-report.py --check            # exit 1 if ilos.yaml is out of sync
"""
import re, sys, pathlib, subprocess, textwrap, yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
args = sys.argv[1:]
REPORT = pathlib.Path(args[args.index("--report") + 1] if "--report" in args else ROOT.parent / "report").resolve()
TEX = REPORT / "sections" / "50-design-ilos.tex"
YAML = ROOT / "ilos.yaml"
STAMP_RE = re.compile(r"^# Statements and justifications imported from .*\n", re.M)

def overleaf_state():
    try:
        return subprocess.run(["git", "-C", str(REPORT), "log", "-1", "--format=%h %cs"],
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "unknown commit"

def clean(s):
    s = re.sub(r"(?<!\\)%.*", "", s)                                   # comments
    s = re.sub(r"\s*\((?:Section|Sec\.|Table|Appendix)[~ ]*\\ref\{[^}]*\}\)", "", s)   # "(Section~\ref{..})" pointers
    s = re.sub(r"\\cite\{([^}]*)\}", lambda m: "[" + "; ".join(cite(k.strip()) for k in m.group(1).split(",")) + "]", s)
    for _ in range(3):
        s = re.sub(r"\\(?:textbf|emph|textit|ilo|la)\{([^{}]*)\}", r"\1", s)
    s = re.sub(r"\\(?:ldots|dots)\b", "…", s).replace("...", "…")
    s = s.replace("``", "“").replace("''", "”").replace("~", " ").replace(r"\&", "&").replace(r"\%", "%")
    s = re.sub(r"(?<!-)---(?!-)", "—", s); s = re.sub(r"(?<!-)--(?!-)", "–", s)
    s = re.sub(r"\\,", " ", s); s = re.sub(r"\\ ", " ", s)
    s = re.sub(r"^\s*…\s*", "", s.strip())                             # leading stem ellipsis
    for cmd in sorted(set(re.findall(r"\\[a-zA-Z]+", s))):
        print(f"warning: unconverted LaTeX command {cmd} in: {s[:60]}", file=sys.stderr)
    return re.sub(r"\s+", " ", s).strip()

_BIB = None
def cite(key):
    """Short 'Surname et al., year' for a bib key, from the report's .bib files."""
    global _BIB
    if _BIB is None:
        _BIB = {}
        for f in REPORT.glob("*.bib"):
            for m in re.finditer(r"@\w+\{([^,]+),(.*?)\n\}", f.read_text(), flags=re.S):
                _BIB[m.group(1).strip()] = m.group(2)
    e = _BIB.get(key)
    if e is None:
        print(f"warning: unknown cite key {key}", file=sys.stderr); return key
    def field(n):
        m = re.search(rf"\b{n}\s*=\s*(?:[{{\"](.*?)[}}\"]|(\w+))\s*,?\s*\n", e, flags=re.S | re.I)
        return re.sub(r"\s+", " ", m.group(1) or m.group(2)).strip("{} ") if m else ""
    authors = [a.strip() for a in re.split(r"\s+and\s+", field("author")) if a.strip()]
    def surname(a): return a.split(",")[0].strip() if "," in a else a.split()[-1]
    first = re.sub(r"[{}]", "", surname(authors[0])) if authors else field("title")[:30]
    return f"{first}{' et al.' if len(authors) > 2 else (' & ' + surname(authors[1]) if len(authors) == 2 else '')}, {field('year') or 'n.d.'}"

def parse_report():
    tex = TEX.read_text()
    rows = re.findall(r"\\textbf\{\\ilo\{(\w+)\}\}\s*&(.*?)&(.*?)\\\\", tex, flags=re.S)
    return {i: (clean(st), clean(ju)) for i, st, ju in rows}

def folded(key, text, indent=4):
    body = textwrap.fill(text, width=78, initial_indent=" " * (indent + 2), subsequent_indent=" " * (indent + 2),
                         break_long_words=False, break_on_hyphens=False)
    return f"{' ' * indent}{key}: >-\n{body}\n"

def sync(src, rep):
    out, missing = src, []
    for i in yaml.safe_load(src)["ilos"]:
        if i["id"] not in rep:
            missing.append(i["id"]); continue
        st, ju = rep[i["id"]]
        m = re.search(rf"^  - id: {re.escape(i['id'])}\n(.*?)(?=^  - id: |\Z)", out, flags=re.S | re.M)
        block = m.group(1)
        new = re.sub(r"^    statement: >-\n(?:      .*\n?)+", lambda _: folded("statement", st), block, count=1, flags=re.M)
        if re.search(r"^    justification: >-\n", new, flags=re.M):
            new = re.sub(r"^    justification: >-\n(?:      .*\n?)+", lambda _: folded("justification", ju), new, count=1, flags=re.M)
        else:
            new = re.sub(r"(^    statement: >-\n(?:      .*\n?)+)", lambda mm: mm.group(1) + folded("justification", ju),
                         new, count=1, flags=re.M)
        out = out[:m.start(1)] + new + out[m.end(1):]
    return out, missing

def main():
    check = "--check" in args
    rep = parse_report()
    src = YAML.read_text()
    out, missing = sync(src, rep)
    stamp = (f"# Statements and justifications imported from the WG11 report, sections/50-design-ilos.tex "
             f"(Overleaf commit {overleaf_state()}) by scripts/import-from-report.py; re-run it, do not hand-edit them.\n")
    out = STAMP_RE.sub(stamp, out) if STAMP_RE.search(out) else out.replace("\nstem:", "\n" + stamp + "\nstem:", 1)
    extra = sorted(set(rep) - {i["id"] for i in yaml.safe_load(src)["ilos"]})
    for i in missing: print(f"warning: {i} is in ilos.yaml but not in the report", file=sys.stderr)
    for i in extra: print(f"warning: {i} is in the report but not in ilos.yaml", file=sys.stderr)
    changed = STAMP_RE.sub("", out) != STAMP_RE.sub("", src)
    if check:
        print("out of sync with the report" if changed else "in sync with the report")
        sys.exit(1 if changed or extra else 0)
    YAML.write_text(out)
    print(f"synced {len(rep)} ILOs from {overleaf_state()}; ilos.yaml {'rewritten' if changed else 'unchanged (stamp only)'}")

main()
