<!-- introduction
     Written by hand, the source for the Widoco section of the same name.
     Never edit the generated HTML. -->

Three standards describe an AI application in an automated plant, and each
describes a third of it. VDI/VDE 3682 covers the technical process, ISO/IEC
7498-1 the communication, ISO/IEC 22989 the artificial intelligence. Each has a
pattern of its own, and each answers questions inside its own subdomain.

The questions that matter cross the boundaries. Which resource carries out the
inference, and which process step does that same resource perform? Which data
leaves the organisation, and over which communication? Where was the data
recorded that a model was trained on? None of these can be asked of one pattern
alone, because the terms they join belong to different ones.

This ontology is what closes that gap. It imports the three patterns and ties
them together at the points where the subdomains meet.

The mechanism is three collecting classes. A **function** is any purposeful
transformation, so a process operator of VDI 3682 and an inference of
ISO/IEC 22989 both sit below it. A **component** is any physical element of the
plant. A **relation** is a tie between the two, and the assignment, the flow
and the communication are its three specialisations, one from each pattern.

What that buys is a single mechanism where there were three. The same
assignment that ties a stamping step to a motor ties an inference to a cloud,
and a query asking which resource carries which function does not have to know
whether the function is a process step or a piece of AI.

**Nothing here is normative.** The three patterns rest on standards. This
ontology rests on design decisions, and the notes on each class say which
decision and why. Where a choice could have gone the other way, the note says
that too.
