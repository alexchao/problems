import unittest

from array_problems import find_pair_with_sum


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


if __name__ == '__main__':
    unittest.main()
