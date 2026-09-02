#!/usr/bin/env python3
"""Render the UML diagrams of every package.

Each package keeps its diagrams as PlantUML sources in <package>/figures/. This
script renders them to SVG, which is vector, opens in any browser and is taken
by LaTeX through svg or after a conversion.

A figures directory may also hold files named `norm-*.png`, which are excerpts
from a purchased standard, placed there by hand and excluded from version
control. This script never writes or removes them, and neither should any
cleanup of rendered output: `rm figures/*.png` would take them with it.

The sources are written by hand, not generated from the ontology. That is
deliberate. A diagram generated from the whole of an ontology shows everything
and therefore says nothing, and the complete picture is already available as the
WebVOWL view that Widoco produces. These diagrams are partial on purpose: each
one carries one statement, and what it leaves out is part of the statement.

The header comment of every source records what it leaves out and why, so that a
reader can tell a deliberate omission from an oversight.

Requires: plantuml.jar in this directory or reachable via PLANTUML_JAR, and
Java 8 or later. PlantUML brings its own Graphviz, so nothing else is needed.

    python shared/make_figures.py                     # everything
    python shared/make_figures.py --package iec60050  # one package
    python shared/make_figures.py --list              # what is discovered

Only SVG is produced. PlantUML also writes PNG and EPS, and PDF once Apache
Batik is on the classpath. Add the wanted format to FORMATS when a raster or a
PDF version is actually needed.
"""

import argparse
import os
import subprocess
import sys
import re
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

PLANTUML = os.environ.get("PLANTUML_JAR", str(HERE / "plantuml.jar"))
FORMATS = ["svg"]

GREEN, RED, YELLOW, BOLD, RESET = (
    "\033[32m", "\033[31m", "\033[33m", "\033[1m", "\033[0m")
if os.name == "nt" and not os.environ.get("WT_SESSION"):
    GREEN = RED = YELLOW = BOLD = RESET = ""



def discover(version=None):
    """Every package version that has a figures/ directory with sources."""
    found = []
    for d in _versions(version):
        figures = d / "figures"
        if figures.is_dir() and list(figures.glob("*.puml")):
            # Name it package/version, since one package may carry several.
            found.append((f"{d.parent.name}/{d.name}", figures))
    return found


def render(source: Path, fmt: str):
    """Render one source into one format. Returns (ok, message)."""
    try:
        r = subprocess.run(
            ["java", "-jar", PLANTUML, f"-t{fmt}", str(source)],
            capture_output=True, text=True, timeout=300)
    except FileNotFoundError:
        return False, "java not found"
    except subprocess.TimeoutExpired:
        return False, "timed out"

    out = source.parent / f"{source.stem}.{fmt}"
    if r.returncode != 0:
        return False, (r.stderr or r.stdout).strip()[:200]
    if not out.exists() or out.stat().st_size == 0:
        return False, f"{out.name} is empty"
    return True, f"{out.stat().st_size // 1024} KB"


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--version", default=None,
                    help="restrict to one published version, e.g. 1.0")
    ap.add_argument("--package", help="render one package only")
    ap.add_argument("--list", action="store_true", help="list what is discovered")
    args = ap.parse_args()

    packages = discover(version=args.version)
    if args.package:
        # A name is now package/version, so match either part: --package aias
        # takes every version of it, --package aias/v2.0.0 just the one.
        want = args.package.lstrip("v") if "/" not in args.package else args.package
        packages = [p for p in packages
                    if p[0] == args.package or p[0].split("/")[0] == want]
        if not packages:
            sys.exit(f"no package {args.package!r} with a figures/ directory")

    if args.list:
        for name, figures in packages:
            sources = sorted(figures.glob("*.puml"))
            print(f"{name}: {len(sources)} diagram(s)")
            for s in sources:
                print(f"    {s.name}")
        return

    if not Path(PLANTUML).exists():
        sys.exit(f"plantuml.jar not found at {PLANTUML}\n"
                 "Set PLANTUML_JAR, or download it with\n"
                 "  curl -sL -o shared/plantuml.jar \\\n"
                 "    https://github.com/plantuml/plantuml/releases/download/"
                 "v1.2025.4/plantuml-1.2025.4.jar")

    print(f"PlantUML: {PLANTUML}")
    print("Note: files named norm-*.png are excerpts from a standard, kept "
          "by hand and never touched by this script. Do not delete them "
          "when clearing rendered output.")
    failed = 0
    for name, figures in packages:
        print(f"\n{BOLD}=== {name} ==={RESET}")
        for source in sorted(figures.glob("*.puml")):
            done = []
            for fmt in FORMATS:
                ok, msg = render(source, fmt)
                if ok:
                    done.append(f"{fmt} {msg}")
                else:
                    failed += 1
                    print(f"  {RED}FAIL{RESET} {source.name} -> {fmt}: {msg}")
            if done:
                print(f"  {GREEN}OK{RESET}   {source.name}  ({', '.join(done)})")

    print()
    if failed:
        print(f"{RED}{failed} render(s) failed{RESET}")
        sys.exit(1)
    print(f"{GREEN}all diagrams rendered{RESET}")


if __name__ == "__main__":
    main()
