# IEC 60050-351: Reference of All Entries

Every entry of DIN IEC 60050-351:2014, the International Electrotechnical
Vocabulary, Part 351: Control technology, with a note on whether the
pattern takes it up.

The table exists so that the selection is checkable. A pattern that takes
a quarter of 409 entries has to say which ones and why the rest stay out,
otherwise the choice looks arbitrary. Leaving an entry out is a decision, not an
oversight, and this is where those decisions are recorded.

**Why not all of them.** The vocabulary is a dictionary, not an ontology.
Roughly 150 entries are the mathematical apparatus of control theory, such
as transfer functions, Nyquist plots or pole assignment. They are terms an
engineer uses, not things an engineering model instantiates: no model ever
creates an instance of a root locus plot. Taking them up would produce
classes that stay empty, that no competency question reaches, and that no
test case exercises.

**What the selection follows.** An entry is taken up when it stands in a
relation the pattern needs, appears in a test case, and answers a
competency question. Characteristics that a model states as a value, such
as a sampling period or an overshoot, become named individuals rather than
classes, in the same way and for the same reason as the quality of service
parameters of the ISO 7498 pattern.

Legend: **taken** names the class or individual the entry becomes.
**out** gives the reason, or refers to the reason stated for its section.

---

## Six entries dropped after review

`ActualValue` 351-41-02, `DesiredValue` 351-41-03, `Automaton` 351-42-32,
`Prediction` 351-47-47, `Risk` 351-57-03 and `TechnicalProcess` 351-42-34 were
taken up at first and removed again. None of them took part in any relation, so
no model could reach them and no competency question returned them.

**The criterion applied here**: a term enters the pattern when it appears in a
relation, or when it is documented what it is there for otherwise. Standing in
the standard is not enough on its own, since this table exists precisely to
record that leaving an entry out is a decision.

Two of the six could not be related without inventing something. 351-41-02 and
351-41-03 define the actual and the desired value as the value of a variable
quantity **at a given instant**, and this pattern carries no notion of time. A
relation such as hasActualValue would state a value without the instant its
definition requires. Note also that the desired value, symbol Xd, is not the
reference variable w: the reference variable is a quantity in the control loop,
the desired value is what that quantity should be at one instant.

The remaining four were taken up because they are terms of the standard, which
this review found to be an insufficient reason on its own. Any of them can be
taken back up once a model or the alignment needs it.

## Elements taken from the figures rather than from the entries

One class of the pattern has no entry in the standard. It is drawn in Figures 1
and 2 and named there, but carries no number, no definition and no index line.
A search of the full text finds the wording only inside the two figures.

| Element | Where it appears | Why it is kept |
|---|---|---|
| `FinalControlledVariableGeneration` | the box at the right-hand edge of Figures 1 and 2, where x enters and q leaves | the final controlled variable it produces is a term, 351-48-10, and without a unit for it that variable would have no origin in a model |

It is recorded here so that the selection stays checkable in both directions:
the table above says which entries are taken up, and this one says what is in
the pattern without being an entry. Anyone aligning this pattern with another
should treat the class as a construct of this work rather than as normative
vocabulary.

## 351-41 Variables and signals

15 entries, 2 taken up.

| Code | Term | In the pattern |
|---|---|---|
| 351-41-14 | binary variable | out |
| 351-41-15 | continuous-time variable | out |
| 351-41-16 | discrete-time variable | out |
| 351-41-17 | signal | **Signal** |
| 351-41-18 | information parameter | **InformationParameter** |
| 351-41-19 | continuous-value signal | out |
| 351-41-20 | discrete-value signal | out |
| 351-41-21 | binary signal | out |
| 351-41-22 | continuous-time signal | out |
| 351-41-23 | discrete-time signal | out |
| 351-41-24 | Leittechnik anzupassen.] | out |
| 351-41-25 | digital signal | out |
| 351-41-26 | sampled signal | out |
| 351-41-27 | Definitionen abgeleitete neue Formulierung.] | out |
| 351-41-28 | Frequenzen beitragen | out |

