"""Jede Regel der Regelbasis gegen die Testfaelle des Alignments.

    python shared/run_rules.py
    python shared/run_rules.py --only S4
    python shared/run_rules.py --tc tc1_stanzprozess

Eine Regel je Datei. Der Dateiname traegt die Nummer des Anhangs, damit sich
Tabelle und Datei zuordnen lassen. Die Ausgabe nennt je Testfall, wie viele
Knoten die Regel beanstandet und welche.

Validiert wird mit RDFS-Inferenz. Ohne sie folgt SHACL keiner Unterklassen-
oder Aequivalenzbeziehung, und eine Regel auf AIAS:Component uebersaehe ein
VDI3682:Product, das nur ueber owl:equivalentClass eine Komponente ist. Das
Werkzeug der Arbeit prueft aus demselben Grund vor und nach dem Reasoning.
"""
import argparse
import pathlib
import sys

import pyshacl
from rdflib import Graph

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent
RULES = REPO / "alignment/aias/v1.0.0/rules"

ONT = ["alignment/aias/v1.0.0/AIAS.ttl",
       "odps/vdi3682/v1.0.0/VDI3682.ttl",
       "odps/iso7498/v1.0.0/ISO7498.ttl",
       "odps/iso22989/v1.0.0/ISO22989.ttl"]
TCS = ["tc1_stanzprozess", "tc2_eki_instandhaltung", "tc3_eki_primerauftrag"]

SHORT = {"https://w3id.org/aias/example/stanzprozess#": "ex:",
         "https://w3id.org/aias/example/eki1#": "ex:",
         "https://w3id.org/aias/example/eki2#": "ex:"}


def load(paths):
    g = Graph()
    for p in paths:
        g.parse(data=(REPO / p).read_text(encoding="utf-8").replace("\r\n", "\n"),
                format="turtle")
    return g


def short(s):
    for long, pre in SHORT.items():
        s = s.replace(long, pre)
    return s


def focus_nodes(text):
    out = []
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("Focus Node:"):
            out.append(short(line.split(":", 1)[1].strip()))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="", help="nur Regeln, deren Name das enthaelt")
    ap.add_argument("--tc", default="", help="nur dieser Testfall")
    args = ap.parse_args()

    files = sorted(p for d in ["static", "consistency", "notes", "regulations"]
                   for p in (RULES / d).glob("*.ttl"))
    files = [f for f in files if args.only.lower() in f.name.lower()]
    tcs = [t for t in TCS if args.tc.lower() in t.lower()]
    if not files:
        print("keine Regeldatei gefunden")
        return 1

    ont = load(ONT)
    data = {t: load(ONT + ["alignment/aias/v1.0.0/tests/data/%s.ttl" % t])
            for t in tcs}

    print("%-46s %s" % ("REGEL", "  ".join("%-22s" % t.split("_")[0] for t in tcs)))
    print("-" * (46 + 24 * len(tcs)))
    total = 0
    for f in files:
        sg = Graph()
        sg.parse(data=f.read_text(encoding="utf-8").replace("\r\n", "\n"),
                 format="turtle")
        cells, detail = [], []
        for t in tcs:
            conforms, _, text = pyshacl.validate(
                data[t], shacl_graph=sg, ont_graph=ont, inference="rdfs",
                advanced=True, abort_on_first=False)
            nodes = focus_nodes(text)
            if "Validation Failure" in text:
                cells.append("FEHLER")
                detail.append((t, [text.strip().splitlines()[0]]))
                continue
            cells.append("konform" if conforms else "%d Treffer" % len(nodes))
            if nodes:
                detail.append((t, nodes))
            total += len(nodes)
        print("  %-44s %s" % (f.stem[:44],
                              "  ".join("%-22s" % c for c in cells)))
        for t, nodes in detail:
            print("      %-18s %s" % (t.split("_")[0], ", ".join(sorted(set(nodes)))))
    print()
    print("  %d Regel(n), %d Treffer insgesamt" % (len(files), total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
