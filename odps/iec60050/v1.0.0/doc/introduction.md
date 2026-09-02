<!-- introduction
     Written by hand, the source for the Widoco section of the same name.
     Never edit the generated HTML. -->

A plant that runs an AI application is a controlled plant first. Sensors
measure, controllers compare against a set point, actuators intervene, and the
AI sits somewhere in that arrangement, either observing it or acting in it.
Describing the AI without describing the control leaves out the part that
determines what the AI can do at all.

The difficulty is that control technology is described in prose, and the prose
is imprecise where it matters most. Whether an arrangement is an open-loop or a
closed-loop control is not a matter of naming: it depends on whether the
controlled variable influences itself continuously through the action path. A
diagram shows that, a sentence usually does not, and a query can read neither.

This pattern formalises the terminology of DIN IEC 60050-351, the
International Electrotechnical Vocabulary for control technology. It models a
control as a chain of action paths and actions, so the distinction that the
standard makes in words becomes a distinction a reasoner can check. Around that
chain sit the variable quantities of a control loop, the devices carrying out
the control, the normative taxonomy of control functions, and the
characteristics a device has.

The standard holds 409 entries and this pattern takes up 86 of them. Roughly
150 of the rest are the mathematical apparatus of control theory, transfer
functions and Nyquist plots among them, which an engineering model names but
never instantiates. `REFERENCE.md` lists every entry with the reason it was
taken or left out, so the selection is checkable rather than asserted.

The pattern is a subdomain pattern of the AIAS information model and is meant
to be imported and aligned rather than used on its own.
