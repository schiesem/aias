#!/usr/bin/env python3
"""Write the values of the metadata.md files into the ontology headers.

`shared/metadata.md` carries what is the same for every package, each
`<package>/v<version>/doc/metadata.md` what belongs to that one, and a package
overrides a shared value by setting the same key. The Turtle files are
generated from those two, never edited by hand.

Only the ontology header is touched. Everything below the first class or
property declaration is copied through untouched, and the result is checked
with rdflib: if the number of triples outside the header changes, the file is
not written.

Usage:
    python shared/apply_metadata.py [--package vdi3682] [--version 1.0.0]
                                    [--check]
"""

import argparse
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
ROOT = HERE.parent
SEARCH_DIRS = [ROOT / "odps", ROOT / "alignment"]
VERSION_RE = re.compile(r"^v\d+\.\d+\.\d+$")

# Which key of metadata.md becomes which predicate, and how it is written.
#
# "iri"      the value is an IRI, written in angle brackets
# "text"     a plain literal, tagged @en
# "plain"    a plain literal without a language tag, for names and versions
# "date"     an xsd:date
# "auto"     an IRI where the value looks like one, a plain literal otherwise
#
# The order is the order the header is written in.
FIELDS = [
    ("title",                 "dcterms:title",                 "text"),
    ("abstract",              "dcterms:abstract",              "text"),
    ("description",           "dcterms:description",           "text"),
    ("created",               "dcterms:created",               "date"),
    ("modified",              "dcterms:modified",              "date"),
    ("creator",               "dcterms:creator",               "auto"),
    ("contributor",           "dcterms:contributor",           "auto"),
    ("publisher",             "dcterms:publisher",             "auto"),
    ("rights",                "dcterms:rights",                "text"),
    ("fundedBy",              "foaf:fundedBy",                 "iri"),
    ("license",               "dcterms:license",               "iri"),
    ("bibliographicCitation", "dcterms:bibliographicCitation", "text"),
    ("doi",                   "bibo:doi",                      "plain"),
    ("source",                "dcterms:source",                "iri"),
    ("references",            "dcterms:references",            "text"),
    ("subject",               "dcterms:subject",               "list"),
    ("codeRepository",        "schema:codeRepository",         "iri"),
    ("latestVersion",         "dcterms:hasVersion",            "iri"),
    ("priorVersion",          "owl:priorVersion",              "iri"),
    ("priorVersion",          "dcterms:replaces",              "iri"),
    ("incompatibleWith",      "owl:incompatibleWith",          "iri"),
    ("status",                "bibo:status",                   "text"),
]

# Prefixes the header may need. Written only where actually used.
PREFIXES = {
    "dcterms": "http://purl.org/dc/terms/",
    "vann":    "http://purl.org/vocab/vann/",
    "bibo":    "http://purl.org/ontology/bibo/",
    "foaf":    "http://xmlns.com/foaf/0.1/",
    "schema":  "https://schema.org/",
    "skos":    "http://www.w3.org/2004/02/skos/core#",
}

# Keys that are ours rather than the ontology's, and are never written.
NOT_WRITTEN = {"iri", "prefix", "version", "label", "pagesBase"}


# Keys whose indented lines are separate values rather than one wrapped
# paragraph. Everything else is prose and is joined back into one string.
LIST_KEYS = {"creator", "contributor", "publisher", "fundedBy", "references"}


def read_metadata(path: Path) -> dict:
    """Parse a metadata.md into a dict of key to value or list of values.

    One `key: value` per line, continued on the following lines while they are
    indented by two spaces. For a key in LIST_KEYS each indented line is a
    value of its own; for any other key they are one paragraph, wrapped for
    readability and joined back together here. HTML comments are skipped.
    """
    if not path.is_file():
        return {}
    text = path.read_text(encoding="utf-8")
    while "<!--" in text:
        a = text.index("<!--")
        b = text.find("-->", a)
        text = text[:a] + (text[b + 3:] if b != -1 else "")

    out, key, buf = {}, None, []

    def close():
        if key is None or not buf:
            return
        # an empty value drops the field rather than writing an empty string
        if key in LIST_KEYS and len(buf) > 1:
            out[key] = list(buf)
        else:
            out[key] = " ".join(buf)

    for raw in text.splitlines():
        if raw.startswith("#") or not raw.strip():
            continue
        if raw.startswith("  ") and key is not None:
            buf.append(raw.strip())
            continue
        m = re.match(r"^([A-Za-z][A-Za-z0-9_]*)\s*:\s*(.*)$", raw)
        if not m:
            continue
        close()
        key, value = m.group(1), m.group(2).strip()
        buf = [value] if value else []
    close()
    return out


