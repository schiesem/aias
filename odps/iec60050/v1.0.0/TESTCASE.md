# Test Cases: IEC 60050-351 Pattern

Three test cases built from the definitions of DIN IEC 60050-351:2014, the
International Electrotechnical Vocabulary, Part 351: Control technology.

Two rules govern these cases, the same as for the other patterns:

1. **Taken from the standard.** Each case is built from the definitions of
   clause 351-47, and the element names stay generic. The standard is a
   vocabulary rather than a set of worked examples, so the cases follow its
   definitions rather than a figure.
2. **Independent of the alignment.** No test case assumes anything about AI,
   communication, or a formalised process description. They exercise the
   IEC 60050 pattern alone, so a failure can only come from this pattern.

| Case | Source | Covers |
|---|---|---|
| 1 | 351-47-02, 351-47-05 | open-loop control over an open action path |
| 2 | 351-47-01, 351-47-03, 351-47-04 | closed-loop control over a closed action |
| 3 | 351-47-06, 351-47-62 | open-loop control **despite** a closed action path |

Case 3 is the one that matters most. It is the case the standard names
explicitly, and it is what separates this pattern from the simplified reading
that feedback alone makes a closed-loop control.

---

## Why the distinction needs three cases

IEC 60050-351 separates two things that are easy to confuse, and the whole
pattern turns on keeping them apart.

**The path is structure**, 351-44-03: a directed path connecting two variable
quantities. Something that is drawn in a functional diagram, and that either
exists or does not.

**The action is behaviour**, 351-42-24: the influence of one variable quantity
on another. What actually happens over that structure.

The nearest everyday comparison: the action path is the cable that has been
laid, the action is what flows through it.

### Two questions, not one

Both are graded as open or closed, but by different criteria:

| | open | closed |
|---|---|---|
| **Path** | 351-47-05: **no** path goes back from the output to the input variable | 351-47-03: an additional path goes back |
| **Action** | 351-47-06: the output influences the input only under conditions that do **not act permanently** | 351-47-04: the output influences the input **continuously**, and thereby itself |

For the path the question is *is there a way back*. For the action it is *does
it act continuously*. Two questions, so the answers can come apart.

### The sentence everything turns on

351-47-06 defines the open action as an action in an open action path, **or in
a closed action path** where the output influences the input only under
conditions that do not act permanently.

The part after the "or" is the decisive one. The standard states outright that
an open action can occur inside a closed path. That is why `OpenLoopControl`
and `ClosedLoopControl` are **not** disjoint in this pattern, and why path and
action are two classes rather than one.

### What follows for the kind of control

351-47-01 requires the closed **action** for closed-loop control, not the
closed path: characteristic for closed-loop control is the closed action in
which the controlled variable continuously influences itself.

Three combinations therefore occur, and all three are modelled:

| Path | Action | Result | Case |
|---|---|---|---|
| open | open | open-loop control | 1 |
| closed | closed | **closed-loop control** | 2 |
| closed | **open** | **open-loop control** | 3, the reset circuit |

The fourth combination, an open path with a closed action, is impossible:
without a way back nothing can act back. Negative models 02 and 03 test that
neither the path nor the action can be open and closed at once.

### Nothing here is derived

All three statements are asserted by the modeller, none is computed:

```turtle
ex:PathC   a iec:ClosedActionPath .     # statement 1: the structure
ex:ActionC a iec:OpenAction .           # statement 2: the behaviour
ex:ControlC a iec:OpenLoopControl .     # statement 3: the classification
```

`actionOverPath` only ties the second to the first. It does not make one follow
from the other. Removing the action would leave the path a `ClosedActionPath`,
and one path may carry several actions, of which one acts permanently and
another does not.

The reasoner intervenes **within** each of the three, never between them: a
path cannot be open and closed at once, an action cannot, and nothing can be
both a path and an action. `ClosedActionPath` together with `OpenAction` is
entirely consistent, which is what makes case 3 possible.

Deriving the kind of control would not be supported by the standard either,
since 351-47-01 additionally requires the controlled variable to be measured
and compared. The closed action is necessary, not sufficient.

### What is computed

