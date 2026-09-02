# ISO/IEC 7498-1 v1.0.0: what was changed and what was kept

This version publishes the model of the dissertation. It was cleaned up for
release, and this file records every change so that a reader can tell the model
from the cleanup.

The binding source is the figure of the dissertation together with the passage
of section 7 describing the pattern and the definition table of the appendix.

---

## Corrected

### The standard number was wrong

The file, the ontology IRI and every class carried `ISO7489`. The standard is
**ISO/IEC 7498-1**. A transposed digit, and one that would have been permanent
had it gone out under that IRI.

Now `https://w3id.org/aias/odp/iso7498`, with the version IRI
`.../iso7498/1.0.0`.

### Namespace

`http://www.semanticweb.org/schieseck/ISO7489` was the value Protégé inserts
when none is given. It does not resolve and carries a user name.

### `Package` to `Packet`

A packet is a data unit, a package is something else. A typing error rather
than a naming decision.

### `Com1`, `Com2`, `Com3` are gone

Three classes named after the communications of a case study. They are
instances of a particular plant, not concepts, and modelling them as classes
says "the set of all communications of the kind Com1", which states nothing.

They appear in neither the figure nor the text.

### `transmitsData` and `hasDataUnit` were one relation

The OWL file carried two relations, `hasDataUnit` from a layer and
`transmitsData` from a communication. The text names neither. It names `hasDU`
and says the content transmitted is assigned "to the respective layer **or to
the communication directly**", which is one relation with two domains.

Now one `hasDataUnit` with the domain `Layer` or `Communication`, carrying
`hasDU` as an alternative label so the name of the text remains findable.

### `1000BASE-T` as a class name

A name beginning with a digit is awkward in a namespace and in a query. The
class is `Ethernet1000BASET` and carries `1000BASE-T` as its label.

### Comments were German only, some with broken umlauts

Every class and relation now carries `@de` with the wording of the work and
`@en` with its translation. Six classes had `tbd.` and now have definitions.

---

## Kept, though version 2.0.0 does it differently

### Layers, technologies and data units are subclasses

This is the substantial difference between the two versions.

| | 1.0.0 | 2.0.0 |
|---|---|---|
| seven layers | subclasses of `Layer` | named individuals |
| nine technologies | subclasses of `Technology` | named individuals, 21 of them |
| five data units | subclasses of `DataUnit` | named individuals, plus the PDU/SDU distinction |

A layer is a particular thing, not a kind of thing: there is one physical
layer, not a set of physical layers. Version 2.0.0 models it accordingly, which
also lets a layer carry its number as a value and makes an ordering expressible.

The 1.0.0 keeps the subclasses because the figure of the dissertation draws
them that way.

**Note on the text.** Section 7 of the dissertation says the seven layers are
"modelliert als Instanzen der Klasse `Layer`", which contradicts both the figure
and the OWL file. The figure was followed here.

**For the author:** that sentence and the figure disagree. One of the two would
have to be adjusted for the dissertation to describe one model.

### `Name` as a class

A communication is given a name through a class of its own rather than through
`rdfs:label`. Version 2.0.0 drops the class.

---

## Not taken up

Everything version 2.0.0 adds stays out, since it is not part of the model the
dissertation describes:

- the architecture of an open system: `OpenSystem`, `Subsystem`, `Entity`,
  `Service`, `Protocol`, `ServiceAccessPoint`, and the peer relation between
  entities
- the two transmission modes, connection-mode and connectionless, and the
  direction of a communication
- the quality of service with its seven parameters and their values
- the composition of a protocol data unit out of control information and user
  data, and its mapping onto a service data unit one layer down

**Result:** 26 classes and 4 relations, against 20 classes, 43 named
individuals and 22 relations in version 2.0.0.
