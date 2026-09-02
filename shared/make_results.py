#!/usr/bin/env python3
"""Generate the competency question report of an ontology design pattern.

For each question the report shows what was asked, the query that answers it,
the result on every test case, and an interpretation. It exists so that a
reviewer can follow what the pattern actually answers without running anything.

The split of responsibilities matters:

  generated   question, query, results. Taken from the queries and the recorded
              expectations, so they cannot fall out of step with the models.
  written     the interpretation, kept in <package>/interpretations.md. A
              question without an entry is marked as missing in the report
              rather than silently omitted.

Empty results are reported as such, since an empty result is an assertion: that
no operator lacks a resource is the answer to question 15, not a gap.

Usage:
    python shared/make_results.py [--package vdi3682]
"""

import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
ROOT = HERE.parent
# Every ontology carries its own version, so the version sits one level below
# the package rather than above it: odps/vdi3682/v2.0.0/. IEC 60050-351 has no
# predecessor and is therefore a v1.0.0 while the others are already v2.0.0,
# which no shared version directory could express.
#
# A version is a maintained branch rather than a frozen copy: the 1.0.0 of a
# pattern is the model of the dissertation and may still receive a 1.0.1.
SEARCH_DIRS = [ROOT / "odps", ROOT / "alignment"]
VERSION_RE = re.compile(r"^v\d+\.\d+\.\d+$")


def _versions(version=None):
    """Every package version directory, optionally restricted to one version."""
    want = None if version is None else (
        version if version.startswith("v") else "v" + version)
    out = []
    for base in SEARCH_DIRS:
        if not base.is_dir():
            continue
        for pkg in sorted(base.iterdir()):
            if not pkg.is_dir():
                continue
            for v in sorted(pkg.iterdir()):
                if v.is_dir() and VERSION_RE.match(v.name)                         and (want is None or v.name == want):
                    out.append(v)
    return out



def packages(only=None, version=None):
    found = []
    for d in _versions(version):
        # d is the version directory; the package name is its parent.
        if (d / "tests" / "queries").is_dir():
            if only is None or only.lower() in d.parent.name.lower():
                found.append(d)
    return found


def read_catalogue(directory: Path):
    """Question text and section headings from CQ_<NAME>.md."""
    cq_files = list(directory.glob("CQ_*.md"))
    if not cq_files:
        return {}, {}
    text = cq_files[0].read_text(encoding="utf-8")

    questions, sections, current = {}, {}, None
    for line in text.splitlines():
        heading = re.match(r"^## (\d+\.\s+.*)$", line)
        if heading:
            current = heading.group(1)
            continue
        row = re.match(r"^\|\s*(\d{2})\s*\|\s*([^|]+?)\s*\|", line)
        if row:
            num = row.group(1)
            questions[num] = row.group(2).strip()
            if current:
                sections.setdefault(current, []).append(num)
    return questions, sections


def read_interpretations(directory: Path):
    f = directory / "interpretations.md"
    if not f.exists():
        return {}
    out, key, buf = {}, None, []
    for line in f.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^## cq(\d+)\s*$", line.strip(), re.I)
        if m:
            if key:
                out[key] = "\n".join(buf).strip()
            key, buf = m.group(1).zfill(2), []
        elif key is not None:
            buf.append(line)
    if key:
        out[key] = "\n".join(buf).strip()
    return out


def query_body(path: Path):
    """The query without its leading comment block."""
    lines = path.read_text(encoding="utf-8").splitlines()
    while lines and (lines[0].startswith("#") or not lines[0].strip()):
        lines.pop(0)
    return "\n".join(lines).strip()


def query_doc(path: Path):
    """The leading comment block, minus the restated question."""
    lines, out = path.read_text(encoding="utf-8").splitlines(), []
    for line in lines:
        if not line.startswith("#"):
            break
        out.append(line.lstrip("#").strip())
    while out and (out[0].startswith("CQ ") or not out[0]):
        out.pop(0)
    return " ".join(x for x in out if x).strip()


