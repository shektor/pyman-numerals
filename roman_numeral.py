
def convert(number):
    numerals = {
        1: 'I',
        5: 'V',
        10: 'X',
    }
    units = [10, 5, 1]

    numeral = ''
    while number > 0:
        if number in numerals:
            numeral += numerals[number]
            number -= number
        else:
            for index, unit in enumerate(units):
                if unit % 10 == 0:
                    minor_unit = units[index + 2]
                    abbreviated_unit = unit - minor_unit

                    if number == abbreviated_unit:
                        numeral += numerals[minor_unit] + numerals[unit]
                        number -= abbreviated_unit
                        break
                if number > unit:
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
