# ISO/IEC 22989: Reference of All Entries

Every entry of clause 3 of ISO/IEC 22989:2022, Information technology,
Artificial intelligence, Artificial intelligence concepts and terminology, with
a note on whether the pattern takes it up.

The table exists so that the selection is checkable. Leaving an entry out is a
decision, not an oversight, and this is where those decisions are recorded.

**Why not all of them.** The standard is a vocabulary of a whole field, not a
modelling language. Clauses 3.4, 3.6 and 3.7 name techniques and application
tasks: activation functions, convolution, sentiment analysis, image recognition.
They are terms an engineer uses, not things an engineering model instantiates.
A model needing them records a concrete algorithm or task as a named individual
of the class above it, which keeps the pattern independent of libraries and
methods.

**What the selection follows.** An entry is taken up when it appears in a
relation of the pattern, or when it is documented what it is there for
otherwise. Standing in the standard is not sufficient on its own. The same rule
was applied to the IEC 60050-351 pattern, where six entries were dropped again
after review for failing it.

**Classes without an entry.** Some classes of this pattern have no entry in
clause 3. They are recorded in a separate section at the end, so the selection
stays checkable in both directions: the tables say which entries are taken up,
and that section says what is in the pattern without being an entry.

**No class of another namespace appears here.** The pattern stands on its own
and imports nothing. Where a term of this standard matches a term of another,
as control 3.5.5 matches IEC 60050-351, 351-42-19, word for word, the two are
related in the alignment ontology rather than in either pattern. A pattern that
referenced another would drag it along wherever it is used.

---

## What becomes a class, what becomes an individual

Three destinations, and the criterion is what the thing carries rather than how
many of them there are.

| Destination | For | Because |
|---|---|---|
| Class in the pattern | task kinds, data process steps, learning kinds, AI kinds | a model instantiates them and the instance carries its own statements |
| Individual in the pattern | `Cloud`, `Edge`, `Hybrid` | a closed choice the structure itself refers to, with nothing further to say about each |
| Individual in `ISO22989-instances.ttl` | the qualities of clause 3.5 | an open vocabulary a model states values against, and one it may ignore |

**Why the task kinds are classes.** A classification task in a model is a thing
of its own: some prediction fulfils it, some model addresses it, some metric
measures it. `Classification` names the kind of that thing, not the thing. As
an individual it would be the task itself, which is wrong as soon as two
classification tasks appear in one model.

**Why the process steps are classes.** The same holds for filtering or
normalisation: a concrete step has input data and output data of its own.

**Why the qualities are individuals.** Robustness is not something a model
contains, it is something a model states a value for. The value is the
instance, the quality is what it refers to.

**Clauses 3.4, 3.6 and 3.7 go nowhere at all**, not even into the instances
file. Neural network topologies, language processing tasks and vision tasks name
techniques and application fields, both of which are open sets. A model using a
convolutional network records it where the accompanying text of this work says
to record it:

    ex:ResNet50 a iso22989:ModelAlgorithm ;
        rdfs:label "ResNet-50, a convolutional neural network" .

A fixed list of techniques in this pattern would be a selection out of an open
field, out of date as soon as a method is added.

---

**47 of 115 entries** are taken up by the pattern.

---

## 3.1 Terms related to AI

35 entries, 10 taken up.

35 entries. The core of the pattern: what an AI system is, what it is made of
and what it does.

**Autonomy, 3.1.5, and heteronomy, 3.1.16, are left out**, and with them the
seven level scale of Table 1 in clause 5.13, which grades a system from no
automation to autonomy. The scale is normative vocabulary, but the models this
work targets are heteronomous throughout: an AI application in an automated
plant operates under external control by definition. A property whose value is
the same in every case records nothing, so the pattern leaves it out. The scale
can be taken up if a case ever needs to state a level.

*Entries not taken up*: the discipline of AI itself, 3.1.3, and its kinds,
3.1.14 and 3.1.24, which classify research rather than a system a model
records. The technique names, 3.1.8, 3.1.10, 3.1.11, 3.1.15, 3.1.26, 3.1.31 and
3.1.32, name approaches rather than elements of a system, and the same holds for
3.1.13. Robotics, 3.1.29 and 3.1.30, and the internet of things, 3.1.18 to
3.1.20, are neighbouring domains with their own vocabularies. Knowledge, 3.1.12,
3.1.21 and 3.1.28, would open a representation subject this pattern does not
cover. Hardware, 3.1.6, belongs to the plant view rather than here.

