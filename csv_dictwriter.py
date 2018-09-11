import csv

DATA = [
    {'first_name': 'José'},
    {'last_name': 'Jiménez'},
    {'first_name': 'Иван', 'last_name': 'Иванович'},
    {'first_name': 'Max', 'last_name': 'Peck', 'born': 1961},
    {'first_name': 'José', 'born': 1961, 'first_step': 1969},
]

fieldnames = set()

for row in DATA:
    fieldnames.update(row.keys())

with open(file='data.csv', mode='w', encoding='utf-8') as file:
    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_NONE,
        lineterminator='\n')

    writer.writeheader()

    for row in DATA:
        writer.writerow(row)
