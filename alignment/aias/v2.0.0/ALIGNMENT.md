# AIAS Alignment: Every Bridge and Its Basis

The four subdomain patterns stand on their own and import nothing from one
another. This file records every bridge the alignment builds between them, and
the reason for each, so that the connections are checkable rather than
asserted.

It is the counterpart of the `REFERENCE.md` files of the patterns. Those record
which entries of a standard are taken up and why. This one records which
classes of different namespaces are related and how strongly.

**Nothing here is normative.** The patterns rest on standards, the alignment
rests on design decisions of this work. Where a bridge follows from a standard,
the entry says so. Where it follows from a reading, it says that instead.

---

## The three main classes

The alignment is built around the system elements of Haberfellner: a function
transforms, a component is transformed or performs, and a relation ties the two
together.

| Class | What it collects |
|---|---|
| `aias:Function` | everything that transforms something, whatever subdomain it comes from |
| `aias:Component` | the physical elements of a system |
| `aias:Relation` | the ties between functions and components |

They hang off `iso22989:AISystem` through `hasFunction`, `hasComponent` and
`hasRelation`, so that a model of an AI application in an automated plant has
one root.

**Why a function class at all.** Without it a process operator of VDI 3682 and
an inference of ISO 22989 are unrelated things, and nothing can be said about
both at once. Under one superclass they become comparable: both are assigned to
a resource through the same mechanism, and a query asking what a device does
returns process steps and AI functions in one answer. That comparability is
what the whole alignment exists for.

---

## Equivalent classes

Two, and only where the definitions are word for word the same.

| A | B | Basis |
|---|---|---|
| `iso22989:Control` | `iec60050:Control` | **Both standards give the same definition**: purposeful action on or in a process to meet specified objectives. ISO/IEC 22989, 3.5.5 takes it from IEC 61800-7-1:2015, 3.2.6, and IEC 60050-351, 351-42-19 carries the identical wording with national footnote N1 confirming it as the general term. The two are the same concept, not similar ones. |
| `aias:Resource` | `vdi3682:TechnicalResource` | A design decision of this work, carried over from the information model this rebuilds. A resource is what performs a function, which is what VDI 3682 defines the technical resource as. |

**Why so few.** An `owl:equivalentClass` says that two classes have the same
extension in every model, in both directions. That is a strong claim, and it is
wrong wherever the two merely overlap. The bridges below say less on purpose.

---

## The function level

Everything that transforms something becomes a subclass of `aias:Function`.

| Subclass | From | Why |
|---|---|---|
| `vdi3682:ProcessOperator` | VDI 3682 | An operation transforming input states into output states. The transformation of the technical process. |
| `iso22989:Training` | ISO/IEC 22989, 3.3.15 | determining the parameters of a model |
| `iso22989:Validation` | 3.5.18 | confirming the requirements for an intended use |
| `iso22989:Verification` | 3.5.17 | confirming specified requirements |
| `iso22989:Evaluation` | clause 5.10 | assessing a final model |
| `iso22989:Inference` | 3.1.17 | deriving conclusions from premises |
| `iso22989:DataProcessing` | clause 5.10 | transforming input data into output data |
| `iso22989:Acquisition` | clause 8.6.1 | obtaining data from a source |
| `iso22989:Storing` | clause 8.6.1 | persisting data to a sink |
| `iso22989:Control` | 3.5.5 | purposeful action on a process |

### Control replaces the automating function

The information model of the dissertation carried a class `Automate` here, for
describing automated procedures. It is gone, and control takes its place.

The reason is that ISO/IEC 22989, 3.1.7 defines automatic, automation and
automated as **an adjective**: pertaining to a process or system that, under
specified conditions, functions without human intervention. IEC 60050-351,
351-42-30 says the same. Neither defines a thing a model instantiates, so
neither pattern carries a class for it.

