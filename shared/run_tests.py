#!/usr/bin/env python3
"""Test runner for the AIAS ontology design patterns.

Discovers every package under odps/ and alignment/ that contains a tests/
directory, and runs five kinds of check against each:

  1. Syntax          every ontology and test file parses
  2. Profile         every ontology is in OWL 2 DL
  3. Consistency     every positive test model is consistent under HermiT
  4. Negative        every negative test model is INCONSISTENT (a test that
                     passes here proves an axiom actually bites)
  5. Competency      every SPARQL query returns the recorded expected result,
                     evaluated against the reasoned graph

A package looks like this:

    odps/<name>/
        <NAME>.ttl                 the ontology
        CQ_<NAME>.md               the competency question catalogue
        TESTMODEL.md               the test model documentation
        tests/data/*.ttl           positive models
        tests/negative/*.ttl       models that must be rejected
        tests/queries/*.rq         competency questions as SPARQL
        tests/expected/*.json      recorded results

Requires: rdflib, and robot.jar in this directory or reachable via ROBOT_JAR.

Usage:
    python shared/run_tests.py [--package vdi3682] [--update-expected] [--list]
"""

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    from rdflib import Graph, URIRef
except ImportError:
    sys.exit("rdflib is required: pip install rdflib")

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

sys.path.insert(0, str(HERE))

ROBOT = os.environ.get("ROBOT_JAR", str(HERE / "robot.jar"))

GREEN, RED, YELLOW, BOLD, RESET = (
    "\033[32m", "\033[31m", "\033[33m", "\033[1m", "\033[0m")
if os.name == "nt" and not os.environ.get("WT_SESSION"):
    GREEN = RED = YELLOW = BOLD = RESET = ""

results = {"pass": 0, "fail": 0, "skip": 0}
failures = []


def report(ok, name, detail="", package=""):
    if ok is None:
        results["skip"] += 1
        print(f"  {YELLOW}SKIP{RESET} {name} {detail}")
    elif ok:
        results["pass"] += 1
        print(f"  {GREEN}PASS{RESET} {name}")
    else:
        results["fail"] += 1
        failures.append(f"{package}: {name}")
        print(f"  {RED}FAIL{RESET} {name}")
        if detail:
            for line in str(detail).strip().splitlines()[:6]:
                print(f"       {line}")


def robot(*args, timeout=600):
    """Run ROBOT, returning (returncode, stdout+stderr)."""
    try:
        p = subprocess.run(
            ["java", "-jar", ROBOT, *args],
            capture_output=True, text=True, timeout=timeout,
        )
        return p.returncode, (p.stdout or "") + (p.stderr or "")
    except FileNotFoundError:
        return None, "java or robot.jar not found"
    except subprocess.TimeoutExpired:
        return 1, "timeout"


class Package:
    """One ontology together with its tests."""

    def __init__(self, directory: Path):
        self.dir = directory
        # directory is the version, its parent the package: vdi3682/v2.0.0
        self.name = f"{directory.parent.name}/{directory.name}"
        # A package may hold more than one ontology file, for instance a
        # pattern and its named individuals. The one whose name has no suffix
        # is the pattern; the rest are companions checked alongside it.
        ttls = sorted(directory.glob("*.ttl"))
        plain = [p for p in ttls if "-" not in p.stem]
        self.ontology = (plain or ttls)[0] if ttls else None
        self.companions = [p for p in ttls if p != self.ontology]
        self.tests = directory / "tests"
        self.data = sorted((self.tests / "data").glob("*.ttl"))
        self.negative = sorted((self.tests / "negative").glob("*.ttl"))
        self.queries = sorted((self.tests / "queries").glob("*.rq"))
        self.expected = self.tests / "expected"

    def __bool__(self):
        # A version without tests is still a package. The 1.0.0 of a pattern is
        # published as documentation without test infrastructure, and its
        # syntax and its OWL 2 DL profile have to be checked all the same.
        return self.ontology is not None