## 351-42 General concepts

39 entries, 10 taken up.

| Code | Term | In the pattern |
|---|---|---|
| 351-42-01 | ? | out |
| 351-42-02 | ? | out |
| 351-42-03 | ? | out |
| 351-42-04 | ? | out |
| 351-42-05 | ? | out |
| 351-42-06 | ? | out |
| 351-42-07 | transition matrix | out |
| 351-42-08 | system | **System** |
| 351-42-09 | structure | out |
| 351-42-10 | system parameter | out |
| 351-42-11 | linear system | out |
| 351-42-12 | linearize, verb | out |
| 351-42-13 | characteristic equation | out |
| 351-42-14 | time-invariant system | out |
| 351-42-15 | beeinflusst | out |
| 351-42-16 | darzustellen | out |
| 351-42-17 | minimal-phase system | out |
| 351-42-18 | all-pass system | out |
| 351-42-19 | ? | **Control** |
| 351-42-20 | Ruhelage verbleiben | **Stability** |
| 351-42-21 | asymptotic stability | out |
| 351-42-22 | controllability | **Controllability** |
| 351-42-23 | observability | **Observability** |
| 351-42-24 | action | **Action** |
| 351-42-25 | interface | out |
| 351-42-26 | model | **Model** |
| 351-42-27 | algorithm | out |
| 351-42-28 | redundancy | **Redundancy** |
| 351-42-29 | erfordert | out |
| 351-42-30 | automatic, adj | out |
| 351-42-31 | degree of automation | **DegreeOfAutomation** |
| 351-42-32 | automaton | out |
| 351-42-33 | process in control technology | out |
| 351-42-34 | technical process | out |
| 351-42-35 | plant | **Plant** |
| 351-42-36 | cybernetics | out |
| 351-42-37 | expert system | out |
| 351-42-38 | knowledge base | out |
| 351-42-39 | inference engine | out |

## 351-43 Tasks and functions in control technology

24 entries, 10 taken up.

| Code | Term | In the pattern |
|---|---|---|
| 351-43-01 | measure, verb | **Measure** |
| 351-43-02 | count, verb | out |
| 351-43-03 | monitor, verb | **Monitor** |
| 351-43-04 | indicate, verb | out |
| 351-43-05 | notify, verb | **Notify** |
| 351-43-06 | alert, verb | out |
| 351-43-07 | Betriebsbedingungen liegt | **Warn** |
| 351-43-08 | alarm, verb | **Alarm** |
| 351-43-09 | record, verb | out |
| 351-43-10 | wird | out |
| 351-43-11 | archive, verb | out |
| 351-43-12 | manipulate, verb | **Manipulate** |
| 351-43-13 | evaluate, verb | **Evaluate** |
| 351-43-14 | optimize, verb | **Optimize** |
| 351-43-15 | intervene, verb | **Intervene** |
| 351-43-16 | safeguard, <equipment> verb | out |
| 351-43-17 | safeguard, <action> verb | out |
| 351-43-18 | lock, verb | out |
| 351-43-19 | structure, verb | out |
| 351-43-20 | configure, verb | out |
| 351-43-21 | parameterize, verb | out |
| 351-43-22 | automate, verb | out |
| 351-43-23 | acknowledge, verb | out |
| 351-43-24 | operate, verb | **Operate** |

## 351-44 Structures of control systems

10 entries, 3 taken up.

| Code | Term | In the pattern |
|---|---|---|
| 351-44-01 | Verzweigungsstelle. | out |
| 351-44-02 | Schaltfunktion angegeben werden. | out |
| 351-44-03 | action path | **ActionPath** |
| 351-44-04 | action line | **ActionLine** |
| 351-44-05 | direction of action | **fromUnit / toUnit** |
| 351-44-06 | summing point | out |
| 351-44-07 | branching point | out |
| 351-44-08 | ist | out |
| 351-44-09 | werden | out |
| 351-44-10 | ? | out |

## 351-45 Behaviour and characteristics

55 entries, 5 taken up.