def columns_of(query: str):
    """Projected variable names, in order, including aliases."""
    m = re.search(r"SELECT\s+(DISTINCT\s+)?(.*?)\s+WHERE", query, re.S | re.I)
    if not m:
        return []
    cols, depth, token = [], 0, ""
    for ch in m.group(2):
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth == 0:
                alias = re.search(r"AS\s+\?(\w+)", token, re.I)
                if alias:
                    cols.append(alias.group(1))
                token = ""
                continue
        if depth == 0 and ch.isspace():
            if token.startswith("?"):
                cols.append(token[1:])
            token = ""
        else:
            token += ch
    if token.startswith("?"):
        cols.append(token[1:])
    return cols


def shorten(value: str):
    """Drop namespaces so the tables stay readable."""
    for sep in ("#", "/"):
        if value.startswith("http") and sep in value:
            tail = value.rsplit(sep, 1)[1]
            if tail:
                return tail
    return value


def build(directory: Path) -> Path:
    name = directory.name
    questions, sections = read_catalogue(directory)
    interpretations = read_interpretations(directory)
    queries = {q.stem[2:4]: q for q in sorted((directory / "tests" / "queries").glob("cq*.rq"))}
    expected_dir = directory / "tests" / "expected"

    cases = sorted({f.stem.split("__")[0] for f in expected_dir.glob("*.json")})

    out = [
        f"# Competency Question Results: {name}",
        "",
        "Generated by `shared/make_results.py`. Do not edit: the questions come "
        "from the catalogue, the queries and results from the test suite, and "
        "the interpretations from `interpretations.md`.",
        "",
        f"Test cases: {', '.join(f'`{c}`' for c in cases)}",
        "",
        "An empty result is an answer, not a gap. Where a question returns "
        "nothing on a case, the interpretation says what that absence "
        "asserts.",
        "",
        "---",
        "",
    ]

    ordered = []
    for heading, nums in sections.items():
        ordered.append((heading, nums))
    covered = {n for _, nums in ordered for n in nums}
    rest = sorted(set(queries) - covered)
    if rest:
        ordered.append(("Further questions", rest))

    for heading, nums in ordered:
        out.append(f"## {heading}")
        out.append("")
        for num in nums:
            q = questions.get(num, "")
            out.append(f"### CQ {num}: {q}")
            out.append("")

            qf = queries.get(num)
            if qf is None:
                out.append("_No query for this question._")
                out.append("")
                continue

            doc = query_doc(qf)
            if doc:
                out.append(f"{doc}")
                out.append("")

            out.append(f"**Query** `tests/queries/{qf.name}`")
            out.append("")
            out.append("```sparql")
            out.append(query_body(qf))
            out.append("```")
            out.append("")

            cols = columns_of(query_body(qf))
            rows = []
            for case in cases:
                f = expected_dir / f"{case}__{qf.stem}.json"
                if not f.exists():
                    continue
                data = json.load(open(f, encoding="utf-8"))
                if not data:
                    rows.append([case, "*(empty)*"] + [""] * (len(cols) - 1))
                else:
                    for r in data:
                        vals = [shorten(v) for v in r.split("|")]
                        vals += [""] * (len(cols) - len(vals))
                        rows.append([case] + vals[:len(cols)])

            out.append("**Results**")
            out.append("")
            header = ["Case"] + cols
            out.append("| " + " | ".join(header) + " |")
            out.append("|" + "---|" * len(header))
            for r in rows:
                out.append("| " + " | ".join(x if x else "" for x in r) + " |")
            out.append("")

            interp = interpretations.get(num)
            if interp:
                out.append(f"**Interpretation.** {interp}")
            else:
                out.append("**Interpretation.** _Missing. Add a `## cq"
                           f"{num}` section to `interpretations.md`._")
            out.append("")

    target = directory / "RESULTS.md"
    target.write_text("\n".join(out) + "\n", encoding="utf-8")
    return target


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--version", default=None,
                    help="restrict to one published version, e.g. 1.0")
    ap.add_argument("--package", default=None)
    args = ap.parse_args()

    pkgs = packages(args.package, args.version)
    if not pkgs:
        sys.exit("no packages found")

    for d in pkgs:
        target = build(d)
        text = target.read_text(encoding="utf-8")
        missing = text.count("_Missing.")
        noquery = text.count("_No query")
        print(f"  {target.relative_to(ROOT)}  "
              f"({len(text.splitlines())} lines"
              + (f", {missing} interpretations missing" if missing else "")
              + (f", {noquery} questions without a query" if noquery else "")
              + ")")
    return 0


if __name__ == "__main__":
    sys.exit(main())
