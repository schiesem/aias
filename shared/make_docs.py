#!/usr/bin/env python3
"""Generate Widoco documentation for the AIAS ontology design patterns.

Widoco produces the human readable documentation and, with -webVowl, the
WebVOWL visualisation of the same ontology in one run. The visualisation is
linked from the generated index page, so both are published together.

For each package under odps/ and alignment/ the documentation is written to
<package>/docs/, ready to be served from GitHub Pages at
https://schiesem.github.io/aias/<package>/v<version>/.

Requires: widoco.jar, reachable via WIDOCO_JAR or in this directory. Download
the JDK 17 build from https://github.com/dgarijo/Widoco/releases

Usage:
    python shared/make_docs.py [--package vdi3682] [--serve]
"""

import argparse
import os
import subprocess
import sys
import shutil
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


def _dirs(version=None):
    """The search directories, optionally restricted to one version."""
    if version is None:
        return SEARCH_DIRS
    want = version if version.startswith("v") else "v" + version
    return [d for d in SEARCH_DIRS if d.parent.name == want]


WIDOCO = os.environ.get("WIDOCO_JAR", str(HERE / "widoco.jar"))

# Widoco pulls in Jena and the OWL API, which touch JDK internals that are
# sealed from Java 16 onwards.
JAVA_OPTS = [
    "--add-opens", "java.base/java.lang=ALL-UNNAMED",
    "--add-opens", "java.base/java.lang.reflect=ALL-UNNAMED",
    "--add-opens", "java.base/java.util=ALL-UNNAMED",
]


def packages(only=None, version=None):
    """Each package with the ontologies to document.

    A package may hold more than one ontology file, for instance a pattern and
    its named individuals. The pattern is the one whose file name carries no
    suffix; taking the first file alphabetically would pick the companion,
    since ISO7498-instances.ttl sorts before ISO7498.ttl.

    Both are documented, the pattern into docs/ and each companion into a
    subdirectory of its own, so the vocabulary is browsable as well.
    """
    found = []
    for d in _versions(version):
        # d is the version directory; the package name is its parent.
        if only is not None and only.lower() not in d.parent.name.lower():
            continue
        ttls = sorted(d.glob("*.ttl"))
        if not ttls:
            continue
        plain = [p for p in ttls if "-" not in p.stem]
        ontology = (plain or ttls)[0]
        found.append((d, ontology, "docs"))
        for companion in (p for p in ttls if p != ontology):
            suffix = companion.stem.split("-", 1)[-1].lower()
            found.append((d, companion, f"docs-{suffix}"))
    return found


# The hand written sections. Widoco reads them from a sections/ directory next
# to the ontology and drops its own placeholder text for each one it finds.
# The abstract is not among them: it lives in the ontology header as
# dcterms:abstract, so that it travels with the Turtle file.
SECTIONS = ["introduction", "description"]


