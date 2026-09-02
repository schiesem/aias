# Test Cases: ISO/IEC 7498-1 Pattern

Four test cases built from the reference model of ISO/IEC 7498-1, second
edition 1994. A reviewer can hold every model against the standard.

Two rules govern these cases, the same as for the VDI 3682 pattern:

1. **Taken from the standard.** The structure follows Figures 9 and 11, and the
   element names stay neutral, `SystemA` and `SystemB`, as the standard's own
   figures do. Nothing is borrowed from a case study.
2. **Independent of the alignment.** No test case assumes anything about AI,
   plants, or technical processes. They exercise the ISO 7498 pattern alone, so
   a failure can only come from this pattern.

| Case | Source | Covers |
|---|---|---|
| 1 | Figure 11, clause 6.1 | two systems communicating over a layer, level 1 |
| 2 | Figures 9 and 11, clause 5 | the same communication refined to level 2 |
| 3 | clause 5.8.4, 6.4 | connectionless mode |
| 4 | clause 5.3.1.4, 5.3.1.9 | a communication with more than two participants |

Each case also carries a different direction of data flow, so the three
directions of 5.3.1.14 to 5.3.1.16 are covered between them: case 1 is two-way
simultaneous with both systems sending and receiving, case 2 two-way alternate
from A to B, case 3 one-way.

Cases 2 to 4 take case 1 as their starting point and change exactly one thing:
case 2 adds the architectural detail, case 3 switches the transmission mode,
case 4 raises the number of participants.

**Why the cases are neutral.** ISO/IEC 7498-1 draws its figures with unnamed
open systems, since 1.3 states that the reference model implies no particular
implementation or technology. Naming the systems after a case study would carry
in assumptions the pattern does not make and would tie the test to a domain the
pattern is meant to be independent of.

---

## Case 1: two systems communicating, level 1

`tests/data/tc1_communication.ttl`, after Figure 11.

```
    ┌─────────────┐                                    ┌─────────────┐
    │  SystemA    │                                    │  SystemB    │
    │             │                                    │             │
    │  Open       │◀───────── Communication ──────────▶│  Open       │
    │  System     │      application layer, MQTT       │  System     │
    └─────────────┘      over TCP, IPv4, Ethernet      └─────────────┘
                                    │
                                    │ hasQualityOfService
                                    ▼
                         ┌─────────────────────┐
                         │ transit delay 12 ms │
                         │ throughput 100 Mbit/s│
                         └─────────────────────┘
```

**What it puts under test.** This is the level at which an engineering model
normally works: two systems, one communication, the layer it uses, the
technologies realising it, and what the communication delivers. Nothing of
clause 5 appears, which is the point: a model may stay here.

The communication names four technologies, one per layer involved. Each
technology already knows the layer it realises, asserted once in
`ISO7498-instances.ttl`, so the model need only name the technology. Whether
those technologies fit the layer the communication claims is a question for the
rule base of the modelling assistance, not for this pattern.

**Quality of service.** Two values, transit delay and throughput, both named in
7.4.4. They are reified, so a value carries its parameter, its quantity, and
its unit and can be referred to. This is the vocabulary the technical process
pattern lacks for non-functional properties, and it is why the class is here.

## Case 2: the same communication refined to level 2

`tests/data/tc2_layered.ttl`, after Figures 9 and 11.

Case 1 with the architecture of clause 5 filled in for the three lower layers,
which is what a model does when the detail is needed.

```
        SystemA                                            SystemB
    ┌───────────────┐                                  ┌───────────────┐
    │ Subsystem L4  │  entity ◀── peerEntity ──────────▶ entity        │
    │  TransportSAP │     │                            │    │          │
    ├───────────────┤     │ atLayer                    ├───────────────┤
    │ Subsystem L3  │  entity ◀── peerEntity ──────────▶ entity        │
    │  NetworkSAP   │     │                            │    │          │
    ├───────────────┤     │                            ├───────────────┤
    │ Subsystem L2  │  entity ◀── peerEntity ──────────▶ entity        │
    └───────────────┘                                  └───────────────┘

    encapsulation, Figure 9

    TransportPDU ──mapsToServiceDataUnit──▶ NetworkSDU
                                                 │
                                            NetworkPDU ──▶ DataLinkSDU
                                                                 │
                                                            DataLinkPDU
```

**What it puts under test.** Three things the standard states and this pattern
has to reproduce.

Subsystems belong to exactly one layer each, 5.2.2.1, and hold entities,
5.2.1.11. Entities of the same layer in different systems are peer entities,
5.2.1.3, which the symmetric `peerEntity` relation records.

