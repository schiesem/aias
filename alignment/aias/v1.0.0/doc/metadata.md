# Metadata: AIAS Alignment Ontology

**This is version 1.0.0**, the first published state of the alignment, kept as
a maintained branch of its own.

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
     Overrides the single creator of shared/metadata.md. -->
creator:
  Marvin Schieseck
  Philip Topalis
  Lasse Reinpold
  Felix Gehlhoff
  Alexander Fay

---

## Identity

<!-- dcterms:title — the full name, as it appears in the documentation. -->
title: AIAS Alignment Ontology

<!-- rdfs:label — the short name, for a browser tab or a diagram legend. -->
label: AIAS

<!-- The permanent IRI. The version IRI is built from this and version below. -->
iri: https://w3id.org/aias

<!-- vann:preferredNamespacePrefix -->
prefix: aias

---

## Version

<!-- owl:versionInfo and owl:versionIRI. Three numbers, for example 1.0.0. -->
version: 1.0.0

<!-- dcterms:hasVersion — what Widoco shows as "Latest version". The
     unversioned IRI, which the w3id redirect points at whatever the
     current version is, so this line never has to be touched again. -->
latestVersion: https://w3id.org/aias

<!-- owl:priorVersion — the version IRI this one succeeds. Empty here: this
     is the first release. -->
priorVersion:

<!-- owl:incompatibleWith — the version IRI a model cannot be migrated from
     without change. Set it only where that is actually the case. -->
incompatibleWith:

<!-- dcterms:created — the date the ontology was first written. -->
created: 2024-09-01

<!-- dcterms:modified — the date of this version. -->
modified: 2026-09-03

<!-- bibo:status — Draft, or Published once it is released. -->
status: Draft

---

## What it is about

<!-- dcterms:source — the standard the pattern rests on, as an IRI. Empty
     here: an alignment rests on design decisions rather than on a standard,
     and the three patterns it imports name their own sources. -->
source:

<!-- dcterms:references — works the ontology draws on without resting on
     them normatively. One per line, indented by two spaces. -->
references:
  R. Haberfellner, O. de Weck, E. Fricke and S. Vössner, Systems Engineering. Springer, 2019. ISBN 978-3-030-13430-3

<!-- dcterms:subject — keywords, comma separated. These are what someone
     searching a registry types, so use the terms of the field rather than of
     this project. -->
subject: Ontology Alignment, Artificial Intelligence, Automated Plant, Industrial Automation, System Architecture

<!-- dcterms:abstract — one paragraph, at most about 150 words. Widoco shows
     it at the top of the documentation and it travels with the Turtle file,
     which is why it is the only abstract there is. -->
abstract:
  An alignment ontology describing artificial intelligence applications in
  automated plants together with the plant and the technical process it runs.
  It imports three subdomain patterns, for the technical process after
  VDI/VDE 3682, for communication after ISO/IEC 7498-1 and for artificial
  intelligence after ISO/IEC 22989, and ties them together through three
  collecting classes: a function, a component and a relation. Placing a process
  operator and an inference under one function class is what makes them
  comparable, so that the same assignment states which resource carries out
  which function, whichever subdomain that function comes from. Twelve own
  classes and eight own relations. Nothing here is normative: the patterns rest
  on standards, the alignment rests on design decisions.

---

## Publication

<!-- dcterms:bibliographicCitation — what Widoco shows as "Cite as" at the top
     of the documentation. The paper, so that a reader citing this work cites
     the publication rather than the file. -->
bibliographicCitation: M. Schieseck, P. Topalis, L. Reinpold, F. Gehlhoff and A. Fay, "A Formal Model for Artificial Intelligence Applications in Automation Systems," 2024 IEEE 29th International Conference on Emerging Technologies and Factory Automation (ETFA), Padova, Italy, IEEE, September 2024. DOI 10.1109/ETFA61755.2024.10710890

<!-- bibo:doi — the DOI of that paper. -->
doi: 10.1109/ETFA61755.2024.10710890

---

## Overrides

<!-- Any field of shared/metadata.md can be repeated here to override it for
     this package. Leave this section empty unless something really differs. -->
