# -*- coding: utf-8 -*-


import unittest


from math_problems import count_staircase_climb
from math_problems import is_power_of_three


class IsPowerOfThreeTest(unittest.TestCase):

    def test_zero(self):
        self.assertFalse(is_power_of_three(0))

    def test_one(self):
        self.assertTrue(is_power_of_three(1))

    def test_three(self):
        self.assertTrue(is_power_of_three(3))

    def test_basic(self):
        self.assertTrue(is_power_of_three(9))
        self.assertTrue(is_power_of_three(27))
        self.assertTrue(is_power_of_three(81))
        self.assertTrue(is_power_of_three(243))

    def test_multiples_but_not_powers(self):
        self.assertFalse(is_power_of_three(12))
        self.assertFalse(is_power_of_three(18))
        self.assertFalse(is_power_of_three(99))
        self.assertFalse(is_power_of_three(120))


class CountStaircaseClimbTest(unittest.TestCase):

    def test_base_case(self):
        self.assertEqual(count_staircase_climb(0), 0)
        self.assertEqual(count_staircase_climb(1), 1)
        self.assertEqual(count_staircase_climb(2), 2)
        self.assertEqual(count_staircase_climb(3), 4)

    def test_four_five_six(self):
        self.assertEqual(count_staircase_climb(4), 7)
        self.assertEqual(count_staircase_climb(5), 13)
        self.assertEqual(count_staircase_climb(6), 24)


if __name__ == '__main__':
    unittest.main()
