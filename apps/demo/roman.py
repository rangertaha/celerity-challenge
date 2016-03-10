"""

"""
rom_table = (
    (0, ''), (1, 'I'), (4, 'IV'), (5, 'V'), (9, 'IX'), (10, 'X'), (40, 'XL'),
    (50, 'L'), (90, 'XC'), (100, 'C'), (400, 'CD'), (500, 'D'), (900, 'CM'),
    (1000, 'M')
)


class RomanNumeral(object):
    """

    """
    def __init__(self, x):
        if isinstance(x, int):
            self.x = x
        if isinstance(x, str):
            self.x = self.__rom_to_int(x)

    @property
    def int(self):
        """Returns the integer"""
        return self.x

    @property
    def rom(self):
        """Returns the roman numeral"""
        return self.__int_to_rom(self.x)

    def __highest_value(self, s):
        """Returns the highest value object.

        The common recurring pattern in bother functions is to identify the
        highest number or character value.

        """
        for value, chars in sorted(rom_table, reverse=True):
            if isinstance(s, str) and s.startswith(chars):
                return chars, value
            elif isinstance(s, int) and (s - value) >= 0:
                return chars, value

    def __int_to_rom(self, n, c=''):
        """Converting from integer to roman numerals"""
        chars, value = self.__highest_value(n)
        c += chars
        if (n - value) > 0:
            return self.__int_to_rom((n - value), c)
        else:
            return c

    def __rom_to_int(self, s, i=0):
        """Converting from roman numerals to integer """
        chars, value = self.__highest_value(s)
        i += value
        s = s[len(chars):]
        if len(s) > 0:
            return self.__rom_to_int(s, i)
        else:
            return i

    def __add__(self, other):
        return self.x + other

    def __repr__(self):
        return self.__int_to_rom(self.x)

    def is_valid(self):
        """
        Checking for roman numbers from the lookup table that are not in
        order highest to lowest
        """
        pass
