# Shared metadata

The values that are the same for every ontology and never differ between
them. Everything tied to a publication lives in the package instead, because
each ontology belongs to a paper of its own: `references`,
`bibliographicCitation` and `doi` are per package. The funding is the same for
all of them and therefore stands here.

`shared/apply_metadata.py` reads this file together with the `doc/metadata.md`
of each package and writes the result into the ontology header.
**Edit here, never in the Turtle.**

A package can override any field by setting it in its own `doc/metadata.md`.

Format: one `key: value` per line under a heading. A value spanning several
lines is indented by two spaces on the following lines. A line starting with
`#` outside a value is a comment and is ignored. An empty value means the field
is left out of the Turtle rather than written as an empty string.

---

## People

<!-- dcterms:creator — the author. Written as "Name | ORCID-URL" once the ORCID
     is known; until then the name alone is written as a string.
     TODO: add the ORCID, https://orcid.org/0000-0000-0000-0000 -->
creator: Marvin Schieseck

<!-- dcterms:publisher — the institution issuing the ontology.
     TODO: the exact name of the institute. The usual form is
     "Helmut-Schmidt-Universität / Universität der Bundeswehr Hamburg,
     Institut für ...". A ROR ID can be added as a second line. -->
publisher: Helmut-Schmidt-Universität / Universität der Bundeswehr Hamburg

---

## Funding

<!-- dcterms:rights — the funding statement, in the funder's exact wording.
     Do not reword it, not even the dashes: it is what the funder requires.
     Identical for every package. -->
rights: This research is funded by dtec.bw – Digitalization and Technology Research Center of the Bundeswehr. dtec.bw is funded by the European Union – NextGenerationEU

<!-- foaf:fundedBy — the funder as an IRI. Machine readable, unlike the
     sentence above. -->
fundedBy: https://dtecbw.de/

---

## Legal

<!-- dcterms:license — the licence IRI, not its name. CC BY 4.0: attribution,
     otherwise free. What registries such as LOV expect, and what allows reuse
     in commercial tooling. -->
license: https://creativecommons.org/licenses/by/4.0/

---

## Where it lives

<!-- schema:codeRepository — the repository the sources are kept in. -->
codeRepository: https://github.com/schiesem/aias

<!-- The GitHub Pages base the w3id IRIs redirect to. Used to build the
     documentation links, not written into the Turtle. -->
pagesBase: https://schiesem.github.io/aias