def esc(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"')


def render(value: str, kind: str) -> str:
    """One value as a Turtle object."""
    if kind == "iri":
        return f"<{value}>"
    if kind == "date":
        return f'"{esc(value)}"^^xsd:date'
    if kind == "plain":
        return f'"{esc(value)}"'
    if kind == "auto":
        # "Name | https://orcid.org/…" becomes the IRI, so that a person is a
        # thing rather than a string. A bare name stays a literal.
        if "|" in value:
            return f"<{value.split('|', 1)[1].strip()}>"
        if value.startswith("http://") or value.startswith("https://"):
            return f"<{value}>"
        return f'"{esc(value)}"'
    if "\n" in value or len(value) > 90:
        return f'"""{esc(value)}"""@en'
    return f'"{esc(value)}"@en'


def header_lines(meta: dict) -> tuple:
    """The predicate lines of the header, and the prefixes they need."""
    lines, used = [], set()
    for key, predicate, kind in FIELDS:
        if key not in meta:
            continue
        values = meta[key]
        if kind == "list":
            values = [v.strip() for v in str(values).split(",") if v.strip()]
            kind = "text"
        elif not isinstance(values, list):
            values = [values]
        for v in values:
            lines.append(f"    {predicate} {render(v, kind)} ;")
            used.add(predicate.split(":", 1)[0])
    return lines, used


def apply(directory: Path, check: bool = False) -> bool:
    """Rewrite the header of the ontology in one version directory."""
    meta = dict(read_metadata(ROOT / "shared" / "metadata.md"))
    meta.update(read_metadata(directory / "doc" / "metadata.md"))

    ttls = sorted(p for p in directory.glob("*.ttl") if "-" not in p.stem)
    if not ttls:
        return True
    ttl = ttls[0]
    text = ttl.read_text(encoding="utf-8")

    iri = meta.get("iri")
    version = meta.get("version")
    prefix = meta.get("prefix")
    if not (iri and version and prefix):
        print(f"  SKIP {directory.parent.name}/{directory.name}: "
              "iri, version or prefix missing")
        return True

    # The header runs from the ontology declaration to the statement's
    # closing full stop. A blank line is no use as the end marker: the long
    # description and comment contain several of their own.
    start = text.index(f"<{iri}>\n    a owl:Ontology ;")
    end, i, in_long = None, start, False
    while i < len(text):
        if text.startswith('"""', i):
            in_long = not in_long
            i += 3
            continue
        if not in_long and text[i] == "." and text[i - 1] in " \n" \
                and (i + 1 >= len(text) or text[i + 1] in "\n "):
            end = i + 1
            break
        i += 1
    if end is None:
        print(f"  SKIP {directory.parent.name}/{directory.name}: "
              "header has no closing full stop")
        return True
    old_header = text[start:end]

    # owl:imports belongs to the ontology statement but is not a metadata
    # field: it is what the ontology needs in order to be loadable at all.
    # Carried over verbatim, since rebuilding the header from the field list
    # alone would silently drop it.
    # The list may run over several lines separated by commas, so it ends at
    # the semicolon closing the predicate, not at the first IRI.
    # The list may run over several lines separated by commas, so it ends
    # at the semicolon closing the predicate, not at the first IRI.
    imports = re.search(r"\n    owl:imports\s+<[^;]*>(?=\s*[;.])",
                        old_header, re.S)

    lines, used = header_lines(meta)
    header = "\n".join([
        f"<{iri}>",
        "    a owl:Ontology ;",
        f"    owl:versionIRI <{iri}/{version}> ;",
        f'    owl:versionInfo "{version}" ;',
        *lines,
        f'    vann:preferredNamespaceUri "{iri}#" ;',
        f'    vann:preferredNamespacePrefix "{prefix}" ;',
    ])
    if imports:
        header += imports.group(0).rstrip().rstrip(";").rstrip() + " ;"
    used.update({"vann"})

    # rdfs:comment of the old header is written by hand and stays.
    m = re.search(r'\n    rdfs:comment """.*?"""@en', old_header, re.S)
    if m:
        header += m.group(0) + " ."
    else:
        header = header.rstrip(" ;") + " ."
    if header.rstrip().endswith(";"):
        header = header.rstrip().rstrip(";").rstrip() + " ."

    new_text = text[:start] + header + text[end:]

    # Prefixes the new header needs but the file does not declare yet.
    for p in sorted(used):
        if f"@prefix {p}:" not in new_text and p in PREFIXES:
            anchor = new_text.index("\n\n")
            decl = f"@prefix {p}:{' ' * max(1, 8 - len(p))}<{PREFIXES[p]}> .\n"
            new_text = new_text[:anchor] + "\n" + decl.rstrip() + new_text[anchor:]

    # Annotation properties must be declared for OWL 2 DL. The block sits
    # directly below the header; it is rewritten rather than added to, so a
    # second run does not produce a second copy.
    wanted = [pred for _, pred, _ in FIELDS if f"    {pred} " in header]
    wanted += ["vann:preferredNamespaceUri", "vann:preferredNamespacePrefix"]
    if "skos:note" in new_text:
        wanted.append("skos:note")
    if "skos:altLabel" in new_text:
        wanted.append("skos:altLabel")

    seen, ordered = set(), []
    for pred in wanted:
        if pred not in seen and not pred.startswith("owl:"):
            seen.add(pred)
            ordered.append(pred)

    new_text = re.sub(
        r"(?m)^[a-z]+:[A-Za-z]+ a owl:AnnotationProperty \.\n", "", new_text)
    decls = "\n".join(f"{pred} a owl:AnnotationProperty ." for pred in ordered)
    anchor = new_text.index(header) + len(header)
    tail = new_text[anchor:].lstrip("\n")
    new_text = new_text[:anchor] + "\n\n" + decls + "\n\n" + tail

    if new_text == text:
        print(f"  unchanged {directory.parent.name}/{directory.name}")
        return True

    # Nothing outside the header may change.
    try:
        from rdflib import Graph, URIRef
        before, after = Graph(), Graph()
        before.parse(data=text, format="turtle")
        after.parse(data=new_text, format="turtle")
        from rdflib.compare import isomorphic
        from rdflib.namespace import OWL, RDF
        subject = URIRef(iri)

        def body(g):
            """Everything that is not the header, as a graph of its own.

            owl:imports is the exception: it carries the ontology's own
            subject but is not metadata, and losing it breaks every model
            that builds on this file, so it is compared along with the body.

            The header is the ontology's own statements plus the annotation
            property declarations that go with them, which carry a subject of
            their own but belong to the same block.
            """
            out = Graph()
            for triple in g:
                if triple[0] == subject and triple[1] != OWL.imports:
                    continue
                if triple[1] == RDF.type and triple[2] == OWL.AnnotationProperty:
                    continue
                out.add(triple)
            return out

        # Compared for isomorphism rather than equality: the anonymous class
        # expressions of the domains and ranges are blank nodes, and those are
        # given fresh identifiers on every parse.
        if not isomorphic(body(before), body(after)):
            print(f"  REFUSED {directory.parent.name}/{directory.name}: "
                  "the body of the file would change")
            return False
    except ImportError:
        print("  rdflib not available, writing without the check")

    if check:
        print(f"  would rewrite {directory.parent.name}/{directory.name}")
        return True

    ttl.write_text(new_text, encoding="utf-8")
    print(f"  OK {directory.parent.name}/{directory.name}: {ttl.name}, "
          f"{len(lines)} values")
    return True


def versions(package=None, version=None):
    want = None if version is None else (
        version if version.startswith("v") else "v" + version)
    out = []
    for base in SEARCH_DIRS:
        if not base.is_dir():
            continue
        for pkg in sorted(base.iterdir()):
            if not pkg.is_dir():
                continue
            if package and package.lower() not in pkg.name.lower():
                continue
            for v in sorted(pkg.iterdir()):
                if v.is_dir() and VERSION_RE.match(v.name) \
                        and (want is None or v.name == want):
                    out.append(v)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", default=None)
    ap.add_argument("--version", default=None)
    ap.add_argument("--check", action="store_true",
                    help="say what would change without writing")
    args = ap.parse_args()

    dirs = versions(args.package, args.version)
    if not dirs:
        sys.exit("no version directories found")

    failed = 0
    for d in dirs:
        if not apply(d, args.check):
            failed += 1
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