| Code | Term | In the pattern |
|---|---|---|
| 3.1.1 | AI agent | out, agent, an arrangement of the elements below rather than one of them |
| 3.1.2 | AI component | **AIComponent** |
| 3.1.3 | artificial intelligence | out, the discipline, not a system element |
| 3.1.4 | artificial intelligence system | **AISystem** |
| 3.1.5 | autonomy | out, see the note below the table |
| 3.1.6 | application specific integrated circuit | out, hardware, belongs to the plant view |
| 3.1.7 | automatic | **Automation** |
| 3.1.8 | cognitive computing | out, names an approach |
| 3.1.9 | continuous learning | out, a way of training rather than an element |
| 3.1.10 | connectionism | out, names an approach |
| 3.1.11 | data mining | out, names an approach |
| 3.1.12 | declarative knowledge | out, knowledge representation, out of scope |
| 3.1.13 | expert system | out, a kind of system, recorded through AIType instead |
| 3.1.14 | general AI | out, classifies research |
| 3.1.15 | genetic algorithm | out, names an approach |
| 3.1.16 | heteronomy | out, see the note below the table |
| 3.1.17 | inference | **Inference** |
| 3.1.18 | internet of things | out, neighbouring domain |
| 3.1.19 | IoT device | out, neighbouring domain |
| 3.1.20 | IoT system | out, neighbouring domain |
| 3.1.21 | knowledge | out, knowledge representation, out of scope |
| 3.1.22 | life cycle | out, the general systems engineering term, taken from ISO/IEC 15288 |
| 3.1.23 | model | **Model** |
| 3.1.24 | narrow AI | out, classifies research |
| 3.1.25 | performance | **Performance** |
| 3.1.26 | planning | out, names an approach |
| 3.1.27 | prediction | **Prediction** |
| 3.1.28 | procedural knowledge | out, knowledge representation, out of scope |
| 3.1.29 | robot | out, neighbouring domain |
| 3.1.30 | robotics | out, neighbouring domain |
| 3.1.31 | semantic computing | out, names an approach |
| 3.1.32 | soft computing | out, names an approach |
| 3.1.33 | symbolic AI | **SymbolicAI** |
| 3.1.34 | subsymbolic AI | **SubsymbolicAI** |
| 3.1.35 | task | **Task** |

## 3.2 Terms related to data

15 entries, 11 taken up.

15 entries. The data view: what data is, how it is grouped and what is done
to it before it is used.

*Entries not taken up*: exploratory data analysis, 3.2.6, and data quality
checking, 3.2.2, are activities of a project rather than elements of a system.
Ground truth, 3.2.7, is a value of a label rather than a thing of its own, and
personally identifiable information, 3.2.11, is a legal category that a model
records as an annotation rather than as a class.

| Code | Term | In the pattern |
|---|---|---|
| 3.2.1 | data annotation | **Annotation** |
| 3.2.2 | data quality checking | out, an activity of a project |
| 3.2.3 | data augmentation | **Augmentation** |
| 3.2.4 | data sampling | **Sampling** |
| 3.2.5 | dataset | **DataSet** |
| 3.2.6 | exploratory data analysis | out, an activity of a project |
| 3.2.7 | ground truth | out, a value of a label |
| 3.2.8 | imputation | **Imputation** |
| 3.2.9 | input data | **InputData** |
| 3.2.10 | label | **Label** |
| 3.2.11 | personally identifiable information | out, a legal category, recorded as an annotation |
| 3.2.12 | production data | **ProductionData** |
| 3.2.13 | sample | **Sample** |
| 3.2.14 | test data | **EvaluationData** |
| 3.2.15 | validation data | **ValidationData** |

## 3.3 Terms related to machine learning

17 entries, 13 taken up.

17 entries. Machine learning: the algorithm, the model it produces, the
parameters of both, and the kinds of learning.

*Entries not taken up*: the named algorithms, 3.3.1, 3.3.2 and 3.3.13, are
implementations. As the accompanying text of this work states, a concrete
algorithm is recorded as a named individual of the algorithm class rather than
as a class of its own, so that the pattern stays independent of libraries and
methods. Human-machine teaming, 3.3.3, describes an organisational arrangement
rather than a system element.

