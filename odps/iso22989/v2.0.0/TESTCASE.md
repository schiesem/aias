# Test Cases: ISO/IEC 22989 Pattern

Three test cases built from the definitions of ISO/IEC 22989:2022, Information
technology, Artificial intelligence, Artificial intelligence concepts and
terminology.

Two rules govern these cases, the same as for the other patterns:

1. **Taken from the standard.** Each case is built from the definitions of
   clause 3, and the element names stay generic. The standard is a vocabulary
   rather than a set of worked examples, so the cases follow its definitions
   rather than an application.
2. **Independent of the alignment.** No test case assumes anything about a
   technical process, a communication or a control. They exercise the ISO 22989
   pattern alone, so a failure can only come from this pattern.

| Case | Kind of AI | Covers |
|---|---|---|
| 1 | subsymbolic | the full machine learning life cycle, from acquisition to inference |
| 2 | symbolic | a model without training, and the parameters that are not learned |
| 3 | both | one system using two approaches, and what that implies for disjointness |

Case 2 is the one that carries the most weight. It is what justifies keeping
`Model`, 3.1.23, apart from `MLModel`, 3.3.7: a symbolic system has a model
without ever learning it, and a pattern that only knew the learned kind could
not record such a system at all.

---

## Why the three kinds matter

ISO/IEC 22989 distinguishes two approaches, and the distinction runs through
the whole pattern.

**Symbolic AI**, 3.1.33, is based on techniques and models that *manipulate
symbols and structures according to explicitly defined rules to obtain
inferences*. Note 1 to that entry adds that it produces declarative outputs.

**Subsymbolic AI**, 3.1.34, is based on techniques and models that *use an
implicit encoding of information, that can be derived from experience or raw
data*. The same note adds that it rests on statistical approaches and produces
outputs with a given probability of error.

### What follows for the model

Both definitions speak of a **model**, and both reference 3.1.23, the general
entry: a physical, mathematical or otherwise logical representation. Neither
references 3.3.7, the machine learning model.

That is why the pattern carries both classes, with `MLModel` below `Model`:

| Class | Clause | Comes from |
|---|---|---|
| `Model` | 3.1.23 | any representation, however it was arrived at |
| `MLModel` | 3.3.7 | a mathematical construct generating an inference, produced by training |

A symbolic system instantiates `Model` and nothing below it. A subsymbolic one
instantiates `MLModel`, and 3.3.15 says where its parameters came from.

### What follows for the parameters

The two parameter entries divide along the same line:

| Class | Clause | Definition | Chosen |
|---|---|---|---|
| `ModelParameter` | 3.3.8 | internal variable of a model that affects how it computes its outputs | by training |
| `Hyperparameter` | 3.3.4 | characteristic of an algorithm that affects its learning process | before training, by a person |

A rule threshold in a symbolic system is chosen in advance and steers the
behaviour of the procedure, which is what 3.3.4 describes. It is therefore a
hyperparameter, not a model parameter, and case 2 records it that way.

The wording of 3.3.4 names the machine learning algorithm specifically, so
applying it to a rule-based procedure is a reading of the entry rather than the
entry itself. The pattern records that reading on the class, and case 2 is where
it becomes visible.

### The two kinds are not disjoint

3.1.33 and 3.1.34 compare the two approaches without excluding one another, and
clause 5.9 discusses combining them. A system may therefore use both, which case
3 asserts. A pattern declaring them disjoint would make such a system
inconsistent, and hybrid systems are common enough that this would be a defect
rather than a safeguard.

---

## Case 1: a subsymbolic system

`tests/data/tc1_subsymbolic.ttl`, after 3.1.34, 3.3.5, 3.3.7 and 3.3.15.

A system that learns a classifier from labelled data and runs it. The full life
cycle, and the case every other one is read against.

### Step 1: the system, its kind and its task

```turtle
ex:SystemA  a  iso:AISystem ;
    iso:hasType    iso:SubsymbolicAI ;      # 3.1.34
    iso:hasTask    ex:TaskA ;
    iso:hasDesign  iso:Edge .

ex:TaskA a iso:Classification .             # a kind of task, clause 9
```

3.1.4 defines the AI system as an engineered system generating outputs for a
given set of human-defined objectives. The task is what those objectives are,
3.1.35, and the design is where the system runs.

### Step 2: the algorithms

Three kinds, and this case has all three:

```turtle
ex:ModelAlgA a iso:ModelAlgorithm ;         # the structure of the model
    iso:hasHyperparameter ex:HP_Layers .

ex:TrainAlgA a iso:MLAlgorithm ;            # 3.3.6, determines the parameters
    iso:basedOnLearning iso:SupervisedLearning ;   # 3.3.12
    iso:hasHyperparameter ex:HP_LearningRate .

ex:EvalAlgA a iso:EvaluationAlgorithm ;
    iso:usesMetric ex:MetricA .
```

