# Tools

Everything here works on all packages at once, so a check or a rebuild covers
the whole model rather than one pattern.

| Script | What it does | Detail |
|---|---|---|
| `run_tests.py` | syntax, OWL 2 DL profile, reasoning, competency questions, A-box check | [TESTING.md](TESTING.md) |
| `apply_metadata.py` | writes the metadata.md values into the Turtle headers | below |
| `make_docs.py` | Widoco documentation and WebVOWL, one per package version | [DOCUMENTATION.md](DOCUMENTATION.md) |
| `make_figures.py` | renders the PlantUML diagrams | [FIGURES.md](FIGURES.md) |
| `make_results.py` | writes RESULTS.md from the recorded query results | [TESTING.md](TESTING.md) |

Each takes `--package` and `--version` to work on one package only.

## The jar files

Three Java tools are needed and none is in the repository, together they are
about 140 MB. Put them in this directory, or point the environment variable
named beside each one at them.

| File | Version | Where from | Variable |
|---|---|---|---|
| `robot.jar` | 1.9.x | [ROBOT releases](https://github.com/ontodev/robot/releases) | `ROBOT_JAR` |
| `widoco.jar` | JDK 17 build | [Widoco releases](https://github.com/dgarijo/Widoco/releases) | `WIDOCO_JAR` |
| `plantuml.jar` | 1.2024 or later | [PlantUML downloads](https://plantuml.com/download) | `PLANTUML_JAR` |

Java 17 or later is required. Widoco pulls in Jena and the OWL API, which touch
JDK internals sealed from Java 16 onwards, so `make_docs.py` passes the
`--add-opens` flags they need.

Python needs `rdflib`. Nothing else.

## Metadata

The Turtle headers are generated, never edited by hand. Two Markdown files feed
them:

- `shared/metadata.md` carries what every package shares: author, publisher,
  funding, licence, repository
- `<package>/v<version>/doc/metadata.md` carries what belongs to that one:
  title, IRI, version, abstract, keywords, citation

A package overrides a shared value by setting the same key.

`apply_metadata.py` rewrites only the ontology header and then checks the
result with rdflib: if anything outside the header changed, it refuses to
write. The comparison is for isomorphism rather than equality, since the
anonymous class expressions used as domains and ranges are blank nodes and get
fresh identifiers on every parse.

`owl:imports` is carried over verbatim. It sits inside the ontology statement
but is not metadata, and an alignment that lost its imports would still parse
while no longer finding the classes it refers to.

## What make_docs.py adds after Widoco

Widoco leaves out or garbles a few things, and the script repairs them rather
than accepting them:

- the hand written `introduction.md` and `description.md` replace the
  placeholder sections
- the References section is filled from the `references` field
- `This version` and `Latest version` are added to the header block, which
  Widoco fills from a configuration file that is incompatible with
  `-getOntologyMetadata`
- the authors are put back into the order metadata.md gives, since RDF triples
  carry none
- `webvowl/data/ontology.json` is rewritten as UTF-8, which it is not: one en
  dash from the funding statement leaves WebVOWL unable to read the file at all
- the funding statement is placed in the acknowledgements, ahead of Widoco's
  own thanks to the authors of LODE and Widoco
- header rows Widoco writes without a value are dropped
