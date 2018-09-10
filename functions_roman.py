

CONVERSION_TABLE = {
    'I': 1,
    'II': 2,
    'III': 3,
    'IV': 4,
    'V': 5,
    'VI': 6,
    'VII': 7,
    'VIII': 8,
    'IX': 9,
    'X': 10,
    'XX': 20,
    'XXX': 30,
    'XL': 40,
    'L': 50,
    'LX': 60,
    'LXX': 70,
    'LXXX': 80,
    'XC': 90,
    'C': 100,
    'D': 500,
    'M': 1000,
}


def roman_to_arabic(roman_number):
    '''
    >>> roman_to_arabic('X')
    10

    '''
    arabic_number = 0
    for i in range(1, len(roman_number) - 1):
        prev = roman_number[i - 1]
        next = roman_number[i]
        if prev >= next:
            arabic_number += CONVERSION_TABLE[prev]
        elif prev < next:
            arabic_number -= CONVERSION_TABLE[prev]
    arabic_number += CONVERSION_TABLE[roman_number[-1]]
    return arabic_number


while True:
    roman_number = input('Roman number: ')
    if not roman_number:
        break
    else:
        arabic_number = roman_to_arabic(roman_number)
        print(arabic_number)