`MLAlgorithm` is the only one of the three with an entry, 3.3.6. The other two
are constructs of this work, which `REFERENCE.md` records. `Hyperparameter`,
3.3.4, sits on the algorithm superclass, so all three may carry one.

3.3.12 defines supervised machine learning as using only labelled data during
training, which is what step 5 records.

### Step 3: the functions of the life cycle

```turtle
ex:SystemA iso:hasFunction
    ex:AcquisitionA , ex:ProcessingA , ex:TrainingA ,
    ex:ValidationA , ex:EvaluationA , ex:InferenceA .
```

Six functions, in the order the life cycle runs. Each is related to the data it
uses, which is what makes the order visible in a query rather than only in the
naming.

### Step 4: training produces the model

The step where the pattern earns the distinction between algorithm and model:

```turtle
ex:TrainingA a iso:Training ;               # 3.3.15
    iso:basedOnAlgorithm ex:TrainAlgA ;
    iso:usesData         ex:TrainDataA ;
    iso:determines       ex:MP_Weights .    # 3.3.8

ex:ModelA a iso:MLModel ;                   # 3.3.7
    iso:basedOnAlgorithm ex:ModelAlgA ;
    iso:hasParameter     ex:MP_Weights ;
    iso:isCreatedBy      ex:TrainingA .
```

3.3.15 defines training as the process determining or improving the parameters
of a machine learning model, based on an algorithm and using training data.
3.3.14 calls the result a trained model.

The model is therefore the algorithm **plus** the parameters the training
determined. Without the parameters the algorithm is a procedure, with them it is
a model that computes something.

### Step 5: the data, and its disjointness

```turtle
ex:TrainDataA a iso:TrainingData ;   iso:isLabelled true .    # 3.3.16
ex:ValDataA   a iso:ValidationData .                          # 3.2.15
ex:EvalDataA  a iso:EvaluationData .                          # 3.2.14
ex:ProdDataA  a iso:ProductionData .                          # 3.2.12

[] a owl:AllDisjointClasses ;
   owl:members ( iso:TrainingData iso:ValidationData iso:EvaluationData ) .
```

The notes to 3.2.14 and 3.2.15 state that test data is disjoint from training
and validation data. The pattern asserts it, and negative model 01 tests that
the assertion bites. It is what keeps an evaluation honest: a model evaluated on
data it was trained on says nothing about its performance.

Production data, 3.2.12, is not part of that disjointness. It arises during
operation, so it cannot overlap with data that existed beforehand.

### Step 6: inference and prediction

```turtle
ex:InferenceA a iso:Inference ;             # 3.1.17
    iso:usesData     ex:ProdDataA ;         # 3.2.9, the input data
    iso:isExecutedBy ex:ModelA ;
    iso:creates      ex:PredictionA .

ex:PredictionA a iso:Prediction ;           # 3.1.27
    iso:fulfilsTask ex:TaskA .
```

3.1.27 defines the prediction as the primary output of an AI system when given
input data. `fulfilsTask` closes the circle back to step 1: what the system was
built for is what the prediction addresses.

### Step 7: data processes, source and sink

```turtle
ex:AcquisitionA a iso:Acquisition ; iso:hasDataSource ex:SourceA .
ex:StoringA     a iso:Storing ;     iso:hasDataSink   ex:SinkA .

ex:ProcessingA a iso:DataProcessing ;
    iso:consistsOfStep ex:StepNorm , ex:StepLabel .

ex:StepNorm  a iso:Normalization .
ex:StepLabel a iso:Labelling .
```

Acquisition and storing are the two functions reaching outside the AI system,
which makes them the handover point to whatever supplies or receives the data.

### Step 8: a quality

```turtle
ex:CV_Robustness a iso:CharacteristicValue ;
    iso:forCharacteristic inst:Robustness ;     # 3.5.12
    iso:quantity "0.92"^^xsd:decimal .
```

The same construction the IEC 60050-351 pattern uses for settling time and
overshoot. The value is reified so a model can annotate where it came from, and
`forCharacteristic` is functional: one value quantifies one quality.

---

## Case 2: a symbolic system

`tests/data/tc2_symbolic.ttl`, after 3.1.33 and 3.1.23.

A system whose model is a set of explicitly defined rules. Nothing is learned,
and the case exists to show what the pattern records when nothing is.

### What is present

```turtle
ex:SystemB  a  iso:AISystem ;
    iso:hasType   iso:SymbolicAI ;          # 3.1.33
    iso:hasTask   ex:TaskB ;
    iso:hasDesign iso:Edge .

ex:ModelB a iso:Model ;                     # 3.1.23, NOT MLModel
    iso:basedOnAlgorithm ex:RuleAlgB .

ex:RuleAlgB a iso:ModelAlgorithm ;
    iso:hasHyperparameter ex:HP_Threshold .

ex:HP_Threshold a iso:Hyperparameter .      # 3.3.4, chosen in advance

ex:SystemB iso:hasFunction ex:AcquisitionB , ex:InferenceB .
```

### What is absent, and has to be

