# -*- coding: utf-8 -*-


def find_pair_with_sum(values, desired_sum):
    """Find pair with a given sum in the array.

    Given an unsorted array of integers, find a pair with given sum in it.
    """
    v_to_counts = {}
    for v in values:
        if v not in v_to_counts:
            v_to_counts[v] = 1
        else:
            v_to_counts[v] += 1

    for v1 in values:
        v2 = desired_sum - v1
        if v2 in v_to_counts:
            if v2 == v1 and v_to_counts[v2] < 2:
                return None
            return set([v1, v2])
    return None
