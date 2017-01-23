# -*- coding: utf-8 -*-

# From leetcode.com
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1, l2):

    def _copy(list_node, is_carry_over):
        if not list_node:
            if is_carry_over:
                return ListNode(1)
            return None
        digit_sum = list_node.val + (1 if is_carry_over else 0)
        next_has_carry_over = digit_sum >= 10
        l = ListNode(digit_sum - 10 if next_has_carry_over else digit_sum)
        l.next = _copy(list_node.next, next_has_carry_over)
        return l

    def _add(l1, l2, is_carry_over):
        if l1 is None and l2 is None:
            if is_carry_over:
                return ListNode(1)
            return None
        if l1 is None:
            return _copy(l2, is_carry_over)
        if l2 is None:
            return _copy(l1, is_carry_over)
        digit_sum = l1.val + l2.val + (1 if is_carry_over else 0)
        next_has_carry_over = digit_sum >= 10
        l = ListNode(digit_sum - 10 if next_has_carry_over else digit_sum)
        l.next = _add(l1.next, l2.next, next_has_carry_over)
        return l

    return _add(l1, l2, False)
