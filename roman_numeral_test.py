import pytest
from roman_numeral import convert


@pytest.mark.parametrize('number, numeral', [
    (1, 'I'),
    (2, 'II'),
    (3, 'III'),
    (4, 'IV'),
    (5, 'V'),
    (6, 'VI'),
    (7, 'VII'),
    (8, 'VIII'),
    (9, 'IX'),
    (10, 'X'),
    (14, 'XIV'),
    (21, 'XXI'),
    (89, 'LXXXIX'),
    (91, 'XCI'),
    (984, 'CMLXXXIV'),
    (1000, 'M'),
    (1889, 'MDCCCLXXXIX'),
    (1989, 'MCMLXXXIX'),
    (3999, 'MMMCMXCIX'),
    (45, 'XLV'),
    (3518, 'MMMDXVIII'),
])
def test_convert(number, numeral):
    assert convert(number) == numeral
