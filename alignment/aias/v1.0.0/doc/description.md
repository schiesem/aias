<!-- description
     Written by hand, the source for the Widoco section of the same name.
     Never edit the generated HTML. -->

Twelve own classes and eight own relations, plus the statements that place the
elements of the three imported patterns below them. The ontology is small on
purpose: most of what it can express comes from what it imports, not from what
it adds.

## The three collecting classes

Everything of the three patterns is placed below one of three classes, which is
what makes elements of different subdomains comparable.

`Function` describes transformations by which inputs are turned into outputs in
order to reach the objectives of a system. Without it, a process operator of
VDI 3682 and an inference of ISO/IEC 22989 are unrelated things and nothing can
be said about both at once.

`Component` describes physical system elements that perform functions or are
transformed by them.

> Software artefacts such as models or AI components are deliberately **not**
> components. They stay in the AI subdomain, and their place in the whole is
> recorded through the functions they realise and the assignment of those
> functions to a resource.

`Relation` describes structured relationships and dependencies between
functions and components. Relations are classes rather than object properties
so that a model can annotate one: an assignment is a thing, not an arrow.

All three follow the system elements of Haberfellner et al., *Systems
Engineering*, Springer 2019.

## What the patterns contribute

| Level | From VDI 3682 | From ISO/IEC 7498-1 | From ISO/IEC 22989 |
|---|---|---|---|
| Function | `ProcessOperator` | | `AIFunction` |
| Relation | `Assignment`, `Flow` | `Communication` | |

Each keeps the properties of its own pattern alongside the ones it gains here,
which is what lets a dependency be described across the subdomains.

## Resources and products

`Resource` is a physical component performing a function, equated with
`vdi3682:TechnicalResource`: a resource is what performs a function, which is
what that standard defines the technical resource as.

`Product` covers physical objects created, changed or consumed in the course of
a technical process, equated with `vdi3682:Product`.

Both sit below `Component` and differ in their role. A resource performs
functions, a product is transformed by them.

Seven kinds of device sit flat below `Resource`: `Sensor`, `Actuator`,
`Controller`, `EdgeDevice`, `Computer`, `InternalCloud` and `ExternalCloud`.
None of them rests on a standard, and they can be refined further through a
classification of equipment such as ECLASS.

`ExternalCloud` is the one that carries weight in a query. A function running
there leaves the organisation, which is what separates it from the internal
cloud.

## Data

The data classes of ISO/IEC 22989 are **not** lifted into this ontology. They
stay in the AI subdomain and act as the inputs and outputs of the functions
defined there.

One statement ties the two notions of data together:

```turtle
iso7498:Data owl:equivalentClass iso22989:Data .
```

That is what lets a dataset be tied to a communication as well, so a model can
state which kind of data is used in which phase of the life cycle and where in
the plant it sits or is communicated.

## Relations

`hasFunction`, `hasComponent` and `hasRelation` reach from an AI system to its
parts, whichever subdomain each part comes from.

`isAssignedTo` relates a function or a component to the assignment stating
which resource carries out which function. VDI 3682 states the assignment from
the process operator, which cannot reach a function of another subdomain. This
relation is what closes that gap.

`hasFlow` relates a function, a component or a product to a flow it takes part
in.

### The three communication relations

`hasCommunication` states a bidirectional use, `hasInputCommunication` a use as
a receiver, `hasOutputCommunication` a use as a sender.

> **They are independent, not a hierarchy.** A sensor that only sends carries
> `hasOutputCommunication` and nothing else. Were the two directed relations
> subproperties of the first, a reasoner would infer that the sensor is
> bidirectional as well, which is the opposite of what the model states.

All three have `Component` as their domain rather than `Resource`, and that is
deliberate. A product may take part in a communication: a workpiece carrying an
RFID tag or a barcode is read along the line, and restricting the relation to
resources would rule that out.

## Disjointness

Three axioms. The three collecting classes are pairwise disjoint, so are the
seven kinds of device, and so are the three relations the patterns contribute.

Without them a wrong `rdfs:domain` does not fail. It quietly infers that
something is a function and a component at once, and no query asking which
resource carries which function has a reliable answer any more.

Three things are deliberately **not** disjoint:

- `Resource` and `Product` differ in their role rather than in their nature. A
  workpiece may be a product now and serve as a fixture later.
- `ProcessOperator` and `AIFunction`, because an automation function of
  ISO/IEC 22989 acts on the process, so the two can meet in one step.
- `ParallelFlow` and `AlternativeFlow`, since a flow may be part of a parallel
  run at one point of a process and of an alternative one at another.
