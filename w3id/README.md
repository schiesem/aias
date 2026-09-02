# The w3id redirect

The file next to this one, `.htaccess`, is what makes the `w3id.org/aias`
IRIs resolve. It is **not** used from this repository: it lives in
[perma-id/w3id.org](https://github.com/perma-id/w3id.org) under `aias/`, and
this copy is the source it is kept in sync with.

Changing a redirect means opening a pull request there with the new file.

## What it does

An IRI resolves differently depending on what asks for it. A browser gets the
documentation, a reasoner the ontology, in whichever serialization it accepts.
Both under the same IRI, through an HTTP 303 redirect.

| IRI | Browser | Reasoner |
|---|---|---|
| `w3id.org/aias` | the alignment's documentation | `AIAS.ttl` and the other serializations |
| `w3id.org/aias/1.0.0` | that version's documentation | that version |
| `w3id.org/aias/odp/vdi3682` | the pattern's documentation | the pattern |
| `w3id.org/aias/odp/vdi3682/2.0.0` | that version's documentation | that version |

An IRI without a version resolves to 1.0.0, the published one. The default
moves to 2.0.0 once that is released, which is one line per block in the file.

Anything the rules do not match goes to the repository rather than to an
error page.

## Checking it

Every target must exist before the pull request is opened: a redirect to a
page that is not there will not be merged.

```
curl -sI -H "Accept: text/html"  https://w3id.org/aias/odp/vdi3682
curl -sI -H "Accept: text/turtle" https://w3id.org/aias/odp/vdi3682
```

Both should answer `303` with a `Location` header pointing at
`schiesem.github.io/aias/…`.
