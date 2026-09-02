# ISO/IEC 22989 v1.0.0: what was changed and what was kept

This version publishes the model of the dissertation. It was cleaned up for
release, and this file records every change so that a reader can tell the model
from the cleanup.

Three sources describe this pattern, and they do not agree. Section 7 of the
dissertation and the three figures describe one model, the OWL file another.
The rule is that the dissertation is binding, so the text and the figures were
followed where they differ from the file.

---

## Where the OWL file was behind the dissertation

This is the largest difference of the three patterns, and it concerns the
algorithm view.

The OWL file has `MLAlgorithm` with no superclass, `MLModel`, an
`OptimizingMethod` with `GradientDescent` and `NetwonMethod` below it, and
`hasParameterMod` alongside `hasParameter`.

Section 7 and the figure `figures-iso22989-ai-v2` describe something else, and
that is what was built:

| | text and figure | OWL file |
|---|---|---|
| algorithms | `Algorithm` with `ModelAlgorithm`, `TrainingAlgorithm`, `EvaluationAlgorithm` | `MLAlgorithm` alone |
| machine learning | `MLAlgorithm` **below** `TrainingAlgorithm` | `MLAlgorithm` at the top |
| hyperparameter | on `Algorithm`, so every kind may carry one | on `Training` and `OptimizingMethod` |
| the model | `Model` | `MLModel` |
| model parameter | `hasParameter` from the model | `hasParameterMod` |
| gradient descent | "als **benannte Instanz** des `TrainingAlgorithm`" | a class below `OptimizingMethod` |

The text is explicit about the last point: a particular procedure such as
gradient descent is recorded as a named instance, not as a class. The classes
`OptimizingMethod`, `GradientDescent` and `NetwonMethod` are therefore gone.
The last of them was also misspelt.

---

## Corrected

### Namespace

`http://www.semanticweb.org/schieseck/ISO22989` was the value Protégé inserts
when none is given. Now `https://w3id.org/aias/odp/iso22989`, with the version
IRI `.../iso22989/1.0.0`.

### Class names follow the appendix table

The definition tables of the appendix write `AIFunction`, `AITask`,
`SymbolicAI`, `SubSymbolicAI`, `DataProcessing` and `Storing`. The OWL file
wrote `Function`, `Task`, `Symbolic`, `SubSymbolic`, `DataProcess` and
`Storage`. The tables were followed.

`DataProcess` is kept alongside `DataProcessing`, since the appendix uses both:
`DataProcessing` for the function of the life cycle, `DataProcess` for the
collecting class of the eight steps below it.

### `isPerformedBy` was symmetric

Declared `owl:SymmetricProperty` with a union of `MachineLearning` and
`Training` as both domain and range. A training is performed by a machine
learning, not the other way round.

### `TestData` and `EvaluationData` are equivalent

The figure `figures-iso22989-data` draws an `owl:equivalentClass` between them.
The OWL file carried them as two separate subclasses of `Data`, both inside the
disjointness axiom over the five kinds of data.

Equivalent and disjoint at once is a contradiction, and a reasoner would have
rejected the model. Both are therefore taken out of that axiom, which now
covers training, validation and production data.

### Comments were German only, some with broken umlauts

Every class and relation carries `@de` with the wording of the work and `@en`
with its translation. The definitions come from the four appendix tables where
they exist.

---

## Kept, though version 2.0.0 does it differently

| | 1.0.0 | 2.0.0 |
|---|---|---|
| `Automate` | a function of the life cycle | dropped: 3.1.7 defines automatic as an adjective, and control, 3.5.5, takes its place |
| `hasParameter` | one relation reaching a hyperparameter or a model parameter | two relations, `hasHyperparameter` and `hasParameter` |
| evaluation metrics | `Accuracy`, `Precision`, `Recall`, `F1Score` as classes | named individuals |
| `Model` | one class | `Model` with `MLModel` below it, so a rule-based system has a model without a training |

The last is the central distinction of version 2.0.0 and the reason it exists:
a symbolic system has a model that was written rather than learned, and one
class cannot say that.

---

## Not taken up

Everything version 2.0.0 adds stays out:

- the qualities of clause 3.5 with their values, controllability and risk
- the general model above the machine learning model
- the separation of a chosen hyperparameter value from a measured quality
- retraining, and the data sources and sinks as first-class parts of a chain

**Result:** 62 classes and 26 relations, against 95 classes, 9 named
individuals and 33 relations in version 2.0.0.

---

## For the author

Three places where the dissertation disagrees with itself:

1. **The OWL file and the algorithm figure describe different models.** The
   file has `MLModel`, `MLAlgorithm` without a superclass and an
   `OptimizingMethod`; the figure and section 7 have the `Algorithm` hierarchy.
   The figure was followed.

2. **`NetwonMethod`** is a misspelling of Newton in the OWL file. The class is
   gone here, so nothing carries the error forward.

3. **The appendix tables and the OWL file use different class names** for six
   terms, listed above. The tables were followed.
