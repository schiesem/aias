<!-- description
     Written by hand, the source for the Widoco section of the same name.
     Never edit the generated HTML. -->

Twenty-six classes and four relations. Every class carries a German wording
alongside its English translation. The `skos:note` of each element names the
clause of the standard it rests on, and says so plainly where the term is one
of engineering practice rather than of ISO/IEC 7498-1: several of the classes
below are, and the notes mark each one.

## The communication

A `Communication` is a connection between at least two components describing
the directed exchange of data. It is the entry point of the pattern, and
everything else hangs off it.

A `Name` is the designation a communication is known by. It is not a class of
the standard but a construct of this model, so that a communication can be
referred to by a name of its own.

## The seven layers

A `Layer` is a delimited group of functions carrying out defined communication
tasks at a given level of abstraction. Clause 6.1.2 of the standard enumerates
exactly seven, and each is a subclass here:

| Class | Layer | Clause |
|---|---|---|
| `Physical` | Bitübertragungsschicht | 7.7 |
| `DataLink` | Sicherungsschicht | 7.6 |
| `Network` | Vermittlungsschicht | 7.5 |
| `Transport` | Transportschicht | 7.4 |
| `Session` | Sitzungsschicht | 7.3 |
| `Presentation` | Darstellungsschicht | 7.2 |
| `Application` | Anwendungsschicht | 7.1 |

A communication reaches them through `hasLayer`.

## Data units

A `DataUnit` is a delimited, coherent quantity of data that a layer processes
or transmits as one unit, defined in clause 5.6.

The five subclasses are the names practice gives to the data unit of a
particular layer, and only one of them is a term of the standard:

- `Bit`, of the physical layer. The one practice term ISO/IEC 7498-1 names,
  in 7.7.3.3.1
- `Frame`, of the data link layer. Not defined by the standard. A note to
  7.6.4.5 observes that the delimiting function is sometimes called framing
- `Packet`, of the network layer. A term of the network layer protocol
  standards, not of this one
- `Segment`, of the transport layer. The standard uses *segmenting* in 5.8.1.9
  as the name of a function, not of a data unit
- `Data`, of the upper layers, meaning what an application exchanges

`hasDataUnit` relates a layer, **or the communication itself**, to what it
carries. One relation with two domains: the content transmitted is assigned to
the respective layer, or to the communication directly. It carries `hasDU` as
an alternative label, since that is the short form the relation is commonly
written as.

## Technologies

A `Technology` is a concrete protocol or transmission technique realising the
tasks of a layer. Clause 1.3 states that the fact a system is open implies no
particular implementation or technology, so the standard names none. An
engineering model needs them all the same.

Nine are supplied: `Ethernet` and `Ethernet1000BASET`, `IP`, `TCP`, `HTTP`,
`HTTPS`, `FTP`, `MQTT` and `DHCP`. A layer reaches its technology through
`usesTechnology`.

## Disjointness

Four axioms. The five root classes are pairwise disjoint, and so are the
members of each of the three sets of subclasses: the seven layers, the five
kinds of data unit, and the nine technologies. Nothing can be a layer and a
technology at once, nor a frame and a packet.