*Entries not taken up: mathematical apparatus of control theory: transfer functions, frequency response, poles and zeros. Not instantiated in an engineering model. Selected time and quality characteristics are taken as named individuals.*

| Code | Term | In the pattern |
|---|---|---|
| 351-45-01 | principle of superposition | out |
| 351-45-02 | principle of shifting | out |
| 351-45-03 | festlegen | out |
| 351-45-04 | linear transfer element | out |
| 351-45-05 | time-invariant transfer element | out |
| 351-45-06 | Verteilung darzustellen | out |
| 351-45-07 | Systems darstellt | out |
| 351-45-08 | transient behaviour | out |
| 351-45-09 | vorgegebenen Betriebsbedingungen hervorgerufen wird | out |
| 351-45-10 | Leittechnik anzupassen.] | out |
| 351-45-11 | Kennlinienschar. | out |
| 351-45-12 | operating point | out |
| 351-45-13 | ? | out |
| 351-45-14 | ? | out |
| 351-45-15 | Zone genannt. | **individual DeadBand** |
| 351-45-16 | durchlaufen wird | out |
| 351-45-17 | reset windup | out |
| 351-45-18 | damping | out |
| 351-45-19 | damping ratio | out |
| 351-45-20 | entsprechend modifiziert. | out |
| 351-45-21 | Zusammenhang entsprechend festgelegt werden. | out |
| 351-45-22 | 4 a) 4 b) 4 c) | out |
| 351-45-23 | δ | out |
| 351-45-24 | ε | out |
| 351-45-25 | ρ | out |
| 351-45-26 | δ δ δ 0 | out |
| 351-45-27 | ? | out |
| 351-45-28 | seiner Sprungantwort. | out |
| 351-45-29 | unit-impulse response | out |
| 351-45-30 | unit-step response | out |
| 351-45-31 | unit-ramp response | out |
| 351-45-32 | time constant | **individual TimeConstant** |
| 351-45-33 | ? | out |
| 351-45-34 | ? | **individual EquivalentDeadTime** |
| 351-45-35 | ? | out |
| 351-45-36 | ? | out |
| 351-45-37 | ? | **individual SettlingTime** |
| 351-45-38 | step of the disturbance variable (bottom) | **individual Overshoot** |
| 351-45-39 | transfer function | out |
| 351-45-40 | Anfangswerte gleich null sind | out |
| 351-45-41 | ? | out |
| 351-45-42 | ? | out |
| 351-45-43 | ? | out |
| 351-45-44 | ? | out |
| 351-45-45 | ? | out |
| 351-45-46 | ? | out |
| 351-45-47 | ? | out |
| 351-45-48 | corner angular frequency | out |
| 351-45-49 | ? | out |
| 351-45-50 | describing function | out |
| 351-45-51 | rational transfer element | out |
| 351-45-52 | minimal-phase element | out |
| 351-45-53 | all-pass element | out |
| 351-45-54 | konstanten Beharrungswert zustrebt | out |
| 351-45-55 | ? | out |

## 351-46 Behaviour and characteristics of control loops

14 entries, 4 taken up.

*Entries not taken up: frequency domain analysis of control loops. Selected stability margins are taken as named individuals.*

| Code | Term | In the pattern |
|---|---|---|
| 351-46-01 | step of the disturbance variable (bottom) | **individual ControlRiseTime** |
| 351-46-02 | step of the disturbance variable (bottom) | **individual ControlSettlingTime** |
| 351-46-03 | open-loop frequency response | out |
| 351-46-04 | ? | out |
| 351-46-05 | ? | **individual PhaseMargin** |
| 351-46-06 | ? | out |
| 351-46-07 | ? | **individual GainMargin** |
| 351-46-08 | 1+K 0 | out |
| 351-46-09 | Messeinrichtung wird dabei zu eins angenommen. | out |
| 351-46-10 | ? | out |
| 351-46-11 | phase plane analysis | out |
| 351-46-12 | step of the disturbance variable (bottom) | out |
| 351-46-13 | step of the disturbance variable (bottom) | out |
| 351-46-14 | hunting | out |

