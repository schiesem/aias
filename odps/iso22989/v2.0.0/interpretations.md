# Interpretations of the competency question results

Source text for `RESULTS.md`, which the test runner generates. Everything else
in that report is produced from the queries and the recorded results, so it
cannot go stale. These interpretations are written by hand and have to be kept
in step with the models.

Format: one `## cqNN` heading per question, followed by free text. A question
without an entry appears in the report marked as missing rather than silently
omitted.

The three cases carry the distinction of clause 5.9. Case 1 is a subsymbolic
system with the full life cycle, from acquiring data to evaluating a trained
model. Case 2 is a symbolic one: a model that was written rather than learned.
Case 3 combines the two in one system with two components.

---

## cq01

One system per case. Only case 3 reports components, having two, one per
approach.

Entry 3.1.2 makes the component a functional element that constructs a system,
and a model needs it as soon as one system carries more than one approach: a
learned classifier alongside a rule-based decision would otherwise be
indistinguishable.

## cq02

The kind of AI. Case 1 is subsymbolic, case 2 symbolic, case 3 both.

That case 3 reports both is possible because the two types are deliberately not
disjoint. Neither entry excludes the other and clause 5.9 discusses combining
them, so a system may be typed as both rather than having to choose.

## cq03

Where each system runs. The class comes from clause 8.6.2 rather than from an
entry, and it is a construct of this work, which the note on the class records.

It exists for the alignment. The design says where a system runs, and the
assignments of the plant say where it actually does, and question 09 of the
alignment compares the two.

## cq04

The task of each system with its kind. All three cases classify, which is what
makes them comparable: the same task solved three ways.

Asked of the case rather than of the class hierarchy. Listing the task kinds
the pattern knows would answer the same whichever model is loaded.

## cq05

Which prediction fulfils which task. Entry 3.1.27 has the prediction as the
primary output of an AI system, and the task as what it was asked for, and this
joins the two.

## cq06

The functions of each system: seven in case 1, two in case 2, three in case 3.

The spread is the point. Case 1 runs the full life cycle, acquiring, labelling,
training, evaluating, validating and inferring. Case 2 does none of that: a
rule-based system acquires its input and infers, and everything else in the
life cycle exists to produce a model it was never going to learn.

## cq07

Only case 3 answers, with two rows. Entry 3.1.2 has the component construct the
system, and where a system carries one approach the distinction between the
system and its component adds nothing.

## cq08

Which function uses which data, five rows in case 1. The relation that ties the
function view to the data view, and the one the alignment extends: the data a
function uses is what a communication has to carry.

## cq09

One row, case 1: a validation of the trained model. No case states a
verification, so the question reports half of what it asks about, and the
absence is worth reading.

Both are recorded as AI functions here, which `REFERENCE.md` records as a
decision rather than as an entry of the standard: 3.5.13 and 3.5.14 define the
two activities without placing them in a life cycle. Validation asks whether
the right system was built, verification whether it was built right, and a
model stating only the first has not said the second was done.

Cases 2 and 3 answer empty. A rule-based model is validated by review rather
than against held-out data, and the pattern does not pretend otherwise.

## cq10

Functions with no data, three in case 1 and one each in the others.

The kind is what makes the answer readable. The control of case 3 is the case
worth pointing at: 3.5.5 has it act on a process rather than on a dataset, so
stating no data is correct rather than incomplete, and the AIAS alignment
reaches what it acts on through a relation of its own.

An inference without data would be a different matter, since it computes a
prediction from something.

## cq11

The algorithms with their kind. The pattern separates the model algorithm, the
training algorithm and the evaluation algorithm, none of which the standard
defines: 3.3.6 defines the machine learning algorithm alone.

Case 2 reports one, a rule algorithm, and it is a model algorithm rather than a
machine learning algorithm. That is the distinction of question 14 seen from
the algorithm side.

## cq12

The hyperparameters with the value each was set to. Case 1 states three, one on
each kind of algorithm: twelve layers on the model algorithm, a learning rate
on the training algorithm, a threshold on the evaluation algorithm.

That spread is why the pattern places the hyperparameter on the algorithm
superclass rather than on the training. Entry 3.3.4 names the machine learning
algorithm specifically, so applying it to a rule threshold is a reading of the
entry rather than the entry itself, and the note on the class records that.

The value arrives through `hasSetting` rather than through `forCharacteristic`.
A hyperparameter is chosen before a training and a quality of clause 3.5 is
established by one, so which relation leads to a value says whether it was
stated or measured.

## cq13

