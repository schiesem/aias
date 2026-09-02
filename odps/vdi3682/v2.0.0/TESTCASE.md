# Test Cases: VDI 3682 Pattern

Three test cases, each taken from a figure of VDI/VDE 3682 Part 1 rather than
invented. A reviewer can hold every model against the standard.

Two rules govern these cases:

1. **Taken from the standard.** Element names follow the figure labels, so
   `ex:O11` is the operator the standard calls `ID (O11)`. The readable name
   lives in `rdfs:label` and `vdi3682:longName`.
2. **Independent of the alignment.** No test case assumes anything about AI,
   plants, or communication. They exercise the VDI 3682 pattern alone, so a
   failure can only come from this pattern.

| Case | Source | Covers |
|---|---|---|
| 1 | Part 1, Figures 4 and 5 | base description and decomposition |
| 2 | Part 1, Figures 5 and 7 | parallel process runs |
| 3 | Part 1, Figures 5 and 8 | alternative process runs |

Cases 2 and 3 follow the structure of case 1 and add one parallel or one
alternative step before the decomposition, so that the three differ in exactly
one construct.

**Only case 1 carries energy and information.** Cases 2 and 3 work with
products alone, for two reasons. Whatever enters a process operator has to
leave it again in some form, so an energy or an information going in without a
counterpart coming out would state a balance the model cannot keep, and the
system limit is exactly what Part 1 Section 4.1 ties the balance to. And the
figures those cases come from, Figure 7 and Figure 8, show products only.
Restricting them to products therefore stays closer to the standard and keeps
the difference to case 1 down to the one construct under test. That energy and
information behave as subclasses of state is already established by case 1.

---

## Case 1: base description and decomposition

`tests/data/tc1_decomposition.ttl`, after Part 1 Figure 4 and Figure 5.

```
BEFORE DECOMPOSITION (Figure 4, and Figure 5 left)

    ┌────P1────────E1────────I1────┐
    │ S0 │         │         │     │
    │    ▼         ▼         ▼     │        ┌────┐
    │            O1  ◀─────────────┼───────▶│ T1 │
    │    ▲         ▲         ▲     │        └────┘
    │    │         │         │     │
    └───P2────────P3────E2───I2────┘

AFTER DECOMPOSITION (Figure 5 right)

    ┌────P1────────E1────────I1────┐
    │ S1 │         │         │     │
    │    ▼         ▼         ▼     │        ┌─────┐
    │           O11  ◀─────────────┼───────▶│ T11 │
    │            │                 │        └─────┘
    │      ┌─────┴─────┐           │
    │     P4          E3           │   (inner only)
    │      └─────┬─────┘           │
    │            ▼                 │        ┌─────┐
    │           O12  ◀─────────────┼───────▶│ T12 │
    │    ▲         ▲         ▲     │        └─────┘
    │    │         │         │     │
    └───P2────────P3────E2───I2────┘
```

**What it puts under test.** The inputs `P1`, `E1`, `I1` and the outputs `P2`,
`P3`, `E2`, `I2` are the same on both levels, while `P4` and `E3` exist only
inside the decomposition. That is the claim of Figure 5, and it is what the
inferred chains `hasSubProcess` and `hasUpperProcess` have to reproduce.

**Inputs and outputs sit on the system limit**, which is where the standard
draws them: they are what crosses the boundary, so they belong to both the
process and its environment. Only `P4` and `E3` lie strictly inside.

**The decomposition releases nothing extra.** Whatever leaves the refined view
has to leave the undecomposed view as well, otherwise the two levels would not
balance. `P2` therefore leaves `O1` in the parent view and `O11` in the refined
one. Getting this wrong is easy to miss, since both views are consistent on
their own and only the comparison exposes it.

**Resource assignment.** Figure 5 shows `T1` on the left and `T11`, `T12` on
the right. These are two views of one process at different levels of detail,
not two statements holding at once. The model therefore assigns resources to
the decomposed operators only. Assigning one to `O1` as well would count the
same work twice, which query `cq17` would report as three operators on two
resources.

