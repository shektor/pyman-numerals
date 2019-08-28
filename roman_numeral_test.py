from roman_numeral import convert


def test_convert():
    number = 1
    numeral = 'I'

    assert convert(number) == numeral
