# Interpretations of the competency question results

Source text for `RESULTS.md`, which the test runner generates. Everything else
in that report is produced from the queries and the recorded results, so it
cannot go stale. These interpretations are written by hand.

All thirteen questions are asked of three cases: the worked example of the
concept chapter and the two case studies of the evaluation. `TESTCASE.md`
describes them.

Reading one answer across the three columns is where the value lies. Cases 2
and 3 are the same kind of plant with the same kind of AI, and the answers
differ because the applications do.

---

## cq01

One row: the training runs on ProCube, an external cloud.

The training reaches its resource through the same assignment that ties a
stamping step to a motor. That is what the common function level is for, and
it is why this question can be asked at all: without it a training and a
process step would be unrelated things.

The kind of resource is the part that matters. An external cloud means the
training data leaves the organisation, which question 12 reports in full.

## cq02

One row, and it runs from end to end: the inference takes the prepared position
data, produces the classified state of the belt, and that state addresses the
classification task the system was built for.

The chain closes back on the task, so a model can be asked whether what it
produces is what it was asked for.

## cq03

Two rows, one per input. The training uses the training dataset and the merged
production data, fixes the model parameters, and the model carrying them is
`ProductionNet_v1`.

The asymmetry to question 02 is worth reading. An inference produces a
prediction, a training produces parameters. The model is not the output of the
training in the way the prediction is the output of the inference; it is the
thing the parameters end up in, which `isCreatedBy` records from the other
side.

## cq04

Three datasets are stored, all of them in the cloud through one storing
function: the raw position data, the raw motor data and the merged result.

Two steps lead there. `isStoredBy` names the function, the function names its
sink and the assignment names the device. Sink and device answer different
questions: the sink says what the data is written to, the device says which
machine holds it.

The prepared data does not appear. It passes through the edge device and is
merged rather than stored on its own, which the answer shows by leaving it out.

## cq05

One row: `ProductionNet_v1` runs on ProCube, through `Inferenz1`.

The indirection is the answer rather than an obstacle to it. A model is an
artefact and is assigned to nothing; what runs is the inference it carries out.
Asking where a model runs means asking where its inference runs, and the model
says so by making the step explicit.

## cq06

One row: the model is `models/ProductionNet_v1.onnx`, created by `Training1`,
which is based on the training algorithm.

The question asks for a name, not for a place. The label of a model instance is
the relative path of the file it stands for, which is how the dissertation ties
the abstract model to what is deployed. A relation from a model to a resource
would state where a file lies, and that belongs to the deployment rather than
to the description of the system.

## cq07

One row: the training algorithm carries `config/MLflowHyperParameter1.json`.

The hyperparameter hangs on the algorithm rather than on the training, which
is what lets a model algorithm and an evaluation algorithm carry one as well:
the number of layers of a network, the threshold of a metric. In this case only
the training algorithm has one.

## cq08

Empty, which is the intended state: every function of this case is carried by
some resource.

OWL cannot require the assignment under the open world assumption. A function
without one is unstated rather than unassigned, so the answer reports where a
description has stayed silent rather than where it is wrong.

## cq09

Two rows on case 1, three on each of the others.

Source and device answer different questions, which is why both are reported.
The source says what the data is about, the device says where in the plant it
was taken. The two often nearly coincide, but they need not.

Case 3 is where they come apart in a way that matters. The picture comes from
the camera, the identification from the RFID reader, and the segment of the
path from the robot control. Three devices, three sources, and only all three
together let a gap be placed on a pane.

An earlier version of this question asked for production data alone and
returned nothing on case 2, where the three acquisitions deliver plain data and
only the result of merging them is production data. The question now anchors on
the data, which is what it was always about.

## cq10

One row: the merging runs in the cloud, takes the prepared position data and
the raw motor data, and produces the merged dataset.

The question matters for provenance. A merged dataset has more than one origin,
and a model trained on it inherits every one of them. Following `isProcessedBy`
backwards from the merged data reaches both sources, and from there question 09
reaches the devices that recorded them.

## cq11

Twelve rows, and reading them is how the architecture becomes visible:

| Resource | carries |
|---|---|
| the two motors | the stamping step |
| the position sensor | the stamping step and the acquisition |
| the Siemens S7 | the motor acquisition and the automation |
| the Raspberry Pi | the preparation |
| ProCube | storing, merging, training, evaluation, inference |

Five of the twelve rows are AI functions on the external cloud. That is the
architectural decision of this case stated as a fact rather than as prose.

The same assignment carries a process step and an inference alike, which is the
question the whole alignment is built for.

## cq12

Seven rows: everything ProCube does and the data each function works on.

Training data, evaluation data and production data all leave the organisation,
since the training, the evaluation and the inference run in the external cloud.
For a plant this is the first question a review asks.

Two rows carry an empty data column, the storing and the merging. They are
assigned to the cloud but state no `usesData` of their own; what they act on is
reached through `isStoredBy` and `isProcessedBy` instead, which questions 04 and
10 report.

## cq13

Eight rows, one per resource and communication, and the direction is what makes
the answer readable.

On the fieldbus alone, three kinds of use appear: the two motors receive
commands and send process data, the position sensor only sends, and the control
does both. No single relation could express that, and the distinction is what
lets a model say which way data actually flows.

The three relations are independent rather than a hierarchy. Were the two
directed ones subproperties of `hasCommunication`, a reasoner would infer that
the sensor is bidirectional as well, which the model denies.


---

## Reading the answers across the three cases

Two questions are worth reading as a row rather than one case at a time.

### cq11, which resource carries which function

| | case 1 | case 2 | case 3 |
|---|---|---|---|
| rows | 12 | 17 | 13 |
| AI functions in the cloud | 5 | 6 | 3 |
| AI functions at the edge | 1 | 0 | 4 |

Case 2 puts everything in the cloud, case 3 splits the work in half. That is
the architectural decision of each case stated as a fact, and it follows from
the application: a wear classification tolerates minutes, a rework has to
finish inside the production cycle of one pane.

### cq12, what leaves the organisation

Case 3 is the shortest answer of the three, with four rows against seven. Only
the training and the test data go to the cloud; the data the inference works on
stays in the cell, because the inference does.

Moving the inference outward would lengthen this answer without changing a
single class of the ontology, which is what makes the question worth asking of
a design rather than of a finished plant.
