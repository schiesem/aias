# Diagram conventions

Binding for every diagram of this project. Written down so that the patterns,
which are drawn at different times, do not drift apart in their notation.

The style follows the figures of the dissertation, so that a reader who knows
those recognises these. Three elements are added, because the patterns here
carry things the dissertation figures did not have to show: data properties,
imported individuals, and functional properties.

Sources are PlantUML in `<package>/figures/*.puml`, rendered by
`shared/make_figures.py` to SVG. The sources are versioned, the renderings are
not.

---

## 1. What a diagram is for

A diagram shows the whole of a view, not the whole of an ontology. It answers
"how do these concepts hang together", and it is allowed, indeed required, to
leave things out to do so. The complete picture is the WebVOWL view that Widoco
generates, and it is not a substitute for a drawing.

Every source carries a header comment stating what it leaves out and why, so a
reader can tell a deliberate omission from an oversight.

## 2. Elements

| Element | Drawn as |
|---|---|
| Class | Flat rectangle, class name only |
| Subclass | Generalisation, hollow triangle at the superclass |
| Object property | Directed edge, name written on the edge |
| Data property | Line inside the box, prefixed `dataProp:` |
| Imported individuals | Compartment inside the box, headed `«enum»` |
| Functional property | Multiplicity `1` at the arrowhead |
| Equivalent class | Undirected edge labelled `owl:equivalentClass` |

## 3. What is left out on purpose

**No namespace prefixes in a pattern diagram.** A pattern diagram shows one
namespace, so writing it on every box is noise. The alignment diagram is the
exception: there the namespace is the statement, so every class carries its
prefix and a legend resolves the prefixes to their IRIs.

**No clause numbers.** `«351-47-04»` on a box helps someone checking a single
class against the standard, but a diagram is for the overall picture, and the
ontology carries the clause on every term anyway. The clause belongs in the
running text where a single class is discussed.

**No disjointness markers.** `{disjoint}` on every generalisation set would
fill an overview drawing with an axiom that a reader of the overview does not
act upon.

**No notes inside the drawing.** Everything explanatory goes into the
`\figcaption`. A figure that needs a sticky note to be understood has not been
drawn tightly enough, and the note is not translatable into the caption style
the journal expects.

## 4. Colour

One fill for classes of the pattern being shown, a second for classes reached
from another pattern. Nothing else is coloured.

Colour never carries a statement on its own. The figures must survive being
printed in greyscale, so anything colour separates must also be separated by
position, by name or by an edge.

| Role | Fill | Border |
|---|---|---|
| Class of this pattern | `#FCEFC7` | `#C9A227` |
| Class from another pattern | `#FFFFFF` | `#8A98A8` |

## 5. Layout

Orthogonal edges, never curves. Left to right or top to bottom, one direction
per diagram. Related classes stand next to one another rather than being tied
together by a frame.

Edges must not cross where an arrangement avoids it. Where a generalisation
would have to cross the whole drawing, it is left out and the relationship is
stated in the caption instead.

## 6. Captions

The caption says what can be seen, in at most two sentences, and carries the
clause numbers of the classes shown. Interpretation belongs in the running
text, not in the caption.

## 7. Excerpts from standards

A figures directory may hold files named `norm-*.png`, which are pages or
figures from a purchased standard. They are placed there by hand, excluded from
version control, and never produced or removed by the tooling.

Clearing rendered output has to spare them. `rm figures/*.png` deletes them
along with the renderings, and they cannot be regenerated.

## 8. The overview diagram

Every package may carry one diagram that shows the whole of the pattern rather
than one statement. It is for the documentation, not for a paper, and it is the
one place where the rule of section 1 is set aside on purpose.

Its value is completeness: a reader asking what a pattern offers gets an answer
without opening the Turtle. Its header comment has to say which classes it
leaves out and why, since a diagram claiming to show everything invites the
reader to assume nothing is missing.

## 9. One statement per diagram

A diagram that needs a dozen boxes on one node has two statements in it and
should be split. The IEC 60050 package splits its functional diagram that way:
diagram 2 carries the mechanism, how a path decomposes into lines and how a
line reaches units, and diagram 2b carries the units the standard names. Both
stay readable. Together in one drawing neither did.

Where a diagram is about the shape of a chain rather than about a hierarchy,
draw it as a flow of boxes and edges instead of as a class diagram. Diagram 4
does that, and the single edge running back up the page is what makes the cycle
visible.
