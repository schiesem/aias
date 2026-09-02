<!-- description
     Written by hand, the source for the Widoco section of the same name.
     Never edit the generated HTML. -->

Twelve classes and seven relations. Every class carries the German wording of
the standard alongside an English translation. The
`skos:note` of each element names the section of the standard it rests on, and
says so explicitly where the pattern departs from it.

## The process and what bounds it

A `Process` is a network. Its nodes are the states of products, energies and
information, and its directed edges are the transformation steps. It reaches
its elements through `consistsOf`, whose range takes in the process itself:
that is how this version records decomposition, a process consisting of further
processes.

A `ProcessOperator` is a single transformation step. It turns the input state
of products, energies or information into an output state, and it is the class
around which everything else is arranged.

A `SystemBorder` bounds the observation horizon. It answers the question of
what is described and what is left outside, and under certain conditions it
also serves as a balance limit for incoming and outgoing products and energies.

## States, and the things that have them

A `State` is the condition of something at a given point of a process, either
before a transformation or after it. `Product`, `Energy` and `Information` are
the three kinds of things that have a state.

They are **not** subclasses of `State`. A product is not a condition, it has
one, which `hasState` records. Keeping the thing apart from its condition is
what lets the same product appear in two states.

## Flows

A `Flow` is a directed connection between process operators. In the graphical
notation of Part 1 it is an edge; here it is a class, so that the connection
itself can carry something. What it carries is a state, through `hasState`.

`ParallelFlow` and `AlternativeFlow` are subclasses. The standard models
concurrent runs as a partially shared flow and mutually exclusive paths as
separate flows, and needs no extra symbols for either. Naming the two cases is
a decision of this pattern.

A process operator reaches its flows through `hasInput` and `hasOutput`, and
the flow reaches back through `isInput` and `isOutput`. Both directions are
stated, because a model may describe a process from either end.

## Resources and their assignment

A `TechnicalResource` is a physical component of the plant: a motor, a sensor,
a controller, a computer. Resources realise the transformations that process
operators describe.

An `Assignment` states that a particular resource carries out a particular
operator. Like the flow, it is an edge of the graphical notation, the usage
symbol, reified here as a class.

`isAssignedTo` runs along a chain of two steps, from the operator to the
assignment and from the assignment to the resource. One relation, used twice,
whose domain and range are therefore unions covering both ends of the chain.

This is the point at which the pattern earns its place in the AIAS model. The
same assignment that ties a stamping step to a motor ties an inference to a
cloud, and that is what makes it possible to ask which resource carries which
function without caring whether the function is a process step or a piece of AI.