Control does what the automating function was there for, and it does it with a
normative definition on both sides. Because `iec60050:Control` is the
superclass of `OpenLoopControl` and `ClosedLoopControl`, the two inherit the
function property, and the alignment thereby carries the distinction between
open-loop and closed-loop control into the function view. That distinction was
the reason for taking up IEC 60050-351 in the first place.

---

## The component level

| Subclass | From | Why |
|---|---|---|
| `aias:Resource` | this work | what performs a function, equivalent to `vdi3682:TechnicalResource` |
| `aias:Product` | this work | what a function transforms, matching `vdi3682:Product` |

Resources and products share the component level and differ in their role:
a resource performs functions, a product is transformed by them.

### What is deliberately not a component

`iso22989:AIComponent` stays in the AI subdomain and is **not** made a subclass
of `aias:Component`. The component class covers physical elements, and a
software artefact is not one. Its place in the whole is recorded through the
functions it performs and their assignment to a resource.

The same holds for `iec60050:FunctionalUnit`. A controlling system is a unit
seen by function, not a piece of equipment, and IEC 60050-351 keeps that apart
from the physical unit, 351-56-03, on purpose. Only the latter is a component
in the sense used here.

### The devices

`aias:Sensor`, `aias:Actuator`, `aias:Controller`, `aias:EdgeDevice`,
`aias:Computer`, `aias:InternalCloud` and `aias:ExternalCloud` remain classes
of this work, as subclasses of `aias:Resource`. They come from no standard, and
that is recorded here rather than hidden.

**Not bridged to the IEC 60050-351 units, on purpose.** The standard defines a
sensing element, 351-56-26, an actuator, 351-49-07, and a controller,
351-49-11, but all three are functional units rather than devices, and one of
them means something different from what the name suggests:

| Term | IEC 60050-351 | What `aias:Actuator` means here |
|---|---|---|
| actuator, 351-49-07 | the signal side, generating the manipulated variable to drive the final controlling element | the element acting on the flow |
| final controlling element, 351-49-08 | the element acting on the mass or energy flow, a valve | this is the match |

Relating `aias:Actuator` to `iec60050:Actuator` would therefore state the
opposite of what is meant. The nearest match is the final controlling element,
and even that is a functional unit rather than a device. The bridge is left out
until the devices are related to a classification of equipment such as ECLASS,
which is where they belong.

---

## The relation level

| Subclass | From | What it ties |
|---|---|---|
| `vdi3682:Assignment` | VDI 3682 | a function to the resource performing it |
| `iso7498:Association` | ISO/IEC 7498-1 | two or more resources exchanging information |
| `vdi3682:Flow` | VDI 3682 | products or information along a process |

Relations are classes rather than object properties, so that they can carry
properties of their own. An assignment is a thing a model can annotate, not an
arrow.

### The assignment needs one relation of its own

VDI 3682 states the assignment from the process operator: `hasAssignment` runs
from `vdi3682:ProcessOperator` to `vdi3682:Assignment`, and `assignedResource`
from there to the resource. Both follow the guideline, and neither reaches an
AI function, which is not a process operator.

The alignment therefore adds one relation:

```turtle
aias:assignedFunction a owl:ObjectProperty ;
    rdfs:domain vdi3682:Assignment ;
    rdfs:range  aias:Function .
```

`hasAssignment` stays as the guideline defines it. The new relation says which
function an assignment carries, whatever subdomain that function comes from,
and it is what makes the common function level usable rather than merely
stated. Without it a model could group a process operator and an inference
under one superclass and still have no way to assign the second to a device.

The relation is deliberately not made a superproperty of `hasAssignment`. The
two run in opposite directions, from the function and from the assignment, and
relating them would require an inverse the pattern does not state.

---

## The data bridge

The dissertation set `iso7498:Data` equal to `iso22989:Data`. That bridge does
not hold, for two reasons.

**There is no such class.** The ISO 7498 pattern of this work has no `Data`
class. It has `DataUnit` with the four kinds the standard defines, of which
`UserData`, the payload carried on behalf of the layer above, is the one that
matters here.

**The two are not the same thing.** They differ in what determines them and in
how many of them there are:

| | `iso7498:UserData` | `iso22989:Data` |
|---|---|---|
| what it is | the payload of one transmission | a collection of samples |
| determined by | a transmission between two entities | a use in the AI life cycle |
| lifetime | the transmission | the life cycle |
| how many | one per transmission | one dataset, transmitted many times |

An equivalence would claim that every payload is an AI dataset and every
dataset is a payload. Neither holds: a ping carries payload without any AI
involved, and a training dataset exists whether or not it is ever transmitted.

### What the alignment states instead

```turtle
aias:carriesData a owl:ObjectProperty ;
    rdfs:domain iso7498:UserData ;
    rdfs:range  iso22989:Data .
```

The payload carries the dataset. The chain then reads:

    iso22989:Data  <--carriesData--  iso7498:UserData
                                          ^
                                     hasUserData
                                          |
                                  iso7498:ProtocolDataUnit
                                          ^
                                      transmits
                                          |
                                   iso7498:Association

A model can then say that a given dataset travels over a given communication,
on a given layer, with a given quality of service. **That question only becomes
answerable because the two stay apart.** Under an equivalence the dataset would
be the payload of one transmission, and asking which communications carry it
would be meaningless.

Nothing has to be added to the ISO 7498 pattern for this. `UserData` and
`transmits` are already there.

---

## Reaching the control role from a resource

A model of an automated plant starts from devices. It knows a sensor, a
controller, a valve, and it needs to ask what each of them does in the control
that runs over them: which action lines touch it, which variables pass through
it, and whether the path it takes part in is open or closed.

### A resource is a physical unit

The chain starts at a class the IEC 60050-351 pattern does not know. It reaches
a device through `iec60050:PhysicalUnit`, and a model of a plant writes
`aias:Sensor` or `aias:Controller`. One statement joins the two:

    aias:Resource rdfs:subClassOf iec60050:PhysicalUnit .

An `owl:equivalentClass` would be wrong here, and the reason is worth stating,
since the two classes look interchangeable and are not.

| | `vdi3682:TechnicalResource` | `iec60050:PhysicalUnit` |
|---|---|---|
| clause | VDI 3682 Part 1, 4.2 | IEC 60050-351, 351-56-03 |
| definition | a physical component **that realises the transformation** carried out by a process operator | an item under consideration defined **according to construction or configuration** |
| requires a function | yes | no |

VDI 3682 requires the resource to do something. IEC 60050-351 requires only
that the thing be looked at by how it is built. A terminal block, a cabinet or
a power supply is a physical unit and realises no transformation, so it is not
a technical resource. Every resource is a physical unit, the converse does not
hold, and the subclass is what states that asymmetry.

The direction that matters is the one a model uses. It asserts a resource, and
the reasoner infers the physical unit that the relations below start from.

### The relations run the wrong way

The rest of the path exists, but the IEC 60050-351 pattern stated it in one
direction only. A functional unit **is realised by** a physical unit, 351-56-02 and -03,
and an action path **is composed of** action lines, 351-44-03 and -04. Both
follow the wording of the standard, and both are useless to a model asking from
the device end.

Four inverse relations were added to that pattern for this. They assert nothing
of their own, since the reasoner derives each of them from a statement already
made:

| Relation | Inverse of | Lets a model go from |
|---|---|---|
| `realisesFunctionalUnit` | `realisedByPhysicalUnit` | a device to what it does |
| `isSourceOfActionLine` | `fromUnit` | a unit to the lines leaving it |
| `isTargetOfActionLine` | `toUnit` | a unit to the lines entering it |
| `partOfActionPath` | `hasActionLine` | a line to the path and on to the control |

The chain then runs forwards:

    aias:Resource
      --realisesFunctionalUnit-->  iec60050:FunctionalUnit
      --isSourceOfActionLine-->    iec60050:ActionLine
      --carriesVariable-->         iec60050:VariableQuantity
      --partOfActionPath-->        iec60050:ClosedActionPath
      <--runsOverActionPath--      iec60050:ClosedLoopControl

