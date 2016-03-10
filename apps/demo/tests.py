# Third party imports
from django.test import TestCase

# Local imports
from .roman import RomanNumeral


class RomanNumeralTestCase(TestCase):
    def setUp(self):
        self.TEST_CASES = [
            ('', 0),
            ('VI', 6),
            ('IX', 9),
            ('XVIII', 18),
            ('XIX', 19),
            ('XXXVIII', 38),
            ('XXXIX', 39),
            ('XL', 40),
            ('XCVIII', 98),
            ('CCCLXXXVIII', 388),
            ('CDXCIX', 499),
            ('DCCCLXVII', 867),
            ('MCMXCVIII', 1998),
            ('MMMCMXCIX', 3999),
        ]

    def test_int_to_rom(self):
        """Testing the conversion from int to roman numerals"""
        for c, n in self.TEST_CASES:
            self.assertEqual(RomanNumeral(n).rom, c)

    def test_rom_to_int(self):
        """Testing the conversion from int to roman numerals"""
        for c, n in self.TEST_CASES:
            self.assertEqual(RomanNumeral(c).int, n)