| Code | Term | In the pattern |
|---|---|---|
| 3.3.1 | Bayesian network | out, an implementation, recorded as a named individual |
| 3.3.2 | decision tree | out, an implementation, recorded as a named individual |
| 3.3.3 | human-machine teaming | out, an organisational arrangement |
| 3.3.4 | hyperparameter | **Hyperparameter** |
| 3.3.5 | machine learning | **MachineLearning** |
| 3.3.6 | machine learning algorithm | **MLAlgorithm** |
| 3.3.7 | machine learning model | **MLModel** |
| 3.3.8 | parameter | **ModelParameter** |
| 3.3.9 | reinforcement learning | **ReinforcementLearning** |
| 3.3.10 | retraining | **Retraining** |
| 3.3.11 | semi-supervised machine learning | **SemiSupervisedLearning** |
| 3.3.12 | supervised machine learning | **SupervisedLearning** |
| 3.3.13 | support vector machine | out, an implementation, recorded as a named individual |
| 3.3.14 | trained model | **TrainedModel** |
| 3.3.15 | training | **Training** |
| 3.3.16 | training data | **TrainingData** |
| 3.3.17 | unsupervised machine learning | **UnsupervisedLearning** |

## 3.4 Terms related to neural networks

10 entries, 0 taken up.

10 entries, none taken up.

The whole clause is implementation vocabulary: activation functions, convolution,
gradients and network topologies. A model that needs them records a neural
network as a named individual of the model algorithm class. Taking them up would
produce classes that no competency question reaches.

| Code | Term | In the pattern |
|---|---|---|
| 3.4.1 | activation function | out |
| 3.4.2 | convolutional neural network | out |
| 3.4.3 | convolution | out |
| 3.4.4 | deep learning | out |
| 3.4.5 | exploding gradient | out |
| 3.4.6 | feed forward neural network | out |
| 3.4.7 | long short-term memory | out |
| 3.4.8 | neural network | out |
| 3.4.9 | neuron | out |
| 3.4.10 | recurrent neural network | out |

## 3.5 Terms related to trustworthiness

18 entries, 13 taken up.

18 entries. Six are taken up, and one of them carries the pattern into the
control domain.

**3.5.5 control is defined here word for word as in IEC 60050-351, 351-42-19**:
purposeful action on or in a process to meet specified objectives. Both trace
back to the same source. That makes the two classes equivalent rather than
merely similar, and the alignment states it with owl:equivalentClass.

The pattern models it as a function rather than as a quality. The entry is
filed in this clause among the terms related to trustworthiness, but the
definition says action, which is what training, inference and validation are as
well. It therefore sits below AIFunction and a system relates to it through
hasFunction like any other activity.

**The qualities are a vocabulary, not classes.** Availability 3.5.3, bias
3.5.4, explainability 3.5.7, predictability 3.5.8, reliability 3.5.9,
resilience 3.5.10, robustness 3.5.12 and trustworthiness 3.5.16 are properties
a model states a value for, not things it instantiates. They are therefore
carried as named individuals of a Characteristic class in
`ISO22989-instances.ttl`, and a model relates a value to one of them:

    ex:RobustnessOfModel1 a iso22989:CharacteristicValue ;
        iso22989:forCharacteristic inst:Robustness ;
        iso22989:quantity "0.92"^^xsd:decimal .

This is the same construction the IEC 60050-351 pattern uses for settling time
and overshoot. Keeping the two patterns in the same shape makes the alignment
simpler, and it lets a model state a measured value without the pattern having
to prescribe a scale for it. Performance, 3.1.25, joins them from clause 3.1
for the same reason.

**Verification and validation are functions.** 3.5.17 and 3.5.18 define the two
as confirmations through objective evidence, of requirements and of intended
use respectively. Clause 5.16 and clause 6.2.4 treat them together as a stage
of the life cycle, so both are taken up as functions alongside training and
evaluation rather than as qualities.

*Entries not taken up*: accountability, 3.5.1 and 3.5.2, transparency, 3.5.14
and 3.5.15, and stakeholder, 3.5.13, are governance terms about organisations
rather than about a system.

