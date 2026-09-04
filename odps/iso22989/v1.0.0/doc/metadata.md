# Metadata: ISO/IEC 22989 Ontology Design Pattern

**This is version 1.0.0**, the first published state of the pattern, kept as a
maintained branch of its own.

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
title: ISO/IEC 22989 Ontology Design Pattern

<!-- rdfs:label — the short name, for a browser tab or a diagram legend. -->
label: ISO/IEC 22989 ODP

<!-- The permanent IRI. The version IRI is built from this and version below. -->
iri: https://w3id.org/aias/odp/iso22989

<!-- vann:preferredNamespacePrefix -->
prefix: iso22989

---

## Version

<!-- owl:versionInfo and owl:versionIRI. Three numbers, for example 1.0.0. -->
version: 1.0.0

<!-- dcterms:hasVersion — what Widoco shows as "Latest version". The
     unversioned IRI, which the w3id redirect points at whatever the
     current version is, so this line never has to be touched again. -->
latestVersion: https://w3id.org/aias/odp/iso22989

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

<!-- dcterms:source — the standard the pattern rests on, as an IRI. -->
source: https://www.iso.org/standard/74296.html

<!-- dcterms:subject — keywords, comma separated. These are what someone
     searching a registry types, so use the terms of the field rather than of
     this project. -->
subject: Artificial Intelligence, ISO/IEC 22989, Ontology Design Pattern, Machine Learning, AI Life Cycle

<!-- dcterms:abstract — one paragraph, at most about 150 words. Widoco shows
     it at the top of the documentation and it travels with the Turtle file,
     which is why it is the only abstract there is. -->
abstract:
  An ontology design pattern for describing an artificial intelligence
  application, following the terminology of ISO/IEC 22989. It covers three
  views of the same system: the AI system with the functions of its life cycle
  and the tasks it addresses, the algorithms and models with the parameters
  that configure them, and the data with the processes that acquire, prepare
  and store it. The three meet where a training consumes a dataset and produces
  a model, which is what lets a model be traced back to the data it was built
  from. Sixty-two classes and twenty-five relations. The pattern is one of
  three subdomain patterns of the AIAS information model and is meant to be
  imported and aligned rather than used on its own.

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
