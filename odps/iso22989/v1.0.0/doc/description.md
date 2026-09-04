<!-- description
     Written by hand, the source for the Widoco section of the same name.
     Never edit the generated HTML. -->

Sixty-two classes and twenty-five relations, arranged in three views. Every
class carries a German wording alongside its English translation, and the
`skos:note` of each element names the clause of ISO/IEC 22989 it rests on. Where
a class is a term of engineering practice rather than of the standard, the note
says so.

## The system

An `AISystem` is what is being described. It reaches its parts through
`consistsOf`, which takes in `AIComponent`, and it carries an `AIType`, either
`SymbolicAI` or `SubSymbolicAI`.

A `SystemDesign` says where the system runs: `Cloud`, `Edge` or `Hybrid`. This
is the class that turns an architectural decision into a statement a query can
read, rather than something a reader has to infer from a diagram.

An `AITask` is what the system is asked to do, one of `Classification`,
`Clustering`, `Regression` or `Generation`. A `Prediction` produced by the
system addresses a task, so what a model outputs can be checked against what it
was built for.

## Functions of the life cycle

An `AIFunction` is a step of the life cycle. Nine are supplied:

| Function | What it does |
|---|---|
| `Acquisition` | records data from a source |
| `DataProcessing` | prepares it |
| `Storing` | writes it to a sink |
| `Training` | produces a model from data |
| `Validation` | checks the model during training |
| `Evaluation` | measures the finished model |
| `Inference` | runs the model on new data |
| `Automate` | acts on what the inference produced |
| `DataProcess` | the eight preparation steps, below |

A function is the level at which this pattern meets the others. In the AIAS
alignment a function and a process operator are treated alike, so the same
assignment that ties a stamping step to a motor ties an inference to a cloud.

`DataProcess` collects the eight steps of preparation: `Annotation`,
`Augmentation`, `Filtering`, `Imputation`, `Labeling`, `Merging`,
`Normalization` and `Sampling`.

> `Labeling` and `Merging` are not defined as processes of their own by the
> standard. Labelling is discussed in clause 5.10 as part of annotation, and
> merging is a construct of this model for the step that joins several datasets
> into one. Both notes say so.

## Algorithms and models

An `Algorithm` is a parameterisable mathematical procedure. Three kinds are
distinguished by what they are used for: `ModelAlgorithm`, `TrainingAlgorithm`
and `EvaluationAlgorithm`, with `MLAlgorithm` below the training algorithm.

A `Model` is what a training produces, reached through `isCreatedBy`, and it
runs an inference through `executes`. It carries `ModelParameter`, the values
the training fixed.

A `Hyperparameter` is set before the training rather than learned by it. It
hangs on `Algorithm`, the superclass, which is what lets a model algorithm and
an evaluation algorithm carry one as well: the number of layers of a network,
the threshold of a metric.

`hasParameter` is one relation with two domains, for the hyperparameter of an
algorithm and the parameter of a model.

`MachineLearning` performs a training, and a `LearningType` says which kind:
`SupervisedLearning`, `UnsupervisedLearning`, `SemiSupervisedLearning` or
`ReinforcementLearning`.

An `EvaluationMetric` measures a finished model, one of `Accuracy`,
`Precision`, `Recall` or `F1Score`.

## Data

A `DataSet` is composed of `Data`, and data of `Sample`. `isComposedOf` is one
relation used at both levels, so its domain and range are unions covering each.

Five kinds of data are distinguished by the role they play:

- `TrainingData`, what a training consumes
- `ValidationData`, what checks the model while it is being trained
- `TestData` and `EvaluationData`, which measure the finished model
- `ProductionData`, what the plant produces in operation

> `TestData` and `EvaluationData` are stated as **equivalent**. They name the
> same thing, one in the wording of the standard and one in the wording of
> practice, and equating them means a model written with either term answers
> the same query.

A `DataSource` is where data comes from, a `DataSink` where it is written. The
relations `isAcquiredBy`, `isProcessedBy` and `isStoredBy` tie a dataset to the
functions acting on it, which is what makes provenance answerable: follow
`isProcessedBy` backwards from a merged dataset and every origin appears.

## Disjointness

The root classes are pairwise disjoint, and so are the members of each set of
subclasses: the four tasks, the four learning types, the three system designs,
the four metrics and the kinds of data. Nothing can be a task and a metric at
once.

`TestData` and `EvaluationData` cannot be disjoint from **each other**, since
they are equivalent. Against the other three kinds of data they are, which a
second axiom states: training, validation and production data on one side,
evaluation data on the other.