| Code | Term | In the pattern |
|---|---|---|
| 3.5.1 | accountable | out, governance |
| 3.5.2 | accountability | out, governance |
| 3.5.3 | availability | **Availability** |
| 3.5.4 | bias | **Bias** |
| 3.5.5 | control | **Control** |
| 3.5.6 | controllability | **Controllability** |
| 3.5.7 | explainability | **Explainability** |
| 3.5.8 | predictability | **Predictability** |
| 3.5.9 | reliability | **Reliability** |
| 3.5.10 | resilience | **Resilience** |
| 3.5.11 | risk | **Risk** |
| 3.5.12 | robustness | **Robustness** |
| 3.5.13 | stakeholder | out, governance |
| 3.5.14 | transparency | out, governance |
| 3.5.15 | transparency | out, governance |
| 3.5.16 | trustworthiness | **Trustworthiness** |
| 3.5.17 | verification | **Verification** |
| 3.5.18 | validation | **Validation** |

## 3.6 Terms related to natural language processing

18 entries, 0 taken up.

18 entries, none taken up.

Natural language processing is a field of application, covered in clause 9.2 of
the standard as such. Its terms name tasks a concrete system performs, and a
model records those as named individuals of the task class rather than as
classes here.

| Code | Term | In the pattern |
|---|---|---|
| 3.6.1 | automatic summarization | out |
| 3.6.2 | dialogue management | out |
| 3.6.3 | emotion recognition | out |
| 3.6.4 | information retrieval | out |
| 3.6.5 | machine translation | out |
| 3.6.6 | named entity recognition | out |
| 3.6.7 | natural language | out |
| 3.6.8 | natural language generation | out |
| 3.6.9 | natural language processing | out |
| 3.6.10 | natural language processing | out |
| 3.6.11 | natural language understanding | out |
| 3.6.12 | optical character recognition | out |
| 3.6.13 | part-of-speech tagging | out |
| 3.6.14 | question answering | out |
| 3.6.15 | relationship extraction | out |
| 3.6.16 | sentiment analysis | out |
| 3.6.17 | speech recognition | out |
| 3.6.18 | speech synthesis | out |

## 3.7 Terms related to computer vision

2 entries, 0 taken up.

2 entries, none taken up.

Computer vision, like natural language processing, is a field of application.
The same reasoning applies.

| Code | Term | In the pattern |
|---|---|---|
| 3.7.1 | computer vision | out |
| 3.7.4 | image recognition | out |

---

## Classes without an entry in clause 3

Eleven classes of the pattern have no definition entry in the standard. Each is
recorded here so that a reader can tell a construct of this work from normative
vocabulary.

Three of them are drawn from prose clauses of the standard rather than from
clause 3, which is a weaker but still normative basis. The rest are constructs
of this work, carried over from the information model of the dissertation this
pattern rebuilds.

| Class | Basis | Why it is kept |
|---|---|---|
| `AIType` | clause 5.9, symbolic and subsymbolic approaches | the standard defines the two kinds, 3.1.33 and 3.1.34, but names no common superclass for them |
| `LearningType` | clause 5.11, machine learning concepts | the standard defines the four kinds of learning, 3.3.9 and 3.3.11 to 3.3.17, but names no common superclass |
| `AIFunction` | construct of this work | collecting class for the activities of the AI life cycle. Note that clause 8.3 uses the term AI function in a narrower sense, for computing a prediction alone |
| `Algorithm` | construct of this work | superclass of the three algorithm kinds below. The standard defines only the machine learning algorithm, 3.3.6 |
| `ModelAlgorithm` | construct of this work | the procedure describing the structure of a model, as against the parameters learned for it. Derived from 3.1.23 and 3.3.7 |
| `TrainingAlgorithm` | construct of this work | the procedure determining the parameters. 3.3.6 defines the machine learning case of it |
| `EvaluationAlgorithm` | construct of this work | the procedure assessing a model against a metric |
| `EvaluationMetric` | construct of this work | what an evaluation measures against, for example an F1 score |
| `SystemDesign` | construct of this work | where an AI system runs, that is cloud, edge or hybrid. Clause 8.6.2 discusses cloud and edge computing without defining the choice as a term |
| `DataProcess` | construct of this work | collecting class for the data preparation steps. The standard defines the steps, 3.2.1 to 3.2.8, but names no common superclass |
| `Acquisition` | construct of this work | obtaining data from a source. Discussed in clause 8.6.1 without an entry |
| `Storing` | construct of this work | persisting data to a sink. Discussed in clause 8.6.1 without an entry |
| `DataSource`, `DataSink` | construct of this work | where data comes from and where it goes. Needed for the two above |
| `Characteristic` | construct of this work | collecting class for the qualities of clause 3.5, which the standard defines without naming what they have in common |
| `CharacteristicValue` | construct of this work | the value a model states for a quality, reified so it can be annotated with its source. The same construction the IEC 60050-351 pattern uses |