def _md(text: str) -> str:
    """Markdown to HTML, for the subset the hand written sections use.

    Headings, paragraphs, blockquotes, fenced and inline code, bold, italics
    and links. Writing this out is shorter than taking a dependency, and it
    fails loudly on anything it does not know rather than silently dropping it.
    """
    import html as _html

    def inline(s):
        out, i, n = [], 0, len(s)
        while i < n:
            c = s[i]
            if c == "`":
                j = s.find("`", i + 1)
                if j == -1:
                    out.append(_html.escape(c)); i += 1; continue
                out.append("<code>" + _html.escape(s[i + 1:j]) + "</code>")
                i = j + 1
            elif s.startswith("**", i):
                j = s.find("**", i + 2)
                if j == -1:
                    out.append("**"); i += 2; continue
                out.append("<strong>" + inline(s[i + 2:j]) + "</strong>")
                i = j + 2
            elif c == "[":
                j = s.find("](", i)
                k = s.find(")", j) if j != -1 else -1
                if j == -1 or k == -1:
                    out.append("["); i += 1; continue
                out.append(f'<a href="{_html.escape(s[j+2:k], quote=True)}">'
                           + inline(s[i+1:j]) + "</a>")
                i = k + 1
            else:
                out.append(_html.escape(c)); i += 1
        return "".join(out)

    # The comment header every hand written section carries is not content.
    while "<!--" in text:
        a = text.index("<!--")
        b = text.find("-->", a)
        if b == -1:
            text = text[:a]
            break
        text = text[:a] + text[b + 3:]

    html, para, quote, table, items = [], [], [], [], []
    fence, code = False, []

    def flush_items():
        """One list, with each entry joined back out of its wrapped lines."""
        if not items:
            return
        html.append("<ul>" + "".join(f"<li>{inline(' '.join(i))}</li>"
                                     for i in items) + "</ul>")
        items.clear()

    def flush_table():
        """A pipe table. The second row is the alignment rule and is dropped."""
        if not table:
            return
        rows = [[c.strip() for c in r.strip().strip("|").split("|")]
                for r in table]
        table.clear()
        body = rows[2:] if len(rows) > 1 and set("".join(rows[1])) <= set("-: ") \
            else rows[1:]
        head = "".join(f"<th>{inline(c)}</th>" for c in rows[0])
        out = [f"<table><thead><tr>{head}</tr></thead><tbody>"]
        for row in body:
            out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in row)
                       + "</tr>")
        out.append("</tbody></table>")
        html.append("".join(out))

    def flush():
        if para:
            html.append("<p>" + inline(" ".join(para)) + "</p>")
            para.clear()
    def flush_quote():
        if quote:
            html.append("<blockquote>" + inline(" ".join(quote))
                        + "</blockquote>")
            quote.clear()

    for raw in text.splitlines():
        line = raw.rstrip()
        # A fenced code block is copied through verbatim, so that Turtle in
        # the text stays readable rather than being escaped word by word.
        if line.lstrip().startswith("```"):
            if fence:
                html.append("<pre><code>"
                            + _html.escape("\n".join(code))
                            + "</code></pre>")
                code.clear()
            else:
                flush(); flush_quote(); flush_table(); flush_items()
            fence = not fence
            continue
        if fence:
            code.append(raw)
            continue
        if not line.strip():
            flush(); flush_quote(); flush_table(); flush_items(); continue
        if line.lstrip().startswith("|"):
            flush(); flush_quote()
            table.append(line)
            continue
        flush_table()
        if line.lstrip().startswith("- "):
            flush(); flush_quote()
            items.append([line.lstrip()[2:].strip()])
            continue
        if items and line.startswith("  "):
            # a wrapped line belongs to the entry above it
            items[-1].append(line.strip())
            continue
        flush_items()
        if line.startswith("#"):
            flush(); flush_quote()
            lvl = len(line) - len(line.lstrip("#"))
            # Widoco writes the section heading itself as h2, so ## in the
            # source becomes h3, one level below it.
            n = min(lvl + 1, 6)
            html.append(f"<h{n}>{inline(line.lstrip('# ').strip())}</h{n}>")
        elif line.startswith(">"):
            flush()
            quote.append(line.lstrip("> ").strip())
        else:
            flush_quote()
            para.append(line.strip())
    flush(); flush_quote(); flush_table(); flush_items()
    return "\n".join(html)


