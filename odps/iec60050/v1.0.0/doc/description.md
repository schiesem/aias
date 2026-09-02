<!-- description
     Written by hand, the source for the Widoco section of the same name.
     Never edit the generated HTML. -->

Seventy-nine classes, twenty-nine relations and three data properties, drawn
from 86 of the standard's 409 entries. The `skos:note` of each element names
the entry number it rests on, so every definition can be traced back. Where a
term comes from a neighbouring standard rather than from this one, the note
says which.

## What the pattern exists for: paths and actions

A `Control` runs over an `ActionPath` and has an `Action`. Those two are
separate on purpose, and the separation is what lets open-loop and closed-loop
control be told apart by structure rather than by name.

The **path** says whether something returns:

- `OpenActionPath`, where the chain does not close
- `ClosedActionPath`, where it does
- `ForwardPath` and `FeedbackPath`, the two halves of a closed one

The **action** says whether the return acts continuously:

- `OpenAction`
- `ClosedAction`

A `ClosedLoopControl`, entry 351-47-01, requires a **closed action**, not
merely a closed path. The standard states it in words: characteristic for
closed-loop control is the closed action in which the controlled variable
continuously or sequentially influences itself. Modelling path and action
apart is what turns that sentence into something a reasoner can check.

An `ActionLine` is a single edge of the diagram, `partOfActionPath` places it
in a path, and `isSourceOfActionLine` and `isTargetOfActionLine` say which
functional unit it runs between. A `ControlLoop` reaches its two halves through
`hasForwardPath` and `hasFeedbackPath`.

## Kinds of control

`ClosedLoopControl` carries eight kinds below it, each defined in 351-47 with
the genus the standard states: `AdaptiveControl`, `CascadeControl`,
`FuzzyControl`, `ModelBasedControl`, `MultivariableControl`, `RobustControl`,
`RuleBasedControl` and `SamplingControl`.

`OpenLoopControl` carries `SequentialControl`. `ComputerControl`,
`OptimalControl` and `ProgrammedControl` sit directly below `Control`, since
the standard does not place them under either.

## Variables

A `VariableQuantity` is what travels through a control. The hierarchy follows
the roles the standard defines:

| Group | Members |
|---|---|
| Input | `CommandVariable`, `ReferenceVariable`, `DisturbanceVariable` |
| Output | `ControlledVariable`, `ControllerOutputVariable`, `FinalControlledVariable` |
| Others | `ManipulatedVariable`, `FeedbackVariable`, `ControlDifferenceVariable`, `StateVariable`, `Signal` |

A control reaches them through `hasControlledVariable`,
`hasReferenceVariable`, `hasManipulatedVariable` and `hasDisturbanceVariable`.

## Items, units and devices

An `ItemUnderConsideration` is specialised along two lines that the standard
keeps apart, and keeping them apart is what makes the pattern usable.

A `FunctionalUnit` is a **role**: `Controller`, `SensingElement`,
`Actuator`, `ComparingElement`, `MeasuringElement`, `ControlledSystem`,
`FinalControllingElement` and others. A `PhysicalUnit` is a **device**. The two
are tied by `realisedByPhysicalUnit` and its inverse `realisesFunctionalUnit`,
so one device may realise several roles and one role may be realised by
different devices.

> Three readings are easy to get wrong and are stated in the ontology comment.
> An **actuator**, 351-49-07, is the signal side driving the final controlling
> element, not the element acting on the flow. The **final controlling
> element**, 351-49-08, belongs to the controlled system, recorded here as a
> relation so another pattern may hold it as a resource without contradiction.
> And the standard **defines no sensor**: it says sensing element, 351-56-26,
> and grades further by accuracy and signal standardisation.

`consistsOfUnit` decomposes a functional unit into further ones.

## Control functions

The ten functions of 351-43 are **named individuals**, not classes: `Measure`,
`Monitor`, `Manipulate`, `Evaluate`, `Optimize`, `Intervene`, `Notify`, `Warn`,
`Alarm` and `Operate`.

The standard states them as verbs, and they form a normative taxonomy of tasks.
A model that maps its use cases onto them stays connected to existing plant
documentation instead of inventing categories of its own. `performsFunction`
reaches them.

## Characteristics and their values

A `Characteristic` is a property a device or a control has,
with `TimeCharacteristic` and `QualityCharacteristic` below it. A
`CharacteristicValue` carries what was measured, tied back through
`forCharacteristic`, with `quantity`, `unit` and `symbol` as data properties.

Thirteen named individuals supply the characteristics the standard defines,
among them `SamplingPeriod`, `DeadTime`, `SettlingTime`, `Overshoot`,
`PhaseMargin` and `GainMargin`. They live in the companion file
`IEC60050-instances.ttl`, so a model may import the vocabulary without them.

## System properties

`Stability`, `Controllability`, `Observability`, `RealTimeCapability`,
`Redundancy`, `DegreeOfAutomation` and `FunctionalSafety`, each with the entry
it comes from. A `Fault` distinguishes `ActiveFault` from `PassiveFault`.

## What the standard leaves to others

Named in the ontology comment so a reader does not look for them here:
availability and reliability come from IEC 60050-192, accuracy and resolution
from IEC 60050-300, safety integrity from IEC 61508, and everything concerning
data quality from ISO/IEC 22989.
