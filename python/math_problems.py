# -*- coding: utf-8 -*-


def is_power_of_three(n):

    def _recurse(x):
        if x == 3:
            return True
        if x == 0:
            return False
        if x % 3 != 0:
            return False
        return _recurse(x / 3)

    if n == 1:
        return True
    return _recurse(n)


def count_staircase_climb(n):
    """You can climb a set of n stairs 3 steps, 2 steps, or 1 step at a time.
    How many ways are there to climb the stairs?
    """
    memo = [None] * (n + 1)
    memo[:4] = [0, 1, 2, 4]
    return _count_staircase_climb(n, memo)

def _count_staircase_climb(n, memo):
    if n < 4:
        return memo[n]

    n_minus_3 = memo[n - 3]
    if n_minus_3 is None:
        n_minus_3 = memo[n - 3] = _count_staircase_climb(n - 3, memo)
    n_minus_2 = memo[n - 2]
    if n_minus_2 is None:
        n_minus_2 = memo[n - 2] = _count_staircase_climb(n - 2, memo)
    n_minus_1 = memo[n - 1]
    if n_minus_1 is None:
        n_minus_1 = memo[n - 1] = _count_staircase_climb(n - 1, memo)

    return n_minus_3 + n_minus_2 + n_minus_1