def fix_webvowl(directory: Path, out: Path) -> list:
    """Rewrite webvowl/data/ontology.json as UTF-8, authors in paper order.

    Widoco writes the file in the platform encoding, so one en dash from the
    funding statement leaves WebVOWL with a file it cannot decode. The author
    list carries no order at all, since RDF triples are a set.
    """
    import json
    import re as _re

    data = out / "webvowl" / "data" / "ontology.json"
    if not data.is_file():
        return []

    raw = data.read_bytes()
    for enc in ("utf-8", "cp1252", "latin-1"):
        try:
            doc = json.loads(raw.decode(enc))
            break
        except (UnicodeDecodeError, json.JSONDecodeError):
            continue
    else:
        return []

    md = directory / "doc" / "metadata.md"
    authors = []
    if md.is_file():
        text = md.read_text(encoding="utf-8")
        while "<!--" in text:
            a = text.index("<!--")
            b = text.find("-->", a)
            text = text[:a] + (text[b + 3:] if b != -1 else "")
        m = _re.search(r"^creator:[ \t]*\n((?:  +.*\n)+)", text, _re.M)
        if m:
            authors = [line.strip().split("|")[0].strip()
                       for line in m.group(1).splitlines() if line.strip()]

    changed = False
    other = doc.get("header", {}).get("other", {})
    for key in ("author", "creator"):
        entries = other.get(key)
        if not (authors and isinstance(entries, list) and len(entries) > 1):
            continue

        def rank(entry):
            value = entry.get("value") if isinstance(entry, dict) else entry
            for i, name in enumerate(authors):
                if value == name:
                    return i
            return len(authors)

        ordered = sorted(entries, key=rank)
        if ordered != entries:
            other[key] = ordered
            changed = True

    # Written as UTF-8 either way: the file may have been readable only
    # because it happened to carry no character outside ASCII this time.
    data.write_text(json.dumps(doc, ensure_ascii=False, indent=2),
                    encoding="utf-8")
    return ["webvowl"] if changed else ["webvowl encoding"]



def fix_serializations(directory: Path, ontology: Path, out: Path) -> list:
    """Put the ontology header of the source back into what Widoco emitted.

    Widoco resolves owl:imports while it works and lets the header of the last
    ontology it read win, so the serializations it writes can carry the IRI of
    an import rather than of the ontology itself. These files are what a
    reasoner downloads, so the defect is not cosmetic: an alignment that names
    itself after one of its imports cannot be loaded at all.
    """
    from rdflib import Graph, URIRef
    from rdflib.namespace import OWL, RDF

    # Read as text and normalised first: under Windows the working copy
    # has CRLF endings, and inside a multi-line literal the carriage
    # return becomes part of the text rather than of the file format.
    src = Graph()
    src.parse(data=ontology.read_text(encoding="utf-8").replace("\r\n", "\n"),
              format="turtle")
    subject = next(src.subjects(RDF.type, OWL.Ontology), None)
    if subject is None:
        return []
    want = {p: set(src.objects(subject, p))
            for p in (OWL.versionIRI, OWL.imports)}
    # rdflib binds only the prefixes it knows, so a file it writes
    # loses the ones that make it readable: aias:, vdi3682: and the
    # rest, with bibo: turning into ns1:.
    # Only what the source declares: rdflib carries dozens of bindings of
    # its own, brick and csvw among them, which have nothing to do with this
    # ontology and would clutter every file written through it.
    declared = {line.split()[1].rstrip(":")
                for line in ontology.read_text(encoding="utf-8").splitlines()
                if line.startswith("@prefix")}
    prefixes = [(p, ns) for p, ns in src.namespaces() if p in declared]

    fixed = []
    for name, fmt in (("ontology.ttl", "turtle"), ("ontology.owl", "xml"),
                      ("ontology.nt", "nt"), ("ontology.jsonld", "json-ld")):
        f = out / name
        if not f.is_file():
            continue
        g = Graph()
        try:
            text = f.read_text(encoding="utf-8").replace("\r\n", "\n")
            g.parse(data=text, format=fmt)
        except Exception:
            continue

        wrong = [s for s in g.subjects(RDF.type, OWL.Ontology) if s != subject]
        # Every file is rewritten, not only a misnamed one: the prefixes have
        # to be set even where the header is already right, and rewriting a
        # graph through rdflib loses nothing.
        #
        # Move every statement of a misnamed ontology onto the right subject,
        # then restore the header from the source.
        for s in wrong:
            for pred, obj in list(g.predicate_objects(s)):
                g.remove((s, pred, obj))
                if pred not in (OWL.versionIRI, OWL.imports):
                    g.add((subject, pred, obj))
        g.add((subject, RDF.type, OWL.Ontology))
        for pred in (OWL.versionIRI, OWL.imports):
            for obj in list(g.objects(subject, pred)):
                g.remove((subject, pred, obj))
            for obj in want[pred]:
                g.add((subject, pred, obj))

        for prefix, ns in prefixes:
            g.bind(prefix, ns, replace=True)
        g.serialize(destination=str(f), format=fmt)

        # RDF/XML keeps only the namespaces rdflib needs to abbreviate an
        # element name, and every class here is written out in full, so the
        # bindings above are dropped again. Protege reads this serialization,
        # so they are written into the rdf:RDF header by hand.
        if fmt == "xml":
            head = f.read_text(encoding="utf-8")
            end = head.find(">", head.find("<rdf:RDF"))
            if end != -1:
                opening = head[:end]
                missing = "".join(
                    f'\n   xmlns:{prefix}="{ns}"'
                    for prefix, ns in prefixes
                    if prefix and f'xmlns:{prefix}=' not in opening)
                if missing:
                    f.write_text(opening + missing + head[end:],
                                 encoding="utf-8")
        fixed.append(name.split(".")[-1])

    return ["header: " + ", ".join(fixed)] if fixed else []



