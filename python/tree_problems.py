# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def find_lowest_common_ancestor(root, p, q):
    """Does not assume ordering."""

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

    path_p = _get_path(root, p)
    if not path_p:
        return None

    searched = set([sn.val for sn in path_p])

    # search entire subtree below p for q
    p_node = path_p.pop()
    if _get_path(p_node, q):
        return p_node

    # walk up path to p and search unsearched branches for q
    while path_p:
        ancestor = path_p.pop()
        if ancestor.val == q.val:
            return ancestor
        search_node = None
        if ancestor.left and ancestor.left.val not in searched:
            search_node = ancestor.left
        elif ancestor.right and ancestor.right.val not in searched:
            search_node = ancestor.right
        if search_node:
            if _get_path(search_node, q):
                return ancestor

    return None