One thing only: whether the chain of action lines actually forms a cycle.
Question 23 works that out from the lines, not from the class assignment, which
is what turns the claim that a path is closed into something checkable. Where
the claim and the chain disagree, the answer shows `ClosedActionPath` with
`no`.

---

## The functional diagram

Each case records its action path as the chain of units it runs through, after
Figures 1 and 2 of the standard. Without that chain a path can only be asserted
to be open or closed. With it the assertion becomes checkable: the closed path
of case 2 is a cycle in the graph, and the open path of case 1 is not.

**The figures.** Figures 1 and 2 of the standard show the elements of an
elementary open-loop and closed-loop control system. Both are reproduced under
`figures/` for reference while reading the cases:

| File | Figure |
|---|---|
| `norm-figure1-openloop.png` | Figure 1, elementary open-loop control system |
| `norm-figure2-closedloop.png` | Figure 2, elementary closed-loop control system |

They are excerpts from a purchased standard and are therefore excluded from
version control. Each has to be obtained from DIN IEC 60050-351:2014 by whoever
works on the package.

**The elements.** An action path is composed of action lines, 351-44-04, each
running from one functional unit to another and carrying one variable quantity.
The direction of action, 351-44-05, is carried by the two relations `fromUnit`
and `toUnit` rather than by a class of its own, since note 2 of that entry
states that the direction of action need not agree with the direction of the
mass or energy flow.

**The units of Figures 1 and 2**, with the German terms the standard gives, so
that the cases can be checked against the printed figures:

| Class | German | Clause | Forms |
|---|---|---|---|
| `ReferenceVariableGeneratingElement` | Fuehrungsgroessenbildner | 351-49-10 | w from c |
| `ComparingElement` | Vergleichsglied | 351-49-03 | e from w and r |
| `ControllingElement` | Steuerglied, Regelglied | 351-49-04 | m from c or from e |
| `Actuator` | Steller | 351-49-07 | y from m |
| `FinalControllingElement` | Stellglied | 351-49-08 | acts on the flow |
| `MeasuringElement` | Messglied | 351-49-05 | r from x |
| `ControlledSystem` | Strecke | 351-49-01 | x from y and z |

**The variables**, with the letters of the figure legends:

| Letter | Class | German |
|---|---|---|
| c | `CommandVariable` | Zielgroesse |
| w | `ReferenceVariable` | Fuehrungsgroesse |
| e | `ControlDifferenceVariable` | Regeldifferenz |
| m | `ControllerOutputVariable` | Reglerausgangsgroesse |
| y | `ManipulatedVariable` | Stellgroesse |
| z | `DisturbanceVariable` | Stoergroesse |
| x | `ControlledVariable` | Regelgroesse |
| q | `FinalControlledVariable` | Aufgabengroesse |
| r | `FeedbackVariable` | Rueckfuehrgroesse |

**Two groupings** are recorded through `consistsOfUnit`, since the standard
draws them as dashed frames and their parts stay units in their own right: the
final controlling equipment, 351-49-09, out of actuator and final controlling
element, and the control system, 351-49-06, out of controlling and controlled
system.

**Function and construction stay apart.** The units above are functional units,
351-56-02. What a model calls hardware is a physical unit, 351-56-03, and the
two are joined by `realisedByPhysicalUnit` without any cardinality: one device
may realise several functions, and one function may be spread over several
devices. Case 2 exercises both directions.

### What the chain does and does not prove

The chain makes the structure of a path visible and queryable rather than
enforceable, for the reason given under "Nothing here is derived" above. The
suite reports the chain, it does not validate it against the asserted class.

---

## Case 1: open-loop control

`tests/data/tc1_openloop.ttl`, after 351-47-02, 351-47-05 and Figure 1 of the
standard, reproduced in `figures/norm-figure1-openloop.png`.

A valve is set from a given command, and nothing measures what comes out. The
walkthrough below builds that model step by step. Each step states what is
asserted and why the pattern requires it.

### Step 1: what runs

```turtle
ex:ControlA  a  iec:OpenLoopControl .
```

That is the base statement. `OpenLoopControl` is a subclass of `Control`,
351-42-19, defined as purposeful action on or in a process to meet specified
objectives, and 351-47-02 defines open-loop control as the process whereby
input variables influence output variables in accordance with the proper laws
of the system.

### Step 2: the two conditions that justify the type

