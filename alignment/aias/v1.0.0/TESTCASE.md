# Use cases of the AIAS alignment, version 1.0.0

The cases of the dissertation, modelled with this version. They show that the
model carries a real application rather than testing the ontology against
constructed edge cases the way the 2.0.0 does: there are no negative models
here, and nothing is built to fail.

Thirteen competency questions run against all three, which `CQ_AIAS.md` lists.
Reading one answer across the three columns is how the difference between the
architectures becomes visible.

| Case | Where it comes from | What it shows |
|---|---|---|
| 1 | the worked example of the concept | a cloud architecture with edge preparation |
| 2 | case study 1 of the evaluation | the same plant in full, and why the cloud |
| 3 | case study 2 of the evaluation | a hybrid architecture, and an AI that acts |

**Reading cases 2 and 3 beside each other is the point.** Both are the same
kind of plant and the same kind of AI. What differs is where the inference
runs and whether its output reaches the process, and both differences follow
from the application rather than from the technology.

---

## Case 1: stamping process with belt wear

`tests/data/tc1_stanzprozess.ttl`

### The application

A stamping machine produces sheet metal parts. A movable punch is driven by two
electric motors through a belt, and a position sensor records where the punch
is.

As the belt wears the punch positions less accurately, and the parts leave
their tolerance. The belt is therefore replaced at fixed intervals, which costs
more than it needs to. **The AI classifies the state of the belt** so that
maintenance can follow the condition rather than the calendar.

### The architecture

```
   two motors, one sensor
            │  Profibus1
            ▼
      Siemens S7                    control
            │  Ethernet1
            ▼
     Raspberry Pi 4                 edge: preparation
            │  Internet1
            ▼
        ProCube                     cloud: storing, training,
                                    evaluation, inference
            │
            └──► the classified state goes back to the control
```

The design is `Cloud`, not `Hybrid`: only the preparation of the data sits at
the edge, while the inference runs in the cloud. That is the decision the model
is meant to make visible, and it follows from the application rather than from
the technology — a wear classification tolerates a delay of minutes.

### What the model states

45 individuals across the three subdomains.

**The process.** Two products, one operator, two flows. A flow carries a state
and enters or leaves an operator, which is how version 1.0.0 models it:

```turtle
ex:InputStanze a vdi3682:Flow ;
    vdi3682:isInput  ex:Stanzen ;
    vdi3682:hasState ex:Blech .
```

**The devices.** Two actuators, one sensor, one controller, one edge device and
one external cloud. Each is tied to what it does through an assignment, and
`isAssignedTo` runs along both steps of that chain: from the operator to the
assignment, and from the assignment to the resource.

**The communication.** Three communications, and the direction is what tells
the three ways of taking part apart:

| Resource | Relation | Why |
|---|---|---|
| the two motors | `hasCommunication` | they receive commands and send process data |
| the position sensor | `hasOutputCommunication` | it only sends |
| the Siemens S7 | `hasCommunication` | it receives sensor data and sends commands |
| ProCube | `hasInputCommunication` | it only receives, over the internet |

**The data.** One dataset appears in four places, and that is the point of the
model rather than a redundancy:

```turtle
ex:RawPositionData a iso22989:ProductionData ;
    iso22989:isAcquiredBy  ex:PositionDataAcquisition ;
    iso22989:isProcessedBy ex:Vorverarbeitung ;
    iso22989:isStoredBy    ex:Speicherung .

ex:Profibus1  iso7498:hasDataUnit ex:RawPositionData .
ex:Ethernet1  iso7498:hasDataUnit ex:RawPositionData .
```

The same instance is acquired once, travels over two communications and is then
prepared. A model can therefore say where a given dataset comes from, what
carries it and what is done with it. That works because this version equates
`iso7498:Data` with `iso22989:Data`.

**The AI.** Training with a hyperparameter file produces a model file, which is
evaluated and then runs the inference:

```turtle
ex:ProductionNet_v1 a iso22989:Model ;
    iso22989:isCreatedBy   ex:Training1 ;
    iso22989:hasParameter  ex:ModelParam1 ;
    iso22989:isEvaluatedBy ex:Evaluation1 ;
    iso22989:executes      ex:Inferenz1 .
```

The instances point at real artefacts, `config/MLflowHyperParameter1.json` and
`models/ProductionNet_v1.onnx`. That is how the dissertation ties the abstract
model to what is actually deployed: a name in the graph is a path in the
project.

