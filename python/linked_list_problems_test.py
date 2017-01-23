# -*- coding: utf-8 -*-


import unittest

from linked_list_problems import ListNode
from linked_list_problems import add_two_numbers


class AddTwoNumbersTest(unittest.TestCase):

    def test_base_case(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)
        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)

        result = add_two_numbers(l1, l2)
        assert result.val == 7
        assert result.next.val == 0
        assert result.next.next.val == 8

    def test_different_digits(self):
        l1 = ListNode(7)
        l1.next = ListNode(3)
        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(2)

        result = add_two_numbers(l1, l2)
        assert result.val == 2
        assert result.next.val == 0
        assert result.next.next.val == 3

    def test_different_digits_reverse(self):
        l1 = ListNode(7)
        l1.next = ListNode(3)
        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(2)

        result = add_two_numbers(l2, l1)
        assert result.val == 2
        assert result.next.val == 0
        assert result.next.next.val == 3

    def test_different_digits(self):
        l1 = ListNode(8)
        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(2)
        l2.next.next.next = ListNode(1)

        result = add_two_numbers(l1, l2)
        assert result.val == 3
        assert result.next.val == 7
        assert result.next.next.val == 2
        assert result.next.next.next.val == 1

    def test_two_fives(self):
        l1 = ListNode(5)
        l2 = ListNode(5)

        result = add_two_numbers(l1, l2)
        assert result.val == 0
        assert result.next.val == 1

    def test_one_plus_ninety_nine(self):
        l1 = ListNode(1)
        l2 = ListNode(9)
        l2.next = ListNode(9)

        result = add_two_numbers(l1, l2)
        assert result.val == 0
        assert result.next.val == 0
        assert result.next.next.val == 1


if __name__ == '__main__':
    unittest.main()
