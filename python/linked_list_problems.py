# -*- coding: utf-8 -*-

# From leetcode.com
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1, l2):

    def _get_val_from_digit(list_node):
        if list_node:
            return list_node.val
        return 0

    def _add(l1, l2, is_carry_over):
        if l1 is None and l2 is None:
            if is_carry_over:
                return ListNode(1)
            return None

        digit_sum = _get_val_from_digit(l1) + \
                _get_val_from_digit(l2) + \
                (1 if is_carry_over else 0)
        next_has_carry_over = digit_sum >= 10
        l = ListNode(digit_sum - 10 if next_has_carry_over else digit_sum)
        l.next = _add(
            l1.next if l1 else None,
            l2.next if l2 else None,
            next_has_carry_over)
        return l

    return _add(l1, l2, False)


def reverse_linked_list(head):
    """Reverse a linked list in place."""
    new_head = None
    new_tail = None
    cursor = head
    while cursor:
        original_next = cursor.next
        if not new_head:
            new_head = cursor
            new_tail = cursor
        else:
            cursor.next = new_head
            new_head = cursor
            new_tail.next = original_next
        cursor = original_next
