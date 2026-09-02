# AIAS Alignment v1.0.0: what was changed and what was kept

This version publishes the model of the dissertation. It was cleaned up for
release, and this file records every change so that a reader can tell the model
from the cleanup.

The binding source is the figure `figures-aias-alignment` of the dissertation
together with section 7 of its text.

---

## Corrected

### Namespace

`http://www.semanticweb.org/schieseck/AIAS` was the value Protégé inserts when
none is given. Now `https://w3id.org/aias`, with the version IRI
`https://w3id.org/aias/1.0.0`.

The figure already carries w3id IRIs in its legend, so the intention was there
before the file caught up.

### The device classes follow the figure

The OWL file has eight device classes in two levels, with `CloudSystem` as an
intermediate class and both a `ComputerSystem` and a `PersonalComputer`. The
figure draws seven, flat below the resource.

| figure and 1.0.0 | OWL file |
|---|---|
| `Sensor`, `Actuator`, `Controller`, `EdgeDevice`, `Computer`, `InternalCloud`, `ExternalCloud` | the same, plus `CloudSystem` above the two clouds, `ComputerSystem` and `PersonalComputer` |

### `Product` rather than `State` below `Component`

The OWL file places `vdi3682:State` below `aias:Component`, the figure places
`vdi3682:Product` there.

The figure is right. A product is a physical thing and therefore a component. A
state is the condition that thing is in, and a condition is not a component of
a system.

### `aias:Process` is gone

A class `Process` below `Function`, in the OWL file only. VDI 3682 already has
a process, and a second one in the alignment namespace states nothing the
pattern does not.

### `communicatesWith` and `isAssignedBy` had neither domain nor range

Two object properties declared and never described. `isAssignedBy` is the
inverse of `isAssignedTo` and is left out, since the pattern declares no
inverse for it. `communicatesWith` is covered by `hasCommunication`.

### Comments were missing entirely

The OWL file carries no comment on any class of the alignment. Every class and
relation now has one in German and in English.

---

## Kept, though version 2.0.0 does it differently

### The data of the two subdomains are equated

`iso7498:Data owl:equivalentClass iso22989:Data`, as the OWL file states it.

Version 2.0.0 separates them, and the reason is recorded there: the payload of
one transmission and a collection of samples are determined by different things
and exist in different numbers. A ping carries payload with no dataset
involved, and a training dataset exists whether or not it is ever transmitted.

Under the equivalence a question such as "which communications carry this
dataset" cannot be asked, because the dataset would be the payload of one
transmission.

### Three patterns, not four

IEC 60050-351 does not exist in this version. Control technology enters with
version 2.0.0, and with it the equivalence between the two control classes and
the chain from a device to its role in a control.

### `isAssignedTo` reaches the assignment from both sides

One relation with a union of function and component as its domain. Version
2.0.0 splits the two, so that each step states its own domain and range.

---

## Imports are versioned

`owl:imports` names the version IRI of each pattern, not the plain ontology
IRI:

```turtle
owl:imports <https://w3id.org/aias/odp/vdi3682/1.0.0> ,
            <https://w3id.org/aias/odp/iso7498/1.0.0> ,
            <https://w3id.org/aias/odp/iso22989/1.0.0> .
```

Both versions of a pattern carry the same ontology IRI and differ only in their
version IRI, which is how OWL versioning works. An unversioned import would
therefore be ambiguous once two versions exist, and this alignment would pull
in whichever the server happens to serve.

**A defect found while doing this:** every file of version 2.0.0 still carried
`versionIRI .../1.0.0`. The version IRI had never been raised when the rework
began, so all ten files claimed to be the first version. Corrected across the
six files concerned.

---

## Not taken up

- the fourth pattern and everything it brings
- the separation of user data from a dataset
- the subclass relation between a resource and a physical unit
- `assignedFunction`, which reaches an AI function from an assignment

**Result:** 11 own classes and 8 relations, against 12 classes and 7 relations
in version 2.0.0, which reaches further with fewer own terms because it leans
on the fourth pattern.
