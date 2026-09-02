# Interpretations of the competency question results

Source text for `RESULTS.md`, which the test runner generates. Everything else
in that report is produced from the queries and the recorded results, so it
cannot go stale. These interpretations are written by hand and have to be kept
in step with the models.

Format: one `## cqNN` heading per question, followed by free text. A question
without an entry appears in the report marked as missing rather than silently
omitted.

The two cases run the same kind of AI on the same kind of plant. What differs
is where the inference runs and whether its output reaches the control:

| | Case 1 | Case 2 |
|---|---|---|
| architecture | cloud | hybrid |
| inference runs | in the cloud | at the edge |
| the AI acts on the process | no | **yes** |

Reading the two columns of every answer beside each other is what the alignment
is for.

---

## cq01

One system per case, with twelve functions, nine components and sixteen
relations in case 1, and eleven, nine and fourteen in case 2.

The counts are close because the two models describe plants of similar size.
What they do not show is the difference, which the questions below bring out.
This one exists as an entry point rather than as a finding.

## cq02

The functions with the standard each comes from. Both cases answer with all
three: process operators from VDI 3682, AI functions from ISO/IEC 22989, and
controls from IEC 60050-351.

**This is the answer the alignment exists for.** In their own standards the
three have nothing in common. A process operator transforms products, an
inference derives a conclusion, and a control acts on a process, and no
standard relates any two of them. Under `aias:Function` they appear in one
answer, and every question of the next section builds on that.

## cq03

The resources with their kind. Case 1 has two sensors, two controllers, an edge
device and a cloud. Case 2 has two sensors, an actuator, a controller, an edge
device and a cloud.

All seven kinds come from no standard, which `ALIGNMENT.md` records. Question
25 returns the same set for that reason.

## cq04

Which resource performs which function. Both cases answer for every function
they record, whatever subdomain it comes from.

The relation doing the work is `aias:assignedFunction`. VDI 3682 states the
assignment from the process operator, which cannot reach an AI function, and
without the added relation the common function level would be stated but
unusable. This answer is where it earns its place.

## cq05

The same relation read from the resource. Case 2 shows the edge device carrying
three functions, an inference, a data processing and a control, all from
different clauses of two standards.

That one device carries functions of two subdomains is what a mixed
architecture looks like in this model.

## cq06

Which resources carry AI functions and which carry process operations.

| | Case 1 | Case 2 |
|---|---|---|
| carries AI | cloud, controls, sensors | cloud, **edge device**, controls, sensors |
| carries process | the motor control | the robot control |

The edge device of case 1 answers no to both. It exists because the machine
control cannot reach the cloud on its own, which is a fact about the plant
rather than about the AI, and question 23 names it again for that reason.

## cq07

Empty on both cases, after a first version of case 1 was corrected: two of its
three process steps had no assignment, and this question found them.

That is what it is for. A model naming a function without saying what carries
it is unfinished, and the gap is easy to miss by reading.

The question reports rather than enforces. OWL cannot require that every
function be assigned, and stating it as a cardinality would make a model under
construction inconsistent rather than incomplete.

## cq08

Where each AI function runs. Case 1 answers with the cloud throughout. Case 2
splits: inference, merging and correction on the edge device, training,
evaluation and storing in the cloud.

**The split is not arbitrary.** The inference has to finish within a production
cycle, and a cloud cannot promise that. Training on image data is heavy and has
no deadline. The model records the decision, and question 18 records the reason
behind it.

## cq09

The design a system claims, beside the resource kinds actually carrying its AI
functions.

| Case | claims | AI functions sit on |
|---|---|---|
| 1 | Cloud | controller, sensor, external cloud |
| 2 | Hybrid | controller, **edge device**, sensor, external cloud |

Both are consistent with their claim. Had case 2 claimed `Edge` while training
sits in a cloud, this answer would show the mismatch and nothing in OWL would
object. Enforcing the agreement belongs to SHACL, which the open points record.

The sensors and controllers appear because acquisitions are AI functions in
ISO/IEC 22989, and acquisitions sit on the devices that acquire. That is
correct rather than noise: an acquisition is part of the AI life cycle and runs
where the data arises.

## cq10

Which functions run outside the plant. Case 1 answers with five, case 2 with
three.

What makes a cloud external is who operates it, which is a matter of
organisation rather than of technology. The question is the first one a data
protection review asks, and the answer is what it acts on.

## cq11

**The question the two cases turn on.**

Case 1 has one control, a closed-loop position control, and no AI performs it.
Case 2 has two: the same kind of control of the plant, and a correction that an
AI does perform.

The question is answerable because `iso22989:Control` and `iec60050:Control`
are equivalent classes. One statement in the model is seen by both subdomains,
so a control stated in the AI namespace appears here with its kind from the
control namespace.

## cq12

Which AI functions take part in a control. Empty on case 1, two rows on case 2.

The two rows report two ways of taking part. The correction **is** a control.
The inference **produces what the control uses**, which is the indirect case
and the one that matters: an inference whose output steers a plant is not the
same thing as an inference whose output is displayed.

The dissertation this work rebuilds records a rule that fires exactly here,
asking whether an application intervening in a control counts as a control task
and possibly as a high-risk application. The rule fired because the AI output
was modelled as the input of an automating function. This answer is that
situation, stated once and readable from both subdomains.

## cq13

