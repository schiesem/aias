# Interpretations of the competency question results

Source text for `RESULTS.md`, which the test runner generates. Everything else
in that report is produced from the queries and the recorded results, so it
cannot go stale. These interpretations are written by hand and have to be kept
in step with the models.

Format: one `## cqNN` heading per question, followed by free text. A question
without an entry appears in the report marked as missing rather than silently
omitted.

The three cases differ in one construct each. Case 1 is the base description
with a decomposition after Figures 4 and 5, case 2 adds a parallel run after
Figure 7, case 3 an alternative after Figure 8. Reading an answer across the
three columns is therefore a way of seeing what a single construct changes.

---

## cq01

Each operator appears once per process it belongs to, with its inputs and
outputs collected. In case 1 the parent operator `O1` shows the same inputs and
outputs as the two refined operators together, which is the balance a
decomposition has to keep.

Inputs and outputs are grouped rather than paired. Listing them as separate
columns would join the two sets into their cartesian product, which reads as a
pairing of one input with one output, and VDI 3682 asserts no such pairing.

## cq02

Two rows per case, and the same two in all three: the parent operator and the
two operators it consists of. The construct that separates the cases sits
elsewhere, which this answer confirms by not moving.

## cq03

The elementary operators, where the description stops. Case 1 has two, cases 2
and 3 have three, the added one being the parallel or alternative branch.

The answer is the complement of question 02 and worth asking on its own: the
elementary operators are the ones a resource is assigned to, and question 22
returns to them.

## cq04

The level of each operator and the process above it. Case 1 reaches level one,
which is as deep as Figure 5 goes.

An operator with no parent process is at level zero, and in these cases that is
the operator of the coarse view. The number is computed by counting steps
upwards rather than asserted, so a model states its decomposition once.

## cq05

One row per case: the refined operators run in sequence, the first before the
second. Part 1, Figure 4 connects operators through states rather than
directly, and the order relation is stated alongside that, not derived from it.

The sparse answer is the correct one. These cases order two operators and say
nothing about the rest, which question 06 reports from the other side.

## cq06

Where the order starts, stops, and was never stated. Two operators begin and
end the chain in every case, and the interesting rows are the remaining ones.

`O1` of case 1 carries no order and is decomposed: the coarse view shows one
step and the refined view orders the two it consists of, so the order sits one
level down. That is Figure 5 working as intended.

Cases 2 and 3 add a second unordered operator, `O1b`, and it is elementary.
Nothing states when it runs, and nothing has to: it is the parallel or
alternative branch, and its relation to the other branch is stated by the flow
rather than by a sequence. The two situations are reported apart for that
reason, since only one of them would be a gap in a different model.

## cq07

The states entering and leaving each operator, which is the base relation of
Part 1, 4.1. Read against question 01 it shows the same information per
operator rather than per process.

## cq08

The three state kinds told apart. Only case 1 carries energies and information;
cases 2 and 3 work with products alone, so their answers list products only.
Nine states in case 1 against four and three, which is the price of a base
description that shows all three kinds.

The kinds behave as subclasses of `State` here, and the answer reports the
direct one rather than repeating the superclass.

## cq09

Every product with the operators consuming and producing it, eight rows in each
case. A product with a producing operator and no consuming one leaves the
process, and one with neither is unconnected, which question 11 reports.

## cq10

The dependency of Part 1, 4.1.2, which the standard carries alongside the flow.
Only case 2 answers, with two rows: `P2a` and `P2b` depend on each other.

That is what holds a parallel run together. The two products arise from
branches running alongside each other, and the dependency states that they
arise together, which no flow between them says. Cases 1 and 3 have no
parallelism and therefore no dependency, which is the correct empty answer.

The relation is symmetric in these models and the pattern does not assert it as
such, so both directions appear as stated.

## cq11

States that are neither input nor output of an operator, four in case 1 and
fewer in the others. Each is a boundary of the description rather than an
error: a state consumed but never produced enters from outside the modelled
section, and one produced but never consumed leaves it.

The answer therefore reads as a list of open ends, and whether each is intended
is a question the model cannot answer on its own. Where a system limit is
modelled, question 16 says which of them cross it.

## cq12

The flows as reified objects, eighteen in case 1. These are what the graphical
notation draws, and they are classes rather than plain edges because the
annotation of Part 2 attaches to them.

The count drops to eight in cases 2 and 3, which follows from those cases
carrying fewer states rather than from anything about parallelism.

