import json
from pprint import pprint
from dataclasses import dataclass
from typing import List

FILENAME = 'addressbook.json'

@dataclass
class Address:
    street: str = None
    city: str = None


@dataclass
class Contact:
    first_name: str
    last_name: str
    addresses: List[Address] = ()


@dataclass
class AddressBook:
    contacts: List[Contact]


ksiazka_adresowa = AddressBook(contacts=[
    Contact(first_name='José', last_name='Jiménez'),
    Contact(first_name='Иван', last_name='Иванович', addresses=[]),
    Contact(first_name='Max', last_name='Peck', addresses=[
        Address(street='2101 E NASA Pkwy', city='Houston'),
        Address(city='Kennedy Space Center'),
        Address(street='4800 Oak Grove Dr', city='Pasadena'),
        Address(street='2825 E Ave P', city='Palmdale'),
    ])
])


class JSONObjectEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return super().default(obj)
        except TypeError:
            return obj.__dict__


class JSONObjectDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_object)

    def decode_object(self, dictionary):
        if dictionary.get('contacts'):
            return AddressBook(**dictionary)
        if dictionary.get('city'):
            return Address(**dictionary)
        else:
            return Contact(**dictionary)


out = json.dumps(ksiazka_adresowa, cls=JSONObjectEncoder)

with open(FILENAME, mode='w', encoding='utf-8') as file:
    file.write(out)


with open(FILENAME, mode='r', encoding='utf-8') as file:
    dane = file.read()


out = json.loads(dane, cls=JSONObjectDecoder)
pprint(out)