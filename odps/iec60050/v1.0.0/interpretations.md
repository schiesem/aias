# Interpretations of the competency question results

Source text for `RESULTS.md`, which the test runner generates. Everything else
in that report is produced from the queries and the recorded results, so it
cannot go stale. These interpretations are written by hand and have to be kept
in step with the models.

Format: one `## cqNN` heading per question, followed by free text. A question
without an entry appears in the report marked as missing rather than silently
omitted.

The three cases are the two figures of the standard and the trap between them.
Case 1 is the open-loop chain of Figure 1, case 2 the closed loop of Figure 2,
case 3 the reset circuit of 351-47-06: a closed action path with an open
action. Reading an answer across the three shows what the standard separates.

---

## cq01

One control per case, each with its direct kind. Case 2 reports a sampling
control rather than a closed-loop control, since the reasoner materialises the
narrowest class and the query reports that one.

## cq02

The distinction the pattern exists for. Cases 1 and 3 are open-loop, case 2
closed-loop.

That case 3 is open-loop despite its closed path is the whole point of it, and
question 08 is where that becomes readable.

## cq03

Only case 2 answers, with one row: its control is a sampling control, which
sits under the closed loop.

Asked of the case rather than of the class hierarchy. The pattern knows seven
special kinds, and listing them would answer the same whichever model is
loaded. The genus is reported alongside, since a sampling control is a closed
loop that acts at intervals rather than continuously, and the special kind
means nothing without that.

## cq04

The three variables of a control in one row. Case 2 states all three, cases 1
and 3 fewer.

Collecting them rather than listing them separately is deliberate: three rows
per control would repeat the control and say nothing more.

## cq05

Cases 1 and 3 answer, case 2 does not. An open-loop control acting through a
chain without holding a variable is ordinary, and 351-47-04 has the sequential
control run through steps rather than hold anything.

The kind is reported so a reader can tell that from a gap. OWL cannot require
the variable under the open world assumption, so this reports where a model has
stayed silent.

## cq06

The path of each control with its kind. Cases 2 and 3 both report a closed
action path, and that they agree here while differing everywhere else is what
makes case 3 worth having.

## cq07

The action alongside the path. Case 1 has an open action over an open path,
case 2 a closed action over a closed path, case 3 an open action over a closed
path.

The third is the divergence, reported in full by question 08.

## cq08

One row, case 3, and empty on the other two.

Entry 351-47-06 defines the reset circuit as a switching system with a closed
action path containing at least one binary storage element, and the note to the
entry states that it has an open action despite the closed path. The answer
shows exactly that: the path is closed, the action is open, the control is
open-loop.

A model reading a closed path as a closed loop would type it wrongly, which is
the reason the three kinds are reported side by side rather than inferred from
one another. That the question returns nothing on cases 1 and 2 is what makes
the one row mean something.

## cq09

The chain line by line, five in case 1, nine in case 2, six in case 3. Each
line names the unit it leaves, the unit it enters and the variable it carries,
so the answer reads as the figure of the standard written out.

Case 2 is Figure 2 with its letters: the reference variable enters the
comparing element, the control difference leaves it, and the feedback closes
the loop back to where the forward path began.

## cq10

Whether the chain returns to where it started, computed over the transitive
closure of the lines rather than by looking for adjacency.

The distinction matters. An earlier version of this question tested whether two
lines met, and every chain came out as closing. Following the path to see
whether a unit is reachable from itself is what actually answers it.

Case 1 answers no, cases 2 and 3 yes. Case 3 answering yes alongside an open
action and an open-loop control is the reset circuit again, seen from the chain
rather than from the type.

## cq11

Only case 2 answers. Entries 351-44-05 and 351-44-06 split a control loop into
a forward and a feedback path, and only a closed loop has both.

Case 3 has a closed path and no branches, which is consistent: a closed path is
not by itself a control loop.

## cq12

Empty in all three cases, which is the intended state. A line outside every
path connects two units without taking part in any chain, so nothing reaches it
and it reaches nothing.

## cq13

The variables with their role, two in case 1, four in case 2, one in case 3.

The role is the relation that carries the variable rather than its class:
hasReferenceVariable, hasManipulatedVariable and the rest are subproperties of
hasVariable, and the query reports which of them applies. Reading the role off
the class would say what a variable is, reading it off the relation says what
it is to this control, and the second is what a model is asked.

