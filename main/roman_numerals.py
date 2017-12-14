
def roman_numerals(number):
    if number <= 3:
        return 'I'*number
    elif number == 4:
        return 'IV'
    elif number == 5:
        return 'V'
    return 'V' + 'I'*(number-5)
