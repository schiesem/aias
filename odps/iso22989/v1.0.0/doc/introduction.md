<!-- introduction
     Written by hand, the source for the Widoco section of the same name.
     Never edit the generated HTML. -->

Asking where an AI application runs in a plant sounds like a question about
hardware. It is not. The answer depends on what the application does: a wear
classification that tolerates a delay of minutes can run in a cloud, while a
rework decision that has to finish inside the production cycle of one part
cannot. To decide that from a model rather than from experience, the model has
to state what the AI consumes, what it produces, and what it was asked for.

This pattern supplies the vocabulary for that, following ISO/IEC 22989, the
standard that fixes the terminology of artificial intelligence. It is used
because it is a terminology standard rather than a method: it names what an AI
system, a model, a training and a dataset are, without prescribing how any of
them is built.

Three views of the same system are covered. The system view has the AI system,
its components, the functions of its life cycle and the tasks it addresses. The
algorithmic view has the algorithms, the models they produce, and the
parameters that configure them. The data view has the kinds of data and the
processes that acquire, prepare, merge and store them.

The three meet at one point, and that is what makes the pattern useful: a
training is a function, it consumes a dataset, and it produces a model. Follow
that chain backwards and a model can be traced to the data it was built from,
and from there to the device that recorded it.

The pattern is one of three subdomain patterns of the AIAS information model.
The other two cover the technical process (VDI/VDE 3682) and communication
(ISO/IEC 7498-1). None of them is meant to be used on its own. They are
imported by the AIAS alignment ontology, which ties them together at the points
where the subdomains meet, and it is that alignment that lets a single question
reach across all of them, such as which resource carries out an inference and
which process step that same resource performs.
