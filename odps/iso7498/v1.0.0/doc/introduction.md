<!-- introduction
     Written by hand, the source for the Widoco section of the same name.
     Never edit the generated HTML. -->

An AI application in an automated plant is distributed. The data is recorded by
a sensor, passes a controller, reaches an edge device, and may travel on to a
cloud outside the organisation. Where the inference actually runs is an
architectural decision, and it is made along the path the data takes.

Describing that path needs more than naming a cable. The question is which
components exchange data, over which technology, and what exactly is
transmitted. ISO/IEC 7498-1, the Basic Reference Model of Open Systems
Interconnection, is the standard that answers it, and its seven layers are
familiar enough that an engineer reading a model does not have to learn a new
vocabulary first.

This pattern formalises that model for use in a plant description. A
communication ties components together, is structured into layers, each layer
is realised by a technology, and a data unit is what travels. That is enough to
say that a position signal leaves a sensor over Profibus, reaches a controller,
and goes on to a cloud over HTTPS, all as statements a query can follow.

The pattern is one of three subdomain patterns of the AIAS information model.
None of them is meant to be used on its own. They are imported by the AIAS
alignment ontology, which ties them together at the points where the subdomains
meet, and it is that alignment that lets a single question reach across all of
them, such as which data leaves the organisation and which resource sends it.