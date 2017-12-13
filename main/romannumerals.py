
def roman_numerals(number):
    if number <= 3:
        return 'I'*number
    elif number == 4:
        return 'IV'
    return 'V'