The disturbance appears here against the controlled system rather than against
the control, which is where 351-42-13 places it.

## cq14

The disturbance variables, one each in cases 1 and 2, none in case 3. Entry
351-42-13 has the disturbance act on the controlled system from outside the
chain, which is why it is reached by `actsOn` rather than by an action line.

## cq15

One row in cases 1 and 2, the disturbance variable, and none in case 3.

The answer needs reading rather than fixing. A disturbance is precisely the
variable that does not flow along the chain: it acts on a unit from outside it.
Its appearing here is the model working correctly, and the role reported
alongside is what lets a reader see that rather than take it for a forgotten
connection.

## cq16

Empty in all three cases. Entry 351-42-24 separates the signal from what it
carries, and these cases describe their chains in terms of variables rather
than of the signals conveying them.

That is the level Figures 1 and 2 work at. The question is here for a model
that goes below it, where the same current carries a temperature or a position
depending on what its magnitude is taken to mean.

## cq17

Every item under consideration with two columns saying whether it is a
functional unit, a physical unit, or both. Twelve in case 1, nineteen in case
2, ten in case 3.

The two columns are the point. Entries 351-56-02 and 351-56-03 keep the
functional and the physical view apart, and an item may be seen either way, so
a single kind column would force a choice the standard does not make.

## cq18

Which device realises which functional unit, four in case 1, nine in case 2.
The relation joining the two views of question 17.

## cq19

The question the pattern is built for, and the largest answer: seventeen rows
in case 2.

Device C realises four functional units at once, the reference generator, the
comparing element, the controlling element and the controller they make up, and
appears on six action lines. That is not an ambiguity to resolve. Entries
351-56-02 and 351-56-03 keep the two views apart precisely so that one device
can carry several functions, and asking such a device for one role would
require a cardinality the standard does not state.

Nothing in the answer is asserted on the device. The model states which unit a
device realises and which units a line connects, and the role, the variable and
the kind of path follow from walking the chain.

The AIAS alignment uses the same chain. `aias:Resource` is a subclass of
`iec60050:PhysicalUnit`, so a model stating a sensor or a controller can be
asked this question across the subdomains, and question 13 of that package does
exactly that.

## cq20

Functional units with no device behind them, five in case 1, six in case 2.

The answer needs reading rather than clearing, and the class is what tells the
two situations apart. The controlled system, 351-49-01, is the part of the
plant being influenced: it is the process rather than a device, so nothing
realises it and nothing should. A comparing element without a device is a
different matter, being a function with no equipment behind it.

## cq21

The composition of functional units, seven rows in case 1, nine in case 2.
Entry 351-56-02 lets a unit consist of further units, and the standard uses
that in its own definitions: the controller of 351-49-11 is a unit made of a
comparing and a controlling element.

Reported with the kind of each part, since the composition is only readable
against what the parts are. The pattern asserts no rule about which
combinations are sound, so a controller made of two measuring elements would be
accepted and would show up here as what it is.

## cq22

The functions performed, one row per case. The functions are named individuals,
supplied with the pattern, and a case states which of them an item performs.

## cq23

The characteristic values stated, one in case 1, three in case 2. The value is
reified so that it can carry the characteristic it belongs to alongside the
quantity and the unit, which is what makes a bare number readable.

## cq24

The thirteen characteristics of 351-45 held against the case, with the standing
of each. Case 2 states three of them and leaves ten open.

The catalogue is the yardstick rather than the answer here, which the query
declares. Listing the characteristics would report the same thirteen whatever
case is loaded; holding them against the case reports what this control
actually specifies.

The unstated half is the useful one. A control with no stated dead time carries
no timing that a requirement could be checked against.

## cq25

One row, case 2: the programmable controller carries a real-time capability.
Entry 351-45-32 defines it as the capability to meet a required response time.

The capability is reported as a thing rather than as a number, since that is
how the pattern records it. What it is worth in seconds is a characteristic
value, which question 23 reports: the case states a control settling time of
2.5 s.

Cases 1 and 3 answer empty, which is consistent with their level of detail:
both describe a chain without saying what carries it in time.
