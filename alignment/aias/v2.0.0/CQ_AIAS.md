# Competency Questions: AIAS Alignment Ontology

The alignment joins the four subdomain patterns into one model of an AI
application in an automated plant.

IRI: `https://w3id.org/aias/`

Every question is answered from the A-box of a modelled case. The imported
patterns ship named individuals, and a case uses them as it needs them, but
listing any of those catalogues is not a competency question: the answer would
be the same whichever case is loaded. No question here needs the exemption the
other catalogues use, since every one of them starts from a modelled system.

The answer column states what a query returns, not how it is computed.

**What separates these questions from those of the patterns.** Every catalogue
so far asked something answerable inside one standard. These questions cannot
be answered inside any one of them, and that is the criterion for belonging
here: a question that one pattern can answer alone stays in that pattern.

The bridges each question relies on are recorded in `ALIGNMENT.md`, with the
reason for each and the strength it is stated at.

---

## 1. The system as a whole

| ID | Competency question | Answer | Note |
|---|---|---|---|
| 01 | Which functions, components and relations make up a modelled system? | The three main classes per system | The entry point. `aias:Function`, `aias:Component` and `aias:Relation` after Haberfellner, related to an `iso22989:AISystem` so that a model has one root. |
| 02 | Which functions come from which subdomain? | The functions with their pattern of origin | A process operator, an inference and a control all answer, which is what the common function level is for. Without it nothing could be said about all three at once. |
| 03 | Which resources does a model contain, and of which kind is each? | The resources with their kind | Sensors, actuators, controllers, edge devices, computers and the two cloud kinds. They are classes of this work rather than of a standard, which `ALIGNMENT.md` records. |

## 2. Functions and the resources performing them

| ID | Competency question | Answer | Note |
|---|---|---|---|
| 04 | Which resource performs a given function? | The resource per function, through the assignment. A function is assigned to at least one resource | The question the whole alignment is built for. `vdi3682:Assignment` ties a function to a resource, and because process operators and AI functions share a superclass, the same relation answers for both. |
| 05 | Which functions does a given resource perform, and from which subdomains? | The functions per resource with their origin | Asked from the other end. An edge device carrying an inference and a process step answers with both, which is what makes a mixed architecture visible. |
| 06 | Which resources perform AI functions, and which perform process operations only? | The resources by the kind of function they carry | Separates the plant that computes from the plant that produces. The answer is what a deployment decision acts on. |
| 07 | Which functions are not assigned to any resource? | The unassigned functions. An empty answer means the model is complete in that respect | A model that names a function without saying what carries it is unfinished. The question finds that. |

## 3. Where a system runs

| ID | Competency question | Answer | Note |
|---|---|---|---|
| 08 | On which kind of resource does each AI function run? | The functions with the resource kind | Whether an inference runs on an edge device or in an external cloud is the architectural decision this model exists to record. |
| 09 | Does the system design stated for an AI system agree with where its functions actually run? | The design against the resource kinds. The design is a claim the assignments have to bear out | `iso22989:SystemDesign` says cloud, edge or hybrid. The assignments say where things are. A mismatch is a modelling error the question surfaces. |
| 10 | Which functions run outside the plant? | The functions on external resources | The question a data protection review asks first. |

## 4. Control and the process

| ID | Competency question | Answer | Note |
|---|---|---|---|
| 11 | Which controls of the plant are carried out by an AI system, and which are not? | The controls by whether an AI system performs them | The two control classes are equivalent across the standards, so a control stated in either subdomain answers. Question 02 of the IEC 60050-351 pattern asks which kind a control is. This one asks who performs it, which needs both subdomains. |
| 12 | Which AI functions take part in a control? | The AI functions related to a control | Whether an inference feeds a closed-loop control or only reports is the difference between an assistant and a controller. |
| 13 | Which resource plays which role in a control, and where does it sit in the chain? | The functional units a resource realises, with the action lines. A resource may hold several roles | Reached through the inverse relations of the IEC 60050-351 pattern. The role belongs to the functional unit, and one device may realise several, which the answer reports rather than resolves. |
| 14 | Which process operators does a control act on? | The process steps under control | Ties the control subdomain to the technical process. A control acts on a controlled system, and the process operator is what happens there. |

