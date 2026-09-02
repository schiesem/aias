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

Anything the rules do not match goes to the repository rather than to an
error page.

## Moving the default to a later version

An IRI without a version resolves to 1.0.0. Moving that to 2.0.0 is an edit
to this file and nothing else: there is no registration to update, since w3id
holds no record beyond the file itself.

Replace `v1.0.0` with `v2.0.0` in the ten lines of the two blocks headed
*without a version*, then open a pull request against `perma-id/w3id.org`
with the changed file. The blocks that carry an explicit version are left
alone.

That is the point of a versioned IRI: `/odp/vdi3682/1.0.0` keeps resolving to
1.0.0 for good, so a model that imported it a decade ago still gets the
ontology it was written against. Only the bare IRI follows the current
version.

## Checking it

Every target must exist before the pull request is opened: a redirect to a
page that is not there will not be merged.

```
curl -sI -H "Accept: text/html"  https://w3id.org/aias/odp/vdi3682
curl -sI -H "Accept: text/turtle" https://w3id.org/aias/odp/vdi3682
```

Both should answer `303` with a `Location` header pointing at
`schiesem.github.io/aias/…`.