| Absent | Why |
|---|---|
| `MLModel` | 3.3.7 defines it as produced by training. Nothing was trained. |
| `Training`, `Validation`, `Evaluation` | there are no parameters to determine and no candidate models to compare |
| `TrainingAlgorithm`, `MLAlgorithm` | 3.3.6 determines parameters from data. There is no such step |
| `ModelParameter` | 3.3.8 defines it as an internal variable. The thresholds were chosen, not computed |
| `TrainingData`, `ValidationData`, `EvaluationData` | only production data arises, 3.2.12 |
| `LearningType` | nothing learns |

**The thresholds are hyperparameters.** 3.3.4 defines the hyperparameter as a
characteristic of an algorithm affecting its learning process, chosen prior to
training. A rule threshold is chosen the same way and steers the behaviour of
the procedure the same way, which is why the pattern places it there. The
wording of the entry names machine learning specifically, so this is a reading
of it, recorded as such on the class.

### What the queries return

Question 15 asks which trainings are machine learning. On this case the answer
is empty, and that emptiness is the assertion: a model exists, it was not
learned, and the pattern can say so.

Question 17, which model parameters a model has, is likewise empty here and
populated in case 1. Read together the two cases show what training adds.

---

## Case 3: a system using both

`tests/data/tc3_hybrid.ttl`, after 3.1.33, 3.1.34 and clause 5.9.

One system with two components: one that learned a classifier, one that decides
what to do with its output by rule.

```turtle
ex:SystemC a iso:AISystem ;
    iso:hasType iso:SubsymbolicAI , iso:SymbolicAI ;   # both
    iso:hasDesign iso:Hybrid ;
    iso:consistsOf ex:ComponentC1 , ex:ComponentC2 .

ex:ComponentC1 a iso:AIComponent ;          # 3.1.2
    iso:hasFunction ex:InferenceC1 ;
    iso:realisedByModel ex:ModelC1 .        # an MLModel, as in case 1

ex:ComponentC2 a iso:AIComponent ;
    iso:hasFunction ex:InferenceC2 ;
    iso:realisedByModel ex:ModelC2 .        # a Model, as in case 2
```

### What it puts under test

**The two kinds of AI are not disjoint.** `ex:SystemC` is typed as both, and the
model has to stay consistent. 3.1.33 and 3.1.34 compare the two without
excluding one another, and clause 5.9 discusses combining them. A pattern
declaring them disjoint would reject a system that the standard describes.

**A component is what carries a function.** 3.1.2 defines the AI component as a
functional element constructing an AI system. Cases 1 and 2 relate functions to
the system directly, which is enough while there is one of each. Here two
components perform the same kind of function differently, so the intermediate
step is what keeps them apart.

**The prediction of one is the input of the other.** `ex:PredictionC1` is
produced by the subsymbolic component and used by the symbolic one, which the
chain records.

### The system performs a control

```turtle
ex:SystemC iso:hasFunction ex:ControlC .
ex:ControlC a iso:Control .                 # 3.5.5
```

Purposeful action on or in a process to meet specified objectives. The entry is
filed in clause 3.5 with the terms related to trustworthiness, but the
definition says action, which is what training, inference and validation are as
well, so the pattern models it as a function alongside them.

Recording it is what lets a model state that a system acts on something rather
than only computing outputs. The definition is word for word the one
IEC 60050-351 gives in 351-42-19, which makes this the class the alignment joins
the two subdomains at.

### The design is hybrid

3.1.4 says nothing about where a system runs. Clause 8.6.2 discusses cloud and
edge computing, and the pattern carries `Cloud`, `Edge` and `Hybrid` as
individuals of `SystemDesign`. Case 3 uses `Hybrid`, since one component runs
near the process and the other elsewhere.

---

## Negative models

Each file under `tests/negative/` violates exactly one axiom, so a failure
names its own cause. All must be rejected by the reasoner. A model that is
accepted proves the axiom under test does not bite.

| File | Axiom | Normative basis |
|---|---|---|
| `neg01_data_kinds_overlap` | `TrainingData` and `EvaluationData` are disjoint | note 1 to 3.2.14, test data is disjoint from training and validation data |
| `neg02_model_is_algorithm` | `Model` and `Algorithm` are disjoint | 3.1.23 defines a representation, 3.3.6 a procedure. One is not the other |
| `neg03_two_learning_types` | `basedOnLearning` is functional | an algorithm uses one kind of learning, 3.3.9 to 3.3.17 |
| `neg04_data_is_function` | `Data` and `AIFunction` are disjoint | data is not the activity processing it |
| `neg05_value_for_two_qualities` | `forCharacteristic` is functional | one value quantifies exactly one quality |

**Not tested, on purpose**: that a system is both symbolic and subsymbolic. Case
3 asserts exactly that and must stay consistent, so the opposite is not an
error to catch.

---

## Running

```bash
python ../../shared/run_tests.py --package iso22989
```

`RESULTS.md` carries every competency question with its result and an
interpretation.
