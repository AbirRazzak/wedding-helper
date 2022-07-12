import csv
from typing import Dict, List

'''
This script is used to read in data/seating.csv to print out names that we want to use to for a physical foam
board seating chart. It capitalizes everyone's names and prints the table number they are at.
'''

if __name__ == '__main__':
    tables: Dict[str, List[str]] = {}

    with open('../data/seating.csv') as csvfile:
        for line in csv.DictReader(csvfile):
            table_number = line['Table']
            name = f"{line['First Name']} {line['Last Name']}".upper()

            if tables.get(table_number) is None:
                tables[table_number] = []

            tables[table_number].append(name)

    for k, v in tables.items():
        print(f'TABLE {k}')
        for person in v:
            print(person)

        print('\n\n')
