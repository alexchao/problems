# -*- coding: utf-8 -*-


import unittest


from math_problems import is_power_of_three


class IsPowerOfThreeTest(unittest.TestCase):

    def test_zero(self):
        assert is_power_of_three(0) == False

    def test_one(self):
        assert is_power_of_three(1) == True

    def test_three(self):
        assert is_power_of_three(3) == True

    def test_basic(self):
        assert is_power_of_three(9) == True
        assert is_power_of_three(27) == True
        assert is_power_of_three(81) == True
        assert is_power_of_three(243) == True

    def test_multiples_but_not_powers(self):
        assert is_power_of_three(12) == False
        assert is_power_of_three(18) == False
        assert is_power_of_three(99) == False
        assert is_power_of_three(120) == False


if __name__ == '__main__':
    unittest.main()