## 351-47 Types of control

63 entries, 24 taken up.

| Code | Term | In the pattern |
|---|---|---|
| 351-47-01 | closed-loop control | **ClosedLoopControl** |
| 351-47-02 | open-loop control | **OpenLoopControl** |
| 351-47-03 | closed action path | **ClosedActionPath** |
| 351-47-04 | damit fortlaufend sich selbst beeinflusst | **ClosedAction** |
| 351-47-05 | open action path | **OpenActionPath** |
| 351-47-06 | open action | **OpenAction** |
| 351-47-07 | forward path | **ForwardPath** |
| 351-47-08 | feedback path | **FeedbackPath** |
| 351-47-09 | and reference-variable feedforward control (bottom) | out |
| 351-47-10 | and reference-variable feedforward control (bottom) | out |
| 351-47-11 | control loop | **ControlLoop** |
| 351-47-12 | control chain | **ControlChain** |
| 351-47-13 | Verhalten zu erzeugen | out |
| 351-47-14 | (Zweipunktregler). | out |
| 351-47-15 | konstant gehalten werden | **SamplingControl** |
| 351-47-16 | Abtastung | **individual SamplingPeriod** |
| 351-47-17 | fixed set-point control | out |
| 351-47-18 | time scheduled closed-loop control | out |
| 351-47-19 | ? | out |
| 351-47-20 | programmed control | **ProgrammedControl** |
| 351-47-21 | Verbindungen zwischen diesen Einheiten bestimmt ist | out |
| 351-47-22 | storage-programmable logic control | out |
| 351-47-23 | non-clocked control | out |
| 351-47-24 | clocked control | out |
| 351-47-25 | cascade control | **CascadeControl** |
| 351-47-26 | secondary control | out |
| 351-47-27 | ratio control | out |
| 351-47-28 | x Zustandsvektor State vector Vecteur d’état | out |
| 351-47-29 | output-feedback control | out |
| 351-47-30 | distributed feedback control | out |
| 351-47-31 | x Zustandsvektor State vector Vecteur d’état | **Observer** |
| 351-47-32 | x Zustandsvektor State vector Vecteur d’état | out |
| 351-47-33 | model-based control | **ModelBasedControl** |
| 351-47-34 | modal control | out |
| 351-47-35 | multivariable control | **MultivariableControl** |
| 351-47-36 | Regelungssysteme. | out |
| 351-47-37 | decoupling | out |
| 351-47-38 | centralized control | out |
| 351-47-39 | decentralized control | out |
| 351-47-40 | hierarchical control | out |
| 351-47-41 | optimal control | **OptimalControl** |
| 351-47-42 | adaptive control | **AdaptiveControl** |
| 351-47-43 | parameter identification | out |
| 351-47-44 | parameter sensitivity | out |
| 351-47-45 | dienen. | **RobustControl** |
| 351-47-46 | ? | out |
| 351-47-47 | prediction | out |
| 351-47-48 | vorbestimmten Grenzwerte erreicht | out |
| 351-47-49 | alternative control | out |
| 351-47-50 | split-range control | out |
| 351-47-51 | switching control | out |
| 351-47-52 | computer control | **ComputerControl** |
| 351-47-53 | time-shared control | out |
| 351-47-54 | Abtastperiode berechnet | out |
| 351-47-55 | velocity algorithm | out |
| 351-47-56 | fuzzy control | **FuzzyControl** |
| 351-47-57 | membership function | out |
| 351-47-58 | rule-based control | **RuleBasedControl** |
| 351-47-59 | sequential control | **SequentialControl** |
| 351-47-60 | process-oriented sequential control | out |
| 351-47-61 | time-oriented sequential control | out |
| 351-47-62 | reset circuit | out |
| 351-47-63 | ? | out |

## 351-48 Variables and signals in control systems

18 entries, 10 taken up.

