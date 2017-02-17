# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def find_lowest_common_ancestor(root, p, q):

    def _get_path(n, target):
        if not n:
            return []
        if n.val == target.val:
            return [n]
        left_path = _get_path(n.left, target)
        if left_path:
            return [n] + left_path
        right_path = _get_path(n.right, target)
        if right_path:
            return [n] + right_path
        return []

    path_a = _get_path(root, p)
    path_b = _get_path(root, q)

    lca = None
    i = 0
    while i < len(path_a) and i < len(path_b):
        if path_a[i].val == path_b[i].val:
            lca = path_a[i]
        else:
            break
        i += 1
    return lca