### Subclasses named in prose rather than in clause 3

The standard names further terms in its prose clauses without giving them
entries. They are taken up as subclasses of the classes above, since a model
needs them to say what kind of task or step it is dealing with.

| Class | Superclass | Where the standard names it |
|---|---|---|
| `Classification`, `Regression`, `Clustering` | `Task` | note 2 to entry of 3.1.35 lists them as examples of tasks, and clause 9 discusses them |
| `Generation` | `Task` | clause 9.2, natural language generation, and the note to 3.1.27 |
| `DataProcessing` | `AIFunction` | clause 5.10, transforming input data into output data |
| `Filtering`, `Normalization`, `Labelling` | `DataProcess` | clause 5.10 names them among the preparation steps, alongside those with entries |
| `Cloud`, `Edge`, `Hybrid` | `SystemDesign` | clause 8.6.2, cloud and edge computing. The hybrid case is the combination of the two |
| `Evaluation` | `AIFunction` | clause 5.10 and clause 6.2.8, assessing a model before deployment |

The distinction matters for the alignment. A class with an entry carries the
wording of the standard as its definition. A class named in prose carries a
definition this work derived from that prose, and the note on the term says so.

**On the collecting classes.** Five of them, `AIType`, `LearningType`,
`AIFunction`, `Algorithm` and `DataProcess`, exist because the standard defines
a set of terms without naming what they have in common. An ontology needs that
superclass to relate the set to anything, so the pattern supplies it and says so
here. The IEC 60050-351 pattern carries the same construction for its
characteristics and control functions.


---

## Where this pattern departs from the information model it rebuilds

Three decisions differ from the ISO 22989 ontology of the dissertation. Each is
a correction rather than a restructuring, and each is recorded here because a
reader comparing the two would otherwise take the difference for an oversight.

### The hyperparameter sits on the algorithm, not on the training

The earlier model related the hyperparameter to the training, with the domain
of `hasParameter` given as the union of training and optimizing method. That
follows the process: a hyperparameter is what a training is set up with.

Entry 3.3.4 defines it otherwise, as a characteristic **of a machine learning
algorithm** affecting its learning process. This pattern follows the entry and
places it on the algorithm superclass, which also takes in the two cases the
earlier arrangement could not reach: the number of layers belongs to a model
algorithm and the fold count of a cross-validation to an evaluation algorithm,
and neither is a training. Question 12 returns all three on test case 1.

The earlier reading is still available, one step longer, since a training
reaches its algorithm through `basedOnAlgorithm`.

### `hasParameter` now carries the model parameter

A consequence of the above, and a trap when comparing the two models, since the
name survived but changed what it relates.

| | earlier model | this pattern |
|---|---|---|
| `hasParameter` | training to **hyperparameter** | model to **model parameter** |
| `hasParameterMod` | model to model parameter | dropped, the name above took its place |
| `hasHyperparameter` | did not exist | algorithm to hyperparameter |

The names now follow the entries: 3.3.4 is a hyperparameter and 3.3.8 is a
parameter, so `hasParameter` leads to the second.

### The value of a hyperparameter is reached by its own relation

The value chosen for a hyperparameter is a `CharacteristicValue`, the same
class that carries the values of the qualities of clause 3.5, but it is reached
by `hasSetting` rather than by `forCharacteristic`.

Both could have led there. Keeping them apart records where a value came from:
a hyperparameter is selected prior to training, in the wording of 3.3.4, and a
quality of clause 3.5 is established by one. The relation that leads to a value
therefore says whether it was stated or measured, which no single relation
could. Negative model 06 tests that a hyperparameter carries one value.

ML Schema keeps the same two apart, as `HyperParameterSetting` against the
qualities, which is a second reading of the same distinction rather than a
basis for it.