def write_references(directory: Path, out: Path) -> list:
    """Replace Widoco's placeholder References section with the real ones.

    The entries come from the references field of metadata.md, which is also
    what apply_metadata.py writes into the header as dcterms:references, so
    the two cannot drift apart.
    """
    import html as _html
    import re as _re

    md = directory / "doc" / "metadata.md"
    sec = out / "sections" / "references-en.html"
    if not md.is_file() or not sec.is_file():
        return []

    text = md.read_text(encoding="utf-8")
    while "<!--" in text:
        a = text.index("<!--")
        b = text.find("-->", a)
        text = text[:a] + (text[b + 3:] if b != -1 else "")

    m = _re.search(r"^references:[ \t]*\n((?:  +.*\n)+)", text, _re.M)
    if not m:
        return []
    entries = [line.strip() for line in m.group(1).splitlines() if line.strip()]
    if not entries:
        return []

    items = "".join("<li>" + _html.escape(e) + "</li>" for e in entries)
    sec.write_text(
        '\n<h2 id="ref" class="list">References '
        '<span class="backlink"> back to <a href="#toc">ToC</a></span></h2>\n'
        '<ul>' + items + '</ul>\n', encoding="utf-8")
    return ["references"]


def write_sections(directory: Path, out: Path) -> list:
    """Replace Widoco's placeholder sections with the hand written ones.

    Widoco writes each section as its own file under sections/ and the index
    pulls them in, so overwriting a file there is enough: no second run, and no
    editing of the index itself. Returns the names written.
    """
    doc = directory / "doc"
    sec = out / "sections"
    if not doc.is_dir() or not sec.is_dir():
        return []
    written = []
    for name in SECTIONS:
        src = doc / f"{name}.md"
        if not src.is_file():
            continue
        body = _md(src.read_text(encoding="utf-8")).strip()
        if not body:
            continue
        (sec / f"{name}-en.html").write_text(body + "\n", encoding="utf-8")
        written.append(name)
    return written