A service access point attaches to one entity of its layer and one of the layer
above, 5.5.5, and both lie in the same system, 5.5.2.

The encapsulation of Figure 9: a protocol data unit of one layer becomes the
service data unit of the layer below, which combined with that layer's control
information forms its protocol data unit. The chain runs from the transport
layer down to the data link layer, so a query can follow a datum through the
layers, which is the claim the practice terms frame and packet only gesture at.

**What is deliberately incomplete.** Only three layers are refined. The
standard needs no model to elaborate all seven, and leaving four at level 1
demonstrates that the two levels coexist: `SystemA` carries subsystems for
layers 2 to 4 and nothing for the rest, while the communication of case 1
remains valid.

## Case 3: connectionless mode

`tests/data/tc3_connectionless.ttl`, after 5.8.4 and 6.4.

Case 1 with the transmission mode changed, and nothing else.

```
    ┌─────────────┐                                    ┌─────────────┐
    │  SystemA    │◀──── Connectionless Communication ▶│  SystemB    │
    └─────────────┘       application layer, MQTT      └─────────────┘
                          over UDP, IPv4, Ethernet
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ transit delay 3 ms  │
                         │ residual error rate │
                         └─────────────────────┘
```

**What it puts under test.** ISO/IEC 7498-1 distinguishes connection-mode from
connectionless-mode operation throughout, and 6.4 restricts how the two may be
combined across layers. The two subclasses of communication are disjoint, so a
model cannot declare both at once, which the negative models check.

The transport technology changes from TCP to UDP with the mode, which is the
practical consequence a model records.

**Why the quality of service parameters differ.** Case 1 states an
establishment delay, since a connection is established before data flows.
Case 3 does not: 7.4.4 defines establishment delay for connection-mode
communication, and there is no establishment in connectionless mode. Instead it
states a residual error rate, which is what a connectionless service leaves to
the layer above. Query `cq23` reports the parameters per communication, so the
difference is visible rather than asserted in prose.

## Case 4: a communication with more than two participants

`tests/data/tc4_multiendpoint.ttl`, after 5.3.1.4 and 5.3.1.9.

```
                    ┌─────────────┐
                    │  SystemA    │  initiates
                    └──────┬──────┘
                           │
    ═══════════════════════╪═══════════════════════  Bus segment
           │               │               │          PROFIBUS
    ┌──────┴──────┐ ┌──────┴──────┐ ┌──────┴──────┐   two-way alternate
    │  SystemB    │ │  SystemC    │ │  SystemD    │
    └─────────────┘ └─────────────┘ └─────────────┘

    one communication, four participants
```

**What it puts under test.** ISO/IEC 7498-1, 5.3.1.4 calls a connection with
more than two connection endpoints a multi-endpoint connection, and 5.3.1.9
defines data transmission as conveying service data units from one entity to
one or more entities. The pattern asserts no cardinality on `connects` for that
reason, and this case is what verifies the claim: a fieldbus segment is one
communication with four participants rather than three or six point to point
objects.

Cases 1 to 3 all have exactly two participants, so without this case the
absence of a cardinality would be an untested assertion. Query `cq29` counts
the participants and reports which communications are multi-endpoint.

**All four systems are named on both sides**, since the responders answer the
initiator. Direction is two-way alternate, 5.3.1.15, which is what master and
slave access amounts to: both sides send, but never at the same time. That the
pattern does not distinguish an initiating system from a responding one is a
limit recorded in the catalogue, since ISO/IEC 7498-1 knows no such roles.

---

## Negative models

Each file under `tests/negative/` violates exactly one axiom, so a failure
names its own cause. All must be rejected by the reasoner; a model that is
accepted proves the axiom under test does not bite.

| File | Axiom | Normative basis |
|---|---|---|
| `neg01_layer_is_system` | `Layer` and `OpenSystem` are disjoint | a layer is a subdivision of the architecture, 5.2.1.2, a system an entity of the real world, 4.1.3 |
| `neg02_both_transmission_modes` | the two modes are disjoint | 6.4 treats them as alternatives throughout |
| `neg03_pdu_is_pci` | `ProtocolDataUnit` and `ProtocolControlInformation` are disjoint | 5.6.1.3: a protocol data unit *consists of* control information, so it is not one |
| `neg04_technology_realises_two_layers` | `realisesLayer` is functional | a technology realises the services of one layer |
| `neg05_value_for_two_parameters` | `forParameter` is functional | one value quantifies exactly one parameter |

---

## Running

```bash
python ../../shared/run_tests.py --package iso7498
```

The queries are also the debugging tool: a failing competency question names
the relation that is missing, which is more precise than reading it off a
diagram. `RESULTS.md` carries every question with its result and an
interpretation.
