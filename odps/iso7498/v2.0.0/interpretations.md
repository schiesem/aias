# Interpretations of the competency question results

Source text for `RESULTS.md`, which the test runner generates. Everything else
in that report is produced from the queries and the recorded results, so it
cannot go stale. These interpretations are written by hand and have to be kept
in step with the models.

Format: one `## cqNN` heading per question, followed by free text. A question
without an entry appears in the report marked as missing rather than silently
omitted.

The four cases differ in one thing each. Case 1 is a communication between two
systems, case 2 the same communication with its architecture opened up, case 3
the same again in connectionless mode, case 4 with four participants instead of
two. An answer read across the four columns therefore shows what one change
does.

---

## cq01

One communication per case, connecting two systems in cases 1 to 3 and four in
case 4. The base relation of clause 5.2 and the anchor every other question
starts from.

## cq02

The mode, told apart by the class. Cases 1, 2 and 4 are connection-mode, case 3
connectionless.

Clause 5.8.4 makes this a property of the communication rather than of the
data: a connectionless transmission carries no state between units, which is
why the two are separate classes rather than a flag.

## cq03

The direction, one row per case. Cases 1 and 2 are two-way simultaneous, case 3
one-way.

That case 3 changes here as well is the point of it. The mode was the one thing
changed, and the direction followed: 6.4 has connectionless transmission convey
a unit from one entity to one or more others without a return path being part
of the arrangement. The model states the consequence rather than describing it.

`hasDirection` is functional, so a communication runs in one direction, which
negative model 02 tests.

## cq04

The participant count. Cases 1 to 3 answer with two endpoints, case 4 with four
and the label multi-endpoint.

Clause 5.3.1.4 names a connection with more than two connection endpoints a
multi-endpoint connection, and the threshold is computed rather than asserted,
so a model states its participants and the kind follows.

## cq05

Empty in all four cases: every communication is typed as one mode or the other.

The question cannot be enforced. A communication of the general class is
unstated rather than modeless under the open world assumption, so the answer
reports a gap where one exists and SHACL is where it would become a rule.

## cq06

The architecture of clause 5.2: an open system consists of subsystems, one per
layer it takes part in. Only case 2 answers, with six rows, being two systems
of three subsystems each.

The others describe a communication without opening it up, which the standard
permits and question 08 reports as the difference it is.

## cq07

The layer a communication states for itself, one row per case, the application
layer in each. That is where the payload originates, and the layers below carry
it without the communication being about them.

## cq08

Which of the seven layers a case says anything about, and how much. The
catalogue of layers is the yardstick here rather than the answer, which is why
the query declares itself as such.

The distinction in the third column is what the question is for. Case 1 names
four technologies and reaches five layers that way, and every one of them reads
as named only: the model says Ethernet carries layer 2 and stops there. Case 2
refines three of them into subsystems and entities, and those read as refined.

Layers 5 and 6 stay empty in every case. That is ordinary rather than missing:
the session and presentation layers of the reference model have no counterpart
in most industrial stacks, and a model that does not use them says so by
leaving them out.

## cq09

Which technology realises which layer. Cases 1 to 3 answer with four rows, case
4 with one, a fieldbus.

`realisesLayer` is functional: a technology realises one layer, which negative
model 04 tests. The pattern does not check that the assignment is sensible, and
the open points of the catalogue record why: rejecting MQTT at the network
layer belongs to a rule base rather than to a descriptive pattern.

## cq10

Empty in all four cases, since each names its technology.

The question matters once the pattern is used for a plant rather than for a
reference model. Clause 1.3 states that the model implies no particular
technology, so a communication without one is complete as far as the standard
goes and incomplete as far as a deployment goes. The answer is the list of what
is still undecided.

## cq11

The neighbours of a subsystem within one open system, twelve rows in case 2 and
none elsewhere.

Asked relative to a subsystem of the case rather than to a fixed layer number,
because the architecture rests on what is above and below: an entity uses the
service of the layer below and provides one to the layer above. The absolute
number is a label, the relation is the structure.

Reported within one system only. Two subsystems of different systems have no
above or below to each other, they are peers, which question 13 covers.

## cq12

The entities of each subsystem, six rows in case 2. Clause 5.2.1 has the entity
as the active element of a layer, and a subsystem is what holds them.

One entity per subsystem in this case, which is the simple arrangement. The
standard permits several, and nothing in the pattern limits it.

## cq13