Asserting `OpenLoopControl` is not enough. The model has to say what it is
recognised by, and the pattern requires **two separate** statements for that.

```turtle
ex:PathA    a  iec:OpenActionPath .        # structure, 351-47-05
ex:ActionA  a  iec:OpenAction ;            # behaviour, 351-47-06
            iec:actionOverPath  ex:PathA .

ex:ControlA iec:runsOverActionPath ex:PathA ;
            iec:hasAction          ex:ActionA .
```

| Individual | Class | What it asserts |
|---|---|---|
| `PathA` | `OpenActionPath` | **structurally** no path goes back from the output to the input variable |
| `ActionA` | `OpenAction` | **behaviourally** nothing influences the input continuously |

The two are kept apart because case 3 shows that they can come apart.

### Step 3: what carries it out

```turtle
ex:ChainA  a  iec:ControlChain .           # 351-47-12, a series structure
ex:ControlA iec:realisedBy ex:ChainA .
```

A control chain, not a control loop. The range of `realisedBy` is the union of
the two, and they are disjoint.

### Step 4: the functional diagram

Now the path is resolved. Every arrow of Figure 1 becomes one `ActionLine`.

```turtle
ex:PathA iec:hasActionLine ex:L1, ex:L2, ex:L3, ex:L4, ex:L5 .

ex:L1 a iec:ActionLine ;
    iec:fromUnit        ex:CommandSourceA ;
    iec:toUnit          ex:ControllingElementA ;
    iec:carriesVariable ex:c .              # command variable

ex:L2 a iec:ActionLine ;
    iec:fromUnit        ex:ControllingElementA ;
    iec:toUnit          ex:ActuatorA ;
    iec:carriesVariable ex:m .              # output of the controlling element

ex:L3 a iec:ActionLine ;
    iec:fromUnit        ex:ActuatorA ;
    iec:toUnit          ex:ValveA ;
    iec:carriesVariable ex:y .              # manipulated variable

ex:L4 a iec:ActionLine ;
    iec:fromUnit        ex:ValveA ;
    iec:toUnit          ex:ControlledSystemA ;
    iec:carriesVariable ex:x .              # controlled variable

ex:L5 a iec:ActionLine ;
    iec:fromUnit        ex:ControlledSystemA ;
    iec:toUnit          ex:FinalVariableGenerationA ;
    iec:carriesVariable ex:q .              # final controlled variable
```

As a chain:

```
CommandSource --c--> ControllingElement --m--> Actuator --y--> Valve
                                                                 | x
                                                                 v
                                       q <-- FinalVariableGeneration <-- ControlledSystem
                                                                                  X
                                                                            no way back
```

**This is the evidence for step 2.** No `toUnit` points at a unit an earlier
line starts from. Question 23 tests exactly that and answers `chainCloses = no`.

### Step 5: the functional units

Every box of Figure 1 is instantiated, with the German term the standard gives:

```turtle
ex:ControllingElementA  a iec:ControllingElement .        # Steuerglied, 351-49-04
ex:ActuatorA            a iec:Actuator .                  # Steller, 351-49-07
ex:ValveA               a iec:FinalControllingElement .   # Stellglied, 351-49-08
ex:ControlledSystemA    a iec:ControlledSystem .          # Steuerstrecke, 351-49-01
ex:FinalVariableGenerationA a iec:FinalControlledVariableGeneration .
```

The last unit is the box at the right-hand edge of Figure 1, where x enters and
the final controlled variable q leaves the control system.

**It is the one class of the pattern that has no entry in the standard.** The
figures draw it and name it, but it carries no number and no definition. The
class is kept because the variable it produces is a term, 351-48-10, and would
otherwise have no origin in a model. `REFERENCE.md` lists it apart from the
entries for that reason.

The groupings the standard draws as dashed frames are recorded through
`consistsOfUnit`, since their parts stay units in their own right:

```turtle
ex:ControlSystemA a iec:ControlSystem ;                          # 351-49-06
    iec:consistsOfUnit ex:ControllingSystemA, ex:ControlledSystemA .

ex:ControllingSystemA a iec:ControllingSystem ;                  # 351-49-02
    iec:consistsOfUnit ex:ControllingElementA, ex:FinalControllingEquipmentA .

ex:FinalControllingEquipmentA a iec:FinalControllingEquipment ;  # 351-49-09
    iec:consistsOfUnit ex:ActuatorA, ex:ValveA .
```