Question 19 of the IEC 60050-351 pattern asks exactly that, and its answer on
test case 2 shows a device sitting in the feedback branch and another in the
forward branch. Neither fact is asserted anywhere. Both follow from the chain.

Question 13 of this package walks the same chain from the alignment side, and
test case 2 carries the model it needs: the control of the plant is resolved
into the four functional units of Figure 2 of the standard and the four action
lines between them. The answer names the robot control three times, once per
unit it realises, and the application unit once as the final controlling
element. The class of the path comes out of the model rather than out of a
label, which is what makes the bridge testable instead of asserted.

### The role stays on the functional unit

One point matters for the alignment and is easy to get wrong. The role belongs
to the functional unit, not to the device, and a device may realise several
units at once. Device C of test case 2 of the IEC 60050-351 pattern realises
four: a reference generator, a
controller and the comparing and controlling elements inside it.

Asking such a device for its role therefore has several answers, and that is
the correct result rather than an ambiguity to remove. IEC 60050-351 keeps the
functional and the physical view apart on purpose, and a model wanting one role
per device would have to assert a cardinality the standard does not state.

The alignment adds no shortcut from `aias:Resource` to a role for that reason.
A shortcut would have to choose, and there is nothing to choose by.

## Three further bridges

Three classes are related without being listed above, because each is a single
statement rather than a level of the alignment.

| Bridge | Statement | Basis |
|---|---|---|
| `aias:Component` appears as `iso7498:OpenSystem` | a component becomes an open system when its communication is described | The ISO 7498 pattern already states this on the class: 4.1.3 defines the open system as the representation of those aspects of a real system pertinent to interconnection. A thing is not an open system in itself, it is one under that view. The domain is the component rather than the resource, since a product may communicate as well: a workpiece carrying an RFID tag is read along the line. |
| `aias:carriesData` | the payload of a transmission carries a dataset | The data bridge above, stated as a relation because the two are not the same thing. |
| `iso22989:SystemDesign` against the assignments | the design claims where a system runs, the assignments say where it does | Not an axiom. The design is a statement a model makes, and the assignments are what it has to bear out. Question 09 compares the two and reports a mismatch, since OWL cannot require the agreement. |

## Two names, two concepts

`Controllability` appears in both new patterns with the same spelling and
different meanings. **They are not related, and relating them would be a
mistake.**

| | `iec60050:Controllability` | `iso22989:Controllability` |
|---|---|---|
| clause | IEC 60050-351, 351-42-22 | ISO/IEC 22989, 3.5.6 |
| definition | the state variables may be changed from an initial state into a desired final state within a finite time interval | a human or another external agent can intervene in the system's functioning |
| what it is about | a mathematical property of a dynamic system | whether a person can take over |

A query asking which systems are controllable would otherwise return controlled
systems and AI systems with a stop button in one answer, and the answer would
mean nothing.

This is recorded here so that the two are not merged later by someone tidying
up a duplicate name.

`Model` is a milder case of the same. `iec60050:Model`, 351-42-26, is a
representation of a system or process based on known laws. `iso22989:Model`,
3.1.23, is a representation of a system, entity, phenomenon, process **or
data**. The second is the broader one, so the alignment relates them with
`rdfs:subClassOf` rather than with an equivalence.

`CharacteristicValue` exists in both patterns with identical wording, but both
are constructs of this work rather than entries of a standard. The alignment
introduces `aias:CharacteristicValue` and places the two below it, so that the
shared construction is stated rather than duplicated by accident.

---

## What still has to be decided

1. **The devices need a classification.** ECLASS or a comparable catalogue
   would give `aias:Sensor` and its siblings a basis they currently lack. Until
   then they are proprietary classes and this file says so.

2. **Whether a control is also an assignment.** A control acts on a controlled
   system, and an assignment ties a function to a resource. The two describe
   the same situation from different sides, and whether the alignment should
   relate them is open.