## Case 2: parallel process runs

`tests/data/tc2_parallel.ttl`, after Part 1 Figure 7, decomposed as in
Figure 5.

```
BEFORE DECOMPOSITION (Figure 7)

    ┌─────────P1───────────────────┐
    │ S0      │                    │
    │     ┌───┴───┐                │        ┌─────┐
    │     ▼       ▼                │        │ T1a │
    │    O1a  ◀───┼────────────────┼───────▶└─────┘
    │     │       │                │
    │     │      O1b ◀─────────────┼───────▶┌─────┐
    │     │       │                │        │ T1b │
    │     ▲       ▲                │        └─────┘
    └────P2a─────P2b───────────────┘
       both arise, in parallel

AFTER DECOMPOSITION (O1a refined)

    ┌─────────P1───────────────────┐
    │ S1      │                    │
    │     ┌───┴───┐                │
    │     ▼       ▼                │        ┌──────┐
    │   O11a ◀────┼────────────────┼───────▶│ T11a │
    │     │       │                │        └──────┘
    │    P4a      │                │  (inner only)
    │     ▼       │                │        ┌──────┐
    │   O12a ◀────┼────────────────┼───────▶│ T12a │
    │     │       │                │        └──────┘
    │     │      O1b ◀─────────────┼───────▶┌─────┐
    │     │       │                │        │ T1b │
    │     ▲       ▲                │        └─────┘
    └────P2a─────P2b───────────────┘
```

`P1` feeding both operators is the partially shared flow that Part 1
Section 4.2.1 recommends for parallel runs.

**What it puts under test.** Part 1 Section 4.2.1 models parallel runs as a
partially shared flow and explicitly needs no additional graphical element.
This pattern expresses the same thing in two complementary ways, and the case
checks that both are present:

- `ParallelFlow` qualifies the individual connection.
- `dependency` between `P2a` and `P2b` states that the two arise together.
  Without it, the open world assumption reads several outputs as alternatives,
  which is exactly the reading case 3 wants and this case does not.

## Case 3: alternative process runs

`tests/data/tc3_alternative.ttl`, after Part 1 Figure 8 right, decomposed as in
Figure 5.

```
BEFORE DECOMPOSITION (Figure 8 right)

    ┌─────────P1───────────────────┐
    │ S0      │                    │
    │     ┌───┴───┐                │        ┌─────┐
    │     ▼       ▼                │        │ T1a │
    │    O1a  ◀───┼────────────────┼───────▶└─────┘
    │     │       │                │
    │     │      O1b ◀─────────────┼───────▶┌─────┐
    │     │       │                │        │ T1b │
    │     └───┬───┘                │        └─────┘
    │         ▲                    │
    └────────P2────────────────────┘
       arises from O1a OR from O1b

AFTER DECOMPOSITION (O1a refined)

    ┌─────────P1───────────────────┐
    │ S1      │                    │
    │     ┌───┴───┐                │
    │     ▼       ▼                │        ┌──────┐
    │   O11a ◀────┼────────────────┼───────▶│ T11a │
    │     │       │                │        └──────┘
    │    P4a      │                │  (inner only)
    │     ▼       │                │        ┌──────┐
    │   O12a ◀────┼────────────────┼───────▶│ T12a │
    │     │       │                │        └──────┘
    │     │      O1b ◀─────────────┼───────▶┌─────┐
    │     │       │                │        │ T1b │
    │     └───┬───┘                │        └─────┘
    │         ▲                    │
    └────────P2────────────────────┘
```

**What it puts under test.** Part 1 Figure 8 right shows a product arising from
one or the other process operator, carrying the same properties from the view
of the parent process. `AlternativeFlow` marks both connections, and no
`dependency` is asserted, so the open world reading of alternatives stands.

**The balance limit rule.** Part 1 Section 4.1 states that a system limit
cannot serve as a balance limit when alternative runs are described. This case
is the one where query `cq23` must answer "no". Cases 1 and 2 are the
counter-check: without alternative flows, the same query must answer "yes" for
every system limit. Only both directions together show that the rule
discriminates rather than answering uniformly.

