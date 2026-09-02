# Generating the documentation

Widoco produces the human readable documentation of an ontology and, in the
same run, the WebVOWL visualisation of it. Both are published together: the
generated index page links to the visualisation as a subpage.

This is the arrangement used by comparable published patterns, for example
https://doernern.github.io/MQTT4SSNOntology/documentation/index-en.html

## Setup

Download the JDK 17 build of Widoco and place it in this directory:

```bash
curl -sL -o shared/widoco.jar \
  https://github.com/dgarijo/Widoco/releases/download/v1.4.25/widoco-1.4.25-jar-with-dependencies_JDK-17.jar
```

The jar is 40 MB and is deliberately not under version control. Set
`WIDOCO_JAR` to keep it elsewhere. Java 11 or later is required.

## Running

From VS Code, press `Ctrl+Shift+P` and pick **Tasks: Run Task**:

| Task | What it does |
|---|---|
| Ontology: build and serve documentation | regenerate everything, then keep serving |
| Ontology: open documentation in Firefox | open a page in a new tab, asks which pattern |
| Ontology: build documentation | regenerate only |
| Ontology: build documentation (one pattern) | asks which pattern |
| Ontology: serve documentation | serve what is already generated |
| Ontology: fetch tools | one-off download of the two jars |

The combined task is the default build task, so `Ctrl+Shift+B` runs it. It
leaves the server running in its terminal panel, so run the Firefox task
afterwards, or whenever you want a second page open.

From a terminal:

```bash
python shared/make_docs.py                   # every package
python shared/make_docs.py --package vdi3682 # one package
python shared/make_docs.py --serve           # generate, then serve on :8899
```

Either way the result is at

```
http://127.0.0.1:8899/odps/vdi3682/v2.0.0/docs/index-en.html
```

The documentation page itself would also open by double click, but WebVOWL
loads its data by fetch, which a browser blocks over `file://`. That is why the
server is needed to see the visualisation.

Output goes to `<package>/docs/`:

```
odps/vdi3682/v2.0.0/docs/
  index-en.html          the documentation
  ontology.ttl           the ontology, alongside .owl, .nt and .jsonld
  webvowl/               WebVOWL, with data/ontology.json
  provenance/  resources/
```

## What ends up in the documentation

Everything comes from the ontology file itself, which is why the annotations
there matter:

| In the ontology | In the documentation |
|---|---|
| `dcterms:title`, `dcterms:description` | title and abstract |
| `dcterms:creator`, `contributor`, `publisher` | authorship block |
| `dcterms:license` | licence notice |
| `owl:versionIRI`, `owl:versionInfo` | version banner |
| `vann:preferredNamespacePrefix` | namespace declaration |
| `rdfs:label` | the readable name of every term |
| `rdfs:comment` | the definition of every term |
| `skos:note` | the normative source and the design decisions |

A term without `rdfs:label` and `rdfs:comment` appears as an empty entry, which
is why the test runner treats missing ones as a defect.

The `TODO` placeholders in the metadata are visible in the generated page. They
have to be replaced before publication: author names with ORCID, institution,
funding statement, and the citation of the accompanying publication.

## Publishing

The `docs/` directories are ready to be served from GitHub Pages:

```
https://schiesem.github.io/aias/odps/vdi3682/v2.0.0/docs/index-en.html
```

The w3id redirect then points the permanent ontology IRI at that location,
serving the documentation to a browser and the Turtle file to a tool, based on
the Accept header.