def all_ontologies():
    """Every ontology file across all packages and versions.

    Used to resolve owl:imports locally while the w3id redirect is not filed.
    All versions are included on purpose: a model may import a pattern at a
    version other than the newest, and the catalogue maps the version IRI to
    the file providing it.
    """
    found = []
    for d in _versions():
        found.extend(sorted(d.glob("*.ttl")))
    return found



def discover(version=None):
    packages = []
    for d in _versions(version):
        p = Package(d)
        if p:
            packages.append(p)
    return packages


def resolve_imports(path: Path) -> Path:
    """Concatenate a test model with the ontologies it imports.

    The w3id IRIs do not resolve yet, so imports are satisfied locally by
    merging the files. Once the w3id redirect is live this can be dropped.
    Imports are followed transitively, so an alignment model pulls in the
    patterns its ontology imports as well.
    """
    text = path.read_text(encoding="utf-8")
    merged, seen = [], set()

    # Map each ontology file to its declared ontology IRI, so that an
    # owl:imports can be matched against the file providing it.
    OWL_ONTOLOGY = "http://www.w3.org/2002/07/owl#Ontology"
    RDF_TYPE = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
    catalogue = {}
    for onto in all_ontologies():
        g = Graph()
        g.parse(str(onto), format="turtle")
        # A file is reachable under two IRIs: the ontology IRI, which every
        # version of a pattern shares, and its own versionIRI, which is unique.
        # An alignment imports the versioned one, so that a model gets the
        # version it was built against rather than whichever happens to be
        # newest.
        #
        # The version IRI therefore wins. Two versions of one pattern claim the
        # same ontology IRI, and whichever is read last would otherwise take
        # it, which is how a 1.0 alignment came to import 2.0 patterns.
        OWL_VERSION_IRI = "http://www.w3.org/2002/07/owl#versionIRI"
        for s, p, o in g.triples((None, None, None)):
            if str(p) == RDF_TYPE and str(o) == OWL_ONTOLOGY:
                catalogue.setdefault(str(s).rstrip("/"), onto)
                for v in g.objects(s, URIRef(OWL_VERSION_IRI)):
                    catalogue[str(v).rstrip("/")] = onto
                break

    def collect(source_text):
        """Follow owl:imports transitively.

        A model may import a companion file, such as the named individuals of a
        pattern, which in turn imports the pattern itself. Only the imports
        declared in the text under inspection are followed, so that merging one
        model does not drag in unrelated patterns.
        """
        # An owl:imports may list several targets separated by commas, which
        # a pattern matching one IRI would silently truncate to the first.
        imported = []
        for block in re.findall(r"owl:imports\s+((?:<[^>]+>\s*,\s*)*<[^>]+>)",
                                source_text):
            imported.extend(re.findall(r"<([^>]+)>", block))
        for target in imported:
            target = target.rstrip("/")
            onto = catalogue.get(target)
            if onto is None or onto in seen:
                continue
            seen.add(onto)
            onto_text = onto.read_text(encoding="utf-8")
            merged.append(onto_text)
            collect(onto_text)

    collect(text)
    if not merged:
        return path

    # Drop owl:imports so the reasoner does not try to fetch the w3id IRI.
    # Parsing and re-serialising avoids leaving dangling separators behind.
    g = Graph()
    g.parse(str(path), format="turtle")
    for s, p, o in list(g.triples((None, None, None))):
        if str(p) == "http://www.w3.org/2002/07/owl#imports":
            g.remove((s, p, o))

    tmp_dir = Path(tempfile.mkdtemp())
    body = tmp_dir / "body.ttl"
    g.serialize(destination=str(body), format="turtle")

    # Strip owl:imports from the merged ontologies as well. A companion file
    # such as the named individuals of a pattern imports the pattern itself,
    # and that declaration would send the reasoner to the unresolved w3id IRI
    # even though the pattern is already present in the merge.
    merged_text = "\n".join(merged)
    IMPORT_LIST = r"(?:<[^>]+>\s*,\s*)*<[^>]+>"
    merged_text = re.sub(rf"^\s*owl:imports\s+{IMPORT_LIST}\s*;\s*$", "",
                         merged_text, flags=re.M | re.S)
    merged_text = re.sub(rf"\s*owl:imports\s+{IMPORT_LIST}\s*\.", " .",
                         merged_text, flags=re.S)

    tmp = tmp_dir / path.name
    tmp.write_text(merged_text + "\n" + body.read_text(encoding="utf-8"),
                   encoding="utf-8")
    return tmp


