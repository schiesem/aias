# Testing the AIAS ontology design patterns

How the tests work, why they are shaped this way, and how to add a package.

## Why five kinds of check

A single reasoner run proves very little. An ontology with no axioms is
consistent, answers no question, and passes any naive test. The five checks
below are ordered so that each rules out a different way of being wrong.

| Check | What it rules out |
|---|---|
| 1. Syntax | the file does not parse at all |
| 2. Profile | the ontology leaves OWL 2 DL, so reasoners may refuse or diverge |
| 3. Consistency | the axioms contradict each other on a realistic model |
| 4. Negative | **the axioms are toothless.** A model violating a constraint must be rejected. Without this, checks 1 to 3 pass on an ontology that constrains nothing |
| 5. Competency | the pattern cannot answer the questions it was built for |

Check 4 is the one most often missing in practice and the one that carries the
most weight. Each negative model isolates exactly one axiom, so a failure names
its own cause.

## Package layout

The runner discovers any version directory under `odps/<name>/v<version>/` or
`alignment/<name>/` that holds a
`tests/` subdirectory:

```
odps/<name>/
  <NAME>.ttl            the ontology
  CQ_<NAME>.md          competency questions, numbered
  TESTMODEL.md          the test scenario, what it proves, known gaps
  tests/
    data/*.ttl          positive models
    negative/*.ttl      models that must be rejected
    queries/*.rq        competency questions as SPARQL
    expected/*.json     recorded results
```

Query files are numbered after the competency question catalogue, so
`cq22_assignment_level.rq` answers question 22 of `CQ_VDI3682.md`. Not every
question needs a query: those whose answer the pattern deliberately cannot give
are better left out with a note in the catalogue than answered wrongly.

## Running

```bash
pip install rdflib
export ROBOT_JAR=/path/to/robot.jar    # https://github.com/ontodev/robot

python shared/run_tests.py                      # everything
python shared/run_tests.py --package vdi3682    # one package
python shared/run_tests.py --list               # what is discovered
python shared/run_tests.py --update-expected    # re-record expectations
```

Requires Java 11 or later for ROBOT, which supplies the HermiT reasoner. The
runner exits non-zero if any check fails.

`--update-expected` overwrites the recorded results. **Only use it when a
change of results is intended**, and read the diff before committing.
Regenerating expectations to make a red test go green defeats the purpose of
having them.

## The results report

Every run regenerates `<package>/RESULTS.md`, which shows per question what was
asked, the query answering it, the result on every test case, and an
interpretation. It exists so that a reviewer can follow what the pattern
answers without running anything.

Responsibilities are split deliberately:

| Part | Source | Kept current by |
|---|---|---|
| question | `CQ_<NAME>.md` | the catalogue |
| query and its note | `tests/queries/*.rq` | the query file |
| results | `tests/expected/*.json` | the test run |
| interpretation | `interpretations.md` | written by hand |

Only the interpretation is written prose, and it lives in its own file rather
than in the report, so that regenerating never overwrites it. A question
without an entry is marked as missing in the report instead of being silently
omitted.

Empty results are reported as `*(empty)*` rather than dropped, since an empty
result is an assertion: that question 15 returns nothing on every case is what
establishes that no elementary operator lacks a resource.

Generate it by hand with:

```bash
python shared/make_results.py --package vdi3682
```

## Visual inspection

The ontology itself is best inspected through the WebVOWL visualisation that
Widoco generates alongside the documentation. See `DOCUMENTATION.md`.

That view shows the T-Box, meaning classes and properties. It does not show the
individuals of a test model, because VOWL represents individuals only as an
instance count on the class node. Debugging a test model therefore happens
through the competency questions: a query result names exactly which relation is
missing, which is the same information a diagram would carry and is checked
automatically on every run.

## Imports are merged locally

The patterns carry `https://w3id.org/aias/...` IRIs, which do not resolve until
the w3id redirect is filed. The runner therefore strips `owl:imports` from a
test model and concatenates the ontology files instead, following imports
transitively so that an alignment model pulls in the patterns its ontology
imports as well. Once the redirect is live, `resolve_imports()` can be reduced
to a passthrough.

## Adding a package

1. **Write the ontology.** Every class and property needs `rdfs:label` and
   `rdfs:comment`, otherwise Widoco produces empty entries. Record design
   decisions and deviations from the standard in `skos:note` at the affected
   element, not only in prose.

2. **Write the competency questions** as `CQ_<NAME>.md`, numbered from 01, in
   the format: ID, question, answer, restriction, note. The note carries the
   clause of the standard where one exists.

3. **Write one positive model** under `tests/data/`. Prefer one realistic
   scenario over several fragments, so the model doubles as documentation.
   Exercise every construct the pattern claims to support, and nothing it does
   not.

4. **Write `TESTMODEL.md`.** It explains the scenario, states per construct what
   it puts under test, names what the reasoner adds over what is asserted, and
   records the known and intended gaps. This document is what makes a test model
   reviewable by someone who did not write it.

5. **Write negative models**, one per axiom worth defending, each violating
   exactly one axiom. Name the normative basis in `TESTMODEL.md`.

6. **Turn the questions into queries** under `tests/queries/`.

7. **Run with `--update-expected`, then read every recorded result** and check
   it against what the standard says. An expectation recorded without reading it
   freezes whatever bug produced it.

## Continuous integration

```yaml
- run: pip install rdflib
- run: curl -sL -o robot.jar https://github.com/ontodev/robot/releases/latest/download/robot.jar
- run: ROBOT_JAR=robot.jar python infomodels/shared/run_tests.py
```
