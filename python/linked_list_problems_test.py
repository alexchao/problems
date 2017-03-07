# -*- coding: utf-8 -*-


import unittest

from linked_list_problems import ListNode
from linked_list_problems import add_two_numbers
from linked_list_problems import delete
from linked_list_problems import find_intersection
from linked_list_problems import find_kth_to_last
from linked_list_problems import reverse_linked_list


def make_list(values):
    head = None
    cursor = None
    for v in values:
        if not head:
            head = ListNode(v)
            cursor = head
        else:
            cursor.next = ListNode(v)
            cursor = cursor.next

    return head


class LinkedListTestCase(unittest.TestCase):

    def assert_list(self, head, expected_values):
        cursor = head
        list_values = []
        while cursor:
            list_values.append(cursor.val)
            cursor = cursor.next
        self.assertEqual(list_values, expected_values)


class MakeListTestCase(LinkedListTestCase):

    def test_empty(self):
        self.assertEqual(make_list([]), None)

    def test_base_case(self):
        self.assert_list(make_list([1, 2, 3]), [1, 2, 3])


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


class ReverseLinkedListTest(LinkedListTestCase):

    def test_one(self):
        ll = ListNode(10)
        reverse_linked_list(ll)
        self.assert_list(ll, [10])

    def test_two(self):
        l1 = ListNode(1)
        l2 = ListNode(2)
        l1.next = l2
        reverse_linked_list(l1)
        self.assert_list(l2, [2, 1])

    def test_many(self):
        l1 = ListNode(1)
        l2 = ListNode(2)
        l3 = ListNode(3)
        l4 = ListNode(4)
        l5 = ListNode(5)

        l1.next = l2
        l2.next = l3
        l3.next = l4
        l4.next = l5

        self.assert_list(l1, [1, 2, 3, 4, 5])
        self.assert_list(l5, [5])

        reverse_linked_list(l1)

        self.assert_list(l5, [5, 4, 3, 2, 1])
        self.assert_list(l4, [4, 3, 2, 1])
        self.assert_list(l3, [3, 2, 1])
        self.assert_list(l2, [2, 1])
        self.assert_list(l1, [1])


class FindKthToLastTestCase(LinkedListTestCase):

    def setUp(self):
        self.ll = make_list([10, 20, 30, 40, 50, 60, 70])

    def test_base_case(self):
        self.assertEqual(find_kth_to_last(self.ll, 2).val, 60)
        self.assertEqual(find_kth_to_last(self.ll, 6).val, 20)

    def test_1st_last_value(self):
        self.assertEqual(find_kth_to_last(self.ll, 1).val, 70)

    def test_no_value(self):
        self.assertEqual(find_kth_to_last(self.ll, 10), None)


class DeleteTestCase(LinkedListTestCase):

    def setUp(self):
        self.ll = make_list([10, 20, 30, 40, 50])

    def test_value_does_not_exist(self):
        self.assert_list(delete(self.ll, 60), [10, 20, 30, 40, 50])

    def test_delete_head(self):
        self.assert_list(delete(self.ll, 10), [20, 30, 40, 50])

    def test_delete_inner(self):
        self.assert_list(delete(self.ll, 20), [10, 30, 40, 50])

    def test_delete_last(self):
        self.assert_list(delete(self.ll, 50), [10, 20, 30, 40])


class FindIntersectionTestCase(LinkedListTestCase):

    def test_no_intersection(self):
        l1 = make_list([10, 20, 30])
        l2 = make_list([10, 20, 30, 40])
        self.assertEqual(find_intersection(l1, l2), None)

    def test_middle_intersection(self):
        l1 = ListNode(1)
        l2 = ListNode(2)
        l3 = ListNode(3)
        l4 = ListNode(4)
        l5 = ListNode(5)
        l6 = ListNode(6)
        l7 = ListNode(7)

        l1.next = l2
        l2.next = l3
        l3.next = l4
        l4.next = l5

        l6.next = l7
        l7.next = l4
        self.assertEqual(find_intersection(l1, l6), l4)

    def test_subset(self):
        l1 = ListNode(1)
        l2 = ListNode(2)
        l3 = ListNode(3)
        l4 = ListNode(4)
        l5 = ListNode(5)

        l1.next = l2
        l2.next = l3
        l3.next = l4
        l4.next = l5

        self.assertEqual(find_intersection(l1, l3), l3)



if __name__ == '__main__':
    unittest.main()
