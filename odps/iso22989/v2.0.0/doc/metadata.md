# Metadata: ISO/IEC 22989 Ontology Design Pattern

What is specific to this package. Everything shared with the other four is in
`shared/metadata.md`, and a field set here overrides the shared value.

`shared/apply_metadata.py` writes these into the ontology header.
**Edit here, never in the Turtle.**

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

<!-- owl:versionInfo and owl:versionIRI. Three numbers, for example 2.0.0. -->
version: 2.0.0

<!-- dcterms:hasVersion — what Widoco shows as "Latest version". The
     unversioned IRI, which the w3id redirect points at whatever the
     current version is, so this line never has to be touched again. -->
latestVersion: https://w3id.org/aias/odp/iso22989

<!-- owl:priorVersion — the version IRI this one succeeds. Empty for a first
     release. -->
priorVersion: https://w3id.org/aias/odp/iso22989/1.0.0

<!-- owl:incompatibleWith — the version IRI a model cannot be migrated from
     without change. Set it only where that is actually the case. -->
incompatibleWith:

<!-- dcterms:created — the date the ontology was first written. -->
created: 2026-08-19

<!-- dcterms:modified — the date of this version. -->
modified:

<!-- bibo:status — Draft, or Published once it is released. -->
status: Draft

---

## What it is about

<!-- dcterms:source — the standard the pattern rests on, as an IRI. -->
source: https://www.iso.org/standard/74296.html

<!-- dcterms:subject — keywords, comma separated. These are what someone
     searching a registry types, so use the terms of the field rather than of
     this project. -->
subject:

<!-- dcterms:abstract — one paragraph, at most about 150 words. Widoco shows
     it at the top of the documentation. The long form lives in
     doc/abstract.md; this is the version that fits in a search result. -->
abstract:

---

## Overrides

<!-- Any field of shared/metadata.md can be repeated here to override it for
     this package. Leave this section empty unless something really differs. -->
