
def convert(number):
    numerals = {
        1: 'I',
        5: 'V',
    }
    units = [5, 1]

    numeral = ''
    while number > 0:
        for unit in units:
            if number >= unit:
                numeral += numerals[unit]
                number -= unit
                break

    return numeral
