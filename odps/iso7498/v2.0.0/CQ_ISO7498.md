# Competency Questions: ISO/IEC 7498-1 Pattern (Communication)

Ontology design pattern for the description of communication between open
systems.

Normative basis: ISO/IEC 7498-1:1994, Information technology, Open Systems
Interconnection, Basic Reference Model: The Basic Model, second edition,
identical to ITU-T Recommendation X.200.

IRI: `https://w3id.org/aias/odp/iso7498/`
Named individuals: `https://w3id.org/aias/odp/iso7498/instances/`

Every question is answered from the A-box of a modelled case. The pattern ships
named individuals for the seven layers, the transmission directions, the
quality of service parameters and a set of technologies, and a case uses them
as it needs them. Those individuals are A-box themselves, but listing them is
not a competency question: the answer would be the same whichever case is
loaded.

Two questions, 08 and 25, hold such a catalogue against a case and report per
entry whether the case states anything about it. They are marked below, and
their queries declare it, since the rows there are the scale rather than the
finding.

The answer column states what a query returns, not how it is computed.

---

## A. The communication

| ID | Competency question | Answer |
|---|---|---|
| 01 | Which communications exist, and which systems do they connect? | Communication, the systems it connects |
| 02 | Which communications are connection-mode, which connectionless? | Communication, mode |
| 03 | In which direction does a communication run? | Communication, direction |
| 04 | Which communications have more than two participants? | Communication, participant count, kind |
| 05 | Which communications state no transmission mode? | Communication. Empty where every one is typed |

## B. Open systems and their layers

| ID | Competency question | Answer |
|---|---|---|
| 06 | Which open systems take part, and through which subsystems? | System, layer number, subsystem |
| 07 | Which layers does a communication run over? | Communication, layer, number |
| 08 | Which layers does a case occupy, and which stay empty? | Layer, number, occupied or empty. *Catalogue as yardstick* |
| 09 | Which technology realises which layer in a case? | Communication, layer number, technology |
| 10 | Which communications name no technology? | Communication, mode. Clause 1.3 requires none |
| 11 | Which subsystems lie above and below a given one? | System, subsystem, layer, position, neighbour |

## C. Entities, services, protocols

| ID | Competency question | Answer |
|---|---|---|
| 12 | Which entities does a subsystem contain? | Subsystem, entity |
| 13 | Which entities are peers, and at which layer? | Entity, peer, layer |
| 14 | Which service does an entity provide, and at which layer? | Entity, service, layer, subsystem |
| 15 | Which protocols do the entities employ? | Protocol, entity count, entities |
| 16 | Through which service access points are entities reachable? | Access point, entity, layer |
| 17 | Which entities provide no service? | Entity, layer, subsystem |

## D. Data units

| ID | Competency question | Answer |
|---|---|---|
| 18 | Which data units does a communication transmit? | Communication, data unit, layer |
| 19 | What is a protocol data unit of a case made of? | PDU, control information, user data, layer |
| 20 | How does a protocol data unit map onto a service data unit? | PDU, SDU, layer |
| 21 | Which data units of a case sit at which layer? | Layer number, data unit, kind |
| 22 | Which user data does a communication carry, and through which PDU? | Communication, PDU, user data, control information, layer |

## E. Quality of service

| ID | Competency question | Answer |
|---|---|---|
| 23 | Which quality of service is stated for a communication? | Communication, parameter, quantity, unit |
| 24 | Which values does a quality of service carry, for which parameter and unit? | Communication, parameter, quantity, unit |
| 25 | Which parameters does a case state, and which does it leave open? | Parameter, standing, communication, value. *Catalogue as yardstick* |
| 26 | Which communications state no quality of service? | Communication |
| 27 | How do the qualities of service of a case differ from each other? | Parameter, how many communications state it, the values |

---

## On questions 08 and 25

Both take a supplied catalogue and report, per entry, what the case says about
it. Question 08 does it for the seven layers, question 25 for the quality of
service parameters of 5.5.5.

Listing either catalogue would answer the same thing whatever case is loaded.
Comparing it against the case answers something about the case: which layers a
description has opened up, and which guarantees a communication actually makes.
The unstated half is the useful one, since a communication with no stated
transit delay carries no timing a deadline could be checked against.

---

## Open points for modelling

1. **`Association` carries the label "Communication".** The class name follows
   the standard, 5.1.3 c), while the readable label is the term used in the
   accompanying publication and the modelling tool. One class, two labels, no
   equivalence between a standard term and an own term.

2. **Technologies are an addition.** ISO/IEC 7498-1, 1.3 states the reference
   model implies no particular technology. The class exists because an
   engineering model has to record which protocol is used, and the individuals
   live in the instances file, where the list stays open.

3. **Whether a technology fits its layer is a rule, not an axiom.** The pattern
   permits a model to claim MQTT at the network layer. Rejecting that is the
   job of the rule base of the modelling assistance, which keeps the pattern
   descriptive and the judgement where it can be revised.

4. **Peer entities across layers are permitted.** Clause 5.2.1.3 has peer
   entities sit at the same layer, and nothing in the pattern forbids a model
   from relating two entities across layers. Question 13 reports the layer
   alongside each pair, so the violation is readable, but reading it is left to
   whoever looks at the answer.

   Enforcing it would need a property chain comparing the two layers, which OWL
   cannot express as a constraint. This is a SHACL shape, not an axiom. An
   earlier version of this catalogue asked for the violation directly; the
   question answered from the pattern rather than from a case, so it was
   dropped in favour of reporting the layer where it can be seen.

5. **Routing is out of scope.** Clause 5.9 and the relay systems of 6.5.1.2
   describe how a communication is carried across intermediate systems. That is
   the operation of a running communication rather than the structure an
   engineering model records. A model needing it would type the intermediate
   system as an open system and split the communication in two.

6. **Direction is stated twice over, deliberately.** The source and target
   systems say who sends and who receives; `hasDirection` says whether both
   directions are possible at once or only in turn. Neither replaces the other:
   a Profibus segment names its master as source and its slaves as targets, and
   is two-way alternate, since both sides send but never at the same time.

7. **Master and slave are not distinguished.** A bus segment names all its
   participants as source and as target, which records that data flows both
   ways but not which system initiates. ISO/IEC 7498-1 knows no such roles: it
   speaks of end systems and relay systems, 6.5.1, which is about the position
   in a path rather than about who starts an exchange. Recording the roles
   would be an addition, and the pattern leaves it out until a case study needs
   it.

8. **A broker is an open system, not a class of its own.** A publish and
   subscribe arrangement is modelled as two communications, one from the sender
   to the broker and one from the broker to the receivers. The broker is target
   of the first and source of the second, which makes its role visible to a
   query without a relay system class. ISO/IEC 7498-1, 6.5.1.2 defines such a
   class, and the pattern leaves it out for the reason given at point 5.

9. **Connection endpoints are out of scope.** Clause 5.3 details endpoints,
   identifiers and multi-endpoint connections. The pattern keeps the
   transmission mode, which is what has architectural consequences, and leaves
   the machinery.
