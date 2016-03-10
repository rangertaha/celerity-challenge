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
            self.x = self._rom_to_int(x)

    @property
    def int(self):
        """Returns the integer"""
        return self.x

    @property
    def rom(self):
        """Returns the roman numeral"""
        return self._int_to_rom(self.x)

    def _highest_value(self, s):
        for value, chars in sorted(rom_table, reverse=True):
            if isinstance(s, str) and s.startswith(chars):
                return chars, value
            elif isinstance(s, int) and (s - value) >= 0:
                return chars, value

    def _int_to_rom(self, n, c=''):
        chars, value = self._highest_value(n)
        c += chars
        if (n - value) > 0:
            return self._int_to_rom((n - value), c)
        else:
            return c

    def _rom_to_int(self, s, i=0):
        chars, value = self._highest_value(s)
        i += value
        s = s[len(chars):]
        if len(s) > 0:
            return self._rom_to_int(s, i)
        else:
            return i

    def __add__(self, other):
        return self.x + other

    def __repr__(self):
        return self._int_to_rom(self.x)

    def is_valid(self):
        """
        Checking for roman numbers from the lookup table that are not in
        order highest to lowest
        """
        pass
