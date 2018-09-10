DATABASE = [
    {'last_name': 'Jiménez'},
    {'first_name': 'Max', 'last_name': 'Peck'},
    {'first_name': 'Иван', 'age': 42},
    {'first_name': 'Max', 'last_name': 'Peck', 'born': 1961},
    {'first_name': 'José', 'born': 1961, 'agency': 'NASA'},
]

key_set = set()
for dict in DATABASE:
    for key in dict.keys():
        key_set.add(key)


print(key_set)