One membership the standard states explicitly:

```turtle
ex:ValveA iec:partOfControlledSystem ex:ControlledSystemA .
```

351-49-08 places the final controlling element inside the controlled system.
The pattern records that as a relation rather than as a subclass axiom, because
VDI 3682 would hold the same valve as a technical resource of the process. As a
relation both readings stand.

### Step 6: the hardware

```turtle
ex:DeviceA a iec:PhysicalUnit .
ex:DeviceB a iec:PhysicalUnit .
ex:DeviceC a iec:PhysicalUnit .

ex:ControllingSystemA  iec:realisedByPhysicalUnit ex:DeviceA .
ex:ControllingElementA iec:realisedByPhysicalUnit ex:DeviceA .   # the same device
ex:ActuatorA           iec:realisedByPhysicalUnit ex:DeviceB .
ex:ValveA              iec:realisedByPhysicalUnit ex:DeviceC .
```

`FunctionalUnit` and `PhysicalUnit` are the two views of one item under
consideration, 351-56-01: by function and by construction. Here one device
realises two functional units. The standard asserts no cardinality, and the
pattern follows it.

`ControlledSystemA` gets no device. The controlled system is the process, not a
piece of equipment.

### Step 7: variables, function and characteristic

```turtle
ex:c a iec:CommandVariable .            # Zielgroesse
ex:m a iec:ControllerOutputVariable .   # Ausgangsgroesse des Steuerglieds
ex:y a iec:ManipulatedVariable .        # Stellgroesse
ex:z a iec:DisturbanceVariable .        # Stoergroesse
ex:x a iec:ControlledVariable .         # gesteuerte Groesse
ex:q a iec:FinalControlledVariable .    # Aufgabengroesse

ex:ControlA iec:hasManipulatedVariable ex:y ;
            iec:performsFunction       iec:Manipulate ;      # 351-43-12
            iec:hasCharacteristicValue ex:CV_ManipulatingTime .

ex:CV_ManipulatingTime a iec:CharacteristicValue ;
    iec:forCharacteristic inst:ManipulatingTime ;            # 351-48-17
    iec:quantity "4"^^xsd:decimal ;
    iec:unit     "s" .
```

The characteristic value is reified, that is an individual of its own rather
than a literal on the control. A value can then be annotated with its source or
the conditions it holds under without changing the pattern. `forCharacteristic`
is functional: one value quantifies exactly one characteristic.

### What is absent, and has to be

No comparing element, no measuring element, no reference variable, and no
`hasControlledVariable`. Without a comparison there is nothing to compare, and
351-48-01 defines the controlled variable as the one that is measured and
compared. A model claiming one here would state something the standard does not
support.

---

## Case 2: closed-loop control

`tests/data/tc2_closedloop.ttl`, after 351-47-01, 351-47-03, 351-47-04 and
Figure 2 of the standard, reproduced in `figures/norm-figure2-closedloop.png`.

The same chain as case 1, but the controlled variable is measured and returned.

### Step 1: what runs

```turtle
ex:ControlB  a  iec:ClosedLoopControl , iec:SamplingControl .
```

Two types. `SamplingControl`, 351-47-15, is a subclass of `ClosedLoopControl`,
and it is what makes the sampling period of step 7 meaningful.

### Step 2: the two conditions

```turtle
ex:PathB   a iec:ClosedActionPath .        # 351-47-03
ex:ActionB a iec:ClosedAction ;            # 351-47-04
           iec:actionOverPath ex:PathB .

ex:ControlB iec:runsOverActionPath ex:PathB ;
            iec:hasAction          ex:ActionB .
```

**Both** closed. 351-47-01 requires the closed action, not merely the closed
path, which is where case 3 differs.

### Step 3: the control loop and its two branches

```turtle
ex:LoopB a iec:ControlLoop ;               # 351-47-11
    iec:hasForwardPath  ex:ForwardB ;      # 351-47-07
    iec:hasFeedbackPath ex:FeedbackB .     # 351-47-08

ex:ForwardB  a iec:ForwardPath .
ex:FeedbackB a iec:FeedbackPath .

ex:ControlB iec:realisedBy ex:LoopB .
```

