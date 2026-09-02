# Test Cases: AIAS Alignment

Two test cases, generalised from the case studies of the dissertation this work
rebuilds. They keep the structure of those cases and drop the industry: a
product, a workpiece and a processing step stand where a glass pane, a foam and
a coating stood.

Two rules govern them, as for the four patterns:

1. **Built from the bridges, not from a standard.** The alignment rests on
   design decisions, and `ALIGNMENT.md` records each of them. A case exercises
   bridges rather than clauses.
2. **Every case spans at least three subdomains.** A model that stays inside
   one pattern belongs in that pattern, and so does the test for it.

| Case | Architecture | What sets it apart |
|---|---|---|
| 1 | cloud | the AI reports, and nothing acts on the process |
| 2 | hybrid | the AI acts back on the control of the plant |

**The difference between them is the point.** Both run the same kind of AI on
the same kind of plant. What differs is where the inference runs and whether
its output reaches the control, and those two differences are what the
alignment has to make visible. A model that could not tell them apart would not
support the architectural decision it exists for.

---

## The four levels

Both cases are built along the levels the dissertation uses, which the
alignment reproduces without naming them as a class of their own:

| Level | What sits there | Which pattern |
|---|---|---|
| 0 | the technical process, its steps and products | VDI 3682 |
| 1 | field devices: sensors and actuators | AIAS resources |
| 2 | controls, and an edge device where one is present | AIAS resources, IEC 60050 |
| 3 | cloud infrastructure | AIAS resources |

The levels are an arrangement for reading, not an axiom. What ties an element to
a level in the model is the kind of resource it is and what it is connected to.

---

## Case 1: an AI that reports

`tests/data/tc1_cloud.ttl`

A plant is monitored to plan maintenance before a part fails. Sensor data is
collected, sent to a cloud, and analysed there. The result is displayed to an
operator, who decides what to do with it.

Response times of minutes are acceptable, and the analysis being unavailable
for a while is acceptable too. **That is why everything runs in the cloud**,
and the model records the reason as much as the result.

### Level 0: the process

```turtle
ex:Step1 a vdi3682:ProcessOperator ;   # closing
    vdi3682:hasInput  ex:WorkpieceIn ;
    vdi3682:hasOutput ex:StateAfter1 .

ex:Step2 a vdi3682:ProcessOperator .   # processing
ex:Step3 a vdi3682:ProcessOperator .   # opening
```

Three steps and two products, connected by flows. Nothing here knows about AI.

### Level 1: the sensors

```turtle
ex:SensorLeft  a aias:Sensor .
ex:SensorRight a aias:Sensor .

ex:AcqLeft  a iso22989:Acquisition ; iso22989:hasDataSource ex:SensorLeft .
ex:AssignLeft a vdi3682:Assignment ;
    vdi3682:assignedResource ex:SensorLeft ;
    aias:assignedFunction    ex:AcqLeft .
```

Each sensor is a resource, and each carries an acquisition function. The
assignment is what ties the two, and it is the same class that ties a process
operator to a resource. **That is the point of the common function level**: one
mechanism for both.

### Level 2: the controls

```turtle
ex:MotorControl a aias:Controller .
ex:PositionControl a iec60050:ClosedLoopControl ;
    iec60050:runsOverActionPath ex:PathPos ;
    iec60050:hasAction          ex:ActionPos .
```

The motor control performs a closed-loop position control. **No AI is involved
in it**, and question 11 answers accordingly: the plant controls, the AI does
not. Case 2 differs exactly there.

An edge device sits at this level as well, but only as a bridge: the existing
control cannot reach the cloud on its own.

```turtle
ex:EdgeDevice a aias:EdgeDevice .
```

### Level 3: the cloud

```turtle
ex:Cloud a aias:ExternalCloud .

ex:Storing    a iso22989:Storing .
ex:Processing a iso22989:DataProcessing .
ex:Training   a iso22989:MachineLearning .
ex:Evaluation a iso22989:Evaluation .
ex:Inference  a iso22989:Inference .
```

All five AI functions are assigned to the cloud resource. The AI system states
`iso22989:Cloud` as its design, and question 09 checks that claim against the
assignments.

### The communication chain

```turtle
ex:CommSensorToControl a iso7498:Association ;
    iso7498:hasSourceSystem ex:SensorLeft ;
    iso7498:hasTargetSystem ex:MotorControl ;
    iso7498:transmits       ex:PduPosition .

ex:PduPosition a iso7498:ProtocolDataUnit ;
    iso7498:hasUserData ex:PayloadPosition .

ex:PayloadPosition a iso7498:UserData ;
    aias:carriesData ex:PositionData .

ex:PositionData a iso22989:TrainingData .
```

The chain is what questions 17 and 18 walk. A resource appears as an open
system when its communication is described, which the ISO 7498 pattern states
on that class. The payload carries the dataset, and the dataset keeps its
identity across every transmission that carries it.

### What the queries return

| Question | Answer on this case |
|---|---|
| 06 which resources perform AI functions | the cloud only |
| 09 design against assignments | cloud, and all AI functions sit there. No mismatch |
| 10 which functions run outside the plant | all five |
| 11 which controls does an AI perform | **none** |
| 12 which AI functions take part in a control | **none** |

The last two are the reason this case exists. An AI that reports is not an AI
that controls, and the model says which of the two it is.

---

## Case 2: an AI that acts

`tests/data/tc2_hybrid.ttl`

The same plant, a different task. A property of the product is checked during
production, and where the check fails, a correction is triggered **within the
same production cycle**.

