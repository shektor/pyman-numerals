
def convert(number):
    numerals = {
        1: 'I',
        5: 'V',
    }
    units = [5, 1]

    numeral = ''
    while number > 0:
        for index, unit in enumerate(units):
            if number >= unit:
                if index != 0:
                    previous_unit = units[index - 1]
                    abbreviated_unit = previous_unit - unit

                    if number == abbreviated_unit:
                        numeral += numerals[unit] + numerals[previous_unit]
                        number -= abbreviated_unit
                        break

                numeral += numerals[unit]
                number -= unit
                break

    return numeral