A loop, not a chain, and only a loop has a forward and a feedback branch.

### Step 4: the functional diagram, now closed

Nine lines instead of five:

```turtle
ex:PathB iec:hasActionLine ex:M1, ex:M2, ex:M3, ex:M4, ex:M5, ex:M6, ex:M7, ex:M8, ex:M9 .
```

| Line | from | to | carries |
|---|---|---|---|
| M1 | CommandSourceB | ReferenceGeneratorB | c |
| M2 | ReferenceGeneratorB | **ComparingElementB** | w |
| M3 | **ComparingElementB** | ControllingElementB | e |
| M4 | ControllingElementB | ActuatorB | m |
| M5 | ActuatorB | ValveB | y |
| M6 | ValveB | ControlledSystemB | y |
| M7 | ControlledSystemB | MeasuringElementB | x |
| M8 | MeasuringElementB | **ComparingElementB** | r |
| M9 | ControlledSystemB | FinalVariableGenerationB | q |

```
    +---------------- M8 (r) ------------------+
    |                                          |
    v                                          |
ComparingElement --e--> ControllingElement     |
    ^                            |             |
    | M2 (w)                     | m           |
ReferenceGenerator               v             |
    ^                       Actuator           |
    | M1 (c)                     | y           |
CommandSource                    v             |
                              Valve            |
                                 | y           |
                                 v             |
                        ControlledSystem --x---+
```

M7 and M9 together are the branching point of Figure 2: the controlled variable
is taken off towards the measuring element and at the same time leaves the
control system as q.

**M8 ends at `ComparingElementB`, where M3 starts.** The chain is therefore a
cycle in the graph. Question 23 tests it by reachability and answers
`chainCloses = yes`.

### Step 5: the units case 1 does not have

```turtle
ex:ReferenceGeneratorB a iec:ReferenceVariableGeneratingElement .  # 351-49-10, forms w from c
ex:ComparingElementB   a iec:ComparingElement .                    # 351-49-03, forms e from w and r
ex:MeasuringElementB   a iec:MeasuringElement .                    # 351-49-05, forms r from x
```

And the controller as a grouping:

```turtle
ex:ControllerB a iec:ProgrammableController ;                      # 351-56-25
    iec:consistsOfUnit ex:ComparingElementB, ex:ControllingElementB .
```

351-49-11 defines the controller as exactly that, a comparing element and a
controlling element together.

**Two terms that are easy to confuse**, and which the standard keeps apart:

| Class | Clause | Task |
|---|---|---|
| `MeasuringElement` | 351-49-05 | forms the **feedback variable** r from x |
| `SensingElement` | 351-56-26 | responds to the **measurand** |

Two entries, two classes. A model may realise both through one device:

```turtle
ex:SensingElementB   iec:realisedByPhysicalUnit ex:DeviceD1 .
ex:MeasuringElementB iec:realisedByPhysicalUnit ex:DeviceD1, ex:DeviceD2 .
```

### Step 6: hardware in both directions

```turtle
ex:ReferenceGeneratorB  iec:realisedByPhysicalUnit ex:DeviceC .
ex:ControllerB          iec:realisedByPhysicalUnit ex:DeviceC .
ex:ComparingElementB    iec:realisedByPhysicalUnit ex:DeviceC .
ex:ControllingElementB  iec:realisedByPhysicalUnit ex:DeviceC .
```

One device realising four functions, as a programmable controller does. And in
the other direction, one function realised by two devices, as the measuring
element above. Both are admitted, and that is the axis VDI 3682 lacks, where a
technical resource is atomic and carries its function implicitly.

The real-time capability sits on the device, not on the control:

```turtle
ex:ControllerB iec:hasProperty ex:RealTimeB .
ex:RealTimeB a iec:RealTimeCapability .            # 351-54-06
```

351-54-06 defines it as the capability of a system to keep tasks runnable, so it
belongs to what executes, and the interval is stated separately as a
characteristic value.

### Step 7: variables and characteristics