The learning type, one row in cases 1 and 3, none in case 2. Only a machine
learning algorithm has one, which is what `basedOnLearning` restricts it to.

Functional: an algorithm performs one kind of learning, which negative model 03
tests.

## cq14

The question the pattern is built around.

Case 1 reports one model, learned. Case 2 reports one, not learned: a `Model`
that is not an `MLModel`, based on a rule algorithm, created by no training.
Case 3 reports both.

Entry 3.1.23 defines the model in general and 3.3.7 the machine learning model,
and keeping the second below the first is what lets case 2 be described at all.
A pattern equating the two would either force a training that never happened or
leave a rule-based system without a model.

The column is read off the class rather than off the presence of a training, so
a model recorded before its training is stated still answers correctly.

## cq15

Which training created which model, with the parameters it determined. Cases 1
and 3 answer, case 2 does not, for the reason question 14 gives.

## cq16

The model parameters a training determines, 3.3.8. The counterpart of the
hyperparameter of question 12: this one is learned, that one is set.

The name is worth watching when comparing this pattern with the information
model it rebuilds. `hasParameter` carried the hyperparameter there and carries
the model parameter here, and `REFERENCE.md` records the change.

## cq17

Empty in all three cases. Entry 3.3.10 defines retraining, and none of these
cases has been through it: they describe systems as first built.

The question is here for a model of a system in operation, where the difference
between the model that was deployed and the model that is running matters.

## cq18

The chain from a model to what it produces: an inference is executed by a
model and creates a prediction. Case 3 answers twice, once per component.

## cq19

The data of each case with their kind, five in case 1. Clause 3.2 separates
them by the part they play, and the pattern makes the kinds disjoint: a set
used for training and for evaluating at once would make the evaluation
meaningless, which negative model 01 tests.

Asked of the case rather than of the disjointness axioms. Reporting which kinds
the pattern keeps apart would answer the same whichever model is loaded.

## cq20

How the data are composed. Entry 3.2.4 has the dataset as a collection, and
`isComposedOf` carries the same relation down to the sample, so a model can
describe data at whichever level it needs.

## cq21

Which data are labelled, and with what. Case 1 answers with its training data
and their labels, case 2 with production data marked as not labelled.

The `false` in case 2 is a statement rather than a gap. A rule-based system
needs no labels, and saying so is different from saying nothing.

## cq22

The data processing steps, two in case 1: a labelling and a normalization on
the training data.

Cases 2 and 3 answer empty. Neither prepares data, which follows from what they
are: case 2 has nothing to train and case 3 describes an architecture rather
than a pipeline.

## cq23

Where data come from and where they go. Cases 1 and 2 answer, case 3 does not,
which question 24 reports from the other side.

The two classes are constructs of this work. Clause 8.6.1 discusses acquiring
and storing data without defining a source or a sink as terms, and the notes on
the classes say so.

## cq24

Data with no stated origin: three datasets in case 3, none in cases 1 and 2.

For an audit this is the first question. A dataset a system was trained on and
whose origin is unrecorded cannot be checked for the licence it came under, the
consent it rests on, or the population it represents.

That case 3 answers with everything is a property of the case rather than of
the pattern. It describes a hybrid architecture and leaves the data pipeline to
the other two cases, which is a reasonable division of labour between test
models and exactly what this question makes visible.

## cq25

The quality values stated, two in case 1. The value is reified so it can carry
the characteristic it quantifies alongside the quantity and the unit.

`forCharacteristic` is functional: one value quantifies one characteristic,
which negative model 05 tests.

## cq26

The nine qualities of clause 3.5 held against the case. Every case states one
or two and leaves the rest open.

The catalogue is the yardstick rather than the answer here, which the query
declares. Listing the qualities would report the same nine whatever case is
loaded; holding them against the case reports what this system claims about
itself.

The unstated half is the half a review asks about. A system with no stated
robustness has not said how it behaves outside its training distribution.

## cq27

The controllability, one row in cases 1 and 2. Entry 3.5.6 has it as the
property of allowing an external agent to intervene, and the pattern records it
as a relation to a thing rather than as a value, since what matters is what the
intervention consists of.

The term is a trap across the subdomains. IEC 60050-351 defines controllability
as the mathematical property of a system being steerable into a given state,
which is a different concept under the same name, and the alignment keeps the
two apart deliberately.

## cq28

One risk, case 2. Clause 3.5 treats risk as central to trustworthiness, and a
model that records none has not said what could go wrong.

That only one case states one is a property of the test models rather than a
finding about the pattern.