| Code | Term | In the pattern |
|---|---|---|
| 351-48-01 | controlled variable | **ControlledVariable** |
| 351-48-02 | reference variable | **ReferenceVariable** |
| 351-48-03 | feedback variable | **FeedbackVariable** |
| 351-48-04 | control difference variable | out |
| 351-48-05 | bleibende Regeldifferenz, f | **ControlDifferenceVariable** |
| 351-48-06 | controller output variable | **ControllerOutputVariable** |
| 351-48-07 | manipulated variable | **ManipulatedVariable** |
| 351-48-08 | disturbance variable | **DisturbanceVariable** |
| 351-48-09 | command variable | **CommandVariable** |
| 351-48-10 | final controlled variable | **FinalControlledVariable** |
| 351-48-11 | measuring range | out |
| 351-48-12 | measuring span | out |
| 351-48-13 | range of the controlled variable | out |
| 351-48-14 | range of the reference variable | out |
| 351-48-15 | range of the final controlled variable | out |
| 351-48-16 | range of the manipulated variable | out |
| 351-48-17 | manipulating time | **individual ManipulatingTime** |
| 351-48-18 | range of the disturbance variable | out |

## 351-49 Functional units in control systems

11 entries, 11 taken up.

| Code | Term | In the pattern |
|---|---|---|
| 351-49-01 | controlled system | **ControlledSystem** |
| 351-49-02 | controlling system | **ControllingSystem** |
| 351-49-03 | comparing element | **ComparingElement** |
| 351-49-04 | controlling element | **ControllingElement** |
| 351-49-05 | measuring element in control technology | **MeasuringElement** |
| 351-49-06 | control system | **ControlSystem** |
| 351-49-07 | actuator | **Actuator** |
| 351-49-08 | final controlling element | **FinalControllingElement** |
| 351-49-09 | final controlling equipment | **FinalControllingEquipment** |
| 351-49-10 | reference-variable generating element | **ReferenceVariableGeneratingElement** |
| 351-49-11 | controller for closed-loop control | **Controller** |

## 351-50 Characteristics of functional units in control systems

40 entries, 1 taken up.

*Entries not taken up: transfer element taxonomy, that is P, I, D and their combinations, plus arithmetic elements. Describes controller internals rather than the engineering structure this pattern records.*

| Code | Term | In the pattern |
|---|---|---|
| 351-50-01 | Nullstellen besitzt | out |
| 351-50-02 | first-order lag element | out |
| 351-50-03 | second-order lag element | out |
| 351-50-04 | lead-lag element | out |
| 351-50-05 | proportional element | out |
| 351-50-06 | proportional action coefficient | out |
| 351-50-07 | proportional band of a controlling element | out |
| 351-50-08 | integral element | out |
| 351-50-09 | integral action coefficient | out |
| 351-50-10 | integral action time | out |
| 351-50-11 | proportional plus integral element | out |
| 351-50-12 | ? | out |
| 351-50-13 | derivative element | out |
| 351-50-14 | derivative action coefficient | out |
| 351-50-15 | derivative action time | out |
| 351-50-16 | proportional plus derivative element | out |
| 351-50-17 | Dabei ist | out |
| 351-50-18 | ? | out |
| 351-50-19 | proportional plus integral plus derivative element | out |
| 351-50-20 | wird Schaltdifferenz genannt (siehe 351-50-25). | out |
| 351-50-21 | ? | out |
| 351-50-22 | on-off element | out |
| 351-50-23 | ? | out |
| 351-50-24 | ? | out |
| 351-50-25 | ? | out |
| 351-50-26 | ? | out |
| 351-50-27 | limit monitor | out |
| 351-50-28 | ? | out |
| 351-50-29 | ? | out |
| 351-50-30 | dead time | **individual DeadTime** |
| 351-50-31 | Totzeitglied beschrieben. | out |
| 351-50-32 | ? | out |
| 351-50-33 | ? | out |
| 351-50-34 | v(t)= K ⋅ 1 1 | out |
| 351-50-35 | function generator | out |
| 351-50-36 | square-root element | out |
| 351-50-37 | squaring element | out |
| 351-50-38 | absolute-value element | out |
| 351-50-39 | sign element | out |
| 351-50-40 | ? | out |