---

## Coverage of the competency questions

| CQ | Question | Answered on |
|---|---|---|
| 01 | operators with inputs and outputs | 1, 2, 3 |
| 02 | inputs and outputs by state type | 1, 2, 3 |
| 03 | predecessor and successor | 1, 2, 3 |
| 04 | decomposed steps | 1, 2, 3 |
| 05 | decomposition level and parent | 1, 2, 3 |
| 06 | elementary operators | 1, 2, 3 |
| 07 | states never produced or never consumed | 1, 2, 3 |
| 08 | number of states of a process | 1, 2, 3 |
| 09 | states by subtype | 1, 2, 3 |
| 10 | input and output state of one operator | 1, 2, 3 |
| 11 | operators a product passes | 1, 2, 3 |
| 12 | information crossing the system limit | 1 only, cases 2 and 3 carry no information |
| 13 | resource realising an operator | 1, 2, 3 |
| 14 | operators realised by one resource | 1, 2, 3 |
| 15 | operators without a resource | empty everywhere, which is the assertion: every elementary operator has one |
| 16 | resources without an operator | empty everywhere, which is the assertion: no resource is unused |
| 17 | resource load | 1, 2, 3 |
| 18 | flows incident to an operator | 1, 2, 3 |
| 19 | parallel runs | 2 only |
| 20 | alternative runs | 3 only |
| 21 | alternative producers of one product | 3 only |
| 22 | elements inside a system limit | 1, 2, 3 |
| 23 | balance limit admissible | 1 and 2 admit, 3 rejects the limit enclosing alternatives |
| 24 | flows crossing the system limit | 1, 2, 3 |
| 25 | identification of an object | 1, 2, 3 |
| 26 | version and revision | 1, 2, 3 |
| 27 | characteristics of an object | 1 only |
| 28 | reference to an external identification system | 1 only |

An empty result counts as an answer and is recorded as such. Questions 15 and
16 return nothing on every case, and that is what they are meant to establish:
no elementary operator lacks a resource and no resource lies unused. Should a
later change break either, the expectation stops matching.

`CQ_VDI3682.md` carries a second table stating how each question is answered,
that is which of them read stored triples, which rely on the reasoner, which
report an absence, and which compute a result.

**Not covered, deliberately.** Question 17 also asks whether operators sharing
a resource are mutually exclusive in time. The pattern carries no temporal
semantics, so no test case can answer that half of it, and the catalogue
records the limit rather than leaving it to be discovered.

---

## Negative models

Each file under `tests/negative/` violates exactly one axiom, so a failure
names its own cause. All must be rejected by the reasoner; a model that is
accepted proves the axiom under test does not bite.

| File | Axiom | Normative basis |
|---|---|---|
| `neg01_state_is_operator` | `State` and `ProcessOperator` are disjoint | Part 1, Sec. 4.1 distinguishes the two object classes |
| `neg02_product_is_energy` | `Product` and `Energy` are disjoint | Part 1, Fig. 3 |
| `neg03_two_system_limits` | a process has exactly one system limit | Part 2, Fig. 2, cardinality 1 |
| `neg04_flow_target_resource` | `hasOperatorTarget` has range `ProcessOperator` | flows connect states and operators, not resources |
| `neg05_identification_not_functional` | `isIdentifiedBy` is functional | Part 2, Fig. 3, cardinality 1 |

---

## Running

```bash
python ../../shared/run_tests.py --package vdi3682
```

The queries are also the debugging tool: a failing competency question names
the relation that is missing, which is more precise than reading it off a
diagram. The ontology itself can be viewed through the WebVOWL page that Widoco
generates under `docs/webvowl/`, but that view carries the classes and
properties, not the individuals of these models.

Changing a model changes the recorded expectations under `tests/expected/`.
Regenerate them with `--update-expected`, then read the diff before committing.
An expectation recorded without reading it freezes whatever bug produced it.
