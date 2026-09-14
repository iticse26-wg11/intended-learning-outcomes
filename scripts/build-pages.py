#!/usr/bin/env -S uv run --quiet --with pyyaml python3
"""Generate the per-ILO pages (ilos/<ID>.md), the per-area tables (areas/*.md) and the
README quick index from ilos.yaml, the single canonical source
(statements and justifications there are themselves synced from the report by scripts/import-from-report.py).

Usage:  scripts/build-pages.py            # rewrite generated files
        scripts/build-pages.py --check    # exit 1 if anything is stale or ids are malformed

Stable URL for an ILO:
  https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/<ID>.md
Activities that address an ILO are read from ../learning-activities when that checkout exists.
Runs via uv (shebang), or `python3 scripts/build-pages.py` with PyYAML installed.
"""
import re, sys, pathlib, yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
ACTS = ROOT.parent / "learning-activities" / "activities"
BEGIN, END = "<!-- BEGIN GENERATED -->", "<!-- END GENERATED -->"
ACT_REPO = "https://github.com/iticse26-wg11/learning-activities"
ACT_URL = ACT_REPO + "/blob/main/activities/{id}/README.md"
AREA_FILE = {"H": "history", "MM": "mental-models", "EPR": "ethics-policy-regulations", "CS": "computer-science"}
ID_RE = re.compile(r"^(H|MM|EPR|CS)\d{2}[a-z]?$")

def load():
    y = yaml.safe_load((ROOT / "ilos.yaml").read_text())
    areas = {a["id"]: a["name"] for a in y["areas"]}
    ilos = y["ilos"]
    seen = set()
    for i in ilos:
        if not ID_RE.match(i["id"]) or i["id"] in seen or i["area"] not in areas:
            sys.exit(f"bad or duplicate id: {i}")
        seen.add(i["id"])
    return y["stem"], areas, ilos

def activities():
    """ILO id -> [(activity id, title)] from activity frontmatter."""
    rev = {}
    if not ACTS.exists():
        return rev
    for d in sorted(ACTS.glob("LA[0-9][0-9]")):
        m = re.match(r"---\n(.*?)\n---\n", (d / "README.md").read_text(), re.S)
        fm = yaml.safe_load(m.group(1))
        for ilo in fm.get("related_ilos", []):
            rev.setdefault(ilo, []).append((fm["id"], fm["title"]))
    return rev

def one_line(s):
    return " ".join(s.split())

def ilo_page(stem, areas, i, acts):
    out = [f"# {i['id']}", "",
           f"**Area:** {areas[i['area']]} ({i['area']})"
           + (f" · **Sub-area:** {i['subarea']}" if i.get("subarea") else "")
           + f" · **Topic:** {i['topic']}", "",
           f"> *{stem.rstrip(' …')}* …", ">",
           f"> **{one_line(i['statement'])}**", ""]
    if i.get("status"):
        out.insert(2, f"**Status:** {i['status']}\n")
    if i.get("justification"):
        out += ["## Why it is included", "", one_line(i["justification"]), ""]
    out += ["## Addressed by", ""]
    out += [f"- [{a} {t}]({ACT_URL.format(id=a)})" for a, t in acts.get(i["id"], [])] or ["- *(no activity yet)*"]
    out += ["", "---", f"Stable link: `https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/{i['id']}.md` · "
            f"Generated from [`ilos.yaml`](../ilos.yaml) by `scripts/build-pages.py`; edit the YAML, not this file.", ""]
    return "\n".join(out)

def addressed_by(acts, ilo_id):
    return ", ".join(f"[{a}]({ACT_URL.format(id=a)})" for a, _ in acts.get(ilo_id, [])) or "—"

def area_table(rows, acts):
    out = ["| ID | Topic | ILO | Addressed by |", "|----|-------|-----|--------------|"]
    for i in rows:
        out.append(f"| [**{i['id']}**](../ilos/{i['id']}.md) | {i['topic']} | … {one_line(i['statement'])} | {addressed_by(acts, i['id'])} |")
    return "\n".join(out)

def area_page(stem, areas, code, rows, acts):
    out = [f"# {areas[code]} ({code})", "",
           f"All outcomes complete the stem: **\"{stem}\"**", "",
           f"*Generated from [`ilos.yaml`](../ilos.yaml) by `scripts/build-pages.py`; each ID links to the ILO's stable page, "
           f"and \"Addressed by\" links to the [learning activities]({ACT_REPO}) that cover it.*", ""]
    subs = []
    for i in rows:
        s = i.get("subarea")
        if s not in subs:
            subs.append(s)
    for s in subs:
        if s:
            out += [f"## {s}", ""]
        out += [area_table([i for i in rows if i.get("subarea") == s], acts), ""]
    return "\n".join(out)

def readme_block(areas, ilos, acts):
    out = ["| ID | Area | Topic | Outcome | Addressed by |", "|----|------|-------|---------|--------------|"]
    for i in ilos:
        out.append(f"| [{i['id']}](ilos/{i['id']}.md) | {i['area']} | {i['topic']} | … {one_line(i['statement'])} | {addressed_by(acts, i['id'])} |")
    return "\n".join(out)

def main():
    check = "--check" in sys.argv
    stem, areas, ilos = load()
    acts = activities()
    unknown = sorted(set(acts) - {i["id"] for i in ilos})
    if unknown:
        print("activities reference unknown ILO ids:", ", ".join(unknown))
    files = {}
    for i in ilos:
        files[ROOT / "ilos" / f"{i['id']}.md"] = ilo_page(stem, areas, i, acts)
    for code in areas:
        files[ROOT / "areas" / f"{AREA_FILE[code]}.md"] = area_page(stem, areas, code, [i for i in ilos if i["area"] == code], acts)
    readme = ROOT / "README.md"
    pre, _, rest = readme.read_text().partition(BEGIN)
    _, _, post = rest.partition(END)
    files[readme] = f"{pre}{BEGIN}\n{readme_block(areas, ilos, acts)}\n{END}{post}"
    stale = [p for p, s in files.items() if not p.exists() or p.read_text() != s]
    if check:
        for p in stale: print("stale:", p.relative_to(ROOT))
        sys.exit(1 if stale or unknown else 0)
    (ROOT / "ilos").mkdir(exist_ok=True)
    for p, s in files.items():
        p.write_text(s)
    print(f"wrote {len(ilos)} ILO pages, {len(areas)} area pages, README index")

main()
