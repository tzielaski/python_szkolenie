import csv


class Contact:
    def __init__(self, first_name, last_name, addresses=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.addresses = addresses

    def get_addresses_as_str(self):
        addresses_str = []
        for Address in self.addresses:
            addresses_values = Address.__dict__.values()
            single_address = '|'.join(str(x) for x in addresses_values)
            addresses_str.append(single_address)
        return addresses_str.join(';')

class Address:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


addressbook = [
    Contact(first_name='Max', last_name='Peck', addresses=[
        Address(street='2101 E NASA Pkwy', city='Houston', state='Texas', code='77058', country='USA'),
        Address(street=None, city='Kennedy Space Center', code='32899', country='USA'),
        Address(street='4800 Oak Grove Dr', city='Pasadena', code='91109', country='USA'),
        Address(street='2825 E Ave P', city='Palmdale', state='California', code='93550', country='USA', data_urodzenia=None),
    ]),
    Contact(first_name='José', last_name='Jiménez'),
    Contact(first_name='Иван', last_name='Иванович', addresses=[]),
]

to_csv = []
for contact in addressbook:
    contact_data = contact.__dict__
    contact_data['addresses'] = contact.get_addresses_as_str()
    to_csv.append(contact_data)

with open('addressbook.csv','w',encoding='utf-8') as file:
    fieldnames = set()
    for record in contact_data:
        for key in record.keys():
            fieldnames.update(key)

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL,
        lineterminator='\n'
    )

    writer.writeheader()

    for record in contact_data:
        writer.writerow(record)


