import csv
import genanki
import sys

def main():
    if len(sys.argv) != 3:
        print("Benutzung: gen.py <Csvdatei> <Ausgabedatei>")
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())