```turtle
ex:w a iec:ReferenceVariable .           # Fuehrungsgroesse
ex:e a iec:ControlDifferenceVariable .   # Regeldifferenz, closed-loop only
ex:x a iec:ControlledVariable .          # Regelgroesse
ex:r a iec:FeedbackVariable .            # Rueckfuehrgroesse, closed-loop only

ex:ControlB iec:hasControlledVariable  ex:x ;      # 351-48-01
            iec:hasReferenceVariable   ex:w ;      # 351-48-02
            iec:hasManipulatedVariable ex:y ;
            iec:performsFunction  iec:Measure, iec:Manipulate, iec:Monitor ;
            iec:hasCharacteristicValue ex:CV_SettlingTime,
                                       ex:CV_Overshoot,
                                       ex:CV_SamplingPeriod .
```

`hasControlledVariable` appears only here. The controlled variable is by
definition what is measured and compared with the reference variable.

---

## Case 3: a closed path with an open action

`tests/data/tc3_resetcircuit.ttl`, after 351-47-06 and 351-47-62.

The reset circuit, and the case the pattern exists for.

```turtle
ex:ControlC a iec:OpenLoopControl ;            # open-loop control
    iec:runsOverActionPath ex:PathC ;
    iec:hasAction          ex:ActionC ;
    iec:realisedBy         ex:ChainC .

ex:PathC   a iec:ClosedActionPath .            # path CLOSED
ex:ActionC a iec:OpenAction ;                  # action OPEN
           iec:actionOverPath ex:PathC .

ex:N4 a iec:ActionLine ;
    iec:fromUnit        ex:StorageElementC ;
    iec:toUnit          ex:ControllingElementC ;   # runs back
    iec:carriesVariable ex:reset .
```

351-47-62 defines a reset circuit as a switching system with a closed action
path containing at least one binary storage element, and the note to 351-47-06
states that its action is open despite that structure.

The chain is **a cycle exactly as in case 2**, but the reset signal acts only
under a condition that does not act permanently. The action is therefore open,
and the control is open-loop control.

The binary storage element has no class of its own in clause 351-49, so the
model records a plain `FunctionalUnit` rather than inventing a term.

### What the queries return

```
           Path              Chain closes   Action         Type
Case 1     OpenActionPath    no             OpenAction     OpenLoopControl
Case 2     ClosedActionPath  yes            ClosedAction   ClosedLoopControl
Case 3     ClosedActionPath  yes            OpenAction     OpenLoopControl
```

Cases 2 and 3 are **structurally indistinguishable**. Only the action separates
them, which is what 351-47-01 turns on.

This is where the pattern departs from the dissertation, whose active text
separates the two by whether the signal is continuous, after
`litz2013-grundlagen`. The standard uses the feedback criterion, and it applies
it to the action rather than to the structure.

---

## What the reasoner catches, and what it does not

Two limits, both stated under "Nothing here is derived" above and repeated here
as a summary: the pattern does not derive the kind of control, and OWL cannot
require a closed action path to contain a cycle.

What the reasoner does catch is the subject of the negative models below: a
path that is also an action, a path that is open and closed at once, an action
that is both, a quantity that is also an item under consideration, and one
value claiming two characteristics. Each of the five is rejected, and the
explanation names the axiom responsible.

---

## Negative models

Each file under `tests/negative/` violates exactly one axiom, so a failure
names its own cause. All must be rejected by the reasoner. A model that is
accepted proves the axiom under test does not bite.

| File | Axiom | Normative basis |
|---|---|---|
| `neg01_path_is_action` | `ActionPath` and `Action` are disjoint | 351-44-03 defines a path as structure, 351-42-24 an action as influence |
| `neg02_open_and_closed_path` | `OpenActionPath` and `ClosedActionPath` are disjoint | 351-47-03 and 351-47-05 are complementary: a path either has a return or it has not |
| `neg03_open_and_closed_action` | `OpenAction` and `ClosedAction` are disjoint | 351-47-04 and 351-47-06 |
| `neg04_variable_is_unit` | `VariableQuantity` and `ItemUnderConsideration` are disjoint | a quantity is not a thing under consideration |
| `neg05_value_for_two_characteristics` | `forCharacteristic` is functional | one value quantifies exactly one characteristic |

---

## Running

```bash
python ../../shared/run_tests.py --package iec60050
```

`RESULTS.md` carries every competency question with its result and an
interpretation.
