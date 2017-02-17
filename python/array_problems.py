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


def quick_sort(x):

    def _swap(values, i, j):
        tmp = values[i]
        values[i] = values[j]
        values[j] = tmp

    def _partition(values, lo, hi):
        pivot_value = values[hi]
        pivot_index = lo
        for i in range(lo, hi):
            if values[i] <= pivot_value:
                _swap(values, i, pivot_index)
                pivot_index += 1
        _swap(values, pivot_index, hi)
        return pivot_index

    def _quick_sort(values, lo, hi):
        if lo < hi:
            pivot_index = _partition(values, lo, hi)
            _quick_sort(values, lo, pivot_index - 1)
            _quick_sort(values, pivot_index + 1, hi)

    _quick_sort(x, 0, len(x) - 1)


def first_missing_positive(nums):
    gaps = [(1, float('inf'))]

    for n in nums:
        if n < 1:
            continue
        for i, g in enumerate(gaps):
            # TODO: optimize this search
            if g[0] <= n and n <= g[1]:
                gaps.pop(i)
                if g[0] == g[1]:
                    # closes a gap
                    pass
                elif n == g[0]:
                    gaps.insert(i, (g[0] + 1, g[1]))
                elif n == g[1]:
                    gaps.insert(i, (g[0], g[1] - 1))
                else:
                    # split
                    gaps.insert(i, (n + 1, g[1]))
                    gaps.insert(i, (g[0], n - 1))
                break

    return gaps[0][0]
