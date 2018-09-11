import csv
from pprint import pprint

FILENAME = r'csv-iris.csv'
with open(FILENAME, encoding='utf-8') as file:
    fieldnames = [
        'sepal_length',
        'sepal_width',
        'petal_length',
        'petal_width',
        'species'
    ]
    data = csv.DictReader(
        file,
        fieldnames=fieldnames,
        delimiter=',',
        quotechar='"')

    species_dict = {
        '0': 'setosa',
        '1': 'versicolor',
        '2': 'virginica',
    }

    for i, row in enumerate(data):
        if i == 0:
            continue
        print(
            row['sepal_length'],
            row['sepal_width'],
            row['petal_length'],
            row['petal_width'],
            species_dict[row['species']]
        )