## 5. Communication

| ID | Competency question | Answer | Note |
|---|---|---|---|
| 15 | Which resources communicate with one another, and in which direction? | The pairs with their direction | A resource appears as an `iso7498:OpenSystem` when its communication is described, which the pattern already states on that class. |
| 16 | Over which technology and which layers does a given communication run? | The technology and layers per communication | The OSI structure of the communication pattern, reached from a pair of resources rather than from the association. |
| 17 | Which data travels over which communication? | The datasets per communication | Through `aias:carriesData`: the payload of a transmission carries a dataset. The bridge that replaces the equivalence the dissertation assumed, and `ALIGNMENT.md` gives the reason. |
| 18 | What quality of service does the communication carrying a given dataset have? | The quality of service values per dataset | The question that only the chain makes answerable. A training dataset with a latency requirement is an architectural constraint, not a data property. |
| 19 | Which resources exchange data without a recorded communication? | The pairs sharing data with no association. An empty answer means every exchange is described | Finds what a model assumes but does not state. |

## 6. Data across the subdomains

| ID | Competency question | Answer | Note |
|---|---|---|---|
| 20 | Where does the data an AI function uses come from? | The chain from data source to function | Acquisition reaches outside the AI system, and what it reaches is a resource of the plant. |
| 21 | Which data of a model originates from the technical process? | The datasets acquired from plant resources | Separates data measured in the plant from data brought in from elsewhere, which is what a provenance question asks. |
| 22 | Which information flows of the process are carried by which communication? | The flows with their communication | VDI 3682 states that information flows between process steps. ISO 7498 states how it gets there. Neither says it alone. |

## 7. Completeness of a model

| ID | Competency question | Answer | Note |
|---|---|---|---|
| 23 | Which resources carry no function at all? | The idle resources | Not necessarily an error. A cabinet or a power supply carries nothing and is still part of the plant. The question reports rather than judges. |
| 24 | Which AI functions use data that no resource of the plant acquires? | The functions whose data has no origin in the plant | Question 08 of the ISO/IEC 22989 pattern asks which data a function uses, question 24 which data lacks an acquisition. This one asks whether the acquisition reaches a resource, which neither pattern can answer alone. |
| 25 | Which parts of a model belong to no subdomain pattern? | The instances of `aias:` classes only | What a model states beyond the four standards. A large answer means the standards cover less of the case than intended. |

---

## Open points for modelling

1. **The function level is what carries the alignment.** A process operator of
   VDI 3682 and an inference of ISO/IEC 22989 have nothing in common in their
   own standards. Under `aias:Function` they become comparable, and every
   question of section 2 depends on that. It is a design decision of this work,
   not a finding, and `ALIGNMENT.md` says so.

2. **The role of a resource has more than one answer.** IEC 60050-351 keeps the
   functional and the physical view apart, 351-56-02 against 351-56-03, and one
   device may realise several functional units. Question 13 reports all of them.
   A model wanting one role per device would have to assert a cardinality the
   standard does not state.

3. **The data bridge is a relation, not an equivalence.** `iso7498:UserData` is
   the payload of one transmission, `iso22989:Data` a collection of samples that
   may travel many times or never. Question 17 and 18 work only because the two
   stay apart.

4. **Controllability is not bridged.** The two standards use the same word for
   different concepts, and `ALIGNMENT.md` records the difference so that the two
   are not merged later. No question here asks across them.

5. **The devices rest on nothing.** `aias:Sensor` and its siblings come from no
   standard. Question 03 and 06 answer with them, and the answers are only as
   good as that classification. Relating them to a catalogue of equipment is
   open work.

6. **Questions 09, 19, 23 and 24 report rather than enforce.** OWL cannot
   require that a design agrees with the assignments, or that every function
   states its data. A model may be inconsistent in those respects without the
   reasoner objecting. Enforcing it belongs to SHACL, and until then these
   questions are how a reviewer finds it.