def fix_header(directory: Path, out: Path) -> list:
    """Add what Widoco leaves out of the generated page.

    Two things: the Latest version and Previous version rows of the header
    block, and the funding statement in the acknowledgements.

    Widoco fills those two from a configuration file rather than from the
    ontology, and -confFile is incompatible with -getOntologyMetadata, so it
    leaves both rows out entirely. The values are in doc/metadata.md and the
    Turtle carries them as dcterms:hasVersion and owl:priorVersion, so the
    rows are inserted here rather than dropping the information.

    Returns the rows added.
    """
    import re as _re

    def strip_comments(s):
        while "<!--" in s:
            a = s.index("<!--")
            b = s.find("-->", a)
            s = s[:a] + (s[b + 3:] if b != -1 else "")
        return s

    md = directory / "doc" / "metadata.md"
    if not md.is_file():
        return []
    # The package file first, so that a value set there wins over the shared
    # one, which is how apply_metadata.py reads them as well.
    text = strip_comments(md.read_text(encoding="utf-8"))
    shared = ROOT / "shared" / "metadata.md"
    if shared.is_file():
        text += chr(10) + strip_comments(shared.read_text(encoding="utf-8"))

    def field(name):
        # The value is on the key's own line, so a key with nothing after the
        # colon is empty. Without the negative lookahead the pattern would run
        # on and pick up the next key in the file.
        m = _re.search(rf"^{name}:[ 	]*(?!$)(\S+)[ 	]*$", text, _re.M)
        return m.group(1) if m else None

    def paragraph(name):
        """A field whose value may be wrapped over several indented lines."""
        m = _re.search(rf"^{name}:[ \t]*(.*(?:\n  +.*)*)", text, _re.M)
        if not m:
            return None
        value = " ".join(part.strip() for part in m.group(1).splitlines())
        return value.strip() or None

    latest, prior = field("latestVersion"), field("priorVersion")
    iri, version = field("iri"), field("version")
    funding = paragraph("rights")
    index = out / "index-en.html"
    if not index.is_file():
        return []

    html = index.read_text(encoding="utf-8")
    added = []

    anchor = "<dt>Revision:</dt>"
    if anchor in html and (latest or prior or iri):
        rows = ""
        # Widoco leaves out "This version" where the version IRI starts with
        # the ontology IRI, taking the two for the same thing. That is the
        # case for the alignment, whose IRI is the root of the namespace.
        if iri and version and "<dt>This version:</dt>" not in html:
            this = iri + "/" + version
            rows += ('<dt>This version:</dt>' + chr(10)
                     + '<dd><a href="' + this + '">' + this + '</a></dd>'
                     + chr(10))
            added.append("this")
        if latest:
            rows += (f'<dt>Latest version:</dt>\n'
                     f'<dd><a href="{latest}">{latest}</a></dd>\n')
            added.append("latest")
        if prior:
            rows += (f'<dt>Previous version:</dt>\n'
                     f'<dd><a href="{prior}">{prior}</a></dd>\n')
            added.append("previous")
        html = html.replace(anchor, rows + anchor, 1)

    # Widoco sorts the authors alphabetically, which turns the author order of
    # a paper into a lookup order. The list is put back into the order given
    # by metadata.md, where the first name is the first author.
    authors = []
    m = _re.search(r"^creator:[ \t]*\n((?:  +.*\n)+)", text, _re.M)
    if m:
        authors = [line.strip().split("|")[0].strip()
                   for line in m.group(1).splitlines() if line.strip()]
    if len(authors) > 1:
        block = _re.search(r"(<dt>Authors:</dt>\s*)((?:<dd>.*?</dd>\s*)+)",
                           html, _re.S)
        if block:
            cells = _re.findall(r"<dd>.*?</dd>", block.group(2), _re.S)
            def rank(cell):
                inner = _re.sub(r"<[^>]+>", "", cell).strip()
                for i, name in enumerate(authors):
                    if inner == name or inner in name or name in inner:
                        return i
                return len(authors)
            if len(cells) == len(authors):
                ordered = "".join(sorted(cells, key=rank))
                html = html.replace(block.group(0),
                                    block.group(1) + ordered + "\n", 1)
                added.append("author order")

    # A <dt> with no <dd> after it is a label Widoco wrote for a value the
    # ontology does not carry, such as "Cite as:" before a publication exists.
    empty = _re.findall(r"<dt>[^<]*:</dt>\s*(?=<dt>|</dl>)", html)
    for row in empty:
        html = html.replace(row, "", 1)
    if empty:
        added.append("dropped %d empty row%s"
                     % (len(empty), "" if len(empty) == 1 else "s"))

    # Widoco writes the acknowledgements section with a fixed text thanking
    # the authors of LODE and Widoco, and takes no funding statement of its
    # own. The funder requires theirs to appear, so it goes in ahead of that
    # text rather than in place of it: both belong there.
    ack = '<h2 id="ack" class="list">Acknowledgments'
    if funding and ack in html and "funding-statement" not in html:
        i = html.index(ack)
        j = html.index("</h2>", i) + len("</h2>")
        html = (html[:j]
                + f'\n<p class="funding-statement">{funding}</p>'
                + html[j:])
        added.append("funding")

    index.write_text(html, encoding="utf-8")
    return added