## 351-51 Variables and signals in switching systems

10 entries, 0 taken up.

*Entries not taken up: commands and signals of switching systems, close to programming.*

| Code | Term | In the pattern |
|---|---|---|
| 351-51-01 | checkback signal | out |
| 351-51-02 | enabling signal | out |
| 351-51-03 | blockiert | out |
| 351-51-04 | ? | out |
| 351-51-05 | stored command | out |
| 351-51-06 | conditional command | out |
| 351-51-07 | delayed command | out |
| 351-51-08 | time-limited command | out |
| 351-51-09 | waiting time | out |
| 351-51-10 | check time | out |

## 351-52 Functional units in switching systems

12 entries, 0 taken up.

*Entries not taken up: switching elements, flip-flops, registers, counters. Digital circuit level.*

| Code | Term | In the pattern |
|---|---|---|
| 351-52-01 | switching system | out |
| 351-52-02 | Schaltglieder. | out |
| 351-52-03 | combinatorial circuit | out |
| 351-52-04 | ? | out |
| 351-52-05 | NICHT-Glied Negation; | out |
| 351-52-06 | Englischen streng abgelehnt. | out |
| 351-52-07 | dynamic input | out |
| 351-52-08 | triggered bistable element | out |
| 351-52-09 | monostable multivibrator | out |
| 351-52-10 | binary delay element | out |
| 351-52-11 | register | out |
| 351-52-12 | counter | out |

## 351-53 Characteristics of functional units in switching systems

16 entries, 0 taken up.

*Entries not taken up: function charts and state graphs for sequential control. A description means of its own, closer to IEC 61131-3.*

| Code | Term | In the pattern |
|---|---|---|
| 351-53-01 | switching function | out |
| 351-53-02 | state state | out |
| 351-53-03 | ? | out |
| 351-53-04 | ? | out |
| 351-53-05 | Schalttabelle, f | out |
| 351-53-06 | state graph | out |
| 351-53-07 | Boolean operation | out |
| 351-53-08 | Sinne zu verwenden. | out |
| 351-53-09 | step | out |
| 351-53-10 | transition | out |
| 351-53-11 | transition condition | out |
| 351-53-12 | sequence chain | out |
| 351-53-13 | beginning of sequence selection | out |
| 351-53-14 | end of sequence selection | out |
| 351-53-15 | beginning of simultaneous sequences | out |
| 351-53-16 | end of simultaneous sequences | out |

## 351-54 Process computer systems

20 entries, 2 taken up.

| Code | Term | In the pattern |
|---|---|---|
| 351-54-01 | process computer system | out |
| 351-54-02 | compact process computer system | out |
| 351-54-03 | distributed process computer system | out |
| 351-54-04 | redundant process computer system | out |
| 351-54-05 | process interface | out |
| 351-54-06 | real-time capability | **RealTimeCapability** |
| 351-54-07 | interrupt capability | out |
| 351-54-08 | restart capability | out |
| 351-54-09 | real-time operating system | out |
| 351-54-10 | process monitoring system | out |
| 351-54-11 | process peripherals | out |
| 351-54-12 | analog output unit | out |
| 351-54-13 | digital output unit | out |
| 351-54-14 | analog input unit | out |
| 351-54-15 | digital input unit | out |
| 351-54-16 | timer | out |
| 351-54-17 | interrupt input unit | out |
| 351-54-18 | interrupt reaction time | **individual InterruptReactionTime** |
| 351-54-19 | input transfer rate | out |
| 351-54-20 | output transfer rate | out |

## 351-55 Control hierarchies

16 entries, 0 taken up.

*Entries not taken up: control hierarchies of three levels. The graphical notation of this work follows the automation pyramid with five levels, so the two do not align and mixing them would create friction.*

