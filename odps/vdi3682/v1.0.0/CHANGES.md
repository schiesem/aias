# VDI 3682 v1.0.0: what was changed and what was kept

This version publishes the model of the dissertation. It was cleaned up for
release, and this file records every change so that a reader can tell the model
from the cleanup.

The binding source is the figure of the dissertation, which draws the classes
and the relations between them, together with the definition table of its
appendix.

---

## Corrected

### Namespace

`http://www.semanticweb.org/schieseck/VDI3682` was the value Protégé inserts
when none is given. It does not resolve and carries a user name.

Now `https://w3id.org/aias/odp/vdi3682`, with the version IRI
`.../vdi3682/1.0.0`.

### `TechnicalRessource` to `TechnicalResource`

A typing error. The definition table of the appendix already writes one s.

### `isAssignedTo` was symmetric

The property was declared `owl:SymmetricProperty` with a union of three classes
as both domain and range. Symmetry does not hold here: a resource is not
assigned to an operator because the operator is assigned to it, and
`Assignment` to `Assignment` states nothing at all.

The figure draws two steps, from the operator to the assignment and from the
assignment to the resource. Domain and range now say exactly that, and the
symmetry is gone.

### `hasElement` to `hasState`

The OWL file called it `hasElement`, the dissertation text and its figure call
it `hasState` throughout. The text is the binding source.

### `isInput` and `isOutput` were missing

Section 7 of the dissertation names four relations for the flow directions,
`hasInput` and `hasOutput` **or** `isInput` and `isOutput`, and its example
uses the second pair. The OWL file carried only the first.

Both pairs are now present and declared inverse to each other, which is what
lets a model describe a process from either end.

### Six classes had no definition

`State`, `Energy`, `Information`, `ParallelFlow`, `AlternativeFlow` and
`SystemBorder` carried `tbd.` as their comment. They are also the six classes
missing from the definition table of the appendix, so the gap is in both
artefacts.

The definitions are taken from VDI 3682 itself.

**For the author:** the appendix table `tab:vdi3682-begriffe` lists six of the
twelve classes. The six named above would have to be added there for the table
to cover the ontology.

### Comments were German only, some with broken umlauts

Every class and relation now carries `@de` with the wording of the standard and
`@en` with its translation. The standard is issued bilingually, and the German
is the wording the dissertation cites.

---

## Kept, though version 2.0.0 does it differently

These are decisions of the work, not defects. The difference between the two
versions is therefore visible rather than silently repaired.

| | 1.0.0 | 2.0.0 |
|---|---|---|
| what an operator takes in | `hasInput` reaches a **flow**, and the flow carries a state | `hasInput` reaches a **state** directly |
| decomposition | `consistsOf` has `Process` in its range: a process consists of processes | separate `hasSubProcess` and `hasUpperProcess` |
| assignment | one `isAssignedTo` along a chain of two steps | `hasAssignment` and `assignedResource`, one per step |
| flow direction | `isInput`/`isOutput` as the inverse pair | four relations naming source and target by kind |
| system border | `SystemBorder` | `SystemLimit`, which is what the standard calls a Systemgrenze |

`SystemBorder` is the one name kept against the standard. The dissertation uses
it, and renaming it would make the published 1.0.0 disagree with the text it
belongs to.

---

## Read off the figure rather than off the OWL file

The figure connects `Product`, `Energy` and `Information` to `State` through
`hasState`. The OWL file made them subclasses of `State` instead.

The figure is right, and the difference matters: a product is not a kind of
state, it is a thing that has one. The same sheet of metal before and after a
stamping is one product in two states, which the subclass reading cannot
express.

`hasState` therefore has two domains, the flow and the three kinds of thing,
exactly as drawn.

---

## Not taken up

Everything version 2.0.0 adds stays out, since it is not part of the model the
dissertation describes:

- the attribute structure of Part 2 Section 4.4: `Attribute`,
  `Identification`, `Characteristic` with nine data properties
- the order of process operators: `hasPredecessor`, `hasSuccessor`
- their decomposition: `isComposedOf`, `hasSubProcess`, `hasUpperProcess`
- the directed flow relations: `hasStateSource`, `hasStateTarget`,
  `hasOperatorSource`, `hasOperatorTarget`, `hasSource`, `hasTarget`
- `dependency` between states and `isWithin` for the system limit

**Result:** 12 classes and 7 relations, against 15 classes and 21 relations in
version 2.0.0.
