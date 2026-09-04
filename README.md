# AIAS Ontologies

AIAS is an information model for describing artificial intelligence
applications in automated plants, together with the plant they run in and the
technical process they observe or steer. It consists of four ontology design
patterns, one per subdomain, and an alignment ontology tying them together.

Each pattern formalises the terminology of a standard. The alignment rests on
design decisions and is the only part that is not normative.

## Key Features

The model captures what is needed to state where an AI application sits in a
plant and what it acts on. It covers the following key features:

* Describes the technical process, the communication, the control and the
  artificial intelligence of a plant in one connected model
* Places a process step and an inference under one function class, so a single
  assignment states which resource carries out which function, whichever
  subdomain that function comes from
* Distinguishes open-loop from closed-loop control by structure rather than by
  name, following the action path and action of IEC 60050-351
* Records the direction of a communication, so a model can say which component
  sends and which receives
* Traces a model back to the data it was trained on and to the device that
  recorded that data
* Each pattern is usable on its own and is imported by the alignment through
  its versioned IRI

## The patterns

| Package | Standard | IRI | Documentation | Visualization |
|---|---|---|---|---|
| VDI 3682 ODP | VDI/VDE 3682 | `w3id.org/aias/odp/vdi3682` | [![Documentation](https://img.shields.io/badge/Documentation-Ontology_Specification-blue.svg)](https://w3id.org/aias/odp/vdi3682/1.0.0) | [![WebVowl](https://img.shields.io/badge/Visualize_with-WebVowl-blue.svg)](https://schiesem.github.io/aias/odps/vdi3682/v1.0.0/docs/webvowl/index.html#) |
| ISO/IEC 7498-1 ODP | ISO/IEC 7498-1 | `w3id.org/aias/odp/iso7498` | [![Documentation](https://img.shields.io/badge/Documentation-Ontology_Specification-blue.svg)](https://w3id.org/aias/odp/iso7498/1.0.0) | [![WebVowl](https://img.shields.io/badge/Visualize_with-WebVowl-blue.svg)](https://schiesem.github.io/aias/odps/iso7498/v1.0.0/docs/webvowl/index.html#) |
| ISO/IEC 22989 ODP | ISO/IEC 22989 | `w3id.org/aias/odp/iso22989` | [![Documentation](https://img.shields.io/badge/Documentation-Ontology_Specification-blue.svg)](https://w3id.org/aias/odp/iso22989/1.0.0) | [![WebVowl](https://img.shields.io/badge/Visualize_with-WebVowl-blue.svg)](https://schiesem.github.io/aias/odps/iso22989/v1.0.0/docs/webvowl/index.html#) |
| IEC 60050-351 ODP | IEC 60050-351 | `w3id.org/aias/odp/iec60050` | [![Documentation](https://img.shields.io/badge/Documentation-Ontology_Specification-blue.svg)](https://w3id.org/aias/odp/iec60050/1.0.0) | [![WebVowl](https://img.shields.io/badge/Visualize_with-WebVowl-blue.svg)](https://schiesem.github.io/aias/odps/iec60050/v1.0.0/docs/webvowl/index.html#) |
| AIAS Alignment | — | `w3id.org/aias` | [![Documentation](https://img.shields.io/badge/Documentation-Ontology_Specification-blue.svg)](https://w3id.org/aias/1.0.0) | [![WebVowl](https://img.shields.io/badge/Visualize_with-WebVowl-blue.svg)](https://schiesem.github.io/aias/alignment/aias/v1.0.0/docs/webvowl/index.html#) |

Every IRI resolves through [w3id.org](https://w3id.org) by content
negotiation: a browser is served the documentation, a reasoner the ontology as
JSON-LD, RDF/XML, N-Triples or Turtle, whichever it asks for.

## Versions

**Version 1.0.0 is the stable one.** It is the model the ETFA paper and the
dissertation both rest on, and it is what an IRI without a version number
resolves to.

| IRI | Resolves to |
|---|---|
| `https://w3id.org/aias` | the alignment, currently 1.0.0 |
| `https://w3id.org/aias/1.0.0` | the alignment, that version, for good |
| `https://w3id.org/aias/odp/<name>` | a pattern, currently 1.0.0 |
| `https://w3id.org/aias/odp/<name>/<version>` | a pattern, that version, for good |

Version 2.0.0 is a reworking and is still being written. It is reachable under
its own IRI, and the unversioned IRI moves to it once it is released.

Each package holds its versions in directories of their own. A version is a
maintained branch rather than a frozen copy: a model written against `v1.0.0`
keeps working, and that version may still receive a `v1.0.1`.

**Import the versioned IRI, never the bare one.** Two versions of a pattern
share the ontology IRI and differ only in their version IRI, so an import
naming the bare IRI is ambiguous and follows whatever the current version
happens to be:

```turtle
@prefix vdi3682: <https://w3id.org/aias/odp/vdi3682#> .

<https://example.org/my-plant>
    a owl:Ontology ;
    owl:imports <https://w3id.org/aias/odp/vdi3682/1.0.0> .
```

Note the difference between the two. The **namespace** of the prefix carries a
`#` and no version, so `vdi3682:ProcessOperator` means the same in every
version. The **import** names a version and no `#`, since it has to say which
one applies.

## Documentation

The ontology specifications were generated with the help of the
[WIDOCO](https://github.com/dgarijo/Widoco) wizard. The hand written sections
live in `<package>/v<version>/doc/` as Markdown and are the source: the
generated HTML is never edited.

## Working on the ontologies

```
python shared/run_tests.py             # syntax, OWL 2 DL, reasoning, queries
python shared/apply_metadata.py        # metadata.md into the Turtle headers
python shared/make_docs.py --serve     # Widoco, then serve on port 8899
python shared/make_figures.py          # PlantUML diagrams
```

Metadata is written into the Turtle headers from Markdown, never by hand:
`shared/metadata.md` carries what every package shares, each
`<package>/v<version>/doc/metadata.md` what belongs to that one.

The three `.jar` files the tools need are not in the repository. See
[`shared/README.md`](shared/README.md) for where to fetch them.

## How to cite

If you want to use these ontologies in your own research, please cite as:

```
Schieseck, M., Topalis, P., Reinpold, L., Gehlhoff, F., & Fay, A. (2024).
A Formal Model for Artificial Intelligence Applications in Automation Systems.
2024 IEEE 29th International Conference on Emerging Technologies and Factory
Automation (ETFA), Padova, Italy. IEEE. https://doi.org/10.1109/ETFA61755.2024.10710890
```

and, once it is published:

```
Schieseck, M. (to be published). [Dissertation title].
Helmut-Schmidt-Universität / Universität der Bundeswehr Hamburg.
```

If you are using a BiBTeX file, you can copy the following:

```
@inproceedings{Schieseck2024FormalModel,
  author    = {Marvin Schieseck and Philip Topalis and Lasse Reinpold and
               Felix Gehlhoff and Alexander Fay},
  title     = {A Formal Model for Artificial Intelligence Applications in
               Automation Systems},
  booktitle = {2024 IEEE 29th International Conference on Emerging Technologies
               and Factory Automation (ETFA)},
  year      = {2024},
  address   = {Padova, Italy},
  month     = sep,
  publisher = {IEEE},
  DOI       = {10.1109/ETFA61755.2024.10710890}
}
```

```
@phdthesis{SchieseckDissertation,
  author = {Marvin Schieseck},
  title  = {[Dissertation title]},
  school = {Helmut-Schmidt-Universität / Universität der Bundeswehr Hamburg},
  note   = {to be published}
}
```

[![DOI](https://img.shields.io/badge/DOI-10.1109/ETFA61755.2024.10710890-blue.svg)](https://doi.org/10.1109/ETFA61755.2024.10710890)

## License

All resources are licensed under Creative Commons Attribution 4.0
International.

[![License](https://img.shields.io/badge/License-CC_BY_4.0-blue.svg)](https://creativecommons.org/licenses/by/4.0/)

The definitions quoted in the ontologies are taken from the standards each
pattern rests on. Those standards are copyright of their issuing bodies and are
not distributed here. Every element carries a `skos:note` naming the clause it
comes from, so a reader can go back to the source.

## Funding

This research is funded by dtec.bw – Digitalization and Technology Research
Center of the Bundeswehr. dtec.bw is funded by the European Union –
NextGenerationEU
