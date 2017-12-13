import unittest
from main.romannumerals import roman_numerals


class RomanNumeralsShould(unittest.TestCase):

    def test_return_one(self):
        assert roman_numerals(1) == 'I'

    def test_return_II_for_two(self):
        assert roman_numerals(2) == 'II'

    def test_return_III_for_three(self):
        assert roman_numerals(3) == 'III'

    def test_return_V_for_five(self):
        assert roman_numerals(5) == 'V'