**Which resource carries which function.** The same `vdi3682:Assignment` that
ties a stamping step to a motor also ties an inference to a cloud. One
mechanism for both, which is what the common function level of the alignment
exists for.

### Where the figures and the model differ

The five knowledge graphs of section 7 draw this case. Two carry slips that the
model does not follow:

- `figures-wissensgraph-dataflow` writes `ex:SiemensS6` for the control, which
  is `SiemensS7` everywhere else, and prefixes `isAcquiredBy` with `ISO7489`
  rather than `ISO22989`
- `figures-wissensgraph-communication` prefixes the three communication
  relations with `ISO7489`, although the alignment defines them:
  `AIAS:hasCommunication` and the two that give it a direction

Both are prefix slips in the drawings. The structure they show is unambiguous
and is what this model states.


---

## Case 2: condition-based maintenance of drive belts

`tests/data/tc2_eki_instandhaltung.ttl`

The full version of the case that case 1 is an excerpt of. A plant foams glass
panes with polyurethane; two electric motors move the upper die through drive
belts, and a belt in need of maintenance makes the position data oscillate
while the tool opens and closes. The wear can therefore be read from the
movement itself.

### What it adds over case 1

| | case 1 | case 2 |
|---|---|---|
| process | one step, two products | five steps, eight product states |
| sensors | one | two, left and right |
| controls | one | a machine control and a motor control |
| acquisitions | one | three, feeding one merging |

86 individuals against 45.

### Where the architecture comes from

The application has no real-time requirement. Answers within minutes are
acceptable and the analysis may be unavailable for a while, so every AI
function sits in the cloud and the design is `Cloud`.

Two consequences are modelled rather than described. The existing control
cannot reach the cloud, so a Raspberry Pi sits between them. And the machine
control carries a function of its own that fetches the result when an operator
calls it up, which is why the answer to "which resource carries which function"
names the control twice.

### What the answers show

Three process steps carry no resource: loading, foaming and unloading. Only
closing and opening are assigned to the sensors, because those are the two
steps in which a worn belt shows itself. Question 08 reports the three, and the
answer is a property of the case rather than a gap in it.

The merging runs on the machine control, not in the cloud. It joins the two
position signals and the time stamps into one dataset, and only that dataset
travels onward. Reading question 10 and question 12 together shows what
actually leaves the organisation.

---

## Case 3: gaps in a primer coat

`tests/data/tc3_eki_primerauftrag.ttl`

Before a pane is foamed, a primer is applied to the faces the foam will cover.
A gap in that coat risks the polyurethane coming loose later. A camera is added
to the cell, the panes carry RFID tags, and the AI classifies each segment of
the path as coated or faulty.

### What sets it apart: the AI acts

In cases 1 and 2 the AI reports a state to an operator. Here its output is the
input of a function that moves the robot:

```turtle
ex:Modelausfuehrung iso22989:creates ex:Segmentbewertung .

ex:Segmentnacharbeitssteuerung a iso22989:Automate ;
    iso22989:usesData ex:Segmentklassifikation .
```

The rework happens inside the same production cycle, which is what makes the
architecture hybrid rather than a matter of taste.

### Why the split

| | where | why |
|---|---|---|
| inference, merging, preparation, rework | edge | the cycle of one pane is the deadline, and it has to work without an internet connection |
| storing, training, evaluation | cloud | training on image data is computationally heavy |

Question 12 shows what that buys: only the training and test data leave the
organisation. The data the inference works on stays in the cell.

### A product that communicates

```turtle
ex:ScheibeMitRFID aias:hasOutputCommunication ex:ScheibeZuRFIDReader .
```

The pane carries an RFID tag and is read as it passes, which is what ties a
picture to the pane it shows. A product taking part in a communication is the
reason the relation reaches a component rather than a resource, and this case
is where that decision earns itself.

### Three sources, one merging

To place a gap on a pane the model needs three things at once: the picture, the
identification of the pane, and the segment of the path the picture was taken
at. The robot control divides the path into a fixed number of segments, which
is what lets a picture be tied to a place.

The merging runs on the edge device rather than in the cloud, because what it
produces is the input of an inference that must finish inside the cycle.

### What the model does not have

There is no deployment model for this case, only a concept model, so this is
the last state that exists. The evaluation metric of case 2 has no counterpart
here, and the hyperparameters are not recorded.