def reason(model: Path, materialise=False):
    """Run HermiT. Returns (returncode, message, output path or None)."""
    merged = resolve_imports(model)
    out = Path(tempfile.mkdtemp()) / "reasoned.ttl"
    args = ["reason", "--input", str(merged), "--reasoner", "hermit"]
    if materialise:
        args += ["--axiom-generators",
                 "PropertyAssertion ClassAssertion SubClass"]
    args += ["--output", str(out)]
    rc, msg = robot(*args)
    return rc, msg, (out if rc == 0 else None)


def normalise(rows):
    return sorted(["|".join("" if v is None else str(v) for v in r)
                   for r in rows])


def run_package(pkg: Package, update: bool):
    print(f"\n{BOLD}=== {pkg.name} ==={RESET}")

    print("\n [1] Syntax")
    for f in [pkg.ontology] + pkg.data + pkg.negative:
        try:
            g = Graph()
            g.parse(str(f), format="turtle")
            report(True, f"{f.name} ({len(g)} triples)", package=pkg.name)
        except Exception as e:
            report(False, f.name, e, package=pkg.name)

    print("\n [2] OWL 2 DL profile")
    # Checked against the merged ontology rather than the file. An ontology
    # importing others, as the alignment does, cannot be loaded on its own
    # while the w3id IRIs are unresolved, and the profile of an ontology
    # covers its imports closure anyway.
    rc, out = robot("validate-profile",
                    "--input", str(resolve_imports(pkg.ontology)),
                    "--profile", "DL")
    if rc is None:
        report(None, pkg.ontology.name, out)
    else:
        report("in profile" in out.lower() and rc == 0,
               pkg.ontology.name, out, package=pkg.name)

    print("\n [3] Consistency of positive models")
    if not pkg.data:
        report(None, "no positive models")
    for m in pkg.data:
        rc, msg, _ = reason(m)
        if rc is None:
            report(None, m.name, msg)
        else:
            report(rc == 0, m.name, msg, package=pkg.name)

    print("\n [4] Negative models (must be INCONSISTENT)")
    if not pkg.negative:
        report(None, "no negative models")
    for m in pkg.negative:
        rc, msg, _ = reason(m)
        if rc is None:
            report(None, m.name, msg)
            continue
        inconsistent = rc != 0 and "inconsisten" in msg.lower()
        report(inconsistent, f"{m.name} rejected as expected",
               "model was accepted, so the axiom under test does not bite"
               if not inconsistent else "", package=pkg.name)

    print("\n [5] Competency questions")
    if not pkg.queries:
        report(None, "no queries")
        return
    if not pkg.data:
        report(None, "no model to query")
        return

    # Every query runs against every test case, with its own expectation per
    # case. A query that returns nothing for a case is still recorded, since an
    # empty result is itself an assertion: test case 1 must find no alternative
    # flows, and test case 3 must find no parallel ones.
    pkg.expected.mkdir(parents=True, exist_ok=True)
    for model in pkg.data:
        print(f"   {model.stem}")
        rc, msg, out = reason(model, materialise=True)
        if rc != 0:
            report(None, f"reasoning {model.name}", msg[:300])
            continue
        g = Graph()
        g.parse(str(out), format="turtle")

        for q in pkg.queries:
            name = f"{model.stem}/{q.stem}"
            exp_file = pkg.expected / f"{model.stem}__{q.stem}.json"
            try:
                rows = normalise(g.query(q.read_text(encoding="utf-8")))
            except Exception as e:
                report(False, name, e, package=pkg.name)
                continue

            if update or not exp_file.exists():
                exp_file.write_text(json.dumps(rows, indent=2), encoding="utf-8")
                report(None, name, f"expectation written ({len(rows)} rows)")
                continue

            expected = json.loads(exp_file.read_text(encoding="utf-8"))
            if rows == expected:
                report(True, f"{name} ({len(rows)} rows)", package=pkg.name)
            else:
                missing = [r for r in expected if r not in rows]
                extra = [r for r in rows if r not in expected]
                detail = ""
                if missing:
                    detail += f"missing: {missing[:3]}\n"
                if extra:
                    detail += f"unexpected: {extra[:3]}"
                report(False, name, detail, package=pkg.name)

    # A competency question asks about a modelled case. One that answers from
    # the pattern alone asks about the vocabulary instead, and its answer is
    # the same whichever case is loaded, so it tests that the terms were
    # written down rather than that the pattern can describe anything.
    #
    # The check runs each query against the ontology and its named individuals
    # with no test case loaded. Anything that still returns a row is anchored
    # on what the pattern ships rather than on what a model states.
    #
    # A few questions hold a supplied catalogue against a case and report, per
    # entry, whether the case states anything about it. Those answer with rows
    # either way, and the rows are the yardstick rather than the finding. They
    # opt out by carrying the line below in their comment, which has to say why
    # rather than merely switching the check off.
    OPT_OUT = "# A-box check: catalogue as yardstick."
    print("\n [6] Queries must answer from the A-box")
    tbox = Graph()
    for onto in [pkg.ontology, *pkg.companions]:
        tbox.parse(str(onto), format="turtle")
    for q in pkg.queries:
        text = q.read_text(encoding="utf-8")
        try:
            rows = [r for r in tbox.query(text) if any(v is not None for v in r)]
        except Exception as e:
            report(None, f"{q.stem} not checkable", str(e)[:120])
            continue
        if rows and OPT_OUT not in text:
            report(False, f"{q.stem} answers without a case ({len(rows)} rows)",
                   "anchored on the T-box: rewrite it to start from individuals, "
                   f"or declare it with '{OPT_OUT}' and say why",
                   package=pkg.name)
        elif rows:
            report(True, f"{q.stem} (catalogue as yardstick)", package=pkg.name)
        else:
            report(True, f"{q.stem}", package=pkg.name)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--version", default=None,
                    help="restrict to one published version, e.g. 1.0")
    ap.add_argument("--package", default=None,
                    help="restrict to one package, e.g. vdi3682")
    ap.add_argument("--update-expected", action="store_true",
                    help="record current query results as the expectation")
    ap.add_argument("--list", action="store_true",
                    help="list discovered packages and exit")
    args = ap.parse_args()

    packages = discover(version=args.version)
    if args.package:
        packages = [p for p in packages if args.package.lower() in p.name.lower()]

    if args.list:
        for p in packages:
            print(f"{p.name:16} ontology={p.ontology.name:20} "
                  f"models={len(p.data)} negative={len(p.negative)} "
                  f"queries={len(p.queries)}")
        return 0

    if not packages:
        print("no packages found")
        return 1

    for p in packages:
        run_package(p, args.update_expected)

    # Refresh the report, so the recorded results and their interpretations
    # never lag behind the models they document.
    try:
        from make_results import build
        for p in packages:
            target = build(p.dir)
            text = target.read_text(encoding="utf-8")
            missing = text.count("_Missing.")
            note = f", {missing} interpretations missing" if missing else ""
            print(f"\n report: {target.relative_to(ROOT)}{note}")
    except Exception as e:
        print(f"\n report: skipped ({e})")

    print(f"\n{'=' * 54}")
    print(f"passed {results['pass']}   failed {results['fail']}   "
          f"skipped {results['skip']}")
    if failures:
        print("\nfailed checks:")
        for f in failures:
            print(f"  {f}")
    return 1 if results["fail"] else 0


if __name__ == "__main__":
    sys.exit(main())
