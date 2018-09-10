number_str_dict = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '0': 'zero',
    '.': 'and'
}


def number_to_str(number):
    string_number = ''
    number = str(number)
    for char in number:
        string_number += (number_str_dict[char] + ' ')
    return string_number


while True:
    number = input('Number: ')
    if not number:
        break
    else:
        print(number_to_str(float(number)))
