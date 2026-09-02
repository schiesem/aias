# Versions of the AIAS Alignment ontology

Every version is a directory of its own and a maintained branch, not a frozen
copy. A version may still receive a patch release after a newer one exists.

| Version | Standing | Directory |
|---|---|---|
| **2.0.0** | current | `v2.0.0/` |
| 1.0.0 | maintained | `v1.0.0/` |

**Current is 2.0.0.** An IRI without a version resolves to it; a versioned
IRI such as `.../2.0.0` resolves to that version and keeps doing so once a
newer one is published.

The 1.0.0 is the model of the dissertation, cleaned up for publication. It
carries documentation but no test infrastructure: the competency questions and
test cases belong to the rework, not to the state the dissertation describes.