| Code | Term | In the pattern |
|---|---|---|
| 351-55-01 | ? | out |
| 351-55-02 | manual operation | out |
| 351-55-03 | automatic operation | out |
| 351-55-04 | semi-automatic operation | out |
| 351-55-05 | step-setting operation | out |
| 351-55-06 | time program | out |
| 351-55-07 | priority | out |
| 351-55-08 | ? | out |
| 351-55-09 | kompakt verwendet. | out |
| 351-55-10 | werden. | out |
| 351-55-11 | ? | out |
| 351-55-12 | control level | out |
| 351-55-13 | individual control level | out |
| 351-55-14 | group control level | out |
| 351-55-15 | plant control level | out |
| 351-55-16 | process control function | out |

## 351-56 Specific units in control technology

39 entries, 9 taken up.

| Code | Term | In the pattern |
|---|---|---|
| 351-56-01 | item under consideration | **ItemUnderConsideration** |
| 351-56-02 | functional unit | **FunctionalUnit** |
| 351-56-03 | physical unit | **PhysicalUnit** |
| 351-56-04 | signal generator | out |
| 351-56-05 | filter element | out |
| 351-56-06 | adjuster | out |
| 351-56-07 | control device | out |
| 351-56-08 | time scheduler | out |
| 351-56-09 | clock generator | out |
| 351-56-10 | bus | out |
| 351-56-11 | selbst betreffen, an seinen Folgeteilnehmer weitergibt | out |
| 351-56-12 | star | out |
| 351-56-13 | mesh | out |
| 351-56-14 | OSI/ISO-Sieben-Schicht-Modell organisiert sein. | out |
| 351-56-15 | linking element | out |
| 351-56-16 | actuating drive | out |
| 351-56-17 | positioner | out |
| 351-56-18 | indicating element | out |
| 351-56-19 | liefert | out |
| 351-56-20 | decoupled output | out |
| 351-56-21 | werden | out |
| 351-56-22 | active fault in control equipment | **ActiveFault** |
| 351-56-23 | passive fault in control equipment | **PassiveFault** |
| 351-56-24 | ? | **ControlEquipment** |
| 351-56-25 | Anweisungen | **ProgrammableController** |
| 351-56-26 | entsprechendes Messsignal abgibt | **SensingElement** |
| 351-56-27 | transducing element | out |
| 351-56-28 | measuring transducer | out |
| 351-56-29 | measuring transmitter | **MeasuringTransmitter** |
| 351-56-30 | transformer | out |
| 351-56-31 | barrier | out |
| 351-56-32 | amplifier | out |
| 351-56-33 | operational amplifier | out |
| 351-56-34 | magnetic amplifier | out |
| 351-56-35 | BEISPIEL 1 Analog-digital-Umsetzer. | out |
| 351-56-36 | analog-to-digital converter | out |
| 351-56-37 | digital-to-analog converter | out |
| 351-56-38 | serial-to-parallel converter | out |
| 351-56-39 | parallel-to-serial converter | out |

## 351-57 Safety aspects in control technology

7 entries, 1 taken up.

| Code | Term | In the pattern |
|---|---|---|
| 351-57-01 | hazard | out |
| 351-57-02 | harm | out |
| 351-57-03 | risk | out |
| 351-57-04 | tolerable risk | out |
| 351-57-05 | safety | out |
| 351-57-06 | functional safety | **FunctionalSafety** |
| 351-57-07 | security | out |

---

**92 of 409 entries** are taken up by the pattern.

Terms the standard does **not** define, which a model of an
automated plant nevertheless needs, so that another source has to
supply them:

| Missing | Where to look |
|---|---|
| availability, reliability | IEC 60050-192, Dependability |
| accuracy, resolution, uncertainty | IEC 60050-300, or the VIM |
| safety integrity level | IEC 61508 |
| cycle time, scan time | not defined; `sampling period` (351-47-16) is the normative equivalent |
| sensor | not defined; the standard says `sensing element` (351-56-26) |
| programmable logic controller | not defined as a device; 351-47-22 covers it as a *kind of control* |
| field device, fieldbus | not defined; `process peripherals` (351-54-11) is the nearest category |
| data quality, training data, explainability | outside the scope of control technology; ISO/IEC 22989 |

