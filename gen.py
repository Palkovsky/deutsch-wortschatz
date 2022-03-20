#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import csv
import genanki
import random
import sys

def main():
    if len(sys.argv) != 3:
        panic('Benutzung: gen.py <Csvdatei> <Ausgabedatei>')

    model = genanki.Model(
        2097819111, 'Model',
        fields=[
            {'name': 'Frage'},
            {'name': 'Antwort'},
            {'name': 'Beispiel'},
            {'name': 'Beschreibung'}
        ],
        templates=[
        {
            'name': 'Card',
            'qfmt': '<center><h1>{{Frage}}</h1></center>',
            'afmt': '<center>{{FrontSide}}<hr id="answer"><h1>{{Antwort}}</h1><h3>{{Beispiel}}<br><i>{{Beschreibung}}</i></h3></center>',
        },
    ])
    deck = genanki.Deck(1250160807, 'Deutsch Wortschatz')

    try:
        f = open(sys.argv[1], 'r', encoding = 'utf-8')
    except IOError:
        panic('Fehler: Datei konnte nicht geöffnet werden')

    rows = []
    for row in csv.reader(f):
        if len(row) != 4:
            panic("CSV ist invalide")
        rows.append(row)

    random.shuffle(rows)

    for row in rows:
        note = genanki.Note(model=model, fields=row)
        deck.add_note(note)

    genanki.Package(deck).write_to_file(sys.argv[2])

    return 0

def panic(msg, retcode = 1):
    print(msg)
    sys.exit(retcode)

if __name__ == "__main__":
    sys.exit(main())