def generate(directory: Path, ontology: Path, outdir: str = "docs") -> bool:
    out = directory / outdir
    # Empty the directory rather than removing it. On Windows the folder
    # itself can be held open by an editor or a file browser, and rmtree then
    # fails on the last step after having deleted everything inside it.
    if out.exists():
        for item in out.iterdir():
            if item.is_dir():
                shutil.rmtree(item, ignore_errors=True)
            else:
                try:
                    item.unlink()
                except OSError:
                    pass
    else:
        out.mkdir(parents=True)

    cmd = ["java", *JAVA_OPTS, "-jar", WIDOCO,
           "-ontFile", str(ontology),
           "-outFolder", str(out),
           "-getOntologyMetadata",   # read dcterms and vann from the ontology
           "-webVowl",               # WebVOWL visualisation as a subpage
           "-includeAnnotationProperties",
           "-rewriteAll",
           "-lang", "en"]

    p = subprocess.run(cmd, capture_output=True, text=True, timeout=900)
    ok = (out / "index-en.html").exists()

    if not ok:
        print(f"  FAILED {directory.name}/{outdir}")
        for line in ((p.stdout or "") + (p.stderr or "")).splitlines()[-8:]:
            print(f"    {line}")
        return False

    # Only the pattern itself carries hand written sections; a companion
    # vocabulary of named individuals is documented from the ontology alone.
    sections = write_sections(directory, out) if outdir == "docs" else []
    if outdir == "docs":
        sections += fix_serializations(directory, ontology, out)
        sections += write_references(directory, out)
        sections += fix_webvowl(directory, out)
        sections += fix_header(directory, out)

    n_vowl = len(list((out / "webvowl" / "data").glob("*.json"))) \
        if (out / "webvowl" / "data").is_dir() else 0
    size = sum(f.stat().st_size for f in out.rglob("*") if f.is_file())
    print(f"  OK {directory.parent.name}/{directory.name}: {outdir}/index-en.html"
          f"  ({ontology.name}, webvowl: {'yes' if n_vowl else 'no'}, "
          f"sections: {', '.join(sections) if sections else 'none'}, "
          f"{size // 1024} KB)")
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--version", default=None,
                    help="restrict to one published version, e.g. 1.0")
    ap.add_argument("--package", default=None,
                    help="restrict to one package, e.g. vdi3682")
    ap.add_argument("--serve", action="store_true",
                    help="serve the generated documentation on port 8899")
    args = ap.parse_args()

    if not Path(WIDOCO).exists():
        sys.exit(f"widoco.jar not found at {WIDOCO}\n"
                 "Set WIDOCO_JAR, or download the JDK 17 build from\n"
                 "https://github.com/dgarijo/Widoco/releases")

    pkgs = packages(args.package, args.version)
    if not pkgs:
        sys.exit("no packages found")

    print(f"Widoco: {WIDOCO}")
    failed = 0
    for d, onto, outdir in pkgs:
        if not generate(d, onto, outdir):
            failed += 1

    if args.serve and not failed:
        import http.server, socketserver, functools
        os.chdir(ROOT)
        handler = functools.partial(http.server.SimpleHTTPRequestHandler,
                                    directory=str(ROOT))
        print(f"\nServing {ROOT} on http://127.0.0.1:8899")
        for d, _, outdir in pkgs:
            rel = d.relative_to(ROOT).as_posix()
            print(f"  http://127.0.0.1:8899/{rel}/{outdir}/index-en.html")
        with socketserver.TCPServer(("127.0.0.1", 8899), handler) as httpd:
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("\nstopped")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
