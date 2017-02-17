# -*- coding: utf-8 -*-
import unittest

from array_problems import find_pair_with_sum
from array_problems import first_missing_positive
from array_problems import quick_sort


class FindPairWithSumTest(unittest.TestCase):

    def test_find_pair(self):
        pair = find_pair_with_sum([4,3,2], 6)
        assert pair == set([4, 2])

    def test_cannot_find_pair(self):
        pair = find_pair_with_sum([4,3,2], 9)
        assert pair is None

    def test_half_edge_case(self):
        pair = find_pair_with_sum([4,3,2], 8)
        assert pair is None

        pair = find_pair_with_sum([4,3,2,4], 8)
        assert pair == set([4, 4])

    def test_sum_is_in_array(self):
        pair = find_pair_with_sum([4,3,2], 3)
        assert pair is None


class QuickSortTest(unittest.TestCase):

    def test_base_case(self):
        values = [5, 8, 9, 137, -5, 32, 0]
        quick_sort(values)
        assert values == [-5, 0, 5, 8, 9, 32, 137]

    def test_empty(self):
        values = []
        quick_sort(values)
        assert values == []

    def test_one_element(self):
        values = [2387]
        quick_sort(values)
        assert values == [2387]


class FirstMissingPositiveTest(unittest.TestCase):

    def test_one(self):
        nums = [0, -1, -2]
        self.assertEqual(first_missing_positive(nums), 1)

    def test_base_case(self):
        nums = [1, 2, 0]
        self.assertEqual(first_missing_positive(nums), 3)

    def test_inner_number(self):
        nums = [3, 4, -1, 1]
        self.assertEqual(first_missing_positive(nums), 2)

    def test_many_gaps(self):
        nums = [1, 7, 9, 13, 15, 2, 3, 5, 6]
        self.assertEqual(first_missing_positive(nums), 4)

    def test_fill_many_gaps(self):
        nums = [2, 4, 6, 9, 11, 10, 8, 7, 5, 3]
        self.assertEqual(first_missing_positive(nums), 1)


if __name__ == '__main__':
    unittest.main()
