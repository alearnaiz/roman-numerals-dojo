import unittest
from main.romannumerals import roman_numerals


class RomanNumeralsShould(unittest.TestCase):

    def test_return_one(self):
        assert roman_numerals(1) == 'I'