That deadline is why the inference cannot run in a cloud. Training on image
data is computationally heavy and stays there, so the two are split. **The
architecture follows from the requirement**, and the model records both.

### What is the same

Levels 0 and 1 are built like case 1: process steps with products, sensors with
acquisition functions, assignments tying them together. A second sensor and an
actuator are added, since this case acts on the process rather than watching it.

### What differs: where the functions run

```turtle
ex:AISystem2 a iso22989:AISystem ;
    iso22989:hasDesign iso22989:Hybrid .

# on the edge device, inside the cycle
ex:Inference   a iso22989:Inference .
ex:Merging     a iso22989:DataProcessing .
ex:Correction  a iso22989:Control .        # <-- acts on the process

# in the cloud, outside the cycle
ex:Training    a iso22989:MachineLearning .
ex:Evaluation  a iso22989:Evaluation .
ex:Storing     a iso22989:Storing .
```

Question 09 checks `Hybrid` against these assignments and finds them
consistent. Had the model claimed `Edge` while training sits in a cloud, the
question would report the mismatch, and the reasoner would not object. OWL
cannot require the agreement, which is stated among the open points.

### What differs most: the AI reaches the control

```turtle
ex:Correction a iso22989:Control ;
    iso22989:usesData ex:InferenceOutput .

ex:CorrectionControl a iec60050:OpenLoopControl ;
    iec60050:runsOverActionPath ex:PathCorrection .
```

The output of the inference is the input of a function that acts on the plant.
That is the difference to case 1, and it is what questions 11 and 12 report.

**Why this matters beyond the model.** The dissertation records a rule that
fires here: whether an application intervening in a control counts as a control
task, and possibly as a high-risk application. The rule fired because the AI
output was modelled as the input of an automating function. The alignment can
now answer the question the rule asks, because control is defined identically
in ISO/IEC 22989, 3.5.5 and IEC 60050-351, 351-42-19, and the two are equivalent
classes. A model states one control, and both subdomains see it.

### The kind of control

`ex:CorrectionControl` is an `OpenLoopControl`. The correction is triggered on
a result and does not continuously influence what it measures, which is what
351-47-02 describes and what test case 1 of the IEC 60050-351 pattern shows in
detail.

A model claiming a closed loop here would have to record an action path that
returns and an action acting continuously. The IEC pattern would accept that
claim, since OWL cannot check it, but question 10 of that pattern would report
that the chain does not close.

### The chain of the plant control, resolved

The control of the plant is a different matter. `ex:PathControl` is a closed
loop performed without any AI, and this case states it in full: four functional
units after Figure 2 of IEC 60050-351, four action lines between them, and the
variable each line carries.

Two devices realise them. The robot control realises the comparing, the
controlling and the measuring element, the application unit realises the final
controlling element, and the controlled system is realised by nothing, since it
is the process rather than a device.

That detail is what question 13 needs. It is the only part of these two cases
modelled below the level of an architecture, and it is here because the bridge
from `aias:Resource` to `iec60050:PhysicalUnit` is otherwise asserted without
ever being walked.

### What the queries return

| Question | Case 1 | Case 2 |
|---|---|---|
| 06 resources performing AI functions | cloud | **edge and cloud** |
| 08 where each AI function runs | all in the cloud | **split by deadline** |
| 09 design against assignments | cloud, consistent | hybrid, consistent |
| 11 controls performed by an AI | none | **one** |
| 12 AI functions taking part in a control | none | **the inference** |
| 13 role of a resource in a control | empty, the path is not resolved | **four roles on two devices** |

Reading the two columns beside each other is what the alignment is for. Same
kind of plant, same kind of AI, and a different answer to whether the AI acts.

---

## Negative models

Each file under `tests/negative/` violates exactly one axiom, so a failure
names its own cause. All must be rejected by the reasoner. A model that is
accepted proves the axiom under test does not bite.

| File | Axiom | Basis |
|---|---|---|
| `neg01_function_is_component` | `aias:Function` and `aias:Component` are disjoint | A function is not a thing that performs it. Without the axiom a model could record a sensor that is its own acquisition |
| `neg02_product_is_resource` | `aias:Product` and `aias:Resource` are disjoint | A product is transformed, a resource transforms. The two roles are what the component level distinguishes |
| `neg03_relation_is_function` | `aias:Relation` and `aias:Function` are disjoint | An assignment ties a function to a resource and is not one of them |
| `neg04_data_is_userdata` | `iso22989:Data` and `iso7498:UserData` are disjoint | The bridge between them is a relation. Asserting one thing as both would be the equivalence `ALIGNMENT.md` argues against |

**Not tested, on purpose**: that a design disagrees with the assignments, or
that a function has no resource. Neither is an inconsistency. Both are findings
a query reports, and questions 07, 09 and 19 are how a reviewer finds them.

---

## What these cases do not cover

**No edge-only architecture.** A case with everything on one device would
exercise no bridge the two above leave untested, and the architectural question
this model exists for is about distribution.

**No symbolic AI.** Both cases use a learned model. The distinction between a
learned and a rule-based model is exercised in the ISO/IEC 22989 pattern, where
it belongs, and repeating it here would test that pattern rather than the
alignment.

**No closed-loop AI control.** Case 2 has an AI acting on the plant through an
open-loop control. An AI inside a closed loop is possible in the model and is
the case a safety review would look at hardest, but recording it well needs the
action path of the IEC 60050-351 pattern resolved into its chain, which makes
it a case for that pattern rather than for this one.

---

## Running

```bash
python ../shared/run_tests.py --package alignment
```

`RESULTS.md` carries every competency question with its result and an
interpretation.
