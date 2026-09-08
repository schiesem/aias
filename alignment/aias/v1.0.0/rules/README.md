# Regeln der Modellierungsassistenz

Die Regeln, die das Implementierungskapitel der Dissertation als Listings
zeigt, hier als lauffähige Dateien. `run_rules.py` prüft sie gegen die drei
Testfälle des Alignments.

| Datei | Art | Listing |
|---|---|---|
| `shacl_validate.ttl` | Konsistenzregel | SHACL-Konsistenzregel |
| `shacl_common_note.ttl` | Hinweisregel | SHACL-Hinweisregel |
| `swrl_design.txt` | Erweiterungsregel | SWRL-Erweiterungsregel |

## Was die Prüfung zeigt

| | tc1 | tc2 | tc3 |
|---|---|---|---|
| Konsistenzregel | konform | 3 Funktionen ohne Ressource | konform |
| Hinweisregel | Speicherung auf ProCube | Speicherung auf ProCube | Datenspeicherung auf ProCube |
| SWRL Edge | greift nicht | greift nicht | Modelausfuehrung auf RaspberryPI5 |
| SWRL Cloud | Inferenz1 auf ProCube | Modellinferenz auf ProCube | greift nicht |

Die drei Verletzungen in tc2 sind die manuellen Schritte des Fallbeispiels,
Einlegen, Entnehmen und Umschäumen. Sie tragen keine Ressource, weil ein
Mensch sie ausführt. Dieselben drei findet `cq08`.

## Die Kette der Zuweisung

Die Regeln folgen dem Weg, den das Modell vorgibt:

```
Function  ──AIAS:isAssignedTo──>  Assignment  ──VDI3682:isAssignedTo──>  Resource
```

Der erste Schritt gehört dem Alignment, weil VDI 3682 nur vom
`ProcessOperator` ausgeht und keine Funktion eines anderen Teilbereichs
erreicht. Der zweite gehört VDI 3682. Die Konsistenzregel lässt über `sh:or`
beide Wege gelten, sonst meldete sie jeden Prozessoperator als Verletzung.

## SWRL

`swrl_design.txt` ist kein ausführbares Format für pyshacl. Die Regel wird
über die äquivalente SPARQL-Abfrage geprüft: findet sie die Konstellation, die
die Regel als Prämisse beschreibt?

## Was nicht geschrieben wurde

**E1 bis E14, die Erweiterungsregeln.** E1 bis E12 erzeugen inverse
Relationen. Zwei davon, `isInput` und `isOutput`, führt das Muster bereits als
`owl:inverseOf`, der Reasoner leitet sie ohne Regel ab. Die übrigen
Gegenrelationen gibt es nicht und sie wurden bewusst nicht eingeführt: SPARQL
liest ein Tripelmuster von beiden Enden, und SHACL hat `sh:inversePath`.

E13 und E14 klassifizieren das `SystemDesign` nach der Ressource, auf der die
Inferenz läuft. Beide sehen jeweils nur eine Prämisse. In tc3 läuft die
Inferenz auf einem Edge-Gerät, das Design ist dort aber `Hybrid`, und `Cloud`,
`Edge` und `Hybrid` sind disjunkt: HermiT erklärt das Modell für inkonsistent.
Eine Fassung, die alle drei Fälle trifft, bräuchte die Negation, die SWRL
nicht hat.

**K6.** Sie verlangt, dass jede Ressource eine Funktion trägt. Ein Gateway,
das nur weiterleitet, wie der Raspberry Pi in tc2, trägt keine und ist
trotzdem eine sinnvolle Architektur.

**V8 und V9.** Sie fragen, ob die Ausgabe einer Inferenz die Eingabe einer
Automatisierung ist und umgekehrt. `Automate` hat im Muster keine einzige
Relation, weder für Eingang noch für Ausgang. Die Verbindung ist nicht
modellierbar.
