import math


def convert(number):
    numerals = {
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M',
    }
    units = [1000, 500, 100, 50, 10, 5, 1]

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

                    round_one_sig = number
                    if number > 10:
                        tens = 1
                        while round_one_sig > 10:
                            round_one_sig = math.floor(round_one_sig / 10)
                            tens = tens * 10
                        round_one_sig = round_one_sig * tens

                    if round_one_sig == abbreviated_unit:
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
