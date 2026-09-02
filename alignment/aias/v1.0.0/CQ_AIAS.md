# Competency Questions: AIAS Alignment, version 1.0.0

Thirteen questions asked of the three cases of the dissertation: the worked
example of the concept chapter and the two case studies of the evaluation.

Every question is answered from the A-box of the modelled case. A question
whose answer would be the same with no case loaded belongs in the
documentation of the ontology rather than here, and the test runner enforces
that.

The answer column states what a query returns, not how it is computed.

---

## A. Where the AI runs

| ID | Competency question | Answer |
|---|---|---|
| 01 | Where is the AI trained? | Training, resource, kind of resource |
| 05 | Where does a model run? | Model, its inference, the resource carrying it |
| 11 | Which resource carries out which function? | Resource, kind, function, kind |
| 12 | Which data leaves the organisation? | Resource, function, data, kind |

## B. What goes in and what comes out

| ID | Competency question | Answer |
|---|---|---|
| 02 | What does an inference take in, and what does it produce? | Inference, input, output, the task it addresses |
| 03 | What does a training take in, and what does it produce? | Training, input, the parameters it fixes, the model carrying them |

## C. Data along its way

| ID | Competency question | Answer |
|---|---|---|
| 04 | Which data is stored, and where? | Data, storing, sink, resource |
| 09 | Which data is recorded, and where? | Data, kind, acquisition, source, resource |
| 10 | Where is data merged, and out of what? | Merging, resource, inputs, output |
| 13 | How is a component tied to a communication? | Component, kind, direction of use, communication |

## D. Artefacts and gaps

| ID | Competency question | Answer |
|---|---|---|
| 06 | Which artefact is a model, and which training produced it? | Model, path of the file, training, algorithm |
| 07 | Which hyperparameters does an algorithm carry, and in which artefact? | Algorithm, kind, hyperparameter, path of the file |
| 08 | Which functions are assigned to no resource? | Function, kind. Empty where every function is carried |

---

## On questions 06 and 07

Neither asks for a place, and that is deliberate.

The label of a model instance is the relative path of the file it stands for,
`models/ProductionNet_v1.onnx`, and the label of a hyperparameter is the path
of its configuration file. That is how the dissertation ties the abstract model
to what is actually deployed: a name in the graph is a path in the project.

Adding a relation from a model to a resource would state something the model
does not know. Where a file lies is a matter for the deployment, not for the
description of the system, and the ontology of the dissertation carries no such
relation.

## On question 13

The three relations are independent, not a hierarchy. `hasCommunication` states
a bidirectional use, `hasInputCommunication` a use as a receiver,
`hasOutputCommunication` a use as a sender.

Making the two directed ones subproperties of the first would let a reasoner
infer that a sensor which only sends is also bidirectional, which is the
opposite of what the model states.
