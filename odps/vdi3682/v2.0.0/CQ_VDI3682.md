# Competency Questions: VDI 3682 Pattern (Technical Process)

Ontology design pattern for the formalised description of technical processes.

Normative basis: VDI/VDE 3682 Part 1 (concept and graphic representation) and
Part 2 (information model), issue May 2015, bilingual German/English.

IRI: `https://w3id.org/aias/odp/vdi3682/`

Every question is answered from the A-box of a modelled case. The class
hierarchy is traversed where a kind has to be reported, but the answer is
always made of individuals: a question whose answer would be the same with no
case loaded belongs to the documentation of the pattern rather than here.

Six questions ask what a model has left open, marked with a dash in the answer
column. They return nothing on a complete description, and that is the point.
OWL cannot require any of it under the open world assumption, so the answers
report rather than enforce, and each is a place where SHACL would later take
over.

The answer column states what a query returns, not how it is computed.

---

## A. The process and its decomposition

| ID | Competency question | Answer |
|---|---|---|
| 01 | Which process operators does a process consist of, and what enters and leaves each? | Process, operator, its inputs and outputs |
| 02 | Which operators are decomposed, and into which sub operators? | Parent operator, sub operator |
| 03 | Which operators are not decomposed any further? | The elementary operators, where the description ends |
| 04 | Which process is above an operator, and across how many levels? | Operator, parent process, level number |
| 05 | In which order do the operators run? | Predecessor, successor |
| 06 | Which operators begin a chain, which end one, and which state no order? | Operator and its role. Distinguishes an operator ordered one level down from one with no order at all |

## B. States: what an operator consumes and produces

| ID | Competency question | Answer |
|---|---|---|
| 07 | Which states enter an operator, and which leave it? | Operator, its inputs, its outputs |
| 08 | Of which kind are the states of a case: product, energy or information? | State, kind |
| 09 | Which products arise in the process, and which are consumed again? | Product, role, operator |
| 10 | Which states depend on which others? | State, dependent state, both with their kind |
| 11 | Which states are neither input nor output of an operator? | State and what is missing, produced or consumed. Empty on a closed description |

## C. Flows, including parallel and alternative

| ID | Competency question | Answer |
|---|---|---|
| 12 | Which flows connect which elements? | Flow, source, target, direction |
| 13 | Which flows are simple, which parallel, and which alternative? | Flow, its kind, source, target |
| 14 | Which states feed a parallel run, and into which operators? | State, the operators it feeds, the branch count |
| 15 | Which alternatives lead to the same product? | Product, the operators producing it |
| 16 | Which flows cross a system limit? | Flow, source, target |
| 17 | Which elements lie within which system limit? | Element, limit |

## D. Technical resources

| ID | Competency question | Answer |
|---|---|---|
| 18 | Which resource performs which operator? | Operator, assignment, resource |
| 19 | Which operators have no resource? | Operator. Empty where every step is assigned |
| 20 | How many operators is each resource assigned to? | Resource, operator count. A count above one marks a shared resource |
| 21 | Which resources are modelled but assigned to no operator? | Resource. Empty where nothing stands idle |
| 22 | On which decomposition level is each resource assigned? | Resource, operator, level, and whether the parent carries the same resource |

## E. Attributes: identification and characteristics

| ID | Competency question | Answer |
|---|---|---|
| 23 | How is an element identified, and with which entries? | Element, short name, long name, version |
| 24 | Which of the named elements carry no identification? | Element, kind. Flows are left out, being read off their endpoints |
| 25 | Which characteristics are recorded on which elements? | Element, characteristic, category, value |
| 26 | Which resources and operators are named but described no further? | Element, kind, short name. Carries an identification and no characteristic |

---

## On question 22

Figure 5 shows one process at two levels of detail, and a resource may be
assigned on either. Assigning it on both counts the same work twice: the
refined operators do the work of the coarse one, not work in addition to it.

Test case 1 follows that rule and assigns the refined resources only. The
question makes it checkable, since a row naming one resource on an operator
and on its parent is the double count.

---

## Open points for modelling

1. **`State` is normatively covered.** Part 1 Sec. 4.1 gives the term up for the
   graphical notation, Part 2 Fig. 2 uses it as a class in the information
   model. The pattern keeps it, and the `rdfs:comment` cites Part 2.

2. **`Flow`, `Assignment`, `ParallelFlow`, `AlternativeFlow`.** The standard has
   flow and usage as symbols and resolves parallel and alternative runs as
   patterns. Reifying them as classes is this work's own and must be documented
   as such, not as adoption.

3. **Characteristics carry a structure, not a vocabulary.** Part 2 Sec. 5.2
   fixes that a characteristic consists of category, descriptive element, and
   relational element. The entries shown in Figures 6 and 7 (setpoint value,
   validity limits, actual values, view, model) are **examples**, closed by an
   open "(...)" box, not a normative list. VDI 3682 therefore supplies the
   container for non-functional properties but not the properties themselves.
   **A second standard has to supply the vocabulary.** First candidates:
   IEC 60050-351 for real-time and control quantities, ISO/IEC 24765 for
   software and system properties. To be decided when those are read.

4. **Version and revision.** The identification of Part 1, 4.4 carries a
   version and a revision number, which question 23 reports. They offer a
   standard-backed anchor for the four model states, which currently exist
   only as copied files.

5. **`TechnicalRessource` → `TechnicalResource`** on rebuild.

6. **No temporal semantics.** The pattern records no time. Question 05 orders
   the operators and states no duration, which is deliberate.
   Whether actual values with time stamps (Part 2 Fig. 6) are adopted is open;
   taking them would soften that boundary. Recommendation: leave them out.
