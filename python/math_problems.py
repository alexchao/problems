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
