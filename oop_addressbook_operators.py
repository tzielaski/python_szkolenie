from dataclasses import dataclass

@dataclass()
class Contact:
    name: str
    addresses: list = None

    def __str__(self):
        return f'{self.__dict__}'

    def __iadd__(self, other):
        if isinstance(other, Address):
            self.addresses.append(other)
        return self

    def __contains__(self, item):
        if isinstance(item, Address):
            return item in self.addresses


@dataclass
class Address:
    location: str

    def __repr__(self):
        return f'{self.__dict__}'


contact = Contact(name='José', addresses=[Address(location='JPL')])
contact += Address(location='Houston')
contact += Address(location='KSC')

print(contact)
# {'name': 'José', 'addresses': [{'city': 'JPL'}, {'city': 'Houston'}, {'city': 'KSC'}]}

if Address(location='Bajkonur') in contact:
    print(True)
else:
    print(False)
# False