Empty on case 1, eight rows on case 2, and the difference is the point of the
question.

The question walks from a resource through the functional units it realises to
the action lines of the control chain and on to the class of the path. Case 1
describes an architecture and leaves its action path unresolved, so the walk
stops at the first step and the answer is empty. That is the correct result for
a model that does not state what it is not asked to state.

Case 2 resolves the control of the plant into the four functional units of
Figure 2 of IEC 60050-351 and the four action lines between them. The answer
then reports the robot control three times, once as comparing element, once as
controlling element and once as measuring element, and the application unit
once as final controlling element. Two rows per device follow from a unit
sitting between two lines, one entering and one leaving.

Three points are readable from the answer and asserted nowhere:

- The device to unit direction. The model states which physical unit realises a
  functional unit, and the answer runs the other way, through the inverse
  relations of the pattern.
- The class of the resource. The model writes `aias:Controller`, and the query
  anchors on `iec60050:PhysicalUnit`. The subclass axiom of the alignment is
  what carries it across.
- The class of the path. `ClosedActionPath` comes out of the chain of lines
  rather than out of the label of the control.

The multiple rows per device are the answer rather than an ambiguity in it. A
device may realise several functional units, the role belongs to the unit, and
ALIGNMENT.md records why the alignment adds no shortcut that would have to
choose one.

## cq14

Which process steps a control acts on. Case 1 answers with one, case 2 with
two.

The relation is one the alignment adds. IEC 60050-351 has a control act on a
controlled system, which is a functional unit, and VDI 3682 describes what
happens there as a process operator. Neither standard states the connection,
since neither knows the other.

In case 2 both controls act on the same step, which is the situation the model
is built to make visible: the plant controls the movement, and the AI corrects
the result of the same operation.

## cq15

Which resources communicate. Case 1 answers with four pairs, case 2 with three.

A resource appears as an open system when its communication is described,
which the ISO 7498 pattern states on its own class. The alignment records the
appearance so that a model can walk from a device to its communication rather
than starting at the association.

## cq16

The technology and layers of each communication. Both cases answer with empty
columns.

That is a legitimate state. The models record which devices communicate and
what they carry, without committing to how. A model deciding on a fieldbus or
a protocol later fills these columns without changing anything else, which is
what keeping the communication pattern separate buys.

## cq17

Which data travels over which communication. Four rows in case 1, three in case
2.

The chain runs from the association through the protocol data unit and its
payload to the dataset. **It works only because the payload and the dataset
stay apart.** The information model of the dissertation set the two equal, and
under that equivalence a dataset would be the payload of one transmission,
making this question meaningless.

Case 1 shows the same position data on two communications, from each sensor to
the control. One dataset, two transmissions, one identity. That is precisely
what the equivalence would have lost.

## cq18

The quality of service of the communication carrying a dataset. The answer that
spans three subdomains.

Case 2 is the informative one. Both time critical links carry the same quality
of service, the one named after the production cycle, and the link to the cloud
carries none. Read together with question 08 the two answers give the whole
architectural argument: the inference sits at the edge because its data has a
deadline, and the training sits in the cloud because its data has none.

Case 1 has a quality of service only on the link to the cloud, where minutes
are acceptable. That is the reason its whole analysis may sit in a cloud.

## cq19

Empty on both cases. Every dataset shared between two resources travels over a
recorded communication.

The question finds what a model assumes but does not state: two functions on
different devices working on the same dataset, with nothing saying how it got
from one to the other. An empty answer means the model is explicit about its
data paths.

## cq20

Where the data of each AI function comes from, through the acquisition to the
resource that performs it.

Both cases trace every dataset to a device of the plant. The chain crosses
three subdomains: the data and its acquisition from ISO/IEC 22989, the
assignment from VDI 3682, and the resource from this ontology.

## cq21

Which data originates from the plant. Both cases answer with all of their
datasets.

The test is whether the acquisition that produced the data is assigned to a
resource. An acquisition without one reaches nothing, so the data would have to
come from somewhere the model does not describe.

## cq22

The information flows of the process beside the communications. Both cases
answer with their flows and no communication.

The flows recorded here are product flows rather than information flows, so
nothing should match, and nothing does. The question is kept because a model
recording information flows between process steps can ask whether a link exists
to carry them, which is a question about the plant rather than about either
standard.

## cq23

Which resources carry no function. One in each case, and neither is an error.

Case 1 names the edge device, which exists only to bridge the machine control
to the cloud. Case 2 names the application unit, which acts on the material
without any function being assigned to it in this model.

Both are legitimate. A cabinet or a power supply carries nothing and is still
part of the plant, and the question reports rather than judges.

## cq24

Empty on both cases. Every dataset an AI function uses traces back to an
acquisition on a resource.

Data without an origin in the plant is not wrong. It may come from a supplier,
a simulation or an earlier project. The question names it so that a reviewer
can ask where it did come from, and an empty answer says there is nothing to
ask about.

## cq25

Six rows in each case, and all of them are devices.

That is the expected answer. `aias:Sensor` and its siblings come from no
standard, so they are the parts of a model belonging to no subdomain pattern.
Anything else appearing here would be worth looking at, since it would mean the
four standards cover less of the case than intended.

The answer is also a measure of how much of a model rests on decisions of this
work rather than on standards. Six of roughly forty individuals per case is a
proportion the accompanying text can state rather than estimate.