The peer entities, six rows in case 2. Clause 5.2.1.2 pairs the entities of the
same layer in different systems, and that pairing is what a protocol governs.

The layer is reported alongside for a reason the open points record: 5.2.1.3
has peers sit at the same layer, and nothing in the pattern forbids a model
from relating two across layers. The violation is readable in the answer, and
enforcing it needs SHACL.

## cq14

The services provided, three rows in case 2. Clause 5.2.2 has an entity of one
layer provide a service to the layer above, which is the vertical relation of
the architecture.

Three services for six entities, which question 17 explains: only one side of
each pair provides one in this model.

## cq15

The protocols, one row in case 2: a transport protocol employed by two
entities.

Reported per protocol rather than per entity, so the entities sharing one
appear together. That two peer entities employ the same protocol is the normal
case and the reason the concept exists, and a protocol employed by one entity
alone would mean either an unmodelled peer or a rule nothing on the other side
follows.

## cq16

The service access points, three rows in case 2. Clause 5.2.2.1 makes them the
place where a service is reached, which is what separates the service from the
entity providing it: the point is addressable, the entity is not.

## cq17

Three entities without a service in case 2, all of them in system B.

The answer needs reading rather than fixing. Case 2 models the service relation
from one side, so the entities of system A provide services and their peers in
system B consume them. That is a modelling choice rather than a defect, and the
layer reported alongside is what lets a reader see it: an application entity
providing no service is ordinary, a network entity providing none usually is
not.

## cq18

The data units a communication transmits, one per case. The relation between a
communication and its payload, and the starting point of questions 19 to 22.

## cq19

What the transmitted unit is made of. Clause 5.6.1 splits it into control
information and user data, and case 2 is the one that states both.

Restricted to units a communication transmits. The pattern supplies frame,
packet, segment and the rest as named individuals, and those say what a unit at
a layer is called rather than what a given communication carried. An earlier
version of this question answered with the catalogue whatever case was loaded.

## cq20

The mapping between layers, two rows in case 2. Clause 5.6.2 has a protocol
data unit of one layer become the service data unit handed to the layer below,
and the two rows are that step happening twice, from transport to network and
from network to data link.

This is encapsulation stated as a relation rather than described in prose, and
it is what makes the layered architecture checkable in a model.

## cq21

The data units of a case with their layer, one row in case 1 and four in case
2. The four are the same payload seen at three layers, which is what a refined
model shows.

The reachable set is collected by following the composition from the
transmitted unit. Collecting it by class instead would match every individual
of that class, the supplied catalogue included, and an earlier version of this
question did exactly that.

## cq22

The chain from a communication to its payload, one row per case. Case 1 reaches
a unit with no stated user data, case 2 reaches the application data through
the transport unit.

The question exists for the alignment. `aias:carriesData` starts at this user
data and reaches the dataset of the ISO/IEC 22989 pattern, so a model can ask
which communications carry a given dataset, and the chain has to be walkable
from this end for that to work.

A unit with control information and no user data is legitimate rather than
incomplete: an acknowledgement conveys no payload.

## cq23

The quality of service stated for a communication. Cases 1 and 3 state three
values, case 4 two, case 2 none.

That case 2 states none is deliberate. It refines the architecture rather than
what the communication delivers, and the two are independent: a model may say
how a communication is built without saying what it guarantees.

## cq24

The same values with their parameter and unit. `forParameter` is functional, so
one value quantifies one parameter, which negative model 03 tests.

The reification is what makes the answer readable. Without it a model could
state a number and not what it is a number of.

## cq25

Which parameters a case states and which it leaves open. Case 1 states three of
seven: throughput at 100 Mbit/s, transit delay at 12 ms, establishment delay at
250 ms. The remaining four read as not stated.

The catalogue is the yardstick rather than the answer here, which the query
declares. Listing the parameters would report the same seven whatever case is
loaded; holding them against the case reports what this communication actually
promises.

The unstated half is the useful one. A communication with no stated transit
delay carries no timing a deadline could be checked against, and for a plant
that is the question worth asking first.

## cq26

One row, case 2, for the reason given at question 23.

## cq27

The comparison per parameter. Cases 1 and 3 answer with three parameters, case
4 with two, and each is stated by one communication, since these cases carry
one communication each.

The degenerate answer is still worth returning: it says what the one
communication promises. The question comes into its own on a model of a plant,
where one path is time critical and another is not, and the comparison then
reads down a column.