## cq13

Where the three cases separate. Case 1 answers with plain flows only, case 2
adds two `ParallelFlow`, case 3 two `AlternativeFlow`.

The question is anchored on the flow rather than on one of its subclasses, so a
model without parallelism answers with its simple flows instead of returning
nothing. The direct class is reported: the reasoner materialises the subclass,
and naming `Flow` alongside it would say nothing.

## cq14

The parallel run as an arrangement rather than as an edge. Case 2 answers with
one row: the state `P1` feeds two operators, and the branch count is two.

Part 1, 4.2.1 models a parallel run as a partially shared flow, which is why
the question is asked from the state rather than from the flow. Cases 1 and 3
answer empty, and case 3 is the one worth noting: it has two branches as well,
but they are alternatives, so exactly one of them runs.

## cq15

The counterpart for case 3, which answers with two rows against none in the
others: the product `P2` arises from `O1a` or from `O1b`.

Figure 8 right shows exactly that, and the difference from question 14 is the
whole distinction between the two constructs. A parallel run produces both
products, an alternative produces one product by one of several paths.

## cq16

Flows crossing a system limit, seven in case 1. A flow crosses where its source
and target lie within different limits, or where one of them lies within none.

The second case is included on purpose. An element outside every stated limit
is outside the described section, so a flow reaching it leaves that section
just as one crossing between two limits does.

## cq17

Which elements lie within which limit, thirty rows in case 1. The basis of
question 16 and the larger answer of the two, since it reports every element
rather than only the crossings.

## cq18

The assignment of resources to operators, through the reified `Assignment` of
Part 1, 4.2. Two rows in case 1 and three in the others, matching the number of
elementary operators.

The reification is what lets the assignment carry properties of its own, and
the alignment uses it: `aias:assignedFunction` starts from the same class in
order to reach a function that is not a process operator.

## cq19

Empty in all three cases, which is the intended state. Every operator that does
work has a resource performing it.

The question cannot be enforced by OWL. An operator without an assignment is
unstated rather than unassigned under the open world assumption, so the answer
reports a gap rather than a contradiction, and SHACL is where it would become a
constraint.

## cq20

The load per resource. Every resource in these cases carries exactly one
operator, so every count is one.

The count is reported rather than filtered to the shared ones. A model with no
sharing would otherwise answer nothing, and that each resource is used once is
itself a fact worth reading off. A count above one marks a resource two steps
depend on, which matters for scheduling and for a fault stopping both.

## cq21

Empty in all three cases, the counterpart of question 19 from the resource
side. A resource modelled and assigned to nothing is either a gap in the
description or equipment that stands idle, and the model cannot tell the two
apart.

## cq22

The level each resource is assigned on. Case 1 assigns both resources at level
one, cases 2 and 3 add one at level zero, the parallel or alternative branch.

The last column is the one the question exists for. Figure 5 shows one process
at two levels, and assigning a resource on both counts the same work twice: the
refined operators do the work of the coarse one, not work in addition to it.
The column stays empty in all three cases, which is the correct result and the
rule the test cases were built to follow.

## cq23

The identification of Part 1, 4.4, with short name, long name and version. Five
elements in case 1, two in the others.

`isIdentifiedBy` is functional, so an element carries at most one
identification, which negative model 05 tests.

## cq24

The elements a description names that carry no identification, twelve in each
case. Flows are left out: a flow is the line between two named things and is
read off its endpoints, so an unidentified flow is the normal case and
reporting it would bury the rest.

The answer is large because these cases identify a few elements as examples
rather than all of them. That is a property of the test models rather than of
the pattern, and the question is what makes it visible.

## cq25

The characteristics of Part 1, 4.4, with their category. One row in case 1 and
none in the others.

Part 2, 5.2 fixes that a characteristic consists of category, descriptive
element and relational element, and the entries of Figures 6 and 7 are examples
rather than a normative list. The pattern therefore supplies the container and
not the vocabulary, and the open points of the catalogue record which standard
could supply it.

## cq26

Elements carrying a name and nothing else. One row in case 1, `O1`, and none in
the others.

Narrower than question 24 and asking something else. That question finds what
was never named, this one finds what was named and then left at that, which is
the state a description passes through halfway and should not stay in.

Restricted to operators and resources, since those are the two kinds a reader
asks about. A state is often fully described by its kind and its name, so
including it would report ordinary modelling as a gap.
