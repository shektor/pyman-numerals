
def convert(number):
    numerals = {
        1: 'I',
        5: 'V',
    }

    if number < 5:
        if number < 4:
            return numerals[1] * number
        else:
            return numerals[1] + numerals[5]

    value_over_five = number % 5
    return numerals[5] + (numerals[1] * value_over_five)
