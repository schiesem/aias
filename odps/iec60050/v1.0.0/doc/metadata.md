# Metadata: IEC 60050-351 Ontology Design Pattern

**This is version 1.0.0**, the first release of this pattern.

What is the same for every package lives in `shared/metadata.md`: publisher,
funding, licence, repository. The authors and the citation are here, because
each ontology belongs to a paper of its own.

`shared/apply_metadata.py` writes these into the ontology header.
**Edit here, never in the Turtle.**

---

## People

<!-- dcterms:creator — the authors of the paper this ontology belongs to. One
     per line, indented by two spaces. An ORCID is appended as
     "Name | https://orcid.org/…" and is then written as an IRI.
     Overrides the single creator of shared/metadata.md.
     TODO: this pattern belongs to the new paper, so the author list may
     differ from the four patterns of the ETFA paper. -->
creator:
  Marvin Schieseck

---

## Identity

<!-- dcterms:title — the full name, as it appears in the documentation. -->
title: IEC 60050-351 Ontology Design Pattern

<!-- rdfs:label — the short name, for a browser tab or a diagram legend. -->
label: IEC 60050-351 ODP

<!-- The permanent IRI. The version IRI is built from this and version below. -->
iri: https://w3id.org/aias/odp/iec60050

<!-- vann:preferredNamespacePrefix -->
prefix: iec60050

---

## Version

<!-- owl:versionInfo and owl:versionIRI. Three numbers, for example 1.0.0. -->
version: 1.0.0

<!-- dcterms:hasVersion — what Widoco shows as "Latest version". The
     unversioned IRI, which the w3id redirect points at whatever the
     current version is, so this line never has to be touched again. -->
latestVersion: https://w3id.org/aias/odp/iec60050

<!-- owl:priorVersion — the version IRI this one succeeds. Empty here: this
     pattern has no predecessor, it is a first release. -->
priorVersion:

<!-- owl:incompatibleWith — the version IRI a model cannot be migrated from
     without change. Set it only where that is actually the case. -->
incompatibleWith:

<!-- dcterms:created — the date the ontology was first written. -->
created: 2026-08-18

<!-- dcterms:modified — the date of this version. -->
modified: 2026-09-02

<!-- bibo:status — Draft, or Published once it is released. -->
status: Draft

---

## What it is about

<!-- dcterms:source — the standard the pattern rests on, as an IRI. -->
source: https://www.dinmedia.de/de/norm/din-iec-60050-351/208013542

<!-- dcterms:references — works the ontology draws on without resting on
     them normatively. One per line, indented by two spaces. Terms the
     standard leaves to others are named in the ontology comment. -->
references:

<!-- dcterms:subject — keywords, comma separated. These are what someone
     searching a registry types, so use the terms of the field rather than of
     this project. -->
subject: Control Technology, IEC 60050-351, Ontology Design Pattern, Closed-loop Control, Automation

<!-- dcterms:abstract — one paragraph, at most about 150 words. Widoco shows
     it at the top of the documentation and it travels with the Turtle file,
     which is why it is the only abstract there is. -->
abstract:
  An ontology design pattern for the terminology of control technology,
  following DIN IEC 60050-351:2014, the International Electrotechnical
  Vocabulary. It models a control as a chain of action paths and actions, which
  is what allows open-loop and closed-loop control to be told apart by
  structure rather than by name: a closed-loop control requires a closed action,
  not merely a closed path. Around that it holds the variable quantities of a
  control loop, the items under consideration with their functional and
  physical units, the normative taxonomy of control functions, and the
  characteristics a device carries with their values and units. Seventy-nine
  classes drawn from 86 of the standard's 409 entries, with the selection
  documented entry by entry.

---

## Publication

<!-- dcterms:bibliographicCitation — what Widoco shows as "Cite as" at the top
     of the documentation. The paper, so that a reader citing this work cites
     the publication rather than the file.
     TODO: this pattern belongs to the new paper rather than to the ETFA one.
     Fill in once that publication exists. -->
bibliographicCitation:

<!-- bibo:doi — the DOI of that paper. -->
doi:

---

## Overrides

<!-- Any field of shared/metadata.md can be repeated here to override it for
     this package. Leave this section empty unless something really differs. -->
