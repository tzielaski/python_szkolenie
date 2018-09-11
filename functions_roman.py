CONVERSION_TABLE = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


def roman_to_arabic(roman_number):
    '''
    >>> roman_to_arabic('X')
    10

    >>> roman_to_arabic('XIV')
    14

    >>> roman_to_arabic('LXXXIV')
    84
    '''
    arabic_number = 0
    if len(roman_number) > 1:
        for i in range(1, len(roman_number)):
            prev = CONVERSION_TABLE[roman_number[i - 1]]
            next = CONVERSION_TABLE[roman_number[i]]
            if prev >= next:
                arabic_number += prev
            elif prev < next:
                arabic_number -= prev
    arabic_number += CONVERSION_TABLE[roman_number[-1]]
    return arabic_number


while True:
    roman_number = input('Roman number: ')
    if not roman_number:
        break
    else:
        arabic_number = roman_to_arabic(roman_number)
        print(arabic_number)
